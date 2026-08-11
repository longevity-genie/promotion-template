# Copy pack

The voice model, plus copy that already exists and can be reused or adapted. An agent reads this alongside `PROJECT.md` before drafting anything, so what's here shapes everything downstream.

---

## Why this file exists

Several people and at least two AI harnesses will draft text for this project. Without a fixed reference, output drifts toward generic marketing register, and posts written in January stop sounding like posts written in June. This file is what a fresh agent with no memory of prior conversations reads before writing, so post #40 sounds like post #4.

---

## Register by audience

**Scientists / researchers**
> Lead with the evidence-rating methodology and the translational ladder. Never lead with the game or the sculpture. They care about the knowledgebase's curation standards, the split ratings, and whether the sources hold up. They are put off by marketing register, overselling, and anything that looks like a toy rather than a resource.

**General / curious public**
> Lead with the constraint that makes it interesting: you get 100 credits and it is not enough for everything, so every choice is real. Assume no background in genetics. The hook is the organisms and what they can do - tardigrade radiation resistance, naked mole-rat cancer immunity, axolotl regeneration.

**Designers / artists / maker community**
> Lead with the sculpture and the constraint: the form is not designed by hand; it grows from the biophysical properties of the genes, and every result across the combination space must print cleanly. The printability constraint shaped the geometry more than any aesthetic decision.

**Developers / open source**
> Lead with the stack and the data architecture. Link the repo, not the site. Mention the 9-table relational DB, DoltHub sync, Reflex framework, and open MIT licence.

**Funders / curators / exhibitions**
> Lead with what exists today and what was shown where (Milano Design Week, RoBioinfo 2026). Be concrete about what is built versus what is planned. Overstating maturity is the fastest way to lose a serious one.

**Longevity / biohacking / transhumanism communities**
> Lead with the knowledgebase and the honest ratings. The 8 already-commercial therapies establish credibility. The split ratings and unflattering entries (AQP1, Dsup's neuron reversal, FOXO3's single-lab replication gap) show intellectual honesty.

---

## Voice samples

### Anton Kulaga - the science and the evidence

> We catalogued 1,023 experiments on genes that let other animals do things humans cannot, and then we made you spend a budget on them. The part I care about most is how we rate things. Not works or doesn't work, but how far up the translational ladder a claim actually got: purified protein, cell line, model animal, primate, human trial, market. The same gene often carries different ratings for different claims. CAHS D from tardigrades is high confidence in yeast and only medium in human cells. Being precise about where the evidence stops turns out to make the science more interesting, not less. The gap is the story.

### Livia Zaharia - the design and the object

> Every set of gene choices grows a different sculpture, and none of them were designed by hand. Protein mass, exon count, hydrophobicity, disorder, isoelectric point - the biophysical properties of the genes you pick become the parameters of a Voronoi shell. Then the shell has to actually print, on a cheap machine, across an enormous combination space, without a human checking each result. That constraint did more for the work than any aesthetic decision.

---

## Standing copy

**One-liner** (matches `PROJECT.md`)
> An open, evidence-rated knowledgebase of 109 human enhancement genes from 108 organisms, wrapped in a character generator with a hard credit budget so people actually read the science.

**Two-sentence version**
> Materialized Enhancements gives you 100 credits and 80 real genes from 108 organisms, and you cannot afford everything - so you end up reading the evidence. Every claim is rated by how far up the translational ladder it actually got, not works or doesn't, and your choices grow a unique 3D-printable sculpture from the biophysical properties of the genes you picked.

**Paragraph version**
> Materialized Enhancements is a browser tool where you design an enhanced human from real genes. You get 100 enhancement credits and a library of 80 playable genes drawn from 108 organisms - tardigrade Dsup for radiation resistance, naked mole-rat hyaluronic acid for cancer resistance, African elephant multi-copy TP53, axolotl Lin28a for regeneration. The budget is deliberately too small, so every credit is a real choice, and people read the science before spending it. Every gene is rated by how far up the translational ladder the evidence actually got - cells, model animal, primate, human trial, market - with split ratings where confidence in the mechanism differs from confidence in the intervention. Eight of the therapies in the library are already sold to adults today. Your choices then procedurally grow a unique 3D-printable Voronoi sculpture from the biophysical properties of the genes you selected. The knowledgebase behind it - 109 genes, 1,023 experiments, 850 DOI-linked references - is open and citable.

**Bio line** - for when a community requires an intro post
> Aging researcher at University of Rostock. We built an open knowledgebase of 109 genes that let other organisms do things we cannot, rated by translational stage, and wrapped it in a character generator where the credit budget forces real choices. enhancement.bio

---

## Per-platform openings

| Platform | Opening that works | Why |
|---|---|---|
| LinkedIn | "We catalogued 1,023 experiments on genes that let other animals do things humans cannot, and then we made you spend a budget on them." | Knowledge-first, no announcement register, the ask is implied |
| Bluesky | "Every gene you pick changes the shape." | Visual hook in under 10 words, fits the feed-scroll pattern |
| Reddit self-post | "The premise: 100 credits, 80 real genes from 108 real organisms, and every upgrade has a genuine biological tradeoff." | States the mechanic immediately, signals substance |
| Telegram (warm room) | Context-specific - "We finally put our enhancement project online" for English groups, varying first line per language | Member-with-news register, not marketer |
| Forum showcase | "Inputs per gene: protein mass, exon count, GRAVY score, disorder, pI, and the size of the biological system it belongs to." | Technique-first for technical forums |
| Hacker News | (write by hand - no LLM text) | HN moderator March 2026 guidance: no LLM, not even for editing |

---

## Phrases to avoid

Beyond the hard `forbidden_words` list in `PROJECT.md`, these are stylistic tells worth avoiding:

- "excited to announce", "thrilled to share", "game-changing", "revolutionary"
- "it's not just X, it's Y" - a very recognisable LLM construction
- Rhetorical question openers ("Ever wondered what would happen if...")
- Hedging stacks: "it could potentially perhaps"
- Em dashes (use plain hyphens)
- "Leveraging", "harnessing", "unlocking"
- "At the intersection of" (use "where X meets Y" or just describe what it is)

---

## Gene-of-the-week candidates

Strong candidates already written in the knowledgebase, ordered by how well they travel:

1. **FOXO3** - strongest human longevity association, and only one lab has ever put it in a mouse and measured lifespan (Inci 2025, ~30% increase, awaits replication)
2. **AQP1** - the debunk: water-holding frog aquaporin, a case study in how a plausible enhancement story gets assembled entirely from sources that do not support it (counterintuitive, therefore shareable)
3. **CPD photolyase** - a UV-repair gene placental mammals threw away 170 million years ago; marsupials kept it
4. **Klotho** - narrow dosing window: two copies of KL-VS is worse than one
5. **TP53 in elephants** - Peto's paradox, plus the honest caveat that a 2023 follow-up failed to reproduce the key binding result
6. **RBM3** - hibernation neuroprotection without the cooling
7. **CHRNA1** - cobra-venom resistance, convergently evolved thirteen times
8. **Dsup** - works for radiation shielding, and behaved badly in nerve cells
9. **Reflectin** - cuttlefish camouflage needs skin organs and neural control you do not have
10. **MGMT P140K** - already in chemo-protection trials

**Timing note:** Pair the axolotl Lin28a entry with the SciShow axolotl video from 28 July 2026 while it is still current.

---

## Copy that already worked

(This section fills in as posts are sent and measured. After a few months it becomes the most valuable section in the file.)

### Template

> **Date** - **platform** - outcome: **what followed**
>
> the post text
>
> Why it worked: ...
