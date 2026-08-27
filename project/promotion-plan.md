# Sugar-Sugar - promotion plan

**Written 27 August 2026. Budget: zero. Labour: Anton + Livia, a few hours per week combined.**
Languages: English first; German, Romanian, Russian, Ukrainian when the room is already in that language.
Goals, in priority order: play the study, share a result card, recruit toward about 200 adults, take contributions that do not break the protocol, connect with diabetes / CGM / glucose-ML groups.

Everything named here was checked against the sugar-sugar repo and the contacts file on 27 August 2026. Items that could not be verified on the live web (the Dash homepage is a WebSocket shell) are marked UNVERIFIED. Nothing here is invented.

---

## 1. The strategic problem, stated honestly

This branch exists to recruit for a live observational study, not to grow a consumer app brand. The protocol target is about 200 adults. Warm rooms Anton and Livia are already in will move that number faster than cold diabetes subreddits, and cold diabetes subreddits will ban a blast that looks like an app launch.

Four things about the situation make this workable:

**The instrument is already live.** https://sugar-sugar.study is the pillar. You do not need a preprint before the first post. You need screenshots of a real playthrough and the honesty not to invent a participant count.

**You are already inside longevity, biohacking, bioinformatics and Romanian / Russian / Ukrainian science chats.** Those rooms will not fill a 100-person diabetes arm by themselves, but they will fill the non-diabetes and wellness-CGM arm, and they will do it without a modmail wait. Posting once, as a member with a study link, is what those rooms already do.

**You have institutional leverage.** Anton is PI at IBIMA, Universitätsmedizin Rostock. That unlocks the university press office and The Conversation in a way a GlucoseDAO-only account does not. Livia is at HEALES, which hosts the app. Use those names in institutional email, not in casual Telegram.

**Diabetes and CGM rooms are a different sport.** Many of them treat unsolicited study links as spam. The destination rows for those rooms start `on-hold` until someone reads the pin and, where needed, writes the mods. Do not "just post".

### Time allocation

| Where the time goes | Share | Why |
|---|---|---|
| **Week-zero assets** | ~30% | One honest playthrough, screenshots, one share card, one short screen recording. Without these every post is a bare URL. |
| **Warm rooms** | ~30% | Telegram, WhatsApp, LinkedIn personal feeds. One distinct blurb per room, hours apart. |
| **One-off durable asks** | ~25% | Uni press office, HEALES channels, diabetes-org emails after ethics language is checked, Show HN written by hand. |
| **Replying** | ~15% | An unanswered "is this medical advice?" comment kills the thread. Answer it. |

### Tactical rules

1. **Never claim the app gives medical advice or calculates insulin.** Ethics clearance is A 2026-0064 for a non-interventional historical-data study.
2. **Do not use an LLM to write anything posted on Hacker News.**
3. **Read the room's rules before posting, every time.** Diabetes rooms first.
4. **Write from inside the study.** Question -> gap -> drawing task -> live URL.
5. **Do not invent N.** If you need "how many people played", read the running site or the study CSVs.
6. **Do not run `sync_tracker.py` until `.env` has a Sugar-Sugar sheet id.** The copied id is the enhancement.bio tracker.
7. **Vary wording across chats.** Identical text in many Telegram rooms is how personal accounts get flagged.

---

## 2. Week zero: fixes before any outreach

| # | Fix | Status | Notes |
|---|---|---|---|
| 1 | Live URL answers and consent works | UNVERIFIED in this pass | Open https://sugar-sugar.study in a real browser before the first send |
| 2 | Desktop + mobile screenshots of a drawn prediction vs the real line | TODO | Repo has `assets/images/screenshot.png`; crop for LinkedIn / Telegram |
| 3 | One real or staging share-card PNG | TODO | `uv run share` in the sugar-sugar repo; do not invent a MAE |
| 4 | 15-20 s silent screen recording of drawing a forecast | TODO | Best asset for Telegram and LinkedIn |
| 5 | Sugar-Sugar Google tracker sheet, shared with `keys/service.json` | TODO | Replace `TRACKER_SHEET_ID` before any sync |
| 6 | GlucoseDAO LinkedIn / X / Telegram bios point at sugar-sugar.study | UNVERIFIED | Contacts file lists the accounts; check the live bios |
| 7 | Nightscout language stays honest | DONE in PROJECT.md | Planned, not implemented |

---

## 3. Content engine

Make **one thing per week**, in about 40 minutes. Reuse it across rooms with a changed first line.

**A. The missing baseline** - why ML papers have a model error and no human error. Best for LinkedIn, LessWrong, Habr, Show HN (hand-written).

**B. The drawing task** - screenshot or short recording of a line being pulled, then the real trace. Best for Telegram, Bluesky, Facebook groups once rules are read.

**C. A number you actually have** - ethics reference, 6-12 rounds, 3 hours in / 60 minutes out, GlucoBench 60-minute MAE 9-13 mg/dL as the published *model* range (cite the paper, do not imply we beat it). No fake participant counts.

**D. How it was built** - Dash, share cards, file formats, why protocol changes need a conversation. Best for GitHub, r/opensource, Habr.

Cadence: A, B, A, C, A, B, A, D.

### Reuse chain for one artefact

Make it Monday. Then: Bluesky (image + short mechanic) - LinkedIn Anton (methods) - GlucoseDAO LinkedIn page (we) - two or three warm Telegram rooms with distinct wording - one WhatsApp longevity / health room - Livia personal if the artefact is the drawing task.

---

## 4. Key deadlines

| Deadline | What | Action |
|---|---|---|
| As soon as week-zero assets exist | Warm Telegram / WhatsApp | First recruitment blurbs, hours apart |
| After diabetes-room rules are quoted | r/diabetes and CGM subs | Modmail first if the pin says so |
| When a genuine technical write-up exists | Show HN / Habr | Hand-written HN; Habr is a real article, not a launch note |
| When N is worth a methods post | The Conversation / uni press | Anton as academic, not GlucoseDAO as brand |

No CFP dates were verified for Sugar-Sugar on 27 August 2026. Do not copy enhancement.bio exhibition deadlines onto this study.
