#!/usr/bin/env python3
"""Build the human-readable view of the registry in Google Sheets.

`sync_tracker.py` dumps the CSVs verbatim: every column, cryptic names, text
clipped to one line. That is the right shape for a machine and the wrong shape
for two people deciding where to post next. This script builds the reading
view instead - one tab per kind of thing, plain tab names, and four columns
that answer the only questions that matter in front of a room:

    what is this, what are their rules, how do we approach it, how important

The CSVs remain the source of truth. Everything here is derived from them, so
a wrong sentence in this sheet is a wrong cell in a CSV, not a thing to fix by
hand in Google.

Usage:  python scripts/build_reading_sheet.py [--dry-run]
Needs:  keys/service.json, TRACKER_SHEET_ID in .env,
        google-auth and google-api-python-client
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
REGISTRY = REPO / "registry"
SERVICE_ACCOUNT = REPO / "keys" / "service.json"
ENV_FILE = REPO / ".env"
SCOPE = "https://www.googleapis.com/auth/spreadsheets"

PRIORITY = {
    "A": "A - core fit",
    "B": "B - good",
    "C": "C - marginal",
    "D": "D - do not post",
    "1": "1 - post here first",
    "2": "2 - good",
    "3": "3 - marginal",
}


def load_env() -> dict[str, str]:
    env = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env


def read(name: str) -> list[dict]:
    path = REGISTRY / name
    if not path.exists():
        return []
    return list(csv.DictReader(path.open(encoding="utf-8")))


def tidy(*parts: str) -> str:
    """Join non-empty fragments into one sentence-ish string."""
    return " ".join(p.strip() for p in parts if p and p.strip())


# --------------------------------------------------------------------------
# Turning a written rule into an instruction.
#
# The rule column is the research; this is what to DO about it. The order of
# the checks matters: a hard ban has to win over a softer phrase appearing
# later in the same rule text.

BAN_PHRASES = (
    "permaban", "zero tolerance", "do not allow study recruitment",
    "we do not allow study recruitment",
)
SELF_PROMO_PHRASES = (
    "self-promotion, spam and irrelevant links",
    "no promotions or spam", "no spam or gratuitous self-promotion",
    "fara promotii", "no promotions",
)


def advice(rule: str, *, platform: str = "", relevance: str = "",
           admin: str = "", status: str = "", lead: str = "") -> str:
    """`lead` is the room's own recorded guidance and goes first when present;
    the derived sentences only fill the gap where we have none."""
    r = (rule or "").strip().lower()
    out: list[str] = []

    if lead:
        lead = lead if lead.endswith((".", "!", "?")) else lead + "."
    if not r:
        base = ("Nobody has read the rules here yet. Open it, read the rules "
                "tab, and write the rule into the registry before anything is "
                "drafted for this room.")
        base = base if not (relevance == "D" or status == "retired") \
            else "DO NOT POST. " + base
        return tidy(lead, base)

    if relevance == "D" or status == "retired":
        out.append("DO NOT POST.")
    if any(p in r for p in BAN_PHRASES):
        out.append("The written rule bans research or survey posts outright, "
                   "with no warning before a ban. Nothing we can post here is "
                   "worth the account.")
    elif "regular members" in r:
        out.append("The rule permits regular members to share what they do, so "
                   "the way in is to take part first: comment for a couple of "
                   "weeks, then post as a member rather than as a project.")
    elif any(p in r for p in SELF_PROMO_PHRASES):
        out.append("Self-promotion is banned, so do not post a link. Message "
                   "the admins first: say it is an ethics-approved study from "
                   "University Medicine Rostock, that we are recruiting adults "
                   "18+, that nothing is being sold, and ask whether a post is "
                   "welcome.")
    elif ("publishes no rules" in r or "no rules published" in r
          or "no self-promotion rule" in r or "no self promotion rule" in r):
        out.append("No self-promotion rule is published. That is not the same "
                   "as permission - ask an admin, then post as a participant "
                   "sharing something we made, not as an announcement.")
    elif "unverified" in r or "not read" in r:
        out.append("The rule here is unconfirmed. Open it, read the rules tab, "
                   "and record the actual rule before anything is drafted for "
                   "this room.")
    elif not lead:
        # Only worth saying when the room has no guidance of its own; otherwise
        # it is a line of filler repeated down the whole column.
        out.append("Write to the rule in the previous column.")

    if platform == "reddit":
        out.append("Never ask anyone to upvote or comment: Reddit penalises "
                   "the linked site as well as the account.")
    elif platform == "linkedin-group":
        out.append("LinkedIn groups have no API and no scheduler - a person "
                   "types the post into the group composer, one at a time.")
    elif platform == "linkedin":
        out.append("Posts to this feed go through the official API, so Buffer "
                   "and scheduling work here - unlike LinkedIn groups.")
    elif platform == "whatsapp":
        out.append("Draft only. WhatsApp runs on a personal number.")

    if admin and admin not in ("-", "") and "message the admins" in " ".join(out).lower():
        out.append(f"Contact: {admin}.")
    return tidy(lead, *out)


# --------------------------------------------------------------------------
# Descriptions. Never invented: every sentence is assembled out of fields the
# registry actually holds. A room nobody has opened says so, in words.

CATEGORY_WORDS = {
    "cgm": "people using continuous glucose monitors",
    "diabetes": "people living with diabetes",
    "longevity-aging": "longevity and ageing",
    "biohacking": "biohacking and self-experimentation",
    "bioinformatics-compbio": "bioinformatics and computational biology",
    "bioinformatics": "bioinformatics",
    "genetics-biotech": "genetics and biotech",
    "genomics": "genomics",
    "science-popular": "popular science",
    "health-wellness": "health and wellness",
    "clinical-research": "clinical research",
    "clinical": "clinicians and clinical research",
    "digital-health": "digital health and medtech",
    "ml-health": "machine learning in healthcare",
    "wearables": "wearable sensors",
    "transhumanism": "transhumanism",
    "longevity": "longevity",
    "self-tracking": "self-tracking and quantified self",
    "research-recruitment": "study recruitment",
    "open-source": "open-source software",
    "science-qa": "science questions and answers",
    "science": "science",
    "tech": "technology",
    "webdev": "web development",
    "side-project": "side projects",
    "data-viz": "data visualisation",
    "biology": "biology",
    "desci-funder": "decentralised science funding",
    "multi": "a mixed audience",
    "rationalist": "the rationalist community",
    "ea": "effective altruism",
    "design": "design",
    "bioengineering": "bioengineering",
    "media": "diabetes media",
    "advocacy": "diabetes advocacy",
    "creator": "a creator audience",
    "podcast": "podcast listeners",
    "industry": "industry",
    "research": "research",
    "professional": "a professional audience",
}
LANG_WORDS = {"en": "English", "ro": "Romanian", "uk": "Ukrainian",
              "ru": "Russian", "de": "German", "ru/en": "Russian and English"}


def size_of(r: dict) -> str:
    """The member count as its own value, so it can be sorted and filtered."""
    size = (r.get("size") or "").strip()
    return "" if size in ("-", "n/a", "N/A") else size


def lang_of(r: dict) -> str:
    raw = (r.get("language") or "").strip()
    return LANG_WORDS.get(raw, raw)


def describe_room(r: dict, where: str, use_notes: bool = True) -> str:
    """Prose only - no size, no language. Those are columns of their own."""
    raw = (r.get("category") or "").strip()
    cat = CATEGORY_WORDS.get(raw, raw.replace("-", " ") if raw else "")
    bits = [f"A {where} for {cat}." if cat else f"A {where}."]
    notes = (r.get("notes") or "").strip() if use_notes else ""
    if notes and not notes.lower().startswith((
            "in destinations.csv", "promoted to destinations", "release condition")):
        bits.append(notes if notes.endswith(".") else notes + ".")
    elif not notes and use_notes:
        bits.append("Not described yet - nobody has opened it.")
    return tidy(*bits)


ROOM_HEADERS = ["Group", "Where", "Members", "Language", "What it is",
                "Their posting rules", "How to approach them", "Priority",
                "Status", "Link"]


def rows_destinations() -> list[list[str]]:
    out = []
    for r in read("destinations.csv"):
        out.append([
            r["name"],
            r["platform"].replace("-", " "),
            size_of(r),
            lang_of(r),
            describe_room(r, "room", use_notes=False),
            r.get("self_promo_rule") or "Not read yet.",
            advice(r.get("self_promo_rule", ""), platform=r["platform"],
                   admin=r.get("admin_contact", ""), status=r.get("status", ""),
                   lead=(r.get("notes") or "").strip()),
            PRIORITY.get((r.get("tier") or "").strip(), r.get("tier", "")),
            r.get("status", ""),
            r.get("handle_or_url", ""),
        ])
    out.sort(key=lambda x: (x[8] != "active", x[7]))
    return [ROOM_HEADERS] + out


def rows_groups(filename: str, where: str, platform: str) -> list[list[str]]:
    out = []
    for r in read(filename):
        rel = (r.get("relevance") or "").strip()
        out.append([
            r["name"],
            where,
            size_of(r),
            lang_of(r),
            describe_room(r, where.lower().rstrip("s")),
            r.get("self_promo_rule") or "Not read yet.",
            advice(r.get("self_promo_rule", ""), platform=platform,
                   relevance=rel, status=r.get("status", "")),
            PRIORITY.get(rel, rel),
            r.get("status", ""),
            r.get("url") or r.get("username_or_url", ""),
        ])
    out.sort(key=lambda x: (x[7] or "z", x[0].lower()))
    return [ROOM_HEADERS] + out


CONTACT_HEADERS = ["Name", "Channel", "Followers", "Language", "What they are",
                   "Why they matter to us", "What to ask them for", "Priority",
                   "Status", "Link"]


def rows_media() -> list[list[str]]:
    out = []
    for r in read("media-catalogue.csv"):
        ch = {"tiktok": "TikTok creator", "instagram": "Instagram account",
              "youtube": "YouTube channel",
              "podcast": "Podcast", "blog": "Blog or news site",
              "newsletter": "Newsletter"}.get(r["channel"], r["channel"])
        what = ch + "."
        if (r.get("audience_source") or "").endswith("UNVERIFIED"):
            what += (" Follower figure comes from a published ranking and has not "
                     "been checked on the platform.")
        out.append([
            r["name"], ch, (r.get("audience") or "").strip(),
            LANG_WORDS.get((r.get("language") or "").strip(), r.get("language", "")),
            what, r.get("bio_or_focus", ""), r.get("suggested_ask", ""),
            PRIORITY.get(r.get("relevance", ""), r.get("relevance", "")),
            r.get("status", ""), r.get("handle_or_url", ""),
        ])
    out.sort(key=lambda x: (x[7] or "z", x[0].lower()))
    return [CONTACT_HEADERS] + out


def rows_people() -> list[list[str]]:
    out = []
    for r in read("linkedin-people-catalogue.csv"):
        kind = {"company-page": "LinkedIn company page",
                "person": "Person on LinkedIn",
                "showcase": "LinkedIn showcase page"}.get(r["type"], r["type"])
        country = (r.get("country") or "").strip()
        what = kind + (f", based in {country}." if country else ".")
        out.append([
            r["name"], kind, "", country, what, r.get("why_relevant", ""),
            r.get("suggested_ask", ""),
            PRIORITY.get(r.get("relevance", ""), r.get("relevance", "")),
            r.get("status", ""), r.get("url", ""),
        ])
    out.sort(key=lambda x: (x[7] or "z", x[0].lower()))
    return [CONTACT_HEADERS] + out


def rows_orgs() -> list[list[str]]:
    out = []
    for r in read("diabetes-orgs-catalogue.csv"):
        country = (r.get("country") or "").strip()
        focus = (r.get("focus") or "").strip()
        size = (r.get("size") or "").strip()
        what = tidy(
            f"Diabetes organisation in {country}." if country else "Diabetes organisation.",
            f"Focus: {focus}." if focus else "",
            f"Size: {size}." if size else "")
        ask = ("Approach as a grant or funding contact - they fund external research."
               if (r.get("grants") or "").strip().lower().startswith("y")
               else "Approach for distribution: ask them to put the study in front of "
                    "their members or in a newsletter.")
        out.append([
            r["name"], "Organisation", size, country, what,
            r.get("sugar_sugar_relevance", ""), ask, "",
            r.get("status", ""), r.get("url", ""),
        ])
    out.sort(key=lambda x: x[0].lower())
    return [CONTACT_HEADERS] + out


MFR_HEADERS = ["Manufacturer", "Country", "Market share", "Tier", "Reachability",
               "What they make", "How to reach them", "What to ask them for",
               "When", "Status", "Link"]


def rows_manufacturers() -> list[list[str]]:
    """CGM makers. Not an audience - a partnership and hardware-access list.

    Sorted by outreach phase, because the order of approach is the point: the
    open programmes first, the enterprise review committees last.
    """
    out = []
    for r in read("cgm-manufacturers-catalogue.csv"):
        reach = r.get("reachability", "")
        contact = tidy(r.get("contact_emails", ""),
                       ("Portals: " + r["portals"]) if r.get("portals") else "")
        out.append([
            r["name"], r.get("country", ""), r.get("market_share", ""),
            "Tier " + r.get("tier", ""), reach, r.get("products", ""),
            contact, tidy(r.get("why_relevant", ""), r.get("suggested_ask", ""),
                          r.get("notes", "")),
            r.get("phase", ""), r.get("status", ""), r.get("website", ""),
        ])
    out.sort(key=lambda x: (x[8] or "z", x[3]))
    return [MFR_HEADERS] + out


TABS = [
    ("Places to post", rows_destinations),
    ("Facebook groups", lambda: rows_groups(
        "facebook-groups-catalogue.csv", "Facebook group", "facebook")),
    ("LinkedIn groups", lambda: rows_groups(
        "linkedin-groups-catalogue.csv", "LinkedIn group", "linkedin-group")),
    ("Telegram", lambda: rows_groups(
        "telegram-groups-catalogue.csv", "Telegram chat", "telegram")),
    ("Influencers & media", rows_media),
    ("People & pages", rows_people),
    ("Organisations", rows_orgs),
    ("CGM manufacturers", rows_manufacturers),
]

# Column widths in pixels, by header name. Anything not listed gets NARROW.
WIDE = {"What they make": 240, "How to reach them": 300,
        "What to ask them for": 430, "Manufacturer": 190, "Country": 130,
        "Market share": 100, "Reachability": 110, "When": 130,
        "What it is": 300, "Their posting rules": 330,
        "How to approach them": 380, "Why they matter to us": 330,
        "What to ask them for": 330, "What they are": 220, "Link": 260,
        "Group": 220, "Name": 200, "Members": 90, "Followers": 110,
        "Language": 95, "Channel": 120}
NARROW = 110
WRAPPED = {"What they make", "How to reach them", "What to ask them for",
           "What it is", "Their posting rules", "How to approach them",
           "Why they matter to us", "What to ask them for", "What they are"}


def style_requests(sheet_id: int, headers: list[str], n_rows: int) -> list[dict]:
    """Header, widths, wrap, then row auto-resize LAST.

    Order matters. A fixed row height silently defeats wrapping: the text
    wraps but the row stays one line tall and you read a clipped sentence.
    Rows are auto-resized only after the wrap strategy is set.
    """
    req = [
        {"repeatCell": {
            "range": {"sheetId": sheet_id, "startRowIndex": 0, "endRowIndex": 1},
            "cell": {"userEnteredFormat": {
                "backgroundColor": {"red": 0.12, "green": 0.20, "blue": 0.31},
                "textFormat": {"bold": True, "fontSize": 11,
                               "foregroundColor": {"red": 1, "green": 1, "blue": 1}},
                "verticalAlignment": "MIDDLE",
                "wrapStrategy": "WRAP"}},
            "fields": "userEnteredFormat(backgroundColor,textFormat,"
                      "verticalAlignment,wrapStrategy)"}},
        {"updateSheetProperties": {
            "properties": {"sheetId": sheet_id,
                           "gridProperties": {"frozenRowCount": 1}},
            "fields": "gridProperties.frozenRowCount"}},
        {"setBasicFilter": {"filter": {"range": {
            "sheetId": sheet_id, "startRowIndex": 0,
            "endRowIndex": max(n_rows, 1), "startColumnIndex": 0,
            "endColumnIndex": len(headers)}}}},
    ]
    for i, h in enumerate(headers):
        req.append({"updateDimensionProperties": {
            "range": {"sheetId": sheet_id, "dimension": "COLUMNS",
                      "startIndex": i, "endIndex": i + 1},
            "properties": {"pixelSize": WIDE.get(h, NARROW)},
            "fields": "pixelSize"}})
        req.append({"repeatCell": {
            "range": {"sheetId": sheet_id, "startRowIndex": 1,
                      "startColumnIndex": i, "endColumnIndex": i + 1},
            "cell": {"userEnteredFormat": {
                "wrapStrategy": "WRAP" if h in WRAPPED else "CLIP",
                "verticalAlignment": "TOP",
                "textFormat": {"fontSize": 10}}},
            "fields": "userEnteredFormat(wrapStrategy,verticalAlignment,textFormat)"}})
    return req


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="build everything and report, but do not touch Sheets")
    args = ap.parse_args()

    # A tab with only a header is noise - the Telegram catalogue emptied out
    # once the enhancement.bio memberships were pruned.
    built = [(title, rows) for title, rows in ((t, f()) for t, f in TABS)
             if len(rows) > 1]

    if args.dry_run:
        for title, rows in built:
            print(f"{title}: {len(rows) - 1} rows, {len(rows[0])} columns")
            if len(rows) > 1:
                print(f"    e.g. {rows[1][0]}")
                print(f"    ->   {rows[1][4 if len(rows[1]) > 4 else -1][:150]}")
        return 0

    env = load_env()
    sheet_id = env.get("TRACKER_SHEET_ID")
    if not sheet_id:
        sys.exit("TRACKER_SHEET_ID is not set in .env")
    if not SERVICE_ACCOUNT.exists():
        sys.exit(f"missing {SERVICE_ACCOUNT.relative_to(REPO)}")

    from google.oauth2 import service_account as sa
    from googleapiclient.discovery import build

    creds = sa.Credentials.from_service_account_file(str(SERVICE_ACCOUNT),
                                                     scopes=[SCOPE])
    svc = build("sheets", "v4", credentials=creds,
                cache_discovery=False).spreadsheets()

    wanted = [t for t, _ in built]
    meta = svc.get(spreadsheetId=sheet_id).execute()
    existing = {s["properties"]["title"]: s["properties"]["sheetId"]
                for s in meta["sheets"]}

    adds = [{"addSheet": {"properties": {"title": t}}}
            for t in wanted if t not in existing]
    if adds:
        svc.batchUpdate(spreadsheetId=sheet_id, body={"requests": adds}).execute()

    doomed = [t for t in existing if t not in wanted]
    if doomed and len(doomed) < len(existing) + len(adds):
        svc.batchUpdate(spreadsheetId=sheet_id, body={"requests": [
            {"deleteSheet": {"sheetId": existing[t]}} for t in doomed]}).execute()
        print("removed old tabs: " + ", ".join(sorted(doomed)))

    meta = svc.get(spreadsheetId=sheet_id).execute()
    ids = {s["properties"]["title"]: s["properties"]["sheetId"]
           for s in meta["sheets"]}

    svc.values().batchClear(spreadsheetId=sheet_id,
                            body={"ranges": wanted}).execute()
    svc.values().batchUpdate(spreadsheetId=sheet_id, body={
        "valueInputOption": "RAW",
        "data": [{"range": f"'{t}'!A1", "values": rows} for t, rows in built],
    }).execute()

    fmt: list[dict] = []
    for i, (title, rows) in enumerate(built):
        fmt += style_requests(ids[title], rows[0], len(rows))
        fmt.append({"updateSheetProperties": {
            "properties": {"sheetId": ids[title], "index": i},
            "fields": "index"}})
    svc.batchUpdate(spreadsheetId=sheet_id, body={"requests": fmt}).execute()

    svc.batchUpdate(spreadsheetId=sheet_id, body={"requests": [
        {"autoResizeDimensions": {"dimensions": {
            "sheetId": ids[title], "dimension": "ROWS",
            "startIndex": 1, "endIndex": max(len(rows), 2)}}}
        for title, rows in built]}).execute()

    for title, rows in built:
        print(f"{title}: {len(rows) - 1} rows")
    print(f"\nhttps://docs.google.com/spreadsheets/d/{sheet_id}/edit")
    return 0


if __name__ == "__main__":
    sys.exit(main())
