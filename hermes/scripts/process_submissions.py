#!/usr/bin/env python3
"""
Community Submission Processor
Processes GitHub issues tagged 'submission' — scores, reviews, approves/rejects.

Usage:
    python3 process_submissions.py              # Process all open submission issues
    python3 process_submissions.py --issue 12   # Process a specific issue
"""
import json
import re
import os
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path("/tmp/corpusiq-docs/hermes")
DATA_DIR = REPO_ROOT / "data"
TOKEN_PATH = Path("/home/hermes/.hermes/profiles/corpusiq/secrets/github.token")

APPROVED_DB = DATA_DIR / "approved_repos.json"
PENDING_DB = DATA_DIR / "pending_review.json"
REJECTED_DB = DATA_DIR / "rejected_repos.json"
CONTRIBUTORS_DB = DATA_DIR / "contributors.json"
REVIEW_LOG = DATA_DIR / "review_log.json"


def load_db(path):
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return []


def save_db(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)


def parse_issue_body(body):
    """Parse GitHub issue body to extract submission fields."""
    fields = {}

    # Extract URL
    url_match = re.search(r'(https://github\.com/[\w.-]+/[\w.-]+)', body)
    if url_match:
        fields["repo_url"] = url_match.group(1)

    # Extract from markdown headers
    patterns = {
        "category": r'### Category\s*\n\s*(.+)',
        "description": r'### Description\s*\n\s*(.+?)(?:\n###|\n\n|$)',
        "capabilities": r'### Key Capabilities\s*\n\s*(.+?)(?:\n###|\n\n|$)',
        "maintainer": r'### Maintainer.*\s*\n\s*(.+)',
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, body, re.DOTALL)
        if match:
            fields[key] = match.group(1).strip()

    # Also try the form labels
    label_patterns = {
        "repo_url": r'### Repository URL\s*\n\s*(.+)',
        "category": r'### Category\s*\n\s*(.+)',
    }
    for key, pattern in label_patterns.items():
        if key not in fields:
            match = re.search(pattern, body, re.DOTALL)
            if match:
                fields[key] = match.group(1).strip()

    return fields


def score_submission(repo_url, submitter, category_hint=""):
    """Score a community-submitted repo."""
    import urllib.request

    token = open(TOKEN_PATH).read().strip()
    parts = repo_url.replace("https://github.com/", "").strip("/").split("/")
    if len(parts) < 2:
        return {"error": "Invalid GitHub URL", "rejection_reason": "INVALID_URL"}

    owner, repo_name = parts[0], parts[1]

    # Check if already exists
    approved = load_db(APPROVED_DB)
    rejected = load_db(REJECTED_DB)
    pending = load_db(PENDING_DB)

    all_names = set()
    for db in [approved, rejected, pending]:
        for r in db:
            all_names.add(r.get("name", "").lower())

    full_name = f"{owner}/{repo_name}"
    if full_name.lower() in all_names:
        return {"error": "Already exists", "rejection_reason": "DUPLICATE"}

    # Fetch repo data
    url = f"https://api.github.com/repos/{owner}/{repo_name}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "CorpusIQ-Submission-Review/1.0"
    })

    try:
        repo = json.loads(urllib.request.urlopen(req).read())
    except Exception as e:
        return {"error": str(e), "rejection_reason": "FETCH_FAILED"}

    # Score using the same criteria
    from discover import score_repo, score_to_tier
    score, reasons = score_repo(repo)
    tier, color = score_to_tier(score)

    return {
        "name": full_name,
        "url": repo["html_url"],
        "description": repo.get("description", ""),
        "stars": repo.get("stargazers_count", 0),
        "forks": repo.get("forks_count", 0),
        "language": repo.get("language", ""),
        "topics": repo.get("topics", []),
        "updated_at": repo.get("updated_at", ""),
        "category": category_hint or "community_submission",
        "score": score,
        "tier": tier,
        "score_reasons": reasons,
        "submitter": submitter,
        "submitted_at": datetime.now(timezone.utc).isoformat(),
    }


def process_submission(submission_data):
    """Process a scored submission: approve, pend, or reject."""
    tier = submission_data.get("tier", "LOW_PRIORITY")
    rejection_reason = submission_data.get("rejection_reason")

    review_log = load_db(REVIEW_LOG)

    # Handle fetch failures and duplicates
    if rejection_reason:
        rejected = load_db(REJECTED_DB)
        rejected.append({
            **submission_data,
            "status": "rejected",
            "rejection_reason": rejection_reason,
            "rejected_at": datetime.now(timezone.utc).isoformat(),
        })
        save_db(REJECTED_DB, rejected)
        review_log.append({
            "repo": submission_data.get("name", "unknown"),
            "action": "rejected",
            "reason": rejection_reason,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })
        save_db(REVIEW_LOG, review_log)
        update_contributor(submission_data.get("submitter"), "rejected")
        return {"action": "rejected", "reason": rejection_reason}

    if tier == "AUTO_APPROVE":
        # Add to approved
        approved = load_db(APPROVED_DB)
        submission_data["status"] = "approved"
        submission_data["approved_at"] = datetime.now(timezone.utc).isoformat()
        approved.append(submission_data)
        save_db(APPROVED_DB, approved)
        review_log.append({
            "repo": submission_data["name"],
            "action": "approved",
            "score": submission_data["score"],
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })
        update_contributor(submission_data.get("submitter"), "approved")
        return {"action": "approved", "score": submission_data["score"]}

    elif tier == "HIGH_PRIORITY" or tier == "REVIEW":
        # Add to pending
        pending = load_db(PENDING_DB)
        submission_data["status"] = "pending"
        pending.append(submission_data)
        save_db(PENDING_DB, pending)
        review_log.append({
            "repo": submission_data["name"],
            "action": "pending_review",
            "score": submission_data["score"],
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })
        return {"action": "pending", "score": submission_data["score"]}

    else:
        # Reject low-priority
        rejected = load_db(REJECTED_DB)
        submission_data["status"] = "rejected"
        submission_data["rejection_reason"] = "LOW_PRIORITY"
        submission_data["rejected_at"] = datetime.now(timezone.utc).isoformat()
        rejected.append(submission_data)
        save_db(REJECTED_DB, rejected)
        review_log.append({
            "repo": submission_data["name"],
            "action": "rejected",
            "reason": "LOW_PRIORITY",
            "score": submission_data["score"],
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })
        update_contributor(submission_data.get("submitter"), "rejected")
        return {"action": "rejected", "reason": "LOW_PRIORITY"}

    save_db(REVIEW_LOG, review_log)


def update_contributor(github_user, action):
    """Track contributor stats."""
    if not github_user:
        return
    contributors = load_db(CONTRIBUTORS_DB)
    for c in contributors:
        if c["github_user"] == github_user:
            c["submissions"] = c.get("submissions", 0) + 1
            if action == "approved":
                c["approved"] = c.get("approved", 0) + 1
            elif action == "rejected":
                c["rejected"] = c.get("rejected", 0) + 1
            c["last_contribution"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            save_db(CONTRIBUTORS_DB, contributors)
            return
    contributors.append({
        "github_user": github_user,
        "submissions": 1,
        "approved": 1 if action == "approved" else 0,
        "rejected": 1 if action == "rejected" else 0,
        "first_contribution": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "last_contribution": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    })
    save_db(CONTRIBUTORS_DB, contributors)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 2 and sys.argv[1] == "--test":
        # Test with a sample repo
        result = score_submission(
            "https://github.com/nesquena/hermes-webui",
            "test-user",
            "UI & Dashboards"
        )
        print(json.dumps(result, indent=2))
        if "error" not in result:
            outcome = process_submission(result)
            print(f"\nOutcome: {json.dumps(outcome, indent=2)}")
    else:
        print("Submission processor ready.")
        print("Run with --test to test with a sample repo.")
        print("Connect to GitHub Issues API for full automation.")
