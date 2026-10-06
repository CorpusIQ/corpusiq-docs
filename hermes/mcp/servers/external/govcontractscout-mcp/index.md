---
title: "GovContractScout MCP - State and Local Contracts"
description: "Search live US state and local government contracts from any agent: 50-state procurement data, NAICS lookup, fit scoring and win-likelihood signals."
category: Sales & Outreach
stars: n/a (npm package, MIT)
added: 2026-10-05
source: "mcpservers.org /all"
relevance: ★★
tags: [government, contracts, procurement, sam-gov, naics, bidding, npx, self-hosted, stdio]
---

# GovContractScout MCP

**The state and local half of the government market, inside your agent.** GovContractScout exposes US state and local government contracts to AI agents: search live opportunities from 50-state procurement portals, pull the full solicitation, look up NAICS codes, and score a contract's fit for a business profile. It runs locally over stdio through npx, wraps the same public API as scout.govbidportals.com, and gives federal-focused tooling its state and local counterpart.

```
Server type: Local (stdio, npx)
Auth: GovContractScout API key (free tier works, 100 calls/month)
Requires: Node.js 18+
Install: npx -y govcontractscout-mcp
Package: govcontractscout-mcp (MIT)
Built by: GovContractScout
```

## Why This Matters for Operators

Most government-contracting attention goes to the federal market, but state, county and municipal procurement is where a large share of contracts actually get awarded, and it is fragmented across dozens of portals. GovContractScout aggregates those portals into one API and mirrors it into MCP tools, so a small business can ask "find open IT services contracts in California due this month, then score the top one for a 10-person consulting firm" and get both steps done in one agent run.

**Fit scoring is built in.** `score_contract` matches a contract against a business profile, and on paid tiers `win_likelihood` estimates odds against the historical award archetype, with `archetypes` listing who typically wins what. Coverage is honest by design: contracts carry a `data_quality` field that says which fields are populated, so the agent knows what it is missing.

## Tools

| Tool | What it does |
|---|---|
| `search_contracts` | Search active contracts by state, NAICS or keyword; returns title, agency, due date and match signals |
| `get_contract` | One contract's full record by id, including the original solicitation link and documents |
| `search_naics` | Look up NAICS codes by keyword |
| `get_states` | List indexed states with live contract counts |
| `score_contract` | Score a contract's fit for a business profile |
| `win_likelihood` | Estimate win probability vs the historical award archetype (paid tier) |
| `archetypes` | List winning-business archetypes, who wins what (paid tier) |

List and search results deliberately omit source URLs and raw portal fields; the full record with the original solicitation link comes from `get_contract`, exactly as the underlying API serves it.

## Installation

Claude Code:

```bash
claude mcp add govcontractscout \
  --env GCS_API_KEY=gcs_live_YOUR_KEY \
  -- npx -y govcontractscout-mcp
```

Any MCP client:

```json
{
  "mcpServers": {
    "govcontractscout": {
      "command": "npx",
      "args": ["-y", "govcontractscout-mcp"],
      "env": { "GCS_API_KEY": "gcs_live_YOUR_KEY" }
    }
  }
}
```

API keys are instant and card-free at scout.govbidportals.com; the free tier covers 100 calls a month and paid tiers raise it. An optional `GOVCONTRACTSCOUT_API_BASE` override supports self-hosted deployments.

## Business Relevance

- **Small businesses and consultancies** find and qualify state and local opportunities without learning each portal's interface.
- **Sales and capture teams** score fit and estimate win odds before spending bid effort, with archetype data on who typically wins.
- **GovTech-adjacent vendors** monitor specific states and NAICS codes on a schedule by pairing the tools with an agent run.
- **Operators new to public sector** use the agent to translate a plain capability description into NAICS codes and matching solicitations.

## Integration with CorpusIQ

Awarded contracts eventually show up in your systems; winning them starts in the market. CorpusIQ answers the inside questions: pipeline in the CRM, revenue in Stripe or QuickBooks, campaign performance in the ad platforms. GovContractScout answers the outside question of which contracts exist and which fit. Together an operator can track "what can we win" and "how is what we won doing" in one conversation, each read-only. The federal slice is already catalogued separately as GovContract Radar; the two compose into national coverage.

## Limitations

- Local stdio server: it runs on your machine through npx, not as a hosted endpoint.
- API key required even for the free tier; 100 calls/month free, then Starter at $99/mo or Growth at $199/mo.
- `win_likelihood` and `archetypes` are paid-tier tools; the rest work on the free tier.
- Coverage quality varies by state; the `data_quality` field reports which fields are populated per contract.
- The MCP server mirrors the public API, so it exposes exactly what the API exposes.

## FAQ

### Is there a free tier?

Yes. The free tier covers 100 calls a month with no card. Paid tiers ($99 Starter, $199 Growth, 17% off annual) unlock production volume and the derived-data tools.

### How is this different from a federal contracts server?

This covers US state and local government contracts from 50-state procurement portals. Federal opportunities are covered by the catalogued GovContract Radar; the two are complementary halves of the same market.

### Where does the data come from?

Live state procurement portals, updated daily, served through the same /v1 API as the public REST endpoint, with the same auth and rate limits.

### Can it write or bid for me?

No. All seven tools are read and scoring operations: search, lookup, fit scoring and win-likelihood estimates. Bidding stays in your own process.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [GovContract Radar MCP - Federal Contract Alerts](/hermes/mcp/servers/external/gov-contract-radar-mcp/)
- [mcp-sam-gov - US Government Contracting MCP Server](/hermes/mcp/servers/external/sam-gov-mcp/)
- [eCFR.io MCP - US Federal Regulations for Agents](/hermes/mcp/servers/external/ecfr-io-mcp/)
