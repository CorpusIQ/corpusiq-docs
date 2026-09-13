---
title: "StayingAPI MCP - Cross-OTA Accommodation Data for Agents"
description: "StayingAPI Hotel and Accommodation MCP gives AI agents first-class tools over accommodation data across Airbnb, Booking.com, Vrbo and Google Hotels in one unified schema. Seven read-only tools cover stay search, day-by-day availability, listing details, real price quotes, cross-OTA price comparison, normalized reviews and async job polling. OAuth 2.1 PKCE with Dynamic Client Registration."
category: Data & Analytics
stars: n/a (new listing)
added: 2026-09-12
source: "mcpservers.org /all page 1 (night crawl) + vendor docs at stayingapi.com/docs/mcp"
relevance: ★★★
tags: [travel, hotels, accommodation, ota, pricing, oauth, remote-mcp, streamable-http]
---

# StayingAPI MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 PKCE)** - a native MCP surface for StayingAPI, an accommodation data API that normalizes Airbnb, Booking.com, Vrbo and Google Hotels into one schema. Revenue managers, travel agents and analytics teams query live availability and real price quotes across OTAs from inside the assistant, with one credit balance shared with the REST API.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 + PKCE (S256) with Dynamic Client Registration, or stay_live_ bearer key
Endpoint: https://mcp.stayingapi.com/mcp
Tools: 7 (all read-only)
Pricing: Credit balance (free sandbox account for evaluation; no card required)
Category: Data & Analytics
Built by: StayingAPI (stayingapi.com)
```

## Why This Matters for Operators

Cross-OTA price comparison is the core workflow of any short-term rental or hotel operation, and it usually lives in spreadsheets fed by manual checks. StayingAPI puts the comparison inside the agent: `compare_prices` returns one property across platforms with a computed min and median, `check_availability` gives day-by-day windows, and `get_price` returns a real quote for specific dates and occupancy. Because every tool draws from one credit balance and one account, a revenue team can run a full competitive pricing pass in a single conversation instead of four browser sessions.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_stays` | Search stays across platforms by location, dates, occupancy and filters |
| `check_availability` | Day-by-day availability for a known listing over a date window |
| `get_listing` | Full detail for one listing: amenities, photos, host, ratings |
| `get_price` | Real price quote for one listing, specific dates and occupancy |
| `compare_prices` | Compare one property across OTAs with computed min and median |
| `get_reviews` | Normalized, paginated reviews for one listing on one platform |
| `get_job` | Poll status and fetch the result of an async scrape job (costs 0) |

## Installation

1. Create an account at stayingapi.com (sandbox accounts work for evaluation; no card required).
2. In Claude, add a custom connector with the URL `https://mcp.stayingapi.com/mcp` and complete the OAuth browser popup - the connector links to your StayingAPI account and credit balance.
3. Other clients: add the URL as a Streamable HTTP server; clients with OAuth Dynamic Client Registration authenticate automatically, others present a `stay_live_` bearer key.

```bash
claude mcp add stayingapi --transport http https://mcp.stayingapi.com/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "stayingapi": {
      "url": "https://mcp.stayingapi.com/mcp"
    }
  }
}
```

All seven tools are read-only and consume from the same credit balance as the REST keys. The repo (stayingapi/hotel-mcp) publishes registry manifests for the official MCP registry, Smithery and Glama.

## Business Relevance

- **Short-term rental operators** run daily competitive price checks across Airbnb, Booking.com and Vrbo from one tool.
- **Revenue managers** use `compare_prices` min/median computations to set nightly rates against the market.
- **Travel agencies** search and compare inventory across OTAs in a unified schema for client proposals.
- **Market analysts** pull normalized reviews and listing data for supply and demand research.

## Integration with CorpusIQ

StayingAPI is a live data feed for a travel or hospitality vertical; CorpusIQ is the reporting layer that holds it against the business's own numbers. A CorpusIQ agent for a rental operator can pull StayingAPI market prices and compare them with internal booking data from a PMS connector to produce a rate-positioning report - occupancy and revenue from CorpusIQ, market context from StayingAPI, in one analysis.

## Limitations

- Credit-based pricing: every tool call except `get_job` consumes balance; heavy polling can burn credits fast.
- OTA coverage is the four named platforms; niche channels are absent.
- New listing with a 0-star GitHub repo and no third-party review track record yet.
- Platform data freshness depends on the underlying scrapes; treat quotes as of retrieval time.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Airside Labs Aviation Tools MCP - Provenance-Backed Aviation Reference Data](/hermes/mcp/servers/external/airside-aviation-mcp/)
