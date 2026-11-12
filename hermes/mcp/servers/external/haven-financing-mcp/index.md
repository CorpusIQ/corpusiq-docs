---
title: "Haven Financing MCP - Borrowing Against a Portfolio"
description: "Six read-only tools driven live: a 200,000 USD draw priced at 10,600 a year against 17,000, the collateral limits, and a rate sheet nine days old"
category: "Finance and Compliance"
stars: "not applicable (hosted service)"
added: 2026-11-12
source: "the submission queue entry #7189, the official registry record finance.haven/financing 1.0.0 declaring the same remote, the vendor's portfolio-financing page read the same day including its embedded rate table, and a live session on this host: initialize, tools/list and four tools/call requests against https://app.haven.finance/api/mcp"
relevance: ★★★
tags: [finance, lending, portfolio-financing, margin, sbloc, rates, liquidity, keyless, mcp, remote]
last_updated: "2026-11-12"
---

# Haven Financing MCP

**The decision to borrow against a portfolio is made once, in a hurry, usually against one number somebody quoted from memory.** Margin rates differ by brokerage, a securities-backed line is priced off a different curve, and the broker's own simulator is behind a login. Haven publishes the terms as six read-only tools on a keyless endpoint, so the comparison can be run in the conversation instead of in a spreadsheet someone rebuilds.

```text
Server type:  remote Streamable HTTP, keyless
Endpoint:     https://app.haven.finance/api/mcp
Server:       haven-financing 1.0.0 (serverInfo), protocol 2025-03-26
Capabilities: tools (listChanged: true)
Tools:        6 measured, all annotated readOnlyHint: true
Registry:     finance.haven/financing 1.0.0, remote declared as the same URL
Probe:        initialize, tools/list and four tools/call requests in one session
```

## What the server answered

`initialize` returned **200** with no credential. Its instruction block draws the boundary before any tool is called: the tools quote published rates, run illustrative simulations and build a prefilled link to Haven's simulator, and they **cannot** access brokerage accounts, view holdings or balances, open accounts, or execute trades. Applications happen through Haven's own flow, which is where the safety of a read-only financing surface comes from.

`tools/list` returned six, every one annotated `readOnlyHint: true`:

```text
get_current_rates          published fixed and variable rates with the all-in figure
simulate_financing         cost for a collateral value, a draw and a term
compare_existing_debt      an existing loan priced against each Haven option
create_onboarding_link     a prefilled simulator link, not an application
search                     reference documents: rates, fees, collateral, savings method
fetch                      full text of a document found with search
```

Note the parameter names, because they are not the obvious ones: `simulate_financing` requires `collateralValue` and `drawAmount` rather than `portfolioValue` and `amount`, and `compare_existing_debt` requires `balance` and `currentRatePercent`. A call with the intuitive names comes back as a schema error naming the field it wanted, which is a fine error but a wasted round trip.

## Driven: 200,000 USD against a 1,000,000 USD portfolio

`get_current_rates` returned `asOf: 2026-11-03T20:50:09.001Z` with a **0.45 percent** Haven fee and four fixed terms:

```text
term   financing   all-in    after-tax (illustrative)
3M     4.5703 %    5.0203 %  3.3454 %
6M     4.6720 %    5.1220 %  3.4199 %
12M    4.8501 %    5.3001 %  3.5503 %
2Y     4.8969 %    5.3469 %  3.5846 %
monthly variable  4.2798 %    4.7298 %  3.1328 %
```

`simulate_financing` with a 1,000,000 collateral value, a 200,000 draw and the 12M term returned annual `financingInterest: 9,700.20`, `havenFee: 900`, `total: 10,600.20`, against `comparisonAnnualInterest: 17,000` at 8.5 percent, so `annualSavings: 6,399.80` and `havenIsCheaper: true`. The same response carries the collateral arithmetic: LTV **20 percent** in the **Low** band, a facility cap of **70 percent** of collateral, a maximum draw of **700,000**, a minimum draw of **50,000**, and `collateralRequiredForDraw: 285,715`.

The assumptions are printed rather than implied: the collateral value is the figure the caller supplied, Haven has not verified it or the holdings, the portfolio is assumed to be eligible marginable securities at Interactive Brokers or Charles Schwab, and brokerage requirements can be stricter for concentrated or volatile positions. A fall in collateral value raises LTV and can lead to a margin call or liquidation - the risk that turns this from a rate comparison into a leverage decision is stated in the tool output, not buried in a page.

`compare_existing_debt` on a 200,000 margin balance at 8.5 percent returned every option at once: the 3-month term saves **6,959.40** a year, the 6-month 6,756, the 12-month 6,399.80, the 2-year 6,306.20, and the monthly variable **7,540.40** - the cheapest line in the table, and the only one with no rate lock. `search` for "rate lock" returned six documents with stable ids and public `haven.finance` URLs, which `fetch` turns into full text.

## The rate sheet is nine days old, and the vendor page disagrees

This is the finding worth carrying forward. The MCP's `asOf` is **2026-11-03T20:50:09Z**, nine days before this probe, and its rate table is lower than the one embedded in the vendor's own portfolio-financing page on 2026-11-12:

```text
term   MCP (asOf 3 Nov)   vendor page table (12 Nov)
3M     4.5703 %           4.6169 %
6M     4.6720 %           4.7132 %
12M    4.8501 %           4.9409 %
2Y     4.8969 %           5.0782 %
var    4.2798 %           4.6000 %
```

Both surfaces describe the same instrument, so one of them is behind. The honest reading is that the MCP serves a **published snapshot** rather than a live quote, and the `asOf` field is the tell: any answer that quotes a rate should carry that timestamp, and a borrower comparing against a lender's live quote should ask for the current page. A rate that is 5 to 18 basis points stale does not change a strategy, but it does change a comparison, and the response gives you the date to say so.

## Where it sits

It enters beside [Milemarker MCP](/hermes/mcp/servers/external/milemarker-mcp/) and [X1 Wealth MCP](/hermes/mcp/servers/external/x1-wealth-mcp/), which answer questions about what a household owns; this one answers what that ownership can be borrowed against, and it is the first lending entry here.

### Does the server touch a brokerage account?

No. The instruction block states it cannot access brokerage accounts, view holdings or balances, open accounts, or execute trades, and all six tools are annotated read-only. Collateral values are numbers the caller supplies and are recorded as unverified in the response.

### What is the smallest draw?

**50,000 USD**, with the facility capped at **70 percent** of collateral value less any Haven financing already outstanding. Both limits appear in the simulation response rather than in documentation.

### Can it tell me whether to borrow at all?

It compares cost, not suitability. `compare_existing_debt` answers which Haven term is cheaper than an existing loan and by how much a year; the leverage decision, the margin-call risk and the tax treatment stay with the person and their adviser.
