#!/usr/bin/env python3
"""check_setext_rules.py - stop credit lines from rendering as section headings.

The defect
----------
Markdown turns a paragraph line that is immediately followed by `---` into a
setext H2, because `---` is a valid heading underline. Writers use `---` to mean
"horizontal rule", which needs a blank line above it. When the blank line is
missing, the previous sentence is swallowed as a heading.

Measured 2026-11-07 on production: /docs/hermes/prompts renders the page's credit
line as

    <h2 id="from-the-hermes-prompt-collection-...">From the Hermes Prompt
    Collection - production prompts for AI agents. Powered by CorpusIQ.</h2>

and the same shape appears on the skills catalog entries (`Powered by CorpusIQ`,
`Part of the Hermes Skills Library - ...`). The damage is not cosmetic:

* a junk section appears in the page table of contents, so the outline a reader
  or an AI assistant extracts from the page is wrong;
* the sentence is promoted to a heading, which changes how answer engines weigh
  it - the credit becomes a section title instead of a footer line;
* GitHub renders the raw markdown the same way, so the defect is visible in the
  repository too.

Rules
-----
* Only a line that is exactly `---` is inspected (that is the rule intent).
* The line above must be non-blank prose. A blank line above means the `---`
  really is a thematic break, so nothing is reported.
* Fenced code blocks are skipped: their content is literal.
* The closing delimiter of a YAML frontmatter block is skipped.
* Table rows are skipped: `---` under a pipe row is not a setext underline.

Usage
-----
    python3 scripts/check_setext_rules.py            # report, exit 1 on offenders
    python3 scripts/check_setext_rules.py --fix      # insert the missing blank line
    python3 scripts/check_setext_rules.py --paths hermes/prompts
"""

from __future__ import annotations

import argparse
import os
import re
import sys

SKIP_DIRS = {".git", "node_modules", "site", "dist", ".venv", "__pycache__"}


def _iter_markdown(paths: list[str]):
    for root in paths:
        if os.path.isfile(root):
            if root.endswith(".md"):
                yield root
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for name in sorted(filenames):
                if name.endswith(".md"):
                    yield os.path.join(dirpath, name)


def _frontmatter_close(lines: list[str]) -> int:
    """Index of the closing `---` of a leading frontmatter block, or -1."""
    if not lines or lines[0].strip() != "---":
        return -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return i
        if lines[i].strip() == "" and i > 40:
            return -1
    return -1


def offenders(path: str) -> list[int]:
    """1-based line numbers of `---` rules that lack a blank line above them."""
    with open(path, encoding="utf-8", errors="replace") as fh:
        lines = fh.read().split("\n")

    fm_close = _frontmatter_close(lines)
    in_fence = [False] * len(lines)
    fence_delim: set[int] = set()
    fence = ""
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        marker = stripped[:3]
        if marker in ("```", "~~~"):
            fence_delim.add(i)
            if fence == "":
                fence = marker
                in_fence[i] = True
                continue
            if marker == fence:
                fence = ""
            in_fence[i] = True
            continue
        in_fence[i] = fence != ""

    found: list[int] = []
    for i in range(1, len(lines)):
        if lines[i].rstrip() != "---":
            continue
        if in_fence[i] or i == fm_close:
            continue
        # A rule right under a closing fence is a plain thematic break: the fence
        # already ended the previous block.
        if (i - 1) in fence_delim:
            continue
        prev = lines[i - 1]
        if not prev.strip():
            continue
        if prev.strip() == "---":
            continue
        if prev.strip().startswith("|"):
            continue
        # An ATX heading already closed its own block, so a following `---` is a
        # plain thematic break. Reporting those would churn hundreds of files for
        # no visible change.
        if re.match(r"^ {0,3}#{1,6}\s", prev):
            continue
        # Indented code block: the rule is inside literal text, not a paragraph.
        if prev.startswith("    "):
            continue
        # An HTML block (`<!-- ... -->`, `</script>`) is closed on its own line,
        # so the rule under it is a thematic break, not a heading underline.
        if prev.rstrip().endswith(">") and "<" in prev:
            continue
        found.append(i + 1)
    return found


def fix(path: str, lineno: int) -> bool:
    with open(path, encoding="utf-8", errors="replace") as fh:
        lines = fh.read().split("\n")
    idx = lineno - 1
    if idx <= 0 or idx >= len(lines):
        return False
    if lines[idx].rstrip() != "---" or not lines[idx - 1].strip():
        return False
    lines.insert(idx, "")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true", help="insert the missing blank line")
    ap.add_argument("--paths", nargs="*", default=["."], help="files or directories")
    args = ap.parse_args()

    total_files = 0
    total_hits = 0
    for path in sorted(set(_iter_markdown(args.paths))):
        hits = offenders(path)
        if not hits:
            continue
        total_files += 1
        total_hits += len(hits)
        rel = os.path.relpath(path)
        if args.fix:
            for lineno in reversed(hits):
                fix(path, lineno)
            print(f"FIXED {rel}: {len(hits)} rule(s) at {', '.join(map(str, hits))}")
        else:
            for lineno in hits:
                print(f"{rel}:{lineno}: '---' has no blank line above it")

    if args.fix:
        print(f"\n{total_files} file(s), {total_hits} rule(s) fixed")
        return 0
    if total_hits:
        print(
            f"\n{total_hits} setext-rule defect(s) in {total_files} file(s). "
            "A '---' directly under prose renders that prose as an H2 heading. "
            "Fix: add a blank line above the rule, or run --fix.",
            file=sys.stderr,
        )
        return 1
    print("OK: no setext-rule defects")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
