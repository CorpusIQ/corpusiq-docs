---
title: ROIC.ai MCP Server
description: Financial data MCP for AI agents — stock prices, income statements, earnings call transcripts, fundamentals, ratios, and valuation multiples for 60,000+ public companies
category: Finance
stars: n/a (commercial)
added: 2026-08-12
source: mcp.so
relevance: ★★★
tags: [finance, stocks, market-data, earnings-calls, fundamentals, fintech, remote-mcp]
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/roic-ai-mcp-server/"
robots: "index,follow"
last_updated: "2026-08-12"

---

# ROIC.ai MCP Server

**Remote MCP server (Streamable HTTP, API key) for ROIC.ai.** Brings stock market data to AI assistants over the Model Context Protocol: stock prices, financial statements, earnings call transcripts, fundamentals, ratios, and valuation multiples for more than 60,000 public companies. One server covers the whole stack — statements, earnings, and fundamentals.

```
Server type: Remote (Streamable HTTP)
Auth: API key
Endpoint: https://mcp.roic.ai/mcp
Docs: https://www.roic.ai/api/mcp
Category: Finance / Market Data
```

## Why This Matters for Operators

Financial data for agents has historically meant stitching together three or four MCPs — one for prices, one for statements, one for transcripts. ROIC.ai consolidates them: an agent can answer "what's the trend in gross margin over the last eight quarters?" or "what did the CEO say about pricing on the last earnings call?" in one query. Plain-language questions resolve to on-demand data — from a single income-statement line to a full ratio history, plus latest and historical OHLCV prices.

## Tools & Capabilities

- **Stock prices** — latest available and historical OHLCV
- **Financial statements** — income statement, balance sheet, cash flow, line-item level
- **Earnings call transcripts** — full-text access for qualitative research
- **Fundamentals & ratios** — margin trends, efficiency metrics, full ratio history
- **Valuation multiples** — for comparables analysis and market context
- **Coverage** — 60,000+ public companies

## Installation

```bash
claude mcp add roic-ai-mcp-server --transport http https://mcp.roic.ai/mcp
```

Then add your ROIC.ai API key in the client config (below). Works with Claude Code, Codex, Cursor, VS Code Copilot, and OpenAI Codex.

## Configuration

```json
{
  "mcpServers": {
    "roic-ai-mcp-server": {
      "type": "http",
      "url": "https://mcp.roic.ai/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_ROIC_API_KEY"
      }
    }
  }
}
```

## Business Relevance

- **Investors and analysts** can run multi-quarter statement comparisons and ratio histories in plain language
- **Operators** can pull competitor fundamentals — margins, growth, multiples — directly into the analysis workflow their agents already run
- **Finance teams** get earnings-call transcripts as queryable data for board-prep and Q&A
- **Founders** can keep tabs on public comps without leaving the agent environment

## Integration with CorpusIQ

ROIC.ai fills the public-market gap beside CorpusIQ's private-company data connectors. CorpusIQ handles the operational books — QuickBooks, Stripe, Shopify, GA4 — while ROIC.ai supplies the public-market view: an agent can compare a client's QuickBooks margins against public comps pulled through ROIC.ai in the same session. Pairs naturally with CorpusIQ's finance category for competitive teardowns, market sizing, and investor materials where public-company benchmarks are the missing input.

## Limitations

- Commercial hosted service — API key required, pricing on request via roic.ai
- No tool list published on directory pages; validate endpoint coverage against the docs before production use
- Public-company data only — no private market or venture data
- Live-scraped market data can lag exchange feeds; verify latency for trading-grade use
- Not self-hostable

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
