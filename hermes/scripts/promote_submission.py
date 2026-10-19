#!/usr/bin/env python3
"""Promote a scored submission to the ecosystem directory.

Why this exists
---------------
``process_submissions.py`` decides purely on the tier returned by the scorer, and
the scorer reads only the repo NAME, DESCRIPTION and TOPICS. A repository that is
genuinely built for Hermes but does not say "hermes" in its name scores low and
is auto-rejected by the ``else`` branch. That is how a real integration with a
skills installer targeting ``~/.hermes/skills`` scored 24 and was queued for
rejection (issue 109).

The rubric measures how well a repo ADVERTISES itself, not whether it works with
Hermes. This tool is the human-judgement path that closes that gap: it takes a
repo already sitting in the review queue, records WHY it was promoted, and keeps
every downstream file consistent in one transaction.

Usage:
    python3 promote_submission.py --repo owner/name --note "reason" [--dry-run]

What it updates, all idempotently:
    data/approved_repos.json      append (refreshed from GitHub, not the stale row)
    data/pending_review.json      remove
    data/review_log.json          append the promotion and its reason
    data/contributors.json        credit the submitter
    ecosystem.md                  insert the entry, star-sorted within its category
    contributors/index.md         add the submitter to the contributor table
"""
import argparse
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"
TOKEN_PATH = Path("/home/hermes/.hermes/profiles/corpusiq/secrets/github.token")

ECOSYSTEM = REPO_ROOT / "ecosystem.md"
# The page users actually see. ecosystem.md COLLIDES with ecosystem/index.md at
# the /hermes/ecosystem/ URL and is not emitted by mkdocs, so an entry written
# only to ecosystem.md is invisible on the live site (root-caused 2026-10-16:
# the hyperconsciousness promotion of Oct 14 never appeared). Every promotion
# must write BOTH surfaces.
PUBLISHED_INDEX = REPO_ROOT / "ecosystem" / "index.md"
# Two contributor surfaces, two different table shapes. The short table lives on
# contributors.md; the index page carries its own Top Contributors table. Both
# have to be credited or the credit is inconsistent depending on which page a
# reader lands on.
CONTRIBUTORS_TABLE = REPO_ROOT / "contributors.md"
CONTRIBUTORS_INDEX = REPO_ROOT / "contributors" / "index.md"

CATEGORY_HEADINGS = {
    "Content & Media": "## 🎬 Content & Media",
    "Core Framework": "## 🧠 Core Framework",
    "Deployment": "## 🚀 Deployment",
    "Forks & Derivatives": "## 🍴 Forks & Derivatives",
    "Integrations": "## 🔗 Integrations",
    "Memory & Knowledge": "## 💾 Memory & Knowledge",
    "MCP & Integrations": "## 🔌 MCP Servers",
    "Official Resources": "## 🏛️ Official Resources",
    "Other": "## 📋 Other",
    "Research & Benchmarks": "## 🔬 Research & Benchmarks",
    "Security & Governance": "## 🛡️ Security & Governance",
    "Skills & Plugins": "## 🔧 Skills & Plugins",
    "UI & Dashboards": "## 🖥️ Interfaces & UI",
}


def load(path, default=None):
    p = Path(path)
    if not p.exists():
        return [] if default is None else default
    with open(p) as fh:
        return json.load(fh)


def save(path, data):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as fh:
        json.dump(data, fh, indent=2, default=str)
        fh.write("\n")


def fetch_repo(full_name):
    """Refresh from GitHub. The queued row can be weeks stale."""
    token = TOKEN_PATH.read_text().strip()
    req = urllib.request.Request(
        f"https://api.github.com/repos/{full_name}",
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "CorpusIQ-Promotion/1.0",
        },
    )
    return json.loads(urllib.request.urlopen(req, timeout=45).read())


def entry_block(row):
    stars = row.get("stars", 0)
    topics = row.get("topics") or []
    meta = f"**Language:** {row.get('language') or 'Unknown'}"
    if topics:
        meta += " | **Topics:** " + ", ".join(topics)
    desc = (row.get("description") or "").strip()
    return (
        f"### [{row['name']}]({row['url']}) \u2b50 {stars}\n"
        f"\n"
        f">{desc}\n"
        f"\n"
        f"{meta}\n"
        f"\n"
        f"---\n"
    )


def insert_into_ecosystem(row):
    """Insert star-sorted inside the row's category. Returns True when written."""
    text = ECOSYSTEM.read_text()
    if row["url"] in text:
        return False

    heading = CATEGORY_HEADINGS.get(row.get("category", ""))
    if not heading or heading not in text:
        raise SystemExit(f"category heading not found for {row.get('category')!r}")

    start = text.index(heading)
    nxt = text.find("\n## ", start + 1)
    section_end = len(text) if nxt == -1 else nxt
    section = text[start:section_end]

    # Existing entries: (stars, offset within the section)
    found = []
    for m in re.finditer(r"^### .*?\u2b50 (\d+)\s*$", section, re.M):
        found.append((int(m.group(1)), m.start()))

    insert_at = section_end - start
    for stars, offset in found:
        if stars < row.get("stars", 0):
            insert_at = offset
            break

    block = entry_block(row)
    prefix = "" if section[:insert_at].endswith("\n\n") or insert_at == 0 else "\n"
    updated = text[:start + insert_at] + prefix + block + "\n" + text[start + insert_at:]
    ECOSYSTEM.write_text(updated)
    return True


PUBLISHED_HEADINGS = {
    "Content & Media": "## 🎬 Content & Media",
    "Core Framework": "## 🏛 Core & Official",
    "Deployment": "## 🚀 Deployment & Infrastructure",
    "Forks & Derivatives": "## 🔀 Forks & Derivatives",
    "Memory & Knowledge": "## 🧠 Memory & Knowledge",
    "MCP & Integrations": "## 🔌 MCP & Integrations",
    "Orchestration & Multi-Agent": "## 🎯 Orchestration, Multi-Agent & Swarms",
    "Security & Governance": "## 🔒 Security & Governance",
    "Skills & Plugins": "## 🛠 Skills & Plugins",
    "UI & Dashboards": "## 🖥 UI & Dashboards",
}


def published_block(row):
    """Entry block in the published index's own shape (heading, then star line)."""
    stars = int(row.get("stars") or 0)
    lang = row.get("language") or "TypeScript"
    slug = re.sub(r"^https?://", "", row["url"]).rstrip("/")
    desc = (row.get("description") or "").replace("\n", " ").strip()
    topics = row.get("topics") or []
    caps = ", ".join(topics[:8]) if topics else desc[:120]
    return (
        f"### {row['name']}\n"
        f"⭐ **{stars:,}** · `{lang}` · [{slug}]({row['url']})\n\n"
        f"{desc}\n\n"
        f"**Key capabilities:** {caps}\n"
        f"**Related:** [MCP Ecosystem →](/hermes/mcp-ecosystem)\n\n---\n\n"
    )


def bump_published_counts(text):
    """Increment the directory-count stamps so the page does not drift per insert.

    One callback for every stamp shape. Chained `re.sub` calls double-counted:
    the "repos, docs" pass rewrote a line that the bare "repos" pass then
    matched and bumped a second time. The published page carries THREE shapes
    ("N+ repos, docs", "N+ repositories", "N+ repos"), and a pass that only
    knows two of them leaves the third drifting - which is exactly how the
    directory ended up advertising 199+ at the top and 196+ further down.
    """
    def bump(m):
        return f"{int(m.group(1)) + 1}+ {m.group(2)}{m.group(3) or ''}"

    def bump_indexed(m):
        return f"**Repos indexed:** {int(m.group(1)) + 1}+"

    text = re.sub(r"(\d+)\+ (repositories|repos)(, docs)?", bump, text)
    text = re.sub(r"\*\*Repos indexed:\*\* (\d+)\+", bump_indexed, text)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    text = re.sub(r'last_updated: "\d{4}-\d{2}-\d{2}"',
                  f'last_updated: "{today}"', text, count=1)
    text = re.sub(r"\*\*Last updated:\*\* [A-Z][a-z]+ \d{1,2}, \d{4}",
                  "**Last updated:** " + datetime.now(timezone.utc).strftime("%B %-d, %Y"),
                  text, count=1)
    return text


def insert_into_published_index(row):
    """Insert the same entry into ecosystem/index.md, the page that is served.

    ecosystem.md is not emitted by the docs build, so without this the promotion
    is invisible on the live site. Star-sorted within the mapped section.
    Returns True when written, False when already present or unmapped.
    """
    if not PUBLISHED_INDEX.exists():
        return False
    text = PUBLISHED_INDEX.read_text()
    if row["url"] in text:
        return False
    heading = PUBLISHED_HEADINGS.get(row.get("category", ""))
    if not heading or heading not in text:
        print(f"WARN: published index has no heading for category {row.get('category')!r}"
              f" - entry NOT written to {PUBLISHED_INDEX.name}")
        return False

    start = text.index(heading)
    nxt = text.find("\n## ", start + 1)
    section_end = len(text) if nxt == -1 else nxt
    section = text[start:section_end]

    # Blocks inside the section, each starting at a "### " line.
    starts = [m.start() for m in re.finditer(r"^### ", section, re.M)]
    mine = row.get("stars", 0)
    insert_at = None
    for off, blk_start in enumerate(starts):
        blk_end = starts[off + 1] if off + 1 < len(starts) else len(section)
        blk = section[blk_start:blk_end]
        m = re.search(r"⭐ \*\*([\d,]+)\*\*", blk)
        blk_stars = int(m.group(1).replace(",", "")) if m else 0
        if blk_stars < mine:
            insert_at = blk_start
            break
    if insert_at is None:
        # Nothing has fewer stars: append after the last block.
        insert_at = len(section)

    block = published_block(row)
    updated_section = section[:insert_at] + block + section[insert_at:]
    updated = text[:start] + updated_section + text[section_end:]
    updated = bump_published_counts(updated)
    PUBLISHED_INDEX.write_text(updated)
    return True


def credit_contributor(username):
    path = DATA_DIR / "contributors.json"
    contributors = load(path)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for c in contributors:
        if c.get("github_user") == username:
            c["submissions"] = c.get("submissions", 0) + 1
            c["approved"] = c.get("approved", 0) + 1
            c["last_contribution"] = today
            c.setdefault("role", "contributor")
            save(path, contributors)
            return
    contributors.append({
        "github_user": username,
        "submissions": 1,
        "approved": 1,
        "rejected": 0,
        "first_contribution": today,
        "last_contribution": today,
        "role": "contributor",
    })
    save(path, contributors)


def update_contributors_pages(username):
    """Credit the submitter on both contributor surfaces, tol erantly."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    link = f"[@{username}](https://github.com/{username})"

    # contributors.md: replace the empty-row placeholder, or append to the table.
    if CONTRIBUTORS_TABLE.exists():
        text = CONTRIBUTORS_TABLE.read_text()
        if username not in text:
            row = f"| {link} | 1 | 1 | {today} | {today} |"
            placeholder = "| - | - | - | - | - |"
            if placeholder in text:
                text = text.replace(placeholder, row)
            else:
                header = (
                    "| Contributor | Submissions | Approved | "
                    "First Contribution | Last Active |"
                )
                idx = text.index(header)
                sep_end = text.index("\n", text.index("\n", idx) + 1) + 1
                text = text[:sep_end] + row + "\n" + text[sep_end:]
            text = re.sub(
                r"\*No community contributors yet\. \[Be the first \S+\s*"
                r"\(https://github\.com/CorpusIQ/corpusiq-docs/issues/new\?labels=pending-review\)\*\n?",
                "",
                text,
            )
            CONTRIBUTORS_TABLE.write_text(text)

    # contributors/index.md: its table has a Role column instead of dates, and it
    # is ordered by submissions, so a new contributor goes below existing rows,
    # not above them.
    if CONTRIBUTORS_INDEX.exists():
        text = CONTRIBUTORS_INDEX.read_text()
        if username not in text:
            row = f"| {link} | 1 | 1 | Contributor |"
            header = "| Contributor | Submissions | Approved | Role |"
            if header in text:
                idx = text.index(header)
                end = text.index("\n", text.index("\n", idx) + 1) + 1
                while end < len(text) and text[end:].lstrip().startswith("| ["):
                    end = text.index("\n", end) + 1
                text = text[:end] + row + "\n" + text[end:]
                CONTRIBUTORS_INDEX.write_text(text)


# Back-compat alias for the single-page name used earlier.
update_contributors_page = update_contributors_pages


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, help="owner/name")
    ap.add_argument("--note", required=True, help="why this was promoted by hand")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    approved_path = DATA_DIR / "approved_repos.json"
    pending_path = DATA_DIR / "pending_review.json"
    review_log_path = DATA_DIR / "review_log.json"

    approved = load(approved_path)
    pending = load(pending_path)
    review_log = load(review_log_path)

    if any(r.get("name", "").lower() == args.repo.lower() for r in approved):
        raise SystemExit(f"{args.repo} is already approved; nothing to do.")

    queued = next(
        (r for r in pending if r.get("name", "").lower() == args.repo.lower()), None
    )
    if queued is None:
        raise SystemExit(f"{args.repo} is not in the review queue.")
    if queued.get("category") not in CATEGORY_HEADINGS:
        raise SystemExit(
            f"category {queued.get('category')!r} has no directory heading. "
            "Add it to CATEGORY_HEADINGS first."
        )

    live = fetch_repo(args.repo)
    row = {
        "name": live["full_name"],
        "url": live["html_url"],
        "description": live.get("description", ""),
        "stars": live.get("stargazers_count", 0),
        "forks": live.get("forks_count", 0),
        "language": live.get("language", ""),
        "topics": live.get("topics", []),
        "updated_at": (live.get("updated_at") or "")[:10],
        "category": queued["category"],
        "score": queued.get("score"),
        "tier": queued.get("tier"),
        "submitter": queued.get("submitter"),
        "submission_issue": queued.get("submission_issue"),
        "status": "approved",
        "approved_at": datetime.now(timezone.utc).isoformat(),
        "promotion_note": args.note,
        "promoted_from": f"{queued.get('tier')} score {queued.get('score')}",
    }

    print(f"refresh: stars {queued.get('stars')} -> {row['stars']}, "
          f"forks {queued.get('forks')} -> {row['forks']}, "
          f"updated {queued.get('updated_at', '')[:10]} -> {row['updated_at']}")

    if args.dry_run:
        print("DRY RUN, nothing written.")
        print(entry_block(row))
        return

    approved.append(row)
    save(approved_path, approved)

    pending = [r for r in pending if r.get("name", "").lower() != args.repo.lower()]
    save(pending_path, pending)

    review_log.append({
        "repo": row["name"],
        "action": "approved_manual_promotion",
        "score": row["score"],
        "tier": row["tier"],
        "reason": args.note,
        "issue": row["submission_issue"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })
    save(review_log_path, review_log)

    if row.get("submitter"):
        credit_contributor(row["submitter"])
        update_contributors_page(row["submitter"])

    inserted = insert_into_ecosystem(row)
    print(f"approved: {row['name']} ({row['category']}, {row['stars']} stars)")
    print(f"ecosystem.md: {'entry inserted' if inserted else 'already present'}")
    print("PROMOTION_OK")


if __name__ == "__main__":
    main()
