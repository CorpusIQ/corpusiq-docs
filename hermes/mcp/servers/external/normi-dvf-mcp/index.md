---
title: "Normi DVF MCP: French Property Market Data"
description: "17.4M+ geocoded French property transactions (DVF government open data, 2014 to present) as an MCP server - property search, market stats, comparables, price trends, neighborhood comparison, activity, heatmaps and address history. 8 tools, free tier with 100 credits."
category: "Real Estate"
stars: 0
added: 2026-08-23
source: "mcpservers.org /all + GitHub README"
relevance: ★★
tags: [real-estate-data, french-property, dvf, comparables, property-valuation, market-stats, remote-mcp]
last_updated: "2026-10-19"
---

# Normi DVF MCP

**Access 17.4M+ geocoded French property transactions (DVF, the French government's open property-transfer dataset) from any MCP client - search properties, pull market stats, find comparables, track price trends, compare neighborhoods, and read address histories.** Covers all of metropolitan France from 2014 to present, updated semi-annually with each government release, under the Licence Ouverte 2.0.

```
Server type: Remote (Streamable HTTP) or local via npx
Auth: API key (free tier: 100 credits/month)
Endpoint: https://mcp.normi.fr/mcp
Tools: 8
Pricing: Free 100 credits; Agent 55,000 credits 49 EUR/mo; Pro 175,000 149 EUR/mo; Enterprise 500,000 399 EUR/mo
Category: Real Estate
Built by: Normi (normi.fr, MIT)
```

## Why This Matters for Operators

French property prices are one of the few markets with complete, mandatory transaction records - the DVF dataset logs every sale with price, surface and location - but the raw files are quarterly government dumps that require geocoding and a data pipeline to be useful. Normi does that work and exposes the result as eight MCP tools with a credit-based pricing model, so an agent can answer "prix au m2 Paris 15e" or "find comparables for a 65m2 T3 in Lyon 3e" with actual transaction data instead of portal list prices.

For anyone evaluating French property - investors, relocation services, notaries, lenders or agencies - this is the difference between asking a model to guess and asking it to read the official ledger. The REST API (`mcp.normi.fr/v1/...`) is available for non-MCP use cases.

## Tools & Capabilities

| Tool | Description | Credits |
|---|---|---|
| `search_properties` | Search transactions by location, type, price, surface | 5 |
| `get_market_stats` | Aggregate stats: median price, price per m2, volume | 5 |
| `find_comparables` | Find similar properties by proximity and surface | 10 |
| `get_price_trends` | Price evolution over time (month/quarter/year) | 10 |
| `compare_neighborhoods` | Compare 2-5 locations side by side | 10 |
| `get_market_activity` | Transaction volume and seasonality | 10 |
| `get_market_heatmap` | Price data by zone for a department | 15 |
| `get_property_history` | Transaction history for a specific address | 20 |

## Installation

```bash
claude mcp add --transport http normi https://mcp.normi.fr/mcp --header "Authorization: Bearer normi_YOUR_TOKEN"
```

Or local via npx: `npx -y @normi/mcp-dvf` with `NORMI_API_KEY` in the environment.

## Configuration

```json
{
  "mcpServers": {
    "normi": {
      "command": "npx",
      "args": ["-y", "@normi/mcp-dvf"],
      "env": { "NORMI_API_KEY": "normi_YOUR_TOKEN_HERE" }
    }
  }
}
```

Sign up at normi.fr and create a token in the dashboard. The server is listed in the official MCP Registry.

## Business Relevance

- **Property investors and funds** pull comparables, price-per-m2 trends and neighborhood comparisons from official transaction records, not listings.
- **Relocation and mobility teams** answer cost-of-living and housing-market questions with real data per department.
- **Notaries, lenders and valuers** get address-level transaction history with a documented API and MCP path.
- **Analysts covering French markets** build reproducible market snapshots (median price, volume, seasonality) on a credit-metered budget.
