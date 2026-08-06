# PROJECT.md

**Fill this in before running any prompt.** Every prompt reads this file first. While it still contains `<...>` placeholders, an agent should refuse to draft copy rather than invent a voice for you.

---

## Identity

- **project_id:** `<short-lowercase-hyphenated>`
- **Name:** `<Project name>`
- **Live URL:** `<https://...>`
- **Repo URL:** `<https://github.com/...>`
- **UTM campaign prefix:** `<slug>` — every pillar's `utm_campaign` starts with this

## One-liner

One sentence, no adjectives, no marketing register. What it is, plainly. This gets reused everywhere, so it's worth twenty minutes.

> `<One sentence.>`

## Standing facts

The numbers and claims you repeat everywhere. An agent may use **only** these — it is instructed never to invent a figure. Keep them current, and if the live site disagrees with this list, fix one or the other rather than leaving both.

| Fact | Value | Last verified |
|---|---|---|
| `<e.g. items in the database>` | `<109>` | `<YYYY-MM-DD>` |
| | | |

## Voice rules

How this project sounds. Be specific and prescriptive — vague guidance ("professional but friendly") produces generic output.

- `<e.g. Plain hyphens, not em dashes.>`
- `<e.g. No marketing register. Never "excited to announce".>`
- `<e.g. Lead with the method, not the outcome.>`
- `<e.g. Concrete numbers over adjectives.>`

## Forbidden words

Words that must never appear. Include anything that would get you filtered out of a community by its written rules — these are worth more than style preferences, because a single wrong word can cost you a whole room.

| Never say | Say instead | Why |
|---|---|---|
| `<AI-generated>` | `<algorithmically generated>` | `<Several target subreddits ban AI-generated content outright>` |
| | | |

## Who writes as whom

One row per person who posts in their own name. The point is that two teammates should not sound like one generic voice — say what actually distinguishes them.

| Person | Platforms | Their angle | What makes their voice theirs |
|---|---|---|---|
| `<Name>` | `<linkedin, telegram>` | `<the science / the evidence>` | `<first person, methodology-first, admits uncertainty>` |
| `<Name>` | `<linkedin, instagram>` | `<the design / the object>` | `<visual, process-oriented, shows work in progress>` |

## Canonical tags

Hashtags and topic tags used consistently across platforms, so the project accumulates a findable trail.

`<#tag>` `<#tag>` `<#tag>`

## Goals, in priority order

Ranking these changes which rooms are worth posting in at all. Be honest about the order.

1. `<e.g. Scientist contributors to the open knowledgebase>`
2. `<e.g. Exhibitions and funders>`
3. `<e.g. Press coverage>`
4. `<e.g. Site traffic / players>`

## Assets on hand

What already exists to post: images, videos, PDFs, demos. Candidates reference these in their `media_needed` field, so an accurate list prevents an agent proposing a post you can't actually illustrate.

- `<e.g. video of the printed object, 20s, vertical>`
- `<e.g. sample report PDF>`

## Notes and open questions

Anything an agent should know but that doesn't fit above — unresolved inconsistencies, embargoed news, things not to mention yet.
