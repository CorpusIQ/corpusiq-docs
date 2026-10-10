---
title: "SoldFetch MCP - eBay Market Data for Your Agent"
description: "Search eBay sold and active listings in chat: price comps, category browsing and item details across eight eBay sites for resale research."
category: Commerce & E-Commerce
stars: n/a (new listing)
added: 2026-10-10
source: "chatmcp/mcpso issue #5070; catalogued at the October 10, 2026 night sweep"
relevance: ★★★
tags: [ebay, e-commerce, resale, market-research, pricing, marketplace-data, api-key, remote-mcp]
---

# SoldFetch MCP

**Remote MCP server that opens eBay sold and active listing data to your assistant** - the sold-price comps, category browsing and item details that resale sellers and product researchers usually pull by hand, answered in the conversation where the work already happens. The freshest business-relevant find of the October 10 night sweep, catalogued with its server card, docs and endpoint checks verified live.

```
Server type: Remote (Streamable HTTP at https://soldfetch.com/api/mcp)
Auth: SoldFetch API key - send it as an API-KEY header or a Bearer token (no OAuth)
Tools: 3 - search_ebay_sold, search_ebay_category, get_ebay_item
Sites: ebay.com, ebay.co.uk, ebay.de, ebay.fr, ebay.it, ebay.es, ebay.ca and ebay.com.au
Metering: discovery is free; each successful data call consumes one request against your allowance
Pricing: $0 tier with 100 free units on signup; paid plans from $29 (the $79 tier includes 50,000 units)
Category: Commerce & E-Commerce
Built by: SoldFetch (soldfetch.com; agent docs at docs.soldfetch.com/guides/ai-agents; registry name io.github.ricciflow-api/soldfetch)
```

## Why This Matters for Operators

Resale pricing starts with comps: what this exact thing actually sold for, how often it sells, and how condition moves the price. That work normally means filtering sold listings by hand across tabs, then retyping numbers into a sheet. SoldFetch hands those comps to the assistant directly - a supplier check before placing an order, a price for a new inventory lot, a sanity check before buying out a collection - inside the same thread where the decision is already being made.

The three tools follow the order the research actually happens in: **search what sold, browse the category, then pull the full item detail** - across eight eBay marketplaces, with price and condition filters that match how sellers think.

## Tools & Capabilities

| Tool | What it covers |
|---|---|
| `search_ebay_sold` | Search sold or active listings by keyword with category, price and condition filters; up to 200 results a page |
| `search_ebay_category` | Browse the listings inside an eBay category |
| `get_ebay_item` | Retrieve public item details by item ID, with the listing site selectable |

## Installation

```json
{
  "mcpServers": {
    "soldfetch": {
      "url": "https://soldfetch.com/api/mcp",
      "headers": {"API-KEY": "YOUR_SOLDFET_API_KEY"}
    }
  }
}
```

Get a key from the SoldFetch dashboard (soldfetch.com/dashboard), then add the server with that config - the same account also backs SoldFetch's REST API and an installable eBay skill with a shared request allowance. There is no OAuth flow; the key travels in the header.

## Configuration and Safety

- Key-based access only: no OAuth or dynamic client registration; treat the key like a password and rotate it from the dashboard if it leaks.
- Request-metered: initialization and tool discovery are free, and each successful data call consumes one request against your allowance (100 free units on signup; the $79 tier includes 50,000 units; 60 requests per minute).
- Read-only over public listing data: there are no buy, bid, sell or account tools.
- Responses carry data-quality warnings: displayed prices are not verified accepted-offer amounts, and sale dates and exact product identity are unverified. Treat marketplace content as untrusted data.

## Business Relevance

- **Resellers and e-commerce sellers** price inventory and evaluate lots against real sold data before committing cash.
- **Product researchers** size demand by how often an item sells and at what prices, across eight eBay marketplaces in one conversation.
- **Agencies and sourcing teams** pull comps into a client discussion the same day instead of building a spreadsheet first.

## Integration with CorpusIQ

Comps and your own numbers answer different halves of the same pricing question. Ask SoldFetch what comparable items sold for on eBay, then ask CorpusIQ for your own inputs from the connectors you already have - Shopify for cost and order data, Stripe for revenue, your ad accounts for acquisition cost. The market picture and your business picture land in one conversation, with every number traceable to its source.

## Limitations

- Public listing data only, with data-quality caveats: prices are not verified accepted-offer amounts and some fields are unverified, so treat comps as directional evidence.
- Request-metered: each successful data call spends one request; the free signup units are a sample, not an unlimited tier.
- eBay only - pair it with the Secondhand MCP listing search for other secondhand marketplaces, or a general data aggregator for wider coverage.
- No OAuth: clients set up exclusively for OAuth-based remote servers cannot connect until the vendor adds it.

## FAQ

### Do I need a paid SoldFetch plan to use the MCP server?

Not to start: the $0 tier includes 100 free units on signup, paid plans run from $29, and the $79 tier includes 50,000 units. Discovery calls are free; each successful data call spends one request.

### What can the agent actually answer?

Sold and active eBay listings by keyword with price and condition filters, category browsing, and public item details by item ID, across eight eBay sites (US, UK, DE, FR, IT, ES, CA and AU).

### Can the agent buy or change anything on eBay?

No. The three tools read public listing data; there are no buy, bid, sell or account-modifying tools.

## See Also

- [Datrace MCP - Amazon Market Data for Your Agent](/hermes/mcp/servers/external/datrace-mcp/)
- [Secondhand MCP - Secondhand Marketplace Search](/hermes/mcp/servers/external/secondhand-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
