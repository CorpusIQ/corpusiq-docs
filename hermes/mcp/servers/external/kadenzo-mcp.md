---
title: "Kadenzo MCP — Agent-Native Social Media Scheduling and Management"
description: "Kadenzo MCP server lets any MCP-compatible agent schedule, manage, generate, and analyze social media content. Full content pipeline from creation to publishing to analytics."
category: mcp
tags: [mcp-server, social-media, scheduling, content-management, marketing]
last_updated: 2026-07-19
---

# Kadenzo MCP Server — Agent-Native Social Media

Kadenzo MCP lets any AI agent (Claude Desktop, Cursor, ChatGPT, Hermes) schedule, manage, generate, and analyze social media content. It's the first social media management platform purpose-built for agent-driven workflows rather than human dashboards.

**Source:** awesome-mcp-servers PR #9048 (discovered July 19, 2026)
**Category:** Social Media / Marketing
**Author:** Kadenzo
**Repo:** https://github.com/Kadenzo/kadenzo-mcp
**Status:** Active

## Why This Matters

Social media management tools (Postiz, Buffer, Hootsuite) are built for humans clicking buttons. Kadenzo flips the model — the agent is the operator and the tool exposes its full capabilities through MCP. For teams already using AI agents for content creation, Kadenzo eliminates the "copy-paste from agent to scheduler" step.

## Installation

```bash
# Via npm
npm install -g kadenzo-mcp

# Or run directly
npx kadenzo-mcp
```

## Claude Desktop / Hermes Configuration

```json
{
  "mcpServers": {
    "kadenzo": {
      "command": "npx",
      "args": ["kadenzo-mcp"],
      "env": {
        "KADENZO_API_KEY": "your-api-key"
      }
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `schedule_post` | Schedule content to one or more platforms at a specific time |
| `generate_content` | AI-assisted content generation with brand voice parameters |
| `list_scheduled` | View upcoming posts across all connected platforms |
| `get_analytics` | Retrieve post performance metrics |
| `manage_accounts` | Connect and manage social media accounts |

## Authentication

Requires a Kadenzo API key. Sign up at [Kadenzo](https://github.com/Kadenzo/kadenzo-mcp).

## CorpusIQ Relevance

Kadenzo competes in the same space as Postiz (CorpusIQ's current social scheduler) but with an MCP-native architecture. Worth monitoring closely — if agent-native social scheduling becomes the standard, CorpusIQ's Postiz integration should evolve to match. The `generate_content` tool with brand voice parameters is especially interesting for CorpusIQ's multi-avatar content strategy.

## See Also

- [[sweeps/sweep-july19-2026]]
