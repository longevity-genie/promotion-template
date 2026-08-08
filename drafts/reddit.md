# Reddit posts

> Standing facts and voice rules: see [PROJECT.md](../project/PROJECT.md) and [copy-pack.md](../project/copy-pack.md).
> In r/InternetIsBeautiful do not say "game".

## Timing

**Matters significantly for self-posts; less for link posts.** Reddit's algorithm heavily weights early upvotes in the first 1-2 hours. Best window: 06:00-09:00 US Eastern = **13:00-16:00 Bucharest time** on weekdays (Tue-Thu best). Weekends are fine for hobby/interest subs (r/transhumanism, r/generative) but worse for science subs. **For important posts (r/transhumanism, r/AskScienceDiscussion): aim for Tue-Thu 13:00-16:00 Bucharest. For niche subs: post any time, the audience is small enough that timing barely matters.**

## Initial engagement - DO NOT DO THIS

**Reddit vote manipulation is bannable for both accounts AND domains.** Never ask anyone to upvote a Reddit post. HN has the same rule. One incident can get the enhancement.bio domain flagged site-wide. The only thing you can do: be online to reply to early comments quickly (within 30 min). Fast, substantive replies are the one legitimate engagement signal you control.

---

## r/transhumanism (self-post, one image)

**Title:** `We built a character generator for enhanced humans using only real genes, with a hard credit budget so you cannot max everything out`

> The premise: 100 credits, 80 real genes from 108 real organisms, and every upgrade has a genuine biological tradeoff. You cannot afford everything, which is the point - the limited budget forces the same kind of choices biology does.
>
> What I think makes it worth your time rather than another speculative toy: we rate every gene by how far up the translational ladder the evidence actually got, not works/doesn't. Cells, model animal, primate, human trial, market. The same gene often gets different ratings for different claims. Tardigrade CAHS D is high confidence in yeast and medium in human cells. Chernobyl-fungus melanin is high confidence for passive radiation shielding and low for the radiosynthesis hypothesis. Eight of the therapies in the library are already sold to adults today.
>
> Some entries are deliberately unflattering. The water-holding frog aquaporin is in there as a case study in how a plausible enhancement story gets assembled entirely from sources that do not support it - the frog's own aquaporin has never been cloned, and its expression goes down in dormancy, not up.
>
> Free, no signup, open source. Your gene picks also grow a printable Voronoi sculpture, generated procedurally from the biophysical properties of the genes - not AI.
>
> https://enhancement.bio
>
> Genuinely want the arguments: which of these do you think we rated too generously?

---

## r/generative and r/creativecoding (image or video)

**Title:** `Voronoi sculptures grown from real gene data - protein mass, exon count and disorder become the shell parameters`

> Each shape comes from a set of genes someone picked in a science game. The biophysical properties of those genes - protein mass, exon count, GRAVY score, intrinsic disorder, isoelectric point, category size - seed and parameterise a Voronoi shell.
>
> The hard constraint was printability: every result across a very large combination space has to slice and print on a weak machine with nobody checking it. That did more for the output than any aesthetic decision.
>
> Algorithmic, not AI - the generator is ours and it is open source.
>
> https://github.com/longevity-genie/materialized-enhancements

---

## r/proceduralgeneration (technical self-post)

**Title:** `Parameterising a Voronoi shell from biological data, with print-safety as a hard constraint`

> Inputs per gene: protein mass, exon count, GRAVY score, disorder, pI, and the size of the biological system it belongs to. Outputs: seed, radius, layer spacing, Voronoi point count, surface extrusion, and a print-safe scale factor.
>
> The interesting problem was not making it look organic - it was guaranteeing manifold, printable geometry across the whole combination space without a human in the loop, on printers with low tolerance.
>
> Happy to go into the details. Code: https://github.com/longevity-genie/materialized-enhancements

---

## r/AskScienceDiscussion (self-post, no link in the title)

**Title:** `Which comparative-biology longevity genes do you think are most over-sold in popular coverage?`

> I work on aging genomics and we have spent a while cataloguing experiments on genes that let other animals survive things we cannot - tardigrade Dsup, naked mole-rat hyaluronic acid, elephant multi-copy TP53, bowhead whale CIRBP, axolotl Lin28a. 1,023 experiments so far.
>
> The pattern that keeps coming up is that popular coverage collapses a translational ladder into a binary. Dsup shields DNA from radiation damage and also behaved badly in nerve cells. FOXO3 is the strongest human longevity association in biology and nobody has ever overexpressed it in a mammal and measured lifespan. Elephant TP53 might accelerate aging in humans.
>
> My question for people who work adjacent to any of these: which ones do you think we, collectively, oversell most? And are there organisms whose adaptations get ignored because the mechanism is anatomical rather than genetic?
>
> Our notes are open if useful, but I am mainly after the arguments.

---

## r/coolgithubprojects (link post)

**Title:** `Materialized Enhancements - open, evidence-rated knowledgebase of 109 human enhancement genes, with a playable character generator`

Link the **repo**, not the site.

---

## r/InternetIsBeautiful (link post - the word "game" must not appear)

**Title:** `An interactive explorer for 109 real genes that let other animals survive what humans cannot, with the evidence for each one rated by how far it actually got`

---

## r/opensource (with the required `Promotional` flair)

**Title:** `Open knowledgebase of 109 enhancement genes across 108 organisms, with a procedural 3D-sculpture generator`
