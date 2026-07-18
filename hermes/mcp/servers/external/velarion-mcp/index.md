---
title: "Velarion MCP — Executive Compensation & Corporate Governance Intelligence"
description: "Deterministic executive-compensation and governance intelligence for ~3,000 US public companies as callable MCP tools. Sourced from SEC proxy filings, not LLM guesses. 8 tools, self-serve token."
category: mcp
tags: [mcp-server, finance, executive-compensation, corporate-governance, sec-data, investor-tools]
last_updated: 2026-07-18
---

# Velarion MCP Server ★ New (July 18)

## Overview

Velarion exposes deterministic executive-compensation and governance intelligence for ~3,000 US public companies through MCP tools. Every data point is sourced directly from SEC proxy filings — not LLM guesses. Investors, analysts, and compensation committees can query executive pay structures, say-on-pay votes, and governance metrics directly from their AI assistant. Built by Velarion AI at `velarion-ai/velarion-mcp`.

**Key advantage: The first MCP server dedicated to corporate governance data — turns SEC filings into conversational intelligence for investors and operators.**

## Key Features

- **8 specialized tools**: Query executive compensation, say-on-pay votes, director elections, and governance policies across ~3,000 US public companies
- **SEC-sourced data**: All data points trace back to definitive proxy statements (DEF 14A filings) — no AI hallucinations in financial data
- **Self-serve token**: Generate an API token at intel.velarion.ai and start querying immediately
- **Remote MCP**: Connect via Streamable HTTP — no local installation required. Live at `ai.velarion/company-intelligence`

## Installation

```bash
# Remote MCP — no installation needed
# Add directly to your MCP client config:

# For local dev:
git clone https://github.com/velarion-ai/velarion-mcp.git
cd velarion-mcp
npm install
```

## Configuration

```json
{
  "mcpServers": {
    "velarion": {
      "url": "https://intel.velarion.ai/mcp",
      "headers": {
        "Authorization": "Bearer your-velarion-token"
      }
    }
  }
}
```

## Business Relevance

- **Investors and analysts**: Query executive pay ratios, peer group comparisons, and say-on-pay trends across sectors without manually reading proxy statements — saves hours per company
- **Compensation consultants**: Benchmark executive compensation packages against peer groups instantly — ask your AI "compare CEO pay at Company A vs its peer group" and get SEC-verified data
- **Corporate governance teams**: Monitor governance trends, board composition changes, and shareholder proposal outcomes across competitors
- **M&A due diligence**: During acquisition research, query target company governance data alongside financial metrics — all from your AI conversation

## Integration with CorpusIQ

Velarion's corporate governance data complements CorpusIQ's 37+ business connectors by adding a governance layer to financial analysis. Combine Velarion's executive pay data with CorpusIQ's QuickBooks or Xero connectors for a complete picture of company health — financial performance plus governance quality in one AI-powered workflow.

For investor operators, pair Velarion with CorpusIQ's Stripe and GA4 connectors to correlate governance quality with revenue performance and customer acquisition efficiency across portfolio companies.

## Limitations

- **Repository maturity**: 0 stars, 0 forks as of July 2026 — very early stage. Token system and API may change
- **US public companies only**: Coverage limited to ~3,000 companies filing with the SEC — no private companies or international coverage
- **Proxy filing dependency**: Data freshness depends on SEC filing cycles — most companies file annually, so data may be up to 12 months old
- **Token required**: Requires a self-serve token from intel.velarion.ai — unclear if free tier exists

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [Financial News MCP](/hermes/mcp/servers/external/financial-news-mcp/)
- [Alphavantage MCP](/hermes/mcp/servers/external/alphavantage-mcp/)
