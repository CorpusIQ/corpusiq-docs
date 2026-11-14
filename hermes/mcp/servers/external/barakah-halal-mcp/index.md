---
title: "Barakah Halal Stock Screen MCP - Verdicts With Dates"
description: "A keyless two-tool server that screens listed stocks against an AAOIFI-style test and returns every verdict change with the date it happened."
category: "Finance / Compliance Screening"
stars: "0 (hosted and closed source; the screening logic is not published)"
added: 2026-11-14
source: "the mcp.so submission queue entry #7320 at 2026-11-14T05:31Z, the official registry record com.barakahprofits.app/halal-screen, the vendor pages barakahprofits.com and app.barakahprofits.com/halal-verdict-changes read the same day, and a live session on this host: initialize, tools/list and ten tools/call requests against https://app.barakahprofits.com/mcp"
relevance: ★★
tags: [finance, equities, halal, sharia, compliance, screening, aaoifi, ledger, provenance, mcp, remote, keyless]
last_updated: "2026-11-14"
---

# Barakah Halal Stock Screen MCP

**A compliance verdict is a fact with a date on it, and almost nothing on the market treats it that way.** A screen tells you whether a stock passes today. It does not tell you that the company stopped passing three weeks ago because its share price fell, nor that the one you rejected last year passes now. The AAOIFI-style test makes that gap structural: interest-bearing debt is measured against **market capitalisation**, so a falling share price raises the ratio and a company can break the screen without borrowing a single dollar.

Barakah Profits is a halal value-investing service built around that observation. The screen re-checks every covered stock nightly and publishes each verdict change as a dated entry, and the MCP surface is deliberately minimal: **two keyless tools**, one to screen a ticker and one to read the change ledger.

```text
Server type:   remote Streamable HTTP, JSON-RPC 2.0, stateless (no Mcp-Session-Id issued)
Endpoint:      https://app.barakahprofits.com/mcp
Server:        barakah-halal-screen 1.0.0, protocol 2025-06-18, capabilities: tools
Registry:      com.barakahprofits.app/halal-screen, streamable-http, no sign-in and no API key
Auth:          none; every measured call answered keyless
Tools:         2 (check_halal_stock, recent_halal_verdict_changes)
Markets:       US (NASDAQ, NYSE), Australia (ASX), Malaysia (Bursa), Singapore (SGX)
Data source:   Twelve Data; screen re-run nightly, ledger from 24 September 2026
```

## The evidence tier

Fully driven, keyless, ten `tools/call` requests. `initialize` answered **200** with `serverInfo` **barakah-halal-screen 1.0.0** on protocol **2025-06-18** and no session header, and `tools/list` returned both tools with complete schemas.

The server's `instructions` string names the contract in one sentence: *use `check_halal_stock` when the user asks whether a stock is halal or Sharia-compliant, and always pass on the verdict history and the links.* The second tool exists because of the first one's weakness - a verdict without its history is the thing this service was built to stop.

The tool's own error message is the best description of coverage on the surface. Screening an unknown ticker returned *No stock found for 'ZZZZ'. Covered: US (NASDAQ, NYSE), Australia (ASX, e.g. CSL.AX), Malaysia (Bursa, e.g. 1155.KL or a company name) and Singapore (SGX, e.g. D05.SI)* - four markets, and no London, Tokyo or Euronext, which matches the vendor's figure of about **9,000 stocks**.

## What came back when it was driven

Four tickers, chosen to exercise each verdict rather than to flatter the screen.

| Ticker | Verdict | Business activity | Debt vs market cap (limit 30%) | Cash and securities (limit 30%) | Non-permissible income (limit 5%) |
|---|---|---|---|---|---|
| **AAPL** | **DOUBTFUL** | review - 1% credit-card services, ~15% doubtful advertising and mixed digital content | pass - **1.6%** | pass - **1.2%** | review - interest income not reported |
| **MSFT** | **DOUBTFUL** | review - 19.88% doubtful streams: XBOX 6.57%, LinkedIn 5.97%, search advertising 4.57%, M365 Consumer 2.76% | pass - **1.5%** | pass - **2.0%** | pass - **1.0%** |
| **JPM** | **NOT HALAL** | fail - conventional banking, interest-based lending and derivatives, 100% non-permissible | fail - **57.9%** | fail - **90.6%** | review |
| **XOM** | **NEEDS REVIEW** | pass - oil and gas integrated | pass - **6.0%** | pass - **1.5%** | review - interest income not reported |

Three things in that table are worth more than the verdicts themselves.

**The ratio checks are not what decides these stocks.** Both technology names pass debt and cash comfortably - Apple at 1.6% and 1.2%, Microsoft at 1.5% and 2.0% - and both are still **DOUBTFUL**, because the decision lands on the revenue-mix line where the server reads the annual report and quotes the segments it counted. The headline number an investor glances at (debt under 30%) passes on almost every large-cap; the screen's work happens elsewhere.

**The failures are arithmetic, and the arithmetic is explicit.** JPMorgan fails three checks at once: 57.9% debt against a 30% limit, 90.6% cash and securities against the same limit, and a business that is 100% interest-based. Any one of them is disqualifying, and the response states the measured value beside the threshold rather than only the verdict.

**"Cannot be read automatically" is a real answer here.** In six of the ten calls the non-permissible-income line came back as `review` with *interest income isn't reported for this company, so this can't be read automatically. Verify in the financial notes.* A screen that guesses that line produces a confident verdict from an absent input; this one refuses and says which figure to go and find.

Every response carries `as_of` (2026-11-14 on the Apple and Exxon calls, 2026-11-13 on Microsoft), the exchange, the sector, a `method` line reading *AAOIFI-style screen by Barakah Profits. Automated estimate, not a fatwa*, the attribution *financial data provided by Twelve Data*, and two links - the full analysis and the verdict ledger. A Malay translation of the business-activity detail rides along in `detail_ms`.

## The ledger, and the one thing it does better than any price tool

`recent_halal_verdict_changes` returns dated events with `event` of `CLEARED` or `BROKE` and a `reconstructed` flag. Twenty-five rows came back for `limit: 25` (the schema's default is 10), running back from **2026-11-12** to **2026-10-19**:

```text
2026-11-12  OXY   CLEARED     2026-11-12  NBIS  CLEARED
2026-11-11  OXY   BROKE       2026-11-11  NBIS  BROKE
2026-11-10  NBIS  CLEARED     2026-11-10  NE    BROKE
2026-11-06  LUV   BROKE       2026-11-04  TTE   BROKE
2026-11-04  BMRN  BROKE       2026-11-02  TTE   CLEARED
2026-10-29  RCL   CLEARED     2026-10-29  SM    CLEARED
2026-10-29  TTE   BROKE       2026-10-29  BMRN  CLEARED
```

Occidental and Nebius each **broke and cleared inside 48 hours** - broke on 11 November, cleared on 12 November - and Nebius had already cleared on 10 November. That is the mechanism the vendor explains on its own ledger page: market capitalisation sits in the denominator, so a share price move flips a verdict with no balance-sheet change at all. An investor holding either name on the strength of a screen run last week is holding a stale answer.

All rows measured carried `reconstructed: false`. The vendor says rows before 24 September 2026 were reconstructed from published posts and labelled as such, and that every row after it is written live by the nightly screen.

## Defects and limits, recorded

- **The public ledger page and the tool disagree on how much history exists.** The homepage states *17 verdict changes on record, latest 3 Oct 2026*, while the tool returned entries dated up to **12 November 2026**. One of the two is stale; the tool is the surface that answers, so the page copy is the stale one.
- **A burst is answered as a business error, not a rate limit.** Repeated calls in quick succession returned `isError: true` with *busy, try again in a minute*, and one unknown ticker got that same message before a later retry returned the proper *No stock found* with the coverage list. A caller cannot reliably tell "no such ticker" from "slow down", so any screening loop needs a retry and should treat `busy` as retryable rather than as a verdict.
- **One early call returned a single ledger row for `limit: 8`.** A re-run of the same call returned eight. A short page is not the whole record.
- **Two tools, no filings, no financials.** The verdict is the product; the revenue mix behind it is quoted in prose, and the full analysis, quality scores and change alerts sit behind the vendor's paid tier.
- **Four markets.** US, ASX, Bursa Malaysia and SGX; nothing European or Japanese.
- **A commercial screen with a paid upsell**, not a neutral utility: every response carries an `upsell` string pointing at Barakah Watch.
- **Closed source.** The AAOIFI thresholds are stated (30% debt, 30% cash, 5% income) and the segments behind each verdict are quoted, but the screening code and the segment classifier cannot be inspected.

## Connecting it

```bash
claude mcp add --transport http barakah-halal https://app.barakahprofits.com/mcp
```

Any MCP client takes the same URL with no key:

```json
{"mcpServers": {"barakah-halal": {"url": "https://app.barakahprofits.com/mcp"}}}
```

There is nothing to sign in to, which means the screen can be checked before any account exists: ask for a stock you already know the answer for, and read the check table rather than the verdict line.

## Questions this answers that a chat window alone cannot

### Is Apple halal under an AAOIFI-style screen?

It returns **DOUBTFUL**, not a clean pass: debt at 1.6% and cash at 1.2% of market cap both pass the 30% limits, and the verdict is held down by the revenue mix - about 1% from non-permissible credit-card services and an estimated 15% from doubtful advertising and mixed digital content. The interest-income line could not be read and is marked for manual verification.

### Which stocks recently stopped passing the screen?

`recent_halal_verdict_changes` returns the dated record: Occidental and Nebius broke the screen on 11 November 2026 and cleared again the next day, Noble broke on 10 November, Southwest on 6 November, TotalEnergies and BioMarin on 4 November. The cleared and broke events are returned together, so the record reads as movement rather than as a list of failures.

### Can a company pass today and fail tomorrow without changing its books?

Yes, and it is the point of the ledger. The debt test divides by market capitalisation, so a falling share price raises the ratio. No borrowing is needed for a verdict to flip - which is why the vendor keeps a dated record and why a single screening date is not a compliance answer.

### Does it cover non-US markets?

Four: US (NASDAQ and NYSE), Australia (ASX, tickers like CSL.AX), Malaysia (Bursa, tickers like 1155.KL or a company name) and Singapore (SGX, tickers like D05.SI). The coverage list came out of the server's own error message, not from a marketing page.

## Verdict

A two-star entry that closes a real gap: nothing else in this catalog screens a listed company for Sharia compliance, and the AAOIFI test it runs - business activity, interest-bearing debt under 30% of market cap, cash under 30%, non-permissible income under 5% - is the standard one, with the measured value returned beside every threshold.

It earns the second star for the ledger. Returning `CLEARED` and `BROKE` events with dates, and admitting in its own method line that the behaviour is an *automated estimate, not a fatwa*, is the honest shape for a screen whose answer changes with the share price. It does not earn a third because the surface is two tools deep, four markets wide, closed source, and carries a sales line in every response - and because the vendor's own homepage and its own tool still disagree about how many changes the ledger holds.

For a Muslim investor or a fund running a compliance pre-check, this is a fast, free first pass that tells you which figure to go and verify. It is not an audit and does not claim to be.

See also: [SEC EDGAR MCP](/hermes/mcp/servers/external/sec-edgar-mcp/) for the filings the business-activity check reads, [Stock Market MCP Server](/hermes/mcp/servers/external/stock-market-mcp-server/) for price and market-cap data, [Sanctions Screening MCP](/hermes/mcp/servers/external/sanctions-screening-mcp/) for the other compliance screen in this catalog, and [MobileMRR MCP](/hermes/mcp/servers/external/mobilemrr-mcp/) for the provenance-first treatment of another financial figure.
