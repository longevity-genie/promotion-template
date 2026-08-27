# Telegram groups catalogue

`telegram-groups-catalogue.csv` is the durable research inbox for Telegram
communities available to Anton. It is deliberately broader than
`destinations.csv`: it records writable groups, admin-only channels and their
linked discussion chats, already-used rooms, dead rooms and false positives.

The first inventory was made on 2026-08-25 by paging all 1,554 chats visible to
the connected Telegram account: 16 pages at 100 chats per page, with 54 chats
on the final page. Every title in that inventory was screened for
transhumanism, immortalism, cryonics, longevity, biohacking, genetic design,
bioinformatics, futurism, network states and directly adjacent science/art
communities. Strong matches and their linked discussions were then inspected
individually for type, size, latest activity, description, pins and previous
mentions of `enhancement.bio`.

This file was copied onto the `sugar` branch as a membership inventory.
`prior_project_post` still records enhancement.bio history, not Sugar-Sugar
sends. Add a Sugar-Sugar note in `notes` when a room is used for this study.

This is **not** a list of rooms that are automatically safe to post in. Only a
row in `destinations.csv` with `status=active` is selectable for a new draft.

## Columns

| Column | Meaning |
|---|---|
| `chat_id` | Stable Telegram id. Supergroups and channels normally begin with `-100`; old basic groups use shorter negative ids. |
| `name` | Title shown by Telegram on the check date. |
| `username_or_url` | Public route where one exists. Blank means private. |
| `chat_type` | `supergroup`, `basic-group`, or `channel`. A normal member cannot post to a channel. |
| `category` | Topic cluster used for campaign diversity. |
| `relevance` | `A` core fit, `B` good, `C` marginal/context-dependent, `D` skip. |
| `member` | Whether Anton's connected account can access the room. |
| `size` | Participant or subscriber count observed on `checked_at`. |
| `last_activity` | Date of the latest visible message when checked. |
| `language` | Main language or languages. |
| `writable` | `yes`, `no`, or `admin-only`. This prevents a large channel from being mistaken for a member-post destination. |
| `linked_chat_id`, `linked_chat_name` | The corresponding channel or discussion. These two fields are crucial in Telegram, where the visible channel may be large while the writable discussion has a different id and audience size. |
| `self_promo_rule` | The actual written rule or the honest absence of one. This is still the posting gate. |
| `prior_enhancement_post` | Exact historical result, including date and message id where available. Read this before drafting. |
| `status` | `candidate`, `promoted`, `posted`, `hold`, `admin-pitch`, `reference-only`, or `skip`. |
| `notes` | Why the room is or is not useful and how to approach it. |
| `checked_at` | When metadata and history were last inspected. |

## How to use it

1. Filter to `status=candidate` or revisit a justified `hold` row.
2. Re-read the room description, current pins and recent messages: rules and
   culture can change after `checked_at`.
3. Search the room history for `enhancement.bio`, `Materialized Enhancements`
   and the current project phrasing. Do not rely only on Telegram's fuzzy
   search result; verify that the returned message actually contains the
   domain or project name.
4. Promote the room to `destinations.csv` only after the posting rule and the
   correct writable `chat_id` are known.
5. After a real send, update `prior_enhancement_post` here, move the candidate
   to `candidates/sent/`, append `shares.csv`, and update
   `destinations.last_posted`.

## Important findings from the first inventory

- Public Telegram search is not a membership inventory. It missed most of the
  useful private and linked rooms in this account.
- Subscriber count and writable audience are different. For example,
  `Путь долгожителя` has 20,680 channel subscribers, while its writable
  discussion has 1,832 members. `Трансгуманизм в далеком городе` has 4,347
  subscribers, while `Транспозоны` has 766 members and explicitly allows
  participants to publish project/channel messages.
- `Transhuman Coin Official Group` has 10,602 members but is a cryptocurrency
  community, not useful transhumanist reach. Large numbers do not override
  audience fit.
- Historical checks found prior Anton posts in `BiohackerDAO`,
  `Bioinformatics UA`, `Mathematics in aging`, `(sci)Berloga` and the Ukrainian
  `Трансгуманісти` group, plus discussion-thread mentions in `Транспозоны`.
  These rooms must not be presented later as untouched audiences.
