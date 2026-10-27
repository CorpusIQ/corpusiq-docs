---
title: "FlipProfit MCP - Marketplace Fees to the Cent"
description: "Compare eBay, Poshmark, Mercari, Etsy and nine more resale platforms by real fees and profit for one sale, keyless, with dated fee sources."
category: Finance / E-commerce
stars: n/a (free, keyless; Fee Watch $6 per month)
added: 2026-10-27
source: "live MCP probes on mcp.fliprofit.com/mcp (initialize 200, tools/list 200, three tools, compare_platforms executed and returning 13 ranked platforms), the vendor developer page with its OpenAPI 3.1 spec and llms.txt, and the mcpservers.org listing"
relevance: ★★★
tags: [reseller, marketplace-fees, ebay, poshmark, etsy, profit-margin, pricing, keyless]
last_updated: "2026-10-27"
---

# FlipProfit MCP

**The same item priced at 50 dollars nets 32.50 on one resale platform and 22.50 on another. An agent that does not know which platform it is selling on cannot answer a pricing question honestly.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.fliprofit.com/mcp
Transport:   JSON-RPC over POST
Auth:        none, keyless, read-only, GET only upstream
Tools:       calculate_fees, compare_platforms, get_fee_changes
Platforms:   eBay, Poshmark, Mercari, Whatnot, Depop, Etsy,
             Facebook Marketplace, Amazon, Grailed, Reverb,
             TCGplayer, TikTok Shop, Vinted
Built by:    FlipProfit (fliprofit.com)
Registry:    MCP server card at mcp.fliprofit.com/.well-known/mcp/server-card.json
```

## Why This Matters for Operators

Resale and marketplace sellers price against a fee schedule they did not write and cannot see in one place. eBay takes a final value fee on the item plus shipping, Poshmark takes a flat 20 percent above 15 dollars, Mercari changed its seller fee in 2025, and Etsy adds a listing fee, a transaction fee, a payment processing fee charged on tax as well, and an optional Offsite Ads cut capped at 100 dollars.

A model asked to compute that from memory produces a number that looks right and is wrong. This server is the arithmetic done against the platforms' own published rules, plus a dated log of every change, so a margin answer carries a source instead of a guess.

## What It Actually Does

`initialize` on `https://mcp.fliprofit.com/mcp` returns HTTP 200 with `serverInfo` name `fliprofit-mcp`, title "Fliprofit reseller fee calculator", version 1.2.0. `tools/list` returns three tools:

| Tool | What it answers |
|---|---|
| `calculate_fees` | Fees, payout and profit for one sale on one platform. Required: `platform` and `price`. Optional: `shipCharged`, `taxRate`, `itemCost`, `shipCost`, `otherCost`, plus per-platform `options` for category, seller tier and ad rates. |
| `compare_platforms` | Ranks every platform by profit for the same sale, with the fee, payout, margin and a calculator link per platform. |
| `get_fee_changes` | Dated fee changes, each with the platform's own source URL and the date FlipProfit last verified it. Filters by `platform`, `since`, `upcoming`. |

Executed live with a 50 dollar price, a 10 dollar item cost and 7.50 shipping: Vinted nets 32.50 with no fee, Depop 30.40, TikTok Shop 29.50, Reverb 27.91, Mercari and Facebook Marketplace 27.50, Etsy 27.30, Grailed 27.26, Whatnot 26.75, TCGplayer 25.57, eBay 25.30, Amazon 24.01, Poshmark 22.50. Thirteen platforms, ranked, in one call.

The upstream REST API is documented alongside the MCP surface: `GET /api/v1/fees/<platform>`, `/api/v1/compare`, `/api/v1/fees` for platform options and valid values, and `/api/v1/changes?upcoming=true` for the change log, which is also published as an Atom feed. There is an OpenAPI 3.1 spec and an `llms.txt`.

## The Part That Costs You Something

Nothing here spends money. What it costs is a wrong answer that gets published.

- **The rates are US only.** Every number is in US dollars under US marketplace rules. A UK or EU seller gets a plausible figure that does not apply.
- **Defaults are silent arbitrage.** `compare_platforms` uses each platform's default options, so a category with a higher fee or a seller tier below Top Rated shows the default rate, not yours. Pass `options` on `calculate_fees` before quoting a margin.
- **History is the paid tier.** Fee rules in force on a past date, reminders before a change and a private feed sit behind Fee Watch at 6 dollars a month or 60 a year, with a 600 request per minute key. Everything on the free surface stays free.

## How It Is Contained

- **Keyless by design.** No account, no token, no separate sandbox: the API is free, read-only and CORS open, so there is nothing to leak and nothing to revoke.
- **Errors are typed.** Every 4xx and 5xx is RFC 9457 `application/problem+json` with a stable `code`, so a client surfaces a real error instead of an empty answer.
- **Every result carries its own citation.** Fees come back with the calculator link and, on the change log, the platform's own source, which is what makes the answer checkable rather than trusted.

## Limitations Recorded

- Thirteen platforms are supported and the vendor's key list documents twelve, with Vinted reachable through the live tool description. Expect the counts to drift by one as platforms are added.
- Fees are modelled from published rules; promotional rates, negotiated terms and platform-specific category exceptions are not visible to the API.
- `get_fee_changes` reports changes FlipProfit has verified, not every change every platform has announced.
- Amazon unit economics include fulfilment and referral assumptions that vary by size tier, so treat the Amazon figure as the schedule rate rather than your settlement.

## FAQ

### How do I know the numbers are current?
Each result carries the date FlipProfit last verified the rules and, for changes, the platform's own source URL. The change log is also an Atom feed, so an agent can check whether the schedule moved before quoting.

### Is a comparison across platforms meaningful?
Only with the same inputs. Pass the identical `price`, `itemCost`, `shipCost` and `shipCharged` to `compare_platforms`, then re-run `calculate_fees` with real `options` for the platform you actually intend to use, because defaults understate fees on several of them.

### Does it need a key or an account?
No. Connect the URL and call a tool. There is no sign-up, no token and no sandbox to configure, which also means there is nothing to revoke.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [Seller Profit Doctor MCP - storefront profit math](/hermes/mcp/servers/external/seller-profit-doctor-mcp/)
- [CorpusIQ connectors for commerce data](/hermes/mcp/)
