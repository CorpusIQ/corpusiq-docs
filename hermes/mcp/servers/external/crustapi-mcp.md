---
title: "CrustAPI MCP — Live Google Search for AI Agents"
description: "Live Google Search, Maps, News, Images and Reviews for AI agents. Pay only for results — no subscription."
category: mcp
tags: [mcp-server, search, google, maps, news, research]
last_updated: 2026-07-12
---

# CrustAPI MCP Server ★ New (July 12)

MCP server for CrustAPI — live Google Search, Maps, News, Images, and Reviews for AI agents. Pay-as-you-go pricing (pay only for results, no subscription). Brings real-time web intelligence into any MCP-compatible client.

**Source:** mcp.so (submitted July 12, 2026)

## What It Is

A hosted MCP server connecting AI agents to Google Search, Maps, News, Images, and Reviews via CrustAPI. Unlike web-scraping MCPs that parse HTML, CrustAPI returns structured search results optimized for agent consumption. The pay-per-result model means no monthly subscription — ideal for operators who need occasional live search without ongoing cost.

## Business Relevance

- **Research operators** can pull live web data into analysis workflows
- **Sales teams** can research prospects with real-time company/news/address data
- **Marketing operators** can monitor brand mentions and competitor activity
- **CorpusIQ complement** for businesses needing live search alongside structured business data

## Tools Available

| Tool | Description |
|------|-------------|
| `google_search` | Live Google web search with structured results |
| `google_maps` | Place search, details, reviews, and geocoding |
| `google_news` | News search by topic, source, date range |
| `google_images` | Image search with metadata |
| `google_reviews` | Business reviews and ratings |

## Quick Start

```bash
# Remote MCP server — connect via URL
# Add to MCP client config
{
  "mcpServers": {
    "crustapi": {
      "url": "https://api.crustapi.com/mcp",
      "env": {
        "CRUSTAPI_KEY": "your-api-key"
      }
    }
  }
}
```

## Business Use Cases

1. **Prospect research:** "Search for news about [company] and show me their Google Maps listing with reviews"
2. **Market intelligence:** "Find recent news articles about [industry trend] and summarize the top 5"
3. **Competitive monitoring:** "Search for [competitor name] reviews — what are customers complaining about?"
4. **Location intelligence:** "Show me all [business type] within 5 miles of [address] with ratings above 4.0"

## Limitations

- Pay-per-result pricing — costs scale with usage (budget-aware deployment needed)
- Requires CrustAPI account and API key
- Google Search results may differ from consumer Google experience
- Rate limits apply based on CrustAPI plan tier
- Third-party API (not Google official); service continuity depends on CrustAPI

## See Also

- [MentionsAPI](/hermes/mcp/servers/external/mentionsapi/) — Brand mention monitoring
- [Substack Publisher MCP](/hermes/mcp/servers/external/substack-publisher-mcp/) — Newsletter analytics
