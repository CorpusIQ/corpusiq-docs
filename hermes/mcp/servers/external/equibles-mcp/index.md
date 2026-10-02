---
title: "Equibles MCP - SEC Filings and Market Data for AI Agents"
description: "Self-hosted financial data MCP server with 61 tools over primary regulatory sources - SEC filings with semantic search, XBRL fundamentals, 13F holdings, insider trades, and fund data - plus a hosted endpoint."
category: Finance
stars: 202
added: 2026-08-29
source: mcpservers.org /all page 3
relevance: ★★★
tags: [mcp-server, sec-filings, xbrl, 13f, insider-trading, market-data, funds, self-hosted]
---

# Equibles MCP

**A self-hosted, open-source financial data MCP server for AI agents built on primary regulatory sources - SEC filings with full-text and semantic search, XBRL fundamentals, 13F institutional holdings, insider and congressional trades, short interest, FRED, CFTC/CBOE data, and daily prices.** The self-hosted build exposes 61 tools, and the hosted endpoint at mcp.equibles.com/mcp runs the same core with more on top. Apache-style AGPL-3.0 licensing with a 202-star repo and an active commit history since March 2026.

```
Server type: Self-hosted (stdio) + hosted Streamable HTTP
Auth: Self-hosted (your key) / hosted (equibles.com account)
Endpoint: https://mcp.equibles.com/mcp (hosted)
Tools: 61 self-hosted (13F, insider, filings, funds, XBRL, macro, prices)
Pricing: Open source, self-hosted free; hosted tiers on equibles.com
Category: Finance / Market Data
Built by: daniel3303/Equibles (equibles.com); AGPL-3.0
```

## Why This Matters for Operators

Investor-grade market data is expensive precisely because vendors resell the same primary sources - SEC EDGAR, FRED, CFTC - with markup and lock-in. Equibles inverts that: the ingestion pipelines are open source and pointed at primary regulatory feeds, so an operator can self-host the whole stack and let agents query filings, fundamentals, holdings, and insider flows directly, or use the hosted endpoint for the same surface without infrastructure work.

The agent-facing design is the point. Strict-first tokenized searches over institution and insider names, hybrid keyword-plus-semantic search across all SEC filings, and line-range reads of filing documents mean an agent gets answers with citations to the actual filing instead of a vendor's digested summary.

**Primary-source market data with semantic filing search, self-hostable, at open-source pricing.**

## Tools & Capabilities

Grouped by data domain; the self-hosted build exposes 61 tools and the hosted endpoint runs the same core plus additions.

| Area | Representative tools |
|---|---|
| 13F institutional holdings | GetTopHolders, SearchInstitutions, GetInstitutionPortfolio, GetInstitutionConsensusHoldings, GetMarketWide13FActivity, CompareInstitutionPortfolios |
| Insider trading | GetInsiderTransactions, GetInsiderOwnership, GetForm144ProposedSales, SearchInsiders |
| SEC filings search | SearchDocuments (hybrid keyword + semantic), SearchDocument, ListCompanyDocuments, ReadDocumentLines |
| Funds, ETFs & advisers | SearchInvestmentAdvisers (Form ADV), GetInvestmentAdviser, GetFundNcenReports, GetFundsHoldingStock, GetFormDOfferings, GetFundProfile |
| XBRL fundamentals | GetFinancialStatement (income/balance/cash-flow anchored to period end) plus the full statement family |
| Macro & prices | FRED series, CFTC/CBOE data, short interest, fails-to-deliver, daily prices |

## Installation

```bash
claude mcp add --transport http equibles https://mcp.equibles.com/mcp
```

Self-hosters clone the repo and run the stdio server locally; full catalog and client setup are documented in the companion repo daniel3303/stock-market-mcp-server.

## Configuration

```json
{
  "mcpServers": {
    "equibles": {
      "type": "http",
      "url": "https://mcp.equibles.com/mcp"
    }
  }
}
```

The hosted endpoint authenticates against an equibles.com account. Self-hosted deployments run with your own API keys against the primary data sources the repo documents.

## Business Relevance

- **Investors and analysts** get semantic search across all SEC filings plus 13F and insider flows in one agent surface with filing citations.
- **Fund operators** track institutional ownership trends, consensus positions, and quarterly activity without a Bloomberg terminal.
- **Finance teams** pull XBRL fundamentals anchored to exact period ends for models instead of re-keying statements.
- **Compliance and research staff** read exact filing line ranges when an agent flags a disclosure, keeping the primary source one tool call away.

## Integration with CorpusIQ

Equibles is the market-intelligence layer that pairs with CorpusIQ's business-operations connectors: a CorpusIQ workflow reading company data from HubSpot or QuickBooks can hand the ticker or CIK to Equibles for 13F ownership, insider flows, and XBRL fundamentals, then write the cited findings back into the CRM or a recap answer. For investors running diligence alongside operating data, the combination covers both sides of a company - the operational books via CorpusIQ connectors and the public-market record via Equibles - inside one agent session.

## Limitations

- AGPL-3.0 - fine for internal use and open-source work, but review the copyleft terms before embedding in proprietary products.
- Self-hosted means maintaining the ingestion stack yourself; the hosted endpoint trades control for convenience.
- US-market focus (SEC, FRED, CFTC, CBOE) - limited international primary-source coverage.
- Hosted endpoint pricing tiers are account-based; confirm the plan before heavy production use.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Financial News MCP - Real-Time Market Data for AI Agents](/hermes/mcp/servers/external/financial-news-mcp)
- [Hermes Plant MCP Server - Deterministic Finance and Quant APIs](/hermes/mcp/servers/external/hermesplant-mcp-server)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
