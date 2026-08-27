# Reddit posts

> Standing facts and voice rules: see [PROJECT.md](../project/PROJECT.md) and [copy-pack.md](../project/copy-pack.md).
> In r/InternetIsBeautiful do not say "game".

## Timing

**Matters significantly for self-posts; less for link posts.** Reddit's algorithm heavily weights early upvotes in the first 1-2 hours. Best window: 06:00-09:00 US Eastern = **13:00-16:00 Bucharest time** on weekdays (Tue-Thu best). Weekends are fine for hobby/interest subs (r/transhumanism, r/generative) but worse for science subs. **For important posts (r/transhumanism, r/AskScienceDiscussion): aim for Tue-Thu 13:00-16:00 Bucharest. For niche subs: post any time, the audience is small enough that timing barely matters.**

## Initial engagement - DO NOT DO THIS

**Reddit vote manipulation is bannable for both accounts AND domains.** Never ask anyone to upvote a Reddit post. HN has the same rule. One incident can get the enhancement.bio domain flagged site-wide. The only thing you can do: be online to reply to early comments quickly (within 30 min). Fast, substantive replies are the one legitimate engagement signal you control.

---

## r/transhumanism (self-post, one image)

**Posted 2026-08-25:** [live post](https://www.reddit.com/r/transhumanism/comments/1vy0dtb/bringing_together_the_evidence_on_human_gene/) · [sent record](../candidates/sent/2026-08-25-reddit-rd-transhumanism.md). Early snapshot reported by Anton: 11 upvotes, no downvotes and 4 comments. Outcome is still too early to judge.

**Title:** `Bringing together the evidence on human gene enhancement, from early experiments to therapies already offered to adults`

> When I was a kid, I kept reading about tardigrades surviving radiation, naked mole-rats barely ageing, axolotls regrowing limbs, and so on. I assumed we would eventually learn how to borrow some of those abilities.
>
> I came back to this first when I started the Ukrainian transhumanist community, and later when I got into bioinformatics for ageing research. I expected there would already be an open list of genes people were considering for human enhancement, together with the experiments behind them. There was not, so we started making one.
>
> Right now it has 136 genes and 1,134 experiments, with links to papers and our ratings of how far the evidence got. We also made pipelines for extracting data and agents that help us process papers.
>
> One thing that surprised me is that not all of this is hypothetical. Eight therapies in the database are already sold to adults. In alternative jurisdictions such as Prospera, people are receiving follistatin and VEGF gene therapies. A lot of transhumanists I talk to do not seem to know this is already happening.
>
> The science-fiction motivation never went away, so we added some RPG-style character-building elements. You get 100 credits, pick genes, build a character, and get a 3D-printable sculpture based on your choices. It is a way to explore the genes and their trade-offs, rather than a full RPG.
>
> Everything is open source, including the code and the database. We would be glad to hear what people here think. If anyone wants to help us expand it or share the project with other transhumanists, please get in touch.
>
> https://enhancement.bio

### Follow-up comment: what the RPG elements are

> I wanted to share a bit more about the project, since I skipped most of its history in the post. We actually started it as an art project during the CODAME ART+TECH "The New Human" hackathon at Milano Design Week. The initial idea was to choose possible genetic enhancements, turn those choices into a generative object, and then 3D-print it.
>
> After the hackathon, as we kept adding genes and papers, we realized that the knowledgebase was actually more useful to people than the 3D-printing part. That changed where we put most of the work: collecting experiments, linking the papers, and showing where the evidence for each claim stops - cells, animals, primates, humans or something already offered on the market. We now use extraction pipelines and agents to help process the papers, while keeping the data open for review and corrections.
>
> The art part is still there, but now it is mostly a way into the science. This is also why calling it "a small RPG" was imprecise. It is an RPG-style character creator, not a full RPG: you have 100 credits and choose genes as abilities, but there are no quests, combat, progression or PvP. Your choices generate a Voronoi object that you can download and 3D-print.
>
> Short project video: https://youtu.be/ev726lz5sLo
>
> Live project: https://enhancement.bio
>
> Knowledgebase: https://www.dolthub.com/repositories/longevity-genie/enhancement-bio
>
> Code: https://github.com/longevity-genie/materialized-enhancements

---

## r/generative and r/creativecoding (image or video)

**Title:** `Voronoi sculptures grown from real gene data - protein mass, exon count and disorder become the shell parameters`

> Each shape comes from a set of genes someone picked in the character generator. Protein mass, exon count, GRAVY score, intrinsic disorder, isoelectric point and category size seed and parameterise a Voronoi shell.
>
> The hard constraint was printability. Every result across a large combination space has to slice and print on a weak machine without a person checking it first. That constraint shaped the geometry more than any aesthetic decision.
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

> I work on aging genomics and have been cataloguing experiments on genes that let other animals survive things we cannot - tardigrade Dsup, naked-mole-rat hyaluronic acid, elephant multi-copy TP53, bowhead-whale CIRBP and axolotl Lin28a. The database now has 1,134 experimental records.
>
> The pattern that keeps coming up is that popular coverage collapses a translational ladder into a binary. Dsup shields DNA from radiation damage and also behaved badly in nerve cells. FOXO3 has a strong human longevity association, but direct enhancement evidence is thin. Elephant TP53 may carry an ageing cost that the cancer story leaves out.
>
> My question for people who work adjacent to any of these: which ones do you think we, collectively, oversell most? And are there organisms whose adaptations get ignored because the mechanism is anatomical rather than genetic?
>
> Our notes are open if useful, but I am mainly after the arguments.

---

## r/coolgithubprojects (link post)

**Title:** `Materialized Enhancements - open, evidence-rated knowledgebase of 136 human enhancement genes, with a playable character generator`

Link the **repo**, not the site.

---

## r/InternetIsBeautiful (link post - the word "game" must not appear)

**Title:** `An interactive explorer for 136 real genes that let other animals survive what humans cannot, with the evidence for each one rated by where it stops`

---

## r/opensource (with the required `Promotional` flair)

**Title:** `Open knowledgebase of 136 enhancement genes across 72 source species, with a procedural 3D-sculpture generator`

---

## Gene meme posts (use meme as the post image)

These work as standalone posts in subreddits that allow images, or as follow-up posts weeks after the initial introduction. One gene per sub, pick by topic fit. Attach the meme image and write a self-post body.

### r/transhumanism — Dsup meme

**Image:** `images/dsup2_chat_gpt.jpg`

**Title:** `Tardigrade Dsup halves DNA damage in kidney cells. In rat neurons it promoted double-strand breaks and killed them. Same gene.`

> The tardigrade damage-suppressor protein works beautifully in some cell types. In others, the mechanism reverses and the gene becomes destructive. Nobody knows why.
>
> This is one of the reasons we split evidence ratings by tissue and claim instead of giving each gene a single score. The pattern repeats across dozens of genes in the database — what works in one context fails or reverses in another.
>
> 136 genes, 1,134 experiments, open under MIT: https://enhancement.bio

### r/transhumanism — GHR/Laron meme

**Image:** `images/ghr_therapy.jpg`

**Title:** `GHR deficiency: zero diabetes, cancer absent as cause of death in a 22-year cohort. The cost: minus 35 cm height and zero added lifespan.`

> Laron syndrome is one of the sharpest trade-offs in human genetics. A 22-year prospective study of 90 people with GHR deficiency found no diabetes and no cancer deaths. They also had fewer arterial plaques despite elevated LDL.
>
> The catch: 70% of deaths were non-age-related (convulsions, alcohol, accidents), and vascular disease killed them at the same rate as unaffected relatives. The protection didn't translate to longer life.
>
> https://enhancement.bio

### r/biohackers — MSTN meme

**Image:** `images/myostatin.jpeg`

**Title:** `Myostatin knockout: spectacular in mice, cattle, and dogs. Every antibody drug targeting the same pathway in humans failed.`

> Stamulumab (MYO-029): disappointing Phase 2 in adult muscular dystrophy. Domagrozumab: Phase 2 terminated in Duchenne boys. CRISPR in primates showed mosaicism. The knockout also shifts fiber type from slow oxidative to fast glycolytic — power at the cost of endurance.
>
> We rate 136 enhancement genes by how far the evidence got, not how exciting the mouse data looked: https://enhancement.bio

### r/longevity or r/LifeExtension — Klotho meme

**Image:** `images/klotho_chat_gpt.jpg`

**Title:** `One copy of Klotho KL-VS improves cognition. Two copies make you worse. Seven companies are selling it.`

> Classic overdominance. The protein injection improved memory in aged mice and macaques, but at high dose the benefit disappeared. Narrow therapeutic window that nobody has mapped.
>
> This is one of 136 genes in an open, evidence-rated knowledgebase: https://enhancement.bio
