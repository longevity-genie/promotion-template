# Workflow

How this runs week to week, and roughly what it costs in time.

## The loop

```
                    ┌─────────────────────────────────────────────┐
                    │  project/PROJECT.md   (write once, revise)   │
                    │  standing facts · voice · forbidden words    │
                    └──────────────────────┬──────────────────────┘
                                           │  every prompt reads this first
                                           ▼
   prompt 10          ┌──────────────────────────────────┐
   monthly-ish        │  PILLAR   one canonical asset     │
                      │  registry/pillars.csv             │
                      └────────────────┬─────────────────┘
                                       │
   prompt 20          ┌────────────────▼─────────────────┐
   per pillar         │  DERIVATIVES   3-5 native posts   │
                      │  registry/derivatives.csv         │
                      └────────────────┬─────────────────┘
                                       │
   prompt 30          ┌────────────────▼─────────────────┐
   weekly             │  CANDIDATES   one per room        │
                      │  candidates/pending/              │
                      └────────────────┬─────────────────┘
                                       │
                          ╔════════════▼════════════╗
                          ║   YOU read and move it   ║   human-only
                          ║  pending/ -> approved/   ║   no agent does this
                          ╚════════════┬════════════╝
                                       │
   send by hand,       ┌───────────────▼──────────────┐
   or agent sends      │  SENT                         │
   what's approved     │  candidates/sent/             │
   prompt 40           │  + registry/shares.csv row    │
                      └────────────────┬─────────────┘
                                       │  measure_after = +7 days
   prompt 50          ┌────────────────▼─────────────────┐
   weekly             │  MEASURED   outcome per room      │
                      └────────────────┬─────────────────┘
                                       │
                        feeds back into which rooms
                        prompt 30 picks next time
```

## A realistic week

Assume two people with a few hours between them. The point of the structure is that the expensive step happens once a month, not weekly.

**Monday, 20 minutes.** Run prompt `70` (or `30` by hand). You get four or five candidates in `candidates/pending/`, each written for a specific room in its language.

**Monday, 15 minutes.** Read them. Edit the ones that don't sound like you — this is the step that matters, and editing beats regenerating because your edits teach the copy pack. Move what you approve into `candidates/approved/`. Leave the rest; they'll be superseded next week.

**Tuesday to Thursday, a few minutes each.** Send what's approved, spaced hours apart. Capture the message id or permalink as you go. Then prompt `40` to log it.

**Friday, 10 minutes.** Prompt `50`. Anything sent more than a week ago gets measured. After three or four weeks this starts telling you things you didn't know.

**Once a month, a few hours.** Prompt `10` — write an actual pillar. This is the only genuinely expensive step, and everything else is derived from it.

## What the first month looks like

Weeks one and two feel like nothing is happening, because nothing is: you have no baseline, most rooms have a `cap_days` you haven't hit yet, and the durable surfaces (forum showcases, a good Show HN, a published article) pay off over months rather than days. Week three is usually where the `outcome` column starts separating rooms that reliably produce something from rooms that produce reactions and nothing else. Don't retire a room before it has two data points.

## Effort discipline

The failure mode isn't posting too little, it's posting into rooms that never produced anything, week after week, because nobody wrote down that they didn't. Two habits prevent it:

**Respect `cap_days`.** It exists so you're not the person who spams a room. Prompt `30` enforces it automatically.

**Retire on evidence.** Two consecutive `flat` outcomes and the room comes off the active list. Prompt `50` recommends this without being asked. Retiring rooms is what keeps the weekly 20 minutes from becoming 90.

## The three things that break this system

**Skipping the ID capture.** If `platform_msg_id` isn't recorded at send time, that room's numbers are manual forever, and in practice that means never measured. It's five seconds at send time versus a lost data point.

**Editing `shares.csv` optimistically.** Rows go in when something was sent, not when it was drafted. A table containing both is a table you stop trusting, and then the whole exercise is theatre.

**Letting an agent approve its own drafts.** The `pending/` to `approved/` gate is the only thing standing between "an agent drafted forty posts" and forty posts going out in your name. Every prompt is written to refuse this; don't work around it.

## Multiple projects

Each project gets its own clone of this repo. They share the upstream registry, so a room vetted once benefits all of them:

```bash
git fetch upstream && git merge upstream/main
```

Rows marked `scope=template` update; rows you added as `scope=local` stay untouched and don't conflict. If you vet a public room that would help anyone, open a PR upstream — that's what makes the third project cheaper than the second.
