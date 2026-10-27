---
title: "JENNi MCP - Local Shelf Availability and Same-Day Checkout"
description: "JENNi answers whether a specific shelf can sell a product to a specific ZIP now, prices the delivery fee, and returns a hosted checkout link."
category: Commerce & E-Commerce
stars: n/a (no public repo)
added: 2026-10-22
source: "mcp.so /feed page 1 (card posted 2026-10-21T10:38:15Z)"
relevance: ★★★
tags: [commerce, local-inventory, same-day-delivery, product-availability, checkout, retail, agentic-commerce, remote-mcp, keyless]
last_updated: "2026-10-24"
---

# JENNi MCP

**The hard question in agentic commerce is not "what does it cost" but "can anyone actually deliver it to this address today" - and JENNi answers that per product, per ZIP, with the fee and a checkout link.**

```
Server type: Remote (Streamable HTTP) at https://shop.jennipro.com/mcp
Auth: none
Live check: POST initialize returned HTTP 200 (serverInfo jenni-shopping 2.0.0, protocol 2025-03-26); tools/list returned 5 tools
Real call 1: search_catalog at ZIP 78205 for "usb-c cable" returned priced products with shelf_observed_at timestamps, local_delivery and checkout eligibility flags, and a delivery promise
Real call 2: get_buying_options on one product at 78205 returned available true, unit price $6.00, delivery fee $9.99, total $15.99 before tax, same-day ETA
Real call 3: the same product at ZIP 85262 returned available false, reason_code no_live_offer
Tools: 5 (search_catalog, get_product, get_buying_options, start_checkout, get_order_status)
Coverage: same-day delivery in San Antonio, Texas, 79 ZIP codes at capture; $9.99 per order; order by 5:00 PM Central, Monday to Saturday
Vendor: JENNi (jennipro.com)
```

## Why This Matters for Operators

Retail data on the web answers the wrong question. A product feed says a shirt exists and costs $28. It does not say whether the shirt is on a shelf that can reach this customer before dinner, and that is the only version of the question a buyer cares about.

This is where agent shopping usually breaks down and why the failure is worse than a wrong price. An agent that reads a product page, reports "available", and hands over a link has promised a delivery it cannot verify. The correction has to happen before the checkout link is produced, not after the order fails.

## What It Actually Does

Five tools, and the split between them is the design.

`search_catalog` takes a five-digit US ZIP and a query and returns candidate products with price, shelf price, image, variant list, and per-offer eligibility flags for both search and checkout, plus `shelf_observed_at` so the agent can say how fresh the observation is. `get_product` returns product facts by `product_id` without exposing source-shop details.

`get_buying_options` is the one that matters. Given a `product_id`, a ZIP, a quantity and a fulfillment mode (`local_delivery` or `ship_to_home`), it returns whether that mode is available for that destination right now, with `reason_code` when it is not, the unit price, the fee line and the total, and an ETA object. `start_checkout` then returns a hosted `checkout_url` for the exact product and mode, with the delivery address supplied; JENNi picks the source internally. `get_order_status` reads where an order stands: status, delivery ETA when known, courier tracking, and whether the card hold was captured.

The server's own instructions are unusually explicit about the sequence, and they are right: never present a national fallback as local, call `get_buying_options` for both modes with the exact `product_id`, offer only verified modes, and quote the total before handing over the link. A search result with no offer is `not_checked`, not unbuyable.

## Installation

```bash
claude mcp add --transport http jenni https://shop.jennipro.com/mcp
```

No key, no account, no OAuth. The endpoint answers anonymously, and the shopping session itself is what carries state.

## Configuration

```json
{
  "mcpServers": {
    "jenni": {
      "type": "http",
      "url": "https://shop.jennipro.com/mcp"
    }
  }
}
```

## What the Two Buying-Options Calls Actually Return

The same product, two ZIPs, at capture time. San Antonio, where the shelf exists:

```json
{
  "fulfillment_mode": "local_delivery",
  "available": true,
  "delivery_promise": "Get it today",
  "unit_price": "$6.00",
  "fee_kind": "local_delivery_fee",
  "fee": "$9.99",
  "eta": {"kind": "same_day"},
  "total": "$15.99",
  "tax": "added_at_checkout"
}
```

A Scottsdale ZIP, where it does not:

```json
{
  "fulfillment_mode": "local_delivery",
  "available": false,
  "reason_code": "no_live_offer",
  "note": "No source can sell this product for that destination right now."
}
```

That second response is the whole point of the entry. A price scraper would have returned the same $6.00 for both, and the agent would have promised a same-day delivery to an address no shelf can reach. The published coverage list at capture was 79 ZIP codes, all in the San Antonio area, so a `search_catalog` hit at an out-of-area ZIP is a candidate rather than a promise until `get_buying_options` confirms it.

## Business Relevance

- **Local and regional retailers** get their shelf inventory exposed to agents with the delivery fee and ETA attached, rather than a generic product feed.
- **Agents acting for buyers** get a verified availability answer and a checkout link instead of a link a human still has to validate.
- **Ecommerce operators** can see what a competitor's local shelf actually holds in a market they care about, at a known observation time.
- **Field and facilities teams** can source a part same-day instead of ordering one that arrives in three days.
- **Research and pricing work** benefits from real shelf prices with timestamps, which is different data from a nationwide list price.

## Integration with CorpusIQ

CorpusIQ is built for the question after the purchase: did the spend land where it should, and what does the margin look like. Connecting a store or accounting connector alongside a shopping server lets an operator ask the two questions in one place, "can we get this today and at what landed cost" and "how does that compare with what we paid last quarter".

The more interesting use is market reading. `search_catalog` and `get_buying_options` across a set of ZIPs produce a live picture of local assortment and shelf pricing, which is exactly the kind of external evidence a pricing or expansion question needs before anyone commits to a number.

## Limitations

- Coverage is one metro at capture: 79 San Antonio ZIP codes, same-day, order by 5:00 PM Central Monday to Saturday. Everywhere else, the useful answer is `ship_to_home` or no offer at all.
- The $9.99 delivery fee is per order, which matters for small baskets: a $6.00 cable becomes $15.99 delivered.
- Prices carry `tax: added_at_checkout`, so the quoted total is not the final charge.
- Inventory is an observation, not a reservation. A shelf can sell out between `search_catalog` and `start_checkout`, which is why `get_buying_options` must be re-run at the moment of purchase.
- New listing with no independent track record, and the catalog is one retailer network rather than the open web, so absence of a product means absence from JENNi, not absence from the market.

## FAQ

### Does it need an API key or an account?

No. `initialize` and `tools/list` answer anonymously, and `search_catalog` returns real priced products without credentials.

### Can I trust the availability flag on a search result?

Not as a promise. The search-level flag says the offer looks eligible; `get_buying_options` is the authoritative check for a specific product and destination, and it is the call that returns `no_live_offer` when nothing can serve that address.

### What does same-day actually mean here?

Order before 5:00 PM Central, Monday to Saturday, and the order is delivered the same day, from a shop in San Antonio that stays open at least an hour past the order-by time by its own verified hours. Later orders go out on the next delivery day.

### Where does the order get paid?

`start_checkout` returns a hosted `checkout_url`. The card hold stays pending until the order is confirmed, and `get_order_status` reports whether that hold was captured.

## See Also

- [BestPrice Shopping MCP](/hermes/mcp/servers/external/bestprice-shopping-mcp)
- [Shop MCP](/hermes/mcp/servers/external/shop-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
