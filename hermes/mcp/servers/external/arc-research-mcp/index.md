---
title: Arc Research MCP
description: Commodities research over MCP — a knowledge graph, CFTC positioning, natural gas and weather data, futures quotes and private research journals.
category: Finance
stars: n/a (new listing)
added: 2026-08-17
source: mcpservers.org
relevance: ★★
tags: [commodities, research, knowledge-graph, futures, positioning, market-data, research-journal, remote-mcp]
---

# Arc Research MCP

**Remote MCP server (Streamable HTTP, bearer token)** — Arc Research gives an agent live access to a commodities research platform: a knowledge graph over concepts and themes, CFTC COT positioning with week-over-week flows and oscillators, natural gas storage and weather, futures quotes, and your private stories and journals. Tools are thin adapters over the same services that power the web app. Registry name: `com.getarcresearch/arc-research`.

```
Server type: Remote (Streamable HTTP)
Auth: personal bearer token (Account → MCP access)
Endpoint: https://www.getarcresearch.com/mcp
Tools: knowledge-graph search, market data, COT positioning, natural gas & weather, stories & journals
Pricing: included with Arc Research Starter subscription
Category: Finance
Built by: Arc Research (getarcresearch.com)
```

## Why This Matters for Operators

Commodities research has been a copy-paste job: charts, CFTC snapshots, and weather forecasts hand-carried into the prompt. Arc Research makes the underlying platform's data MCP-addressable so the agent reads it directly — and keeps the researcher's own theses in the same surface.

**The knowledge graph is the differentiator**: search concepts, inspect neighborhoods, and explain paths between themes — so an agent can trace how a positioning shift connects to a weather event to a price move, instead of holding three disconnected datasets. Private stories and journals stay scoped to your account; only administrator-owned stories are written into the shared graph.

## Tools & Capabilities

| Area | Purpose |
|---|---|
| Knowledge graph | Search concepts, inspect neighborhoods, explain paths between themes |
| Market data | Resolve commodities and tickers, futures quotes, pinned hubs |
| COT positioning | Latest CFTC snapshots, week-over-week flows, oscillators, published briefs |
| Natural gas & weather | EIA storage, NOAA degree days, GFS/ECMWF demand forecasts |
| Stories & journals | List, read, semantically search, and append entries to your theses |

## Installation

```bash
# 1. Subscribe to Arc Research Starter (or sign in)
# 2. Create a token under Account → MCP access
claude mcp add arc-research --transport http https://www.getarcresearch.com/mcp --header "Authorization: Bearer <token>"
```

## Configuration

```json
{
  "mcpServers": {
    "arc-research": {
      "type": "http",
      "url": "https://www.getarcresearch.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_TOKEN"
      }
    }
  }
}
```

## Business Relevance

- **Commodity traders and analysts** get CFTC positioning and weather data in the same tool call as their own journal notes.
- **Macro researchers** get a knowledge graph that explains the paths between themes rather than returning a document list.
- **Energy operators** get EIA storage and degree-day demand context without building their own ingestion.
- **Fund analysts** get private, account-scoped thesis journals that semantic search can mine.

## Integration with CorpusIQ

Arc Research extends the financial-data layer CorpusIQ already connects. An operator running the numbers in QuickBooks and Stripe can have the agent pull positioning and weather context from Arc Research when a commodity-linked cost line moves, tying macro cause to ledger effect. The journal tooling pairs with the research intelligence framework — thesis notes stay account-scoped while the shared knowledge graph supplies the market context, keeping proprietary thinking and public data cleanly separated.

## Limitations

- Brand new — no track record yet; listing appeared August 17, 2026.
- Requires an Arc Research Starter subscription — token access is not standalone.
- Commodities only — no equities or rates coverage.
- Shared research is available to other Research subscribers; only journals and uploads are private.
- Tool-level schema is thin in the docs; verify against the endpoint after connecting.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
