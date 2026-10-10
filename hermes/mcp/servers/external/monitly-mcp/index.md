---
title: "Monitly MCP - Official Statistics for Your Agent"
description: "Eurostat, World Bank, OECD and IMF statistics as tools: search 100,000+ datasets, read series, track watchlists and alerts."
category: Data & Analytics
stars: n/a (new listing)
added: 2026-10-09
source: "chatmcp/mcpso issues (October 9, 2026 evening sweep)"
relevance: ★★
tags: [official-statistics, economic-data, eurostat, world-bank, oecd, imf, api-key, remote-mcp]
---

# Monitly MCP

**Official statistics for agents** - search and read 100,000+ datasets from Eurostat, the World Bank, the OECD, the IMF and national statistical offices, with watchlists and alerts on the same account. A keyless public server covers clients that cannot send a key.

```
Server type: Remote (Streamable HTTP at https://monit.ly/api/mcp; keyless public variant at /api/mcp/public)
Auth: MCP key (mcpk_..., Bearer or X-API-Key header); public and topic servers need no key
Tools: 5 data tools (search_catalog, its search_datasets alias, inspect_dataset, get_dataset, get_series) plus 16 account tools (watchlist, alerts, keys, plan, usage)
Sources: Eurostat, World Bank, OECD, IMF and national statistical offices
Pricing: Essential (free) - 10 MCP queries a month, 5 watchlist datasets; Pro - 500 queries a month, 100 datasets
Category: Data & Analytics
Built by: Monitly (monit.ly; docs at monit.ly/mcp-docs)
```

## Why This Matters for Operators

Market context usually comes from somewhere else: a statistics office page, a search result, a number someone half-remembers from a deck. Monitly makes those numbers callable - **the agent searches the catalog, reads the series and cites the source** - so "how big is this market" or "what has inflation done in Poland" is answered from Eurostat or the OECD rather than from memory.

The search-first design matters: `search_catalog` returns compact dataset cards (id, code, source, period range, geographies), and only then does the agent read the series. That keeps every analysis one hop away from its source.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `search_catalog` | Hybrid search over the catalog (name/code and embeddings), with optional country and source filters; returns dataset cards, not values |
| `search_datasets` | Alias of search_catalog for clients that prefer the name |
| `inspect_dataset` | Peeks one dataset by id: default slice, whether a country is covered, dataId and the latest values |
| `get_dataset` | Reads one dataset's metadata row including dimensions, default view and geographies |
| `get_series` | Reads the actual time series values |
| Account tools | Watchlist, alerts, MCP key management and usage/plan reads (16 tools, unmetered) |

## Installation

```bash
claude mcp add --transport http monitly https://monit.ly/api/mcp --header "Authorization: Bearer mcpk_YOUR_KEY"
```

Create the key in Settings, then Integrations, then MCP; it is shown once. For clients without header support, connect the keyless read-only server at `https://monit.ly/api/mcp/public`, or a topic server (`/economy`, `/labour`, `/health`).

## Configuration and Safety

- Data tools are metered (one unit per successful call); account tools, initialize, tools/list and ping are never metered.
- Keys are stored as SHA-256 hashes and can be revoked at any time; `mcpk_` MCP keys are separate from the REST keys.
- Read-only data surface: search, inspect and read; nothing writes to the underlying sources.
- Public and topic servers are read-only and rate-limited by fair use.

## Business Relevance

- **Founders and strategy teams** size markets and pull macro context from primary sources instead of stale decks.
- **Analysts** answer comparative questions across countries (labour, prices, trade, health) with citations.
- **Operations teams** watch key indicators with watchlists and alerts instead of manual check-ins.

## Integration with CorpusIQ

Official statistics give the backdrop; CorpusIQ gives the business. Ask Monitly for the market and macro series, then ask CorpusIQ for your own performance - revenue from Stripe, orders from Shopify, spend and conversions from your ad accounts and GA4 - and put the economy and the business side by side in one conversation, each figure source-cited.

## Limitations

- Essential (free) includes 10 MCP queries a month; real analysis needs the Pro plan (500 a month).
- Data coverage follows the underlying sources (European and international statistics), not proprietary market data.
- Account tools manage Monitly itself (watchlists, keys, plan), not third-party systems.
- Newer connector; dataset coverage continues to grow.

## FAQ

### Do I need a key to use it?

Not for the public server: `https://monit.ly/api/mcp/public` is keyless and read-only under fair use. A key unlocks the full catalog with watchlists and alerts.

### Where does the data come from?

Eurostat, the World Bank, the OECD, the IMF and national statistical offices - 100,000+ datasets, each result carrying its source.

### What does the free plan include?

10 MCP queries a month and 5 watchlist datasets; Pro lifts that to 500 queries and 100 datasets, with usage visible via `get_usage`.

## See Also

- [WaitingForPower MCP - US Energy Permitting Tracker](/hermes/mcp/servers/external/waitingforpower-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
