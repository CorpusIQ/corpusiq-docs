---
title: "Astucia Wiki MCP — AI-Enabled Team Wiki for Hermes Agent"
description: "Connect Astucia Wiki to Hermes Agent. AI-native team wiki with semantic search, auto-organization, and natural language querying. For operators who need a single source of truth their AI can actually use."
category: mcp
tags: [mcp-server, wiki, knowledge-management, documentation, team-collaboration, productivity]
last_updated: 2026-07-04
---

# Astucia Wiki MCP Server ★ New (July 4)

## Overview

Astucia Wiki (`astucia-wiki-mcp`) is an AI-enabled team wiki that connects to MCP-compatible AI agents. Unlike traditional wikis where knowledge rots in unsearchable pages, Astucia is built from the ground up for AI access — semantic search, auto-tagging, and natural language queries work out of the box. Your agent can read, write, and organize wiki content as naturally as a team member.

**Key advantage**: Finally, a wiki your AI agent can actually use. No more "our wiki has the answer but the agent can't find it" — Astucia exposes its entire knowledge graph over MCP.

## Key Features

- **Semantic search**: Natural language queries surface relevant pages, not just keyword matches
- **Auto-organization**: AI automatically tags, links, and structures content as it's added
- **Agent-first editing**: Create, update, and organize pages via MCP tools
- **Knowledge graph**: Pages are connected via AI-identified relationships — not manual linking
- **Version history**: Track changes with AI-generated summaries of what changed and why
- **Access control**: Team-based permissions with read/write/admin levels

## Installation

```bash
# Add to Hermes (hosted endpoint)
hermes mcp add astucia --url https://astucia.wiki/api/mcp
```

## Configuration

1. Create an Astucia Wiki workspace at [astucia.wiki](https://astucia.wiki)
2. Generate an API key from your workspace settings
3. Add the endpoint to your MCP configuration with your API key

## Tools

| Tool | Description |
|------|-------------|
| `search_pages` | Semantic search across all wiki pages |
| `get_page` | Retrieve a page with full content and metadata |
| `create_page` | Create a new wiki page with auto-tagging |
| `update_page` | Update an existing page's content |
| `list_recent` | List recently created/updated pages |
| `get_knowledge_graph` | View AI-identified relationships between pages |

## Use Cases for Operators

- **Company playbook**: Maintain your operating manual, onboarding guides, and SOPs in a wiki your AI agent can actually query and update
- **Decision log**: Every major decision gets a wiki page. Agents can search "what was the reasoning behind choosing Postgres over MySQL in Q2" and get the actual decision context
- **Project handoffs**: When team members rotate, the wiki preserves context in a format agents can parse and summarize
- **Customer knowledge base**: Internal wiki + agent access = support agents that can answer nuanced questions from real company knowledge

## Why Operators Need This

Most company wikis are write-only — people add pages, nobody finds them later. Astucia Wiki MCP flips this by making the wiki a first-class data source for AI agents. Your operating knowledge becomes a queryable asset rather than a graveyard of abandoned Confluence pages.

## Comparison: Astucia vs Traditional Wikis

| | Astucia Wiki | Confluence/Notion |
|---|---|---|
| **AI access** | Native MCP, semantic search | Scraped, keyword-only |
| **Auto-organization** | AI tags and links pages | Manual tagging |
| **Agent write access** | Structured MCP tools | API hacks or browser automation |
| **Knowledge graph** | Built-in, AI-maintained | None or manual |

---

*Discovered via mcpservers.org — July 4, 2026*
*← [External MCP Catalog](/hermes/mcp/servers/external/) | [Astucia Wiki](https://astucia.wiki) →*
