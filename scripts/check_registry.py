#!/usr/bin/env python3
"""Validate the registry. Run this before trusting anything the numbers tell you.

Catches the failure modes that silently corrupt the data: duplicate or missing ids,
UTM values that break analytics, shares pointing at destinations that don't exist,
and boost asks recorded against rooms where asking is a bannable offence.

Usage:  python scripts/check_registry.py
Exit code 0 = clean, 1 = problems found. No dependencies beyond the stdlib.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

# Resolve paths relative to this file, never from the working directory or a
# hardcoded absolute path - the repo has to work on anyone's machine.
REPO = Path(__file__).resolve().parent.parent
REGISTRY = REPO / "registry"
CANDIDATES = REPO / "candidates"

SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

problems: list[str] = []
notes: list[str] = []


def load(name: str) -> list[dict[str, str]]:
    path = REGISTRY / name
    if not path.exists():
        problems.append(f"{name}: missing from registry/")
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return [row for row in csv.DictReader(f) if any(v.strip() for v in row.values())]


def main() -> int:
    dests = load("destinations.csv")
    plats = load("platform_rules.csv")
    pillars = load("pillars.csv")
    derivs = load("derivatives.csv")
    shares = load("shares.csv")

    dest_ids = [d["dest_id"] for d in dests]
    known_platforms = {p["platform"] for p in plats}
    pillar_ids = {p["pillar_id"] for p in pillars}
    deriv_ids = {d["deriv_id"] for d in derivs}

    # --- destinations ---
    for dup in {i for i in dest_ids if dest_ids.count(i) > 1}:
        problems.append(f"destinations: dest_id '{dup}' appears more than once")

    utm_sources = [d["utm_source"] for d in dests if d["utm_source"]]
    for dup in {u for u in utm_sources if utm_sources.count(u) > 1}:
        problems.append(
            f"destinations: utm_source '{dup}' is reused across rooms - "
            "clicks from both will merge into one indistinguishable row"
        )

    for d in dests:
        did = d["dest_id"] or "<blank>"
        if not SLUG.match(d["dest_id"] or ""):
            problems.append(f"destinations: dest_id '{did}' is not a lowercase-hyphen slug")
        if d["utm_source"] and not SLUG.match(d["utm_source"]):
            problems.append(
                f"destinations: {did} utm_source '{d['utm_source']}' is not lowercase-hyphen. "
                "UTM values are case-sensitive, so this will split into separate analytics rows"
            )
        if d["platform"] not in known_platforms:
            problems.append(
                f"destinations: {did} platform '{d['platform']}' has no row in platform_rules.csv"
            )
        if d["boost_ok"] not in {"yes", "risky", "no-bannable"}:
            problems.append(f"destinations: {did} boost_ok must be yes/risky/no-bannable")
        if d["scope"] not in {"template", "local"}:
            problems.append(
                f"destinations: {did} scope must be 'template' (maintained upstream) "
                "or 'local' (yours - won't conflict on merge)"
            )
        if d["measurable"] not in {"yes", "no"}:
            problems.append(f"destinations: {did} measurable must be yes/no")
        if not d["self_promo_rule"].strip():
            notes.append(
                f"destinations: {did} has no self_promo_rule recorded - "
                "read the room's rules before posting there"
            )

    # --- shares: the table that has to stay trustworthy ---
    share_ids = [s["share_id"] for s in shares]
    for dup in {i for i in share_ids if share_ids.count(i) > 1}:
        problems.append(f"shares: share_id '{dup}' appears more than once")

    boost_lookup = {d["dest_id"]: d["boost_ok"] for d in dests}
    for s in shares:
        sid = s["share_id"] or "<blank>"
        if s["dest_id"] not in boost_lookup:
            problems.append(f"shares: {sid} references unknown dest_id '{s['dest_id']}'")
        if s["pillar_id"] and s["pillar_id"] not in pillar_ids:
            problems.append(f"shares: {sid} references unknown pillar_id '{s['pillar_id']}'")
        if s["deriv_id"] and s["deriv_id"] not in deriv_ids:
            problems.append(f"shares: {sid} references unknown deriv_id '{s['deriv_id']}'")
        if s["utm_content"] and s["utm_content"] != s["share_id"]:
            problems.append(
                f"shares: {sid} utm_content is '{s['utm_content']}' but must equal share_id - "
                "that equality is what makes a click traceable to one room"
            )
        if s["date_sent"] and not DATE.match(s["date_sent"]):
            problems.append(f"shares: {sid} date_sent '{s['date_sent']}' is not YYYY-MM-DD")
        if s["boost_asked_who"].strip() and boost_lookup.get(s["dest_id"]) == "no-bannable":
            problems.append(
                f"shares: {sid} records a boost ask for {s['dest_id']}, where soliciting "
                "engagement is bannable. On Hacker News this penalises your SITE too"
            )
        if s["dest_id"] in boost_lookup:
            dest = next(d for d in dests if d["dest_id"] == s["dest_id"])
            if dest["measurable"] == "yes" and not s["platform_msg_id"].strip():
                notes.append(
                    f"shares: {sid} is in a measurable room but has no platform_msg_id - "
                    "metrics there can no longer be pulled automatically"
                )

    # --- candidates ---
    for stage in ("pending", "approved", "sent"):
        if not (CANDIDATES / stage).is_dir():
            problems.append(f"candidates/{stage}/ is missing")
    pending = len(list((CANDIDATES / "pending").glob("*.md"))) if (CANDIDATES / "pending").is_dir() else 0
    approved = len(list((CANDIDATES / "approved").glob("*.md"))) if (CANDIDATES / "approved").is_dir() else 0

    # --- report ---
    print(
        f"registry: {len(dests)} destinations, {len(pillars)} pillars, "
        f"{len(derivs)} derivatives, {len(shares)} shares sent"
    )
    print(f"candidates: {pending} pending review, {approved} approved and awaiting send")

    if notes:
        print(f"\n{len(notes)} note(s) - worth a look, not errors:")
        for n in notes:
            print(f"  - {n}")

    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  ! {p}")
        return 1

    print("\nNo problems found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
