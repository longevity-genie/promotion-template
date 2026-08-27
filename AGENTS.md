# Agent instructions

> **Sync rule:** `AGENTS.md` and `CLAUDE.md` must have identical content. When you edit either file, copy the change to the other immediately. A pre-commit hook (`scripts/sync-agents-claude.sh`) enforces this — commit will fail if they differ.

This repo is a promotion and distribution system for one project. Read `README.md` for the shape, `PROMPTS.md` for the numbered tasks, `project/schema.md` for every column's meaning.

## Paths

Resolve everything relative to this repo's root — the folder containing this file. Never write an absolute path, a username, or a home directory into any file, script, or scheduled task. Scripts here locate the repo with `Path(__file__).resolve().parent.parent`; do the same. A hardcoded path is a bug: it works for exactly one person and breaks silently for everyone else.

The same applies to external identifiers. Discover Google Drive folders by title search and create one if none matches; never record the resulting id in a prompt or a committed file.

## Read these two before writing a single word

1. `project/PROJECT.md` — the standing facts, voice rules, forbidden words, and who writes as whom. If it still contains template placeholders, stop and say so rather than inventing a voice.
2. `registry/platform_rules.csv` for the platform, and the specific row in `registry/destinations.csv` for the room. The `self_promo_rule` column holds that community's actual written rule.

## Registry structure

- `registry/destinations.csv` — communities with URLs, sizes, rules, tiers, scheduling and weekend info
- `registry/platform_rules.csv` — platforms with posting rules, scheduling capability, and weekend behaviour
- `registry/facebook-groups-catalogue.csv` — research inbox for Facebook (not a destination list)
- `registry/linkedin-groups-catalogue.csv` — research inbox for LinkedIn groups (not a destination list)
- `registry/telegram-groups-catalogue.csv` — durable inventory of Telegram memberships, linked discussion chats, rules and prior project posts (not a destination list)
- `registry/pillars.csv` — long-form canonical assets
- `registry/derivatives.csv` — platform-native posts made from a pillar
- `registry/shares.csv` — one row per post actually sent, with outcome
- `registry/utm_convention.md` — the tagging scheme

## Drafts structure

Each draft subfolder has a `TODO.md` with image preparation tasks and a pre-posting checklist.

- `drafts/linkedin/` — one folder per posting identity (personal profiles, a company or showcase page, reshare commentary)
- `drafts/long-form/` — Hacker News (write by hand), Habr, The Conversation pitch
- `drafts/facebook/` — page posts
- `drafts/` — single-file drafts for reddit, telegram, bluesky, discord, whatsapp, emails
- `drafts/TODO.md` — shared image preparation tasks across all platforms

## Never invent facts

Use only the figures in `project/PROJECT.md`. Never invent numbers, URLs, contact addresses, or citations. If the standing facts contradict what a live site says, report the contradiction instead of silently picking one.

## The approval gate is human-only

A post candidate is a Markdown file that moves through three folders:

```
candidates/pending/    you drafted it; nobody has reviewed it
candidates/approved/   a human moved it here - this move IS the approval
candidates/sent/       it went out and was logged in registry/shares.csv
```

You may write freely into `pending/`. **You may never move a file into `approved/`.** Only a human does that. You may act on a file already sitting in `approved/` (send it), and afterward you move it to `sent/`, fill in `platform_msg_id` and `permalink` in its frontmatter, and append a row to `registry/shares.csv`.

Nothing enters `shares.csv` until it has actually been sent. That table answers "what went out and how did it do" — a draft row in it is indistinguishable from a real one at a glance.

## Boost asks

`boost_ok` in `destinations.csv` says whether asking contacts to like or comment is safe:

- `yes` — normal in Facebook, Telegram, WhatsApp, Discord group contexts.
- `risky` — LinkedIn removes groups that show engagement-pod behaviour. Ask individuals, never reciprocally.
- `no-bannable` — Reddit, Hacker News, Product Hunt. Never record a boost ask against these. HN's rule penalises **sites** as well as accounts, so one incident can flag the project's domain.

## What every post should drive

Read `project/goals.md` before writing any post. The five goals in priority order: play the study, share a result card, recruit toward about 200 adults, take protocol-safe contributions, connect with diabetes / CGM / glucose-ML groups. Do not write posts that present Sugar-Sugar as a brochure, a knowledgebase, or a dosing app - those framings serve none of the five goals and two of them are false.

## Write as the project team

Posts should sound like the people named in `PROJECT.md` talking about something they made, not like detached popularisation, a press release, or an external reviewer describing the project. Start from the team's own curiosity and decisions: what interested us, why we made it this way, what exists now and where the work could go next. Use first-person language (`I` or `we`) and concrete project vocabulary. Preserve the speaker's characteristic informal phrasing when it sounds natural; correct grammar without replacing the voice with generic professional prose.

A first-person feature list is still detached. Build the post as a causal story, like a scientist walking a mixed audience through their own poster: what interested us -> why it mattered to us -> what we made -> what exists now -> why we chose this form -> what readers can do next. Adapt the steps to the post, but make each transition explain why the next part follows. Use ordinary links such as "because", "so", "as a result", "but we also wanted" or their natural equivalent in the post's language.

Before saving any team-authored draft, reduce it to a one-line causal spine and read it paragraph by paragraph. Each paragraph must answer a question or continue a thought raised by the previous one. If the paragraphs can be rearranged without changing the meaning, the draft is a feature list rather than a story and must be rewritten. This check is required even when the grammar and individual sentences already sound natural.

Do not automatically append generic third-person referral lines. A request to contribute or share is optional. When it belongs in the post, put it at the end, write it afresh for that room in the team's voice, and never reuse it as a mechanical sign-off.

## Varying text

One blurb per room, each genuinely different: different opening line, different fact led with, different sign-off. Never reuse a sentence across two rooms, even in different languages. Identical text across many chats is precisely the pattern that gets a personal Telegram account flagged. When suggesting send times, spread them across a day, hours apart.

## Automation honesty

`platform_rules.csv` has `automation`, `scheduling`, and `weekend_ok` columns. Respect them:

- **scheduling** — use native schedulers where available (LinkedIn, Telegram, Mastodon, newsletters). All scheduling is manual-trigger until tested.
- **weekend_ok** — LinkedIn engagement drops 40-60% on weekends; most other platforms are fine.
- WhatsApp is draft-only because it runs on a personal number.
- Hacker News is never automated and its text must be written by hand — no LLM, not even for editing.
- Third-party Discords are manual because bot-token integrations require adding a bot you cannot add.
- **LinkedIn official API only** (`get_my_profile`, `create_post`, `edit_post`, `delete_post`, `get_my_posts`, `get_my_post_analytics`). Never use unofficial or cookie-based tools (`search_people`, `get_profile`, `get_feed`, `send_message`, `search_companies`, and similar) — they rely on scraping and risk account restrictions.
- **LinkedIn groups have no API at all.** The Groups API was shut down in 2017 and never replaced; `w_member_social` reaches the personal feed and pages you admin, nothing else. No official API tool and no scheduler (Buffer included) can post into a group, and a company or showcase page cannot post in one either — only a member profile can. Group posts are typed into the group composer by a human or by a browser agent in a logged-in session, one at a time, unscheduled. Treat `platform=linkedin-group` rows the way you treat WhatsApp: draft in advance, send by hand. Details in `registry/linkedin-groups-catalogue.README.md`.

## Images

Each original LinkedIn post draft has an `image:` field in its frontmatter specifying the expected filename and what to screenshot. Images go next to their draft file. Reshare commentary references the source post and does not need separate media. No separate assets folder. Most platforms can reuse the same base screenshots cropped differently.

## Tracker spreadsheet

`scripts/sync_tracker.py` pushes every registry CSV and the live Buffer state
into one Google Spreadsheet, editing it **in place** through the Sheets API —
same file, same id, same link on every run. One tab per CSV, plus
`buffer_channels`, `buffer_queue` and `sync_status`.

```
uv run --no-project python scripts/sync_tracker.py --dry-run   # report only
uv run --no-project python scripts/sync_tracker.py             # write
```

Credentials, both gitignored and never committed:

- `keys/service.json` — Google service account with edit rights on the sheet
- `.env` — `TRACKER_SHEET_ID` (or `TRACKER_SHEET_TITLE`) and one `*_BUFFER_API_KEY` per Buffer account. On this branch the copied id is the enhancement.bio sheet; do not run a write sync until it is a Sugar-Sugar sheet.

The script discovers accounts by scanning `.env` for `*_BUFFER_API_KEY`, so
adding a Buffer account is a one-line change with no code edit.

`scripts/style_tracker.py` handles appearance and is deliberately **separate
and manual** — formatting lives on the cell grid, not on the values, so
`values.batchClear` leaves it intact and one run keeps working for every later
sync. Do not fold it into the scheduled job. Re-run it only after adding a tab
or a column:

```
uv run --no-project python scripts/style_tracker.py
```

Two traps it encodes, both found by looking at the rendered sheet rather than
the API response:

- A fixed row height silently defeats wrapping — the text wraps but the row
  stays one line tall and you read a clipped sentence. Rows are auto-resized
  *after* wrap strategies are set.
- Newlines inside a cell make Sheets grow the row even when the column is
  clipped, so a post body with a dozen paragraph breaks turns one row into a
  screenful. `sync_tracker.py` flattens breaks to ` ¶ ` on the way in; the real
  formatting stays in the CSV.

Post bodies (`text`, `text_sent`, `full_text`) are wide but clipped. Only
medium prose (`notes`, `self_promo_rule`, and similar) wraps.

`buffer_queue.in_shares_csv` reconciles what Buffer actually sent against
`shares.csv`. Match is attempted on post id, on permalink, and on the opening of
the post body — the third pass matters because LinkedIn hands Buffer a
`urn:li:share` id while the permalink a human copies carries a different
`urn:li:activity` number for the same post. A `NO - not logged` row means
something went out and was never recorded. Investigate it; never backfill
`shares.csv` automatically, because a wrong row there is worse than a gap.

## After changing the registry

Run `uv run --no-project python scripts/check_registry.py`. It catches duplicate ids, broken references, UTM values that will split into separate analytics rows, and boost asks recorded against rooms where asking is bannable. Fix what it names before finishing.
