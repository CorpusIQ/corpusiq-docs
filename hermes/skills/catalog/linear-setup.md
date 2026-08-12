---
title: Linear Integration — Skill Setup Guide
description: Install and configure linear, the Hermes Agent skill for managing Linear.app issues, projects, and teams via GraphQL API — no OAuth, no MCP server — 80 installs.
---

# Linear — Issue & Project Management Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/linear) (80 installs)
**Category:** Productivity / Project Management
**License:** MIT · **Platforms:** Linux, macOS, Windows
**Dependencies:** Hermes Agent, Linear.app account, Personal API key

Manage Linear issues, projects, and teams directly from Hermes using the GraphQL API via `curl`. No MCP server, no OAuth dance, no extra dependencies — just an API key and HTTP. Create issues, query team workloads, manage sprints, and triage your backlog without leaving the terminal.

---

## What It Does

| Capability | GraphQL Operation |
|-----------|-------------------|
| **Create/update issues** | `IssueCreate`, `IssueUpdate` mutations |
| **Query team issues** | `issues` query with filters (assignee, status, project) |
| **Manage projects** | `projects` query, `ProjectUpdate` mutation |
| **Sprint/cycle management** | `cycles` query, add/remove issues from cycles |
| **Search across workspace** | `searchIssues` with full-text search |
| **Read comments** | `comments` nested under issues |

---

## Architecture

```
┌──────────┐    GraphQL (POST)     ┌──────────────────┐
│  Hermes   │─────────────────────▶│  api.linear.app  │
│  + curl   │   Auth: LINEAR_API   │                  │
└──────────┘   _KEY (no Bearer)    └──────────────────┘
```

No MCP server, no SDK, no proxy. Pure HTTP with your personal API key.

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill linear
```

### Direct from Hermes Agent Repo

```bash
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/productivity/linear ~/.hermes/skills/
```

---

## Setup

### Step 1: Get your Linear API Key

1. Go to [Linear Settings > Account > Security & access](https://linear.app/settings/account/security)
2. Scroll to **Personal API keys**
3. Click **Create new API key**
4. Copy the key (starts with `lin_api_`)

**Important:** The org-level *Settings > API* page only shows OAuth apps and workspace-member keys — not your personal key. You must use the account-level security page.

### Step 2: Configure Hermes

```bash
hermes setup
```

Add to environment:

```
LINEAR_API_KEY=lin_api_your_key_here
```

Or set in your shell:

```bash
export LINEAR_API_KEY="lin_api_..."
```

### Step 3: Verify

```
> Load linear skill
> Show me my assigned issues
```

---

## Basic Usage

### Issue management

```
> Create a Linear issue: "Fix auth token refresh" in project ENG, priority high
> Show open bugs assigned to me
> Move issue ENG-123 to "In Progress"
> What's the status of ENG-456?
```

### Team & project queries

```
> What's on my team's plate this sprint?
> Show all unassigned issues in the Backend project
> Who has the most open issues right now?
```

### Search

```
> Search Linear for "rate limiting"
> Find issues tagged "performance" created this week
```

---

## API Details

| Detail | Value |
|--------|-------|
| **Endpoint** | `https://api.linear.app/graphql` |
| **Method** | POST |
| **Auth Header** | `Authorization: $LINEAR_API_KEY` (no "Bearer" prefix) |
| **Content-Type** | `application/json` |
| **ID format** | Both UUIDs and short IDs (`ENG-123`) work |

---

## Tips

- **Short IDs work everywhere:** Use `ENG-123` instead of full UUIDs — Linear resolves them automatically
- **Batch queries:** GraphQL lets you fetch issues + comments + project in one request
- **Rate limits:** Linear has generous limits (1,000+ requests/minute) — no special handling needed
- **Team awareness:** `team { id, name }` is available on issues for cross-team queries

---

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| 401 Unauthorized | Wrong key or "Bearer" prefix | Remove "Bearer" — Linear API keys don't use it |
| "No team found" | Key scoped to wrong workspace | Verify key is from the correct Linear account |
| Empty results | Query filter too strict | Broaden filters or remove status constraint |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [nousresearch/hermes-agent on skills.sh](https://skills.sh/nousresearch/hermes-agent)*

*Powered by CorpusIQ*
