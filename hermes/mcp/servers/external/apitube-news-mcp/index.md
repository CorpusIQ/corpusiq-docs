---
title: APITube News MCP
description: News intelligence over MCP — search articles from 500,000+ sources in 60+ languages, filtered by sentiment, entities, topics and source quality. Hosted JSON-RPC endpoint with ready-made monitoring prompts.
category: Content & Media
stars: n/a (new listing)
added: 2026-08-16
source: mcpservers.org
relevance: ★★
tags: [news, media-monitoring, sentiment, entities, research, breaking-news]
---

# APITube News MCP

**Hosted news-intelligence server (JSON-RPC over HTTP, Bearer API key)** — APITube's News API becomes an MCP server at a hosted endpoint: search articles from 500,000+ sources in 60+ languages with filters for sentiment, entities, topics, media presence, and source quality. No installation, no maintenance — add the key and ask.

```
Server type: Hosted remote (JSON-RPC)
Auth: Bearer API key (Authorization header)
Endpoint: https://mcp.apitube.io/
Tools: search_news, suggest
Prompts: monitor_company, topic_sentiment, breaking_news, compare_coverage
Pricing: Commercial — apitube.io API plans
Category: Content & Media
Built by: apitube.io
```

## Why This Matters for Operators

Brand monitoring usually means a social listening subscription plus a news alerts inbox. APITube News moves the query to the assistant: "find positive news about Tesla" or "show me breaking stories about our industry from verified sources today" resolves to a structured search with entity and sentiment filtering. The shipped prompts are the operational shortcut — `monitor_company` tracks coverage and sentiment for a company, `compare_coverage` puts two subjects side by side, and `breaking_news` surfaces what is moving now.

The `suggest` tool is the quiet quality signal: it resolves names like "Tesla" to APITube entity/category/topic IDs so follow-up searches filter on canonical identifiers instead of string matching.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_news` | Search articles with filters for language, category, sentiment, entities, media, dates, and source quality |
| `suggest` | Resolve names or prefixes to entity, category, topic, and industry IDs for filtered searches |

| Prompt | Purpose |
|---|---|
| `monitor_company` | Recent news and sentiment about a company |
| `topic_sentiment` | Sentiment breakdown of coverage on a topic |
| `breaking_news` | Latest breaking stories, optionally by subject and country |
| `compare_coverage` | Volume and sentiment comparison for two subjects |

Protocol version negotiates from 2025-11-25 down to 2024-11-05, so current and older clients both connect.

## Installation

```json
{
  "mcpServers": {
    "apitube-news": {
      "url": "https://mcp.apitube.io/",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

For Claude Desktop (local process launcher), bridge with `mcp-remote` and pass the key as `--header "Authorization: Bearer YOUR_API_KEY"`. Error codes are explicit: 401 `ER0230` means an expired key, 403 `ER0603` means the key lacks MCP tool permissions.

## Business Relevance

- **Brand teams** monitor company coverage and sentiment from the assistant they already use
- **Research workflows** filter news by entity, language, and source quality instead of raw keyword spam
- **Executives** get breaking-news briefs scoped to industries and countries on demand
- **Market intel** compares coverage volume and sentiment between competitors

## Integration with CorpusIQ

APITube News is the external-signal layer next to CorpusIQ's internal-data connectors: CorpusIQ tells the operator what their own business did, APITube News tells them what the market said about it and everyone else. A weekly review could pull GA4 and Stripe numbers through CorpusIQ, then run `monitor_company` and `compare_coverage` prompts through APITube News for the narrative context around the numbers.

## Limitations

- API-key pricing sits on APITube's commercial plans — verify the tier against query volume before automating
- Sentiment is vendor-computed; treat it as signal for triage, not ground truth
- Source quality filtering is only as good as the vendor's source registry
- No write or alerting surface — research and monitoring reads only

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
