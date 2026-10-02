---
title: "ToBid MCP - Taiwan Government Tenders for AI Agents"
description: Taiwan government procurement search and intelligence over 14M+ tenders - tender search, award history, vendor win-rate reports, agency spending analysis and bid price suggestions with a free keyless remote MCP endpoint
category: Compliance
stars: n/a (new listing)
added: 2026-09-03
source: mcpservers.org
relevance: ★★
tags: [procurement, government-tenders, taiwan, bid-intelligence, public-contracts, remote-mcp, keyless]
---

# ToBid MCP

**Free, keyless remote MCP server for Taiwan government procurement intelligence over 14M+ tenders.** Ask in plain language and get tender search, full award histories, vendor win-rate reports, agency spending analysis, and a bid price suggestion engine that estimates what a case will actually close at. Published September 3, 2026 - the endpoint is live and free, no registration, paste one URL and ask.

```
Server type: Remote (Streamable HTTP, keyless)
Auth: None (public endpoint)
Endpoint: https://api.tobid.tw/mcp
Tools: 8 (search_tenders, get_tender, price_analysis, vendor_report, unit_report, compare_vendors, hot_opportunities, find_entity)
Pricing: Free, no account
Category: Procurement Intelligence
Built by: ToBid (tobid.tw)
```

## Why This Matters for Operators

Public procurement is a market most vendors ignore because the data is scattered and the language of each jurisdiction is hostile. ToBid's engine turns Taiwan's tender records into operator questions: who keeps winning this agency's work, what does the agency spend, which cases repeatedly fail and sit open (hot opportunities for new entrants), and what price should I actually bid. The live probe confirmed the surface: server `tobid v1.29.1`, all 8 tools enumerated anonymously.

**The price engine is the differentiator.** `price_analysis` returns three bid tiers (conservative / typical / aggressive) computed from historical award-to-budget ratios, choosing its comparison base by sample adequacy: similar cases by title keywords, then same agency, then same category, then the whole database.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `search_tenders` | Keyword search over title and agency name; filter tender / awarded / failed |
| `get_tender` | Full case history: every announcement, budget, award amount, winning vendor, competition (bidder count, single-bid flags), renewal status |
| `price_analysis` | Three-tier bid price suggestion from award-to-budget history |
| `vendor_report` | Win rate, known award totals, biggest client, single-bid share, frequent opponents and relative win rates, recent wins and losses |
| `unit_report` | Agency issuance scale, top suppliers, supplier concentration, competition level, busy months, recurring-cycle cases with predicted next issue dates |
| `compare_vendors` | Head-to-head record between two vendors |
| `hot_opportunities` | Repeatedly failed, still-open cases - low competition entry points (latest 10) |
| `find_entity` | Resolve partial names to official agency/vendor names and codes |

## Installation

```bash
claude mcp add --transport http tobid https://api.tobid.tw/mcp
```

No key, no account. Works in any Streamable HTTP MCP client; setup guides (in Traditional Chinese) are at tobid.tw/guide/mcp.

## Configuration

None. The endpoint is public and free by design.

## Business Relevance

Suppliers bidding into Taiwan government contracts - from air conditioning to smart streetlights - get win-rate and price intelligence without building a data pipeline. International operators entering the market get agency spending maps and a vendor landscape in chat. Procurement researchers get the single-bid share metric (library-wide average 50.1%) that flags where competition is thin.

## Integration with CorpusIQ

CorpusIQ's read-only business connectors cover a company's own financials and operations. ToBid adds the public-sector demand side: an agent preparing a market entry or a bid strategy can pair CorpusIQ's internal margin data with ToBid's award-price benchmarks and competitor win rates to set a bid that is both profitable and winnable.

## Limitations

- Taiwan procurement only; interface language is Traditional Chinese (tool descriptions are Chinese)
- Award-to-budget ratio benchmarks depend on sample sufficiency in the category
- No alerting or saved searches in the current tool surface

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [BidSkim MCP - UK Tenders and Procurement Intelligence](/hermes/mcp/servers/external/bidskim-mcp)
- [TED Tender Monitor - EU Procurement Monitoring for AI Agents](/hermes/mcp/servers/external/ted-tender-monitor)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
