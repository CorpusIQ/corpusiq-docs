---
title: "Substack Publisher MCP — Content Analytics for AI Agents"
description: "Query Substack posts, engagement analytics, subscriber counts, and publications through the official Publisher API from any MCP client."
category: mcp
tags: [mcp-server, substack, content-marketing, analytics, publishing]
last_updated: 2026-07-12
---

# Substack Publisher MCP Server ★ New (July 12)

Queries Substack posts, engagement analytics, subscriber counts, and publications through the official Substack Publisher API. Gives AI agents direct access to newsletter performance data — open rates, click-through, subscriber growth, and post-level engagement.

**Source:** mcp.so (submitted July 12, 2026)

## What It Is

A community MCP server that wraps the Substack Publisher API, allowing AI agents to pull real-time content analytics directly into conversations. Operators can ask agents to analyze newsletter performance, compare post engagement, or surface subscriber trends without leaving their workflow.

## Business Relevance

- **Content operators** can monitor Substack analytics alongside other business data
- **Marketing teams** can correlate newsletter performance with revenue/sales data
- **Growth operators** can identify top-performing content and replicate winning patterns
- **Complementary to CorpusIQ** for businesses that use Substack as a primary content channel

## Tools Available

| Tool | Description |
|------|-------------|
| `get_posts` | List published posts with engagement stats |
| `get_subscribers` | Subscriber counts, growth rate, churn |
| `get_post_analytics` | Per-post opens, clicks, shares, comments |
| `get_publication_stats` | Aggregate publication metrics |

## Quick Start

```bash
# Install via npx (when available on npm/smithery)
npx @substack/mcp-server

# Or add to Claude Desktop config
{
  "mcpServers": {
    "substack-publisher": {
      "command": "npx",
      "args": ["@substack/mcp-server"],
      "env": {
        "SUBSTACK_API_KEY": "your-publisher-api-key"
      }
    }
  }
}
```

## Business Use Cases

1. **Newsletter performance review:** "Compare my last 5 posts by open rate and show which topics performed best"
2. **Content-audience correlation:** "Show subscriber growth trend vs revenue from the same period"
3. **Content calendar intelligence:** "Which day of week has highest engagement for my publication?"
4. **Churn analysis:** "Which posts had the highest unsubscribe rate — what patterns do they share?"

## Limitations

- Requires Substack Publisher API key (available to publication owners only)
- Community-maintained; verify auth scope before use
- Limited to publications where the API key owner has access
- No write capabilities (read-only analytics)

## See Also

- [CrustAPI MCP](/hermes/mcp/servers/external/crustapi-mcp/) — Live Google Search for agent research
- [Financial News MCP](/hermes/mcp/servers/external/financial-news-mcp/) — Real-time financial news data
