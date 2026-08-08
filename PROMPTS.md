# Prompt pack

Copy-paste prompts. Each is self-contained and works in **Claude Cowork** or **OpenAI Codex** without modification. Run them from the repo root; `AGENTS.md` is picked up automatically by both.

**Every prompt inherits these rules.** Restate them if an agent seems to be ignoring one:

0. Resolve paths relative to the repo root. Never accept or write an absolute path.
1. Read `project/PROJECT.md` and `project/copy-pack.md` before drafting a word. If they still contain `<...>` placeholders, stop and say so.
2. Never invent a number, URL, contact address, or citation. Use only the standing facts.
3. Check `registry/platform_rules.csv` for the platform and the destination's own `self_promo_rule` before writing for any room.
4. A draft is a file in `candidates/pending/`. It never goes into `registry/shares.csv` until actually sent.
5. **Only a human moves a file into `candidates/approved/`.** Never do it yourself.
6. Never record a boost ask where `boost_ok` is `no-bannable`.
7. Run `python scripts/check_registry.py` after changing any CSV, and fix what it reports.

---

## 00 — Orientation (run once, first)

```
Read this repo and report. Do not change anything.

1. Read project/PROJECT.md. Is it filled in, or does it still have <...> placeholders?
   List anything still unfilled - I cannot draft until those are real.
2. Read registry/destinations.csv. Break the rooms down by platform and tier. How many are
   status=active vs on-hold/comment-only/retired? Which have measurable=no, so I know where
   measurement will always be manual?
3. Which rooms have boost_ok=no-bannable, so I never ask anyone to engage there?
4. Count files in candidates/pending/ and candidates/approved/ - what is waiting on me?
5. Run python scripts/check_registry.py and report what it says.
6. Tell me anything that looks stale, inconsistent, or self-contradictory.
```

---

## 10 — Draft a pillar

```
Draft a new pillar asset.

Topic: <one line>
Format: <long-form-article | show-hn | blog | preprint | the-conversation | habr>
Language: <en | ru | ro | de>

Steps:
1. Read project/PROJECT.md for standing facts, voice rules, forbidden words, team voices,
   and the goal priority order. Read project/copy-pack.md for register and voice samples.
2. Read registry/pillars.csv - do not duplicate an existing thesis.
3. Draft it. One clear thesis. Only facts from the standing facts table; flag anything you
   would need me to verify rather than filling the gap yourself.
4. IF the format is show-hn: DO NOT WRITE IT. Output a structure and a fact list instead, and
   tell me plainly that Hacker News text must be hand-written - no LLM, not even for editing.
5. Append a row to registry/pillars.csv: new pillar_id, thesis_one_line, key_facts_to_include,
   assets_needed, owner, status=drafted, and a utm_campaign slug (lowercase-hyphenated,
   starting with the project's campaign prefix).
6. Run scripts/check_registry.py.

Print the full draft in chat as well as writing the row.
```

---

## 20 — Derive platform posts from a pillar

```
Turn pillar <PILLAR_ID> into platform-native posts.

Steps:
1. Read the pillar row, project/PROJECT.md, project/copy-pack.md, and registry/platform_rules.csv.
2. Write one post for each of: linkedin (in each team voice that genuinely fits this pillar's
   angle), bluesky, facebook. Add x-twitter only if I explicitly ask.
3. Respect each platform's max_length and hashtag norms. Bluesky is 300 characters INCLUDING
   the tag block - count them and show the count.
4. Each post must stand alone. Someone who never clicks the pillar should still get the point.
5. Do not let two voices blur into one. If two people post about the same pillar, the difference
   between them should be obvious from the first line.
6. Append one row per post to registry/derivatives.csv with full_text, media_needed, voice,
   status=drafted, and a variant_label naming the angle.
7. Run scripts/check_registry.py.

Print every post ready to paste. Do not write per-room blurbs here - that is prompt 30.
```

---

## 30 — Draft candidates for specific rooms

```
Draft this week's per-room candidates, based on <PILLAR_ID or DERIV_ID>.

Number of rooms to target: <N, default 4>

Steps:
1. Read registry/destinations.csv. Choose N rows with status=active, preferring tier 1, then 2,
   then 3. Skip any room whose last_posted is more recent than its cap_days.
2. Skip any room that already has a candidate for this pillar sitting in candidates/pending/
   or candidates/approved/ - do not draft the same room twice.
3. Diversity, applied strictly:
   - Mix categories and languages. Never pick all N from one cluster.
   - Never pick two rooms in the same run that plausibly share members. Check the notes column,
     which flags known overlaps.
4. For EACH room write a genuinely distinct blurb:
   - In that room's language.
   - Different opening line, different fact led with, different sign-off from every other blurb
     in this batch. Never reuse a sentence across two rooms, even across languages.
   - Match the register to the room: warm rooms get a member-with-news tone; scientific rooms
     lead with method and evidence, not with the product.
   - Obey that row's self_promo_rule literally.
5. Pick the link per the room's link_target column and build the UTM URL per
   registry/utm_convention.md. Leave utm_content EMPTY - it is filled with the share_id at
   send time, not now.
6. Write one file per candidate into candidates/pending/, named
   <YYYY-MM-DD>-<platform>-<dest_id>.md, using the frontmatter format in candidates/README.md.
   status: pending. Suggest send times spread across a single day, hours apart.
7. Write NOTHING to registry/shares.csv.
8. Print each blurb in chat with its room, language and platform named, then tell me they are
   waiting in candidates/pending/ for my approval.

Send nothing. Move nothing into approved/.
```

---

## 40 — Log what was sent

```
I sent some of what was in candidates/approved/. Update everything.

What went out:
<filename> - <platform_msg_id or permalink, or "no ID captured"> - <date>
<repeat per line>

Steps:
1. Open each named file in candidates/approved/.
2. Fill platform_msg_id and permalink in its frontmatter where I gave them; set status: sent.
3. Append a row to registry/shares.csv: fresh share_id, dest_id, deriv_id, pillar_id, sender,
   language, date_sent, status=sent, text_sent (the body as sent), link_used, all four utm
   columns with utm_content EQUAL to the new share_id, and measure_after = date_sent + 7 days.
4. If I gave no ID for a room whose measurable=yes, tell me - that ID is the only thing that
   makes later measurement automatic, and it is hard to recover once the message scrolls away.
5. Update last_posted on each destination used.
6. Move each file from candidates/approved/ to candidates/sent/.
7. Run scripts/check_registry.py.

Anything left in approved/ that I did not mention: leave it, and ask whether it is still
pending send or whether I forgot to report it.
```

---

## 50 — Measure (weekly)

```
Sweep registry/shares.csv for anything due measurement.

Steps:
1. Find rows where status=sent and measure_after is on or before today.
2. For each, check the destination's measurable column:
   - Telegram supergroup/channel with a platform_msg_id: pull reaction counts automatically.
   - LinkedIn with a post URN: pull impressions, reactions, comments, shares automatically.
   - Everything else: list it for me with its permalink so I can click straight through.
3. Fill reactions, comments, clicks. Leave clicks empty unless I supply analytics data.
4. Set status=measured and outcome to one of: worked / ok / flat / negative / too-early.
   Judge "worked" by downstream effect - a contributor, a real reply, a curator, actual
   traffic. High reaction counts with nothing following is "flat", not "worked".
5. Report:
   - Top rooms by outcome across all time, not just this week.
   - Any room with two consecutive flat outcomes - recommend retiring it.
   - Which language and which format is performing best.
   - Any room that removed a post, and what that says about its rules.
6. Run scripts/check_registry.py.

Files in candidates/sent/ do not change - they are the fixed record of what was said.
```

---

## 60 — Vet and add a room

```
Add a new destination: <name / URL / handle>

Steps:
1. Actually visit it. Read its rules, pinned messages, or about page. Do not guess, and do not
   fill self_promo_rule from assumption - if you cannot read the rules, say so and mark it
   UNVERIFIED in the notes.
2. Report before adding: approximate size, language, whether self-promotion is allowed and in
   what form, whether links are permitted, and whether asking contacts to engage would break
   its rules.
3. Set boost_ok honestly:
   - no-bannable for Reddit, Hacker News, Product Hunt, and anywhere with a stated vote or
     engagement rule. HN's rule penalises SITES as well as accounts.
   - risky for LinkedIn.
   - yes for Facebook, Telegram, WhatsApp, Discord, Bluesky, Mastodon group contexts.
4. Set measurable: yes for Telegram supergroups/channels and LinkedIn; no for Telegram basic
   groups, WhatsApp, Reddit, Discord, Facebook.
5. For Telegram, capture the numeric chat_id - without it nothing here can be automated later.
6. Set scope=local if this is a room specific to my project, or scope=template if it is a
   public room that would help anyone using this template.
7. Append the row with a unique lowercase-hyphenated utm_source, a tier, a cap_days, and a
   link_target. Run scripts/check_registry.py.

If the room bans self-promotion outright, still add it with status=comment-only and say so.
Knowing where NOT to post is worth recording.
```

---

## 70 — Weekly digest (what a scheduled run should produce)

```
Produce this week's distribution digest. DRAFT ONLY - send nothing, post nothing, and never
move a file into candidates/approved/.

1. Run prompt 30's logic to write 4-5 new candidates into candidates/pending/ for the current
   pillar.
2. If no derivative is queued for a main channel this week, draft one as a candidate too.
3. Run prompt 50's logic for anything due measurement; summarise in two or three lines.
4. Report in this order:
   - One line: what got drafted, and how many files now sit in candidates/pending/.
   - Each candidate, with room, language, platform, and suggested send time.
   - Measurement findings.
   - Anything on-hold, and why.
5. Close with: "Nothing has been sent, posted, or approved. Everything is in
   candidates/pending/ - move what you want into candidates/approved/ and tell me, and I will
   send those, spaced hours apart rather than all at once."
```

---

## 90 — Adapt this template for a new project

```
This repo is a fresh clone of promotion-template. Set it up for a new project.

Project: <name>
URL: <url>
Repo: <url>

Steps:
1. Interview me for everything project/PROJECT.md needs: standing facts with dates, voice
   rules, forbidden words, team voices, goal priority order, assets on hand. Ask about
   anything you cannot determine - never invent a standing fact or a URL.
2. Fill in project/PROJECT.md and as much of project/copy-pack.md as my answers support.
   Leave placeholders where you genuinely lack information, and list what is still missing.
3. Go through registry/destinations.csv and mark rooms that do not suit this project
   status=retired rather than deleting them - a room that is wrong now may fit a later
   pillar, and the rule research stays useful. Report what you retired and why.
4. Tell me which important room categories are MISSING for this project, so I know what to
   go and vet with prompt 60.
5. Do not touch scripts/ or the CSV headers.
6. Run scripts/check_registry.py.

Then tell me the three highest-leverage things to do first, given my stated goal order.
```

---

## Which harness for which prompt

**Cowork** has the connectors wired: LinkedIn posting via the official API, Telegram on a personal account, Gmail drafts, Google Drive, plus a scheduler so prompt `70` can run on a timer. Keep `40`, `50`, and `70` here.

**Codex** has none of those unless you configure them, but it's the better choice for the writing-heavy prompts — `10`, `20`, `30`, `90` — which only read and write local files and run identically in either harness.
