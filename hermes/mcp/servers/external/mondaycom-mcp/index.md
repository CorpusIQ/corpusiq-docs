---
title: "Monday.com MCP — Project Management for AI Agents"
description: "Connect AI agents to Monday.com via the official MCP server. Manage projects, workflows, boards, and automations through natural language."
category: mcp
tags: [mcp-server]
last_updated: 2026-07-15
---

# Monday.com MCP — Project Management for AI Agents

## What It Is

Monday.com MCP exposes Monday.com project management capabilities over the Model Context Protocol. AI agents can create and manage boards, items, columns, and automations — the first major project management platform to ship a dedicated MCP server.

## Tools Available

| Tool | Description |
|------|-------------|
| Board management | List, create, and configure boards |
| Item operations | Create, update, move, and archive items |
| Column management | Manage status, date, person, and number columns |
| Automations | Create and trigger Monday.com automations |

## Quick Start

```bash
npx -y @mondaycom/mcp
```

## Business Use Cases

1. Status reports: "What's the status of all items in the Q3 Launch board?"
2. Task triage: "Create items for each of these 5 bugs in the Engineering board"
3. Cross-team visibility: "Show me all items assigned to me across all boards due this week"

## Limitations

- Monday.com account and API key required. Respects Monday.com user permissions and rate limits.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connector Catalog](/hermes/mcp/connectors/)
