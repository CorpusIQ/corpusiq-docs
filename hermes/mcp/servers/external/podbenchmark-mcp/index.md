---
title: "POD Benchmark MCP - Print-on-Demand Supplier Costs"
description: "Compare print-on-demand supplier prices across Printful, Printify, Gelato and five more, with delivered cost by size, colour and destination over MCP."
category: E-commerce / Product Sourcing
stars: n/a (free, no account, read-only)
added: 2026-10-26
source: "live MCP probe on podbenchmark.com/api/mcp (initialize 200 on protocol 2025-06-18, tools/list 200 with 10 tools, two executed calls returning supplier and category payloads) + vendor site podbenchmark.com + mcpservers.org card + official MCP registry entry com.podbenchmark/podbenchmark"
relevance: ★★★
tags: [print-on-demand, ecommerce, supplier-pricing, product-sourcing, margin, shopify, printful, printify]
---

# POD Benchmark MCP

**The question a print-on-demand seller actually asks is which supplier is cheaper for this shirt in this size delivered to this country, and that question now has one call.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://podbenchmark.com/api/mcp
Transport:   JSON-RPC 2.0 over HTTP, JSON or SSE responses
Auth:        none, read-only, 120 requests per minute per IP
Tools:       10, read from a live tools/list
Built by:    POD Benchmark (podbenchmark.com)
Registry:    com.podbenchmark/podbenchmark
```

## Why This Matters for Operators

Print-on-demand margins are decided before a single order ships. The same unisex tee is a different base cost at Printful, Printify, Gelato, CustomCat, Prodigi, Inkthreadable and Fourthwall, and the gap widens again by size, colour and destination because shipping is folded into the price differently at each supplier. Most sellers settle this with a spreadsheet that is stale the week it is finished, or with whichever supplier they signed up with first.

An assistant holding a normalized supplier catalog answers the comparison inside the conversation where the product decision is being made, and answers it with the delivered number rather than the base number.

## What It Actually Does

`initialize` returned HTTP 200 as `podbenchmark` 1.0.0 on protocol 2025-06-18, advertising tools with `listChanged` and resources. `tools/list` returned **10 tools** with full JSON input schemas.

Two calls were executed against the live endpoint:

- `list_suppliers` returned `ok: true` with seven suppliers, each carrying an id, a name, a type field and its vendor page: `customcat`, `fourthwall` (type `direct`), `gelato`, `inkthreadable` (type `direct`), `printful`, `printify` and `prodigi`.
- `list_categories` returned `ok: true`, `destination: "US"`, `currency: "USD"`, and per-category product counts with starting delivered prices: Apparel 1,971 products of which 1,722 priced across 6 suppliers from $11.33, T-Shirts 457 products with 389 priced from $12.08, Hoodies 277 products with 232 priced from $12.08 and above.

| Tool | What it answers |
|---|---|
| `search_products` | Find a POD product across suppliers by category, type or keyword |
| `list_categories` | Categories with product counts and starting delivered prices |
| `get_product` | Specs, fabric, fit, print methods, similar products |
| `get_product_options` | Supplier pricing for one product in a specific size or colour |
| `compare_product` | Which supplier costs less for one product, with the delivered price |
| `resolve_supplier_link` | Paste a supplier URL from Printify, Printful, Gelato, Prodigi, CustomCat, Fourthwall or Inkthreadable and get the normalized product |
| `list_suppliers` | The supplier set being compared, with type and site |
| `get_supplier` | A supplier's plans, monthly fees, branding, checkout model, support |
| `get_supplier_prices` | A supplier's price position overall, by category, or against one other supplier |
| `supplier_guide` | Choosing a supplier for t-shirts, hoodies, mugs, wall art, stickers or phone cases |

`compare_product` requires a `canonicalProductId` with a destination and currency, which is where a malformed call is caught: passing a free-text query returned an input validation error naming the three required fields rather than a guess. That is the right failure shape for a pricing tool.

## Limitations Recorded

- The catalog is normalized by the vendor, so a wrong normalization becomes a wrong comparison that looks authoritative.
- Prices are US-destination and USD by default; other destinations and currencies are parameters, and the guide does not assume them equal.
- The product count is the vendor's, not independently verified; 1,722 of 1,971 apparel products carry a price, so roughly one in eight has no comparable number.
- Payment and shipping terms, tax and returns are outside the server: this compares cost, not landed obligation.
- The free tier has a per-IP rate limit of 120 requests a minute with no key to raise it.

## FAQ

### Is this the same as quoting from the supplier dashboards?
No. The supplier dashboards show your own account's catalog and your own agreed pricing. This is a cross-supplier comparison surface with a single normalized product identity, which is what makes a like-for-like answer possible at all.

### Can the assistant place an order?
No. The server is read-only and has no order, payment or account tools.

### Does it replace a costing spreadsheet?
It replaces the price column. Volume tiers, transaction fees, platform fees and returns still belong in your own model.

## See Also

- [Print-on-demand in the external catalog](/hermes/mcp/servers/external/)
- [Shopify and storefront connectors in CorpusIQ](/hermes/mcp/)
