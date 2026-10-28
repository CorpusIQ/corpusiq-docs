"""Abort the docs build when the ecosystem directory lists the same entry twice.

Why this exists
---------------
The directory is assembled by several sweeps. Each sweep appends the repos it
found and none of them checked whether the repo was already listed. On
2026-10-28 six repos appeared twice -- three inside one category, three in two
categories -- so the page showed the same project twice and the visible count no
longer matched the census. That mismatch is what pushed a hand-bump of the Quick
Navigation numbers to 33/63/5 against a 31/62/4 census: two answers to one
question on the same page.

Why a build hook instead of a workflow step
-------------------------------------------
A workflow step only runs in CI, and the push credential for this repository has
no `workflow` scope, so a workflow-file change cannot be pushed from the agent
account at all. An MkDocs hook gets the same enforcement where it matters: the
Vercel deploy workflow runs `mkdocs build`, so a duplicate now fails the build
that produces the deployed site, plus every local build.

Behaviour
---------
on_config runs the gate once per build. Clean tree: returns the config and the
build continues. Any duplicate: raises SystemExit naming each entry, so the build
stops before deploying. Fix with scripts/dedupe_ecosystem_entries.py (first
occurrence wins).
"""

import importlib.util
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(REPO, "scripts", "dedupe_ecosystem_entries.py")
INDEX = os.path.join(REPO, "hermes", "ecosystem", "index.md")


def _load():
    spec = importlib.util.spec_from_file_location("dedupe_ecosystem_entries", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["dedupe_ecosystem_entries"] = mod
    spec.loader.exec_module(mod)
    return mod


def on_config(config):
    if not os.path.exists(INDEX):
        return config
    mod = _load()
    text = open(INDEX, encoding="utf-8").read()
    lines = text.split("\n")
    seen = {}
    dupes = []
    for name, start, _end, _limit in mod.blocks(lines):
        if name in seen:
            dupes.append((name, seen[name] + 1, start + 1))
        else:
            seen[name] = start
    if dupes:
        msg = ["ecosystem directory lists the same entry more than once:"]
        for name, first, later in dupes:
            msg.append(f"  - {name}: line {first} and line {later}")
        msg.append("fix: python3 scripts/dedupe_ecosystem_entries.py (first occurrence wins)")
        raise SystemExit("\n".join(msg))
    return config
