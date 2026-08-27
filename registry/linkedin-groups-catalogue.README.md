# LinkedIn groups catalogue

`linkedin-groups-catalogue.csv` is the research inbox for LinkedIn Groups.
Harvest from your own memberships and from keyword search. It is **not** a
destination list. Nothing here is ready to post to.

## Read this first: LinkedIn has no Groups API

The LinkedIn Groups API was shut down in 2017 and never replaced. The official
API this repo is authorised for (`w_member_social`) can post to **your own feed**
and to **pages you admin** — nothing else. There is no group scope, no group
endpoint, and no third-party scheduler (Buffer included) that can put a post
inside a LinkedIn group.

Consequences:

- Group posts are **browser-only**. They are typed into the group's own
  composer, by a human or by a browser-automation agent driving a logged-in
  session.
- They **cannot be scheduled**. The clock icon in the LinkedIn composer does
  not appear inside a group composer.
- A **company or showcase page cannot post in a group.** Only member profiles
  can.
- Nothing in the `linkedin` row of `platform_rules.csv` about automation
  applies to groups. That row is true for the personal feed and pages you
  admin **only**.

## Columns

| Column | Meaning |
|---|---|
| `group_id` | Numeric LinkedIn group id — the stable identifier. Goes into `destinations.platform_chat_id`. |
| `name` | Group name as LinkedIn shows it. |
| `url` | `https://www.linkedin.com/groups/<group_id>/` |
| `category` | Topic cluster. |
| `relevance` | `A` core fit · `B` good · `C` marginal · `D` off-topic, skip. |
| `member` | `yes` you are already in · `NO - join first` · `NO`. |
| `size` | Member count when last checked. |
| `visibility` | `Public group` (posts visible off LinkedIn and indexable) or `Private Listed` / `Private Group`. |
| `post_approval` | `YES` means member posts land in an admin queue before appearing. Budget days, not minutes. |
| `activity_observed` | Ages of the most recent visible posts. Blank / `not sampled` where not checked. |
| `self_promo_rule` | The group's actual written rule, quoted. **This is the gate.** |
| `status` | `uncontacted` / `promoted` (has a row in `destinations.csv`) / `rejected`. |

On LinkedIn the rule is almost always in a **pinned admin post**, not in the
rules field. Read both.

## Promoting a row to `destinations.csv`

1. Open the group. Read the rules tab **and the pinned posts**.
2. Fill `self_promo_rule` here with the rule **quoted**, plus `visibility` and
   `post_approval`.
3. Copy across as a `destinations.csv` row (`scope=local`,
   `platform=linkedin-group`, `platform_chat_id=group_id`,
   `utm_source=dest_id`).
4. Flip `status` to `active` only once the rule is recorded. Set `status`
   here to `promoted`.
5. Run `python scripts/check_registry.py`.

## LinkedIn-group-specific cautions

- `boost_ok=risky` for every row. LinkedIn removes groups that show
  engagement-pod behaviour. Ask individuals to comment, never reciprocally,
  never in a batch.
- Overlapping rooms (same topic, shared members) need a long `cap_days`.
  Posting the same pillar to four related groups inside a week reads as spam
  to the overlap even if no single group's rules are broken.
- Space the sends. One group per day at most, and vary the opening line and
  the fact you lead with. Same rule as Telegram, same reason.
- `post_approval=YES` groups swallow posts silently. Check back after 48h; if
  it never appears, do not repost — message the admin.
- A post inside a **private** group is invisible outside it and cannot be
  reshared to a feed. The UTM is still worth it for attribution.
