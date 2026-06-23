#!/usr/bin/env python3
"""
Hermes Ecosystem Discovery Engine
Nightly GitHub search for Hermes-related repositories with automated scoring.
Runs 10 PM - 2 AM Arizona time.

Usage:
    python3 discover.py                    # Full discovery run
    python3 discover.py --dry-run          # Show what would be added
    python3 discover.py --score-only REPO  # Score a single repo
"""
import json
import os
import sys
import time
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ── Config ──────────────────────────────────────────────────
AZ_TZ = timezone(timedelta(hours=-7))  # Arizona = UTC-7 (no DST)
REPO_ROOT = Path("/tmp/corpusiq-docs/hermes")
DATA_DIR = REPO_ROOT / "data"
TOKEN_PATH = Path(os.path.expanduser("~/.hermes/profiles/corpusiq/secrets/github.token"))
ECOSYSTEM_MD = REPO_ROOT / "ecosystem.md"

# Database files
APPROVED_DB = DATA_DIR / "approved_repos.json"
PENDING_DB = DATA_DIR / "pending_review.json"
REJECTED_DB = DATA_DIR / "rejected_repos.json"
CONTRIBUTORS_DB = DATA_DIR / "contributors.json"
REVIEW_LOG = DATA_DIR / "review_log.json"

# ── Search Queries ──────────────────────────────────────────
SEARCH_QUERIES = [
    # Core hermes repos
    ("hermes-agent+in:name,description+sort:updated", "core"),
    ("hermes+mcp+in:name,description+sort:updated", "mcp"),
    ("hermes+skill+plugin+in:name,description+sort:updated", "skills"),
    ("hermes-agent+fork:true+sort:updated", "forks"),
    ("hermes+integration+connector+sort:updated", "integrations"),
    ("hermes+ui+dashboard+desktop+web+sort:updated", "ui"),
    ("hermes+deployment+docker+production+sort:updated", "deployment"),
    ("hermes+memory+knowledge+brain+sort:updated", "memory"),
    ("hermes+benchmark+evaluation+sort:updated", "benchmarks"),
    ("hermes+research+paper+sort:updated", "research"),
    ("hermes+tutorial+guide+example+sort:updated", "tutorials"),
    ("hermes+sdk+library+client+sort:updated", "sdks"),
    ("hermes+autonomous+agent+production+sort:updated", "production"),
    ("hermes+video+content+social+sort:updated", "content"),
    ("hermes+discord+telegram+slack+whatsapp+sort:updated", "messaging"),
    ("nousresearch+hermes+sort:updated", "official"),
    ("openclaw+hermes+migration+sort:updated", "migration"),
    ("hermes+security+governance+sort:updated", "security"),
    ("hermes+api+rest+graphql+sort:updated", "apis"),
    ("hermes+example+demo+starter+sort:updated", "examples"),
]

# ── Scoring Criteria ────────────────────────────────────────
def score_repo(repo):
    """Score a repo 0-100 based on relevance, quality, activity, docs, adoption, uniqueness."""
    score = 0
    reasons = []

    # 1. Relevance (0-30): Name/description/topics match
    desc = repo.get("description") or ""
    name_lower = (repo.get("name", "") + " " + desc).lower()
    topics = [t.lower() for t in repo.get("topics", [])]

    hermes_keywords = ["hermes", "hermes-agent", "hermes agent", "nousresearch"]
    if any(k in name_lower for k in hermes_keywords):
        if "hermes-agent" in name_lower or "hermes agent" in name_lower:
            score += 25
            reasons.append("direct_hermes_reference")
        elif "hermes" in name_lower:
            score += 18
            reasons.append("hermes_mention")
    elif any(k in " ".join(topics) for k in ["hermes-agent", "hermes"]):
        score += 12
        reasons.append("hermes_topic")

    # Additional relevance signals
    if any(t in topics for t in ["mcp", "agent", "ai-agent", "autonomous-agent"]):
        score += 5
        reasons.append("agent_ecosystem")

    # 2. Quality (0-20): Stars + description quality
    stars = repo.get("stargazers_count", 0)
    if stars > 1000:
        score += 15
        reasons.append("high_stars_1000+")
    elif stars > 100:
        score += 10
        reasons.append("moderate_stars_100+")
    elif stars > 10:
        score += 5
        reasons.append("some_stars_10+")
    else:
        score += 2

    desc = repo.get("description") or ""
    if len(desc) > 80:
        score += 5
        reasons.append("detailed_description")

    # 3. Activity (0-15): Recently updated
    updated = repo.get("updated_at", "")
    if updated:
        try:
            updated_date = datetime.fromisoformat(updated.replace("Z", "+00:00"))
            days_ago = (datetime.now(timezone.utc) - updated_date).days
            if days_ago < 7:
                score += 15
                reasons.append("active_week")
            elif days_ago < 30:
                score += 10
                reasons.append("active_month")
            elif days_ago < 90:
                score += 5
                reasons.append("active_quarter")
            else:
                score += 1
                reasons.append("stale")
        except:
            score += 3

    # 4. Documentation (0-15): Has readme, wiki, homepage
    if repo.get("has_wiki", False):
        score += 3
    if repo.get("homepage"):
        score += 5
        reasons.append("has_homepage")
    if repo.get("has_issues", False):
        score += 2
    # Topic richness as proxy for documentation
    if len(topics) > 10:
        score += 3
    elif len(topics) > 5:
        score += 2

    # 5. Adoption (0-15): Forks + watchers
    forks = repo.get("forks_count", 0)
    if forks > 50:
        score += 10
    elif forks > 10:
        score += 7
    elif forks > 1:
        score += 4

    watchers = repo.get("watchers_count", 0)
    if watchers > 50:
        score += 5
    elif watchers > 10:
        score += 3

    # 6. Uniqueness (0-5): Bonus for niche/specialized
    if any(t in topics for t in ["benchmark", "evaluation", "research", "security", "operator"]):
        score += 5
        reasons.append("niche_specialized")

    return min(score, 100), reasons


def score_to_tier(score):
    """Convert score to tier."""
    if score >= 70:
        return "AUTO_APPROVE", "gold"
    elif score >= 50:
        return "HIGH_PRIORITY", "green"
    elif score >= 30:
        return "REVIEW", "yellow"
    else:
        return "LOW_PRIORITY", "gray"


# ── Database Operations ─────────────────────────────────────
def load_db(path):
    """Load a JSON database file."""
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return []


def save_db(path, data):
    """Save data to a JSON database file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)


def is_duplicate(repo_full_name, approved, pending, rejected):
    """Check if repo already exists in any database."""
    all_names = set()
    for db in [approved, pending, rejected]:
        for r in db:
            all_names.add(r.get("name", "").lower())
    return repo_full_name.lower() in all_names


def find_near_duplicates(repo, approved):
    """Find repos with similar names/descriptions."""
    name = repo.get("name", "").lower()
    desc = (repo.get("description") or "").lower()
    near = []
    for r in approved:
        r_name = r.get("name", "").lower()
        r_desc = (r.get("description") or "").lower()
        # Check name similarity (simple substring)
        if name in r_name or r_name in name:
            near.append(r.get("name"))
        # Check description overlap
        elif desc and r_desc:
            common = set(desc.split()) & set(r_desc.split())
            if len(common) > 5:
                near.append(r.get("name"))
    return near


# ── Discovery Engine ────────────────────────────────────────
def discover_repos(token, dry_run=False):
    """Main discovery function: search GitHub, score, categorize."""
    print(f"🔍 Hermes Ecosystem Discovery — {datetime.now(AZ_TZ).strftime('%Y-%m-%d %H:%M %Z')}")
    print(f"{'='*60}")

    # Load databases
    approved = load_db(APPROVED_DB)
    pending = load_db(PENDING_DB)
    rejected = load_db(REJECTED_DB)
    review_log = load_db(REVIEW_LOG)

    print(f"📊 Loaded: {len(approved)} approved, {len(pending)} pending, {len(rejected)} rejected")

    new_finds = []
    all_seen = set()

    for query, category in SEARCH_QUERIES:
        url = f"https://api.github.com/search/repositories?q={query}&per_page=10"
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "CorpusIQ-Hermes-Discovery/1.0"
        }
        if token and token != "UNAUTHENTICATED":
            headers["Authorization"] = f"token {token}"
        req = urllib.request.Request(url, headers=headers)

        try:
            data = json.loads(urllib.request.urlopen(req).read())
            items = data.get("items", [])
            print(f"\n📡 {category:15s} → {len(items)} results")

            for repo in items:
                full_name = repo["full_name"]
                if full_name in all_seen:
                    continue
                all_seen.add(full_name)

                if is_duplicate(full_name, approved, pending, rejected):
                    continue

                score, reasons = score_repo(repo)
                tier, color = score_to_tier(score)
                near = find_near_duplicates(repo, approved)

                entry = {
                    "name": full_name,
                    "url": repo["html_url"],
                    "description": repo.get("description", ""),
                    "stars": repo.get("stargazers_count", 0),
                    "forks": repo.get("forks_count", 0),
                    "language": repo.get("language", ""),
                    "topics": repo.get("topics", []),
                    "updated_at": repo.get("updated_at", ""),
                    "category": category,
                    "score": score,
                    "tier": tier,
                    "score_reasons": reasons,
                    "near_duplicates": near,
                    "discovered_at": datetime.now(timezone.utc).isoformat(),
                    "status": "pending"
                }

                new_finds.append(entry)

                if tier == "AUTO_APPROVE" and not dry_run:
                    desc_text = (repo.get('description') or '')[:60]
                    print(f"  ✅ AUTO: {full_name} (score: {score}) — {desc_text}")
                elif tier == "HIGH_PRIORITY":
                    desc_text = (repo.get('description') or '')[:60]
                    print(f"  📌 HIGH: {full_name} (score: {score}) — {desc_text}")
                else:
                    print(f"  📋 {tier}: {full_name} (score: {score})")

                time.sleep(3.0 if token == "UNAUTHENTICATED" else 2.0)  # 3.0s unauthenticated (safe under 10/min), 2.0s auth (safe under 30/min)

        except Exception as e:
            print(f"  ❌ Search failed: {e}")

    # Process findings
    auto_approved = [r for r in new_finds if r["tier"] == "AUTO_APPROVE"]
    needs_review = [r for r in new_finds if r["tier"] != "AUTO_APPROVE"]

    print(f"\n{'='*60}")
    print(f"📊 Summary: {len(new_finds)} new repos found")
    print(f"   ✅ Auto-approved: {len(auto_approved)} (score >= 70)")
    print(f"   📋 Needs review: {len(needs_review)}")

    if dry_run:
        print("\n⚠️  DRY RUN — no changes made")
        return new_finds

    # Update databases
    for entry in auto_approved:
        entry["status"] = "approved"
        entry["approved_at"] = datetime.now(timezone.utc).isoformat()
        approved.append(entry)

    for entry in needs_review:
        pending.append(entry)

    # Add to review log
    for entry in new_finds:
        review_log.append({
            "repo": entry["name"],
            "score": entry["score"],
            "tier": entry["tier"],
            "action": "auto_approved" if entry["tier"] == "AUTO_APPROVE" else "pending_review",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })

    # Save
    save_db(APPROVED_DB, approved)
    save_db(PENDING_DB, pending)
    save_db(REVIEW_LOG, review_log)

    print(f"\n💾 Saved: {len(approved)} approved, {len(pending)} pending, {len(review_log)} log entries")

    # Auto-update ecosystem.md with new approved repos
    if auto_approved:
        print(f"\n📝 {len(auto_approved)} new repos ready for ecosystem.md integration")
        # Write a report file for the agent to use when updating ecosystem.md
        report = {
            "run_time": datetime.now(timezone.utc).isoformat(),
            "new_approved": auto_approved,
            "stats": {
                "total_found": len(new_finds),
                "auto_approved": len(auto_approved),
                "pending_review": len(needs_review),
                "total_approved": len(approved),
                "total_pending": len(pending),
            }
        }
        save_db(DATA_DIR / "latest_discovery_report.json", report)

    return new_finds


def score_single_repo(repo_url, token):
    """Score a single repo (for community submissions)."""
    # Extract owner/repo from URL
    parts = repo_url.replace("https://github.com/", "").strip("/").split("/")
    if len(parts) < 2:
        return {"error": "Invalid GitHub URL"}
    owner, repo_name = parts[0], parts[1]

    url = f"https://api.github.com/repos/{owner}/{repo_name}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "CorpusIQ-Hermes-Scorer/1.0"
    })

    try:
        repo = json.loads(urllib.request.urlopen(req).read())
        score, reasons = score_repo(repo)
        tier, color = score_to_tier(score)
        return {
            "name": repo["full_name"],
            "url": repo["html_url"],
            "description": repo.get("description", ""),
            "stars": repo.get("stargazers_count", 0),
            "score": score,
            "tier": tier,
            "reasons": reasons,
        }
    except Exception as e:
        return {"error": str(e)}


# ── CLI ─────────────────────────────────────────────────────
if __name__ == "__main__":
    token = open(TOKEN_PATH).read().strip()

    if len(sys.argv) > 1 and sys.argv[1] == "--no-auth":
        discover_repos("UNAUTHENTICATED")
    elif len(sys.argv) > 1 and sys.argv[1] == "--dry-run":
        discover_repos(token, dry_run=True)
    elif len(sys.argv) > 2 and sys.argv[1] == "--score-only":
        result = score_single_repo(sys.argv[2], token)
        print(json.dumps(result, indent=2))
    else:
        discover_repos(token)
