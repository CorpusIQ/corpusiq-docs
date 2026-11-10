#!/usr/bin/env python3
"""Rewrite PROGRESS.md stated counts to match the tracked tree.

check_progress_counts.py only REPORTS a mismatch, so every commit that adds a
markdown file (auto-published changelogs, skills sweeps) left PROGRESS.md stale
and failed the required `frontmatter` check on its PR. This syncs the values
first so the gate has nothing to catch. Idempotent: exits 0 with no write when
everything already agrees.
"""
import datetime
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_progress_counts as c  # noqa: E402


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    path = os.path.join(root, c.PROGRESS)
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    files = c.tracked_files(root)

    edits = []
    for label, pred, pat in c.CLAIMS:
        actual = sum(1 for f in files if pred(f))
        m = re.search(pat, text)
        if not m:
            continue
        stated = int(m.group(1).replace(",", ""))
        if stated == actual:
            continue
        edits.append((m.start(1), m.end(1), label, stated, actual))

    if not edits:
        print("sync_progress_counts: already in sync")
        return 0

    for start, end, _label, _stated, actual in sorted(edits, reverse=True):
        text = text[:start] + format(actual, ",") + text[end:]

    today = datetime.date.today()
    text = re.sub(r"(## File count \(updated )[A-Z][a-z]+ \d{1,2}, \d{4}",
                  lambda m: m.group(1) + today.strftime("%B ") +
                  str(today.day) + today.strftime(", %Y"), text, count=1)
    text = re.sub(r'(last_updated: ")[\d-]+(")',
                  lambda m: m.group(1) + today.isoformat() + m.group(2),
                  text, count=1)

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    for _s, _e, label, stated, actual in edits:
        print("sync_progress_counts: {} {} -> {}".format(label, stated, actual))
    return 0


if __name__ == "__main__":
    sys.exit(main())
