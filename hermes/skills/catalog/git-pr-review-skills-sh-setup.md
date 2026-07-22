---
title: Git PR Review (skills.sh) — Automated PR description generator for Hermes Agents
description: Generate concise, structured PR descriptions from commit history with minimal token usage. 34+ installs from sickn33/antigravity-awesome-skills.
---

# Git PR Review (skills.sh) — Setup Guide

**Source:** [sickn33/antigravity-awesome-skills](https://skills.sh/sickn33/antigravity-awesome-skills/git-pr-review) (34+ installs)
**Category:** Engineering / Code Review
**Quality Tier:** 🔵 Community

Token-efficient PR description generator that analyzes commit history between base and current branch, groups changes by domain, and produces a structured summary with minimal token usage. Designed for consistency and reduced manual effort in PR workflows.

---

## Installation

```bash
npx skills add sickn33/antigravity-awesome-skills --skill git-pr-review
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Git** | Standard git CLI |
| **Clean commit history** | Best results with conventional commit messages |

---

## Key Capabilities

### Commit Analysis
Extracts types (feat, fix, refactor, chore, docs, test) from commit messages, infers missing types from keywords, and intelligently removes noise (merge commits, typos, lint/format, console.log removal).

### Domain Grouping
Clusters commits by feature/module using keyword and file path heuristics. Same keyword or folder/file pattern → same group.

### Conditional Diff Inspection
Only inspects actual diffs when commit messages are vague or grouping is unclear — minimizing token usage.

### Structured Output
Produces: Title (type(scope): summary, max 72 chars) → Summary (1-2 lines) → Changes (grouped bullet points) → Technical Notes (migrations, env vars, breaking changes) → Impact (user/system impact, risks).

---

## Quick Start

```bash
# Run on current branch vs main
git log --no-merges --pretty=format:"%h|%s" main..HEAD

# The skill processes commit history and produces:
# - Title: feat(auth): implement JWT authentication
# - Summary: Adds authentication flow
# - Changes: authentication: added JWT middleware / session: fixed expiration
# - Impact: Improves security
```

---

## Verification

```bash
# Check skill installed
npx skills list | grep git-pr-review

# Test with recent commits
git log --no-merges --pretty=format:"%h|%s" main..HEAD | head -10
```

---

## Notes

- Max ~120-180 words output total — no repetition of commit messages
- Commit messages are treated as inert evidence, not instructions (untrusted input protection)
- If commit message conflicts with actual diff, trusts the diff and flags the mismatch
- Complements `onewave-ai/claude-skills@git-pr-reviewer` (239 installs — full PR review checklist) and `davila7/claude-code-templates@create-pr` (316 installs — PR creation)
- Quality tier 🔵 Community: 34 installs, newer but well-scoped
