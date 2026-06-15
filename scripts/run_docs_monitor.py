#!/usr/bin/env python3
"""
CorpusIQ Docs Repo Monitor
Checks the corpusiq-docs GitHub repo for new commits since last recorded state.
Updates docs_repo_state.json with new commit SHA and timestamp.
Outputs summary for the cron job agent to process.
"""
import json
import subprocess
import sys
import os
from datetime import datetime, timezone

STATE_FILE = os.path.expanduser("~/.hermes/profiles/corpusiq/data/docs_repo_state.json")
REPO_PATH = os.path.expanduser("~/corpusiq-docs")

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"issues": {}, "comments": {}, "prs": {}, "last_commit_sha": None, "last_commit_date": None}

def get_new_commits(repo_path, since_sha=None):
    os.chdir(repo_path)
    # Fetch latest
    subprocess.run(["git", "fetch", "origin"], capture_output=True, timeout=60)
    
    if since_sha:
        cmd = ["git", "log", f"{since_sha}..HEAD", "--format=%H|%ai|%s"]
    else:
        cmd = ["git", "log", "--format=%H|%ai|%s", "-20"]
    
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        print(f"ERROR: git log failed: {result.stderr}")
        sys.exit(1)
    
    lines = [l.strip() for l in result.stdout.strip().split("\n") if l.strip()]
    commits = []
    for line in lines:
        parts = line.split("|", 2)
        if len(parts) == 3:
            commits.append({
                "sha": parts[0],
                "date": parts[1],
                "message": parts[2]
            })
    return commits

def main():
    state = load_state()
    last_sha = state.get("last_commit_sha")
    
    commits = get_new_commits(REPO_PATH, since_sha=last_sha)
    
    if not commits:
        print("OK: No new activity on corpusiq-docs")
        return
    
    print(f"NEW: {len(commits)} new commits since last check")
    for c in commits:
        print(f"  [{c['date']}] {c['sha'][:7]} {c['message']}")
    
    # Update state
    state["last_commit_sha"] = commits[0]["sha"]
    state["last_commit_date"] = commits[0]["date"]
    state["last_check"] = datetime.now(timezone.utc).isoformat()
    
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

if __name__ == "__main__":
    main()
