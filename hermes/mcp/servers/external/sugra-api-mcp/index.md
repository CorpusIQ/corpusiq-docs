---
title: "Sugra API MCP — Comprehensive Business Data for AI Agents"
description: "Official MCP server for the Sugra API — 1,500+ endpoints across 36 data domains from 160+ primary sources. Markets, economics, company fundamentals, government, news, climate."
category: mcp
tags: [mcp-server, data-analytics, business-intelligence, finance, economics]
source: mcp.so
discovered: 2026-07-22
stars: 1
author: Sugra Systems, Inc.
github: https://github.com/SugraSystems
---

# Sugra API MCP

**Official MCP server** giving AI agents source-attributed access to 1,500+ endpoints across 36 data domains from 160+ primary sources. Covers markets, economics, company fundamentals, government, news, climate, and more.

## Why It Matters for Operators

Sugra API MCP is one of the most comprehensive data MCP servers yet — it gives AI agents structured access to an enormous range of business-critical data through a single MCP connection. Think of it as a Bloomberg Terminal for AI agents, but broader: not just markets, but company data, economic indicators, government statistics, news, and climate data — all source-attributed.

For CorpusIQ operators, this means your AI agent can:
- Pull real-time market and economic data alongside your QuickBooks/Stripe financials
- Research company fundamentals during competitive analysis
- Cross-reference government data with your internal business metrics
- Get source-attributed news context for investment or strategic decisions

## Technical Details

| Field | Value |
|-------|-------|
| **Transport** | Streamable HTTP (remote) |
| **Auth** | API Key |
| **Category** | Data & Analytics |
| **Source** | [mcp.so/servers/sugra-api-mcp](https://mcp.so/servers/sugra-api-mcp) |
| **Author** | Sugra Systems, Inc. |
| **Created** | July 20, 2026 |
| **Stars** | ⭐ 1 |
| **Verified** | ✅ |

## 36 Data Domains (Partial)

- **Markets:** Equities, commodities, forex, crypto, indices, futures
- **Economics:** GDP, inflation, employment, interest rates, trade balances
- **Company Fundamentals:** Financials, filings, ownership, ESG scores
- **Government:** Regulatory data, procurement, spending, census
- **News:** Source-attributed news across sectors and regions
- **Climate:** Emissions data, climate risk scores, weather patterns
- **+ 30 more domains** including healthcare, energy, agriculture, real estate

## Setup

### Claude Desktop
```json
{
  "mcpServers": {
    "sugra-api": {
      "type": "streamable-http",
      "url": "https://api.sugra.io/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_SUGRA_API_KEY"
      }
    }
  }
}
```

### Codex / Claude Code
```bash
claude mcp add sugra-api --url https://api.sugra.io/mcp --header "Authorization: Bearer YOUR_API_KEY"
```

### Cursor / VS Code
Add to `.cursor/mcp.json` or VS Code MCP settings:
```json
{
  "sugra-api": {
    "url": "https://api.sugra.io/mcp",
    "transport": "streamable-http",
    "headers": {
      "Authorization": "Bearer YOUR_SUGRA_API_KEY"
    }
  }
}
```

## CorpusIQ Integration

Sugra API MCP complements CorpusIQ's 37+ business connectors by providing external market and economic context. Use cases:

1. **Competitive Analysis:** Pull company fundamentals + market data alongside your internal financials
2. **Market Research:** Combine Sugra's economic indicators with your GA4/Stripe revenue data
3. **Risk Assessment:** Cross-reference government regulatory data with your compliance workflows
4. **Investment Decisions:** Source-attributed market data alongside your portfolio (via Mercury MCP)

## Limitations

- Requires API key from Sugra Systems (apply at sugra.io)
- 1,500+ endpoints is a lot — use tool filtering in your MCP client to avoid context bloat
- New server (1 star, July 2026) — API stability not yet proven at scale
- Remote only (no local/stdio option) — requires internet connectivity

## See Also

- [[index]] — Full external MCP catalog
- [[capital-com-mcp]] — Trading/CFD MCP
- [[fintel-mcp]] — Financial data MCP
- [[alphavantage-mcp]] — Stock market data MCP
