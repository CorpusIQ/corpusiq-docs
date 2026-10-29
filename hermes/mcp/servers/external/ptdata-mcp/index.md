---
title: "PtData MCP - Fundamentals as They Were Known"
description: "Point-in-time US equity fundamentals from SEC filings, survivorship-free, so a backtest never sees a number that was not public yet."
category: Financial Data
stars: ★★★ (keyless 200 verified, 4 tools listed live)
added: 2026-10-29
source: "live probe of https://api.ptdata.io/mcp: initialize returned HTTP 200 with serverInfo ptdata 3.3.2, a session id was issued, and an authenticated tools/list on that session returned four tools; free tier terms from https://api.ptdata.io/docs"
relevance: ★★★
tags: [finance, sec-filings, point-in-time, backtesting, fundamentals, keyless, remote-mcp]
last_updated: "2026-10-29"
---

# PtData MCP

**Every financial model is a bet that the data it trained on was public on the date it claims. Most market data quietly fails that bet, because the row you read today carries today's restatements.**

```
Server type: Remote (Streamable HTTP, session based)
Endpoint:    https://api.ptdata.io/mcp
Auth:        none on the free tier, Bearer key on Pro and Scale
Tools:       4, verified live
Server:      ptdata 3.3.2, protocol 2025-06-18
Free tier:   120 requests per minute, 200 per day per IP, reset at UTC midnight
```

## Why This Matters for Operators

A business question about a past decision is only answerable if the numbers are frozen at the date of the decision. Ask an ordinary data source what a company's revenue was in the second quarter of last year and it tells you what the company says now, after the restatement, after the reclassification, after the amended filing. The answer is accurate for today and useless for the decision you are reviewing.

PtData's whole premise is the date argument. Each tool takes an `as_of_date` and returns what was knowable on that date.

```
get_index_constituents   index membership on a date, survivorship free
get_fundamentals         metrics for the fiscal period, with source lineage
get_filing_metadata      SEC filings available on that date, amendments linked
get_earnings_event       8-K acceptance timestamp, as-reported figures, price reaction
```

Survivorship free is the phrase that matters for anyone who has ever measured a strategy against the index as it looks today. Companies that were removed are missing from today's list, so any historical measurement built on today's list quietly excludes the failures. This server keeps them in place for the date you name.

The fourth tool is the one an operator outside finance will find most useful. An earnings event returns the 8-K acceptance timestamp and the derived price reaction, which is the honest way to ask whether a result moved the stock, rather than assuming the move happened on the calendar day the announcement appeared in the press.

## What Was Verified

An `initialize` POST returned **HTTP 200** over server-sent events with `serverInfo` name `ptdata` and version `3.3.2`, capabilities covering tools, prompts and resources, and an `io.modelcontextprotocol/ui` extension. The response carried an `mcp-session-id` header.

A second POST to `tools/list` without that header returned `Missing session ID`, and the same call with the header returned the four tools above with their descriptions. So the surface is genuinely keyless and genuinely drivable, which puts it in the small group of servers in this catalogue that were exercised rather than described.

Pricing and limits come from the vendor's own docs at `https://api.ptdata.io/docs`: free with no API key at 120 per minute and 200 per day per IP, Pro at 1,200 per minute and 15,000 per day per key, Scale at 5,000 per minute and 100,000 per day. An invalid bearer returns 401, an exceeded limit returns 429 with a `Retry-After` header and a scope naming whether the rate or the daily quota was hit.

## Limits Worth Recording

The free tier is per IP and resets at UTC midnight, so a shared office address is one allowance, not one per person. Evaluation against a full universe will exhaust 200 calls quickly.

The four tools cover equities only. There are prompts and resources on the capability list, but the tools are the retrieval surface and they are narrow by design.

Point-in-time correctness is the vendor's claim and this pass confirmed the argument in the tool schemas (`as_of_date` on every one), not the underlying data lineage. Check one restatement case you already know before trusting a model that depends on it.

## FAQ

### What does point-in-time mean here?

It means the answer is what was public on the date you name, not what is public now. Restatements, reclassifications and amended filings are excluded from dates before they existed.

### Can I use it without an API key?

Yes. The free tier answers with no credential at 200 requests per day per IP address, and the paid tiers add a Bearer key for higher volume.

### Does it cover anything besides US equities?

No. Index constituents, fundamentals, SEC filing metadata and earnings events, all US listed.

## See Also

- [Financial data servers in this catalogue](/hermes/mcp/servers/external/)
- [Connecting CorpusIQ to your own data sources](/hermes/mcp/)
