---
title: "CryptoExchangeIn MCP - True Trading Cost and Country Rules"
description: "A keyless MCP server that prices the all-in cost of a crypto trade across eight exchanges by mode, and pairs it with a per-country regulatory matrix for licensing, KYC, tax and bank rails."
category: "Finance / Trading Costs"
stars: "0 (hosted, closed source; 6 tools, keyless, 5 of them driven)"
added: 2026-11-15
source: "the mcp.so submission queue entry #7386 filed 2026-11-15T09:13Z, and a driven session against https://cryptoexchangein.com/mcp on 2026-11-15 in which initialize answered 200 as cryptoexchangein 1.0.0, tools/list returned 6 schemas and 32 cost rows across four modes were checked against their own arithmetic"
relevance: ★★
tags: [crypto, exchange-fees, trading-cost, regulation, kyc, tax, keyless, remote-mcp]
last_updated: "2026-11-15"
---

# CryptoExchangeIn MCP

**The advertised fee is not the cost of the trade.** A spot taker fee of 0.10% is one line of a bill that also contains the spread on an instant card buy, the maker rebate somebody else negotiated, and a country rule that decides whether the money can leave at all. Four exchanges quoting the same 0.10% are not offering the same trade, and a 1.65% instant-buy spread is sixteen times the taker fee on the same platform.

CryptoExchangeIn answers in two pieces and they belong together: a cost calculator that ranks exchanges by all-in cost for a given amount and mode, and a country record that carries the regulator, the tax treatment, the fiat rails and a compatibility matrix. Six tools, no key.

```
Server type:   remote Streamable HTTP, JSON-RPC 2.0, keyless and stateless
Endpoint:      https://cryptoexchangein.com/mcp
Server:        cryptoexchangein, title "CryptoExchangeIn", version 1.0.0
Website:       https://cryptoexchangein.com
Setup docs:    https://cryptoexchangein.com/llms.txt
Auth:          none
Tools:         6 (calculate_trade_cost, get_country, list_providers,
               search_guides, get_guide, report_outdated_info)
Data date:     as_of 2026-11-13 on every response read in this pass
Listed on:     the mcp.so submission queue as #7386
```

## The evidence tier

Driven, not documented. `initialize` answered **200** in 0.30 seconds with no credential and no session identifier, `tools/list` returned **6** schemas, and four tools were called: `calculate_trade_cost` sixteen times across all four modes, five amounts and five country values, `get_country` for India, `list_providers` for exchanges, and nothing was taken from the vendor's own pages. The arithmetic control below is mine: every one of the **32** cost rows returned at a 10,000 dollar amount was recomputed as `amount x rate_pct / 100` and matched to the cent.

## The tool surface

| Tool | Arguments | What it returns |
|---|---|---|
| `calculate_trade_cost` | `amountUsd` (10 to 1,000,000), `mode` (spot_maker, spot_taker, instant_buy, futures_taker), `country` | Exchanges ranked ascending by all-in cost for that mode, with the percentage, the dollar cost, a token-discount note and, on most rows, a referral code and link |
| `get_country` | `slug` | Regulator, tax summary, fiat rails, a per-service matrix with a status per row and a `guide_url` on each, and two written paragraphs: a `summary` and a `quick_take` |
| `list_providers` | `category` (exchange, hardware_wallet, software_wallet, tax_onramp, trading_tool) | Provider records with a fee block (spot maker, spot taker, instant spread, futures taker, KYC tier, supported regions), pricing model, and the referral fields |
| `search_guides` | `q`, `country`, `topic` (fees, availability, wallets, beginners, cash_out) | Matching guides and comparisons, eight results for the query `sanctions` |
| `get_guide` | `path` | One full guide by path |
| `report_outdated_info` | `path`, `field`, `message` | A field report channel for a fee tier, KYC rule, bank rail or withdrawal limit that changed |

## What the calls returned

**The calculator is exact, and the ordering is the product.** At 10,000 dollars, four modes:

| Mode | Cheapest rows | Most expensive | Spread |
|---|---|---|---|
| `spot_taker` | Bitget 0.10% = **$10.00**, Binance 0.10% = $10.00, OKX 0.10% = $10.00, Bybit 0.10% = $10.00 | Coinbase Advanced 0.60% = **$60.00** | **6x** |
| `spot_maker` | OKX 0.08% = **$8.00** | Coinbase Advanced 0.40% = **$40.00** | **5x** |
| `futures_taker` | Binance 0.05% = **$5.00**, OKX 0.05% = $5.00, Kraken Pro 0.05% = $5.00 | Coinbase Advanced 0.10% = **$10.00** | **2x** |
| `instant_buy` | OKX 1.65% = **$165.00** | Coinbase Advanced 3.55% = **$355.00** | **2.2x** |

Two things in that table are worth an operator's attention, and neither is on a fee page. **Mode moves the cost more than exchange does**: the same OKX trade costs **$10.00** as a spot taker and **$165.00** as an instant card buy, a factor of **16.5** for the convenience of paying by card. And **the cheap exchanges are cheap in every mode**: Coinbase Advanced is the most expensive line in all four, which is what a retail-facing spread looks like when it is written down.

Every row was recomputed: `rate_pct x amount / 100` matched `estimated_cost_usd` in **32 of 32** rows at the 10,000 dollar amount, and $1,000 at 0.10% returns $1.00 as expected. The ranking was strictly ascending in all four modes, so this is a sort on cost and not a sort on commission.

**The country filter is where the record is uneven.** Names work: `india` returned **4** exchanges, `us` returned **2**, `uk` returned **4**. ISO codes do not: `IN` is echoed back lowercased as `in` and returns **0** rows with no error and no hint, while `US` happened to work because the lowercase form is the slug. So the argument is a slug, and the schema does not say so.

**India, read as a business question rather than a geography quiz.** `get_country` with `slug: "india"` returned the regulator as **FIU-IND under PMLA**, the tax line as *30% flat tax on VDA gains (Sec 115BBH) + 1% TDS (Sec 194S) on transfers*, the rails as *INR IMPS / NEFT (Domestic CEX), UPI and IMPS P2P (Global CEX)*, and then a matrix of services each with `status: "conditional"` and its own guide URL. The prose is written for somebody about to fund an account, and the second paragraph is the one that earns the record: *Check the entity serving your account, product eligibility and withdrawal methods before funding. Registration and a supported bank rail do not guarantee a freeze-free transfer.* That is the sentence an assistant should repeat, and it is the vendor's own, not a summary of one.

**And the commercial arrangement is disclosed in the payload.** `list_providers` carries, beside the fees and the KYC tier, a `referral_code`, a `you_get` line and a field named `we_get` whose value begins *A referral commission share from...*. Every ranked row in `calculate_trade_cost` carries `referral_code`, `direct_referral_url` and a `go_url` stamped `utm_source=mcp`. This is a lead-generation surface that states its economics, which is better than the usual version that hides them, and it is the first thing to tell an operator who is about to read a ranking as advice.

## The limits, and where they bite

- **It is a referral funnel with an honest label.** Four of the eight ranked exchanges in the spot taker list carry a referral code in the response. The sort itself is on cost, and the second cheapest instant-buy row (CoinDCX at 1.70%) carries no referral at all, which is the evidence that the order is not bought. Read a row as a price, not as a recommendation, and expect an affiliate link in the payload.
- **The fees are a maintained table, not a live quote.** Every response states `as_of: 2026-11-13`, two days old at the time of this pass, and the numbers are identical across modes and amounts because they are stored rather than fetched per call. A fee change at an exchange shows up here when the vendor updates the table, and the `report_outdated_info` tool exists because that is a real lag.
- **Eight exchanges, and only exchanges.** The calculator ranks eight venues while `list_providers` covers more categories. A cost comparison against a venue that is not in those eight is not answered, and the response does not say the list is short.
- **The country argument is a slug and a wrong one fails silently.** `IN` returns an empty ranked list rather than an error or a hint. Use the lower-case country name, and check the row count before reporting a result.
- **`estimated_cost_usd` excludes the spread on the exchange modes that have one.** For `spot_taker` and `spot_maker` the figure is the fee, which is the right comparison for a limit order on a book. An instant card buy is priced with the spread folded in at 1.65% to 3.55%, so the two modes are not measuring the same thing and should not be averaged.
- **A crypto cost model is not tax advice, and the country record says as much by pointing at its own guides.** The tax line is a summary with the statutory sections named; the filing itself is per person and per jurisdiction.

## Frequently asked

### Does it need an API key or an account?

No. Every request in this pass returned 200 over plain HTTPS with no credential, and the response carries no session identifier, so the surface is stateless.

### Can I compare more than two exchanges at once?

Yes, that is the default: `calculate_trade_cost` returns the whole ranked list for the mode. Pass `country` to narrow it, and check that the narrowed list is not empty before drawing a conclusion.

### How current is the data?

The response states its own date, `2026-11-13` in this pass, and a freshness field is the honest part of a stored fee table. Re-ask rather than caching a quote across a week, and use `report_outdated_info` when a number is visibly wrong.

### Is the ranking independent?

No, and the server says so itself. Every row can carry a referral code and every provider record carries a `we_get` commission field. The ordering is on computed cost, verified in four modes, and the reader should know both facts at once.

### What is the difference between `spot_taker` and `instant_buy`?

About a factor of sixteen on the same exchange. A spot taker order pays the trading fee against a live book; an instant buy pays a spread for a guaranteed fill. The calculator prices both, which makes the convenience fee of a card purchase visible for the first time to most operators.

## What to check before you build on it

1. Pick the mode first. The mode changes the cost more than the exchange does, and averaging across modes produces a number that describes nothing.
2. Recompute one row before trusting the list: `amount x rate_pct / 100` should equal `estimated_cost_usd`.
3. Pass the country as a lower-case name, and assert the result set is non-empty.
4. Read `as_of` and treat the fee table as dated, not live.
5. Tell the operator about the referral fields before quoting a ranking, because the disclosure is in the payload and not in the answer.
6. Use `get_country` for the rule and the `guide_url` for the detail; the summary names the statute, the guide carries the steps.

## See Also

- [StackRates MCP](/hermes/mcp/servers/external/stackrates-mcp) - the price-benchmarking shape done with a data licence instead of a referral code
- [CryptoStruct Market Data MCP](/hermes/mcp/servers/external/cryptostruct-mcp) - the market-data side of crypto, where this server carries cost and regulation
- [External MCP Server Catalog](/hermes/mcp/servers/external/) - every guide in this catalogue
- [MCP Ecosystem Sweeps](/hermes/mcp/sweeps/) - the pass that found this server
