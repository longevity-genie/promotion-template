# Candidates: pending -> approved -> sent

A candidate is one post, for one community, as a single Markdown file. This folder is the review queue — it exists so that approving a post means reading a file and moving it, rather than opening a spreadsheet and scanning a text column.

## The three folders

**`pending/`** — an agent drafted this. It is not approved and will not be sent. Agents write here freely (prompt `30`).

**`approved/`** — a human read the file and moved it here. **That move is the approval.** There is no status field to set, no checkbox. Edit the text directly before moving it if it needs changes.

**`sent/`** — it went out. An agent moved it here after sending, having filled in the two ID fields below and appended a row to `registry/shares.csv`.

**The rule that makes this a real gate:** only a human moves a file from `pending/` to `approved/`. An agent may act on anything already in `approved/`, but never approves its own draft.

## File format

Named `<YYYY-MM-DD>-<platform>-<dest_id>.md`, e.g. `2026-08-10-reddit-rd-generative.md`.

```markdown
---
dest_id: rd-generative
platform: reddit
language: en
pillar_id: p01
deriv_id: d03
utm_source: rd-generative
utm_medium: community
utm_campaign: my-campaign-slug
utm_content:                    # filled at send time - equals the new share_id
link_used: https://example.org/?utm_source=rd-generative&utm_medium=community&utm_campaign=my-campaign-slug&utm_content=
suggested_send_time: 2026-08-10T14:00
boost_ok: no-bannable
media_needed: photo of the printed object
status: pending
platform_msg_id:                # filled at send time
permalink:                      # filled at send time
---

The post text goes here, exactly as it will be pasted or sent. Nothing above the
second `---` is ever sent - it's metadata for the agent and for the registry row
this candidate becomes once it goes out.
```

Keep `dest_id` and the `utm_*` values consistent with `registry/destinations.csv` and `registry/utm_convention.md`.

## What happens at each step

1. **Drafted** (prompt `30`) — an agent reads a pillar or derivative plus `destinations.csv`, then writes one file per targeted room into `pending/` with `status: pending`. Nothing goes into `shares.csv` yet: an unsent draft has no place in a table of things that were sent.
2. **Approved** — a human moves the file to `approved/`, editing the body first if needed. No agent action.
3. **Sent** (prompt `40`) — the sender reports what went out. An agent fills in `platform_msg_id` and `permalink`, sets `status: sent`, appends a row to `registry/shares.csv` with a fresh `share_id` (and `utm_content` equal to it), updates `last_posted` on the destination, and moves the file to `sent/`.
4. **Measured** (prompt `50`) — the `shares.csv` row gets reactions, comments, clicks, and an outcome. The file in `sent/` never changes again; it's the fixed record of what was actually said.

## Capture the IDs at send time

`platform_msg_id` and `permalink` are the only things that make later measurement automatic — Telegram reaction counts and LinkedIn post analytics both need them. Once a message scrolls away in a busy room, recovering its ID by hand is tedious enough that it won't happen. Capture them at the moment of sending or accept that the room's numbers stay manual forever.

Telegram permalinks only exist for supergroups and channels; basic groups can't produce them. The `measurable` column in `destinations.csv` records which of your rooms can.
