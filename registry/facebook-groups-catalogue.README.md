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

## 2026-08-27 sweep: diabetes and CGM rooms

55 rows added from Facebook group search in a logged-in session, queried in EN/RO/UK/RU:
`continuous glucose monitoring`, `type 1 diabetes`, `dexcom`, `freestyle libre`,
`nightscout looped diabetes`, `type 2 diabetes support`, `diabet zaharat`,
`цукровий діабет`, `сахарный диабет 1 типа`. Four existing rows were re-checked and
their member counts corrected (the Libre CGM room had grown 43.6K to 50.2K, the CGM
support group 4.8K to 7.1K).

Ten A-tier rooms were opened and their rules read; those rows carry `VERIFIED 2026-08-27`
and either the quoted rule or an explicit "publishes NO rules" statement. Everything
else is `UNVERIFIED` and stays that way until someone opens it.

**The finding that matters: almost every large diabetes room bans self-promotion outright.**
Dexcom G7 Issues (95.4K), Type 1 Diabetes Support & Awareness (48.7K), Omnipod & Dexcom
(31.4K), the CGM support group (7.1K) and the Romanian Prediabet room (31.2K) all carry a
near-identical rule: "Self-promotion, spam and irrelevant links aren't allowed." Posting a
study link into any of them without asking first gets the post removed and the account
flagged. The route into these rooms is an admin message describing the ethics approval and
the recruitment goal, and asking permission - not a post.

Two exceptions are worth knowing:

- **FreeStyle Libre 3** (31.5K, private) publishes four rules and none of them ban
  self-promotion; the binding rule is "stay on topic". It is the best first-post candidate
  on Facebook.
- Several rooms - FreeStyle Libre CGM System (50.2K), Dexcom G7 (50K), and both Ukrainian
  rooms - publish **no rules at all**. That is not permission. Ask the admin.

**Language coverage.** Romanian is the deepest non-English vertical found (six rooms over
20K, led by Noisidiabetul at 25.9K, which is T1D-specific and the natural room for Livia to
post in her own voice). Ukrainian rooms exist but are small - the largest CGM-specific one
is 1.1K. Russian has one very large room, Жизнь с Диабетом at 230.3K, but its own rules
make it a recipe group where medical topics are pushed out, so it is filed `C` despite the
size. Do not let member count override the rules text.

**Rooms deliberately filed C or D.** Parent and children's groups (TYPE 1 PARENTS, Kids
With Type 1 Diabetes) are off-limits for recruitment because the study is 18+. Recipe
groups (Вкусные рецепты для диабетиков) are off-topic by their own rules. They are listed
so nobody re-discovers them and mistakes size for fit.
