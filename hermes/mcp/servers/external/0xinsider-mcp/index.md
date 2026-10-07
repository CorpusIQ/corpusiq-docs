---
title: "0xinsider MCP - Polymarket Trader Analytics for Agents"
description: "0xinsider is Polymarket analytics for sports and esports in real time, exposed to agents over a Streamable HTTP MCP endpoint with Bearer auth and an npm stdio client. The 57-operation OpenAPI surface covers market intel and candles, trader profiles and PnL, leaderboards, large positions, whale trades, sharp and smart money flows, insider-radar flags and durable event replay."
category: Finance
stars: n/a (new listing)
added: 2026-09-12
source: "mcpservers.org /all page 1 (night crawl) + developer resources at 0xinsider.com/developers.json + OpenAPI at 0xinsider.com/api/v1/openapi.json"
relevance: ★★★
tags: [polymarket, prediction-markets, trading, analytics, crypto, finance, remote-mcp, streamable-http]
---

# 0xinsider MCP

**Remote MCP server (Streamable HTTP, Bearer auth) + npm stdio client** - real-time Polymarket analytics for sports and esports markets. Traders and analysts get S-F wallet grades from settled records, large-trade and whale flows, smart-money movement and insider-radar flags as typed agent tools, with a public OpenAPI contract covering 57 operations and a machine-readable developer index.

```
Server type: Remote (Streamable HTTP) + local stdio via npm
Auth: Bearer API key (discovery and health endpoints are public)
Endpoint: https://api.0xinsider.com/api/v1/mcp
OpenAPI: https://0xinsider.com/api/v1/openapi.json
npm: @0xinsider/mcp (global install, command: 0xinsider)
Tools: 33 read-only MCP tools (57 REST operations documented)
Category: Finance
Built by: 0xinsider (0xinsider.com)
```

## Why This Matters for Operators

Prediction-market analytics have real operational uses: sentiment readouts for event-driven teams, research on market structure, and trader-level edge analysis. 0xinsider packages the raw Polymarket data into typed operations - `listSharpMoneyFlows` and `listSmartMoneyFlows` separate informed flow from noise, `getWhaleTrade` surfaces the trades that move a market, and `getEventReplaySince` gives durable replay for post-event review instead of a live-only stream. The MCP endpoint lets an agent drive all of it from one toolset.

## Tools & Capabilities

| Area | Operations |
|---|---|
| Markets | `exploreMarkets`, `getMarketSnapshot`, `getMarketCandles`, `getMarketIntel`, `batchGetMarketIntel` |
| Traders | `getTrader`, `getTraderContext`, `getTraderPnl`, `batchGetTraders`, `getTraderContextMarkdown` |
| Positions | `listPositions`, `listLargePositions`, `getPositionTimeline`, `getPositionTimelineById` |
| Flow | `getWhaleTrade`, `listSharpMoneyFlows`, `listSmartMoneyFlows`, `listLeaderboard` |
| Radar | `listInsiderRadar`, `getInsiderRadarFlag`, `listSportsEdgeObservations` |
| Reports | `getDailyReportSnapshot`, `getWeeklyReportSnapshot`, `getMonthlyReportSnapshot`, `getPickOfTheDay`, `getPickOfTheDayArchive` |
| Replay | `getEventReplaySince`, `getStream` |

57 operations in the published OpenAPI contract; the MCP surface exposes the read-only subset (33 tools). Webhooks with signed delivery and an export pipeline (`downloadTraderExport`) extend the API for automation.

## Installation

```bash
claude mcp add 0xinsider --transport http https://api.0xinsider.com/api/v1/mcp
npm install --global @0xinsider/mcp
```

Use the remote endpoint when the client can attach the key as a bearer Authorization header; use the npm package for a local stdio MCP client. Discovery and health endpoints are public, so `getApiDiscovery` works before any key exists.

## Configuration

```json
{
  "mcpServers": {
    "0xinsider": {
      "url": "https://api.0xinsider.com/api/v1/mcp"
    }
  }
}
```

Attach the key as the authorization header. Rate limits and error behavior are documented in the auth guide at 0xinsider.com/auth.md.

## Business Relevance

- **Quant and event-driven desks** get typed market, trader and flow data without building Polymarket scrapers.
- **Research teams** use `getEventReplaySince` for post-event analysis of market reaction.
- **Sports media and data products** pull pick-of-the-day archives and weekly report snapshots.
- **Compliance and risk teams** use insider-radar flags as a review signal on trader activity.

## Integration with CorpusIQ

0xinsider provides the external market-intelligence stream for operators whose business touches prediction markets; CorpusIQ holds their first-party business data. A CorpusIQ-connected agent covering an event-driven vertical can combine 0xinsider market snapshots and sharp-money flows with the operator's own revenue and funnel metrics to correlate market sentiment with business outcomes in one report.

## Limitations

- New listing: no third-party track record and no public source repo for the server itself.
- Bearer-key auth on the remote endpoint; no OAuth PKCE flow documented.
- Sports and esports market focus - general news and politics markets are thinner.
- Data is as fresh as the underlying Polymarket APIs; treat candles and snapshots as retrieved-time values.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [CryptoStruct Market Data MCP - Historical Crypto & Prediction-Market Data](/hermes/mcp/servers/external/cryptostruct-mcp)
