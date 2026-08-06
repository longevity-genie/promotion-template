# promotion-template

A reusable template for promoting a project across many communities without spamming, and for tracking what actually worked.

Clone it, fill in `project/PROJECT.md`, and you have a working distribution system: a registry of communities with their rules attached, a draft-review-send queue with a real human approval gate, and share-level tracking that answers "which rooms are worth posting in" after a few weeks.

Built for [enhancement.bio](https://enhancement.bio), generalised so the next project starts from something instead of nothing.

## The idea in one paragraph

Promoting a niche project fails in two predictable ways: you blast identical text into twenty rooms and get banned or ignored, or you post carefully but never record anything and so never learn which rooms mattered. This template addresses both. Communities live in a registry with their actual written rules attached, so an agent drafting a post knows that r/generative bans "AI art" and that Hacker News penalises soliciting upvotes. Every post is drafted as a file that a human must physically move into `approved/` before anything sends. Every send carries a UTM tag holding its own share id, which is what makes one click traceable to one post in one room.

## How to use it for a project

```bash
git clone https://github.com/longevity-genie/promotion-template my-project-promo
cd my-project-promo
git remote rename origin upstream          # keep upstream, to pull registry updates later
git remote add origin <your-own-repo-url>  # your project's own promo repo
```

Then, in order:

1. **Fill in `project/PROJECT.md`.** Standing facts, voice rules, forbidden words, who writes as whom. Nothing else works until this is real — it's what every prompt reads before drafting a word.
2. **Write `project/copy-pack.md`.** Your voice model, and any copy you already have.
3. **Prune and extend `registry/destinations.csv`.** It ships with public, discoverable communities that suit open-source science, generative art, and research tooling. Delete what doesn't fit. Add your own warm rooms — the Telegram and WhatsApp groups you're personally in — marking them `scope=local`.
4. **Run a prompt.** Open `PROMPTS.md`, paste prompt `00` into Claude Cowork or Codex to get oriented, then `10` to draft your first pillar.

Run `python scripts/check_registry.py` at any point; it validates ids, catches duplicates, and flags rule violations.

## Layout

```
├── project/            <- the only folder you must fill in by hand
│   ├── PROJECT.md          standing facts, voice rules, forbidden words
│   └── copy-pack.md        voice model and drafted copy
├── registry/           <- the data, as CSV so git can diff it
│   ├── destinations.csv    communities, with their real rules and caps
│   ├── platform_rules.csv  per-platform constraints and gotchas
│   ├── pillars.csv         long-form canonical assets
│   ├── derivatives.csv     platform-native posts made from a pillar
│   ├── shares.csv          one row per post ACTUALLY sent, with outcome
│   └── utm_convention.md   the tagging scheme - follow it or the data is noise
├── candidates/         <- the approval gate
│   ├── pending/            an agent drafted this; nobody has reviewed it
│   ├── approved/           a human moved it here; cleared to send
│   └── sent/               it went out; permanent record
├── scripts/
│   ├── build_workbook.py   CSVs -> one .xlsx, if you prefer a spreadsheet view
│   └── check_registry.py   validates ids, duplicates, and rule violations
├── docs/
│   ├── schema.md           every column in every file, explained
│   └── workflow.md         the weekly loop, start to finish
├── AGENTS.md           <- read automatically by Codex, Cursor, Claude Code
└── PROMPTS.md          <- numbered copy-paste prompts, 00 through 90
```

## The content model

Three tiers, because writing twenty original posts a week isn't sustainable and posting the same text twenty times gets you banned.

**Pillar** — one high-effort canonical asset with a URL. A long-form article, a Show HN, a preprint. Maybe one or two a month.

**Derivative** — three to five platform-native posts made from that pillar. A LinkedIn post, a Bluesky post, a Facebook post. Each stands alone; someone who never clicks through to the pillar still gets the point.

**Candidate** — one short blurb per community, written for that specific room in its own language and register. These are files in `candidates/`, never reused between rooms, and they're what actually gets sent.

## Why CSV and not a spreadsheet

The registry is the valuable part, and it has to survive being edited by two people and several agents. CSV diffs in a pull request; a binary `.xlsx` doesn't, so two people editing it produces a conflict you can only resolve by picking one copy and discarding the other. If you want the spreadsheet view, `python scripts/build_workbook.py` generates it from the CSVs, and `.gitignore` keeps the generated file out of git.

## Keeping the registry fresh across projects

Community rules change, and rooms that ban self-promotion are worth knowing about permanently. Rows marked `scope=template` are generic and maintained upstream, so:

```bash
git fetch upstream && git merge upstream/main
```

pulls in newly vetted rooms and rule corrections without touching your own. Rows you add for your own project should be marked `scope=local` — they stay yours and won't conflict on merge. If you vet a public room that would help anyone, send it upstream as a PR.

## What this template deliberately does not do

It does not auto-post. Every prompt that touches a platform is draft-only, and the `pending/` to `approved/` move is human-only by design. That isn't timidity. Telegram and WhatsApp automation runs on your personal account, and a ban costs real relationships rather than just a project. Hacker News penalises sites as well as accounts, so one solicited upvote could get your actual domain flagged. The system is built so an agent does the tedious 90% and stops where judgement starts.

## License

MIT — see `LICENSE`.
