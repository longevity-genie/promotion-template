#!/usr/bin/env python3
"""Sync the registry CSVs and live Buffer state into one Google Spreadsheet.

Every registry CSV becomes a tab. Buffer is queried across every account whose
key is in .env, and lands in two more tabs: one for channels, one for the
queue. Anything Buffer has already sent that is missing from shares.csv is
flagged, because shares.csv is meant to be the record of what actually went
out and a gap there is the thing worth noticing.

The spreadsheet is edited IN PLACE: same file, same id, same link, every run.
Tabs are created on first run and their contents replaced on later runs.

Usage:
    uv run --no-project python scripts/sync_tracker.py [--dry-run]

Credentials:
    keys/service.json   a Google service account with edit rights on the sheet
    .env                *_BUFFER_API_KEY entries, one per Buffer account

Neither file is committed; keys/.gitignore and .gitignore keep them out.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# Resolve everything from this file so the repo works wherever it is cloned.
REPO = Path(__file__).resolve().parent.parent
REGISTRY = REPO / "registry"
SERVICE_ACCOUNT = REPO / "keys" / "service.json"
ENV_FILE = REPO / ".env"

BUFFER_ENDPOINT = "https://api.buffer.com"
SHEETS_SCOPE = "https://www.googleapis.com/auth/spreadsheets"

# The spreadsheet is identified by TRACKER_SHEET_ID in .env, which is
# gitignored, so no document id is ever committed. Falling back to a title
# search covers the case where the sheet is shared directly with the service
# account; a link-shared sheet does not appear in its Drive index at all, which
# is why the id is the primary route.
SHEET_TITLE = "enhancement.bio SMM"
SHEET_ID_VAR = "TRACKER_SHEET_ID"

# Registry CSV -> tab name. Order here is the order of tabs in the document:
# what you write, where it can go, what actually happened, then the rules.
CSV_TABS = [
    ("pillars", "pillars.csv"),
    ("derivatives", "derivatives.csv"),
    ("destinations", "destinations.csv"),
    ("shares", "shares.csv"),
    ("platform_rules", "platform_rules.csv"),
    ("cat_telegram_groups", "telegram-groups-catalogue.csv"),
    ("cat_linkedin_groups", "linkedin-groups-catalogue.csv"),
    ("cat_facebook_groups", "facebook-groups-catalogue.csv"),
]

# Google rejects a cell over 50k characters, and a full post body can approach
# that. Truncate visibly rather than failing the whole run.
CELL_LIMIT = 49_000


# --------------------------------------------------------------------------
# credentials
# --------------------------------------------------------------------------

def load_env() -> dict[str, str]:
    """Read .env into a dict. Missing file is fine; Buffer tabs go empty."""
    values: dict[str, str] = {}
    if not ENV_FILE.exists():
        return values
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        values[key.strip()] = val.strip().strip('"').strip("'")
    return values


def buffer_accounts(env: dict[str, str]) -> list[tuple[str, str]]:
    """Every *_BUFFER_API_KEY in .env, as (label, key). Order is stable."""
    found = []
    for key, val in sorted(env.items()):
        if key.endswith("_BUFFER_API_KEY") and val:
            found.append((key[: -len("_BUFFER_API_KEY")].lower(), val))
    return found


# --------------------------------------------------------------------------
# buffer
# --------------------------------------------------------------------------

def buffer_query(api_key: str, query: str, variables: dict | None = None) -> dict:
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(
        BUFFER_ENDPOINT,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            body = json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        return {"errors": [{"message": f"HTTP {exc.code}"}]}
    except Exception as exc:  # network wobble should not kill the whole sync
        return {"errors": [{"message": str(exc)}]}
    return body


ACCOUNT_Q = "{ account { id email organizations { id name } } }"

CHANNELS_Q = """
query Channels($orgId: OrganizationId!) {
  channels(input: { organizationId: $orgId }) {
    id name displayName service type isDisconnected isLocked timezone
    postingSchedule { day paused times }
  }
}
"""

POSTS_Q = """
query Posts($orgId: OrganizationId!, $status: [PostStatus!], $after: String) {
  posts(
    input: {
      organizationId: $orgId
      filter: { status: $status }
      sort: [{ field: dueAt, direction: asc }]
    }
    first: 100
    after: $after
  ) {
    edges { node {
      id text status dueAt sentAt channelId channelService
      tags { id name } externalLink
    } }
    pageInfo { hasNextPage endCursor }
  }
}
"""

ALL_STATUSES = ["draft", "needs_approval", "scheduled", "sending", "sent", "error"]


def collect_buffer(env: dict[str, str]) -> tuple[list[list], list[list], list[str]]:
    """Return (channel rows, post rows, notes) across every Buffer account."""
    notes: list[str] = []
    channel_rows: list[list] = []
    post_rows: list[list] = []

    accounts = buffer_accounts(env)
    if not accounts:
        notes.append("no *_BUFFER_API_KEY found in .env - Buffer tabs are empty")
        return channel_rows, post_rows, notes

    for label, key in accounts:
        acct = buffer_query(key, ACCOUNT_Q)
        if "errors" in acct or not acct.get("data", {}).get("account"):
            msg = acct.get("errors", [{}])[0].get("message", "unknown error")
            notes.append(f"{label}: account query failed ({msg})")
            continue

        account = acct["data"]["account"]
        email = account.get("email", "")

        for org in account.get("organizations", []):
            org_id = org["id"]

            chans = buffer_query(key, CHANNELS_Q, {"orgId": org_id})
            channels = (chans.get("data") or {}).get("channels") or []
            names: dict[str, str] = {}
            for ch in channels:
                names[ch["id"]] = ch.get("displayName") or ch.get("name") or ""
                sched = "; ".join(
                    f"{d['day']}:{','.join(d.get('times') or [])}"
                    + (" (paused)" if d.get("paused") else "")
                    for d in (ch.get("postingSchedule") or [])
                )
                channel_rows.append([
                    label, email, org.get("name", ""), ch["id"],
                    ch.get("displayName") or ch.get("name") or "",
                    ch.get("service", ""), ch.get("type", ""),
                    "yes" if ch.get("isDisconnected") else "no",
                    ch.get("timezone", ""), sched,
                ])

            after = None
            while True:
                res = buffer_query(
                    key, POSTS_Q,
                    {"orgId": org_id, "status": ALL_STATUSES, "after": after},
                )
                block = (res.get("data") or {}).get("posts")
                if not block:
                    msg = res.get("errors", [{}])[0].get("message", "unknown error")
                    notes.append(f"{label}: posts query failed ({msg})")
                    break
                for edge in block.get("edges") or []:
                    n = edge["node"]
                    post_rows.append([
                        label, email, n["id"], n.get("status", ""),
                        n.get("channelId", ""), names.get(n.get("channelId", ""), ""),
                        n.get("channelService", ""),
                        n.get("dueAt") or "", n.get("sentAt") or "",
                        ", ".join(t.get("name", "") for t in (n.get("tags") or [])),
                        n.get("externalLink") or "",
                        (n.get("text") or "").strip(),
                        "",  # in_shares_csv, filled by reconcile()
                    ])
                page = block.get("pageInfo") or {}
                if not page.get("hasNextPage"):
                    break
                after = page.get("endCursor")

    return channel_rows, post_rows, notes


def _normalise(text: str) -> str:
    """Lowercase alphanumeric run, for comparing post bodies across systems."""
    return "".join(c for c in (text or "").lower() if c.isalnum())


def reconcile(post_rows: list[list]) -> list[str]:
    """Flag Buffer posts that already went out but are absent from shares.csv.

    Three matching passes, because no single identifier survives the trip.
    LinkedIn hands Buffer a urn:li:share id but shows a urn:li:activity id on
    the permalink a human copies, and the two numbers differ for the same post
    - so id matching alone produces false alarms. The third pass compares the
    opening of the post body, which does survive.

    Anything predating the oldest row in shares.csv is called out separately:
    those are posts from before this registry existed, not a logging lapse.
    """
    notes: list[str] = []
    shares = REGISTRY / "shares.csv"
    if not shares.exists():
        notes.append("shares.csv not found - reconciliation skipped")
        return notes

    haystack = shares.read_text(encoding="utf-8")

    logged_bodies: list[str] = []
    earliest = ""
    with shares.open(newline="", encoding="utf-8") as fh:
        for rec in csv.DictReader(fh):
            body = _normalise(rec.get("text_sent", ""))[:120]
            if body:
                logged_bodies.append(body)
            sent = (rec.get("date_sent") or "").strip()
            if sent and (not earliest or sent < earliest):
                earliest = sent

    missing_recent = 0
    missing_old = 0
    for row in post_rows:
        post_id, status, external, text = row[2], row[3], row[10], row[11]
        if status != "sent":
            row[12] = "n/a (not sent yet)"
            continue

        known = post_id in haystack or (external and external in haystack)
        if not known:
            probe = _normalise(text)[:120]
            known = bool(probe) and any(
                probe.startswith(b[:80]) or b.startswith(probe[:80])
                for b in logged_bodies
            )

        if known:
            row[12] = "yes"
        else:
            day = (row[8] or "")[:10]
            if earliest and day and day < earliest:
                row[12] = "no - predates registry"
                missing_old += 1
            else:
                row[12] = "NO - not logged"
                missing_recent += 1

    if missing_recent:
        notes.append(
            f"{missing_recent} Buffer post(s) sent on or after {earliest} are "
            "missing from shares.csv - see buffer_queue, column in_shares_csv"
        )
    if missing_old:
        notes.append(
            f"{missing_old} older Buffer post(s) predate the first shares.csv "
            f"row ({earliest}); backfill only if you want the full history"
        )
    return notes


# --------------------------------------------------------------------------
# sheets
# --------------------------------------------------------------------------

def read_csv_rows(path: Path) -> list[list[str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        return [r for r in csv.reader(fh) if any(c.strip() for c in r)]


def flatten(text: str) -> str:
    """Collapse line breaks into a pilcrow marker.

    A newline inside a cell makes Sheets grow the row to fit, and a post body
    with a dozen paragraph breaks turns one row into a screenful - which is
    what makes a 73-row tab unreadable. Flattening keeps every row one line
    while still showing where the breaks were. The unflattened original stays
    in the source CSV and in Buffer.
    """
    parts = [p.strip() for p in text.replace("\r\n", "\n").split("\n")]
    return " ¶ ".join(p for p in parts if p)


def clip(rows: list[list]) -> list[list[str]]:
    """Stringify, flatten and truncate so no cell exceeds the Google limit."""
    out = []
    for row in rows:
        new = []
        for cell in row:
            text = "" if cell is None else str(cell)
            if "\n" in text or "\r" in text:
                text = flatten(text)
            if len(text) > CELL_LIMIT:
                text = text[:CELL_LIMIT] + " [TRUNCATED - see repo CSV]"
            new.append(text)
        out.append(new)
    return out


def open_spreadsheet(creds, env: dict[str, str]) -> str:
    """Resolve the spreadsheet id. Never hardcode one into a committed file."""
    from googleapiclient.discovery import build

    sheet_id = env.get(SHEET_ID_VAR) or os.environ.get(SHEET_ID_VAR)
    if sheet_id:
        return sheet_id.strip()

    # Only reachable when the sheet is shared directly with the service
    # account rather than by link.
    drive = build("drive", "v3", credentials=creds, cache_discovery=False)
    q = (
        "mimeType='application/vnd.google-apps.spreadsheet' "
        f"and name='{SHEET_TITLE}' and trashed=false"
    )
    found = drive.files().list(
        q=q, fields="files(id,name,modifiedTime)",
        orderBy="modifiedTime desc",
    ).execute().get("files", [])
    if not found:
        raise SystemExit(
            f"Cannot locate the tracker sheet. Add {SHEET_ID_VAR}=<id> to .env "
            "(the id is the long string in the spreadsheet URL), or share the "
            "sheet directly with the client_email in keys/service.json."
        )
    return found[0]["id"]


def sync(sheet_id: str, creds, tabs: list[tuple[str, list[list]]]) -> list[str]:
    """Create missing tabs, then replace the contents of each one."""
    from googleapiclient.discovery import build

    svc = build("sheets", "v4", credentials=creds, cache_discovery=False).spreadsheets()
    meta = svc.get(spreadsheetId=sheet_id).execute()
    existing = {s["properties"]["title"]: s["properties"]["sheetId"]
                for s in meta["sheets"]}

    adds = [{"addSheet": {"properties": {"title": name}}}
            for name, _ in tabs if name not in existing]
    if adds:
        svc.batchUpdate(spreadsheetId=sheet_id, body={"requests": adds}).execute()
        meta = svc.get(spreadsheetId=sheet_id).execute()
        existing = {s["properties"]["title"]: s["properties"]["sheetId"]
                    for s in meta["sheets"]}

    # Clear first: a shorter table must not leave last run's rows below it.
    svc.values().batchClear(
        spreadsheetId=sheet_id,
        body={"ranges": [f"'{name}'" for name, _ in tabs]},
    ).execute()

    svc.values().batchUpdate(
        spreadsheetId=sheet_id,
        body={
            "valueInputOption": "RAW",
            "data": [
                {"range": f"'{name}'!A1", "values": clip(rows)}
                for name, rows in tabs if rows
            ],
        },
    ).execute()

    # Freeze the header row and bold it on every tab.
    fmt = []
    for name, _ in tabs:
        tab_id = existing[name]
        fmt.append({"updateSheetProperties": {
            "properties": {"sheetId": tab_id,
                           "gridProperties": {"frozenRowCount": 1}},
            "fields": "gridProperties.frozenRowCount"}})
        fmt.append({"repeatCell": {
            "range": {"sheetId": tab_id, "startRowIndex": 0, "endRowIndex": 1},
            "cell": {"userEnteredFormat": {"textFormat": {"bold": True}}},
            "fields": "userEnteredFormat.textFormat.bold"}})
    svc.batchUpdate(spreadsheetId=sheet_id, body={"requests": fmt}).execute()

    return [f"{name}: {max(len(rows) - 1, 0)} rows" for name, rows in tabs]


# --------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="collect everything and report, but do not touch Sheets")
    args = ap.parse_args()

    env = load_env()
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    notes: list[str] = []
    tabs: list[tuple[str, list[list]]] = []

    for tab_name, filename in CSV_TABS:
        path = REGISTRY / filename
        if not path.exists():
            notes.append(f"{filename} not found - {tab_name} tab skipped")
            continue
        tabs.append((tab_name, read_csv_rows(path)))

    channel_rows, post_rows, buf_notes = collect_buffer(env)
    notes += buf_notes
    notes += reconcile(post_rows)

    tabs.append(("buffer_channels", [[
        "account", "account_email", "organization", "channel_id", "channel",
        "service", "type", "disconnected", "timezone", "posting_schedule",
    ]] + channel_rows))

    # Built in one order for readability above, presented in another: the
    # reconciliation verdict and the status lead, because those are what you
    # scan for. Identifiers trail at the end - you only want them once you have
    # already found the row that matters.
    built = ["account", "account_email", "post_id", "status", "channel_id",
             "channel", "service", "due_at", "sent_at", "tags",
             "external_link", "text", "in_shares_csv"]
    shown = ["in_shares_csv", "status", "sent_at", "due_at", "service",
             "channel", "account", "tags", "external_link", "text",
             "post_id", "channel_id", "account_email"]
    order = [built.index(c) for c in shown]
    tabs.append(("buffer_queue",
                 [shown] + [[r[i] for i in order] for r in post_rows]))

    summary = [["key", "value"], ["last_synced", stamp]]
    for name, rows in tabs:
        summary.append([f"rows_{name}", str(max(len(rows) - 1, 0))])
    summary.append(["buffer_accounts", str(len(buffer_accounts(env)))])
    for i, note in enumerate(notes, 1):
        summary.append([f"note_{i}", note])
    if not notes:
        summary.append(["note_1", "clean run - nothing to flag"])
    tabs.insert(0, ("sync_status", summary))

    if args.dry_run:
        for name, rows in tabs:
            print(f"{name}: {max(len(rows) - 1, 0)} rows")
        for note in notes:
            print(f"  ! {note}")
        return 0

    if not SERVICE_ACCOUNT.exists():
        sys.exit(f"missing {SERVICE_ACCOUNT.relative_to(REPO)} - see the docstring")

    from google.oauth2 import service_account as sa

    creds = sa.Credentials.from_service_account_file(
        str(SERVICE_ACCOUNT),
        scopes=[SHEETS_SCOPE, "https://www.googleapis.com/auth/drive.readonly"],
    )
    sheet_id = open_spreadsheet(creds, env)
    for line in sync(sheet_id, creds, tabs):
        print(line)
    for note in notes:
        print(f"  ! {note}")
    print(f"\nsynced {stamp}")
    print(f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit")
    return 0


if __name__ == "__main__":
    sys.exit(main())
