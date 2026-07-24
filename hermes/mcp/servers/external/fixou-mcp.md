---
name: "Fixou MCP"
description: "Create and track quote requests to local French tradespeople — 80 trades, remote MCP"
category: "Other"
source: "mcpservers.org"
discovered: "2026-07-23"
verified: true
remote_endpoint: "https://mcp.fixou.fr/mcp"
---

# Fixou MCP — French Tradespeople Quote Requests

Fixou provides MCP access to its platform for creating and tracking quote requests to local French tradespeople across 80 different trades. Remote MCP server at mcp.fixou.fr/mcp, no authentication required.

## What It Does

- **Quote requests** — Create requests for quotes from local French tradespeople
- **80 trade categories** — Covers construction, renovation, plumbing, electrical, roofing, and more
- **Tracking** — Monitor status of submitted quote requests
- **Open access** — No authentication required for the MCP endpoint

## Quick Start

```bash
# Remote endpoint — no auth needed
hermes mcp add fixou --url https://mcp.fixou.fr/mcp

# Or Claude Code
claude mcp add fixou --url https://mcp.fixou.fr/mcp
```

**Prerequisites:** None. Open endpoint.

## Key Tools

| Tool | Description |
|------|-------------|
| `search_trades` | Browse available trade categories (80+ types) |
| `create_quote_request` | Submit a new quote request with project details |
| `track_request` | Check status of a submitted quote request |
| `find_tradespeople` | Search for tradespeople by location and trade |
| `list_regions` | List supported French regions |

## Use Cases

- **Property management** — Automate quote requests for maintenance and renovation projects
- **Construction coordination** — Agents manage multi-trade project quoting
- **Cost estimation** — Gather quotes across trades for project budgeting
- **French market entry** — Research local service provider availability and pricing

---

*Discovered via [mcpservers.org](https://mcpservers.org) sweep. Listed in the [CorpusIQ MCP Catalog](https://corpusiq-docs/hermes/mcp/).*
