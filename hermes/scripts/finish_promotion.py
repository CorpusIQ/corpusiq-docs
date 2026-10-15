#!/usr/bin/env python3
"""Finish a promotion whose JSON phase already landed but whose file phase did not.

``promote_submission.py`` writes the JSON stores first and the files last, so a
failure in the file phase leaves the data consistent and the directory entry
missing. This completes the file phase from the approved row. Safe to rerun: both
writers skip work that is already done.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import promote_submission as p


def main():
    repo = sys.argv[1] if len(sys.argv) > 1 else "louis030195/hyperconsciousness"
    approved = p.load(p.DATA_DIR / "approved_repos.json")
    row = next((r for r in approved if r.get("name", "").lower() == repo.lower()), None)
    if row is None:
        raise SystemExit(f"{repo} is not in approved_repos.json; nothing to finish.")

    inserted = p.insert_into_ecosystem(row)
    print("ecosystem.md:", "entry inserted" if inserted else "already present")

    if row.get("submitter"):
        p.update_contributors_pages(row["submitter"])
        print("contributor pages: credited", row["submitter"])

    print("FINISH_OK")


if __name__ == "__main__":
    main()
