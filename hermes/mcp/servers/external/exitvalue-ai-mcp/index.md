---
title: "M&A Multiples MCP - Private Business Valuation by Industry"
description: "Keyless MCP that answers what a business in 106 industries sells for: median EV/EBITDA and EV/Revenue with the deal count behind each figure."
category: Finance
stars: n/a (hosted vendor server, no public repository)
added: 2026-11-04
source: "mcpservers.org /all page 2 slug exitvalue-ai-ai-connector read through the r.jina.ai reader, plus a keyless driven session on https://exitvalue.ai/api/mcp: initialize 200 as exitvalue-ai 1.1.0, tools/list returning 4 tools, and three calls (list_industries, get_valuation_multiples HVAC, compare_industries dental/HVAC/SaaS)"
relevance: ★★★
tags: [ma-multiples, valuation, ebitda, private-companies, exit-planning, finance, remote-mcp]
last_updated: "2026-11-04"
---

# ExitValue.ai M&A Multiples MCP

**Every owner of a real business eventually asks the same question, and the honest answer is usually "nobody publishes it". Public comparables price a listed company with a ticker and a share count. They say nothing about what a dental practice in Ohio, an HVAC contractor in Arizona or a marketing agency with four clients actually sells for.**

ExitValue.ai publishes the missing number: transaction multiples for private companies, by industry and by deal size, from disclosed M&A. The MCP server puts it in the conversation:

```
Server type: Remote (Streamable HTTP, stateless)
Endpoint:    https://exitvalue.ai/api/mcp
Auth:        none
serverInfo:  exitvalue-ai 1.1.0
Tools:       4 (all read-only)
Coverage:    106 industries and sub-verticals
Data:        1,560 disclosed transactions, 2018 to 2026
Sources:     a licensed historical M&A database, SEC EDGAR filings,
             verified press releases
Site:        exitvalue.ai
```

A keyless `initialize` answered **HTTP 200** and `tools/list` returned all **4** tools, so the surface was driven rather than quoted. There is no session, no key and no account, which is also why every call works as a plain JSON-RPC message.

## Four tools, and each one answers a different question

`list_industries` is the index, and its shape matters more than its length. It does not return a flat list: it returns 15 verticals with their sub-verticals and their ids, so `Healthcare` carries dental practice, medical practice, veterinary, optometry, physical therapy, mental health, home health, hospice, urgent care, pharmacy, imaging, ambulatory surgery, laboratory, devices, DME, healthcare IT and staffing. `Home Services` carries HVAC, electrical, pest control, landscaping, roofing and commercial cleaning. `Professional Services` carries accounting, law, consulting, insurance agency, staffing, IT services and both marketing and advertising agencies. A caller passes the bracketed id, not the display name, though plain names like "HVAC" or "dental practice" also resolve.

`get_valuation_multiples` is the one-line answer. For one industry it returns median and middle-50% EV/EBITDA and EV/Revenue, the deal count behind each, the median deal size of the sample, and the source sentence. HVAC in this pass returned **EV/EBITDA median 9.6x** with a middle 50% of **8.4x to 14.8x** on **n=11**, and **EV/Revenue median 0.95x** with a middle 50% of **0.60x to 2.20x** on **n=13**, over 14 disclosed transactions with a median deal size of **$135 million**.

`compare_industries` puts two to six sub-verticals side by side on one metric. Dental practice, HVAC and SaaS in a single call: dental **11.0x** median with a middle 50% of **7.17x to 14.0x** on **n=80**, HVAC **9.6x** on **n=11**, SaaS **14.66x** with a middle 50% of **8.7x to 25.31x** on **n=414**, and the sample count for the whole response returned as **1,560** disclosed transactions.

`get_multiples_trend` gives year-by-year medians for one sub-vertical from 2018 to 2026, with a floor of **n=10** in any single year.

The response carries structured data alongside the prose, so an agent reads `p25`, `p50`, `p75` and `n` as numbers rather than parsing a sentence: the compare call returned `{"sub_vertical": "hvac", "p50": 9.6, "p25": 8.45, "p75": 14.85, "n": 11}` inside `structuredContent`.

## The refusal is the feature, and it is measurable

The trend tool on HVAC returned no years at all, and said why in one sentence: not enough disclosed transactions with **n < 10** in any single year to publish a year-by-year median. The bracket object in the HVAC multiples response came back empty for the same reason, while the pooled multi-year figure was published and labelled as pooled.

Two consequences follow, and both matter more than the data points. First, a multiple that exists is a multiple with a count behind it, so the reader can tell a number built on 414 deals from a number built on 11 without being told to be careful. Second, withholding is not an error path here: both refusals came back `isError: false` with an explanation and the tools that do have data named as the alternative. An agent that asks for a per-year trend on a thin sub-vertical gets an answer it can relay, not a stack trace.

The residual weakness is the one to state plainly: the pooled figures mix nine years of deal activity, so a rising or falling market is invisible in the headline number. HVAC at 9.6x is an average across 2018 to 2026, not a 2026 price, and the same pooled sample spans a very different rate environment at each end.

## What it is and is not

These are population medians from disclosed transactions. A specific business is not its industry's median, and the server says so on every response: the multiple depends on margins, growth, customer concentration and owner dependence. A dental practice at 11x with 30 percent owner-dependent revenue does not transact at 11x.

Every response also carries a `calculator_url` with `src=mcp` and an `industry` parameter pointing at the vendor's own free valuation calculator. That is a marketing funnel inside the tool output, and it is worth knowing before wiring the tool into an unattended agent that relays text verbatim. The data is separable from it: the structured fields hold the multiples, the counts and the source, and the calculator link is one field that can be dropped.

Two limits are structural. The universe is US-centric disclosed transactions, so a European services business or a business below the size that gets disclosed is not covered by these medians at all. And "disclosed" means the deal price became public, which skews toward larger, cleaner and more newsworthy transactions than the median owner runs.

## Where this belongs in an operator's stack

It belongs beside the questions that already exist rather than replacing anything. A public-market tool prices what a ticker is worth today; this prices what a private business in the same line of work has been sold for. The gap between those two numbers is the reason owners overvalue their own companies, and it is now one tool call.

For an advisory workflow the useful sequence is `list_industries` to confirm the sub-vertical exists, `get_valuation_multiples` for the point estimate with its count, `compare_industries` to show a client what an adjacent line of business trades at, and `get_multiples_trend` only where the yearly counts support a story. One of those four calls is where the honest answer usually ends.

## FAQ

### Does it need an account, a key or a subscription?

No. `initialize` and `tools/list` answered without any credential, and every tool call in this pass ran without one. The endpoint is stateless, so there is no session to hold.

### Can it value one specific business?

No, and it does not claim to. It returns industry population medians with the deal count behind them. The free calculator the vendor links adjusts for the business's own margins, growth, concentration and owner dependence, and a live valuation still needs a qualified party.

### Why did a trend call return nothing?

Because a median built on fewer than ten disclosed deals in a year is not published. The tool says so explicitly and points at the pooled multi-year figure instead of returning a number it cannot defend.

### How many industries are covered?

106 sub-verticals across 15 verticals, from dental practice and HVAC to SaaS, fintech, restaurants by segment, logistics, and the other service and industrial lines a small business actually operates in.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [ROIC.ai MCP - Public Company Fundamentals](/hermes/mcp/servers/external/roic-ai-mcp-server/)
- [DFX Intelligence MCP - Private Credit With Citations](/hermes/mcp/servers/external/dfx-intelligence-mcp/)
- [Velarion MCP - Executive Compensation and Corporate](/hermes/mcp/servers/external/velarion-mcp/)
- [AllClear Lending MCP - Named Lenders and Decline Fallbacks](/hermes/mcp/servers/external/allclear-lending-mcp/)
