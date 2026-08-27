# UTM convention

Follow this exactly or the click data becomes unreadable. UTM values are case-sensitive in every analytics tool, so `RD-Generative` and `rd-generative` become two separate rows in every report, splitting one room's traffic in half.

**All values lowercase, hyphen-separated.** No exceptions.

## The five parameters

| Parameter | What it holds | Example | Rule |
|---|---|---|---|
| `utm_source` | the specific community, one per room | `rd-generative` | Always equals the `utm_source` column in `destinations.csv`. One value per room, never reused for a different room. |
| `utm_medium` | the class of surface, not the platform | `community` | One of: `social`, `community`, `forum`, `newsletter`, `dm`, `press`. This is what lets you compare classes of surface against each other. |
| `utm_campaign` | the pillar asset slug | `evidence-ladder` | Equals the `utm_campaign` column in `pillars.csv`. Every share of the same pillar carries the same campaign, which is how you compare rooms fairly. |
| `utm_content` | **the share id** | `shr-0042` | Always equals `share_id` in `shares.csv`. This is the whole trick. |
| `utm_term` | unused | — | Leave empty. It's a paid-search field; using it for anything else creates confusion later. |

## Why `utm_content = share_id` matters

It's the one mechanism that makes a single click traceable to a single post in a single room. Without it you can tell that Reddit sent forty visitors; with it you can tell that thirty-eight came from one specific post in one specific subreddit and the other two subreddits sent nothing — which is the difference between "Reddit works" and "one room works."

`scripts/check_registry.py` enforces the equality, because it's easy to break by hand and silently useless once broken.

## Full URL shape

```
https://sugar-sugar.study/?utm_source=li-anton&utm_medium=social&utm_campaign=sugar-human-baseline&utm_content=shr-0001
```

## Choosing what to link

Read the `link_target` column on the destination row:

- `pillar` — the site or the long-form article. Use for cold and scientific rooms; they want the thing itself, not your post about it.
- `post` — your own LinkedIn or Facebook post. Use for warm rooms, to concentrate engagement where it feeds the platform's ranking.
- `repo` — GitHub. Use for developer and open-source rooms.
- `none` — no link at all. Some rooms (a genuine question on r/AskScienceDiscussion) work better without one, and some ban links outright.

## Known gotcha worth planning for

When a reader copies your tagged link and reshares it elsewhere, the UTM travels with it and misattributes those clicks to the original room. The standard mitigation is a small client-side script that strips UTM parameters from the address bar after the analytics hit fires. Worth adding once share volume makes the noise matter — not on day one.

## Why bother at all

Without this, "which rooms actually work" is unanswerable, and you keep posting into dead ones indefinitely. With it, the question becomes a filter, and the 90-day review takes fifteen minutes instead of an afternoon of guessing.
