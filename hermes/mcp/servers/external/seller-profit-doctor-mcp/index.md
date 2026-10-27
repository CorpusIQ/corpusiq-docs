---
title: "Seller Profit Doctor MCP - Storefront Profit Math"
description: "Sixteen keyless tools that price Etsy, Shopify and Amazon fees, break-even ad spend and target-margin pricing, each with dated rate sources."
category: Finance / E-commerce
stars: n/a (free tools; paid report on a separate server)
added: 2026-10-27
source: "live MCP probes on sellerprofitdoctor.com/api/mcp (initialize 200, tools/list 200, sixteen tools), the vendor AI assistants page with per-tool documentation, and the official MCP registry entry com.sellerprofitdoctor/free-tools"
relevance: ★★★
tags: [etsy, shopify, amazon, seller-fees, break-even, roas, pricing, keyless]
last_updated: "2026-10-27"
---

# Seller Profit Doctor MCP

**Storefront economics are three platforms pretending to be one. Etsy charges a listing fee per item, Shopify charges a plan plus payment processing per order, and Amazon charges a referral fee plus fulfilment per unit. An operator running two of the three is comparing numbers that were never computed the same way.**

```
Server type: Remote (Streamable HTTP, SSE responses)
Endpoint:    https://sellerprofitdoctor.com/api/mcp
Transport:   JSON-RPC over POST
Auth:        none on the free tools, no sign-in, nothing stored
Tools:       16, listed below
Platforms:   Etsy, Shopify, Amazon (US rates)
Built by:    Seller Profit Doctor (sellerprofitdoctor.com)
Registry:    com.sellerprofitdoctor/free-tools
```

## Why This Matters for Operators

The question a seller actually asks is not what the fee is. It is whether the price covers the fee, whether the ad spend pays for itself, and whether the discount just moved money from the margin column to the volume column.

This server answers those as separate, checkable calls rather than one confident paragraph: fees on one sale, the profit that sale leaves, the ROAS at which ads break even, the price that holds a target margin, and how many extra orders a sale needs just to keep the same monthly profit.

## What It Actually Does

`initialize` on `https://sellerprofitdoctor.com/api/mcp` returns HTTP 200 as `sellerprofitdoctor-free-tools` version 1.5.0, titled "Seller Profit Doctor free profit tools". The live `tools/list` returns sixteen tools, one more than the vendor page documents:

| Tool | Question it answers |
|---|---|
| `sellerprofit_checkup` | Full profit check-up for an Etsy shop, Shopify store or Amazon seller, with a grade word and level 1 to 5. |
| `sellerprofit_etsy_fees` | Etsy's fees on one sale, line by line, including payment processing on tax and Offsite Ads. |
| `sellerprofit_etsy_profit` | What one Etsy sale leaves after every fee. |
| `sellerprofit_offsite_ads` | What Etsy Offsite Ads cost per order and per month, and the price that covers the fee. |
| `sellerprofit_shipping_gap` | What label and packaging cost beyond what the buyer paid for shipping. |
| `sellerprofit_ads_breakeven` | The ROAS at which Etsy Ads pay for themselves. |
| `sellerprofit_price_for_margin` | The item price that keeps a target profit after fees. |
| `sellerprofit_sale_breakeven` | How many more orders a sale or coupon needs to hold the same monthly profit. |
| `sellerprofit_compare_fees` | The fees on one sale across all three platforms, side by side. |
| `sellerprofit_ads_roas_breakeven` | Break-even ROAS as Meta or Google reports it. |
| `sellerprofit_box_billing` | Billable weight with USPS, UPS and FedEx dimensional rules. |
| `sellerprofit_shopify_plan_fit` | Which Shopify plan costs least at a store's card volume. |
| `sellerprofit_shopify_order_fees` | Every fee on one Shopify order, line by line. |
| `sellerprofit_amazon_fees` | Amazon's fees on one unit at a price, by category referral rate plus fulfilment. |
| `sellerprofit_amazon_ads_breakeven` | The ACoS at which Sponsored Products break even. |
| `sellerprofit_rates` | The fee table and rules the server's numbers use, with sources. |

Every result lists the defaults it used, so a partial answer is still auditable, and Amazon fulfilment, storage and returns figures carry `estimate: true` and sit outside the loss total because they depend on the size and stock Amazon measures.

## The Part That Costs You Something

The free server returns numbers, not reports. The paid surface is a separate endpoint that writes the full report for a seller, and keeping it on a different address is the right shape: an assistant wired to the free tools cannot run up a bill by being helpful.

- **US rates only.** Amazon and Shopify figures are US schedule rates.
- **Amazon estimates are labelled, not exact.** Size tier, storage volume and returns are measured by Amazon, so the server marks those as estimated and excludes them from the loss total.
- **Fixes carry a conditional value.** Each fix states a dollar value that holds if orders hold, and the vendor says to say it that way. An assistant that drops the condition turns a model into a promise.

## How It Is Contained

- **No sign-in, nothing stored.** Inputs are numbers, results are computed by fixed formulas, and no AI computes a number, which removes the class of error that makes a profit answer untrustworthy.
- **Sources travel with the result.** Each result carries the date of the rates and their sources, so a fee figure can be checked against the platform's own page.
- **Grade has an honest empty state.** With too few answers there is no grade yet, and `grade.missing` lists what to ask, so the agent asks instead of guessing.

## Limitations Recorded

- The vendor page documents fifteen free tools; the live `tools/list` returns sixteen.
- Etsy is the default platform, so a Shopify or Amazon question must set `platform` explicitly or it will be answered on the wrong fee schedule.
- Amazon fulfilment and storage rates are 2026 rates and remain estimates; point the seller at Fee Preview for the settled number.
- Offsite Ads share defaults to 10 percent, the figure Etsy gave at launch in 2020, when the seller does not know it, and the server flags that default.

## FAQ

### Is this the same thing as a marketplace fee calculator?
No. FlipProfit prices a sale across thirteen resale marketplaces. This server prices a storefront across three platforms and then answers the second question, which is whether the ad spend, the discount and the box size leave anything behind.

### Can it run someone else's store data?
It runs on what you type. It does not connect to a shop, read orders or store anything, so the answer is as good as the numbers the seller gives and every result lists which defaults it filled in.

### What should I test first?
One real order on the platform the seller actually uses, with `options` set from their real account tier, then the same order through `sellerprofit_sale_breakeven` to see what a 10 percent discount actually costs them.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [FlipProfit MCP - marketplace fees to the cent](/hermes/mcp/servers/external/fliprofit-mcp/)
- [CorpusIQ connectors for commerce and finance data](/hermes/mcp/)
