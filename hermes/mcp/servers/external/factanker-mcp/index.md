---
title: "Factanker MCP - Evidence-Backed Company and Bank Facts"
description: 1.18B+ evidence-backed facts about US companies, banks, nonprofits and federal spending from SEC EDGAR, FFIEC call reports, IRS 990 and USAspending - keyless remote MCP with citable fact URLs
category: Finance
stars: n/a (new listing)
added: 2026-09-04
source: "mcp.so feed"
relevance: ★★★
tags: [sec-edgar, company-financials, bank-data, nonprofits, federal-spending, evidence-citations, remote-mcp]
---

# Factanker MCP

**Remote MCP server (Streamable HTTP, keyless) serving 1.18B+ evidence-backed facts about US companies, banks, nonprofits and federal spending, each carrying a filing reference, retrieval timestamp and stable citation URL.** Built as the independent proof layer for AI answers: when an agent states a number, Factanker is the evidence behind it - anchored in SEC EDGAR filings, FFIEC call reports, IRS 990s and USAspending awards. Read-only, no API key, no signup. Operator: Enerlio GmbH.

```
Server type: Remote (Streamable HTTP)
Auth: None (keyless, read-only)
Endpoint: https://factanker.com/mcp
Tools: 6 live-verified (query templates, entity resolution, fact retrieval, search, probe history)
Pricing: Free, no signup
Category: Finance & Public Data
Built by: Enerlio GmbH (factanker.com)
```

## Why This Matters for Operators

The number you quote in a pitch, a diligence memo or a board deck is only as good as its receipt. Factanker eliminates the "where did that come from" problem by construction: every value arrives with its source filing (e.g. SEC accession number), a retrieval timestamp and a citable `fact_url`, and the answer envelope explicitly lists what was NOT claimed. Agents are instructed to replace model-memory numbers with registry results - if there is no evidence, the tool says so instead of estimating.

**Live-verified keyless.** The endpoint answered an anonymous MCP probe (server `factanker` v1.0, protocol 2024-11-05) and returned the full tool list without any account or session - an agent can enumerate and call the surface immediately.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `query_template` | Curated queries over 20 templates: org_profile, search_org, company_financials (SEC), bank_metrics (FFIEC), nonprofit_financials (IRS 990), gov_dependency, peer_percentiles, bank_ranking and more |
| `list_templates` | Self-description of every template - parameters, required fields, allowed enum values |
| `lookup_entity` | Resolve a company, bank or nonprofit to all official identifiers (CIK, LEI, EIN, UEI, RSSD, FDIC cert, NPI, QID) |
| `get_facts` | All current evidence-backed facts for one entity, each with source and citable fact_url |
| `search_facts` | Full-text search across entities and predicates |
| `mcp_server_history` | Claim history of remote MCP servers from Factanker's own periodic probes |

Example prompts: "What revenue did Exxon file for FY2025?", "Median EBITDA margin of US-listed software companies?", "How government-dependent is Lockheed Martin, over time?"

## Installation

```bash
claude mcp add factanker --transport http https://factanker.com/mcp
```

No key. The same endpoint works in Claude Code, Cursor, VS Code and any Streamable HTTP MCP client.

## Configuration

```json
{
  "mcpServers": {
    "factanker": {
      "type": "http",
      "url": "https://factanker.com/mcp"
    }
  }
}
```

No auth configuration. Cite answers with their `fact_url` (`Cite as: FACTANKER, https://factanker.com/fact/<id>`) so readers can inspect the evidence.

## Business Relevance

- **Analysts and founders** get citable company financials, bank call-report metrics and nonprofit 990 finances without filing-archive archaeology
- **Diligence and finance teams** check peer percentiles and sector summaries with every figure traceable to its primary record
- **Compliance and risk operators** quantify federal-contract dependency for suppliers and counterparties with explicit not_claimed scope

## Integration with CorpusIQ

CorpusIQ connects your own financial systems (QuickBooks, Stripe, banking feeds) as read-only context. Factanker adds the external reference layer: registry-grade facts about any US counterparty, competitor or customer - financials, identifiers, government exposure - with citations. Together they give an agent the internal books from CorpusIQ and the independently evidenced external numbers from Factanker in one conversation, which is exactly the split an audit-minded operator wants.

## Limitations

- US-only scope (SEC, FFIEC, IRS 990, USAspending) - no international filing data
- Read-only registry - no writes, no news or opinion fact-checking
- Freshness depends on retrieval timestamps per fact; not a real-time feed
- Brand new listing - rate limits and stability unproven at scale

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Signal Nodus SEC Filings MCP - Primary-Source SEC Intelligence for AI Agents](/docs/hermes/mcp/servers/external/signal-nodus-mcp)
- [LiveDataLink MCP - Live Public Data for AI Agents](/docs/hermes/mcp/servers/external/livedatalink-mcp)
- [Fruit Stand Fund Returns MCP - US Fund and ETF Performance Data](/docs/hermes/mcp/servers/external/fruitstand-fund-returns-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
