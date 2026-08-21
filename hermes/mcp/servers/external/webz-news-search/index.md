---
title: "Webz.io News Search MCP - Global News Monitoring for AI Agents"
description: "Official hosted remote MCP server from Webz.io that gives AI clients a news_search_by_webz tool for natural-language global news search with filters for domain, country, language, date window, sentiment and 17 content categories; results carry title, URL, publish date and excerpt so agents can research and cite coverage of any topic, company or market"
category: Content & Research
stars: n/a (official vendor listing)
added: 2026-08-21
source: "mcpservers.org /all (Aug 21 overnight sweep)"
relevance: ★★
tags: [news, media-monitoring, market-research, current-events, remote-mcp, sentiment, journalism, brand-monitoring]
---

# Webz.io News Search MCP

**Natural-language global news search as an official vendor MCP server.** Webz.io, an established news-data provider, runs a hosted MCP endpoint that gives any AI client a single tool: `news_search_by_webz`. The agent asks in plain language — "EU AI regulation progress" — and gets matching articles with title, URL, publish date and excerpt, filtered by domain, country, language, recency, sentiment and category.

```
Server type: Hosted remote (Streamable HTTP)
Endpoint: https://news-search-mcp.webz.io/mcp
Auth: Bearer token (free key from webz.io dashboard)
Tools: 1 (news_search_by_webz)
Built by: Webz.io (official)
Docs: docs.webz.io/docs/webz/news-search-api-mcp
```

## Why This Matters for Operators

Market research, brand monitoring and competitive tracking all reduce to the same primitive: "what has coverage said about X, recently?" Doing that from an agent normally means a scraping pipeline or a news API integration project. Webz.io's MCP server removes the plumbing — the client connects with one Bearer header and every tool call runs a regular News Search API request with the same credits and limits. The vendor also ships an Agent Skill file so the agent knows when to use the tool and how to map topics to filters, which turns the endpoint into a self-explanatory research tool rather than a bare API.

## Tools & Capabilities

| Parameter | Default | What it does |
|---|---|---|
| `query` | required | Natural-language topic or question, not keyword syntax |
| `k` | 10 | Articles to return (1-50) |
| `days` | 7 | How many days back to search (max 30) |
| `allow_all_dates` | false | Search the full coverage window instead of `days` |
| `domain` | - | Only these source domains (cnn.com, yahoo.com) |
| `exclude_domain` | - | Skip these domains; a domain cannot be in both lists |
| `language` | - | Full names: english, chinese, hebrew, french, spanish, german, arabic, russian, japanese, korean |
| `country` | - | ISO-2 uppercase codes (US, GB, DE, IL) |
| `sentiment` | - | positive, negative, neutral |
| `category` | - | One of 17 news categories from Arts through War, Conflict and Unrest |

Each result returns the article title, URL, publish date and matching text excerpt, so the agent can cite sources directly.

## Installation

```bash
claude mcp add --transport http webz-news-search https://news-search-mcp.webz.io/mcp \
  --header "Authorization: Bearer YOUR_WEBZ_TOKEN"
```

```json
{
  "mcpServers": {
    "webz-news-search": {
      "url": "https://news-search-mcp.webz.io/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_WEBZ_TOKEN"
      }
    }
  }
}
```

Get a free token by signing up at webz.io — it is the same token used for the News Search API. For Claude.ai and ChatGPT, add the endpoint as a custom connector: leave Client ID and Secret empty and paste the token on the authorize page. The endpoint returns 401 in a browser by design.

## Configuration

Set the token once as an environment variable and reference it from config: `"Authorization": "Bearer ${env:WEBZ_API_TOKEN}"`. Never commit the token to git or put it in a URL. Every tool call consumes the same credits and rate limits as the REST API, so keep `days` tight and `k` low for routine checks.

## Business Relevance

- **Marketing and PR teams** monitor brand coverage and share of voice with one agent prompt
- **Investment and strategy teams** research market developments with dated, citable sources
- **Sales teams** prep account briefs from fresh coverage of prospects and their industries
- **Agent builders** embed current-events awareness into research and summarization workflows

## Integration with CorpusIQ

Webz.io supplies the external world view — coverage, sentiment, recency — while CorpusIQ supplies the internal numbers: pair a news sweep on a competitor with CorpusIQ's Ahrefs or Semrush connectors to see whether coverage moved their organic visibility, or run GA4 and Search Console alongside to correlate press with traffic. The news excerpt feeds the narrative; CorpusIQ's connectors produce the metrics the narrative has to match.

## Limitations

- One tool, no write path, no alerts or saved searches — polling is the agent's job
- 30-day recency window unless allow_all_dates is set
- Free tier carries credits and rate limits shared with the REST API
- Sentiment and category filters depend on Webz.io's enrichment, not the raw article text

## See Also

- [tube-bridge MCP — YouTube Research and Local Semantic Corpora](/hermes/mcp/servers/external/tube-bridge-mcp/)
- [Analytics Legends MCP — SAP Analytics Intelligence](/hermes/mcp/servers/external/analytics-legends-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
