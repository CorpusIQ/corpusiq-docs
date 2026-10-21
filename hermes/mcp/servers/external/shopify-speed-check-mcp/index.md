---
title: "Shopify Speed Check MCP - Store Speed and Plan Fees"
description: "A free keyless MCP server that tests a Shopify store's speed, names the apps and scripts slowing it down, and models Shopify plan costs."
category: Commerce & Retail
stars: n/a (hosted service, no public repo)
added: 2026-10-21
source: "mcp.so /feed page 1 (card shopify-speed-check, posted 17:16Z)"
relevance: ★★★
tags: [shopify, ecommerce, web-performance, core-web-vitals, pagespeed, merchant-economics, remote-mcp, keyless]
---

# Shopify Speed Check MCP

**A slow store is a checkout problem, and the first question is always which app did it. This server answers that against a public URL, and prices the plan decision that sits underneath it, with no key and no account.**

```
Server type: Remote (Streamable HTTP)
Endpoint: https://tools.skaidigital.com/mcp
Auth: none, no API key needed
Live check: unauthenticated POST initialize returned HTTP 200 (serverInfo skai-shopify-tools 1.0.0, protocol 2025-06-18) and tools/list returned 3 tools
Vendor: Skai Digital (skaidigital.com), a headless Shopify agency
```

## Why This Matters for Operators

A merchant with a slow storefront is usually looking at a dashboard of green dots and a mobile load time of six seconds. The useful answer is not a score, it is a ranked list of what is responsible, attributed to the apps and scripts the merchant is already paying for. That is a decision about subscription spend and theme work, and it can be made from outside the store with nothing but the public URL.

The second question underneath it is plan economics. Basic, Grow, Advanced and Plus differ by more than a monthly fee: the card rate moves with the plan, and so do the features that stop being optional as a brand grows. A break-even number converts that into a decision instead of a comparison table.

## What It Actually Does

- `check_shopify_store_speed` runs Google PageSpeed Insights on mobile and desktop together with real-user Core Web Vitals, returns the bottlenecks ranked, and labels a headless estimate with its assumptions. A run takes 10 to 90 seconds and results are cached for 24 hours, so a repeat question does not spend another minute.
- `detect_shopify_store` reads only the public page and reports whether the site is a Shopify theme store or an already headless storefront, and which theme it uses. It runs no speed test and costs seconds, which makes it the right first call before a slower one.
- `calculate_shopify_fees` compares Basic, Grow, Advanced and Plus for a monthly sales volume and payment mix, and returns break-even sales between consecutive plans plus the requirements only Plus covers. Shopify's published US prices are used, and because the variable Plus platform fee is not published, the tool takes `plusQuoteMonthly` when the merchant has a quote.

Live calls against the running endpoint, this sweep:

```
detect_shopify_store url=https://www.allbirds.com
  platform: shopify_theme, theme: allbirds-theme
  signals: powered-by Shopify header, Shopify.theme allbirds-theme,
           Shopify theme globals in the page, /cart.js returns a Shopify cart

calculate_shopify_fees monthlyGmv=250000, averageOrderValue=85, billing=yearly
  Basic     $8,436/month   ($101,236/year)  does not meet: staff
  Grow      $7,996/month   ($95,956/year)
  Advanced  $7,766/month   ($93,196/year)   cheapest plan that meets the requirements
  Plus      $9,107/month   ($109,288/year)
  break-even: basic to grow $30,000/month, grow to advanced $135,000/month,
              advanced to plus $808,750/month in online sales
  prices checked 2026-10-21 (US), Plus variable platform fee excluded
```

Note the shape of the answer: at that volume Advanced is cheaper than Basic, because the card rate falls faster than the subscription rises, and Basic is excluded by staff account limits rather than by price. That is the kind of conclusion a comparison table does not surface.

## Installation

```
claude mcp add shopify-speed-check --transport http https://tools.skaidigital.com/mcp
```

Any MCP client that speaks Streamable HTTP can connect with the same URL. No OAuth flow, no key, nothing to install.

## Limits Worth Knowing

- This is an audit and calculator surface, not a Shopify data connector. It reads public pages and does arithmetic. Orders, products, customers and inventory are not here; those live in a Shopify connector.
- The bottleneck list is derived from public page and Lighthouse data. It names apps and scripts it can see in the delivered page and the requests it makes, not the ones configured but inactive.
- The headless estimate is explicitly an estimate and its assumptions are returned with the number. Treat it as a range, not a quote.
- US plan prices only, checked 2026-10-21, and the Plus variable platform fee is excluded unless a quote is supplied.
- The vendor is an agency that sells headless storefront work, and the tool responses link to its service and calculator pages. Read the numbers, ignore the pitch.

## Pricing

Free. No key, no account, no usage cap published in the tool schemas.

## FAQ

### Does this need a Shopify account or admin access?
No. Both the speed check and the store detection work from the public URL, and the fee calculator works from numbers the operator types. Nothing is installed on the store and no Shopify credentials are involved.

### Is this a replacement for the Shopify connector in CorpusIQ?
No, and the two answer different questions. A Shopify connector reads the store's own records, orders and catalogue. This server looks at the store from outside as a visitor and a crawler would, which is the only view that shows what a customer actually waits for.

### Why does the fee comparison use break-even sales instead of a cheapest plan?
Because the cheapest plan changes with volume and with requirements. The tool returns the total cost for each plan at the volume given, names the requirements a plan fails to meet, and gives the sales figure at which moving up pays for itself. The decision is made at the merchant's own volume, not at an average.

### Why is the web performance class already in this catalog?
It is, through GTmetrix MCP and Sorank MCP, and both test any URL. What neither does is attribute the cost to the Shopify apps and scripts a merchant pays for, or price the plan decision. The listing is here for the Shopify-specific surface, not for another speed score.

## See Also

- [GTmetrix MCP - Web Performance Testing](/hermes/mcp/servers/external/)
- [ViewsBase MCP - Creator Payouts for Clipping Campaigns](/hermes/mcp/servers/external/viewsbase-mcp/)
- [CorpusIQ Connectors - Shopify](/hermes/mcp/connectors/)
