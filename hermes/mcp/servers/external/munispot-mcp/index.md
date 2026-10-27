---
title: "MuniSpot MCP - Municipal Financial Statements for Agents"
description: "MuniSpot MCP puts standardized financial statements, MuniScore ratings and economic indicators for 21,000+ US municipalities behind six agent tools."
category: Finance
stars: 0
added: 2026-10-20
source: "chatmcp/mcpso issue window #5811 (submitted 2026-10-20T15:41:00Z)"
relevance: ★★★
tags: [finance, municipal-finance, public-sector, financial-statements, credit-risk, local-government, remote-mcp, api-key]
last_updated: "2026-10-24"
---

# MuniSpot MCP

**A city is a counterparty. Its financial statements have been public for decades and machine-readable for about a week. This is the first server that hands an agent 21,000 of them with a comparable structure.**

```
Server type: Remote (Streamable HTTP) at https://www.munispot.com/api/mcp
Auth: API key in the X-API-Key header (or Authorization: Bearer), same key as the REST API
Live check: unauthenticated POST initialize returned HTTP 401 with
  {"jsonrpc":"2.0","error":{"code":-32000,"message":"Missing API key ..."}}
Registry: com.munispot/municipal-data   |   npm: @munispot/mcp   |   Docs: https://www.munispot.com/mcp
Vendor: MuniSpot, munispot.com (source repository: github.com/chowdhury-raj/munispot-mcp)
```

## Why This Matters for Operators

Every Annual Comprehensive Financial Report is published, and almost none of them are comparable. One city reports its general fund by function, the next by department, a third buries transfers inside a special revenue fund. Reading three of them side by side is an afternoon of manual work, which is why the work usually does not get done and the decision gets made on a headline.

MuniSpot's contribution is standardization, not access. The vendor states it has normalized 64,700+ fiscal-year reports from 21,000+ municipalities across 50 states into a single statement structure, then attached two derived surfaces: a MuniScore rating with a factor breakdown, and economic indicators per municipality.

The operator uses are concrete. A supplier extending terms to a county checks fund balance and debt ratios before signing. A contractor bidding on a multi-year services contract checks whether the buyer can pay in year three. An accountant or advisor comparing two locations checks the same five ratios against peers instead of against a narrative. A finance team watches the municipalities it is already exposed to and reads the change, not the press release.

## The Six Tools

| Tool | What it answers |
|---|---|
| `search_municipalities` | Find municipalities by name, state and filters such as fund balance percentage or MuniScore band |
| `get_municipality` | Profile for one municipality: identifiers, type, state, coverage |
| `get_financials` | The standardized financial statements for a fiscal year: revenues, expenditures, fund balances, debt |
| `get_scores_history` | The MuniScore rating and its history with the factor breakdown |
| `compare_municipalities` | Several municipalities against the same measures, for peer and trend comparison |
| `get_economy` | Economic indicators for the municipality |

The vendor's own worked examples are a fair description of the intended altitude: which cities in Ohio have a fund balance below 15 percent and a MuniScore under 50, how the debt ratios of Phoenix, Denver and Austin compare over five years, and what the latest fiscal year looks like for Cook County.

## Access, Free Tier and Pricing

The MCP server is a first-class surface, not an afterthought: the vendor ships setup blocks for Claude Desktop, Claude Code, Cursor, VS Code and ChatGPT developer mode on the same page as the REST documentation.

- **Free API tier.** 100 calls per month, 20 calls per minute, 100 calls per day, limited to the core endpoints: entities, profiles and scores. No credit card. Enough to test whether the structure fits a workflow, not enough to run a screen.
- **Dashboard.** A 14-day trial with no card, and paid analyst plans from $6,990 a year (Professional) to $19,990 a year (Team, three seats included, additional seats at $400 per seat per month).
- **Full MCP server access** (statements, ACFR line items, all fiscal years) is listed under the Professional API plan and Enterprise, both quoted on contact. That is the honest boundary: statements are the paid surface.

Because access is an API key rather than OAuth, the credential is a secret the operator holds and can rotate, and the free tier means a key can be minted in a minute without a sales conversation.

## What It Cannot Do

- It covers US municipalities. County and city finance in other countries is a different problem with different filings.
- A standardized statement is a translation. Where a municipality reports unusually, the normalized line may not carry the nuance the original footnote carries, so a material decision still ends at the ACFR itself, which the vendor exposes as a download on the analyst plans.
- MuniScore is the vendor's own rating with a published methodology, not a bond rating from a nationally recognized agency. It is a screening signal, not a credit opinion.

## FAQ

### How is this different from the government-contract servers in this catalog?

Theirs is the money going out: awards, solicitations, procurement notices, who won what ([GovContract Radar](/hermes/mcp/servers/external/gov-contract-radar-mcp), [GovContractScout](/hermes/mcp/servers/external/govcontractscout-mcp)). This is the money already committed: what a municipality collects, spends, owes and holds. One is a pipeline question, the other a solvency question.

### Can an agent answer a question without knowing the schema?

That is the point of the tool names. An agent asks for financials for a named entity and a fiscal year, or compares three named entities, and the standardization does the work that used to be a spreadsheet exercise.

### Is the data free?

The underlying filings are public and free at the source. The normalized structure, the rating and the comparable series are the product, and the API plans above are what they cost. The free tier gives 100 calls a month against profiles and scores.

### What is the first question worth asking?

Something with a consequence attached: the fund balance and debt trend for a municipality you are about to invoice, or three peers against the same ratio. Broad browsing burns the monthly quota on questions the dashboard already answers.

## See Also

- [GovContract Radar MCP](/hermes/mcp/servers/external/gov-contract-radar-mcp)
- [GovContractScout MCP](/hermes/mcp/servers/external/govcontractscout-mcp)
- [GovTrade MCP](/hermes/mcp/servers/external/govtrade-mcp)
