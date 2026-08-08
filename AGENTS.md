# Agent instructions

This repo is a promotion and distribution system for one project. Read `README.md` for the shape, `PROMPTS.md` for the numbered tasks, `project/schema.md` for every column's meaning.

## Paths

Resolve everything relative to this repo's root — the folder containing this file. Never write an absolute path, a username, or a home directory into any file, script, or scheduled task. Scripts here locate the repo with `Path(__file__).resolve().parent.parent`; do the same. A hardcoded path is a bug: it works for exactly one person and breaks silently for everyone else.

The same applies to external identifiers. Discover Google Drive folders by title search and create one if none matches; never record the resulting id in a prompt or a committed file.

## Read these two before writing a single word

1. `project/PROJECT.md` — the standing facts, voice rules, forbidden words, and who writes as whom. If it still contains template placeholders, stop and say so rather than inventing a voice.
2. `registry/platform_rules.csv` for the platform, and the specific row in `registry/destinations.csv` for the room. The `self_promo_rule` column holds that community's actual written rule.

## Never invent facts

Use only the figures in `project/PROJECT.md`. Never invent numbers, URLs, contact addresses, or citations. If the standing facts contradict what a live site says, report the contradiction instead of silently picking one.

## The approval gate is human-only

A post candidate is a Markdown file that moves through three folders:

```
candidates/pending/    you drafted it; nobody has reviewed it
candidates/approved/   a human moved it here - this move IS the approval
candidates/sent/       it went out and was logged in registry/shares.csv
```

You may write freely into `pending/`. **You may never move a file into `approved/`.** Only a human does that. You may act on a file already sitting in `approved/` (send it), and afterward you move it to `sent/`, fill in `platform_msg_id` and `permalink` in its frontmatter, and append a row to `registry/shares.csv`.

Nothing enters `shares.csv` until it has actually been sent. That table answers "what went out and how did it do" — a draft row in it is indistinguishable from a real one at a glance.

## Boost asks

`boost_ok` in `destinations.csv` says whether asking contacts to like or comment is safe:

- `yes` — normal in Facebook, Telegram, WhatsApp, Discord group contexts.
- `risky` — LinkedIn removes groups that show engagement-pod behaviour. Ask individuals, never reciprocally.
- `no-bannable` — Reddit, Hacker News, Product Hunt. Never record a boost ask against these. HN's rule penalises **sites** as well as accounts, so one incident can flag the project's domain.

## Varying text

One blurb per room, each genuinely different: different opening line, different fact led with, different sign-off. Never reuse a sentence across two rooms, even in different languages. Identical text across many chats is precisely the pattern that gets a personal Telegram account flagged. When suggesting send times, spread them across a day, hours apart.

## Automation honesty

`platform_rules.csv` has an `automation` column. Respect it. WhatsApp is draft-only because it runs on a personal number. Hacker News is never automated and its text must be written by hand — no LLM, not even for editing. Third-party Discords are manual because bot-token integrations require adding a bot you cannot add.

## After changing the registry

Run `python scripts/check_registry.py`. It catches duplicate ids, broken references, UTM values that will split into separate analytics rows, and boost asks recorded against rooms where asking is bannable. Fix what it names before finishing.
