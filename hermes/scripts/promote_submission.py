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
from datetime import datetime, timezone, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"
TOKEN_PATH = Path("/home/hermes/.hermes/profiles/corpusiq/secrets/github.token")
# Arizona has no DST (UTC-7 year round). Every human-facing "Last updated" /
# contribution stamp uses this, not UTC: a run at 22:00 AZ is already the next
# UTC day, so UTC stamps published tomorrow's date on the directory overnight.
AZ_TZ = timezone(timedelta(hours=-7))


def az_now():
    return datetime.now(AZ_TZ)


def az_today():
    return az_now().strftime("%Y-%m-%d")


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
    "SDKs & Libraries": "## 📦 SDKs & Libraries",
    "UI & Dashboards": "## 🖥️ Interfaces & UI",
}

# discover.py stamps every queued row with its lowercase SEARCH BUCKET ("core",
# "mcp", "skills", ...), not a directory display category. Without this map a
# queued row reached promotion and died on "category 'core' has no directory
# heading", so no hand-promoted repo could ever be placed (first hit
# 2026-10-31 on zeyxx/hermes-antigravity). Keys must cover every bucket in
# discover.SEARCH_QUERIES.
CATEGORY_ALIASES = {
    "core": "Core Framework",
    "official": "Core Framework",
    "forks": "Forks & Derivatives",
    "mcp": "MCP & Integrations",
    "integrations": "MCP & Integrations",
    "messaging": "MCP & Integrations",
    "apis": "MCP & Integrations",
    "skills": "Skills & Plugins",
    "ui": "UI & Dashboards",
    "deployment": "Deployment",
    "production": "Deployment",
    "memory": "Memory & Knowledge",
    "research": "Memory & Knowledge",
    "benchmarks": "Memory & Knowledge",
    "content": "Content & Media",
    "security": "Security & Governance",
    "tutorials": "Documentation & Learning",
    "examples": "Guides",
    "migration": "Guides",
    "sdks": "SDKs & Libraries",
}


def normalise_category(raw):
    """Map a discover.py bucket (or a display name) to a directory category."""
    cat = (raw or "").strip()
    return CATEGORY_ALIASES.get(cat.lower(), cat)


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


def _norm_label(s):
    """Normalise a table label or heading so emoji/markup/link syntax drop out."""
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[^A-Za-z0-9 &]+", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def sync_category_count(text, heading):
    """Recount a section's entries and write the true number into its nav row.

    ``bump_published_counts`` only patches the global repo stamps, so the
    per-category table drifted every time a repo was inserted (the published
    index advertised 21 UI entries while the section held 23). Recount from the
    headings themselves so no insert can push the table out of date again.
    """
    if heading not in text:
        return text
    start = text.index(heading)
    nxt = text.find("\n## ", start + 1)
    section = text[start:len(text) if nxt == -1 else nxt]
    lines = section.split("\n")
    repo_blocks = 0
    total_blocks = 0
    for i, line in enumerate(lines):
        if not line.startswith("### "):
            continue
        total_blocks += 1
        if "\u2b50" in line:
            repo_blocks += 1
            continue
        for nxt_line in lines[i + 1:]:
            if not nxt_line.strip():
                continue
            if nxt_line.lstrip().startswith("\u2b50"):
                repo_blocks += 1
            break
    # Only trust the recount where the section is uniformly repo entries.
    # Sections whose items are bullets or prose sub-headings count differently
    # and a blind rewrite would REPLACE a correct number with a wrong one.
    if total_blocks == 0 or repo_blocks / total_blocks < 0.9:
        return text
    count = repo_blocks
    target = _norm_label(heading.lstrip("# "))

    def repl(m):
        if _norm_label(m.group(1)) == target:
            return "| {} | {} |".format(m.group(1), count)
        return m.group(0)

    return re.sub(r"(?m)^\| ([^|\n]+?) \| (\d+) \|", repl, text)


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
        # The mirror is a secondary surface: the published index is what readers
        # see. Warn instead of aborting so a category the mirror never carried
        # (Documentation & Learning, Guides) still reaches the served page.
        print(f"WARN: ecosystem.md has no heading for category {row.get('category')!r}"
              " - entry NOT written to the mirror")
        return False

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
    updated = sync_category_count(updated, heading)
    ECOSYSTEM.write_text(updated)
    return True


PUBLISHED_HEADINGS = {
    "Content & Media": "## 🎬 Content & Media",
    "Core Framework": "## 🏛 Core & Official",
    "Deployment": "## 🚀 Deployment & Infrastructure",
    "Documentation & Learning": "## 📚 Documentation & Learning",
    "Forks & Derivatives": "## 🔀 Forks & Derivatives",
    "Guides": "## 📖 Guides",
    "Community & Awesome Lists": "## 👥 Community & Awesome Lists",
    "Memory & Knowledge": "## 🧠 Memory & Knowledge",
    "MCP & Integrations": "## 🔌 MCP & Integrations",
    "Orchestration & Multi-Agent": "## 🎯 Orchestration, Multi-Agent & Swarms",
    "Security & Governance": "## 🔒 Security & Governance",
    "Skills & Plugins": "## 🛠 Skills & Plugins",
    "Tools & Utilities": "## 🛠 Tools & Utilities",
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
        + (f"**Related:** [MCP Ecosystem →](/hermes/mcp-ecosystem)\n" if "mcp" in (row.get("category") or "").lower() else "")
        + f"\n---\n\n"
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
    today = az_today()
    text = re.sub(r'last_updated: "\d{4}-\d{2}-\d{2}"',
                  f'last_updated: "{today}"', text, count=1)
    text = re.sub(r"\*\*Last updated:\*\* [A-Z][a-z]+ \d{1,2}, \d{4}",
                  "**Last updated:** " + az_now().strftime("%B ") + str(az_now().day) + ", " + str(az_now().year),
                  text, count=1)
    # Mirror shape: "*429+ repositories in the Hermes ecosystem. Last updated: 2026-10-23.*"
    text = re.sub(r"(Last updated: )\d{4}-\d{2}-\d{2}", r"\g<1>" + today, text, count=1)
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
    updated = sync_category_count(updated, heading)
    PUBLISHED_INDEX.write_text(updated)
    align_mirror_counts(updated)
    return True


def align_mirror_counts(published_text):
    """Make the mirror's numeric stamps agree with the published page.

    ``bump_published_counts`` increments only the FIRST match of each stamp
    pattern, so a page carrying several stamps ended up advertising two
    different totals (430+ at the top, 431+ lower down). The published index is
    the source of truth; project its number onto every mirror stamp.
    """
    m = re.search(r"\*\*Repos indexed:\*\* (\d+)\+", published_text)
    if not m or not ECOSYSTEM.exists():
        return
    count = m.group(1)
    mirror = ECOSYSTEM.read_text()
    aligned = re.sub(r"(\d+)\+ (repositories|repos)", r"{}+ \g<2>".format(count), mirror)
    approved_path = DATA_DIR / "approved_repos.json"
    if approved_path.exists():
        n_approved = len(load(approved_path))
        aligned = re.sub(r"(\d+) auto-approved", r"{} auto-approved".format(n_approved), aligned)
    if aligned != mirror:
        ECOSYSTEM.write_text(aligned)


def credit_contributor(username):
    path = DATA_DIR / "contributors.json"
    contributors = load(path)
    today = az_today()
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
    today = az_today()
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
    ap.add_argument("--category", default=None,
                    help="override the directory category (default: derive from the "
                         "queued discover.py bucket)")
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
    category = normalise_category(args.category or queued.get("category"))
    if category not in CATEGORY_HEADINGS:
        raise SystemExit(
            f"category {category!r} has no directory heading. Add it to "
            "CATEGORY_HEADINGS (and PUBLISHED_HEADINGS) first, or pass --category "
            "with one of: " + ", ".join(sorted(CATEGORY_HEADINGS))
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
        "category": category,
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
    # The served page is ecosystem/index.md. Writing only ecosystem.md left every
    # promotion invisible on the live site (root-caused 2026-10-16, #109), and
    # the inserter alone did not fix it: it has to be CALLED from the promotion
    # path or the twin keeps absorbing promotions that no reader can see.
    published = insert_into_published_index(row)
    print(f"approved: {row['name']} ({row['category']}, {row['stars']} stars)")
    print(f"ecosystem.md: {'entry inserted' if inserted else 'already present'}")
    print(f"ecosystem/index.md: {'entry inserted' if published else 'already present or unmapped'}")
    if not published:
        print("WARN: the served directory did not take the entry - check the category heading map")
    print("PROMOTION_OK")


if __name__ == "__main__":
    main()
