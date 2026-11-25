---
title: "Investor Shelf MCP - Funders, Deals and Cited Reports"
description: "5,853 funders and 27,013 funding rounds behind a Pro key: eight published tools, page-cited reports, and no OAuth discovery document at all."
category: "Finance"
stars: "★★★"
added: 2026-11-25
source: "Surfaced as the canonical slug investorshelf in the mcpservers.org server maps read 2026-11-25 and absent from every prior sweep; registry record com.investorshelf/investor-shelf 1.0.0 with the remote https://investorshelf.com/api/mcp; a keyless initialize and the -32001 refusal on tools/list read 2026-11-25; the three well-known routes probed the same day; the vendor pages /mcp, /pricing and / for the tool list and the plan prices"
relevance: "★★★"
tags: [founders, venture-capital, fundraising, funders, startup-data, market-research, api-key, remote-mcp]
last_updated: "2026-11-25"
---

# Investor Shelf MCP

**Finding the right investor is a search problem that most founders solve with a spreadsheet and a rumour.** Investor Shelf is a library of funders, funding rounds and market reports built for that search, with every figure linked to the page it comes from, and its MCP endpoint hands the same library to an assistant so the founder's own AI writes the answer against cited pages.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://investorshelf.com/api/mcp
Auth:        a Pro API key, sent as a bearer token; no OAuth discovery
Registry:    com.investorshelf/investor-shelf 1.0.0
Pricing:     Pro $29 a month, or $24 a month billed yearly at $290; free tier without MCP
Tools:       8, named on the vendor's own MCP page and refused without a key
```

## The gate, measured

An anonymous `initialize` answers **200** on protocol `2025-06-18` with serverInfo `investor-shelf 1.0.0`, and the server's `instructions` string is the product brief in one line: *"Investor Shelf: free reports on funders and funding markets, and a directory of funders. Cite the report page numbers you are given."*

The tool list is where it closes, and it closes with a JSON-RPC error rather than an HTTP challenge:

```
POST https://investorshelf.com/api/mcp   {"method":"tools/list"}

HTTP 200
{"jsonrpc":"2.0","id":2,"error":{"code":-32001,
  "message":"A valid API key of an active Pro subscription is required:
             create one at https://investorshelf.com/account"}}
```

That is the **keyless-initialize, keyed-execution** tier with a named price in the refusal, which is more honest than a bare 401 and unusual in that the refusal text names the exact page where the key is minted. An operator reading tool output in a client that renders errors sees the next step rather than a dead end.

**There is no OAuth discovery document.** All three well-known routes answer **404**, and not with an empty body: each returns the site's own application HTML at roughly 25 KB, so a client that follows the spec's discovery path finds a web page where a JSON document was expected. The key is a static secret created in the account, sent as a bearer token. That places this server in the static-token tier of this catalog, one rung below the servers that publish a protected-resource document.

## The eight tools the vendor publishes

The vendor's `/mcp` page names the surface, so the guide can record it even though a keyless client cannot read it:

| Tool | What it answers |
| --- | --- |
| `search_reports` | reports on funders and funding markets |
| `get_report` | a report's summary, insights and figures, with page numbers |
| `find_evidence` | exact passages that answer a question, with page links to cite |
| `search_funders` | VCs, angels, private equity and lenders by country, sector and stage |
| `get_funder` | a funder's profile, contacts and latest investments |
| `search_deals` | funding rounds with amount, date, investors and source |
| `get_company` | a funded company's rounds, amounts, investors and sources |
| `active_investors` | the most active investors by country, sector and stage over 24 months |

`find_evidence` is the one worth connecting for. It returns passages rather than summaries, with the page they sit on, and the server tells the assistant to cite page numbers. For an operator who has to defend a number in a memo or a board pack, a passage with a page beats a plausible total.

## The size of the library, as the vendor states it

- **5,853 funders** and **27,013 funding rounds**, inside **86,492 records** that include **55,534 SEC filings**
- **6,289 reports and studies** and **2,398 charts**, each figure linked to the page it comes from
- Contacts for **4,801 funders**: an email and a pitch page taken from their own site

The featured reports on the front page show the register the library keeps, and each carries a hard number:

| Report | The number it leads with |
| --- | --- |
| Austrian Startup Monitor 2025 (AIT, AustrianStartups, WU, April 2026) | survey of 635 founders and managing directors; more than 3,600 startups founded in Austria since 2014, with formation numbers stagnant since the 2019 peak |
| Mobility Industry in Türkiye 2026 (startups.watch) | Turkish automotive exports of $41.5B in 2025, 28% of manufacturing exports and 17.5% of total exports |
| H1 2026 Secondary Market Review (Evercore, July 2026) | first-half 2026 secondary volume above $120 billion, the strongest first half on record and nearly 20% up year over year; 2025 full year above $226 billion |
| Global Game Industry Trend, July-August 2026 (KOCCA, August 2026) | Twitch still first in live-streaming watch time with its share down 8.3 points |
| State of Fintech 2026 (F-Prime Capital) | an index of 54 companies at a $947B market cap, 5.6x revenue multiple and 29% LTM average growth; the index rose 60% in 2025 against the S&P at 25% |

Those are the vendor's own summaries of third-party research, reproduced here as the vendor states them. The value is the provenance: each is a named publisher with a date, which is exactly what a footnote needs.

## What the plans allow

| Plan | Price | What it includes |
| --- | --- | --- |
| Free | $0 | 6,289 reports and charts at 20 pages or 10 minutes a day; 5 pages or 2 minutes without an account; 5 PDF downloads a month; first 10 pages of every funder and deal list; one investor match from Find my investor |
| Pro | $29 a month, or $290 a year | full ranked investor list with the contacts of 4,801 funders, fundraising pipeline tracking, CSV export, and the MCP key |

**MCP is a Pro feature**, stated on the MCP page itself, so the endpoint's refusal at `-32001` is the technical expression of the plan boundary rather than an outage. Sign-in is Google or an emailed link, with no password.

### Do I need the key even though initialize worked without one?

Yes. `initialize` is open on this server and `tools/list` is not, so a client that reports "connected" after the handshake is reporting reachability, not access. The first thing to check when the tool list comes back empty is the error object, because the HTTP status is 200.

### Why does an OAuth client fail to connect?

Because there is nothing to discover. The three well-known routes return the site's HTML with a 404, so a client that only supports dynamic OAuth registration has no path in. Configure the connection as an API key in an `Authorization: Bearer` header, or use a client that supports static headers.

### Which tool should a founder start with?

`search_funders` with the country, sector and stage, then `get_funder` for the contacts. The ranked "Find my investor" product is a separate application feature rather than a tool, so the MCP surface gives the directory and the evidence, not the match score.

## How this fits a CorpusIQ answer

The question "who funds seed-stage logistics in Poland, and what did they back last year" is answered here from a directory plus round records, with a passage to cite. Paired with [BADideas.fund](/hermes/mcp/servers/external/badideas-fund-mcp/), which answers what one specific fund writes and publishes its own regional medians for free, an operator gets both the directory and a sanity check on the numbers.

## See Also

- [BADideas.fund MCP - CEE Pre-Seed Fund and Portfolio](/hermes/mcp/servers/external/badideas-fund-mcp/) for a fund that answers the same questions openly and without a key
- [WeightedShares MCP - SEC Buybacks and Stock Compensation](/hermes/mcp/servers/external/weightedshares-mcp/) for company figures taken straight from SEC filings
