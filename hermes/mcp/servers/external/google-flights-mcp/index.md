---
title: "Google Flights MCP: Real-Time Fare Search with Price"
description: "Hosted ad-free MCP server for real-time Google Flights fares: one-way and round-trip search over date ranges and destination lists, with Google's historical price range on every result so the agent can say whether a fare is actually good. Bring your own RapidAPI key; free tier and a free ad-supported endpoint exist."
category: Content & Research
stars: n/a (new listing)
added: 2026-08-24
source: "chatmcp/mcpso issue #3729"
relevance: ★★
tags: [flights, travel, fares, airline-pricing, price-insights, travel-procurement, remote-mcp]
---

# Google Flights MCP

**Hosted, ad-free MCP server for real-time Google Flights fares.** Published by FlightPowers as `com.flightpowers/google-flights` on the official MCP registry, it answers fare questions rather than date lookups: both tools accept a departure date range, a list of destination airports, and round-trip trip lengths in nights, expanding them internally so one call covers what would otherwise be dozens of single-date queries.

```
Server type: Remote (Streamable HTTP)
Auth: Bring-your-own RapidAPI key (x-rapidapi-key header or rapidapi_key query param)
Endpoint: https://google-flights-mcp.flightpowers.com/mcp
Tools: 2 (search_oneway_flights, search_roundtrip_flights)
Pricing: Free tier on RapidAPI; free ad-supported endpoint also available
Category: Travel / Research
Built by: FlightPowers (repo: mtnrabi/google-flights-mcp, MIT)
```

## Why This Matters for Operators

"Cheapest one-way to Sri Lanka anywhere in October" used to be thirty searches. Here it is one tool call. Every result carries Google's own historical price range for the route and period (`price_insights_low`, `price_insights_high`, and a `price_range_in_relation_to_other_periods` verdict of low / typical / high), so the agent can say "$209 is typical here, do not rush" instead of quoting a bare number. **The fare verdict is the differentiator**: the server turns price discovery into a buy-don't-buy answer with a bookable `buy_link`.

Operators get two practical loops: travel procurement that prices whole date ranges at once, and fare monitoring for routes the business flies repeatedly. Every response also carries `api_usage` (requests used, plan remaining) and `search_coverage` (which dates and destinations the answer is based on), so spend and honesty are both auditable.

## Tools & Capabilities

Both tool names captured by live anonymous `tools/list` (server v1.0.0):

| Tool | Purpose |
|---|---|
| `search_oneway_flights` | One-way fare search over a date range or destination list, with price insights, buy links, and per-call usage |
| `search_roundtrip_flights` | Round-trip search with trip length in nights instead of a fixed return date |

Both tools accept airline include/exclude filters, max stops, departure and arrival time windows, currency, max price, seat class, and passenger mix. Results are live fares and go stale within minutes - re-search instead of caching.

## Installation

```bash
claude mcp add --transport http google-flights https://google-flights-mcp.flightpowers.com/mcp --header "x-rapidapi-key: YOUR_KEY"
```

The key comes from subscribing to the Google Flights Live API on RapidAPI (free tier available). No key yet? A free ad-supported server serves the same search without signup: `claude mcp add --transport http google-flights-free https://google-flights-lulu.flightpowers.com/mcp` (one disclosed sponsored card per result, fan-out capped at 15).

## Configuration

```json
{
  "mcpServers": {
    "google-flights": {
      "type": "http",
      "url": "https://google-flights-mcp.flightpowers.com/mcp",
      "headers": {
        "x-rapidapi-key": "YOUR_RAPIDAPI_KEY"
      }
    }
  }
}
```

The server holds no upstream credential of its own - every search is billed to the caller's RapidAPI subscription, which is why the key travels with the request. If a key is missing, tools return `needs_api_key: true` with the signup URL instead of failing silently.

## Business Relevance

- **Travel and procurement managers** price entire date ranges and destination lists in one call
- **Finance teams** audit fare decisions with the historical price range attached to every result
- **Travel agencies and booking platforms** embed live fare verdicts in agent workflows
- **Frequent flyers and founders** get buy-don't-buy answers with a bookable link

## Integration with CorpusIQ

Fares come from Google Flights MCP; spend reality comes from CorpusIQ. An agent can price a team trip across a date range, then check the travel budget in QuickBooks through the CorpusIQ connector and log the decision in the CRM or a document store. For travel-heavy operators, the composed workflow is fare search plus expense reconciliation in one conversation, with the per-call `api_usage` field feeding cost tracking alongside the business's own spend data.

## Limitations

- New listing (Aug 24, 2026); repo has no star history yet.
- Requires the caller's own RapidAPI key; each date/destination combination is one billed request.
- Live fares go stale within minutes - results are point-in-time by design.
- Travel scope only: fares and price insights, no hotel, seat map, or loyalty data in this server.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
