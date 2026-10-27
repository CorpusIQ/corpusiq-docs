---
title: "SpendQuery MCP - Federal Contract Data for Agents"
description: "Ask US federal spending and contracting questions in plain English and get the query, the SQL and the caveats back, from USAspending and SAM.gov."
category: Business Intelligence / Government
stars: n/a (free, no sign-in)
added: 2026-10-27
source: "live MCP probes on api.spendquery.com/mcp (initialize 200, tools/list 200, thirteen tools), the vendor llms.txt and developers page describing the same endpoint, and the mcpservers.org listing"
relevance: ★★★
tags: [federal-contracts, usaspending, sam-gov, govcon, naics, far, procurement, keyless]
last_updated: "2026-10-27"
---

# SpendQuery MCP

**Every business development conversation about government work starts with a number nobody in the room can produce: who bought this, for how much, from whom, and under which rule. The data is public. It is also spread across USAspending, SAM.gov, the FAR in the eCFR and SBA's size tables.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://api.spendquery.com/mcp
Transport:   JSON-RPC over POST
Auth:        none, no sign-in, read-only
Tools:       13, listed below
Data:        USAspending prime awards FY2023 to FY2026 (through
             Sep 30, 2026), SAM.gov notices, FAR and DFARS from
             the eCFR, SBA size standards, SBIR and STTR awards
Built by:    SpendQuery (spendquery.com)
```

## Why This Matters for Operators

A company chasing federal work needs four answers before it can decide whether to bid: the agency actually spends on this, the money is real and recent, the buyer's notice says what they need, and the company is small enough under the size standard for that NAICS code.

An assistant with web search produces a plausible paragraph about federal contracting. This server produces the figure with the query that produced it, and it separates an obligation from an outlay, which is the distinction that makes a spending number mean what the operator thinks it means. Amounts here are obligations, money committed, not money paid out.

## What It Actually Does

`initialize` on `https://api.spendquery.com/mcp` returns HTTP 200 with prompts and resources alongside tools, and its instructions tell a client to call `get_catalog` once first: the catalog carries metrics, dimensions, the QueryPlan JSON schema, planning rules and worked examples. `tools/list` returns thirteen tools:

| Tool | What it answers |
|---|---|
| `get_catalog` | What the server can answer: coverage, metrics, dimensions and the QueryPlan schema. |
| `run_plan` | Runs a QueryPlan and returns status `ok`, `clarify`, `unsupported` or `error` with a one paragraph answer and the caveats. |
| `search_codes` | Agency, bureau, state, county, NAICS, PSC and program codes and their official names. |
| `search_recipients` | Award recipients by name or UEI, with parent, listed codes and registration. |
| `browse_codes` | What the government buys, with contract spend, by PSC or NAICS. |
| `get_notice` | One SAM.gov contract notice as a decision card: what the buyer needs, blockers, unknowns. |
| `size_standard` | SBA small business size standards from 13 CFR 121.201 by code, prefix or plain industry words. |
| `naics_finder` | Plain description of the work in, the NAICS codes buyers actually use out. |
| `vehicle_match` | The shared contract vehicles for a NAICS code and optional agency. |
| `search_far` | Search the FAR and DFARS as codified in the eCFR. |
| `get_far_section` | One FAR or DFARS section in full, with the sections it references and the ones referencing it. |
| `search_local_bids` | State, county and city bids and contracts from governments that publish them as open data. |
| `sbir_awards` | SBIR and STTR awards since 1983, by year, phase, agency and recipient. |

The design decision worth noting is `run_plan`: the answer arrives with the query and the SQL, so a figure can be re-run and checked instead of accepted.

## The Part That Costs You Something

A wrong federal figure is expensive in a specific way: it turns into a bid decision, a capability statement or a forecast.

- **Obligations are not outlays.** Every amount is committed money. Revenue recognised under a contract is a different number and this server does not report it.
- **Data ends at the fiscal year boundary.** Prime awards run FY2023 through Sep 30, 2026. A question about next quarter is a question about notices, not awards.
- **SAM.gov notices expire.** A notice is a live opportunity with a deadline, so the notice tool answers about the notice, not about the contract that follows.
- **Free tier only covers what it covers.** Federal prime awards, notices, the FAR, SBA standards, SBIR and local bids. Subawards and state-level checkbooks are covered only where those governments publish them as open data.

## How It Is Contained

- **No account, no key.** There is nothing to hold and nothing to leak, and the surface is read-only.
- **Every answer names its source and as-of date.** The vendor states each page shows its source and freshness, and the tool results carry the caveats that apply.
- **Ambiguity is a status, not a guess.** `run_plan` returns `clarify` or `unsupported` rather than a confident wrong figure, which is the behaviour an operator needs when the answer will be forwarded.

## Limitations Recorded

- The vendor llms.txt lists twelve tool names; the live `tools/list` returns thirteen.
- Contract award data lags filing, so a very recent award may exist in SAM.gov or a press release before it appears in the awards data.
- Gap analysis, competitor strategy and bid pricing are outside the surface; this is the public record, not advice.
- Local bid coverage depends on which governments publish open data, so a city that does not publish is simply absent.

## FAQ

### Can an assistant tell me whether to bid?
No, and it should not be asked to. What it can do is put the agency's spend, the notice's requirements, the size standard and the available vehicles in front of the person deciding, each with a source.

### How is this different from asking a model about government spending?
The model answers from memory of news. This answers from the awards data with the query attached, distinguishes obligations from outlays, and returns `unsupported` when the question is outside its coverage.

### What should I test first?
One product category, one agency and one NAICS code: `naics_finder`, then `browse_codes` for the spend, then `search_recipients` for who is winning it, then `size_standard` to see whether the company is small enough to compete.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [TED Tender Monitor - EU public procurement](/hermes/mcp/servers/external/)
- [CorpusIQ connectors for CRM and business data](/hermes/mcp/)
