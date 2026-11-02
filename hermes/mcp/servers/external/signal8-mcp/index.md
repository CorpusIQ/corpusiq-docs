---
title: "Signal8 MCP - Dilution Intelligence for US Filings"
description: "SEC filing intelligence over 109 MCP tools, with a dilution pressure score, baby shelf capacity and cash runway computed from the filings behind them."
category: Finance
stars: ★★★ (109 tools measured, calls gated on Pro)
added: 2026-11-02
source: "the mcp.so recentServers block on 2026-11-02 (slug signal8, created 2026-11-02T05:01:51Z), the mcp.so detail page, signal8.ai/pricing, the public repository github.com/signal8ai/signal8-mcp, and a live probe of https://mcp.signal8.ai/mcp where initialize and tools/list answered HTTP 200 keyless and every tools/call answered JSON-RPC -32001"
relevance: ★★★
tags: [finance, sec-filings, dilution, small-caps, insider-trading, congressional-trading, market-data, oauth, remote-mcp]
last_updated: "2026-11-02"
---

# Signal8 MCP

**A shell registration is not a dilution event. The filing says what was authorised; the float says what it costs per share when it is used, and the gap between those two numbers is where small-cap investors get caught.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.signal8.ai/mcp
Auth:        Bearer sk_live key or MCP OAuth, Pro plan
Tools:       109 measured, all read-only
Discovery:   initialize and tools/list open, every call gated
Pricing:     Pro at $59 a month or $588 a year
```

## What it does

Signal8 reads SEC filings and market data for US listed companies and returns structured answers rather than documents. The parts that matter for an operator are the ones with arithmetic in them.

**Dilution** is the differentiator. `get_dilution_coverage` is a cheap precheck that says whether an analysis exists for a ticker and whether it is fresh. `get_dilution_risk` returns a Dilution Pressure Score from 0 to 100 built from seven components: shelf capacity, ATM and equity line capacity, warrants in the money, convertible proximity, cash burn urgency, historical dilution and toxic financing. `get_baby_shelf_capacity` recomputes the SEC Form S-3 General Instruction I.B.6 cap, the one third of public float limit that applies below a 75 million dollar non affiliate float, less the trailing twelve month takedowns, against the live float. `get_dilution_instruments` lists the instruments family by family, `get_dilution_snapshot` gives the position at a date and `get_dilution_history` gives the path.

**Cash** answers the follow on question. `get_cash_position`, `get_cash_history`, `get_cash_runway_calendar` and `screen_must_raise` turn burn and raises into a runway estimate and a list of companies approaching it.

**Filings** are read as text and as structure: `search_sec_filings`, `screen_sec_filings`, `get_filing_documents`, `get_filing_structured`, `get_filing_document`, `get_filing_exhibits`, `get_exhibit_content`, `search_filing_text`, `lookup_accession_number` and `get_recent_material_filings`.

**Ownership and politics** run deep. Insiders get transactions, cluster buys, positions and cross company patterns; institutions get holdings, position changes, derivatives, portfolio analytics and leaderboards; the political family carries congressional and executive branch trades, per politician profit and loss, scorecards, committees, votes, campaign donors and a policy and trade overlap view.

Two resources and a prompt come with it: `signal8://learn` indexes the Academy tracks and the glossary, and the `explain_dilution` prompt reads a company's dilution data and explains each figure with the Academy guides attached.

## What this pass measured

`initialize` on `https://mcp.signal8.ai/mcp` answered **HTTP 200** with no credential, over `text/event-stream`, reporting `serverInfo` `signal8-mcp` **0.19.0** and capabilities for tools, resources and prompts. The instructions in that response describe the intended workflow, which is resolve a company with `search_companies` and then call ticker scoped tools.

`tools/list` returned **109** tools in **221,131** bytes, and the count is worth noting against the vendor's own numbers: the mcp.so card says 70+, the repository README says 107, and the live list says 109. The live list is the one to trust.

Every tool call was gated. Seven were attempted with no credential, `search_companies`, `get_dilution_coverage`, `get_dilution_risk`, `get_baby_shelf_capacity`, `define_term`, `get_politicians_most_active` and `get_cash_runway_calendar`, and all seven answered JSON-RPC **-32001 Authentication required**. That includes `define_term`, the glossary lookup, which the vendor describes as a free learning tool that works without a key. It does not: the gate is applied to the whole tool surface, so the documented free tier is closed on the MCP path even though discovery is open.

## Where it sits in this catalogue

This catalogue read EDGAR nine ways and none of them computed a dilution position. A grep of all 1,082 guides returns **no entry** that mentions dilution, baby shelf or cash runway, which is the gap this closes.

The nearest neighbours answer narrower questions. [SEC EDGAR MCP](/hermes/mcp/servers/external/sec-edgar-mcp/) is full text search over filings. [Silicon Floor MCP](/hermes/mcp/servers/external/silicon-floor-mcp/) is the strongest owned data surface here, keyless with 18 read only tools over 200 plus AI and semiconductor companies, carrying ownership ranges, insider activity, fund flows, dividends and as filed financials, but it covers a universe rather than the whole listed market and it does not model what the cap table does next. [GovTrade MCP](/hermes/mcp/servers/external/govtrade-mcp/) covers congressional trading with per trade anomaly scoring and is the closest match on the political side, while Signal8 answers the same filings as a full register with profit and loss, committees and donors beside them.

The distinction that earns the file is the direction of the arithmetic. Every other filings entry tells you what a company reported. Signal8 tells you how much stock can still arrive, how much float it dilutes, when the shelf cap binds, and how many months of cash is left to fund it, each figure cited to the filing it was read from.

## What this pass did not establish

Nothing past `tools/list` was measured. The dilution score, the baby shelf recomputation, the runway calendar and the political profit and loss are the vendor's descriptions and the published tool schemas, not outputs seen in this pass. A score out of 100 is only as good as its seven inputs, and this pass could not verify that any of them is read from the filing rather than inferred.

Access is a subscription rather than a key. API and MCP are included with Pro at **$59** a month or **$588** a year, and a free account cannot create an API key at all, so the practical test requires a paid account. `signal8.ai/pricing` also carries a "from $49 a month" line on the same page, which reads as an annual or promotional rate rather than the monthly price.

The data is US listed only, read only, and the vendor states plainly that it is not investment advice and not a registered adviser. Nothing here was driven against a live quote, so latency, market hours behaviour and the freshness of the intraday and premarket tools are untested.

## FAQ

### Is there a free tier on the MCP server?

Discovery is free: `initialize` and `tools/list` answer with no credential. Every tool call is not. The free account covers the web app, and the hosted server needs Pro.

### What is the dilution pressure score?

A 0 to 100 score the vendor builds from seven components: shelf capacity, ATM and equity line capacity, warrants in the money, convertible proximity, cash burn urgency, historical dilution and toxic financing.

### What is baby shelf capacity?

The SEC Form S-3 General Instruction I.B.6 limit, which caps what an issuer with less than a 75 million dollar public float may sell off an effective shelf at one third of the float, less takedowns already made in the trailing twelve months. Signal8 recomputes it against the live float.

### How many tools does it expose?

**109** on the live `tools/list`, against 107 in the README and 70 plus on the mcp.so card.

### Does it work with Claude and ChatGPT?

Yes, and there the OAuth path replaces the key: add the hosted endpoint as a custom connector and sign in with a Signal8 account. Clients without OAuth send `Authorization: Bearer sk_live_...` to `https://mcp.signal8.ai/mcp`.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the full catalogue this entry belongs to
- [Silicon Floor MCP - AI and Chip Stock Research](/hermes/mcp/servers/external/silicon-floor-mcp/) - keyless as filed research over a fixed universe of AI and semiconductor companies
- [SEC EDGAR MCP - Full-Text Filing Search for Agents](/hermes/mcp/servers/external/sec-edgar-mcp/) - the filing text itself rather than a computed position on it
- [GovTrade MCP - Congressional Trading Disclosures](/hermes/mcp/servers/external/govtrade-mcp/) - STOCK Act trades with per trade anomaly scoring, paid per call
