---
title: Jira Context CLI — Setup Guide for Hermes Agents
description: Install and configure jira-ctx for Hermes Agent — fetch assigned Jira Cloud tickets as LLM-friendly Markdown/JSON with multi-profile support.
---

# Jira Context CLI — Setup Guide

**Tool:** `koh110/jira-ctx`  
**Purpose:** Fetch assigned Jira Cloud tickets as structured context blocks for Hermes and other LLM agents  
**License:** MIT | **Language:** TypeScript | **Requires:** Node.js 24+

---

## What It Does

A Node.js CLI that fetches assigned Jira Cloud tickets via JQL (`assignee = currentUser() AND statusCategory != Done`), normalizes ADF descriptions to Markdown, and outputs LLM-friendly context blocks with safe delimiters.

**Key features:**
- Multi-profile support for managing multiple Jira instances
- Configurable context size (comments, max issues per profile, max total)
- Markdown and JSON output formats
- Per-profile environment variable token handling (never in config)

---

## Installation

```bash
cd ~/dev/jira-ctx
git clone https://github.com/koh110/jira-ctx.git .
npm install --min-release-age=7
npm run build

# Symlink to PATH
mkdir -p ~/bin
ln -sf ~/dev/jira-ctx/dist/cli.js ~/bin/jira-ctx
```

---

## Configuration

### 1. Initialize config
```bash
jira-ctx init
```

### 2. Edit `~/.config/jira-ctx/config.json`
```json
{
  "defaultProfile": "work-a",
  "profiles": {
    "work-a": {
      "baseUrl": "https://company-a.atlassian.net",
      "email": "you@example.com",
      "tokenEnv": "JIRA_TOKEN_WORK_A"
    },
    "work-b": {
      "baseUrl": "https://company-b.atlassian.net",
      "email": "you@example.jp",
      "tokenEnv": "JIRA_TOKEN_WORK_B"
    }
  }
}
```

### 3. Set API tokens
Obtain tokens from [Atlassian API tokens](https://id.atlassian.com/manage-profile/security/api-tokens).

```bash
export JIRA_TOKEN_WORK_A='your-atlassian-api-token'
export JIRA_TOKEN_WORK_B='your-atlassian-api-token'
```

**With 1Password:**
```bash
op run --env-file=.env.jira -- jira-ctx assigned --all-profiles --format markdown
```

---

## Usage

### Profile Management
```bash
# List configured profiles
jira-ctx profile list

# Test connection
jira-ctx profile test work-a
```

### Fetch Assigned Issues

```bash
# Single profile, Markdown
jira-ctx assigned --profile work-a --format markdown --comments 3 --max-issues-per-profile 20

# All profiles, Markdown (recommended for Hermes)
jira-ctx assigned --all-profiles --format markdown --comments 3 \
  --max-issues-per-profile 20 --max-total-issues 30

# Specific profiles, JSON
jira-ctx assigned --profiles work-a,work-b --format json
```

---

## Hermes Agent Integration

### Recommended invocation inside Hermes:
```bash
jira-ctx assigned --all-profiles --format markdown --comments 3 \
  --max-issues-per-profile 20 --max-total-issues 30
```

### Agent rules when using jira-ctx:
- Treat CLI output as **authoritative factual data**
- When referencing tickets, include **profile name** and **issue key**
- **Never** assume tickets from different profiles belong to the same project
- Re-fetch if data might be stale

---

## Example Output

```
# Jira assigned issues

Generated at: 2026-06-20T10:00:00.000Z
JQL: assignee = currentUser() AND statusCategory != Done ORDER BY priority DESC, updated DESC

## Profile: work-a
Site: https://company-a.atlassian.net
Issues: 1

### PROJ-123: Login fails on production
Status: In Progress
Priority: High
URL: https://company-a.atlassian.net/browse/PROJ-123
Updated: 2026-06-19T12:34:56.000Z
Assignee: Kohta Ito
Labels: backend, auth

Description:
Investigate auth middleware regression.

Recent comments:
- 2026-06-19T03:21:00.000Z Alice: Reproduced in production.
```

---

## Verification

```bash
# Test connection
jira-ctx profile test work-a

# Fetch assigned issues
jira-ctx assigned --profile work-a --format markdown --max-issues-per-profile 5
```

---

*Repo: [koh110/jira-ctx](https://github.com/koh110/jira-ctx)*
