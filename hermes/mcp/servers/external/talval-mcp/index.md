---
title: "Talval MCP - Fair Value and a $2 Report an Agent Can Buy"
description: "A keyless valuation endpoint over 1,700 listed companies, with filed results as the control and a $2 report behind an HTTP 402 challenge."
category: "Finance"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-26
source: "mcp.so /feed card `/servers/talval` stamped 11/26/2026 08:57 AM UTC, the only card above the November 25 evening top; official registry `com.talval/research` 1.0.2 published 2026-11-20T08:57:06Z (isLatest); keyless initialize 200 and a 7-tool tools/list on https://talval.com/mcp, with eight tools/call requests driven on 2026-11-26 (search_stocks, get_stock_research on AAPL, RHM.DE and PRU.L, screen_stocks undervalued, compare_stocks, list_superinvestors, get_superinvestor berkshire, stocks_of_the_week); the HTTP 402 payment challenge read by hand from GET /api/agent/reports/AAPL; coverage and dataset limits read from the vendor's own dated snapshot on https://talval.com/dataset"
relevance: "★★"
tags: [finance, valuation, stocks, research, 13f, superinvestors, screener, pay-per-report, http-402, mpp, keyless, remote-mcp]
last_updated: "2026-11-26"
---

# Talval MCP

**"Is this business cheap?" is the question an assistant answers worst, because the answer has to be a dated number against a stated value.** An assistant asked to value a listed company will produce a multiple from memory, and the multiple will be a year stale and unlabelled. Talval answers with a fair value, the upside to it, a quality and safety score, the filed results behind them, and an `as_of` date it asks the client to quote. It is keyless, it covers the US, the UK and continental Europe, and the free tier is enough to answer the valuation question on its own.

```
Server type:  Remote (Streamable HTTP)
Endpoint:     https://talval.com/mcp            keyless, no account
              https://talval.com/mcp/pro        OAuth, subscriber's own plan
Auth:         none on /mcp; Bearer on /mcp/pro (401 invalid_token)
Registry:     com.talval/research 1.0.2, published 2026-11-20T08:57:06Z
Instructions: "Talval is a value-investing research platform in the Graham/Buffett tradition."
Tools:        7, read from a keyless tools/list
Pay door:     GET /api/agent/reports/{TICKER} answers HTTP 402 with an MPP challenge, $2
```

`initialize` answers **200** at protocol **2025-06-18** as `talval` **1.0.0**, with the single capability `tools` and an `instructions` block that does the job most servers skip: it states that `fair_value` may be withheld and that `withheld_reason` then says why, that every figure is an end-of-day snapshot carrying a date, that institutional flow, insider activity, consensus and the written thesis are **not** on this surface, and that verdicts are model outputs rather than advice. A client that reads `instructions` will not present a Talval number as a live quote.

## The seven tools

| Tool | Arguments | What comes back |
| --- | --- | --- |
| `search_stocks` | `query`, optional `limit` (default 8, max 25) | typo-tolerant matches with ticker, name and sector |
| `get_stock_research` | `ticker` | verdict, fair value, upside, four scores, P/E, yield, market cap and the latest filed annual results |
| `screen_stocks` | `screen` (one of `undervalued`, `high_quality`, `safe_dividend`, `undervalued_dividend`), optional `sector`, `limit` | ranked rows with price, fair value, upside, verdict, quality |
| `compare_stocks` | `tickers`, 2 to 8 | one table of verdict, conviction, close, fair value, upside and three scores |
| `list_superinvestors` | none | tracked 13F managers with portfolio value, position count and quarter |
| `get_superinvestor` | `slug` | one manager's largest holdings with portfolio weight and quarter-on-quarter activity |
| `stocks_of_the_week` | none | the week's Undervalued picks ranked by conviction, with `week_start` |

Every tool returns both a markdown `content` block for the reader and a `structuredContent` object for the program, and the two are not always the same payload. The table below is driven, not described.

## One company, read both ways

`get_stock_research` on **AAPL** at 03:00 MST on 2026-11-26:

- **Verdict:** Fairly valued · overvalued · conviction 6/10 · risk High, snapshot date **2026-11-26**
- **Last close:** 355.58 USD (as of 2026-11-25)
- **Fair value estimate:** 308.048 USD, **upside -13.367%**
- **Scores (0-100):** value 1.9, quality 92.4, safety 69.3, dividend 53.1, composite 67.3, Piotroski F-score **9/9**
- **Filed results, fiscal 2026:** revenue **478.834B USD**, net income **132.175B USD**, free cash flow **136.056B USD**, diluted EPS **8.98 USD**
- **Market cap:** 5.167T USD across 167,000 employees

The upside reproduces by hand and to the digit: `(308.048 - 355.58) / 355.58 = -0.133674`, against the payload's `-13.367448751440742`. The filed-results block is the part that makes the guide worth writing. **A valuation verdict and a filed revenue figure in the same response is the difference between an opinion and an audit trail**, and the payload says where it came from: *"As reported in the company's own filings - not estimates."* A client quoting the fair value without the revenue is quoting half a page.

## The screen, and the arithmetic that holds

`screen_stocks` with `screen: "undervalued"` and `limit: 5` returned five priced rows in this order:

| # | Ticker | Company | Price | Fair value | Upside | Verdict | Quality |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XP | XP Inc. | 14.39 USD | 22.03 USD | +53.1% | Undervalued | 89/100 |
| 2 | SYF | Synchrony Financial | 68.73 USD | 89.18 USD | +29.8% | Undervalued | 92/100 |
| 3 | NTES | Netease Inc. | 104 USD | 146 USD | +39.7% | Undervalued | 83/100 |
| 4 | NWG.L | NatWest Group plc | 5.74 GBP | 6.96 GBP | +21.3% | Undervalued | 68/100 |
| 5 | ACGL | Arch Capital Group Ltd. | 110 USD | 135 USD | +22.8% | Undervalued | 81/100 |

Three of the five reproduce exactly from the displayed figures: XP `7.64 / 14.39 = 53.09%`, SYF `20.45 / 68.73 = 29.75%`, NWG.L `1.22 / 5.74 = 21.25%`. NTES reads **+39.7%** against a displayed **40.4%** because the row's price is rounded to the dollar and the upside is computed on the unrounded close (`146 / 1.397 = 104.5`), which is the right way round: **the percentage is computed on the exact number and the money column is rounded for the table.** A client that recomputes upside from the rounded columns will disagree with the server by a few tenths, and the server is the one that is right.

## What it does outside the United States

The suffix convention is stated in the tools rather than discovered: `RHM.DE`, `PRU.L`, `AZM.MI`. Two were driven:

- **RHM.DE, Rheinmetall AG (Germany):** close **735.8 EUR**, fair value **817.31 EUR**, upside **+11.08%**, dividend yield **1.56%**, 28,815 employees, market cap **34.2B USD**
- **PRU.L, Prudential plc (United Kingdom):** close **9.28 GBP**, fair value **8.74 GBP**, upside **-5.82%**, P/E **8.1**, yield **2.23%**, Piotroski **4/9**, fiscal 2025 revenue **8.6B GBP** and net income **3.0B GBP**

A search for *Rheinmetall* resolves to the German listing in one call, and an uncovered ticker (`ZZZZ`) refuses rather than guesses: *"Talval does not cover 'ZZZZ'. Use `search_stocks` to find the right ticker - note that non-US listings carry a suffix."* That is the right shape for a negative: the tool names the fix.

## Superinvestors, and the Alphabet trap

`list_superinvestors` returned the tracked managers with their quarter, and `get_superinvestor` on `berkshire` returned **30 positions** and **304.2B USD** for the quarter ending **2026-09-30**, with the largest holdings weighted and labelled `hold`, `add` or `reduce`. The top seventeen rows sum to **98.4%**, which leaves **1.6%** across the remaining thirteen names.

**The row that matters is Alphabet twice.** GOOGL at **8.9%** and GOOG at **3.0%** are the same issuer in two share classes, so the exposure is **11.9%**, not a 8.9% holding beside an unrelated 3.0% one. A client that ranks holdings without collapsing classes reports Alphabet below American Express (**15.2%**) when it is not. The same trap sits in any 13F surface and this one does not solve it for the caller: `activity` is per row, not per issuer.

## The $2 report is a real HTTP 402 door

The vendor's `llms.txt` documents a paid per-report fetch, and the door is measurable without paying:

```text
GET https://talval.com/api/agent/reports/AAPL
HTTP/2 402
content-type: application/problem+json
www-authenticate: Payment id="Dd9x2oNWi-rAm64lv51Q_HaFRAWZ8_oJXfy90AaoUk4",
                  realm="talval.com", method="stripe", intent="charge",
                  expires="2026-11-26T10:07:48.759119Z",
                  description="Talval research report (JSON): AAPL"

{"type": "https://paymentauth.org/problems/payment-required",
 "title": "Payment Required", "status": 402,
 "detail": "Payment is required for \"talval.com\" (Talval research report (JSON): AAPL).",
 "challengeId": "Dd9x2oNWi-rAm64lv51Q_HaFRAWZ8_oJXfy90AaoUk4",
 "hint": "Use a supported wallet to pay for this resource ... https://mpp.dev/tools/wallet.md"}
```

A **five-minute** payment window from the request, `method=stripe`, `intent=charge`, and an RFC 9457 problem document naming the challenge so a client can retry against the same quote instead of re-pricing it. This is the **pay-per-resource** tier our catalog had not carried: Octio priced individual API calls behind an account balance, and this prices one document behind a payment challenge with **no account at all**. The published prices are **$2** for the JSON report and **$2** for the PDF, with prepaid passes at **$14.99 a month or $149 a year** for Premium and **$29 or $290** for Pro, sold over the same challenge or as a Stripe Checkout link the person pays themselves, and the same items exposed to commerce protocols as `report:TICKER` and `pdf:TICKER`. The report adds institutional ownership and insider flow, the Wall Street consensus and the outlook scenarios, none of which the free tools carry.

## Seven defects, measured

1. **`compare_stocks` carries no date at all.** The `structuredContent` is `{companies: [...], not_covered: []}` with no `as_of` field, and the markdown table has no snapshot line, while the server's own instructions say *"Everything is an end-of-day snapshot with an `as_of` date. Quote that date. Never present these figures as a live quote."* The single tool built for side-by-side comparison is the one tool that cannot be dated.
2. **The text and the structured payload disagree about the verdict.** Content reads **"Fairly valued · overvalued"** for AAPL; `structuredContent.verdict` reads **"Fairly valued"**. The second word is a zone suffix derived from the upside and it exists only in the prose, so a client rendering structured data loses the part a reader reacts to. MSFT shows the inverse: *"Quality at a fair price"* in both, because the phrase is one string there.
3. **A covered company with no verdict and no reason.** `RHM.DE` returns `covered: true`, `fair_value: 817.31`, `fair_value_usable: true` and `upside_pct: 11.08`, beside `verdict: "N/A"`, `conviction: 0`, `risk_level: "N/A"`, `pe_trailing: null`, `latest_annual: null` and four of six scores `null`. `withheld_reason` is `null`. The instructions promise an explanation when `fair_value` is withheld; here the fair value **is** published and everything that would let a reader judge it is missing, with nothing saying why. A client showing **"Undervalued by 11%"** for a DAX name on a verdict of N/A is showing a number the payload does not stand behind.
4. **`market_cap` has no currency of its own.** RHM.DE reports **34,245,616,108.6** for a line whose `currency` is **EUR**, PRU.L reports **23.6B GBP**, AAPL **5.167T USD**. There is no `market_cap_currency` field, and the cap does not follow the `currency` field, so any roll-up that sums caps across rows mixes three currencies under one label.
5. **`as_of` and `price_as_of` are different dates and only one is a price date.** AAPL carries `as_of: 2026-11-26` and `price_as_of: 2026-11-25`, which is correct and honest, but the prose header prints *"Snapshot date: 2026-11-26"* one line above *"Last close: 356 USD (as of 2026-11-25)"*. A client quoting the header date as the price date is a day wrong at every read.
6. **A no-argument screen is a soft empty.** `screen_stocks` called with `{}` answered **200**, `isError` absent, `rows: []`, and a content line *"Unknown screen ''. Available: undervalued, high_quality, safe_dividend, undervalued_dividend."* The schema lists no default and an enum, so the call is invalid, but a client that renders only tables shows an empty screen, which reads as **"there are no undervalued stocks"** rather than "you did not pass an argument".
7. **The screen's ranking key is not published.** The tool description says *"The screen is already ranked"*, and the returned order is neither upside-descending (**SYF 29.8%** above **NTES 39.7%**) nor quality-descending (**XP 89** above **SYF 92**), with no rank or score field on any row. A caller asked to show "the top five undervalued names" is showing Talval's order without being able to say what it means, so a re-sort by upside gives a different list from the one the vendor ranked.

## Coverage, and what the vendor's own numbers say

The vendor's agent page states **1,700+ listed companies in the US, the UK and continental Europe**, and its `mcp.so` card repeats **1,700+ listed companies**. Its own **/dataset** page carries a dated snapshot, taken **7 September 2026**, that is narrower and more useful: *"**Daily prices** - 2,294,261 rows - five years per company, end-of-day closes across **960 covered companies**, not redistributed."* Those two figures describe different things (companies covered for research against companies with a price series), and this pass did not reproduce a universe count on either definition. **Quote the dated dataset figure when the claim is about prices and the marketing figure only as a vendor claim.**

The same page states the reuse terms plainly, and they are more permissive than most finance surfaces here: *"Quote our figures, reproduce our tables, and use the 13F export in your own work, including commercially - with attribution and a link. You do not need to ask."* The one condition is the one that matters to an assistant: *"What we ask in return is that you carry the limits with the number."*

## Connecting it

```bash
claude mcp add talval --transport http https://talval.com/mcp
```

No key, no OAuth, no environment variable. `mcp.so` shows the listing as **Verified** and **Featured** under **Finance & Commerce**, transport **Streamable HTTP**, authentication **None**, updated **2026-11-26**, and its tool list as unavailable, which is accurate: the list has to be read from the endpoint. The vendor also publishes an A2A agent at `https://talval.com/api/a2a`, a server card at `/.well-known/mcp.json`, an OpenAPI document and an API catalog, and every page answers to `Accept: text/markdown` or a `.md` suffix, which makes it one of the few research vendors that has published a machine-readable surface on purpose rather than by accident.

## Where it fits a business-answer system

The pattern to take is the **filed-results block beside the model output**. A valuation is an opinion; revenue, net income, free cash flow and diluted EPS from the company's own filing are facts; this server returns both in one payload and labels which is which. An answer system that shows the pair lets the reader check the opinion against the business rather than trusting the verdict, and the instructions field pre-empts the two failures that make financial data unusable in an answer: an undated number and a withheld number presented as a zero.

## See also

- [WeightedShares MCP](/hermes/mcp/servers/external/weightedshares-mcp/) for buybacks, stock-based compensation and True FCF from SEC XBRL, the filed-dollar control this guide borrows its method from.
- [TradingData MCP](/hermes/mcp/servers/external/tradingdata-mcp/) for market prices and indicators across a 48-tool surface.
- [Kote Charts MCP](/hermes/mcp/servers/external/kote-charts-mcp/) for on-chain metrics rather than equity fundamentals.
- [External MCP Server Catalog](/hermes/mcp/servers/external/) for the full index.
