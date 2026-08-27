# PROJECT.md

---

## Identity

- **project_id:** `sugar-sugar`
- **Name:** Sugar-Sugar
- **Live URL:** https://sugar-sugar.study
- **Staging URL:** https://vanilla-sugar.glucosedao.org/
- **Repo URL:** https://github.com/GlucoseDAO/sugar-sugar
- **Org:** [GlucoseDAO](https://github.com/GlucoseDAO)
- **LinkedIn company:** https://www.linkedin.com/company/106917242/
- **X/Twitter:** https://x.com/glucosedao2024
- **GlucoseDAO Telegram:** https://t.me/+yAejJ0xyucExMzg0
- **GlucoseDAO site:** https://glucosedao.github.io
- **Hugging Face:** https://huggingface.co/GlucoseDao
- **UTM campaign prefix:** `sugar` - every pillar's `utm_campaign` starts with this

## One-liner

A browser game that measures how well people can predict the next hour of a CGM trace, so machine-learning models finally have a human baseline to beat.

## Standing facts

The numbers and claims you repeat everywhere. An agent may use **only** these - it is instructed never to invent a figure. Keep them current, and if the live site disagrees with this list, fix one or the other rather than leaving both.

> **Sourced 2026-08-27** from the sugar-sugar README, the study protocol (`The study - technical Guidebook.md`), the German consent form, and `data/glucosedao_contacts.md`. Do not invent a live participant count. The landing page shows "games played so far" from the running app; read it from the site if you need a number.

| Fact | Value | Last verified |
|---|---|---|
| Live study URL | https://sugar-sugar.study | 2026-08-27 |
| Study title | Human Prediction of Next-Hour Glucose from Prior Continuous Glucose Monitor (CGM) Context: An Online Benchmarking Study | 2026-08-27 |
| Ethics committee | Ethikkommission der Universitätsmedizin Rostock (University Medical Center Rostock) | 2026-08-27 |
| Ethics reference | A 2026-0064 | 2026-08-27 |
| Ethics received | 27 February 2026 | 2026-08-27 |
| Ethics status | Positive vote (positives Votum); non-interventional study using historical data only | 2026-08-27 |
| Principal investigator | Anton Kulaga, IBIMA, University Medical Center Rostock | 2026-08-27 |
| Co-investigator | Livia Zaharia, HEALES (Healthy Life Extension Society, Brussels) | 2026-08-27 |
| Biostatistical advice | Benjamin Otte, M.Sc., IBIMA, University Medical Center Rostock | 2026-08-27 |
| Scientific advisor | Irina Gaynanova, Department of Statistics and Department of Biostatistics, University of Michigan | 2026-08-27 |
| Core developers | Livia Zaharia (GlucoseDAO); Anton Kulaga (IBIMA) | 2026-08-27 |
| Maintainer / DevOps | Newton Winter | 2026-08-27 |
| Hosting | Web app hosted by HEALES; research data stored at University Medical Center Rostock | 2026-08-27 |
| Data controller | IBIMA, Universitätsmedizin Rostock | 2026-08-27 |
| Target sample | About 200 adults (18+): about 100 people with diabetes and 100 without; adaptive design allows up to 150 per group | 2026-08-27 |
| Consent form target | At least 200 participants (Teilnehmerinformation v2) | 2026-08-27 |
| Age gate | 18+ and GDPR consent required | 2026-08-27 |
| Task | See 3 hours of CGM context; predict the next 60 minutes by drawing 12 points (one every 5 minutes) | 2026-08-27 |
| Rounds | 6 to 12 prediction tasks per participant; the app offers up to 12 rounds | 2026-08-27 |
| Session length | About 2-3 minutes per round; a full session around 30 minutes. Pilot testing: engagement held through 15-20 minutes (about 10-12 segments) | 2026-08-27 |
| Outcome metrics | MAE and RMSE in mg/dL; the app also reports MAPE | 2026-08-27 |
| Play formats | A = public anonymized traces; B = own uploaded CGM; C = mixed | 2026-08-27 |
| Public datasets used | BIG IDEAs (PhysioNet) and D1NAMO | 2026-08-27 |
| Upload formats named in the README | Dexcom, Libre, Medtronic; Nightscout import is planned and not fully implemented | 2026-08-27 |
| CGM-user definition in the protocol | Used a CGM for more than one month | 2026-08-27 |
| Missing benchmark | No prior published study has systematically quantified human accuracy at next-hour glucose prediction | 2026-08-27 |
| GlucoBench ML 60-minute figures (cited in the protocol) | RMSE 10-16 mg/dL; MAE 9-13 mg/dL. Paper: https://arxiv.org/abs/2410.05780 | 2026-08-27 |
| Privacy until submit | Progress stays in the browser localStorage; nothing is sent without active consent | 2026-08-27 |
| Share cards | After a finished game the app builds a 1200x630 PNG and a public `/share/<id>` page | 2026-08-27 |
| UI languages on disk | English, German, Ukrainian, Romanian, Russian, Chinese, Spanish, French | 2026-08-27 |
| Licence | Apache-2.0 | 2026-08-27 |
| Stack | Plotly Dash (Python), served with gunicorn in production | 2026-08-27 |
| General contact | glucosedao2024@gmail.com | 2026-08-27 |
| Study emails | anton.kulaga@uni-rostock.de; livia.zaharia@uni-rostock.de; nikolay.usanov@uni-rostock.de | 2026-08-27 |

## Voice rules

- Plain hyphens, not em dashes.
- No marketing register. Never "excited to announce", "thrilled to share", "game-changing", "revolutionary".
- Write from inside the study, as one of the people who built it. Lead with the question that interested us (can a person predict the next hour of glucose?), why that gap mattered, and what we made people do about it.
- Give team stories a clear causal sequence: our question -> why it mattered -> what we built -> what exists now -> why it is a game rather than a survey -> what the reader can do next.
- Concrete numbers over adjectives. Use only the standing facts table. Never invent a participant count, a MAE, or a recruitment percentage.
- Use first-person team language (`I` or `we`).
- One clear ask at most per message. The default ask is: play the study at sugar-sugar.study.
- Never append a generic third-person referral line. If asking people to share or recruit is relevant, write it freshly for that room.
- Be precise about what the study does not do. It is not medical advice, not a dosing tool, and not an insulin calculator. It measures prediction, using historical traces.
- Do not oversell safety or clinical utility. Short-term forecasts can support day-to-day decisions; that is the motivation, not a claim that this app manages diabetes.

## Forbidden words

| Never say | Say instead | Why |
|---|---|---|
| medical advice / treats diabetes / calculates insulin | a prediction game / a human-baseline study | This is a non-interventional observational study. Clinical-advice language is false and dangerous |
| FDA-approved / clinically validated app | ethics-cleared observational study | The clearance is ethics, not a device approval |
| AI-generated | (do not describe the traces this way) | Public traces come from named datasets (BIG IDEAs, D1NAMO). Several rooms ban "AI-generated" work |
| game (in r/InternetIsBeautiful) | (do not post this study there) | That sub bans webgames, quizzes and puzzles by written rule. Sugar-Sugar is a game |
| Nightscout works | Nightscout import is planned and not fully implemented | README known-issues list |
| excited to announce | (just state the thing) | LLM cadence |
| thrilled to share | (just state the thing) | LLM cadence |
| it's not just X, it's Y | (restructure) | Recognisable LLM construction |
| Ever wondered... | (lead with the fact) | Rhetorical question openers are filler |

## Who writes as whom

| Person | Platforms | Their angle | What makes their voice theirs |
|---|---|---|---|
| Anton Kulaga | linkedin, telegram, whatsapp, reddit, bluesky, hackernews, email | the study design, the missing human baseline, the statistics | First person, methodology-first, admits uncertainty. PI at IBIMA, Uni Rostock. |
| Livia Zaharia | linkedin, bluesky, instagram, telegram | the game, the drawing task, why a playful form gets people to finish 6-12 rounds | Visual and process-oriented. Core developer. HEALES. Talks about what the player actually does with their hand. |
| Newton Winter | github, discord, forums | the Dash stack, share cards, deployment | Technical, matter-of-fact. Maintainer / DevOps. |

Irina Gaynanova is scientific advisor. Do not write posts in her name unless she asks.

## Canonical tags

`#OpenScience` `#CGM` `#diabetes` `#SciComm` `#glucoseprediction`

Bluesky-specific prefix: a small chart or share-card image before tags. Do not dump medical hashtags into diabetes rooms that treat them as spam.

## Goals

See [goals.md](goals.md) for the full list with metrics. In short: make people play the study, share a result card, help us recruit toward about 200 adults, connect us with diabetes and CGM communities, and keep the protocol intact.

## Assets on hand

- Live study at https://sugar-sugar.study
- Prediction-chart screenshot in the sugar-sugar repo (`assets/images/screenshot.png`)
- Site-wide Open Graph card at `/assets/og-card.png` (1200x630)
- Per-result share cards at `/share/<id>/image.png` after a finished game
- Study protocol and consent text in the sugar-sugar repo
- NEEDED: a fresh desktop screenshot of a drawn prediction vs the real line
- NEEDED: a mobile screenshot of the same moment
- NEEDED: one finished share-card PNG from a real or staging playthrough (use `uv run share` on staging, never invent scores)
- NEEDED: a 15-20 s silent screen recording of drawing a forecast

## Notes and open questions

- The sibling repo for the study app is `sugar-sugar` (workspace folder). Standing facts come from that repo and the live site, not from memory.
- Catalogue files (`registry/*-catalogue.csv`) were copied from the enhancement-bio branch as a membership inventory. Their `prior_project_post` column records enhancement.bio history, not Sugar-Sugar sends.
- `.env` Buffer keys were copied from the enhancement-bio working tree (same posters). `TRACKER_SHEET_ID` currently points at the enhancement.bio tracker. **Do not run `scripts/sync_tracker.py` until that id is replaced with a Sugar-Sugar sheet**, or the enhancement tracker will be overwritten in place.
- Nightscout import is planned and not fully implemented. Do not recruit on a Nightscout-works claim.
- Do not restart-shame in public copy beyond what the README already says: discarding bad scores would skew the study.
- Facebook page for GlucoseDAO: not listed in the contacts file. Do not invent one.
- LinkedIn groups: browser-only. No Groups API since 2017. Treat `platform=linkedin-group` like WhatsApp.
- Diabetes and CGM rooms often ban study recruitment without mod approval. Read the pin, then often modmail, before the first post. Rows for those rooms start as `on-hold` until the written rule is recorded.
