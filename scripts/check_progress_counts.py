#!/usr/bin/env python3
"""Block a commit when PROGRESS.md's file counts disagree with the tree.

Why
---
The file-count block at the top of PROGRESS.md is hand-maintained and is the
one number on that page a reader can check against the repo in one command.
It has drifted repeatedly because it is written by hand mid-cycle and the
cycle's own merges land afterwards. On Nov 7 2026 #239 refreshed the block to
3,633 Markdown files and 1,519 under hermes/mcp/ - the values from 608cff9 -
and then merged after #237 had already added three more files, so main carried
a number that was wrong the moment it landed. Nothing failed, because nothing
reads the block.

This is the same class count_stamp_check.py and reconcile_ecosystem_counts.py
fix for other pages: a derived number maintained by hand. The difference is
that these five are derivable from the tree, so this one derives them.

Semantics
---------
Counts come from `git ls-files`, the index, not from `find` on the working
tree. That matters twice: untracked scratch files cannot inflate the count
(a working-tree find reports higher numbers, which is how the drift went
unnoticed), and staged files count as they will exist after the commit.

A missing claim is not a failure. If a line is reworded beyond recognition the
check prints what it could not parse and exits 0, because a formatting change
is not a wrong number. A parsed claim whose value disagrees with the tree is a
failure, and the message names both numbers.

Usage
-----
    python3 scripts/check_progress_counts.py [repo_root]
    python3 scripts/check_progress_counts.py --fix [repo_root]

Exit 0 when every parsed claim matches, 1 when any parsed claim disagrees.
With --fix, a disagreeing claim is rewritten to the derived value in place and
the script exits 0, so an automated publisher can repair the block instead of
handing back a red check on a number no human typed this cycle.
"""
import re
import subprocess
import sys

PROGRESS = "PROGRESS.md"

# (label, path predicate, regex capturing the stated value from PROGRESS.md)
# The patterns anchor on the words PROGRESS.md uses so a rewrite that keeps the
# meaning keeps working, and a rewrite that drops the claim is skipped rather
# than failed.


def _md(path):
    return path.endswith(".md")


def _under_mcp(path):
    return path.startswith("hermes/mcp/") and path.endswith(".md")


def _setup_guide(path):
    if not path.startswith("hermes/skills/") or not path.endswith(".md"):
        return False
    return "setup" in path.rsplit("/", 1)[-1]


def _top_level_docs_page(path):
    return path.startswith("docs/") and path.count("/") == 1 and path.endswith(".md")


def _connector_reference(path):
    return path.startswith("connectors/") and path.count("/") == 1 and path.endswith(".md")


CLAIMS = [
    ("Total Markdown files", _md,
     r"Total Markdown files:\**\s*([\d,]+)"),
    ("MCP servers under hermes/mcp", _under_mcp,
     r"MCP servers:\**\s*([\d,]+)\s+total \.md under hermes/mcp/"),
    ("Setup guides under hermes/skills", _setup_guide,
     r"Skills catalog:\**\s*([\d,]+)\s+setup guides"),
    ("Top-level docs pages", _top_level_docs_page,
     r"SEO pages:\**\s*([\d,]+)\s+top-level docs pages"),
    ("Connector reference pages", _connector_reference,
     r"plus\s+([\d,]+)\s+connector reference pages"),
]


def tracked_files(root):
    out = subprocess.run(["git", "-C", root, "ls-files"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit("check_progress_counts: git ls-files failed: %s"
                 % out.stderr.strip()[:200])
    return [f for f in out.stdout.split("\n") if f]


def read_progress(root):
    try:
        with open("%s/%s" % (root, PROGRESS), encoding="utf-8") as fh:
            return fh.read()
    except OSError as exc:
        sys.exit("check_progress_counts: cannot read %s (%s)" % (PROGRESS, exc))


def evaluate(text, files):
    """Return (failures, unparsed, checked) for the claims in ``text``.

    Split out from main() so the test suite can drive it with a synthetic file
    listing and a synthetic PROGRESS.md, without needing a git checkout.
    """
    failures = []
    checked = 0
    unparsed = []

    for label, predicate, pattern in CLAIMS:
        actual = sum(1 for f in files if predicate(f))
        match = re.search(pattern, text)
        if not match:
            unparsed.append(label)
            continue
        stated = int(match.group(1).replace(",", ""))
        checked += 1
        if stated != actual:
            failures.append((label, stated, actual))

    return failures, unparsed, checked


def apply_fix(text, failures, files):
    """Rewrite each failing claim to its derived value. Returns (text, changes).

    Kept separate from evaluate() so the test suite can drive it. Only a claim
    that failed is touched: a claim that already agrees is left byte-identical,
    which keeps the diff to the numbers that actually moved.
    """
    changes = []
    for label, predicate, pattern in CLAIMS:
        if label not in [f[0] for f in failures]:
            continue
        actual = format(sum(1 for f in files if predicate(f)), ",")

        def repl(match, actual=actual):
            head = match.group(0)[:match.start(1) - match.start(0)]
            tail = match.group(0)[match.end(1) - match.start(0):]
            return head + actual + tail

        text, n = re.subn(pattern, repl, text, count=1)
        if n:
            changes.append("%s -> %s" % (label, actual))
    return text, changes


def main():
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    do_fix = "--fix" in sys.argv
    root = argv[0] if argv else "."
    files = tracked_files(root)
    text = read_progress(root)
    failures, unparsed, checked = evaluate(text, files)

    for label, stated, actual in failures:
        print("FAIL  %-34s PROGRESS.md says %s, tree has %s"
              % (label, format(stated, ","), format(actual, ",")))
    for label in unparsed:
        print("SKIP  %-34s no claim found in PROGRESS.md" % label)

    if failures and do_fix:
        text, changes = apply_fix(text, failures, files)
        with open("%s/%s" % (root, PROGRESS), "w", encoding="utf-8") as fh:
            fh.write(text)
        for c in changes:
            print("FIXED %s" % c)
        again, unparsed2, checked2 = evaluate(read_progress(root), files)
        if again:
            print("\nRESULT: --fix left %d claim(s) still disagreeing" % len(again))
            return 1
        print("\nRESULT: repaired %d claim(s); %d now match the tree"
              % (len(changes), checked2))
        return 0

    if failures:
        print("\nRESULT: %d claim(s) disagree with the tree. Update the "
              "file-count block at the top of PROGRESS.md, or bypass once "
              "with: git commit --no-verify" % len(failures))
        return 1

    print("RESULT: %d claim(s) match the tree (%d skipped)"
          % (checked, len(unparsed)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
