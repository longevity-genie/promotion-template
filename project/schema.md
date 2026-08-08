# Schema

Every column in every registry file. CSV is the source of truth; `scripts/build_workbook.py` generates a spreadsheet view from it, and `scripts/check_registry.py` validates the constraints marked **enforced** below.

Ids are lowercase-hyphenated slugs throughout. Dates are `YYYY-MM-DD`.

---

## `destinations.csv`

The registry of communities. The most valuable file here, because the research behind each row — what the room's rules actually say — doesn't expire when a campaign ends.

| Column | Meaning |
|---|---|
| `dest_id` | Unique slug. **Enforced:** unique, slug format. |
| `scope` | `template` = generic, maintained upstream, arrives via `git merge upstream/main`. `local` = yours, never conflicts on merge. **Enforced:** one of the two. |
| `platform` | Must match a `platform` in `platform_rules.csv`. **Enforced.** |
| `name` | Human-readable room name. |
| `handle_or_url` | Where to find it. |
| `platform_chat_id` | Numeric Telegram chat id or WhatsApp JID. Without it, nothing about this room can be automated later. |
| `utm_source` | The room's tracking slug. **Enforced:** unique across rooms, lowercase-hyphen. Reuse merges two rooms' clicks into one indistinguishable row. |
| `category` | Topic cluster, used to enforce diversity when selecting rooms. |
| `language` | `en`, `ru`, `ro`, `de`, or a combination like `ru/en`. |
| `size` | Approximate membership. Rough is fine; it's for prioritising. |
| `tier` | `1` = post here first, `2` = good, `3` = marginal. Drives selection order. |
| `measurable` | `yes` if metrics can be pulled automatically (Telegram supergroups/channels, LinkedIn). `no` means manual forever. **Enforced:** yes/no. |
| `boost_ok` | `yes` / `risky` / `no-bannable` — whether asking contacts to engage is safe. **Enforced.** |
| `self_promo_rule` | The room's actual written rule, quoted where possible. An agent reads this before drafting. Blank triggers a warning. |
| `cap_days` | Minimum days between posts here. Respect it or you're the person who spams this room. |
| `link_target` | `pillar` / `post` / `repo` / `none` — what to link. See `registry/utm_convention.md`. |
| `admin_contact` | Modmail, admin handle, or email, for rooms where asking first is the right move. |
| `last_posted` | Updated automatically by prompt `40`. Compared against `cap_days`. |
| `status` | `active` / `comment-only` / `on-hold` / `retired`. Only `active` rooms get selected. |
| `notes` | Anything that changes how you post here. Known audience overlaps with other rooms go here. |

**On `status`:** prefer `retired` over deleting a row. A room that's wrong today may suit a later pillar, and the rule research stays useful either way. `comment-only` means participate but never post — the honest state for several science subreddits. `on-hold` means you are not ready to post yet — a missing asset, a print photo, an STL file, a pending approval. Put the release condition in `notes`. It is not the same as moderation action; if moderators banned you, note that separately.

---

## `platform_rules.csv`

Per-platform constraints. One row per platform; `destinations.platform` references it.

| Column | Meaning |
|---|---|
| `platform` | The key. **Enforced:** referenced by destinations. |
| `max_length` | Hard character limit, or "no limit". |
| `tone` | The register that works on this platform. |
| `media` | What media the platform actually rewards. |
| `hashtags` | How many, and whether they help. Varies enormously — 3-4 drive real discovery on Bluesky; stuffing them on Facebook restricts your reach. |
| `link_behaviour` | What actually happens to reach when a post contains a link. Much folklore here; this column holds only what a platform's own documentation says. |
| `automation` | What can genuinely be automated. Respect it. |
| `key_rule_to_remember` | The one thing that will bite you. |

---

## `pillars.csv`

Long-form canonical assets. One or two a month at most.

| Column | Meaning |
|---|---|
| `pillar_id` | Unique slug. |
| `title` | Working title. |
| `format` | `long-form-article` / `show-hn` / `blog` / `preprint` / `the-conversation` / `habr`. |
| `language` | Primary language. |
| `thesis_one_line` | The single claim. If you can't write it in one line, it isn't a pillar yet. |
| `key_facts_to_include` | Semicolon-separated, drawn from the standing facts. |
| `assets_needed` | Images, video, diagrams required before publishing. |
| `owner` | Who writes it. |
| `status` | `idea` / `drafted` / `published`. |
| `target_date` | Intended publish date. |
| `published_url` | Fill on publication; this is what most candidates link to. |
| `utm_campaign` | Campaign slug. Every share of this pillar carries it, which is how rooms get compared fairly. |
| `notes` | |

---

## `derivatives.csv`

Platform-native posts made from a pillar. Three to five per pillar.

| Column | Meaning |
|---|---|
| `deriv_id` | Unique slug. |
| `pillar_id` | Parent pillar. **Enforced:** must exist. |
| `platform` | Target platform. |
| `voice` | Which team member's voice, matching `PROJECT.md`. |
| `language` | |
| `variant_label` | The angle in a few words, e.g. `object-first` vs `method-first`. |
| `full_text` | The post as it will be published. |
| `media_needed` | |
| `status` | `drafted` / `published`. |
| `scheduled_local_time` | |
| `published_url` | |
| `platform_post_id` | The URN or id. Required for automatic analytics. |
| `notes` | |

---

## `shares.csv`

One row per post **actually sent**. Nothing enters this file until it has gone out — a draft row is indistinguishable from a real one when scanning, which quietly corrupts every conclusion you draw from the table.

| Column | Meaning |
|---|---|
| `share_id` | Unique slug, e.g. `shr-0042`. **Enforced:** unique. |
| `dest_id` | Which room. **Enforced:** must exist. |
| `deriv_id`, `pillar_id` | What was shared. **Enforced:** must exist if given. |
| `sender` | Who actually sent it. |
| `language` | |
| `date_sent` | **Enforced:** `YYYY-MM-DD`. |
| `status` | `sent` / `measured` / `removed-by-mods`. |
| `text_sent` | The exact text. Keep it — it's how you learn which phrasing worked. |
| `link_used` | The full tagged URL. |
| `utm_source`, `utm_medium`, `utm_campaign` | Per `utm_convention.md`. |
| `utm_content` | **Enforced: must equal `share_id`.** This equality is what makes one click traceable to one post in one room. |
| `platform_msg_id` | Telegram message id or LinkedIn URN. Capture at send time or lose it. |
| `permalink` | Direct link to the post. Telegram can only produce these for supergroups and channels. |
| `boost_asked_who`, `boost_asked_date` | Who you asked to engage. **Enforced:** must be empty where `boost_ok=no-bannable`. |
| `measure_after` | Defaults to `date_sent + 7 days`. Prompt `50` sweeps everything past this date. |
| `reactions`, `comments`, `clicks` | Fill at measurement. |
| `outcome` | `worked` / `ok` / `flat` / `negative` / `too-early`. A judgement, not a metric — see below. |
| `notes` | |

**`outcome` is deliberately not computed from the numbers.** `worked` means the post produced something you actually wanted: a contributor, a real conversation, a curator getting in touch, meaningful traffic. Fifty reactions and no downstream effect is `flat`. Optimising for reaction counts is how people end up with popular posts and no project.
