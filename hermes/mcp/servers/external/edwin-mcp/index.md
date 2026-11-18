---
title: "Edwin MCP - Shopping Prices From Merchant Feeds"
description: "A keyless shopping advisor over affiliate product feeds in five markets, with an import timestamp on every price and a ranking that refuses to guess."
category: "Commerce / Product Data"
stars: "0 (hosted Streamable HTTP at https://thebutler.network/api/mcp, keyless and stateless, six tools, all six driven)"
added: 2026-11-17
source: "the mcp.so submission queue entry 7545 filed 2026-11-18T02:00:46Z, and a driven session on 2026-11-17 in which eleven tools/call requests were run against the live endpoint with no credential"
relevance: ★★
tags: [commerce, shopping, prices, product-data, affiliate-feeds, keyless, remote, mcp]
last_updated: "2026-11-17"
---

# Edwin MCP

**A price is a claim about a moment.** Most shopping tools blur that. They return a number and call it the price. Edwin returns the number with the import timestamp of the feed it came from, and its instructions to the calling model are unusually direct: never call these prices current, live or checked.

That honesty is the whole product. The rest is a competent affiliate-feed catalog across five markets, keyless, with six tools and no account.

```
Server type:   remote Streamable HTTP (hosted, stateless)
Endpoint:      https://thebutler.network/api/mcp
Server:        edwin 0.2.0, protocol 2025-06-18
Auth:          none, no account, no OAuth
Tools:         6
Markets:       DE, AT, CH, NL, FR, GB, US (per the tool schema)
Extension:     io.modelcontextprotocol/ui declared
```

## The evidence tier

Keyless and driven with real offers. `initialize` answered 200 with no credential. `tools/list` returned six tools, each with a JSON schema, and the server advertises the MCP Apps UI extension.

Eleven `tools/call` requests were run, covering four markets and both filter bounds. Ten returned data. One returned a documented empty.

## The tool surface

| Tool | Argument | What it returns |
|---|---|---|
| `search_products` | `query`, `market`, `budget_max`, `min_price`, `limit` | Product matches with merchant count, price range and the cheapest current offer per product, each with a tracked link |
| `get_offers` | `pid`, `market` | Every merchant offer for one product: merchant, price, currency, stock status, source network, import timestamp |
| `compare_products` | `pids` (two to five), `market` | Brand, category, price range, merchant count and best offer side by side |
| `find_alternatives` | product, `market`, optional budget and attributes | Comparable products in the same market |
| `recommend_product` | products or a fresh search | A ranked recommendation with the reason |
| `get_product_text` | product from an earlier result | A short summary and key features |

Every response comes in two parts: a rendered markdown table addressed to the human, and a `structuredContent` object addressed to the model. The markdown carries the presentation rules the vendor wants honoured, which is a tidy way to keep the offer links and the price date intact through an intermediary.

## Prices, with their date attached

A German query for `oled 65 zoll` returned three products. The top match, an LG 65 inch OLED G6, carried a price range of 2,099 to 2,119 EUR across three merchants and a `source_imported_at` of 2026-11-17T22:20Z. `get_offers` on that product returned the three merchant rows: Coolblue at 2,099, Quelle at 2,119 and OTTO at 2,119, all in stock, all from the awin affiliate network, each with its own import time between 14:59Z and 22:20Z.

The spread is the point. Three merchants, two prices, three different import moments, and the tool does not pretend they were sampled together.

Market coverage is real. A GB laptop query returned a Dell Pro 14 at 928.09 GBP matched on exact GTIN with a match score of 1, a Samsung Galaxy Book5 at 829 GBP and a Lenovo ThinkBook at 1,047.67 GBP across two merchants. A US headphone query under 150 USD returned a Marshall Major IV at 139.99 USD sourced through the CJ network.

## The refusal is the feature

A US query for `running shoes` under 100 USD returned **zero** items with `empty_reason: no_match_in_market`, plus a note instructing the calling model to tell the user plainly that nothing suitable was found and not to present other products as matches. A German `dyson staubsauger` query under 50 EUR emptied the same way.

A shopping server that returns nothing when nothing fits is worth more than one that returns a plausible near miss. This one also refuses at the argument layer: `compare_products` called without `market` returned a JSON-RPC error naming the missing argument and the expected ISO 3166-1 alpha-2 shape, instead of an empty result.

## The defect worth knowing before you build on it

`min_price` is not honoured the way `budget_max` is. A German query for `kaffeemaschine` with `min_price: 300` returned, as its first row, a De'Longhi machine at 239 EUR whose own price range tops out at 299 EUR, entirely below the floor. The same call was repeated and returned the same row. Two other rows in that response (311.82 and 338.99) did respect the floor, so the filter appears to be applied to some offers and not to the product-level match.

`budget_max` behaved at both ends in testing: 150 USD accepted a 139.99 USD product and 100 USD returned an empty for shoes, and a 50 EUR cap emptied a vacuum query.

The practical fix on the caller side is to read `price_range.min` from the response rather than trusting the filter. A floor is a request, not a guarantee.

A second quirk: a US headphone search returned the same soundcore Space 2 product twice, with two different `pid` values and two different tracked links, at the same 129.99 USD. Two listings, one product. Deduplicate on brand plus model before you count merchants.

## Why this earns a page

For an operator, the useful part is not "an AI can shop". It is that this is a **structured, timestamped, multi-market price feed an agent can query**, with the affiliate disclosure built into the data rather than around it. Competitive price checks, list-price sanity checks on a supplier quote, and category research across five European markets and the US all become one call instead of five browser sessions.

The affiliate model is disclosed plainly: the offer links are tracked, and the source network (awin, cj) is a field on every offer. Anyone building on it should assume the merchant set is the merchant set those networks carry, which is why some queries empty out.

## Installation

```json
{
  "mcpServers": {
    "edwin": {
      "url": "https://thebutler.network/api/mcp"
    }
  }
}
```

No key, no account, no OAuth. The transport is stateless, so no session id needs to survive between calls.

## Configuration

Two rules make the difference between useful results and empty ones:

- **Write the product-type word in the language of the market's merchants.** German for DE, AT and CH, Dutch for NL, French for FR, English for GB and US. The schema says this and the tests bear it out: `fernseher` works in DE where `tv` finds little, and `kaffeemaschine` finds German machines while an English category word does not.
- **Keep brand and model names exactly as the user wrote them.** Matching runs on identifiers first, so a translated brand name costs you the exact-GTIN tier.

## Limitations

- Prices are feed snapshots with an import timestamp. They are not a live quote and the vendor's own instructions forbid describing them as current.
- The merchant list is the affiliate networks' catalogue, so a category a network does not carry returns an empty rather than a partial list.
- `min_price` is unreliable; verify against the returned price range.
- Duplicate product rows exist for at least one product family, so merchant counts can double count.

## FAQ

### Does Edwin MCP require an API key or account?

No. It answered `initialize`, `tools/list` and eleven `tools/call` requests with no credential and no account, and states plainly that it needs none.

### Are the prices live?

No, and the server says so itself. Every offer carries a `source_imported_at` timestamp and the response instructs the calling model never to describe the price as current, live or checked. Quote the date with the price.

### Why does a search return nothing?

Two reasons appear in the data: the query's product-type word is not in the market's merchant language, or nothing in that market fits the request. The empty comes back with a reason field and an instruction not to substitute other products.

### Which markets are covered?

Germany, Austria, Switzerland, the Netherlands, France, Great Britain and the US are named in the tool schema. Driving four of them returned offers in each.

## See Also

- [Cotlet MCP - The Apps That Have No API](/hermes/mcp/servers/external/cotlet-mcp/)
- [Spark Inventory MCP - Stock, Forecasts and Draft POs](/hermes/mcp/servers/external/spark-inventory-mcp/)
- [Laplace MCP - Korean Ecommerce Analytics in Chat](/hermes/mcp/servers/external/laplace-mcp/)
