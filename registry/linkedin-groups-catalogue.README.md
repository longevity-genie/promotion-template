# LinkedIn groups catalogue

`linkedin-groups-catalogue.csv` is the research inbox for LinkedIn Groups, harvested 2026-08-11 from
Anton's own group memberships (53 joined, read from `linkedin.com/groups` by paging the
"Show more results" control) plus keyword sweeps of LinkedIn group search for
`transhumanism`, `gene therapy`, `CRISPR genome editing`, `synthetic biology`,
`longevity aging`, and `human enhancement augmentation`.

It is **not** a destination list. Nothing here is ready to post to.

## Read this first: LinkedIn has no Groups API

The LinkedIn Groups API was shut down in 2017 and never replaced. The official
API this repo is authorised for (`w_member_social`) can post to **your own feed** and to
**pages you admin** - nothing else. There is no group scope, no group endpoint, and no
third-party scheduler (Buffer included) that can put a post inside a LinkedIn group.

Consequences for this repo:

- Group posts are **browser-only**. They are typed into the group's own composer, by a
  human or by a browser-automation agent driving a logged-in session.
- They **cannot be scheduled**. The clock icon in the LinkedIn composer does not appear
  inside a group composer.
- A **showcase page cannot post in a group.** Only member profiles can. The old
  `destinations.csv` note on `li-showcase` saying "use for LinkedIn groups" was wrong and
  has been corrected.
- Nothing in `platform_rules.csv` about LinkedIn automation applies to groups. The
  `linkedin` row's `automation: full (official API)` is true for the personal feed and the
  showcase page **only**.

## Columns

| Column | Meaning |
|---|---|
| `group_id` | Numeric LinkedIn group id - the stable identifier. Goes into `destinations.platform_chat_id`. |
| `name` | Group name as LinkedIn shows it. |
| `url` | `https://www.linkedin.com/groups/<group_id>/` |
| `category` | Topic cluster: `transhumanism` `gene-therapy` `gene-editing` `genomics` `synthetic-biology` `longevity` `bioinformatics` `clinical` `design` `other`. |
| `relevance` | `A` core fit · `B` good · `C` marginal · `D` off-topic, skip. |
| `member` | `yes` Anton is already in · `NO - join first` · `NO`. |
| `size` | Member count read from the LinkedIn group record on 2026-08-11. |
| `visibility` | `Public group` (posts visible off LinkedIn and indexable) or `Private Listed` / `Private Group` (members only). |
| `post_approval` | `YES` means member posts land in an admin queue before appearing. Budget days, not minutes. |
| `activity_observed` | Ages of the most recent visible posts on 2026-08-11. Blank/`not sampled` where not checked. |
| `self_promo_rule` | The group's actual written rule, quoted. **This is the gate.** |
| `status` | `uncontacted` / `promoted` (has a row in `destinations.csv`) / `rejected`. |

## What the sweep found

**The H+ vertical barely exists on LinkedIn.** The largest explicitly transhumanist group
is `h+ Community` at 1,162 members, and Anton has been in it since September 2009. The
next largest is 348 members. Everything else is under 300, several are single-digit, and
one 401-member group (`CASCTT`) is organised *against* transhumanism. Treat LinkedIn as a
place to reach genetics and gene-therapy professionals; Telegram, Facebook and Reddit
remain the H+ surfaces.

**Gene therapy is the opposite.** Six groups over 7,000 members, the largest at 48,529.
Anton is in exactly one of them (`Genetics Network`, 5,848). The rest need a join request
first, and the biggest ones are `Private Listed`, so joining is admin-gated.

**Only one group in the whole sweep publishes written rules** in LinkedIn's rules field:
none of them do. `Genetics and Genomics` (106,226) carries its rule in a pinned admin
post instead, and it is the sharpest one found - it threatens deletion and blocking for
spam while explicitly welcoming articles and peer-reviewed papers. That is the rule to
write to, because it is the one group in the set large enough to matter and strict enough
to punish a mistake.

## Relevance split

- **A - 12 groups.** 6 Anton is already in, 6 need a join request. Promoted to
  `destinations.csv` as `status=on-hold`, `tier=1`.
- **B - 14 groups.** Second wave.
- **C - 17 groups.** Adjacent. Comment-only territory, or one post much later.
- **D - 14 groups.** Off-topic, hostile, dead, or jobs boards. Do not post.

## Promoting a row to `destinations.csv`

1. Open the group. Read the rules tab **and the pinned posts** - on LinkedIn the rule is
   almost always in a pin, not in the rules field.
2. Fill `self_promo_rule` here with the rule **quoted**, plus `visibility` and
   `post_approval`.
3. Copy across as a `destinations.csv` row (`scope=local`, `platform=linkedin-group`,
   `platform_chat_id=group_id`, `utm_source=dest_id`).
4. Flip `status` to `active` only once the rule is recorded. Set `status` here to `promoted`.
5. Run `python scripts/check_registry.py`.

## LinkedIn-group-specific cautions

- `boost_ok=risky` for every row. LinkedIn removes groups that show engagement-pod
  behaviour. Ask individuals to comment, never reciprocally, never in a batch.
- `cap_days=30`. The genetics rooms overlap heavily in membership - `Genetics and
  Genomics`, `Human Genetics`, `AI and Genetics` and `Genetics Network` share a lot of the
  same people. Posting the same pillar to all four inside a week reads as spam to the
  overlap even if no single group's rules are broken.
- **Space the sends.** One group per day at most, and vary the opening line and the fact
  you lead with. This is the same rule as Telegram and for the same reason.
- **`post_approval=YES` groups swallow posts silently.** Check back after 48h; if it never
  appears, do not repost - message the admin.
- A post inside a **private** group is invisible to everyone outside it and cannot be
  reshared to a feed. Only `Public group` posts (here: `Genetics Network`, both
  Bioinformatics groups) are worth a UTM-tracked link for reach reasons; in private groups
  the UTM is still worth it for attribution.
