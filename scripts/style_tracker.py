#!/usr/bin/env python3
"""Apply readable formatting to the tracker spreadsheet. Run by hand, rarely.

Deliberately NOT part of sync_tracker.py. Formatting in Sheets lives on the
cell grid, not on the values, so `values.batchClear` leaves it untouched: style
once and every later sync keeps it. Folding this into the scheduled job would
mean thousands of pointless formatting requests a week to achieve nothing.

What it does, per tab:
  - header row frozen, bold, white on navy, wrapped
  - long prose columns wrapped and widened; everything else clipped and narrow
  - body cells top-aligned so a wrapped row stays readable
  - alternating row banding
  - colour that carries meaning, via CONDITIONAL rules keyed to cell values,
    so the colour follows the data when the next sync rewrites the rows

Usage:
    uv run --no-project python scripts/style_tracker.py [--dry-run]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SERVICE_ACCOUNT = REPO / "keys" / "service.json"
ENV_FILE = REPO / ".env"
SHEET_ID_VAR = "TRACKER_SHEET_ID"
SHEETS_SCOPE = "https://www.googleapis.com/auth/spreadsheets"

NAVY = {"red": 0.122, "green": 0.200, "blue": 0.314}
WHITE = {"red": 1.0, "green": 1.0, "blue": 1.0}
BAND = {"red": 0.965, "green": 0.973, "blue": 0.980}

RED = {"red": 0.992, "green": 0.906, "blue": 0.914}
AMBER = {"red": 1.0, "green": 0.965, "blue": 0.898}
GREEN = {"red": 0.918, "green": 0.969, "blue": 0.933}
GREY = {"red": 0.910, "green": 0.910, "blue": 0.910}

RED_TEXT = {"red": 0.639, "green": 0.106, "blue": 0.153}
GREEN_TEXT = {"red": 0.086, "green": 0.396, "blue": 0.204}
GREY_TEXT = {"red": 0.443, "green": 0.443, "blue": 0.443}

# Prose that needs room to breathe. Everything else stays narrow and clipped so
# a stray long URL cannot smear across the row.
WRAP_COLS = {
    "self_promo_rule", "notes", "thesis_one_line", "key_facts_to_include",
    "link_behaviour", "key_rule_to_remember", "assets_needed",
    "media_needed", "posting_schedule", "value",
}
# Full post bodies. Wide enough to read the opening, but CLIPPED: wrapping a
# 2,000-character post turns one row into half a screen and makes the tab
# unscannable. The whole value is still in the cell - click it and read the
# formula bar, or open the row's source CSV.
BODY_COLS = {"text", "text_sent", "full_text"}
WIDE = 460
MEDIUM_COLS = {
    "handle_or_url", "url", "published_url", "permalink", "link_used",
    "external_link", "name", "title", "channel", "admin_contact",
    "account_email", "key", "in_shares_csv", "dest_id", "utm_source",
    "utm_campaign", "sent_at", "due_at",
}
MEDIUM = 230
NARROW = 120


def load_env() -> dict[str, str]:
    out: dict[str, str] = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def text_rule(sheet_id, col, rows, needle, bg, fg, bold=False):
    """Colour a single column where its text contains `needle`."""
    fmt = {"backgroundColor": bg,
           "textFormat": {"foregroundColor": fg, "bold": bold}}
    return {"addConditionalFormatRule": {"index": 0, "rule": {
        "ranges": [{"sheetId": sheet_id, "startRowIndex": 1,
                    "endRowIndex": rows, "startColumnIndex": col,
                    "endColumnIndex": col + 1}],
        "booleanRule": {
            "condition": {"type": "TEXT_CONTAINS",
                          "values": [{"userEnteredValue": needle}]},
            "format": fmt}}}}


def row_rule(sheet_id, cols, rows, formula, bg, fg=None):
    """Colour a whole row driven by a formula over one column."""
    fmt = {"backgroundColor": bg}
    if fg:
        fmt["textFormat"] = {"foregroundColor": fg}
    return {"addConditionalFormatRule": {"index": 0, "rule": {
        "ranges": [{"sheetId": sheet_id, "startRowIndex": 1,
                    "endRowIndex": rows, "startColumnIndex": 0,
                    "endColumnIndex": cols}],
        "booleanRule": {
            "condition": {"type": "CUSTOM_FORMULA",
                          "values": [{"userEnteredValue": formula}]},
            "format": fmt}}}}


def build_requests(meta, values_by_tab) -> list[dict]:
    reqs: list[dict] = []

    # Idempotency: strip formatting this script previously added, so repeat
    # runs converge instead of stacking duplicate rules.
    for sheet in meta["sheets"]:
        sid = sheet["properties"]["sheetId"]
        for i in range(len(sheet.get("conditionalFormats", [])) - 1, -1, -1):
            reqs.append({"deleteConditionalFormatRule": {"sheetId": sid, "index": i}})
        for band in sheet.get("bandedRanges", []):
            reqs.append({"deleteBanding": {"bandedRangeId": band["bandedRangeId"]}})

    for sheet in meta["sheets"]:
        props = sheet["properties"]
        sid, title = props["sheetId"], props["title"]
        grid = props.get("gridProperties", {})
        max_rows = grid.get("rowCount", 1000)

        header = (values_by_tab.get(title) or [[]])[0]
        n_cols = max(len(header), 1)
        n_rows = len(values_by_tab.get(title) or [[]])
        idx = {name: i for i, name in enumerate(header)}

        # Freeze the header.
        reqs.append({"updateSheetProperties": {
            "properties": {"sheetId": sid,
                           "gridProperties": {"frozenRowCount": 1}},
            "fields": "gridProperties.frozenRowCount"}})

        # Body: top-aligned, clipped, small type.
        reqs.append({"repeatCell": {
            "range": {"sheetId": sid, "startRowIndex": 1},
            "cell": {"userEnteredFormat": {
                "verticalAlignment": "TOP",
                "wrapStrategy": "CLIP",
                "textFormat": {"fontSize": 10},
            }},
            "fields": ("userEnteredFormat(verticalAlignment,wrapStrategy,"
                       "textFormat.fontSize)")}})

        # Header: navy, white, bold, wrapped, centred.
        reqs.append({"repeatCell": {
            "range": {"sheetId": sid, "startRowIndex": 0, "endRowIndex": 1,
                      "startColumnIndex": 0, "endColumnIndex": n_cols},
            "cell": {"userEnteredFormat": {
                "backgroundColor": NAVY,
                "verticalAlignment": "MIDDLE",
                "wrapStrategy": "WRAP",
                "textFormat": {"bold": True, "fontSize": 10,
                               "foregroundColor": WHITE},
            }},
            "fields": ("userEnteredFormat(backgroundColor,verticalAlignment,"
                       "wrapStrategy,textFormat)")}})

        # Per-column width and wrapping.
        for name, col in idx.items():
            wrap = name in WRAP_COLS
            if wrap or name in BODY_COLS:
                width = WIDE
            elif name in MEDIUM_COLS:
                width = MEDIUM
            else:
                width = NARROW
            reqs.append({"updateDimensionProperties": {
                "range": {"sheetId": sid, "dimension": "COLUMNS",
                          "startIndex": col, "endIndex": col + 1},
                "properties": {"pixelSize": width},
                "fields": "pixelSize"}})
            if wrap:
                reqs.append({"repeatCell": {
                    "range": {"sheetId": sid, "startRowIndex": 1,
                              "startColumnIndex": col, "endColumnIndex": col + 1},
                    "cell": {"userEnteredFormat": {"wrapStrategy": "WRAP"}},
                    "fields": "userEnteredFormat.wrapStrategy"}})

        # Hide unused columns beyond the data so the tab ends where data ends.
        if n_cols < grid.get("columnCount", 26):
            reqs.append({"updateDimensionProperties": {
                "range": {"sheetId": sid, "dimension": "COLUMNS",
                          "startIndex": n_cols,
                          "endIndex": grid.get("columnCount", 26)},
                "properties": {"hiddenByUser": True},
                "fields": "hiddenByUser"}})

        # Let each row find its own height, AFTER the wrap strategies above are
        # in place. A fixed height would silently defeat wrapping - the text
        # wraps but the row stays one line tall and you see a clipped sentence.
        # This also clears heights left behind by an earlier run.
        reqs.append({"autoResizeDimensions": {"dimensions": {
            "sheetId": sid, "dimension": "ROWS",
            "startIndex": 1, "endIndex": max(n_rows, 2)}}})

        # Banding for row tracking.
        reqs.append({"addBanding": {"bandedRange": {
            "range": {"sheetId": sid, "startRowIndex": 1,
                      "endRowIndex": max(n_rows, 2),
                      "startColumnIndex": 0, "endColumnIndex": n_cols},
            "rowProperties": {"firstBandColor": WHITE,
                              "secondBandColor": BAND}}}})

        # ---- meaning-bearing colour, per tab -----------------------------
        if title == "buffer_queue" and "in_shares_csv" in idx:
            c = idx["in_shares_csv"]
            reqs.append(text_rule(sid, c, max_rows, "NO - not logged",
                                  RED, RED_TEXT, bold=True))
            reqs.append(text_rule(sid, c, max_rows, "predates", GREY, GREY_TEXT))
            reqs.append(text_rule(sid, c, max_rows, "yes", GREEN, GREEN_TEXT))
            if "status" in idx:
                s = idx["status"]
                reqs.append(text_rule(sid, s, max_rows, "error", RED, RED_TEXT, True))
                reqs.append(text_rule(sid, s, max_rows, "scheduled", GREEN, GREEN_TEXT))

        if title == "destinations" and "tier" in idx:
            col_letter = chr(ord("A") + idx["tier"])
            for tier, colour in (("1", RED), ("2", AMBER), ("3", GREEN)):
                reqs.append(row_rule(
                    sid, n_cols, max_rows,
                    f'=${col_letter}2="{tier}"', colour))

        # Inactive rows grey out, and must win over the tier tint, so they are
        # added last: index 0 puts each new rule at the top of the stack.
        if "status" in idx and title in {"destinations", "pillars",
                                         "cat_linkedin_groups",
                                         "cat_facebook_groups",
                                         "cat_telegram_groups"}:
            col_letter = chr(ord("A") + idx["status"])
            reqs.append(row_rule(
                sid, n_cols, max_rows,
                f'=OR(${col_letter}2="on-hold",${col_letter}2="retired",'
                f'${col_letter}2="comment-only")',
                GREY, GREY_TEXT))

        if title == "sync_status" and "key" in idx:
            reqs.append(row_rule(sid, n_cols, max_rows,
                                 '=LEFT($A2,4)="note"', AMBER))
            reqs.append(row_rule(sid, n_cols, max_rows,
                                 '=$A2="last_synced"', GREEN))

    return reqs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not SERVICE_ACCOUNT.exists():
        sys.exit(f"missing {SERVICE_ACCOUNT.relative_to(REPO)}")
    env = load_env()
    sheet_id = env.get(SHEET_ID_VAR)
    if not sheet_id:
        sys.exit(f"{SHEET_ID_VAR} is not set in .env")

    from google.oauth2 import service_account as sa
    from googleapiclient.discovery import build

    creds = sa.Credentials.from_service_account_file(
        str(SERVICE_ACCOUNT), scopes=[SHEETS_SCOPE])
    svc = build("sheets", "v4", credentials=creds,
                cache_discovery=False).spreadsheets()

    meta = svc.get(spreadsheetId=sheet_id).execute()
    titles = [s["properties"]["title"] for s in meta["sheets"]]
    fetched = svc.values().batchGet(
        spreadsheetId=sheet_id,
        ranges=[f"'{t}'" for t in titles]).execute().get("valueRanges", [])
    values_by_tab = {t: vr.get("values", [[]])
                     for t, vr in zip(titles, fetched)}

    reqs = build_requests(meta, values_by_tab)
    print(f"{len(titles)} tabs, {len(reqs)} formatting requests")
    if args.dry_run:
        return 0

    # Chunked: a single batchUpdate with many hundreds of requests can time out.
    for i in range(0, len(reqs), 100):
        svc.batchUpdate(spreadsheetId=sheet_id,
                        body={"requests": reqs[i:i + 100]}).execute()
    print("styled")
    print(f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit")
    return 0


if __name__ == "__main__":
    sys.exit(main())
