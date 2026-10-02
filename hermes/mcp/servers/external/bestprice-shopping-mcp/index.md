---
title: "BestPrice Shopping MCP - Greek Market Price Comparison"
description: "Read-only product search, merchant offer comparison, and price history for the Greek market. Search the BestPrice.gr catalog, compare delivered totals to Greek postal codes, and see whether today's price is low or high over 30, 90, or 180 days."
category: Commerce & E-Commerce
stars: 0
added: 2026-08-26
source: "mcp.so GitHub issue #3780"
relevance: ★★★
tags: [ecommerce, price-comparison, price-history, greece, retail, remote-mcp, keyless]
---

# BestPrice Shopping MCP

**Remote MCP server (Streamable HTTP, keyless) for BestPrice.gr - product search, offer comparison, and price history for the Greek market.** Three read-only tools: search physical products across the reviewed BestPrice Greece catalog, compare current merchant offers delivered to a five-digit Greek postal code (shipping or delivered totals when available), and check whether today's price is low, typical, or high over 30, 90, or 180-day windows. The endpoint answered an anonymous live probe with serverInfo `bestprice-agent-commerce` v1.5.1 and exposed all three tools.

```
Server type: Remote (Streamable HTTP)
Auth: None
Endpoint: https://mcp.bestprice.gr/mcp
Tools: 3 (all read-only)
Pricing: Free, keyless
Category: Commerce & E-Commerce
Built by: TheBestCo / BestPrice.gr (registry gr.bestprice/mcp)
```

## Why This Matters for Operators

Greek e-commerce pricing intelligence normally means a person opening the BestPrice.gr site and comparing offers by hand, product by product. This endpoint lets an agent do that at scale: search the catalog, compare delivered totals across merchants for a specific postal code, and read the 30/90/180-day price history to judge whether a price is a deal or a trap. For retailers, distributors, and market analysts, that is competitive pricing data without a scraping project.

**The fail-closed design is notable.** Search is bounded to reviewed physical-goods categories; regulated or prohibited categories and catalog-dump requests fail closed. Results return signed BestPrice landing URLs rather than direct merchant URLs, so traffic attribution stays inside the platform.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_products` | Discovers physical products in the supported BestPrice Greece catalog, or looks up a known `product_id` |
| `compare_offers` | Compares current BestPrice offers for one grouped `product_id`, delivered to a five-digit Greek postal code, with shipping or delivered totals when available |
| `get_price_history` | Judges whether a product's current price is low, typical, or high over 30, 90, or 180-day windows |

## Installation

No auth, no install. Add the hosted endpoint to any MCP client:

```json
{
  "mcpServers": {
    "bestprice": {
      "url": "https://mcp.bestprice.gr/mcp"
    }
  }
}
```

Health check: https://mcp.bestprice.gr/healthz · Repo: https://github.com/TheBestCo/bestprice-mcp (license not declared)

## Configuration

Nothing to configure - the endpoint is public and keyless. The server card is published at https://mcp.bestprice.gr/mcp/server-card. Privacy and terms live under www.bestprice.gr/policies/.

## Business Relevance

Three concrete operator use cases: a retailer checks where its own products price against competitors delivered to a customer's postal code; a buyer verifies whether a quote is high or low against 180 days of market history; an analyst tracks catalog price movement by category without building a scraper. The delivered-total comparison is the detail that matters in Greece, where shipping differences between mainland and islands regularly flip which merchant is actually cheapest.

## Integration with CorpusIQ

Complementary to CorpusIQ's commerce and analytics connectors: an agent can pull a brand's own sales and inventory context from CorpusIQ, then use BestPrice to read the Greek market's current offers and price history for the same categories. Both surfaces are read-only, and BestPrice's keyless design means no credential provisioning step before first use.

## Limitations

- Greek market only (`el-GR`), and search is bounded to reviewed physical-goods categories - regulated or prohibited categories fail closed.
- Price history windows are fixed at 30/90/180 days.
- Requires exact grouped `product_id` values for offer comparison and price history - discovery always starts with `search_products`.
- Repo is brand new (created Aug 26, 2026, 0 stars) and declares no license.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Walmart Marketplace MCP](/hermes/mcp/servers/external/walmart-marketplace-mcp)
- [CorpusIQ Connectors](/hermes/mcp/servers)
