# LinkedIn Page Strategy - enhancement.bio showcase

> Standing facts and voice rules: see [PROJECT.md](../../project/PROJECT.md) and [copy-pack.md](../../project/copy-pack.md).
> Groups are a separate surface with separate mechanics - see [LinkedIn groups](#linkedin-groups-a-different-surface-entirely) below and `registry/linkedin-groups-catalogue.README.md`.

## Page identity

- **Showcase page:** https://www.linkedin.com/showcase/138363945/
- **Parent company:** https://www.linkedin.com/company/106920105/ (Longevity Genie)

The page voice is the project's voice, not Anton's or Livia's. Third person plural ("we") or impersonal ("the knowledgebase rates..."). More institutional than the personal profiles but still plain language, not press-release register.

## Draft channels

- `showcase/` - institutional posts published by the enhancement.bio showcase page
- `anton/` - native posts written in Anton's personal scientific voice
- `livia/` - native posts written in Livia's design-process voice
- `anton-reshares/` - Anton's short personal commentary when resharing a corresponding showcase post

Reshare drafts use the same numbered slug as their source in `showcase/`. They are commentary attached to a reshare, not comments posted under the original.

## Articles vs native posts

**Lead with native posts, not articles.** Articles live on a separate tab and get minimal feed impressions in the first 48 hours, while native posts are distributed in the feed. The tradeoff:

> UNVERIFIED: an earlier version of this file claimed native posts are distributed "3-5x more" than articles. No LinkedIn-owned source states that multiplier and it should not be repeated as fact. The direction of the effect is well attested; the number is not.


| Format | Feed reach | Google indexing | Shelf life |
|---|---|---|---|
| Native post | High (first 48h) | No | Dies after ~1 week |
| Article | Low (feed) | Yes, indexed | Months to years |

**The play:** Launch with 4-6 native posts to build page followers and engagement signals. Once the page has some traction (50+ followers, consistent reactions), publish an article version of the evidence-ladder piece as a durable, Google-indexed asset. The article becomes the thing you link from other platforms when someone asks "what is this project?"

## Posting cadence

**One page post per week**, staggered against the personal profiles:

- Monday/Tuesday: Anton's personal post
- Wednesday/Thursday: Page post (reshared from the page, not from Anton)
- Following week: Livia's personal post if scheduled

This avoids cannibalizing engagement between the page and personal profiles.

## Engagement protocol

Same as the personal posts but adapted for a page:

1. **Immediately after posting:** Anton, Livia, Newton each react and comment from personal profiles within 60 minutes. Comments from personal profiles on a page post are the strongest signal.
2. **Within 2 hours:** Anton reshares to personal feed with a one-line comment.
3. **Same day:** Livia reshares to personal feed if the post touches design.
4. **Cross-post to Longevity Genie company page** 2-3 hours after the showcase post.

## Content mix for the page

The page can post things the personal profiles cannot:

- **Knowledgebase updates** - new genes added, ratings revised, experiments catalogued
- **Numbers and milestones** - without it feeling like self-promotion (a page announcing its own stats is expected)
- **Community contributions** - highlighting when someone submits a correction or gene nomination
- **Feature announcements** - AI assistant integration, new organism categories, UI changes
- **Gene-of-the-week reposts** - condensed versions of the personal-profile gene posts

## Hashtag set for page posts

`#OpenScience` `#Genomics` `#SciComm` `#ComparativeBiology` `#longevity` `#generativeart` `#creativecoding`

Use 3-5 per post, not all seven. Pick the ones that match the post's angle.

## What not to do

- Don't post the same text as the personal profiles. Rephrase for the project voice.
- Don't post more than twice a week from the page. Showcase pages with low follower counts get penalized for high frequency.
- Don't use the page to reshare external links without commentary. Native text with the link in the body outperforms link-only shares.
- **Don't plan to post from the page into a LinkedIn group.** It is not possible. See below.

---

## LinkedIn groups: a different surface entirely

Groups are not the page and not the feed. Almost nothing above applies to them.

### Three hard constraints

1. **No API.** The LinkedIn Groups API was shut down in 2017 and never replaced. The `w_member_social` scope this repo is authorised for reaches the personal feed and pages you admin - nothing else. No third-party scheduler, Buffer included, can post into a group.
2. **No scheduling.** The clock icon exists in the feed and page composers. It does not exist in the group composer. Every group post is sent at the moment it is written.
3. **A page cannot post in a group. Only a member profile can.** So group posts are Anton's or Livia's, never the showcase page's, and they cannot be reshared from the page either - a post inside a private group is invisible outside it.

That leaves exactly one route: a human typing into the group composer, or a browser-automation agent driving a logged-in session. Treat group posting the way this repo treats WhatsApp and third-party Discords - manual surface, drafted in advance, sent by hand.

### The rooms

Full inventory, relevance grading and rules in `registry/linkedin-groups-catalogue.csv`; the A-tier is promoted into `destinations.csv` as `platform=linkedin-group`, `status=on-hold`.

The finding worth internalising: **the H+ vertical barely exists on LinkedIn.** The largest explicitly transhumanist group is `h+ Community` at 1,162 members. The next is 348. One 401-member group is organised against transhumanism. LinkedIn is where the genetics and gene-therapy professionals are - six gene-therapy groups over 7,000 members, the largest at 48,529. Transhumanism stays on Telegram, Facebook and Reddit.

### Cadence and spacing

- **One group per day at most**, and no more than three groups in a week.
- `cap_days=30` per room. The genetics rooms overlap heavily in membership; posting the same pillar to Genetics and Genomics, Human Genetics, AI and Genetics and Genetics Network inside one week reads as spam to the people in all four, whatever any single group's rules say.
- Vary the opening line and the fact you lead with, per room. Same rule as Telegram, same reason.
- Stagger against the personal-feed and page cadence. A group post and a feed post on the same day compete for the same first-hour attention from the same small set of colleagues.

### Approval queues

Several groups hold member posts for admin review: both Bioinformatics groups, Singularity University, ISCT, Gene/Cell/RNA Therapy Strategy Network, SynBioBeta. A queued post appears days later or never. Check back after 48 hours. **Do not repost** if it has not appeared - message an admin instead.

### Reading the rules

LinkedIn's group rules field is almost always empty - it was empty for every group in the 2026-08-11 sweep. The real rule lives in a **pinned admin post**. Read the pins, not the rules tab. The sharpest one found:

> Genetics and Genomics (106,226 members): "It is not the place to post spam! Doing so will get you blocked and your post deleted." - alongside an explicit welcome for "relevant articles, peer-reviewed papers, webinars, events, call for papers".

That is the model for the whole set: share a resource, not a product.

### Boosting

`boost_ok=risky` on every group row, same as the personal profiles. LinkedIn removes groups that show engagement-pod behaviour. Ask individuals, never reciprocally, never as a batch.
