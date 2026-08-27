# LinkedIn drafts - TODO

## Images to prepare

- [ ] `showcase/page-01-knowledgebase-launch.png` - screenshot of enhancement.bio knowledgebase showing gene list with evidence ratings
- [ ] `showcase/page-02-ai-assistants.png` - screenshot of a gene page with Ask GPT and Ask Claude buttons visible, ideally mid-conversation
- [ ] `showcase/page-03-credit-budget.png` - screenshot of build view showing credit budget, gene selection with costs, remaining credits
- [ ] `showcase/page-04-sculpture-from-data.png` - sculpture render or photo of a printed sculpture (physical print preferred)
- [ ] `showcase/page-05-gamification.png` - screenshot of build flow mid-game with some genes chosen and budget partially spent
- [ ] `showcase/page-06-companies-building-it.png` - screenshot of knowledgebase filtered to market/clinical-trial genes, or infographic of 8 marketed therapies
- [ ] `anton/anton-evidence-ladder.png` - screenshot of a gene page showing split evidence ratings (e.g. FOXO3 or Dsup)
- [ ] `livia/livia-generative-design.png` - sculpture render or photo of Voronoi shell geometry (Livia wearing it is ideal)

## Before posting

- [ ] Verify all links resolve (enhancement.bio, GitHub repo)
- [ ] Verify LinkedIn company handles for page-06 tags
- [x] Confirm showcase page URL: https://www.linkedin.com/showcase/138363945/
- [x] Confirm company page URL: https://www.linkedin.com/company/106920105/
- [ ] Coordinate with Livia, Newton, Markel for first-hour engagement

## Scheduling

- [x] LinkedIn scheduling tested 2026-08-11 - shr-0001 went out **via Buffer**, not the native composer scheduler. The native scheduler is still untested.
- [ ] Test the native LinkedIn scheduler (clock icon in the composer) on the next personal post, so there is a fallback if Buffer's LinkedIn integration breaks.
- [ ] Note: neither the native scheduler nor Buffer can reach a **group** composer. Group posts are sent live, one at a time.

## Fix the first post (shr-0001, published 2026-08-11)

Two defects logged in `registry/shares.csv`:

- [ ] **Wrong figure, still live.** The published text says "80 real genes from 108 organisms". The current figure is **106 playable genes from 72 source species**; 109 is the organisations count. Edit the live post in place.
- [ ] **Untagged link.** It went out as a bare `https://enhancement.bio` with no UTM, so its clicks are unattributable and the `clicks` column will stay blank. Editing a LinkedIn post does not retroactively tag clicks - accept the loss on this one and never send an untagged link again. Every candidate now carries `link_used` in its frontmatter for exactly this reason.
- [ ] Showcase page and Longevity Genie page reshares of shr-0001 are drafted but not sent.

## LinkedIn groups (new surface, added 2026-08-11)

Inventory and rules: `registry/linkedin-groups-catalogue.csv` and its README. Mechanics: the Groups section of `page-strategy.md`.

**Read first:** there is no Groups API, no scheduler reaches a group, and a showcase page cannot post in one. Groups are a manual surface.

Drafted and waiting in `candidates/pending/`, one distinct variant per room:

- [ ] `2026-08-11-li-grp-hplus.md` - h+ Community (1,162)
- [ ] `2026-08-12-li-grp-genetics-network.md` - Genetics Network, gene therapy (5,848, public)
- [ ] `2026-08-13-li-grp-human-genetics.md` - Human Genetics (11,072)
- [ ] `2026-08-18-li-grp-ai-genetics.md` - AI and Genetics (2,247)
- [ ] `2026-08-19-li-grp-genetics-genomics.md` - Genetics and Genomics (106,226) **strictest room, read the pin before sending**
- [ ] `2026-08-20-li-grp-ila.md` - International Longevity Alliance (1,152)

Join requests to send (not a member yet, admin-gated, so start the clock now):

- [ ] Biopharma and Biologics and Cell and Gene Therapy (48,529)
- [ ] Gene, Cell and RNA Therapy Strategy Network (18,591)
- [ ] ISCT - International Society for Cell & Gene Therapy (17,641)
- [ ] CRISPR and Gene Editing Tools (3,332)
- [ ] Synthetic Biology (6,954)
- [ ] SynBioBeta: Synthetic Biology Community (5,618)
- [ ] Human Longevity and Aging Research (4,073)

After each send: move the candidate to `candidates/sent/`, fill `platform_msg_id` and `permalink` in its frontmatter, append the row to `registry/shares.csv`, set `last_posted` on the destination row, and run `scripts/check_registry.py`.
