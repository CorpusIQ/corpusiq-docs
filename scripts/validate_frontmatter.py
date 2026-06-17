#!/usr/bin/env python3
"""Validate YAML frontmatter across all Markdown pages in the docs site.

Why this exists
---------------
MkDocs builds in non-strict mode (see .github/workflows/pages.yml), so a page
with malformed YAML frontmatter does NOT fail the build — it silently drops the
frontmatter. The symptoms are invisible in CI but ugly in production:

  1. GitHub renders a pink "frontmatter parse" banner above the page.
  2. The page loses its <meta name="description"> (an SEO regression).
  3. Titles containing ' #' get silently truncated at the '#' (read as a
     YAML comment).

The usual source is a bulk-injection sweep (SEO pass, marketplace sweep) that
writes UNQUOTED string values. The classic break is a value containing ': '
(colon-space), which YAML reads as a nested mapping key:

    description: ...autonomous operations: 6-layer architecture...
                                          ^^ "mapping values are not allowed here"

This script catches both failure modes and exits non-zero so the CI gate can
block the merge / deploy. It is intentionally dependency-light: it uses PyYAML,
which is already pulled in transitively by mkdocs-material.

Checks per file (only files that actually start with a '---' frontmatter block):
  * the block has a closing '---'
  * the block is valid YAML (catches the colon-space hard error)
  * known string-scalar keys (title/description/name/...) did not silently lose
    characters to a '#' comment (catches the truncation case)

Exit codes: 0 = all good, 1 = one or more pages broken.
"""
from __future__ import annotations

import glob
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML not installed. `pip install pyyaml` "
          "(it ships transitively with mkdocs-material).", file=sys.stderr)
    sys.exit(2)

# Keys whose value must round-trip as a plain string. If YAML coerces or
# truncates one of these, that's data loss we want to flag.
STRING_KEYS = {
    "title", "description", "name", "category", "source", "setup", "summary",
}

FM_RE = re.compile(r"^---\n(.*?)\n---(\n|$)", re.DOTALL)
LINE_RE = re.compile(r"^([A-Za-z_][\w-]*): (.+?)\s*$")

# Folders to scan. Everything published lives under these; vendored/build dirs
# and the site output are excluded.
EXCLUDE_PREFIXES = ("site/", ".git/", "node_modules/", ".venv/")


def iter_markdown() -> list[str]:
    files = set(glob.glob("**/*.md", recursive=True))
    return sorted(
        f for f in files
        if not f.startswith(EXCLUDE_PREFIXES)
    )


def check_file(path: str) -> list[str]:
    """Return a list of human-readable problems for one file (empty == clean)."""
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        return []  # no frontmatter block — nothing to validate

    m = FM_RE.match(text)
    if not m:
        return [f"frontmatter opener '---' has no matching closing '---'"]

    block = m.group(1)

    # 1. Hard YAML validity (the colon-space case lands here).
    try:
        yaml.safe_load(block)
    except yaml.YAMLError as e:
        first = str(e).split("\n")[0]
        mark = getattr(e, "problem_mark", None)
        where = f" (frontmatter line {mark.line + 1})" if mark else ""
        return [f"invalid YAML frontmatter{where}: {first}"]

    # 2. Silent truncation: a known string key whose raw value got cut by '#'.
    problems = []
    for raw_line in block.split("\n"):
        lm = LINE_RE.match(raw_line)
        if not lm:
            continue
        key, raw_value = lm.group(1), lm.group(2)
        if key not in STRING_KEYS:
            continue
        if raw_value[:1] in ("\"", "'", "[", "{", ">", "|", "&", "*", "!"):
            continue  # already quoted / a flow collection / a tag — fine
        parsed = yaml.safe_load(f"{key}: {raw_value}").get(key)
        if isinstance(parsed, str) and parsed != raw_value:
            problems.append(
                f"`{key}` is silently truncated to {parsed!r} "
                f"(the rest is read as a YAML comment) — wrap the value in quotes"
            )
    return problems


def main() -> int:
    files = iter_markdown()
    broken: dict[str, list[str]] = {}
    for f in files:
        issues = check_file(f)
        if issues:
            broken[f] = issues

    print(f"frontmatter check: scanned {len(files)} Markdown files")
    if not broken:
        print("✓ all frontmatter is valid")
        return 0

    print(f"✗ {len(broken)} file(s) with broken frontmatter:\n", file=sys.stderr)
    for f, issues in sorted(broken.items()):
        for issue in issues:
            print(f"  {f}\n      {issue}", file=sys.stderr)
    print(
        "\nFix: wrap any title/description/name value containing ': ' or ' #' "
        "in double quotes.\n"
        "Run `python scripts/validate_frontmatter.py` locally to re-check.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
