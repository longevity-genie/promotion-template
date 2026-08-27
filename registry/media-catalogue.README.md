# Media and creators catalogue

`media-catalogue.csv` holds the people and publications who could talk *about*
Sugar-Sugar: TikTok and YouTube creators, podcasts, blogs, news sites and
newsletters. It is **not** a destination list. You never post *into* one of these -
you ask its owner for something.

That is the difference from every other file here. A `destinations.csv` row answers
"where do I post". A row in this file answers "who do I write to, and what do I ask
them for". A row with no concrete `suggested_ask` is a bookmark, not a lead.

Harvested 2026-08-27 from published rankings (Feedspot's diabetes TikTok, YouTube and
type-1-blog lists; Beyond Type 1's podcast roundup), then spot-verified on the
platforms themselves.

## Columns

| Column | Meaning |
|---|---|
| `media_id` | Stable slug, prefixed by channel: `tt-` `yt-` `pod-` `bl-`. |
| `name` | Person, show or publication name. |
| `channel` | `tiktok` `youtube` `podcast` `blog` `newsletter`. |
| `handle_or_url` | Profile or site URL. |
| `language` | Content language. |
| `audience` | Followers, subscribers or the platform figures the source gave. |
| `audience_source` | **Where the number came from.** `verified on the platform 2026-08-27` means someone opened the page. `Feedspot list, Aug 2026 - UNVERIFIED` means nobody has. |
| `category` | `creator` `podcast` `media` `advocacy` `research` `industry`. |
| `relevance` | `A` core fit · `B` good · `C` marginal · `D` skip. |
| `bio_or_focus` | What they publish, in their own published words where quoted. |
| `suggested_ask` | The one concrete thing to ask for. |
| `status` | `uncontacted` / `contacted` / `agreed` / `declined`. |
| `notes` | Cross-references and caveats. |

## Two rules that are not optional

**Never record health information about a person.** These rows describe what someone
*publishes* - "public bio: type 1 diabetic / teacher", "listed as T1D content" - not
what they have. Livia's own disclosure is hers to make and belongs in post copy, not
in a table. This is the same rule the project instructions set, and it costs nothing
to follow here because what matters for outreach is the audience, not the diagnosis.

**A ranking is not evidence.** `tt-thecordlefamily` is the cautionary row: Feedspot
lists it first among diabetes TikTok creators at 5M followers, and the bio verified on
the platform says "We love Jesus" with a management contact and no mention of diabetes
at all. Anything carrying `audience_source = Feedspot ... UNVERIFIED` should be opened
before it is contacted.

## What the sweep found

**Podcasts are the strongest channel for this project and the least crowded.** A
30-minute conversation carries an argument that a caption cannot: that no published
human baseline for CGM forecasting exists, so nobody can say whether a model is
actually useful. Four shows fit unusually well - **Diabetech** (a diabetes-technology
show, which is literally the beat), **Think Like a Pancreas** (the book title is the
study's premise), **TCOYD** (hosted by two practising endocrinologists, so the
benchmark argument can be made technically), and **Juicebox**, which is already in
`destinations.csv` for its Facebook group and is the largest audience of the four.

**Several contacts appear on two or three channels.** Justin Eastzer is DiabeTech on
YouTube and Diabetech the podcast. Lauren Bongiorno is a TikTok creator and a podcast
host. Beyond Type 1 is a blog, a YouTube channel, a LinkedIn page and an entry in
`diabetes-orgs-catalogue`. Ask once, for the whole relationship - a second pitch from
the same project to the same person on a different platform reads as a mailing list.

**T1D Exchange is the highest-leverage row in the file and is not media at all.** They
run a patient registry. Recruiting roughly 200 adults is a small ask against a registry,
and a registry conversation is worth more than any single article.

**The recruitment-shaped hook is exercise.** Deciding whether to eat before a workout
*is* the next-hour prediction problem, stated in the words people already use. It is
why the sport and fitness creators (`liv_violette`, `ftfwarrior`, Diabetes Strong) are
rated A despite smaller followings than the lifestyle accounts.

## Extending it

1. Open the profile or site. Fill `audience_source` honestly.
2. Write `bio_or_focus` from what they actually publish. Quote their bio if it is short.
3. Write one concrete `suggested_ask`. "Engage with them" is not an ask.
4. Check whether the person is already in this file under another channel, or in
   `linkedin-people-catalogue.csv` / `diabetes-orgs-catalogue.csv`, before adding a row.
