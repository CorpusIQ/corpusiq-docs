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
import os
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

# Keys that must carry a bare ISO date. They are copied verbatim into the
# page's JSON-LD (datePublished / dateModified), so a stray quote or a prose
# date does not fail YAML - it produces invalid structured data that search
# engines drop silently. See the 2026-11-05 case in check_file below.
DATE_KEYS = {"last_updated", "last_modified", "date_modified", "added"}
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# A YAML plain scalar can never *begin* with these.
SCALAR_STARTS = ("\"", "'", "[", "{", ">", "|", "&", "*", "!", "#", "?")

FM_RE = re.compile(r"^---\n(.*?)\n---(\n|$)", re.DOTALL)
LINE_RE = re.compile(r"^([A-Za-z_][\w-]*): (.+?)\s*$")
KEY_RE = re.compile(r"^([A-Za-z_][\w-]*):")

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
    # 3. Duplicate top-level keys. PyYAML accepts them silently and keeps the
    #    last value, so a second `last_updated:` overwrites the first with no
    #    error and the page ships two contradicting claims about its freshness.
    #    Every other gate reads keys by name and never notices.
    seen_keys: dict[str, int] = {}
    for idx, raw_line in enumerate(block.split("\n"), start=1):
        km = KEY_RE.match(raw_line)
        if not km:
            continue
        key = km.group(1)
        if key in seen_keys:
            problems.append(
                f"duplicate frontmatter key `{key}` "
                f"(first on line {seen_keys[key]}, again on line {idx}) — "
                f"YAML keeps only the last value"
            )
        else:
            seen_keys[key] = idx

    # 4. Date hygiene for keys that reach JSON-LD as dates: ISO only.
    # 5. Quote integrity. PyYAML happily accepts `last_updated: 2026-11-04"` as
    #    the STRING '2026-11-04"' - a plain scalar absorbs a stray closing
    #    quote and nothing complains. That string is then copied verbatim into
    #    the rendered page graph, shipping `"datePublished": "2026-11-04""` on
    #    two live pages (hermes/mcp-ecosystem, hermes/mcp/connectors) and
    #    silently dropping their structured data. So: a plain scalar must never
    #    contain a double quote, and a quoted value must open and close with the
    #    same character and escape any inner double quotes.
    values = yaml.safe_load(block)
    if isinstance(values, dict):
        for key, val in values.items():
            if isinstance(val, str) and key in DATE_KEYS and not ISO_DATE_RE.match(val.strip()):
                problems.append(
                    f"`{key}` must be a bare ISO date (YYYY-MM-DD), got {val!r} — "
                    f"it is copied verbatim into the page JSON-LD"
                )
    for raw_line in block.split("\n"):
        lm = LINE_RE.match(raw_line)
        if not lm:
            continue
        key, raw_value = lm.group(1), lm.group(2)
        if raw_value[:1] in ("\"", "'"):
            quote = raw_value[0]
            if len(raw_value) < 2 or not raw_value.endswith(quote):
                problems.append(
                    f"`{key}` opens with {quote} but never closes with it — the "
                    f"quote ships into the page (meta/JSON-LD)"
                )
            elif quote == "\"" and raw_value[1:-1].replace("\\\"", "").count("\"") % 2:
                problems.append(
                    f"`{key}` has an odd number of unescaped double quotes "
                    f"inside a double-quoted value — escape them as \\\""
                )
            continue
        if raw_value[:1] in SCALAR_STARTS:
            continue
        if '"' in raw_value:
            problems.append(
                f"`{key}` is an unquoted value containing a double quote — "
                f"almost always a dropped opening quote. Wrap it in one pair: "
                f"`{key}: \"...\"`"
            )
    return problems


def brand_title_gate() -> int:
    """Fail when a page title repeats the site brand suffix.

    The theme renders the frontmatter title verbatim, so "Supabase - CorpusIQ
    Docs - CorpusIQ Docs" reaches the SERP twice brand-suffixed. 121 pages
    shipped with the defect; the worst (a catalog page) held 7,483 impressions
    at position 6.5 with 3 clicks over 90 days.

    This lives inside the frontmatter gate because CI already runs this script
    on every push and pull request, and the repository's classic PAT cannot push
    a separate step into .github/workflows/. Repair with
    `python scripts/validate_page_metadata.py --fix`.
    """
    try:
        import validate_page_metadata as vpm
    except ImportError:  # invoked from another working directory
        sys.path.insert(0, __file__.rsplit("/", 1)[0])
        import validate_page_metadata as vpm  # type: ignore

    bad = []
    for path in vpm.pages("."):
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        fm = vpm.frontmatter(text)
        if not fm:
            continue
        title = vpm.value(fm, "title")
        if title and vpm.brand_dupe(title):
            bad.append((os.path.relpath(path, "."), title))

    if not bad:
        return 0
    print(f"✗ {len(bad)} page title(s) repeat the brand suffix:", file=sys.stderr)
    for rel, title in sorted(bad)[:20]:
        print(f"  {rel}: {title}", file=sys.stderr)
    print("  Fix: python scripts/validate_page_metadata.py --fix", file=sys.stderr)
    return 1


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
        return brand_title_gate()

    print(f"✗ {len(broken)} file(s) with broken frontmatter:\n", file=sys.stderr)
    for f, issues in sorted(broken.items()):
        for issue in issues:
            print(f"  {f}\n      {issue}", file=sys.stderr)
    flat = [issue for issues in broken.values() for issue in issues]
    hints: list[str] = []
    if any("duplicate frontmatter key" in i for i in flat):
        hints.append(
            "delete the duplicate key and keep ONE truthful value. YAML would "
            "silently keep only the last one, so the page ends up making two "
            "contradicting claims about itself (the 2026-11-03 case: "
            "`last_updated: June 22, 2026` followed by `last_updated: \"2026-11-01\"`)."
        )
    if any("silently truncated" in i for i in flat):
        hints.append(
            "wrap any title/description/name value containing ': ' or ' #' "
            "in double quotes."
        )
    if any("double quote" in i or "never closes" in i for i in flat):
        hints.append(
            "one matching pair of quotes per value: a plain scalar must not "
            "contain a '\"', and a value that opens with a quote must close "
            "with the same one (escape inner double quotes as \\\")."
        )
    if any("bare ISO date" in i for i in flat):
        hints.append(
            "`last_updated` and `added` must be YYYY-MM-DD - they are copied "
            "verbatim into the page JSON-LD."
        )
    if any(i.startswith("invalid YAML") or i.startswith("frontmatter opener") for i in flat):
        hints.append(
            "fix the YAML itself: quote a value that contains ': ', and make sure "
            "the block opens and closes with '---'."
        )
    if not hints:
        hints.append("see the messages above.")
    print("\nFix:", file=sys.stderr)
    for hint in hints:
        print(f"  - {hint}", file=sys.stderr)
    print("Run `python scripts/validate_frontmatter.py` locally to re-check.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
