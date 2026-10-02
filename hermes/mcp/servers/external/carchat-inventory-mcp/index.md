---
title: CarChat Inventory MCP - Live US Dealership Inventory
description: "Official no-auth MCP server for CarChat's live US dealership vehicle inventory - plain-English search, VIN detail, dealer directory and market price statistics across six tools at carchat.io/mcp, live-verified Aug 31, 2026."
category: Data & Analytics
stars: "0 (new listing, Carchat-io/mcp)"
added: 2026-08-31
source: "mcp.so homepage recentServers (Aug 31, 2026 evening sweep)"
relevance: ★★★
tags: [mcp-server, automotive, vehicle-inventory, used-cars, market-prices, dealership, data, remote]
---

# CarChat Inventory MCP

**Hosted Streamable HTTP MCP server exposing CarChat's live US dealership inventory - the same listings real buyers see, refreshed daily from each dealership's own lot.** Point an MCP client at one URL with no key at all, and six tools appear: plain-English inventory search with structured filters, full vehicle detail by VIN or listing id, curated metro category pages, a dealer directory with per-dealer counts, live market price statistics by body style and metro, and a consent-gated inquiry relay to the selling dealership.

```
Server type: Hosted, remote (Streamable HTTP), stateless
Endpoint: https://carchat.io/mcp
Auth: none - free to use, no API key
Protocol: MCP 2025-06-18, supports tools and prompts
Discovery card: https://carchat.io/.well-known/mcp.json
Repo: github.com/Carchat-io/mcp (MIT)
Homepage: carchat.io
Tools: 6 (search_inventory, get_vehicle, get_market_prices, list_shopping_categories, list_dealers, submit_inquiry)
```

## Why This Matters for Operators

Used-vehicle pricing research is a tab-heavy grind: jump between dealer sites, Craigslist-style boards and auction data, and every source has its own structure. CarChat normalizes all of it into one callable surface.

First, **live market prices without spreadsheets.** The get_market_prices tool returns real-time statistics from live inventory - count, median and price range, broken down by body style and metro - so an agent can answer "what do used trucks go for near Knoxville" with actual listed vehicles behind the numbers, not a model's remembered estimate.

Second, **the inventory is dealer-sourced, not aggregated hearsay.** Listings come from each dealership's own site and are refreshed daily, with the dealer's advertised price attached. No bait listings, no lead-selling middlemen between the data and the question.

Third, **every result is verifiable.** Each vehicle returns its CarChat listing URL, so a human can click through and confirm the price, mileage and dealer before acting on an agent's recommendation.

## Tools and Capabilities

All six tools were live-probed and verified Aug 31, 2026:

| Tool | What it returns |
|------|-----------------|
| `search_inventory` | Live vehicles across all CarChat dealerships from a plain-English query plus optional filters: make, model, body, color, condition, price, year, mileage, dealer, sort and limit |
| `get_vehicle` | Full detail for one vehicle by VIN or listing id: price, miles, dealership, photos, listing URL, plus the inquiry contract |
| `get_market_prices` | Live price statistics: count, median and range, overall and broken down by body style and metro |
| `list_shopping_categories` | Curated category pages, one per buyer intent and metro (for example "used trucks under $25,000 in Knoxville, TN") |
| `list_dealers` | All dealerships with live inventory: city, state, vehicle counts and each dealer's landing page URL |
| `submit_inquiry` | Consent-gated relay of a buyer's question and contact details to the selling dealership, which replies directly |

## Installation

Add the remote MCP server to any MCP client (Claude, Cursor, Cline, VS Code):

```json
{
  "mcpServers": {
    "carchat": {
      "url": "https://carchat.io/mcp"
    }
  }
}
```

## Configuration

No API key, no account, no sign-in. The server is free to use and answers anonymously; the endpoint also publishes a standard discovery card at carchat.io/.well-known/mcp.json for clients that auto-discover servers.

## Business Relevance

- **Dealership operators and sales managers** watch competitor pricing and stocking in their own metro directly from live listings instead of manual lot checks.
- **Auto lenders and fleet buyers** pull median and range pricing by body style to sanity-check valuations and purchase decisions.
- **Market analysts and publishers** cite real listed vehicles behind every price claim, with a URL per data point.
- **Agents in consumer-facing roles** answer car-shopping questions with live inventory, and only relay inquiries to dealers after the buyer explicitly agrees to share contact details.

## Integration with CorpusIQ

CarChat composes with CorpusIQ as the market-facing half of an automotive or asset-pricing workflow. CorpusIQ answers from the books you already run - QuickBooks for margins, Stripe for transaction economics, HubSpot for pipeline - while CarChat answers from the street: what vehicles are actually listed, at what prices, in which metros. An operator can ask "what is my average sale price versus the median listed price in Phoenix right now" and get both numbers, one internal and one market-side, in the same conversation. Pairs naturally with the Small Business Intelligence MCP for metro-level business data and with HasData MCP when the same questions extend to real estate or marketplace listings.

## Limitations

- Brand new listing: repo created Aug 31, 2026, zero stars - expect early-stage roughness and evolving limits.
- US dealership inventory only; no auction data, private-party listings or non-US markets.
- No historical price series - get_market_prices reflects current live inventory only.
- No self-host option; the hosted endpoint is the product.
- submit_inquiry is buyer-facing; operator-side wholesale and dealer-to-dealer flows are not exposed.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [HasData MCP - Marketplace and Web Data Gateway for Agents](/hermes/mcp/servers/external/hasdata-mcp)
- [Small Business Intelligence MCP - Metro Records and Teardowns](/hermes/mcp/servers/external/small-business-intelligence-mcp)
