---
title: "Fullstory MCP Plugin — Behavioral Analytics for AI Agents"
description: "Integration guide for fullstorydev/fullstory-skills: Query session data, user behavior, funnel metrics, and CX insights directly from Claude or Cursor. Official MCP plugin from Fullstory."
category: analytics
tags: [mcp, fullstory, behavioral-analytics, session-replay, funnel-analysis, customer-experience, product-analytics]
source: mcp.so
repo: fullstorydev/fullstory-skills
stars: 9
discovered: 2026-07-23
last_updated: 2026-07-23
---

# Fullstory MCP Plugin — Behavioral Analytics for AI Agents

**Repo:** [fullstorydev/fullstory-skills](https://github.com/fullstorydev/fullstory-skills)
**Website:** [fullstory.com/platform/mcp](https://www.fullstory.com/platform/mcp/)
**Pricing:** Beta program (requires Fullstory account)
**Category:** Analytics / Customer Experience

## Overview

Fullstory's official MCP plugin connects Claude or Cursor directly to the Fullstory behavioral analytics platform. Instead of switching between Fullstory dashboards and your AI agent, you can query session data, analyze user behavior, compute funnel metrics, and retrieve customer experience insights — all from within your AI workflow.

This is the main Fullstory platform integration — distinct from [Subtext](/hermes/mcp/servers/external/subtext-mcp/) (Fullstory's agent-native session replay tool for coding agents).

## Why Business Operators Need This

1. **Session-Level Debugging** — Ask Claude "show me sessions where users rage-clicked on the checkout page" and get real session data without opening the Fullstory dashboard.
2. **Funnel Analysis in Context** — While discussing conversion optimization with your AI agent, pull live funnel metrics directly. No screenshots, no copy-paste.
3. **Customer Experience Intelligence** — Query behavioral patterns across segments, identify friction points, and get AI-powered recommendations backed by actual user data.
4. **Operator Autonomy** — Non-technical operators can query Fullstory data through natural language without learning the Fullstory API or SQL.

## Prerequisites

- A Fullstory account enrolled in the [MCP beta program](https://www.fullstory.com/blog/fullstory-mcp/)
- Fullstory API key (generate in account settings)
- [Claude Code](https://claude.com/product/claude-code) or [Cursor](https://www.cursor.com)

## Installation

### Claude Desktop

```json
{
  "mcpServers": {
    "fullstory": {
      "command": "npx",
      "args": ["-y", "@fullstorydev/fullstory-skills"],
      "env": {
        "FULLSTORY_API_KEY": "<your-api-key>"
      }
    }
  }
}
```

### Cursor

Follow the [official Cursor setup guide](https://developer.fullstory.com/mcp/client-setup/cursor/) for workspace-level MCP configuration.

## Available Capabilities

Tools are auto-discovered once connected. Key capabilities include:

| Capability | Description |
|------------|-------------|
| Session Query | Retrieve individual session replays and metadata |
| Event Search | Search for specific user events (clicks, errors, rage clicks) |
| Funnel Analysis | Build and analyze conversion funnels |
| Segment Analysis | Query behavioral patterns by user segment |
| Metric Extraction | Pull conversion rates, error rates, engagement metrics |
| Journey Mapping | Trace complete user journeys across sessions |

## Setup

1. **Enroll in the beta:** Visit [fullstory.com/platform/mcp](https://www.fullstory.com/platform/mcp/) and request access
2. **Generate an API key:** In Fullstory Settings → API Keys → Create New Key
3. **Configure Claude Code:** Add the MCP server configuration above to `claude_desktop_config.json`
4. **Verify connection:** Ask Claude "list my Fullstory tools" — you should see session query, event search, and funnel analysis tools

## CorpusIQ Integration

CorpusIQ operators using Fullstory can combine both platforms:

- **CorpusIQ** pulls business data (Shopify revenue, Stripe payments, Google Ads spend)
- **Fullstory MCP** pulls behavioral data (session replays, rage clicks, funnel drop-offs)
- **Together:** Connect revenue impact to specific UX friction points. "Show me sessions from users who abandoned cart, cross-reference with their Shopify order history from CorpusIQ."

## Limitations

- **Beta-only:** Requires enrollment in Fullstory's MCP beta program — not generally available yet
- **API key required:** Must have a Fullstory account with API access
- **Read-only:** Query and analysis only — cannot create events or modify Fullstory configuration
- **Claude/Cursor only:** Currently supports Claude Code and Cursor; no VS Code Copilot or other agents documented yet

## See Also

- [Subtext MCP](/hermes/mcp/servers/external/subtext-mcp/) — Fullstory's agent-native session replay for coding agents
- [Fullstory Developer Docs](https://developer.fullstory.com)
- [Fullstory MCP Blog Post](https://www.fullstory.com/blog/fullstory-mcp/)
- [Google Analytics MCP](/hermes/mcp/servers/external/google-analytics-mcp/) — Alternative analytics source
