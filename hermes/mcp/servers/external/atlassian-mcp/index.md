---
title: "Atlassian MCP Server"
description: "Official Atlassian MCP server for Jira, Confluence, Bitbucket, Compass, and Jira Service Management"
stars: 911
language: JavaScript
auth: "OAuth 2.1, API Token"
transport: "Remote HTTP (Streamable)"
status: "Official"
created: 2025-08-01
repository: "https://github.com/atlassian/atlassian-mcp-server"
category: "Enterprise / Project Management"
priority: "★★★"
last_updated: 2026-07-27
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/atlassian-mcp/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# Atlassian MCP Server ★★★ Official

The official remote MCP server from Atlassian. Connects AI agents (Claude, ChatGPT, Cursor, VS Code, Copilot) to the full Atlassian product suite — Jira, Confluence, Jira Service Management, Bitbucket, and Compass. 911 stars on GitHub, created August 2025.

## What It Does

Atlassian MCP gives AI agents structured access to your entire Atlassian workspace. Every tool is scoped to what the user's OAuth token or API key permits — agents see the same data the user does.

**Products covered:**
- **Jira** — Issues, projects, boards, sprints, workflows, filters
- **Confluence** — Pages, spaces, search, content trees
- **Jira Service Management** — Service desk, requests, queues
- **Bitbucket** — Repositories, pull requests, pipelines
- **Compass** — Component catalog, dependencies, scorecards

## Why It Matters for Operators

Most operators live in Jira and Confluence. An AI agent that can read your sprint board, search your wiki, and pull up related PRs without switching contexts is a productivity multiplier. The OAuth 2.1 auth model means enterprise security teams can approve it — agents only see what the user sees, and everything is auditable.

## Auth

Two modes:

1. **OAuth 2.1 (recommended)** — Standard Atlassian OAuth flow. The agent gets a scoped token tied to the user's identity. Sessions can be revoked from `admin.atlassian.com`.

2. **API Token** — Personal access token from `id.atlassian.com/manage/api-tokens`. Simpler setup, less granular scoping. Good for personal use; not recommended for team deployments.

## Transport

Remote Streamable HTTP. No local stdio server needed — the agent connects directly to Atlassian's hosted MCP endpoint.

## Setup

```json
{
  "mcpServers": {
    "atlassian": {
      "type": "url",
      "url": "https://mcp.atlassian.com/mcp",
      "headers": {
        "Authorization": "Bearer <your-oauth-or-api-token>"
      }
    }
  }
}
```

For Claude Desktop, Cursor, or VS Code — add this to your MCP config. For ChatGPT, use the built-in connector if available, or configure via the MCP gateway.

## Tools (Representative)

The server exposes the full Atlassian REST API surface. Representative tool categories:

- `jira.search` — JQL queries, issue lookups
- `jira.boards` — Board and sprint data
- `confluence.search` — Full-text wiki search
- `confluence.pages` — Page content, metadata
- `bitbucket.prs` — Pull request lists, diffs
- `compass.components` — Component catalog queries

Exact tool count depends on which products are enabled in your Atlassian instance.

## Limitations

- Requires an active Atlassian Cloud instance (not compatible with self-hosted/Data Center)
- OAuth 2.1 setup requires Atlassian admin to register an app
- API token auth is simpler but less granular — the agent inherits the user's full permissions

## Verdict

The most important enterprise MCP server we have cataloged. If your team uses Jira and Confluence, this is a must-add. The 911 stars and official Atlassian backing mean this is stable, supported, and production-ready. Combined with the CorpusIQ MCP server (40+ business data sources) and Stripe MCP (payments), this forms the core of an operator's AI toolchain.
