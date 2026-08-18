---
title: "CryptoStruct Market Data MCP - CorpusIQ Docs"
description: Remote MCP for historical crypto and prediction-market data — a catalog of 500K instruments across 35 venues, live market statistics, free samples, and Stripe-checkout data procurement.
category: Finance
stars: n/a (new listing)
added: 2026-08-15
source: mcp.so
relevance: ★★
tags: [crypto-market-data, prediction-markets, historical-data, market-microstructure, data-procurement, trading-research, remote-mcp]
---

# CryptoStruct Market Data MCP

**Remote MCP server (Streamable HTTP, keyless + optional OAuth)** — CryptoStruct is a first-party data platform for historical crypto and prediction-market data. Agents search a catalog of ~500K instruments across 35 venues (spot, perpetuals, futures, options, and event contracts) with day-level archive coverage back to 2021, pull live market statistics, download free samples, and procure paid tick data through a Stripe checkout URL handoff — the server never touches payment credentials.

```
Server type: Remote (Streamable HTTP)
Auth: Keyless for catalog/stats; OAuth optional for account tools
Endpoint: https://cryptostruct.com/mcp  (OAuth: /mcp/auth)
Tools: 21 in four groups (catalog, statistics, commerce, account)
Pricing: Free keyless tier; Premium €20/month; tick files €1 per instrument-day
Category: Finance / Market Data
Built by: CryptoStruct (github.com/cryptostruct/mcp-server, MIT)
```

## Why This Matters for Operators

Market data procurement has always been the least agent-friendly part of quant and event-driven research — catalogs are scattered, pricing is opaque, and evaluation requires buying files blind. CryptoStruct collapses the whole loop into tool calls: an agent can discover instruments, compare coverage and live spreads across venues, evaluate data quality, and only then hand the user a Stripe checkout URL for the exact instrument-days it needs.

**The mechanism worth copying is the keyless evaluation tier** — catalog search, market statistics (OHLC, VWAP, turnover, spreads, top-of-book depth, slippage curves), and free full-day sample files all work with zero credentials, so an agent can qualify a dataset before any spend is committed.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Catalog & discovery | Search ~500K instruments across 35 venues, including prediction-market event contracts |
| Market statistics | Live snapshots and minute/hourly/daily aggregates — OHLC, VWAP, trades, turnover, spreads, depth |
| Quality evaluation | Gap, error, and latency metrics per instrument before committing (Premium) |
| Commerce | Quote instrument-day baskets, get Stripe checkout URLs, download free sample files |
| Account (OAuth) | List orders, download purchased files, check subscription and credit balance |

## Installation

```bash
claude mcp add --transport http cryptostruct https://cryptostruct.com/mcp
# OAuth account link (orders, downloads, credits):
claude mcp add --transport http cryptostruct https://cryptostruct.com/mcp/auth
```

Generic clients use the JSON config below. claude.ai users can add the OAuth endpoint as a custom connector. A machine-readable server card is published at `/.well-known/mcp/server-card.json`.

## Configuration

```json
{
  "mcpServers": {
    "cryptostruct": {
      "url": "https://cryptostruct.com/mcp"
    }
  }
}
```

Auth notes: no API key needed for the catalog, stats, and guest purchase flow. OAuth (Dynamic Client Registration + PKCE) is optional and unlocks order history, purchased-file downloads, and automatic credit redemption. Rate limits are a weighted budget — 120 units/min keyless, 600 units/min Premium; over-tier calls return static upgrade errors rather than hard failures.

## Business Relevance

- **Quant and event-driven researchers** get microstructure data (spreads, depth, turnover, slippage) per instrument before buying
- **Prediction-market analysts** get event contracts as first-class instruments alongside spot and derivatives
- **Data procurement teams** get a quote → checkout → download loop an agent can run end to end
- **Portfolio operators** get coverage comparison across venues for any listed instrument, free and keyless

## Integration with CorpusIQ

CryptoStruct is the data-acquisition layer that pairs with CorpusIQ's financial connectors rather than overlapping them. A composed workflow: run portfolio exposure from the QuickBooks and Stripe connectors, then use CryptoStruct's catalog and market-statistics tools to stress-test crypto-adjacent positions with live depth and slippage curves. For research agents, the Stripe connector's charge ledger can reconcile the €1-per-instrument-day procurement spend back to the exact checkout links CryptoStruct issued — the server hands off payment through Stripe, which is the one credential boundary both systems respect.

## Limitations

- Brand new listing — no long track record yet
- Scope is crypto and prediction markets only — no equities or traditional macro data
- Minute-granularity data is retained ~30 days upstream; hourly/daily aggregates reach further back
- Premium (€20/month) required for longer stats windows, minute-series history, and larger search limits
- Hosted service — the repository documents the server; there is nothing to self-host

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
