---
title: github-code-review — Setup Guide
description: Automate GitHub PR reviews, diffs, and inline comments via gh CLI or REST API for Hermes agents — 281 installs.
---

# github-code-review — Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent)
**Skill:** `github-code-review`
**Installs:** 281

The `github-code-review` skill automates pull request review workflows for Hermes agents. Review diffs, add inline comments, approve or request changes, and manage the review lifecycle — all from the terminal via `gh` CLI or GitHub REST API.

## Installation

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill github-code-review
```

After install, reload skills:
- Hermes CLI: `/reload-skills` or restart session
- Hermes gateway: `/restart` or `hermes gateway restart`

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.16.0+ |
| GitHub CLI | `gh auth login` completed |
| Git | `git` installed and configured |
| Repo access | Write access to target repository |

## Capabilities

| Capability | Trigger | Output |
|-----------|---------|--------|
| Review PR diff | "Review PR #42 on corpusiq-docs" | Structured code review |
| Inline comments | "Comment on line 47 of the PR diff" | Inline review comment |
| Approve/request changes | "Approve PR #42" | Review decision |
| Multi-file review | "Review all changes in PR #42" | Per-file review with suggestions |
| Stale review detection | "Check for un-reviewed PRs" | List of pending reviews |
| Review summary | "Summarize the changes in PR #42" | High-level change overview |

## CLI/Command Reference

```bash
# View PR diff
gh pr diff 42

# View PR details
gh pr view 42 --json title,body,author,additions,deletions,files

# Approve PR
gh pr review 42 --approve --body "LGTM"

# Request changes
gh pr review 42 --request-changes --body "Needs tests"

# Add inline comment
gh api repos/CorpusIQ/corpusiq-docs/pulls/42/comments \
  -f body="Consider using async here" \
  -f commit_id=HEAD \
  -f path="src/main.py" \
  -f line=47

# List open PRs
gh pr list --state open --limit 10
```

## Review Checklist (Automated)

The skill can automatically check for:
- Missing tests for new functionality
- Hardcoded credentials or secrets
- Type safety (TypeScript/Python type hints)
- Breaking API changes
- Performance regressions (N+1 queries, etc.)
- Documentation updates for changed behavior
- Security vulnerabilities (injection, XSS, etc.)

## CorpusIQ Use Cases

1. **corpusiq-docs PR review** — Automated review of community PRs
2. **Internal code review** — First-pass review for CorpusIQ engineering PRs
3. **Dependency updates** — Automated review of Dependabot/Renovate PRs
4. **Open source contributions** — Review Hermes ecosystem PRs
5. **Release validation** — Pre-release diff audit for changelog generation

## Troubleshooting

| Issue | Likely Cause | Resolution |
|-------|-------------|------------|
| gh auth fails | Token expired | `gh auth refresh -h github.com` |
| 403 on inline comment | No write access to repo | Fork and PR from fork |
| Diff too large | PR too many files | Review files individually |
| Review already submitted | Duplicate review | Use `gh pr review` update |

## Verification

After installation, verify the skill is loaded:
```bash
hermes skills list | grep github-code-review
```

Test with a review request:
```
"Review all open PRs on corpusiq-docs and summarize the changes"
```
