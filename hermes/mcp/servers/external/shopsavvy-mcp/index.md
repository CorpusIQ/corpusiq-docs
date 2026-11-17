---
title: "ShopSavvy MCP - Product Prices Across Retailers"
description: "Keyless product data over Streamable HTTP: look up a barcode, compare offers across 25 retailers, read price history and schedule re-checks."
category: "Commerce / Pricing"
stars: "n/a (hosted, keyless for reads; fifteen tools, three driven)"
added: 2026-11-17
source: "the mcp.so submission queue #7496 filed 2026-11-17T06:22:49Z and a driven session on 2026-11-17 in which initialize, tools/list and three tools/call requests answered anonymously on https://api.shopsavvy.com/mcp"
relevance: ★★★
tags: [product-pricing, price-history, retail, price-monitoring, barcode, keyless, remote, mcp]
last_updated: "2026-11-17"
---

# ShopSavvy MCP

**Two retailers can sell the same barcode at prices a hundred dollars apart, and no single storefront will tell you that.** Price comparison is only useful when it is attached to a stable product identity: a barcode, an ASIN, a model number. ShopSavvy's catalogue is built on exactly that identity, so a question like *what does this cost anywhere* becomes answerable from one identifier instead of from a search across tabs.

The server is keyless for reads, enumerates **fifteen** tools with read-only annotations, and answers in the assistant's own text rather than in a table the client must render. Three calls were driven this pass and the answers are checkable line by line.

```
Server type:   remote Streamable HTTP, stateless (no Mcp-Session-Id issued)
Endpoint:      https://api.shopsavvy.com/mcp
Server:        shopsavvy, version 2.0.0, title "ShopSavvy"
Protocol:      2025-06-18
Auth:          none for reads; a key is required for scheduled re-checks and usage reporting
Tools:         15 (annotated read-only or account-scoped)
Repository:    github.com/shopsavvy/shopsavvy-mcp-server
Listed on:     mcp.so submission queue #7496
```

## The evidence tier

**Keyless and driven.** `initialize` answered **200** as *shopsavvy* **2.0.0** on protocol **2025-06-18** with no session identifier and no credential, and `tools/list` returned **fifteen** tools, most carrying `readOnlyHint: true`. Three were called:

- `product_search` on *instant pot duo 6 quart* answered **20 of 72 total matches** with brand, category path, barcode, ASIN and a relevance score on each row, which is how a product identity is obtained in the first place.
- `product_offers` on barcode **853084004088** answered **25 offers checked in the last 90 days**, lowest first, from **$38.22** at Truegether (used) through **$44.99** at BUYA.COM to **$45.00** at two storefronts, each with availability, condition, seller and a last-checked timestamp.
- `product_price_history` for 2026-11-01 to 2026-11-16 answered a per-retailer series: **Walmart at $142.98** and **$143.10** on 11/15, and **Crate & Barrel at $89.99** on the same day for the same barcode.

That spread is the product. A buyer asking whether $142 is a good price gets an answer with a second retailer named, and a seller asking where they sit gets the same list from the other side.

**Two defects are recorded rather than smoothed.** The history answer lists several dozen retailers whose rows read *No historical data available*, including a handful of storefront names that look like catalogue noise rather than shops, and Walmart appears twice with two prices a few cents apart. A reader who takes the retailer count as evidence of coverage will overread it; the price points themselves are the part that reconciles.

## Tools & Capabilities

| Tool | Required arguments | What it answers |
|---|---|---|
| `product_lookup` | `identifier` | One product record: title, brand, model, MPN, barcode, ASIN, ShopSavvy ID |
| `product_lookup_batch` | `identifiers` | The same, for a comma-separated list of barcodes, ASINs, URLs or model numbers |
| `product_search` | `query` | Ranked catalogue matches with brand, category path and identifiers |
| `product_offers` | `identifier` | Current prices at every retailer with an offer, lowest first |
| `product_offers_retailer` | `identifier`, `retailer` | The same, at one domain such as amazon.com or bestbuy.com |
| `product_price_history` | `identifier`, `start_date`, `end_date` | Recorded prices per retailer over a window that ends today or earlier |
| `product_schedule` | `identifiers`, `schedule` | Hourly, daily or weekly automatic re-checks on the key's account |
| `product_unschedule` | `identifiers` | Stops those re-checks |
| `scheduled_products_list` | none | The watchlist, grouped by frequency |
| `api_usage` | none | Credits used, monthly limit, remaining, reset date |
| `content_best_picks` | `query` | Published best-of buying guides for a category |
| `content_tldr_review` | none | A short review summary with a score out of ten |
| `content_qa_answers` | `identifier` | Published answers to common questions about a product |
| `content_buying_guide` | `query` | When-to-buy guidance by category or brand |
| `universal_search` | `query` | Category search with pre-computed rankings |

Reads are keyless. Scheduling, the watchlist and credit accounting sit behind an API key, which is the same shape the vendor's own MCP repository documents.

## Installation

```sh
claude mcp add shopsavvy --transport http https://api.shopsavvy.com/mcp
```

The submitter's listing names an SSE route at `/mcp/sse`; that path answers **404** to a POST, while `/mcp` answers the JSON-RPC handshake directly. Use the bare `/mcp` address.

## Why This Matters for Operators

Retail pricing decisions fail in two directions: buying at a price that another retailer undercuts, and pricing a product above a competitor the seller never checked. Both need the same primitive, a barcode resolving to every current offer plus its history. `product_schedule` turns that from a lookup into a watchlist, and `product_lookup_batch` makes a purchase order or a competitor set checkable in one call rather than one call per item.

## Questions operators ask

### Is the pricing data live or cached?

Cached with timestamps. Each offer carries its own *last checked* time, and the offers call reports how many were checked in the last ninety days, so an agent can say how stale an answer is instead of implying it is current.

### Can it watch prices over time?

Yes, on a key: `product_schedule` sets hourly, daily or weekly re-checks and `scheduled_products_list` reads the watchlist back. Without a key the history tool still answers, from ShopSavvy's recorded points rather than from a schedule you own.

### What is the coverage limit?

The search answered **72** matches for a common kitchen appliance, which is a curated catalogue rather than the whole web. Niche or private-label items may not resolve, and `product_lookup` is the honest test before any workflow depends on one.

## Related

- [SpendCanary MCP](/hermes/mcp/servers/external/spendcanary-mcp) - the advertising side of the same margin question
- [Vizbl MCP](/hermes/mcp/servers/external/vizbl-mcp) - the product-page side of ecommerce conversion
- [Shopify Speed Check MCP](/hermes/mcp/servers/external/shopify-speed-check-mcp) - storefront performance for the same catalogue
