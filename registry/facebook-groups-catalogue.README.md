# Facebook groups catalogue

`facebook-groups-catalogue.csv` is the research inbox for Facebook, harvested 2026-08-11 from
Anton's own group memberships (500 joined; 160 recovered — Facebook's "All groups you've joined"
grid hard-caps at 20 and will not paginate, so the list was mined through the in-sidebar
group-search typeahead with ~150 keyword probes in EN/UK/RU/RO).

It is **not** a destination list. Nothing here is ready to post to.

| Column | Meaning |
|---|---|
| `group_id` | Numeric Facebook group id — the stable identifier. Goes into `destinations.platform_chat_id`. |
| `name` | Group name as Facebook shows it. |
| `url` | `https://www.facebook.com/groups/<group_id>/` |
| `category` | Topic cluster. |
| `relevance` | `A` core fit for Materialized Enhancements · `B` good · `C` marginal · `D` off-topic, skip. |
| `language`, `size` | Blank until someone opens the group and fills them in. |
| `self_promo_rule` | Blank until someone reads the pinned rules. **This is the gate.** |
| `status` | `uncontacted` / `promoted` (has a row in `destinations.csv`) / `rejected`. |

## Relevance split

- **A — 46 groups.** Promoted to `destinations.csv` as `status=on-hold`, `tier=1`.
- **B — 46 groups.** Good second wave. Promote after the A tier has produced signal.
- **C — 32 groups.** Adjacent (neuroscience, open data, EA, clinical research). Comment-only territory.
- **D — 36 groups.** Off-topic (local Romanian/Ukrainian community, sport, space, generic AI). Do not post.

## Promoting a row to `destinations.csv`

1. Open the group, read the pinned post and the rules tab.
2. Fill `self_promo_rule` here with the rule **quoted**, plus `language` and `size`.
3. Copy across as a `destinations.csv` row (`scope=local`, `platform=facebook`,
   `platform_chat_id=group_id`, `utm_source=dest_id`).
4. Flip `status` to `active` only once the rule is recorded. Set `status` here to `promoted`.
5. Run `python scripts/check_registry.py`.

## Why the 46 A-tier rows are `on-hold`, not `active`

`on-hold` in `schema.md` means "we are not ready to post yet", release condition in `notes` —
which is exactly the situation: the rooms are identified but nobody has read their rules.
Their `self_promo_rule` reads `UNVERIFIED - read the group rules before the first post`.
Do not flip one to `active` without replacing that string with the group's actual rule.

## Facebook-specific cautions

- `boost_ok=yes` for all of these — asking contacts to like/comment is normal on Facebook.
- `cap_days=30` is a deliberate default. Several of these rooms share an audience almost
  entirely (the ILA cluster, the four Longevity country groups, the four Ukrainian
  pop-biology groups). Posting the same pillar across all of them inside a week reads as spam
  to the people in the overlap, not to the algorithm.
- Facebook suppresses reach on posts with outbound links. Link in the first comment, or native
  media with the link in the caption. See `drafts/facebook/README.md`.
