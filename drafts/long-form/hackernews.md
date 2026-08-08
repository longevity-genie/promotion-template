# Hacker News - Show HN

> Standing facts and voice rules: see [PROJECT.md](../../project/PROJECT.md) and [copy-pack.md](../../project/copy-pack.md).

**This is the one thing in this pack you must not paste.** HN's moderator updated the canonical Show HN guidance on 28 March 2026 with: *"Write your text by hand. Don't use an LLM to generate any of it (not even a tiny bit, including to edit or spruce it up). Reason: the community is super fussy about this right now, and LLM language leaves imprints on your text which are generating quite some backlash... This is a big dividing line at present!"*

So here is the structure and the raw material. Write the prose yourself, in your own voice, in one sitting, without polishing it.

**Title:** `Show HN: Materialized Enhancements - design an enhanced human from real genes`

**What the body needs to contain, in this order:**

1. **What it is, plainly, in one sentence.** No adjectives. "You get 100 credits and a library of real genes from real organisms, and you spend them building a person."
2. **The backstory - dang explicitly asks for this.** The art hackathon called "The New Human". You are an aging researcher; Livia is a parametric designer. She proposed the thing that became the heart of it: generate a unique printable shape from each person's choices. Say why you personally cared: the childhood question about which animal superpowers are real.
3. **The constraint that makes it work.** 100 credits is not enough to max anything out. Because every credit is a real choice, people read the science before spending it. That is the whole design thesis, and it was confirmed at Milano Design Week where non-biologists crowded around it and read the entries on most genes.
4. **The honest part - this is what HN will actually respect.** You rate by how far up the translational ladder a claim got, not works/doesn't. Same gene, different ratings for different claims. Give one concrete example, and pick an unflattering one: AQP1, the water-holding frog aquaporin, is in the library as a case study in how a plausible enhancement story gets assembled entirely from sources that do not support it - the frog's own aquaporin has never been cloned or characterised, and in dormancy the expression goes *down*, not up. Or FOXO3: strongest human longevity association in biology, and nobody has ever put it in a mammal and measured lifespan.
5. **The technical bit.** Gene parameters (protein mass, exon count, GRAVY score, disorder, pI, system size) feed a generative Voronoi algorithm you wrote, which grows a shell that has to print cleanly on weak machines across a huge combination space. Say what the stack is.
6. **What you want.** Gene nominations and evidence corrections from anyone who knows a corner of this literature better than you do. Point at the labelled issues in the repo.
7. **What is not done yet.** Protein-shape printing, a jigsaw layer built from the source organisms, generated example plasmids. Being straight about the roadmap reads far better than pretending it is finished.

## Initial engagement - DO NOT DO THIS

**Never ask anyone to upvote on Hacker News.** HN penalises **sites**, not just accounts - one solicited upvote can get the enhancement.bio domain flagged permanently. The only thing you can do: be online and reply to every comment substantively within the first 3 hours. Fast, thoughtful replies are the only legitimate engagement lever.

**Before you post:** confirm the core loop needs no signup, block out three hours to answer every comment, and put your email in your HN profile so dang can send a repost invite. If it sinks, email `hn@ycombinator.com` about the second-chance pool rather than reposting.
