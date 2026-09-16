# Workshop venues catalogue

`workshop-venues-catalogue.csv` holds places where **Livia can stand in a room with
people, get them to play Sugar-Sugar, and hand a 3D-printed souvenir to whoever
predicts best** — medical schools, student societies and their congresses, diabetes
patient organisations, professional societies, AI and data events, science festivals
and one makerspace. Mostly Romania, plus Chisinau and two international entries.

It is **not** a destination list. Nothing here is postable through any API. Every row
is a room you have to be invited into, so the unit of work is an email or a call for
proposals, not a scheduled post.

Researched 2026-09-17 from web searches in Romanian and English. Verified against the
organisations' own pages wherever one could be fetched; rows where only press coverage
was found say so in `notes`.

## Why this file exists

It came out of something that already worked once: Livia ran a Sugar-Sugar workshop at
a conference, people played, and everyone who played got a souvenir printed at home on
the team's own 3D printer. There is still a stock of them. That is a repeatable format
with a zero-cost prize attached, and this file is the list of rooms to repeat it in.

The format has two halves, and most rows take only one:

- **The play half** — a room plays a full session, then the room's own MAE goes on a
  slide against the GlucoBench 60-minute figures in `project/PROJECT.md`. Souvenir to
  the best predictor, or to everyone if the room is small.
- **The teaching half** — a lecture on time-series machine learning, using the study
  as the worked example. Only for AI-adjacent rooms: `format = ml-masterclass` or
  `talk`.

`souvenirs` says whether the printed prize fits: `yes` for stands, workshops and
meetups where people play in the room; `limited` for a lecture where they play but the
setting is formal; `no` for a conference stage.

## Columns

| Column | Meaning |
|---|---|
| `venue_id` | Stable slug, prefixed `ws-`. |
| `name` | Venue, event, organisation or department. |
| `type` | `student-congress` / `student-org` / `university-dept` / `professional-society` / `patient-org` / `tech-conference` / `summer-school` / `science-festival` / `makerspace` / `community` / `campaign-window`. |
| `city` | City, or the geography the event rotates through. |
| `country` | `RO`, `MD`, `intl`. |
| `audience` | Who is actually in the room, with a headcount where one is published. |
| `language` | The language the session would run in. |
| `url` | The page the row was verified from. |
| `contact` | Email, phone or call-for-speakers link, where one is published. Blank means none was found — it does not mean none exists. |
| `relevance` | `A` core fit · `B` good · `C` marginal. |
| `format` | `workshop` / `congress-workshop` / `guest-lecture` / `ml-masterclass` / `talk` / `demo-stand`. |
| `timing` | When it recurs, and the last edition's dates where known. |
| `why_relevant` | Why this room, for this study, in one paragraph. |
| `suggested_ask` | The one concrete thing to ask for. |
| `souvenirs` | `yes` / `limited` / `no` — whether the printed prize fits the format. |
| `status` | `uncontacted` / `contacted` / `proposal-sent` / `scheduled` / `done` / `declined`. |
| `notes` | Verification caveats, cross-references, and what still needs checking. |

## What the research found

**The Romanian medical student congress circuit is dense and it runs in spring.**
Medicalis (Cluj, March), Zilele Educatiei Medicale (Bucharest, March), MEDICIS (Iasi,
March), KronMed (Brasov, March), MEDIS (Timisoara, April), MedEspera (Chisinau, May)
and BENG (Iasi, May) all fall between March and May. The 2026 editions have all
passed. This file is therefore a **spring 2027 plan**, and the proposals have to go out
in autumn 2026 — which is now.

**Two of them already have the theme.** MedEspera 2026 ran under "Building a New Era
of Medicine with AI" and carried 74 workshops. The 52nd SRDNBM national congress ran
under "Diabetes in the era of TECH innovation and Artificial Intelligence". Neither
needs convincing that a human-versus-model benchmark belongs on the programme.

**MedEspera is the only row with a published workshop contact.** `medespera@usmf.md`.
Every Romanian student congress announces through Facebook and a university events
page and hides the organising team behind a form. Expect the first contact to be a
message to a student society, not an email to a conference secretariat.

**One named academic contact stands out.** Prof. dr. Gabriela Roman heads the diabetes
discipline at UMF Cluj, publishes `groman@umfcluj.ro`, and the department's stated
research interests include technology and telemedicine in diabetes management. That is
the closest thing in Romania to a department whose own agenda already contains what
this study measures.

**Cluj is the trip that pays for itself.** UMF Cluj diabetes, UBB computer science,
IT Days at Cluj Innovation Park (11-12 November 2026), the Cluj AI meetups and the
Cluj edition of Noaptea Cercetatorilor are all in one city. Timisoara is the second
cluster: UMFT diabetes, UPT's machine learning MSc, and MEDIS.

**Noaptea Cercetatorilor Europeni is the best format match in the file.** One night
each September, ten hours, public, free, and the existing stands already include 3D
printing next to medicine. A table with two laptops and a bowl of printed souvenirs is
the native idiom there rather than an intrusion. The 2026 edition is 25 September —
too late to register a stand, early enough to go and watch how they are run.

**Meetups are the fastest route from ask to stage.** A Cluj or Bucharest AI meetup can
say yes in a week. Run the lecture there first, find out which parts land, then propose
the tested version to a congress.

**Pint of Science does not run in Romania.** Romanian press reported this in 2026. The
format — adults, in pubs, three evenings in May — fits this study better than anything
else found, which is why the row stays in the file, marked `C`.

## The age problem, stated once

The study enrols adults only. Three row types are affected:

- **Science festivals** (`ws-noaptea-cercetatorilor`, `ws-romanian-science-festival`,
  `ws-bucharest-science-festival`) draw large numbers of under-18s. They can play; they
  cannot be enrolled. Their accompanying adults can.
- **ASCOTID Mures** is a paediatric and young-adult association. Only the over-18 tail
  and the parents are eligible.
- **Sprijin pentru Diabet** leans towards insulin-dependent children.

Say this explicitly in the first message to any of them. An organisation that finds out
afterwards that half its audience was ineligible will not invite you twice.

## Priority order

**Now (autumn 2026):**
1. Prof. Gabriela Roman, UMF Cluj — the strongest named contact in the file
2. `medespera@usmf.md` — the only published workshop route
3. SSMB Bucharest — one approach covers both ZEM and IMSCB
4. IT Days Cluj (11-12 November) — nearest large event; ask for a lab or a table
5. Two or three patient organisations for 14 November tables
6. A Cluj or Bucharest AI meetup — to run the lecture once before pitching it

**Winter 2026-27:** workshop proposals to Medicalis, MEDIS, KronMed, BENG; abstract and
workshop enquiry to SRDNBM for the May 2027 congress; stand application to the Cluj
Noaptea Cercetatorilor consortium for September 2027.

**Opportunistic:** DevTalks and DevCon Sessionize submissions — public CFPs, low effort,
low expected recruitment yield.

## Cross-references with existing catalogues

- SRDNBM → `srdnbm-ro` in `diabetes-orgs-catalogue.csv`
- FRDNBM → `frdnbm-ro` in `diabetes-orgs-catalogue.csv`
- ASCOTID Mures → `ascotid-ro` in `diabetes-orgs-catalogue.csv` and `web-ascotid` in
  `media-catalogue.csv` — check what has already been sent before writing
- Forumul Roman de Diabet → `fo-forumdiabet` in `destinations.csv` (on-hold)
- Romanian clinician creators who could publicise a workshop → the `ig-ro-*` rows in
  `media-catalogue.csv`

## Rules for this file

- **Nothing here goes in `shares.csv`.** That table is for posts that were sent. A
  workshop that happened is recorded by moving `status` to `done` and writing what
  happened in `notes`.
- **Professional contact details only.** Published university emails and switchboards.
  Never record anything about any person's health, including a speaker's own.
- **A blank `contact` is a task, not a fact.** It means nobody published one on the
  pages that were fetched.
- **Verify a date before you write it into a message.** Every 2026 date in this file is
  from a source page, but editions move.
