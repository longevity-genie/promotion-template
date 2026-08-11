# PROJECT.md

---

## Identity

- **project_id:** `enhancement-bio`
- **Name:** Materialized Enhancements
- **Live URL:** https://enhancement.bio
- **Repo URL:** https://github.com/longevity-genie/materialized-enhancements
- **LinkedIn showcase:** https://www.linkedin.com/showcase/138363945/
- **LinkedIn company (Longevity Genie):** https://www.linkedin.com/company/106920105/
- **UTM campaign prefix:** `enhbio` - every pillar's `utm_campaign` starts with this

## One-liner

An open, evidence-rated knowledgebase of 109 human enhancement genes from 108 organisms, wrapped in a character generator with a hard credit budget so people actually read the science.

## Standing facts

The numbers and claims you repeat everywhere. An agent may use **only** these - it is instructed never to invent a figure. Keep them current, and if the live site disagrees with this list, fix one or the other rather than leaving both.

| Fact | Value | Last verified |
|---|---|---|
| Genes catalogued | 109 | 2026-07-29 |
| Genes playable in the game | 80 | 2026-07-29 |
| Catalogued experiments | 1,023 | 2026-07-29 |
| Source organisms | 108 | 2026-07-29 |
| Registered clinical trials | 729 | 2026-08-06 |
| Organizations in database | 108 (69 labs, 36 biotech, 3 clinics) | 2026-08-06 |
| Unique DOI-linked references | 850 | 2026-08-06 |
| Therapies already sold to adults | 8 | 2026-07-29 |
| Enhancement credits per character | 100 | 2026-07-29 |
| Gene categories | 6 (Longevity & Genome, Stress Resistance, Environmental Adaptation, Regeneration, Expression, Perception) | 2026-07-29 |
| Evidence rating system | Translational ladder: cells - animals - primates - humans - market, with split ratings for mechanism vs intervention | 2026-07-29 |
| AI assistant integration | "Ask GPT" and "Ask Claude" buttons on individual gene pages and in the general build view | 2026-08-08 |
| Premiered | Milano Design Week (CODAME ART+TECH "The New Human") | 2026-07-29 |
| Shown at | RoBioinfo 2026 | 2026-07-29 |
| Database tables | 9 relational (SQLite, synced from DoltHub every 6h) | 2026-08-06 |

## Voice rules

- Plain hyphens, not em dashes.
- No marketing register. Never "excited to announce", "thrilled to share", "game-changing", "revolutionary".
- Lead with the method or the evidence, not the outcome.
- Concrete numbers over adjectives.
- One ask per message, stated in the first two lines.
- Always include a forward request ("if you know someone who would find this useful, please pass it on").
- The ask comes before the explanation, not after.
- Be precise about where the evidence stops - the gap is the story.
- Never oversell. An unflattering rating is more interesting than a clean claim.
- Do not sell for or against human enhancement - show where the evidence is and where it ends.

## Forbidden words

| Never say | Say instead | Why |
|---|---|---|
| AI-generated | algorithmically generated / procedurally generated from real gene data | r/generative, r/creativecoding, r/proceduralgeneration, r/InternetIsBeautiful, Bluesky art feeds, Colossal, and Habr all exclude AI-generated work by written rule. One careless word disqualifies from most best surfaces at once |
| game (in r/InternetIsBeautiful) | interactive explorer | r/InternetIsBeautiful bans webgames outright including quizzes and puzzles |
| excited to announce | (just state the thing) | LLM cadence, triggers suspicion |
| thrilled to share | (just state the thing) | LLM cadence |
| it's not just X, it's Y | (restructure) | Recognisable LLM construction |
| Ever wondered... | (lead with the fact) | Rhetorical question openers are filler |

## Who writes as whom

| Person | Platforms | Their angle | What makes their voice theirs |
|---|---|---|---|
| Anton Kulaga | linkedin, telegram, whatsapp, reddit, bluesky, hackernews, email | the science, the evidence, the knowledgebase | First person, methodology-first, admits uncertainty, leads with where the evidence stops. Aging researcher at Uni Rostock. |
| Livia Zaharia | linkedin, bluesky, instagram | the design, the object, the geometry | Visual, process-oriented, constraint-first. Parametric designer. Talks about how printability shaped the form more than aesthetics. |
| Newton Winter | github, discord, forums | the stack, the code, the engineering | Technical, matter-of-fact. Web/RPG/devops. |

## Canonical tags

`#generativeart` `#creativecoding` `#SciComm` `#OpenScience` `#Genomics` `#longevity`

Bluesky-specific prefix: the DNA emoji before tags.

## Goals

See [goals.md](goals.md) for the full list with metrics. In short: make people play, share builds, contribute, connect us with experts, suggest funding sources.

## Assets on hand

- Livia's wearing-the-model video (vertical, short)
- Screenshots of the character generator UI
- Screenshots of the knowledgebase entries
- 3D renders of Voronoi sculptures (various gene combinations)
- NEEDED: still photographs of a printed sculpture on neutral background, natural light, in-hand for scale, 3000 px minimum on long edge
- NEEDED: 20-40 s vertical loop of the sculpture from existing video

## Notes and open questions

- Tech stack: Reflex (Python) + Fomantic UI, Three.js for 3D, SQLite synced from DoltHub, Python parametric geometry pipeline, binary STL export.
- No signup wall on core loop - only a nickname is required. No email, no account creation.
- GitHub link is now on the homepage and knowledgebase pages. README links point to the `longevity-genie` org path.
- "Ask GPT" and "Ask Claude" icons on gene pages and general build let visitors interrogate the science behind each gene.
- LinkedIn showcase page: https://www.linkedin.com/showcase/138363945/
- Twitter/X: use existing Longevity Genie account (park, low priority).
- Facebook page: to be created.
- LinkedIn groups available for cross-posting via browser automation.
- Post automation: the promotion-template repo supports pre-generating posts and scheduling them for LinkedIn, Twitter/X, and other platforms.
