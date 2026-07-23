---
title: Confluence to Markdown MCP Server
subtitle: Hybrid search over locally-saved and indexed Confluence content from AI agents
source: mcpservers.org
github: https://github.com/gkoos/confluence2md-mcp
created: 2026-07-09
category: Knowledge Management
stars: 0
tags: [confluence, atlassian, documentation, search, knowledge-retrieval, enterprise]
---

# Confluence to Markdown MCP Server

MCP server for **hybrid search over locally-saved and indexed Confluence content**. Sync your Confluence spaces to local markdown files, then search everything from any AI agent — no Confluence API rate limits, offline-capable.

## What It Does

- **Confluence Sync** — Export Confluence spaces to local markdown files
- **Indexed Search** — Full-text search across all synced Confluence content
- **Hybrid Mode** — Search local index first, fall back to Confluence API for live data
- **Offline-First** — Cached content available even when Confluence is down

## Business Operator Use Cases

| Use Case | Value |
|----------|-------|
| **Knowledge Base Search** | "Find the Q2 2026 product roadmap page" → instant result from local index |
| **Cross-Space Research** | "Show me all pages mentioning 'pricing change' across all spaces" |
| **Offline Documentation** | Access Confluence docs when VPN is down or traveling |
| **AI Agent Context** | Feed Confluence knowledge into agent prompts without hitting API limits |

## Installation

```bash
git clone https://github.com/gkoos/confluence2md-mcp
cd confluence2md-mcp
pip install -r requirements.txt
```

## Configuration

Add to your MCP client config:

```json
{
  "mcpServers": {
    "confluence2md": {
      "command": "python",
      "args": ["path/to/confluence2md-mcp/server.py"],
      "env": {
        "CONFLUENCE_URL": "https://your-instance.atlassian.net/wiki",
        "CONFLUENCE_USERNAME": "your-email@company.com",
        "CONFLUENCE_API_TOKEN": "your-api-token",
        "LOCAL_INDEX_PATH": "/path/to/confluence-cache"
      }
    }
  }
}
```

## Auth

Atlassian API token authentication. Generate an API token at https://id.atlassian.com/manage-profile/security/api-tokens.

## Tools Provided

- `sync_space` — Export a Confluence space to local markdown
- `search_content` — Full-text search across synced content
- `get_page` — Retrieve a specific page by title or ID
- `refresh_index` — Update local index with recent Confluence changes
- `list_spaces` — View all synced spaces

## Limitations

- **0 stars, brand new** — Created July 9, 2026. Early development.
- **Initial sync time** — First sync of large Confluence instances can be slow (1000s of pages).
- **No real-time updates** — Content is only as fresh as your last sync.
- **Confluence license required** — You need access to a Confluence instance.
- **Not official Atlassian** — Community project, not Atlassian-supported.

## Operator Verdict

★★★ **Essential for Confluence-heavy organizations.** This solves the AI agent knowledge gap for teams that live in Confluence. The offline-first approach is smart for large instances where Confluence API rate limits are a real bottleneck. Pair with the Atlassian MCP server for live Jira+Confluence access.
