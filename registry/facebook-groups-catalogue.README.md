# Facebook groups catalogue

`facebook-groups-catalogue.csv` is the research inbox for Facebook groups.
Harvest from your own memberships and from keyword search. It is **not** a
destination list. Nothing here is ready to post to.

| Column | Meaning |
|---|---|
| `group_id` | Numeric Facebook group id — the stable identifier. Goes into `destinations.platform_chat_id`. |
| `name` | Group name as Facebook shows it. |
| `url` | `https://www.facebook.com/groups/<group_id>/` |
| `category` | Topic cluster. |
| `relevance` | `A` core fit · `B` good · `C` marginal · `D` off-topic, skip. |
| `language`, `size` | Blank until someone opens the group and fills them in. |
| `self_promo_rule` | Blank until someone reads the pinned rules. **This is the gate.** |
| `status` | `uncontacted` / `promoted` (has a row in `destinations.csv`) / `rejected`. |

## Promoting a row to `destinations.csv`

1. Open the group, read the pinned post and the rules tab.
2. Fill `self_promo_rule` here with the rule **quoted**, plus `language` and `size`.
3. Copy across as a `destinations.csv` row (`scope=local`, `platform=facebook`,
   `platform_chat_id=group_id`, `utm_source=dest_id`).
4. Flip `status` to `active` only once the rule is recorded. Set `status` here to `promoted`.
5. Run `python scripts/check_registry.py`.

`on-hold` in `destinations.csv` means you are not ready to post yet. That is
the right state for rooms you have identified but whose rules you have not
read. Do not flip one to `active` while `self_promo_rule` still says
`UNVERIFIED`.

## Facebook-specific cautions

- `boost_ok=yes` — asking contacts to like or comment is normal on Facebook.
- Several groups often share an audience. Posting the same pillar across all
  of them inside a week reads as spam to the people in the overlap, not to
  the algorithm. Use a long `cap_days` (30 is a safe default).
- Facebook suppresses reach on posts with outbound links. Link in the first
  comment, or native media with the link in the caption.
