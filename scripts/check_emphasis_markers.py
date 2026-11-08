#!/usr/bin/env python3
"""Detect broken emphasis/code markers in served markdown pages.

Class this guards (found live 2026-11-08)
----------------------------------------
`hermes/mcp/servers/external/dutykit-mcp/index.md` shipped the sentence

    ... `io.github.renschrder-stack/dutykit` **0.1.1`), which reads ...

One stray backtick after `0.1.1` and an unclosed `**` left the live page
rendering a literal ``**0.1.1`),`` to every reader. MkDocs builds non-strict,
so the page deployed fine, no other gate looks at inline emphasis, and the
defect was only visible on the served HTML.

The rule
--------
After fenced code blocks and balanced inline code spans are removed, the
remaining count of `**` must be even (bold on/off) and the remaining count of
backticks must be zero (an unmatched inline code opener). Both are file-level
tests: real markdown allows a code span to wrap a line, so a single odd line is
a hint, not automatically a failure. The line numbers are printed as hints.

Usage
-----
    python3 scripts/check_emphasis_markers.py                 # whole served tree
    python3 scripts/check_emphasis_markers.py FILE [FILE...]  # specific files
    python3 scripts/check_emphasis_markers.py --changed       # vs origin/main

Exit codes: 0 clean, 1 defects found, 2 bad invocation.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

FENCE = re.compile(r"^(?P<fence>[ \t]{0,3}(?P<marker>`{3,}|~{3,})[^\n]*\n(?:.*?\n)??[ \t]{0,3}(?P=marker)[ \t]*$)", re.S | re.M)
INLINE_CODE = re.compile(r"`[^`\n]+`")
ROOTS = ("docs", "hermes", "connectors")


def strip_code(text: str) -> str:
    """Remove fenced blocks and balanced inline code spans, preserving newlines."""
    def blank(match: re.Match) -> str:
        return "\n" * match.group(0).count("\n")

    text = FENCE.sub(blank, text)
    return INLINE_CODE.sub(lambda m: " " * len(m.group(0)), text)


def check_text(text: str) -> tuple[bool, list[str]]:
    body = strip_code(text)
    problems: list[str] = []
    bold = body.count("**")
    ticks = body.count("`")
    if bold % 2:
        problems.append(f"unbalanced bold markers: {bold} '**' left after code removal")
    if ticks % 2:
        problems.append(f"unbalanced inline code: {ticks} backtick(s) left after code removal")
    return (not problems), problems


def odd_lines(text: str, needle: str) -> list[int]:
    """Line numbers whose own count of `needle` is odd (hint only)."""
    hits, fenced, out = [], False, []
    marker = None
    for i, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            m = stripped[:3]
            if not fenced:
                fenced, marker = True, m
            elif m == marker:
                fenced = False
            continue
        if fenced:
            continue
        if line.count(needle) % 2:
            out.append(i)
    return out


def iter_files(paths: list[str]):
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if not d.startswith(".") and d != "site"]
                for name in files:
                    if name.endswith((".md", ".mdx")):
                        yield os.path.join(root, name)
        elif p.endswith((".md", ".mdx")):
            yield p


def changed_files() -> list[str]:
    try:
        out = subprocess.run(
            ["git", "diff", "--name-only", "--diff-filter=ACM", "origin/main", "--"],
            capture_output=True, text=True, check=True,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []
    return [f for f in out.split() if f.endswith((".md", ".mdx")) and os.path.exists(f)]


def main(argv: list[str]) -> int:
    if "--changed" in argv:
        targets = changed_files()
        if not targets:
            print("check_emphasis_markers: no changed markdown vs origin/main")
            return 0
    else:
        targets = [a for a in argv[1:] if not a.startswith("-")] or list(ROOTS)

    files = sorted(set(iter_files(targets)))
    failures = 0
    for path in files:
        try:
            text = open(path, encoding="utf-8").read()
        except (OSError, UnicodeDecodeError) as exc:
            print(f"SKIP {path}: {exc}")
            continue
        ok, problems = check_text(text)
        if ok:
            continue
        failures += 1
        print(f"FAIL {path}")
        for problem in problems:
            print(f"     {problem}")
        for line in odd_lines(text, "**")[:6]:
            print(f"     hint: line {line} has an odd number of '**' inside the text")
        for line in odd_lines(text, "`")[:6]:
            print(f"     hint: line {line} has an odd backtick count")

    print(f"check_emphasis_markers: scanned {len(files)} file(s), {failures} with defects")
    if failures:
        print("RESULT: FAIL - close the stray ` or ** so the served page renders as written")
        return 1
    print("OK: emphasis and inline-code markers are balanced")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
