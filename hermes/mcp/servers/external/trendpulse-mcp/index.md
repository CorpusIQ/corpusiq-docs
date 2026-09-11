---
title: "TrendPulse MCP - Google News and Trends Research"
description: "Community MIT MCP server that combines Google News discovery and article extraction with Google Trends analysis: trending terms by market, interest-over-time, growth windows, related queries and regional breakdowns for keyword, market and content decisions. Sixteen tools, Python, self-hosted."
category: Content
stars: n/a (new listing)
added: 2026-09-11
source: mcpservers.org /all via r.jina.ai
relevance: ★★
tags: [google-trends, google-news, keyword-research, market-demand, content-research, trends, self-hosted]
---

# TrendPulse MCP

**Self-hosted MCP server (Python 3.10+, stdio)** - research current news and search-interest trends from one MCP. Sixteen tools split across Google News discovery with article extraction and Google Trends analysis with growth windows and regional breakdowns, so an agent can evidence-check a keyword, market or content bet before committing.

```
Server type: Self-hosted (Python 3.10+, stdio)
Install: uvx mcp-trendpulse (PyPI) or pip from a checkout
Auth: None (community server)
Tools: 16 (6 news, 10 trends)
Category: Content
Built by: AKzar1el (DigestSEO ecosystem)
```

## Tools

| Group | Tools | Purpose |
|---|---|---|
| News research | get_news_by_keyword, get_news_by_location, get_news_by_topic, get_top_news, get_news_by_site, get_article_content | Search Google News, retrieve top stories, resolve and extract article content (Playwright fallback, optional sampling summary) |
| Trend research | get_trending_terms, get_trends, get_growth, get_ranked_trends, get_top_trends, get_interest_by_region, get_related_queries, get_related_topics, get_suggestions, get_categories | Trending terms by market, interest-over-time, growth over custom windows, ranked trends, regional interest, related queries and topics, category IDs |

## Connection

1. `uvx mcp-trendpulse` from Claude Desktop, VS Code, Cursor or Kiro - no keys, no signup (MIT, Python 3.10+).
2. Ask for evidence: "compare search interest for ergonomic chair vs standing desk in the US over the last 12 months" or "what is trending in Germany this week".
3. The hosted TrendPulse by DigestSEO surface (ChatGPT/Codex) is in development and should not be treated as available.

## Verification (Sep 11, 2026 night sweep)

Not live-probed (self-hosted package, no public endpoint). The README on repo AKzar1el/mcp-trendpulse documents all 16 tool schemas, per-client configuration blocks and the browser-fallback article path; the glama score badge and MIT license are on the listing. The hosted remote layer is explicitly unreleased.

## See Also

- [YoTrends MCP - Live YouTube and TikTok Trends as Content Packs](/hermes/mcp/servers/external/yotrends-mcp/)
- [Encited MCP - SEO and AI Visibility for Agents](/hermes/mcp/servers/external/encited-mcp/)
