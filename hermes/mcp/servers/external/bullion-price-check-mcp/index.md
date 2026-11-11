---
title: "Bullion Price Check MCP - Dealer Metal Pricing and Stock"
description: "Twenty-seven read-only tools over live gold and silver spot, dealer asks, melt value, delivered cost, state tax and aging bullion stock"
category: "Business Operations"
stars: "n/a (hosted, keyless, no credential required, free standard tools)"
added: 2026-11-11
source: "the mcp.so submission window for Nov 11, the official registry record com.bullionpricecheck/bullion-price-check through version 2.0.0, and the endpoint itself at https://bullionpricecheck.com/mcp, where a keyless initialize answered 200 as bullion-price-check 2.1.0, tools/list returned 27 tools all annotated readOnlyHint true, and six calls were driven for live prices, premiums, melt value, delivered cost, state tax and a dealer ladder"
relevance: ★★★
tags: [bullion, precious-metals, gold, silver, dealer, inventory, pricing, scrap, sales-tax, read-only, keyless, streamable-http, remote-mcp]
last_updated: "2026-11-11"
---

# Bullion Price Check MCP

**Every metals quote an operator sees is a price that has already been filtered, and the filter is almost never visible.** A dealer screen gives you one number per product; a marketplace gives you a ranking you cannot audit. This server gives you the ladder, the freshness of every rung, the dealers it had to drop and why, and the delivered cost after shipping and card fees. It is the first bullion entry in this catalog and the first pricing surface here whose main product is **the list of what it refused to rank**.

```text
Server type:  Remote (Streamable HTTP)
Endpoint:     https://bullionpricecheck.com/mcp
Auth:         none for discovery or calls; keyless initialize, tools/list and tools/call all 200
Registry:     com.bullionpricecheck/bullion-price-check, newest published record 2.0.0
Served:       serverInfo bullion-price-check 2.1.0 on protocol 2025-06-18
Tools:        27, every one annotated readOnlyHint true
Spot source:  gold-api.com, exposed in the response rather than hidden
```

The registry record and the served version do not agree, and the direction is worth recording: the newest published registry entry is **2.0.0** while `initialize` answers as **2.1.0**, so the endpoint is ahead of its own listing. That is the reverse of the usual drift recorded in this catalog, where a vendor ships a registry version and the service lags it.

## What one call returns

A keyless `get_spot_prices` call at `2026-11-11T15:52Z` returned all three tracked metals with a per-metal timestamp and a freshness block:

```text
gold      4002.80 USD/ozt    128.69 USD/g    updated 2026-11-11T15:52:30Z
silver      52.38 USD/ozt      1.68 USD/g    updated 2026-11-11T15:52:29Z
platinum     1551 USD/ozt     49.87 USD/g    updated 2026-11-11T15:52:32Z
gold/silver ratio  76.42
spot_source        gold-api.com
freshness          spot_age_minutes 70, spot_stale false, thresholds spot 120 / prices 120
```

Two details in that block matter more than the numbers. **Palladium is declared untracked** in the response itself (`palladium_note`), with a sentence saying spot prices and dealer listings cover gold, silver and platinum only, so an assistant asked about palladium has to say it cannot answer rather than substitute a guess. And every price response carries the **age of the data and the threshold it is judged against** (70 minutes old against a 120-minute limit), so a stale quote cannot silently pass as live.

## The dealer ladder, with the exclusions visible

`get_dealer_prices` for the 1 oz Silver Buffalo Round returned six ranked dealers against a melt value of **52.38**, and the spread is the argument:

```text
rank 1  MintBuilder        54.77    +2.39   +4.57%
rank 2  Agate Metals       55.00    +2.62   +5.01%   (Partner)
rank 3  Monument Metals    55.91    +3.53   +6.75%
rank 4  SD Bullion         59.41    +7.03  +13.43%   (Partner)
rank 5  At Cost Metals     59.86    +7.48  +14.29%   (Partner)
rank 6  APMEX              63.16   +10.78  +20.59%
```

One ounce of the same silver round ranges from **4.57 percent to 20.59 percent over melt**, a spread of **8.39 USD** on a 52.38 USD item. The response states the payment basis as `check, ACH or wire`, which is the second half of the story: a card price sits on top of a ladder that is already 15 percent wide.

The three `Partner` labels are the test of the product's central claim. The instruction string says a partner **pays to list, never to rank**, and the ladder proves it on live data: two partners sit at rank 4 and 5 behind two non-partners, and one sits at rank 2 on a premium barely above the leader. A paid label that does not move the ranking is a claim most comparison sites make and few can demonstrate.

The dropped dealers are listed with the reason, and both reasons are operational rather than editorial:

```text
Hero Bullion    out_of_stock      "out of stock (dealer page)"
Kitco (Partner) unavailable       "price is 471 min old (updated 08:01:59Z);
                                   over the 60-min limit for this source"
```

A dealer is excluded for being **out of stock** or for having a **price older than that source's own freshness limit**, not for being expensive, and the check time of each exclusion is printed. This is the difference between a comparison table and a market measurement.

### What the dealer ladder does not include

Shipping and payment fees are **not** in the ladder prices. The response says `single-unit price before shipping`, so a 4.57 percent leader can lose to a 6.75 percent third place once a flat shipping charge and a card surcharge land on a small order. The server ships the tool that answers that question rather than leaving it to arithmetic: `true_cost` in `your_quote` mode took a 3,200 USD unit price, a quantity of 10, a 45 USD shipping charge and a 3.5 percent card fee, and returned **33,165 USD delivered, 3,316.50 USD per unit**, with the fee and the shipping as separate lines. On a ten-ounce order the card surcharge alone is **1,120 USD**, larger than most of the premium differences in the ladder.

## Premiums move, which is why the history exists

The silver Premium Index at the same minute returned, per tracked product, the lowest premium, the dealer median, the number of dealers, and the seven-day context:

```text
90% "Junk" Silver $1 face   low 1.98%  (Monument)  median 6.02%   6 dealers  173 snapshots/7d
1 Kilo Silver Bar           low 2.30%  (MintBuilder) median 7.21% 7 dealers  173 snapshots/7d
100 oz Silver Bar           low 2.87%  (Monument)  median 6.83%   7 dealers  173 snapshots/7d
10 oz Silver Bar            low 3.63%  (MintBuilder) median 7.64% 6 dealers  173 snapshots/7d
1 oz Silver Buffalo Round   low 4.57%  (MintBuilder) median 10.09% 6 dealers  173 snapshots/7d
```

**The median dealer charges roughly two to two and a half times the lowest premium on the same product**, and the one-ounce round is the worst of the five at 4.57 percent against a 10.09 percent median. A buyer who asks "what is a fair premium on a silver round" and gets the median will overpay by five and a half percentage points. The seven-day figures make the same point over time, and the one-ounce round is the case where the current low (4.57) sits well above its own seven-day median (2.76) and minimum (2.05), so the cheapest dealer today is not cheap by the standards of the last week.

`get_price_history` reads the same series from stored hourly snapshots going back to **2026-10-15**, and `premium_history_alerts` evaluates thresholds against it while separating **percentage-point changes from percent changes**, which is the distinction that makes a premium alert correct rather than merely loud.

## Where this stops being a price feed

Eleven of the twenty-seven tools are for the dealer rather than the buyer, and they are the reason this entry is business software instead of a quote page:

`inventory_aging_exposure` values stock lots into aging buckets with carry cost and melt exposure; `restock_plan` computes velocity, turnover and a reorder point from a sales window the caller supplies; `dealer_scrap_intake_quote` prices a counter scrap intake from karat or purity per lot; `buyback_compare` sets firm dealer bids against recorded bids and melt tiers; `dealer_competitor_position` places your own ask among today's tracked asks; `dealer_bid_spread` compares the lowest and median ask against published buyback; `dealer_price_opportunity` looks for unusual premiums and pricing gaps; `dealer_quote_scenarios` runs up to three buy or sell margin scenarios side by side; `dealer_market_report` assembles a morning briefing.

Two of those descriptions are worth quoting because they describe restraint rather than capability. `buyback_compare` **never invents bids and never applies a market-best label to a single dealer**. `fair_offer_check` refuses input rather than approximating it: on a malformed request it returned

```text
{"ok": false, "error": {"code": "INVALID_INPUT",
 "message": "Input failed validation. No partial numeric result was invented.",
 "diagnostics": [{"code": "EXPECTED_OBJECT", "field": "product",
                  "blocks_validity": true, "blocks_eligibility": true}]}}
```

and that refusal is itself a measurement of a defect worth recording: the `product` field is advertised in the schema as a string or an object, and the implementation requires the object form, so a caller following the schema gets a rejection. The refusal is correct behaviour; the schema is looser than the server.

### What does a bullion purchase actually cost in tax?

`bullion_sales_tax` answers per state with the rule text rather than a bare flag. Arizona, a 2,500 USD gold coin purchase:

```text
status: exempt    needs_verification: false    taxed: false
explanation: "Arizona does not charge state sales tax on a $2,500 purchase of gold coins.
Rule: State transaction privilege tax doesn't apply to precious metal bullion or monetized
bullion. City tax can apply to coins sold mainly for collector value."
```

and the response carries the whole map in `covered_states`, where the statuses are not binary: **exempt**, **no_sales_tax**, **partial** (California, Connecticut, Florida) and **taxable** (District of Columbia, Hawaii). A partial state is the case that costs an operator money, because the threshold or the product form decides it, and the tool takes the amount and the product type as arguments rather than assuming them.

## Verified surface

```text
initialize       200, bullion-price-check 2.1.0, protocol 2025-06-18, no session id issued
tools/list       200, 27 tools, all readOnlyHint true
get_spot_prices  200, three metals, per-metal timestamps, freshness block
get_premium_index 200, five silver products with lowest, median, dealer count, 7d context
get_dealer_prices 200, six ranked dealers plus two exclusions with reasons
melt_value       200, 100 g of 14k gold = 1.8755 ozt fine = 7,507.09 USD at spot
true_cost        200, 10 units delivered at 3,316.50 USD each including a card fee
bullion_sales_tax 200, Arizona exempt with rule text and a 51-jurisdiction status table
fair_offer_check 200 with isError true, a schema-versus-implementation mismatch recorded above
```

`melt_value` is worth one line on its own: 100 grams of 14 karat gold computes to purity 0.583333, 1.8755 troy ounces of fine metal, and **7,507.09 USD** at the live spot, with the formula printed and a sentence attached that a buyer usually pays a share of melt and that refiners and pawn shops deduct fees. A scrap counter that quotes melt as an offer is not quoting a price, and the server says so.

## Good for

A bullion dealer or refiner who needs competitor asks, buyback spread, stock aging and a morning report from one endpoint. A jeweller or pawn operator pricing a scrap intake against live spot instead of yesterday's sheet. A manufacturer or investor buying metal who wants the delivered cost rather than the sticker, and who wants to know which of six dealers was dropped from the comparison and why.

Not for: palladium, which is declared out of scope; order placement, since every tool is read-only; or anyone who needs a price for a product outside the **17 tracked coins and bars**, where the ladder has nothing to rank.

## Related in this catalog

- [NuaSense MCP](/hermes/mcp/servers/external/nuasense-mcp/) - the same discipline in a different market: it publishes the price relationships an operator acts on and refuses to publish a number that cannot support a decision.
- [WeGravel MCP](/hermes/mcp/servers/external/wegravel-mcp/) - materials pricing with quantity breaks, where the safety margin and the truck-load threshold are stated instead of buried.
- [PackIndex MCP](/hermes/mcp/servers/external/packindex-mcp/) - RFQ and price comparison for packaging, a purchasing ladder rather than a marketplace.
