---
title: "stocks.team MCP - Point-in-Time SEC Filing Facts for Agents"
description: "stocks.team exposes point-in-time SEC filing facts to AI agents through a native MCP adapter and REST API with cryptographic provenance. 47 documented operations cover filings, financial metrics and statements, market valuations, insider trades, institutional holdings, executive compensation, segment reporting and material events, each answer carrying the exact SEC source locator."
category: Finance
stars: n/a (new listing)
added: 2026-09-12
source: "mcpservers.org /all page 1 (night crawl) + vendor site stocks.team + OpenAPI at stocks.team/api/openapi.json"
relevance: ★★★
tags: [sec, edgar, financial-data, filings, investing, research, rest-api, mcp-adapter]
---

# stocks.team MCP

**Native MCP adapter + REST API (API key, beta)** - a point-in-time financial data layer built for agents and quants. Instead of parsing raw 10-K and 10-Q filings, the agent receives structured facts that keep the value, reporting period, acceptance timestamp and SEC source coordinates together, so every answer can be checked against the original filing. MCP access goes through a downloadable local adapter; REST works directly.

```
Server type: Remote REST + local MCP adapter
Auth: Server-side API key (beta account)
Endpoint: https://stocks.team/api (REST), OpenAPI at https://stocks.team/api/openapi.json
Tools: 47 documented operations (OpenAPI operationIds)
Pricing: Beta plans from $9.99/mo billed annually (Plus and Ultra tiers)
Category: Finance
Built by: stocks.team
```

## Why This Matters for Operators

Agent-generated financial answers fail in two ways: wrong periods and no evidence. stocks.team attacks both. `compareFilings` keeps fiscal-year versus amendment boundaries explicit, and every response carries provenance fields - CIK, accession number, SEC source locator - so a finance team can verify the number before it enters a memo. The point-in-time fences matter for backtests: a metric only appears if it was knowable at the observation date, which is exactly the discipline a fund or corporate FP&A team needs from agent tooling.

## Tools & Capabilities

| Area | Operations |
|---|---|
| Filings | `compareFilings`, `getFiling`, `listFilings`, `listFacts` |
| Financials | `listFinancialMetrics`, `listFinancialStatements`, `listFinancialRealityMetrics`, `listTrailingTwelveMonths` |
| Market data | `getMarketValuation`, `getPublicCompanyEvidence`, `getEntity` |
| Ownership | `listInsiderTrades`, `listInstitutionalHoldings`, `listBeneficialOwnership` |
| Governance | `listExecutiveCompensation`, `listMaterialEvents`, `listSegmentReporting` |
| Coverage | `listPublicCompanyCoverage`, `requestEntityIngestion`, `getCompanyCoverageRequestStatus` |
| Business data | `getBusinessDataset`, `getEntityIngestionStatus` |

47 operations total from the published OpenAPI contract. Coverage varies by issuer, filing and metric; unmaterialized metrics fail closed rather than guessing.

## Installation

1. Create a beta account at stocks.team, activate a plan and generate a server-side API key (keep it out of client configs).
2. For REST: call `https://stocks.team/api` with the key as the bearer Authorization header; the OpenAPI contract at `https://stocks.team/api/openapi.json` documents every operation.
3. For MCP: follow the MCP installation guide in the account to download the local adapter and point it at the API (hosted remote MCP and npm registry installation are not yet available).

## Configuration

```json
{
  "mcpServers": {
    "stocks-team": {
      "url": "https://stocks.team/api"
    }
  }
}
```

Attach the key as the authorization header on every request. All data requests are authenticated, quota-controlled and tied to the published evidence contract.

## Business Relevance

- **Research analysts** get structured financial facts with SEC source coordinates instead of raw filing text.
- **Quants** use point-in-time fences for backtests where lookahead bias invalidates results.
- **Corporate FP&A** pulls peer financials, insider trades and institutional holdings for board materials.
- **Compliance teams** get provenance on every number before it reaches an external document.

## Integration with CorpusIQ

stocks.team supplies the external financial evidence layer that CorpusIQ reports currently lack. A CorpusIQ agent building an investor update can pull `listFinancialMetrics` and `getMarketValuation` for peer companies and fold them into the same report as the operator's own business data, with every external figure carrying a verifiable SEC citation next to CorpusIQ's first-party numbers.

## Limitations

- Beta product with issuer-dependent coverage; availability varies by company, filing and metric.
- MCP requires a local adapter today - no hosted remote MCP endpoint or npm package yet.
- Paid plans only (from $9.99/mo billed annually); no free tier beyond the beta evaluation.
- Not a market quotes feed: filings, metrics and provenance, not real-time prices.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [SEC EDGAR MCP - Full-Text Filing Search for Agents](/hermes/mcp/servers/external/sec-edgar-mcp/)
- [Alpha Sophia MCP - US Healthcare Provider and Market Data](/hermes/mcp/servers/external/alpha-sophia-mcp/)
