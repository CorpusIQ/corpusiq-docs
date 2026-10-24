---
title: "ShopTrueProfit MCP - Marketplace Fee Math for Sellers"
description: "Itemised Etsy, eBay and Amazon FBA fees, profit, margin, break-even and target price."
category: Commerce & E-Commerce
stars: 0 (github.com/PravinrajV/shoptrueprofit-fee-mcp, MIT, created 2026-10-17)
added: 2026-10-23
source: "chatmcp/mcpso submission #6011 (2026-10-24T03:38Z), the official MCP registry entry io.github.PravinrajV/shoptrueprofit-fee-mcp 1.0.0, and a local build of the open-source package driven with five real tool calls"
relevance: ★★★
tags: [ecommerce, marketplace-fees, unit-economics, profit-margin, etsy, ebay, amazon-fba, pricing, deterministic, stdio-mcp, open-source, remote-mcp]
---

# ShopTrueProfit MCP

**Every seller knows the price and the unit cost. Almost none can say what the marketplace actually takes, and the answer changes by category, by shipping weight, by the day of the year, and by which of three marketplaces the same product is listed on.**

```
Server type: Local (stdio, or Streamable HTTP from the same build) and hosted on Apify Standby
Auth: None for the local build; an Apify API token (Authorization: Bearer) for the hosted endpoint
Live check: hosted endpoint https://mcp.apify.com/?tools=vncntlabs/shoptrueprofit-fee-mcp returned HTTP 401 {"error":"invalid_token","error_description":"Missing or invalid access token. Pass an Apify API token in the Authorization: Bearer header."}
Local build: cloned the MIT repository, npm install, npm run build, PORT=3311 node dist/http.js, POST initialize returned HTTP 200 with serverInfo shoptrueprofit-fee-mcp 1.0.0 on protocol 2025-06-18 and tools/list returned 13 tools
Tools: 13, all read-only arithmetic over published fee schedules (no logins, no scraping, nothing stored)
Pricing: pay per event on Apify, one fee-calculation event per successful calculation; the list_* lookups and rejected inputs are free; the local build is free and offline
Vendor: ShopTrueProfit (shoptrueprofit.com)
```

## Why This Matters for Operators

Ask an e-commerce operator what a product makes them and the answer is usually a price minus a supplier invoice. The part in between is the marketplace, and it is not one number. eBay takes a final value fee that changes with the category and with the portion of the sale above $7,500, charges a per-order fee that steps at $10, charges promoted-listing rates the seller sets, and prices its international and performance surcharges on the seller's own record. Etsy takes a listing fee per unit, a transaction fee on items plus shipping, payment processing that varies by the seller's region and is charged on the customer's sales tax too, and Offsite Ads up to 15% capped at $100. Amazon takes a referral percentage by category with a floor, a closing fee in some categories, a per-item fee on the individual plan, and an FBA fulfilment fee that depends on dimensional weight and on whether the ship date falls inside the peak window that runs from October 15 to January 14, plus a 3.5% fuel and logistics surcharge on top.

Any of those can turn a product the operator believes makes 30% into one that makes 9%. The arithmetic is public, it is just spread across three help centres, revised on different dates, and never assembled in the same place.

This entry is the assembly. It is the first surface in this catalog that answers the per-unit economics question across marketplaces rather than inside one of them, and the answer arrives itemised: each fee line carries the rule that produced it, the sale total it was applied to, the fee-table version and the date that table was checked against the official page, plus a link to the seller-facing calculator the same engine drives.

## What It Actually Does

Thirteen tools, four shapes.

| Shape | Tools | What comes back |
|---|---|---|
| Fees for one order | `etsy_fees`, `ebay_fees`, `amazon_fees` | Every fee line with its basis, the total and its percentage of revenue, the assumptions applied |
| Profit for one order | `etsy_profit`, `ebay_profit`, `amazon_profit` | Fees, costs, profit, margin percentage and the break-even price per unit |
| Price for a target margin | `etsy_target_price`, `ebay_target_price`, `amazon_target_price` | The lowest price that breaks even and the lowest that reaches a stated margin, rounded up to the cent |
| Reference and comparison | `compare_marketplaces`, `list_ebay_categories`, `list_amazon_categories`, `list_etsy_regions` | The same product priced on all three, ranked by profit; 11 eBay fee categories, 37 Amazon referral categories, 12 Etsy Payments regions |

The reference lookups are free and worth knowing: `list_ebay_categories` returned `count: 11` with the seller-performance surcharge options and the per-order fee rule, `list_amazon_categories` returned `count: 37` with referral rates, minimums and size tiers, and `list_etsy_regions` returned `count: 12` with each region's processing rate, flat fee and currency.

## Worked Calls

Five calls against the local build, all real, all reproducible from a fresh clone.

**1. The eBay case, straight from the vendor's own README.** `ebay_profit` with `price 25`, `shipping_charged 5`, `item_cost 8`, `shipping_label_cost 4`, `promoted_listings_pct 5`:

> eBay profit $12.02 on $30.00 revenue (40.07% margin) after $5.98 fees and $12.00 costs. Break-even price $10.24 per unit.

Three fee lines carried their basis: final value fee $4.08 at "13.6% on the portion up to $7,500; 2.35% on the portion over $7,500 (per item, on the total amount of the sale incl. shipping and tax)", per-order fee $0.40 because "order total $30.00 > $10", promoted listings $1.50 as "5% of $30.00". The arithmetic checks by hand: 13.6% of $30.00 is $4.08, 5% is $1.50, the three lines sum to $5.98, and $30.00 minus $5.98 minus $12.00 is $12.02, which is 40.07% of $30.00.

**2. The Etsy case, with the fee nobody budgets for.** `etsy_fees` with `price 24.99`, `shipping_charged 5`, `offsite_ads_pct 15`, `region us`:

> Etsy fees on a $29.99 order: $7.80 (26% of revenue).

Listing $0.20 (one unit), transaction $1.95 at 6.5% of $29.99, payment processing $1.15 at "3% of $29.99 + 0.25 USD", Offsite Ads $4.50 at "15% of $29.99, max 100 per order". Offsite Ads is the line that decides whether a product is viable: an order that arrives from an Offsite Ad pays 15% of the whole order on top of everything else, and the seller does not choose which orders those are.

**3. The Amazon FBA case, with a peak-season ship date.** `amazon_fees` with `price 29.99`, `category home-kitchen`, `fulfillment fba`, `10 x 8 x 4` inches, `1.5 lb`, `ship_date 2026-11-20`:

> Amazon FBA fees on a $29.99 sale: $11.66 (38.89% of revenue).

Referral fee $4.50 at "Home and Kitchen: 15% of the total sales price; minimum $0.30 per unit", closing fee $0.00 in this category, per-item fee $0.00 on the professional plan, FBA fulfilment $6.49 at "Large standard, 2.3 lb shipping weight, peak standard card", fuel and logistics surcharge $0.23. Two things are worth noticing. The $6.49 is priced on 2.3 lb rather than the 1.5 lb the seller entered, because 10 x 8 x 4 inches is 320 cubic inches and dimensional weight beats actual weight. And the surcharge appears only because the ship date falls inside the peak window, which is exactly the kind of line a spreadsheet misses.

**4. The comparison.** `compare_marketplaces` with `price 34.99`, `item_cost 9`, `shipping_label_cost 4.5`, `shipping_charged 5`, `target_margin_pct 30`, Amazon as `home-kitchen` FBA:

> Etsy pays the most for a $34.99 item: Etsy $22.24 (55.62%), eBay $20.65 (51.64%), Amazon $13.58 (38.8%).

| Marketplace | Revenue | Fees | Costs | Profit | Margin | Break-even | Price for 30% |
|---|---|---|---|---|---|---|---|
| Etsy | $39.99 | $4.25 | $13.50 | $22.24 | 55.62% | $10.42 | $18.06 |
| eBay | $39.99 | $5.84 | $13.50 | $20.65 | 51.64% | $11.09 | $19.65 |
| Amazon FBA | $34.99 | $12.41 | $13.50 | $13.58 | 38.80% | see call | see call |

The Amazon revenue is $34.99 rather than $39.99 because FBA shipping is set by Amazon, not by the seller, so the $5 the buyer would have paid on the other two never arrives. That single structural difference plus the fulfilment fee is the whole 17-point margin gap.

**5. The target-price solve.** `amazon_target_price` with `category home-kitchen`, `fulfillment fba`, `target_margin_pct 30`, `item_cost 9`:

> Amazon FBA: list at $29.39 for a 30% margin; break-even $19.02.

At $29.39: revenue $29.39, fees $11.57, costs $9.00, profit $8.82, margin 30.00%. The solve is not a straight division, because the referral percentage and the fulfilment band both move as the price moves, so the tool searches for the lowest price that clears the target.

## Installation

Local, from source, with no account and no network:

```bash
git clone https://github.com/PravinrajV/shoptrueprofit-fee-mcp.git
cd shoptrueprofit-fee-mcp
npm install && npm run build
node dist/stdio.js                 # stdio for a desktop client
PORT=3311 node dist/http.js        # Streamable HTTP at http://127.0.0.1:3311/mcp
```

The vendor also publishes a one-file `.mcpb` bundle on the releases page that opens directly in a desktop client, with no dependencies and no network access.

## Configuration

Local, for Hermes or any client that takes an HTTP MCP server:

```json
{
  "mcpServers": {
    "shoptrueprofit-fees": {
      "type": "http",
      "url": "http://127.0.0.1:3311/mcp"
    }
  }
}
```

Hosted, on Apify Standby, where the URL is the standby endpoint from the actor's Endpoints tab:

```json
{
  "mcpServers": {
    "shoptrueprofit-fees": {
      "type": "streamable-http",
      "url": "https://<standby-url>/mcp",
      "headers": { "Authorization": "Bearer ${APIFY_TOKEN}" }
    }
  }
}
```

## What It Costs

| Path | Price | What you get |
|---|---|---|
| Local build | Free, MIT | 13 tools, offline, no account, nothing stored |
| Apify Standby (hosted MCP) | Pay per event: one `fee-calculation` event per successful calculation | The same 13 tools, plus Apify's small Standby platform usage |
| Apify batch actor | Pay per event, up to 1,000 `{tool, arguments}` calls per run | One dataset item per call with `ok`, `result` or `error`; rejected items are not charged |

The `list_*` lookups are free, and so are rejected inputs, which makes the argument-validation path cheap to test.

## Integration with CorpusIQ

The pairing is a question CorpusIQ cannot answer from the operator's own systems, because none of them hold a fee schedule. CorpusIQ reads the operator's Shopify orders, Stripe charges or Amazon settlement through its own connectors and knows what was charged. This server knows what should have been taken.

The sequence: pull the operator's real orders for a category and a period, take one representative unit per category, and ask what the fee should have been. Where the statement's effective rate and the computed rate disagree beyond a few tenths of a point, the difference is either a fee the operator was not aware of, a category assigned wrong, or a programme they are paying into without knowing. That is the same reconciliation discipline the catalog applies to ad spend, applied to marketplace take-rate.

The second use is forward-looking and cheaper: before a listing goes live, ask which of the three marketplaces clears the target margin at a competitive price. The comparison tool answers it in one call, with the break-even price on each.

## Limitations

- **Three marketplaces, US-centric.** eBay.com US and Amazon.com US only; Etsy covers 12 payment regions for processing rates but the selling fees are Etsy's global schedule. No Walmart, TikTok Shop, Etsy international selling fees, Amazon EU or Amazon CA.
- **The hosted endpoint needs a token.** `POST initialize` on the Apify Standby URL returned HTTP 401 `{"error":"invalid_token"}` without an Apify API token. The drivable path this sweep used is the open-source local build, which needs no credential at all.
- **The strongest accuracy claim is not reproducible from the public repo.** The README states the test suite compares this server's output field by field with the website's own functions on 1,700+ cases, including Amazon's and eBay's own worked examples. In a fresh clone those cross-checks are skipped because they need the private app source: `npm test` on the clone returned 94 passed and 31 skipped, the whole `tests/crosscheck.test.ts` file among the skips. The vendor says so plainly in the README rather than letting a green run imply otherwise, but the claim itself rests on the vendor's word, not on anything a reader can run. What a reader can run does pass: protocol, schemas, distribution, batch and packaging, plus an Apify Standby test on the real SDK.
- **A named list of what is not modelled**, and it matters: eBay Store subscription rates; Etsy Ads cost-per-click, Etsy Plus, currency conversion and the Regulatory Operating Fee; Amazon's low-inventory, inbound placement, returns processing, aged-inventory and storage-utilization surcharges, lithium battery fees, removal and disposal, the Overmax handling fee, and FBA rates after January 14, 2027, which are not published yet and fall back to 2026 non-peak rates with a warning. An operator on the individual Amazon plan, or one paying for a Store subscription, is outside the default assumptions and should read the `assumptions` array before trusting the number.
- **Estimates, not statements.** Every response carries a disclaimer saying the marketplace statement is the final word. This is a planning and reconciliation tool, not a replacement for the settlement report.
- **The fee tables are dated and will age.** eBay and Amazon tables verified 2026-10-16, Etsy 2026-10-13. Each response states the table id and its verification date, and each line carries an `engine_sha256`, so a stale answer is identifiable rather than invisible. It is still stale.
- **A one-week-old repository with no stars.** Created 2026-10-17, last push the same day, 0 stars, MIT. The engineering is real, the track record is not yet. That belongs in the record next to the tool count.

## FAQ

### Do I need an account?

Not for the local build. `git clone`, `npm install`, `npm run build`, run, call: no key, no network, no storage. The hosted Apify path needs an Apify API token, which is why this entry was settled on a local build rather than on the vendor's endpoint.

### Why does a calculator belong in a catalog of data servers?

Because the numbers it holds are the ones operators cannot reproduce. The value is not the addition; it is the fee schedule assembled correctly, dated, and itemised back to the rule and the official page, including the surcharges and the bands a spreadsheet leaves out. The catalog already carries cost-surface entries on this principle - packaging indices, BOM pricing - and marketplace take-rate is the largest missing cost line in the e-commerce group.

### Does it answer "what should I charge?"

Yes, per marketplace: the lowest price that breaks even and the lowest that reaches a stated margin, solved rather than divided, because the bands move with the price. It returns the price with the fees and margin at that price, so the recommendation is checkable.

### Is it safe to run?

The local server is a pure function: no network, no filesystem writes, no credentials, nothing stored. The only data that leaves the machine on the hosted path is the numbers in the tool call.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [PackIndex MCP](/hermes/mcp/servers/external/packindex-mcp)
- [3Dsellers MCP](/hermes/mcp/servers/external/3dsellers-mcp)
- [Nexscope MCP](/hermes/mcp/servers/external/nexscope-mcp)
- [Shopify Speed Check MCP](/hermes/mcp/servers/external/shopify-speed-check-mcp)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
