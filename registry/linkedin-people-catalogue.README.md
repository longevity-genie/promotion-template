# LinkedIn people and organisations catalogue

`linkedin-people-catalogue.csv` is the outreach reference for LinkedIn *entities* -
company pages, foundations, research groups and named individuals. It is **not** a
posting destination list and it never becomes one: you do not post *into* a company
page you do not admin. What you do with a row here is tag it in a post from a member
profile, ask it to share, pitch it a story, or open a partnership conversation.

Harvested 2026-08-27 by keyword sweeps of LinkedIn company search
(`diabetes technology`, `diabetes nonprofit advocacy`, `diabetes app glucose`,
`type 1 diabetes foundation`, `citizen science open research`) plus one targeted
people lookup. Every `entity_id` in this file was read off a real LinkedIn search
result href - none are guessed.

## Columns

| Column | Meaning |
|---|---|
| `entity_id` | LinkedIn slug. `company/<entity_id>` for pages, `in/<entity_id>` for people. |
| `name` | Name as LinkedIn shows it. |
| `type` | `company-page` / `person` / `showcase`. |
| `url` | Full LinkedIn URL. |
| `country` | Headquarters or primary base, blank where not read. |
| `category` | `advocacy` `media` `professional` `research` `industry` `funding`. |
| `relevance` | `A` core fit · `B` good · `C` marginal · `D` skip. |
| `why_relevant` | Why this entity connects to Sugar-Sugar specifically. |
| `suggested_ask` | The concrete thing to ask for. Not "engage with them". |
| `status` | `uncontacted` / `contacted` / `partner` / `rejected`. |
| `notes` | Verification state and caveats. |

## Rules for this file

- **Official API only, and it does not reach these entities.** `w_member_social`
  posts to your own feed and to pages you admin. Nothing here is postable through an
  API. Every action against a row is a human writing a message, a comment, or an email.
- **No unofficial LinkedIn tooling.** `search_people`, `get_profile`, `send_message`
  and friends are cookie-scraping and risk the account. This file was built with a
  logged-in browser session, by hand, and that is the only sanctioned way to extend it.
- **Public professional identity only.** Record what a person or organisation
  publishes and does. Never record health information about anyone. Livia's own
  disclosure is hers to make and belongs in the post copy, not in this table.
- **Upstream collaborators are not promotion targets.** The CRUISE group row exists so
  the contact is findable and attributed correctly, not so it receives a recruitment
  blurb. `notes` says so on the row; keep that distinction when adding more.

## What the sweep found

Company search is far more productive than people search on LinkedIn. People results
are ranked by the searcher's own network, so a query like
`continuous glucose monitoring research` returns second-degree connections rather than
the field's actual researchers. Named individuals should therefore be added one at a
time, by looking up a specific name you already have a reason to contact - which is how
the single person row here was added.

The strongest non-obvious find is **ECSA (European Citizen Science Association)**.
Sugar-Sugar is a citizen-science study with ethics approval, open code and a European
base; ECSA's project directory and newsletter reach an audience that recruits for
studies as a matter of course, and none of the diabetes rooms do.

## Extending it

1. Search LinkedIn companies in a logged-in browser; take the slug from the result href.
2. Fill `why_relevant` with something specific to Sugar-Sugar. If you cannot, the row is
   a `C` at best.
3. Fill `suggested_ask` with one concrete action. A row with no ask is a bookmark.
4. Cross-check `registry/diabetes-orgs-catalogue.csv` - several organisations appear in
   both, and the org catalogue holds the website and grant information.
