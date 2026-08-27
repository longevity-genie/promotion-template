# Copy pack

The voice model, plus copy that already exists and can be reused or adapted. An agent reads this alongside `PROJECT.md` before drafting anything, so what's here shapes everything downstream.

---

## Why this file exists

Several people and at least two AI harnesses will draft text for this project. Without a fixed reference, output drifts toward generic marketing register, and posts written in January stop sounding like posts written in June. This file is what a fresh agent with no memory of prior conversations reads before writing, so post #40 sounds like post #4.

---

## Register by audience

**People with diabetes / CGM users**
> Lead with the next hour: food, insulin, staying safe. Never lead with machine learning. They already predict glucose all day; we are asking them to put that skill on a chart so researchers finally have a number. They are put off by app-store promises, dosing claims, and anyone who sounds like they are teaching them their own disease.

**People without diabetes / wellness / sport CGM**
> Lead with the mechanic: you see three hours, you draw the next one, you find out how far off you were. Glucose is a metabolic signal, not only a diabetes number. Do not lecture them about prevention.

**Scientists / glucose-ML researchers**
> Lead with the missing human baseline. GlucoBench reports 60-minute RMSE 10-16 mg/dL and MAE 9-13 mg/dL on academic sets; nobody published how well an informed human does on the same horizon. They care about protocol, ethics reference A 2026-0064, and whether the task is 6-12 repeated trials. They are put off by "fun game" as the first line.

**Developers / open source**
> Lead with the repo and the stack (Plotly Dash, Apache-2.0). Mention file-format work and localisation. Do not invite drive-by protocol changes.

**Diabetes organisations / clinic contacts**
> Lead with ethics clearance, the non-interventional design, and the 18+ / GDPR consent. Be concrete: historical traces, no treatment, hosted by HEALES, data at Universitätsmedizin Rostock. Overstating clinical utility is the fastest way to lose a serious one.

---

## Voice samples

### Anton Kulaga - the study and the missing baseline

> Machine-learning papers keep publishing next-hour glucose errors, and I kept looking for the human number they were supposed to beat. I could not find one. People who wear a CGM already guess the next hour every day - food, insulin, a walk - and nobody had asked them to draw that guess on a chart and keep the score. So we built a small game that does exactly that: three hours of context, twelve points for the hour ahead, six to twelve rounds so one lucky segment does not become a person. Ethics clearance is A 2026-0064 from Rostock. If you play, you leave a baseline a model can actually be compared to.

### Livia Zaharia - the game and the drawing task

> The only way this study works is if people finish more than one round, so I did not want another form. You click the chart and pull the line where you think glucose will go. Then the real trace appears and you see the gap. That is the whole instrument. We made it a game because a questionnaire does not get you six to twelve forecasts, and without those repeats the score is noise.

### Newton Winter - the stack

> It is a Dash app. Public traces, your own file, or a mix. When you finish, the share page is a real URL with a 1200 by 630 card, not a screenshot you have to crop. If a CGM export fails, open an issue - that is a study-quality bug, not a nice-to-have.

---

## Standing copy

**One-liner** (matches `PROJECT.md`)
> A browser game that measures how well people can predict the next hour of a CGM trace, so machine-learning models finally have a human baseline to beat.

**Two-sentence version**
> Sugar-Sugar shows you three hours of a continuous glucose trace and asks you to draw the next hour. The score is ordinary forecast error (MAE, RMSE in mg/dL), collected under ethics clearance A 2026-0064, because no published human baseline exists for that task.

**Paragraph version**
> Sugar-Sugar is an online study run by GlucoseDAO with University Medical Center Rostock. You see three hours of CGM context and draw what you think happens in the next sixty minutes - twelve points, one every five minutes - for six to twelve rounds. People with diabetes and people without it can play; you can upload Dexcom, Libre or Medtronic data or use public anonymized traces from BIG IDEAs and D1NAMO. Nothing leaves the browser until you consent. The point is not a new dosing app. The point is a human accuracy number that glucose-forecasting models can be compared against.

**Bio line** - for when a community requires an intro post
> Aging / biostatistics researcher at University Medical Center Rostock. We built a small game that measures how well people predict the next hour of a CGM trace, because the ML papers had no human baseline. sugar-sugar.study

---

## Per-platform openings

| Platform | Opening that works | Why |
|---|---|---|
| LinkedIn | "I could not find a published number for how well a person predicts the next hour of a CGM trace, so we asked people to draw it." | Method-first, no announcement register |
| Bluesky | "Three hours of glucose. Draw the next one." | Mechanic in under ten words |
| Reddit self-post | "Task: 3 hours of CGM context, predict the next 60 minutes by drawing 12 points, repeat 6-12 times. We need a human baseline for glucose models." | Protocol on line one |
| Telegram (warm room) | Member-with-news: we opened the glucose-prediction study and you can play it in the browser | Not a marketer |
| Diabetes / CGM room | Ask first, then: we are recruiting for an ethics-cleared observational study, not selling an app | Rooms often treat unsolicited studies as spam |
| Hacker News | (write by hand - no LLM text) | HN rule: no LLM, not even for editing |

---

## Phrases to avoid

Beyond the hard `forbidden_words` list in `PROJECT.md`, these are stylistic tells worth avoiding:

- "excited to announce", "thrilled to share", "game-changing", "revolutionary"
- "it's not just X, it's Y" - a very recognisable LLM construction
- Rhetorical question openers ("Ever wondered what would happen if...")
- Hedging stacks: "it could potentially perhaps"
- Em dashes (use plain hyphens)
- "Leveraging", "harnessing", "unlocking"
- "At the intersection of" (use "where X meets Y" or just describe what it is)
- "superpowers" outside the site's own tagline - it reads as ad-copy in science rooms
- Invented leaderboard drama. The highscore board hides runs below 6 rounds; do not narrate ranks you did not earn

---

## Copy that already worked

(This section fills in as posts are sent and measured.)

### On-site tagline (do not rewrite in posts unless you are quoting the site)

> A game to test your glucose-predicting superpowers.

That line lives on the landing page. It is fine to quote. It is a weak first line for a methods or diabetes-org post.

### Landing "about the study" (canonical, already shipped)

> Can people predict where glucose will go next? Sugar-Sugar turns that question into a game. For people with diabetes, that next hour can decide food, insulin, and staying safe. You don't need diabetes to play. Everyone leaves a human score researchers need.
>
> This is a real study, cleared by the Ethics Committee of University Medical Center Rostock (Germany) - so please read the consent form and tick the required boxes.
