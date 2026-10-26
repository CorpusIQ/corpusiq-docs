---
title: MarketCode MCP - UK Property Intelligence for Agents
description: Value any UK address, read market liquidity and price levels, source land and off-market stock, and screen auction distress through one hosted property-data endpoint.
category: Real Estate
stars: n/a (new listing)
added: 2026-09-02
source: mcp.so
relevance: ★★★
tags: [real-estate, property-valuation, uk, land-registry, auctions, geospatial, remote-mcp]
last_updated: "2026-10-19"
---

# MarketCode MCP

**Remote MCP server (Streamable HTTP, OAuth)** - UK property intelligence for AI agents, built by RoboSapien Limited. Value any address with a free AVM and confidence range, read prices, price per square metre and liquidity across 28 million UK transactions back to 1995, and source land and off-market stock by registered ownership and development upside. Fifty tools over one endpoint, with most reads free.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (claude.ai connectors) or API key (Claude Code, server clients)
Endpoint: https://mcp.marketcode.ai/mcp
Tools: 50 (address resolution, valuations, market analytics, ownership, auctions, sourcing)
Pricing: Most tools free; signup grants 100 credits; paid tools cost 3-10 credits
Category: Real Estate
Built by: RoboSapien Limited
```

## Why This Matters for Operators

Property questions land on operators constantly - what a site is worth, what comparable assets actually traded for, whether a market is liquid, who owns the parcel next door, whether an auction lot that keeps failing is a bargain or a repricing problem. Each of those questions used to mean a different subscription, a spreadsheet of manual lookups, or a broker on the phone.

MarketCode compresses all of it into one agent-callable endpoint with an unusual level of analytical honesty. Every market row carries a `tx_decision` flag stating whether the price behind it is direct, modeled, suppressed, imputed or missing - so an agent can tell you when a figure is a measurement and when it is a borrowed prior. **That distinction is the difference between quoting a real comp and inventing one.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `address_autocomplete` | Ranked candidates for a partial address or postcode (free entry point) |
| `address_resolve` | Free-text address to canonical UPRN record |
| `property_lookup` | Full property record up to ~300 fields, grouped into identity, energy, land, risk, ownership and provenance tiers |
| `property_summary` | One-call headline answer on a specific property |
| `valuation_estimate` / `valuation_full` | AVM point value plus range, back-series, rental estimate and trust score |
| `property_comps` | Comparable sales in the same building with missing attributes backfilled |
| `market_facts` | Price, price per sqm and turnover for one geography, asset class and bedroom band |
| `market_ranking` | Area-versus-area league tables weighted by evidence behind each cohort |
| `market_volume_series` / `market_volume_ranking` | Every registered sale 1995 to present, by district, area or county |
| `ownership_by_title` / `ownership_by_company` | Registered proprietors by HM Land Registry title or Companies House number |
| `auction_lots` / `auction_stats` | Achieved hammer prices measured against the AVM, and quarterly clearing statistics |
| `distressed_assets` | Lots that repeatedly fail at auction, ranked with a guide-to-AVM distress ratio |
| `site_appraisal` | Full site dossier: parcel, valuation, ownership, energy, auction history, designations and signals |
| `planning_designations` | Conservation areas, listed buildings, green belt, flood zones and Article 4 in one call |

## Installation

```bash
claude mcp add marketcode --transport http https://mcp.marketcode.ai/mcp
```

The vendor publishes per-client walkthroughs for Claude Code, Codex, Cursor and VS Code on the listing page.

## Configuration

```json
{
  "mcpServers": {
    "marketcode": {
      "type": "http",
      "url": "https://mcp.marketcode.ai/mcp"
    }
  }
}
```

First connect opens a browser OAuth screen for claude.ai connectors; API keys are used for Claude Code and server clients. Tool discovery needs no credentials, so you can browse the full catalogue before signing up.

## Business Relevance

- **Investors and asset managers** get valuations, comps and liquidity rankings with the evidence level stated per cell, instead of a flat number
- **Agencies and developers** source long-held, high-equity owners who never come to market, with title boundaries as GeoJSON
- **Property operators** reconcile EPC, Rightmove, council tax and OS data divergences in one call
- **Auction buyers** read achieved hammer prices against the AVM to see how far below market a lot cleared

## Integration with CorpusIQ

MarketCode is the UK-property analogue of what CorpusIQ does for business financials - it turns a registry of record into queryable, agent-ready answers. An agent running CorpusIQ connectors for a UK property business can pair QuickBooks or Stripe revenue with MarketCode's market rankings to test whether portfolio turnover matches district liquidity, or join HMLR ownership lookups to deal flow tracked in HubSpot. The composed workflow is: CorpusIQ reads the business, MarketCode reads the market, and the agent reconciles the two.

## Limitations

- UK only; England and Wales coverage is deepest, with some tools excluded for Scotland and Northern Ireland
- Credit-based pricing on several core tools (8-10 credits per resolution call)
- Brand new listing with no track record yet
- Some market metrics (rental value, gross yield, days on market) are declared not yet backfilled and return null by design
