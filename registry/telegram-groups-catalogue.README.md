# Telegram groups catalogue

`telegram-groups-catalogue.csv` is the durable research inbox for Telegram
communities available to the posting account. It is deliberately broader than
`destinations.csv`: it records writable groups, admin-only channels and their
linked discussion chats, already-used rooms, dead rooms and false positives.

This is **not** a list of rooms that are automatically safe to post in. Only a
row in `destinations.csv` with `status=active` is selectable for a new draft.

Public Telegram search is not a membership inventory. It misses most useful
private and linked rooms. Page the account's own chat list.

## Columns

| Column | Meaning |
|---|---|
| `chat_id` | Stable Telegram id. Supergroups and channels normally begin with `-100`; old basic groups use shorter negative ids. |
| `name` | Title shown by Telegram on the check date. |
| `username_or_url` | Public route where one exists. Blank means private. |
| `chat_type` | `supergroup`, `basic-group`, or `channel`. A normal member cannot post to a channel. |
| `category` | Topic cluster used for campaign diversity. |
| `relevance` | `A` core fit, `B` good, `C` marginal/context-dependent, `D` skip. |
| `member` | Whether the connected account can access the room. |
| `size` | Participant or subscriber count observed on `checked_at`. |
| `last_activity` | Date of the latest visible message when checked. |
| `language` | Main language or languages. |
| `writable` | `yes`, `no`, or `admin-only`. This prevents a large channel from being mistaken for a member-post destination. |
| `linked_chat_id`, `linked_chat_name` | The corresponding channel or discussion. The visible channel may be large while the writable discussion has a different id and audience size. |
| `self_promo_rule` | The actual written rule or the honest absence of one. This is still the posting gate. |
| `prior_project_post` | Exact historical result, including date and message id where available. Read this before drafting. |
| `status` | `candidate`, `promoted`, `posted`, `hold`, `admin-pitch`, `reference-only`, or `skip`. |
| `notes` | Why the room is or is not useful and how to approach it. |
| `checked_at` | When metadata and history were last inspected. |

## How to use it

1. Filter to `status=candidate` or revisit a justified `hold` row.
2. Re-read the room description, current pins and recent messages: rules and
   culture can change after `checked_at`.
3. Search the room history for the live URL and the current project name.
   Do not rely only on Telegram's fuzzy search; verify that the returned
   message actually contains the domain or project name.
4. Promote the room to `destinations.csv` only after the posting rule and the
   correct writable `chat_id` are known. Mark `scope=local`.
5. After a real send, update `prior_project_post` here, move the candidate
   to `candidates/sent/`, append `shares.csv`, and update
   `destinations.last_posted`.

## Findings that keep recurring

- Subscriber count and writable audience are different. A channel with tens
  of thousands of subscribers may have a discussion of a few hundred.
- Large numbers do not override audience fit. Crypto or jobs rooms that
  share a keyword are still the wrong room.
- Rooms you have already posted in must not be presented later as untouched
  audiences. That is what `prior_project_post` is for.
