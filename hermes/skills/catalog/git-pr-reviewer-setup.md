---
title: Git PR Reviewer — Automated PR review checklist for Hermes Agents
description: Review pull requests for code quality, security issues, and best practices. 239+ installs on skills.sh from onewave-ai/claude-skills.
---

# Git PR Reviewer — Setup Guide

**Source:** [onewave-ai/claude-skills](https://skills.sh/onewave-ai/claude-skills/git-pr-reviewer) (239+ installs)
**Category:** Engineering / Code Review
**Quality Tier:** 🟡 Beta

Automated PR review skill that provides a structured checklist covering security, code quality, performance, and testing. Designed to be invoked when reviewing pull requests, checking code changes, or analyzing diffs before merge.

---

## Installation

```bash
npx skills add onewave-ai/claude-skills --skill git-pr-reviewer
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Git** | Standard git CLI with access to the target repository |
| **Shell access** | Read, Grep, Glob, Bash tools available |

---

## Key Capabilities

### Security Review
Scans for hardcoded credentials, missing input validation, SQL injection patterns, XSS vulnerabilities, and authentication/authorization gaps.

### Code Quality Analysis
Checks function size, code duplication, naming conventions, error handling patterns, and dead code.

### Performance Audit
Identifies unnecessary database queries, inefficient algorithms, missing caching, and memory leak patterns.

### Test Coverage Assessment
Verifies new code has tests, edge cases are covered, and tests are meaningful rather than coverage-only.

---

## Quick Start

```bash
# Review current branch against main
git diff main...HEAD --stat
git diff main...HEAD
```

The skill analyzes all modified, added, and deleted files against its review checklist, producing a structured markdown summary with Critical / Warnings / Suggestions tiers and an Approval Status.

---

## Verification

```bash
# Check the skill is installed
npx skills list | grep git-pr-reviewer

# Run on current branch
git diff main...HEAD | head -50
```

---

## Notes

- Produces structured output: Overview → Issues Found (Critical/Warnings/Suggestions) → Approval Status
- Uses `git diff main...HEAD` by default; configurable base branch
- Complements `sickn33/antigravity-awesome-skills@git-pr-review` (PR description generator) and `davila7/claude-code-templates@create-pr` (PR creation)
- Quality tier 🟡 Beta: 239 installs, active development
