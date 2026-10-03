---
title: "PredictionMarketsPicks MCP - Kalshi and Polymarket Data"
description: "Keyless remote MCP over live Kalshi and Polymarket contracts, with strike ladders, cross-venue gaps and EV, Kelly and Bayes calculators."
category: "Business Operations"
stars: n/a (hosted platform, predictionmarketspicks.com)
added: 2026-10-03
source: "mcp.so server page (predictionmarketspicks)"
relevance: ★★★
tags: [prediction-markets, kalshi, polymarket, forecasting, finance, remote-mcp]
---

# PredictionMarketsPicks MCP

**Remote MCP server (Streamable HTTP, no key)** - PredictionMarketsPicks serves free, read-only Kalshi and Polymarket data to any MCP client: NFL prop prices across venues, strike ladders and win probability, cross-venue price gaps, Fed and 2026 Senate odds, the Kalshi 15-minute and perpetual boards, plus expected-value, Kelly and Bayes calculators. One URL, no API key, and nothing it exposes places an order.

```
Server type: Remote (Streamable HTTP)
Auth: None (keyless, read-only)
Endpoint: https://predictionmarketspicks.com/api/mcp/mcp
Tools: 34 (verified live via unauthenticated tools/list)
Pricing: Free, no key (Pro membership adds edge calls and mispricing scans)
Category: Business Operations
Built by: PredictionMarketsPicks (predictionmarketspicks.com)
```

## Why This Matters for Operators

Prediction markets are the closest thing to a live, money-weighted forecast of events a business plan depends on: whether the Fed cuts at the next FOMC meeting, which way a Senate race is leaning, what a commodity or crypto contract implies for the next quarter. Reading them normally means juggling Kalshi, Polymarket and CME tabs by hand. This server puts the same contracts behind one endpoint an agent can query, and it returns the cross-venue gap rather than a single venue's price, so an operator sees where the two markets disagree.

**The differentiator is comparability.** Every answer carries the venue breakdown and the divergence in percentage points, so a forecast can be sanity-checked against a second market instead of trusted blindly. The calculators (expected value, Kelly sizing, Bayes updates, odds conversion) turn a price into a position size or a posterior in the same call.

## Tools & Capabilities

34 tools, verified through a live `tools/list`. The notable ones:

| Tool | Purpose |
|---|---|
| `fed_rate_odds` | Live Kalshi odds for each remaining 2026 FOMC meeting, with a Polymarket and CME cross-check and the gap in pp |
| `senate_map` | 2026 Senate race odds across seats |
| `nfl_prop_board` / `nfl_prop_edge` | Every Kalshi NFL prop strike beside other venues' prices, best price per side |
| `nfl_ladder` / `nfl_win_probability` / `nfl_power_ratings` | Strike ladders and win, cover and total probabilities from the model's power ratings |
| `adp_market_gaps` | Fantasy ADP versus market pricing |
| `find_arbitrage` / `ladder_arb` / `combo_edge` | Cross-venue and within-venue mispricing scans |
| `perps_board` / `fifteen_min_board` / `perp_liquidation` | Kalshi perpetual futures and 15-minute boards for crypto, metals and energy |
| `calculate_ev` / `kelly_size` / `bayes_update` / `convert_probability` | Expected value, Kelly sizing, Bayesian updates and odds conversion |
| `edge_alerts` / `scan_mispricings` | Pro-tier edge calls and live mispricing scans |

## Installation

```bash
claude mcp add predictionmarketspicks --transport http https://predictionmarketspicks.com/api/mcp/mcp
```

In Claude, add it under Settings then Connectors as a custom connector with the URL above. In ChatGPT, turn on developer mode and create a connector with the same URL and no authentication. Cursor and VS Code have a one-click install at `https://predictionmarketspicks.com/mcp/cursor`.

Focused servers expose the same tools grouped by topic:

- Fantasy draft: `https://predictionmarketspicks.com/api/mcp-draft/mcp`
- Weather markets: `https://predictionmarketspicks.com/api/mcp-weather/mcp`
- Commodities (gold, silver, oil, Bitcoin): `https://predictionmarketspicks.com/api/mcp-commodities/mcp`

## Configuration

```json
{
  "mcpServers": {
    "predictionmarketspicks": {
      "type": "http",
      "url": "https://predictionmarketspicks.com/api/mcp/mcp"
    }
  }
}
```

No API key and no OAuth step. The endpoint is read-only by design: no tool places, cancels or modifies an order on either venue.

## Business Relevance

- **Founders and finance teams** read the market-implied probability of a Fed move or a macro event before committing to a rate-sensitive plan.
- **Analysts** hedge a forecast by comparing it against the cross-venue gap rather than a single market's price.
- **Sales and strategy teams** track election and policy odds that move regulated or government-facing pipelines.
- **Traders and quants** screen for cross-venue mispricing and size positions with the built-in Kelly and EV calculators.
- **Anyone building forecasting agents** gets a keyless, read-only data surface that carries provenance and freshness on every answer.
