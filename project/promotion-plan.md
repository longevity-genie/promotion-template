# enhancement.bio - promotion plan

**Written 29 July 2026. Revised 8 August 2026. Budget: zero. Labour: Anton + Livia, more than 2 hours per week combined (relaxed from original estimate).**
Languages: English, Russian, Romanian.
Goals, all four weighted equally: site traffic, scientist contributors, exhibitions and funders, press.

Everything named in this document was checked against the live web on 29 July 2026 and revised on 8 August 2026. Items that could not be verified are marked UNVERIFIED and should be confirmed in a browser before you spend time on them. Nothing here is invented.

**What changed on 8 August 2026:**
- Fixes #1-4 from the original "week zero" list are done (GitHub link on site, contributor setup, signup is nickname-only, gene numbers reconciled).
- The site now has "Ask GPT" and "Ask Claude" icons on individual gene pages and in the general build view - a new feature worth highlighting.
- The promotion-template repo provides automation: posts can be pre-generated and scheduled for LinkedIn, Twitter/X, and other platforms.
- More time is available than the original 2h/week estimate.

---

## 1. The strategic problem, stated honestly

The original estimate was 2 hours per week - about 26 hours over 90 days, not enough to run social media accounts. More time is now available, and the promotion-template provides automation for pre-generating and scheduling posts. This changes the calculus: you can now sustain a posting cadence that the original plan explicitly said you could not.

The standard model still spends all its effort on **broadcast**, which decays to zero the moment you stop. But with automation, broadcast becomes cheaper - you batch-generate a week of posts in one sitting and schedule them. The investment shifts from posting to making the artefacts worth posting.

Four things about your situation make this work:

**You are already inside about forty relevant communities.** The Telegram and WhatsApp inventory turned up roughly 40 groups in longevity, biohacking, transhumanism, bioinformatics, DeSci, sci-art, maker and Romanian science circles where you are a long-standing member. Posting once, with a real update, in a group you have been part of for two years is not spam. It is what members do. The spam feeling you are trying to avoid comes almost entirely from cold-blasting strangers, which this plan asks you to do very little of.

**You have institutional leverage almost nobody in bioart has.** Anton is at Uni Rostock. That unlocks two doors that are closed to independents: the Uni press office, which feeds **idw-online** (individuals categorically cannot post there, and idw is what German science desks and NDR actually read), and **The Conversation**, which commissions only academics writing in their own field and gets republished very widely. Neither costs money. Both are single emails.

**The knowledgebase is a better asset than the game.** 109 genes, 80 playable, 1,023 catalogued experiments, 108 source organisms, 8 already-commercial therapies, each rated by how far up the translational ladder the evidence actually got. That is a citable resource. Science venues that will delete a "check out my game" post will happily host "here is a curated database of comparative-biology enhancement evidence." The game is the door; the knowledgebase is the reason serious people stay. **Lead with whichever one the room rewards** - this is the single most important tactical rule in the document.

**You now have "Ask GPT" and "Ask Claude" buttons on gene pages and in the general build.** This turns every gene entry into an interactive research starting point. For science and bioinformatics audiences, this is a genuine feature worth leading with: an evidence-rated knowledgebase where you can immediately interrogate the science behind each gene using AI assistants.

### The allocation

| Where the time goes | Share | Why |
|---|---|---|
| **One-off durable assets and submissions** | ~40% | Directory listings, awesome-list PRs, press submissions, open-call applications, press-office email. Done once, keeps paying for years, needs no maintenance. |
| **One anchor artefact per week, reused everywhere** | ~25% | You make one thing per week. It gets posted to different rooms over the following days with a changed first line. You never write a second piece of content. |
| **Pre-generated and scheduled posts** | ~20% | Use the promotion-template automation to batch-generate platform-native posts from each artefact, then schedule them across LinkedIn, Twitter/X, Bluesky, and other platforms. One batch session per week replaces daily manual posting. |
| **Replying** | ~15% | Where contributors and curators actually come from. Non-negotiable: an unanswered comment on a Show HN or a curator email is the whole opportunity thrown away. |

### Five rules that save you the most time

1. **Never call the sculpture AI-generated.** Say *algorithmically* or *procedurally generated from real gene data*. This is not stylistic. r/generative, r/creativecoding, r/proceduralgeneration, r/InternetIsBeautiful, r/SyntheticBiology, Bluesky's two largest art feeds, Colossal and Habr's sandbox all exclude AI-generated work by written rule. One careless word disqualifies you from most of your best surfaces at once.
2. **Do not use an LLM to write anything you post on Hacker News.** HN's moderator updated the canonical Show HN guidance in March 2026 with exactly this: *"Write your text by hand. Don't use an LLM to generate any of it (not even a tiny bit, including to edit or spruce it up)... this is a big dividing line at present."* The Show HN brief in the copy pack is therefore a list of facts and a structure, not finished prose. Write it yourself.
3. **Read the room's rules before posting, every time.** Most science subreddits and several Discords ban promotion with bans, not warnings. Section 5 marks which. Budget one minute per room.
4. **One ask per message, stated in the first two lines.** Buried asks get ignored.
5. **Always include a forward request.** "If someone you know would find this useful, please pass it on" costs one line and is the only free multiplier that works reliably.

---

## 2. Week zero: five fixes that must happen before any outreach

**Status as of 8 August 2026:** Items 1-4 are done. Only item 5 (print photography) remains.

| # | Fix | Status | Notes |
|---|---|---|---|
| 1 | **GitHub link on the homepage and `/knowledgebase`.** | DONE | GitHub link added to the site. README links corrected to `longevity-genie` org path. |
| 2 | **Make the repo contributor-ready.** Contribution instructions and good-first-issue labels. | DONE | Contribution info added. |
| 3 | **No signup wall on the core loop.** | DONE | Only a nickname is required - no email, no account, no personal information. This is fine for Show HN, r/InternetIsBeautiful, and all other venues. |
| 4 | **Reconcile the public numbers.** | DONE | The gene numbers on the website and README are now consistent. Standing facts: 109 catalogued, 80 playable. |
| 5 | **Print one sculpture and photograph it properly.** Neutral background, natural light, in-hand shot for scale, plus one on a plinth. Export at **3000 px minimum** on the long edge. | STILL NEEDED | This single asset unlocks r/3Dprinting (which bans render-only posts by written rule), Colossal (which will not cover work without images of individual physical works), Dezeen (needs 3000 px jpegs), and every gallery and residency application. Livia's wearing-the-model video already helps here; still photographs are what editors need. |

---

## 3. Content engine: one artefact a week, four rooms

You make **one thing per week**, in about 40 minutes. It is then posted to different rooms over the following days with a changed opening line. You do not write anything twice.

Rotate four formats:

**A. Gene of the week** (your cheapest and best format). Pick one gene. Two paragraphs: the extraordinary thing the organism does, then what the evidence actually supports and where it stops. Use the split rating honestly - "high confidence in mice, nobody has done it in a primate" is a *better* hook than a clean claim, because it is a story with tension. You have 109 of these already written in the knowledgebase, so this format is mostly copy, trim and add a hook.

**B. The object.** A photograph or short loop of a printed sculpture, or Livia wearing one, or the folding-protein print. Say which genes produced that particular shape. This is what travels on visual platforms and it is the only format that gets you into design press.

**C. A number from the knowledgebase.** "Of 109 genes we catalogued, 8 are already sold to adults today." "1,023 experiments, and here is how many made it past mice." This is the format that earns respect from scientists and is the seed of the one genuinely high-ceiling Reddit post (r/dataisbeautiful, Mondays only for personal data, needs a real chart).

**D. How it was built.** How gene parameters drive the Voronoi mesh; how you kept it printable on weak machines across a huge combination space; how you designed the credit costs so the budget forces real choices. This is the format for Hacker News, three.js, Grasshopper, Habr and Creative Applications - and it is the one that reaches other builders, who are your likeliest contributors.

Cadence: A, B, A, C, A, B, A, D and repeat. Gene posts are the backbone because they are nearly free to produce.

### The reuse chain for one artefact

Make it Monday. Then, over the week, without rewriting: Bluesky (with the tag set) - LinkedIn (Anton, framed as knowledge not announcement) - two or three warm Telegram or WhatsApp groups from the rotation - one Discord showcase channel - Mastodon (genomic.social) if it is format A or C.

That is 20 minutes of posting spread over four days, on top of the 40 minutes of making.

---

## 4-11. Channel map, Reddit, Russian/Romanian tracks, exhibitions, influencers, calendar, metrics

See the per-platform draft files in `drafts/` and the original planning documents for complete details on:

- **Section 4:** Channel map (Tier 1 durable assets, Tier 2 weekly rotation, Tier 3 forums)
- **Section 5:** Reddit strategy (green-light subs, modmail-first subs, closed subs, framing traps)
- **Section 6:** Russian-language track (Habr, Telegram channels, vc.ru)
- **Section 7:** Romanian-language track (CINETic, Scientia.ro, RSBi, DevTalks Cluj)
- **Section 8:** Exhibitions, funders and open calls (EMAP, Wissenschaftsjahr, Science Museum, Coalesce, etc.)
- **Section 9:** Influencers, podcasts and press contacts
- **Section 10:** 90-day calendar
- **Section 11:** What to measure

---

## Key deadlines

| Deadline | What | Action |
|---|---|---|
| 2026-08-08 | IndieCade Festival closes | Decide and apply (or skip) |
| 2026-08-16 | DevTalks Cluj CFP closes | Submit abstract |
| 2026-08-23 | WiD Junges Forum | Send Livia |
| 2026-08-30 | SaloneSatellite 2027 | Livia applies (under-35) |
| 2026-09-03 | EMAP opens | Start application |
| 2026-09-07 | Sonar+D KNOWCASE deadline | Decide and submit |
| 2026-11-06 | EMAP closes | Submit by 14:00 CET |
| 2027-01 (est) | Prix Ars Electronica opens | Target Interactive Art category |
