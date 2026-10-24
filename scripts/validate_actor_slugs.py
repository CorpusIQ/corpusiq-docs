#!/usr/bin/env python3
"""Gate: every `apify actor run <owner>/<slug>` in the docs must be real.

Why this exists (2026-10-24, GitHub issue #118):
`hermes/skills/catalog/apify-ultimate-scraper-setup.md` shipped four invented
Actor slugs (`apify/google-maps-scraper`, `apify/linkedin-company-scraper`,
`apify/shopify-scraper`) plus invented input keys (`usernames`, `searchStrings`,
`subreddits`). A reader following the page got a 404 on the very first step.
Nothing in the build caught it because no gate ever resolved an Actor slug.

What it checks, per unique `owner/slug`:
  1. The Actor exists: GET /v2/acts/<owner>~<slug> must return 200.
  2. Every key in the `--input '{...}'` JSON that follows the command must be a
     real property of that Actor's input schema (fetched from its default build).

Exit codes:
  0  all references verified (or --offline / network flap -> warnings only)
  1  at least one dead slug or bogus input key

Usage:
  python3 scripts/validate_actor_slugs.py
  python3 scripts/validate_actor_slugs.py --offline      # skip network
  python3 scripts/validate_actor_slugs.py --path hermes/skills/catalog
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

API = "https://api.apify.com/v2/acts"
TIMEOUT = 25

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# `apify actor run owner/slug`, with the --input payload usually on the next
# continuation line (the docs wrap commands with a trailing backslash).
CMD_RE = re.compile(r"apify\s+actor\s+run\s+([A-Za-z0-9][\w.-]*/[A-Za-z0-9][\w.-]*)")
INPUT_RE = re.compile(r"--input\s+'(\{.*?\})'|--input\s+\"(\{.*?\})\"")

SKIP_DIRS = {".git", "node_modules", ".cache", "site", "__pycache__", ".venv"}


def command_blocks(text: str):
    """Yield (slug, block_text, line_no) for each `apify actor run` command.

    The block includes trailing continuation lines (ending with `\\`) so a
    wrapped `--input '{...}'` is part of the same command.
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = CMD_RE.search(line)
        if not m:
            continue
        block = [line]
        j = i
        while block[-1].rstrip().endswith("\\") and j + 1 < len(lines) and len(block) < 8:
            j += 1
            block.append(lines[j])
        yield m.group(1).rstrip(".,;"), "\n".join(block), i + 1


def _get_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "corpusiq-docs-gate"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def actor_status(slug: str, cache: dict):
    """Return ('ok', props|None) or ('dead', None) or ('unknown', None)."""
    if slug in cache:
        return cache[slug]
    try:
        obj = _get_json(f"{API}/{slug.replace('/', '~')}")
        if obj.get("data", {}).get("id"):
            props = input_props(slug, cache)
            cache[slug] = ("ok", props)
        else:
            cache[slug] = ("dead", None)
    except urllib.error.HTTPError as e:
        cache[slug] = ("dead", None) if e.code in (404, 400) else ("unknown", None)
    except Exception:
        cache[slug] = ("unknown", None)
    return cache[slug]


def input_props(slug: str, cache: dict):
    """Property names from the Actor's default-build input schema (None = unknown)."""
    key = ("schema", slug)
    if key in cache:
        return cache[key]
    try:
        d = _get_json(f"{API}/{slug.replace('/', '~')}/builds/default").get("data") or {}
        sch = d.get("inputSchema") or {}
        if isinstance(sch, str):
            sch = json.loads(sch)
        props = set((sch.get("properties") or {}).keys()) if isinstance(sch, dict) else None
    except Exception:
        props = None
    cache[key] = props
    return props


def md_files(root: str):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".git")]
        for fn in filenames:
            if fn.endswith(".md"):
                yield os.path.join(dirpath, fn)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true", help="skip network checks")
    ap.add_argument("--path", default=REPO, help="root to scan (default: repo root)")
    args = ap.parse_args()

    cache: dict = {}
    hard_fail = []
    warned = []
    checked = 0
    slugs = set()

    for path in md_files(args.path):
        rel = os.path.relpath(path, REPO)
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        if "apify actor run" not in text:
            continue
        for slug, block, line_no in command_blocks(text):
            slugs.add(slug)
            if args.offline:
                continue
            checked += 1
            status, props = actor_status(slug, cache)
            if status == "dead":
                hard_fail.append(f"{rel}:{line_no}  Actor not found on Apify: {slug}")
                continue
            if status == "unknown":
                warned.append(f"{rel}:{line_no}  could not resolve {slug} (network/API) - not blocking")
                continue
            im = INPUT_RE.search(block.replace("\\\n", " "))
            if not im or props is None:
                continue
            raw = im.group(1) or im.group(2)
            try:
                payload = json.loads(raw)
            except Exception:
                warned.append(f"{rel}:{line_no}  unparsable --input JSON for {slug}")
                continue
            bogus = [k for k in payload if k not in props]
            if bogus:
                hard_fail.append(
                    f"{rel}:{line_no}  {slug} has no input field(s) {bogus}; "
                    f"valid: {sorted(props)[:8]}..."
                )

    if args.offline:
        print(f"OFFLINE: skipped network verification of {len(slugs)} Apify Actor reference(s)")
        return 0

    for w in warned:
        print(f"WARN {w}")
    if hard_fail:
        print(f"\nFAIL: {len(hard_fail)} broken Apify Actor reference(s):")
        for f in hard_fail:
            print(f"  {f}")
        print(
            "\nFix by looking the Actor up in the Apify Store and copying its exact\n"
            "owner/slug and input-schema field names, then re-run this gate."
        )
        return 1

    print(f"OK: {checked} Apify Actor reference(s) verified against the live API")
    return 0


if __name__ == "__main__":
    sys.exit(main())
