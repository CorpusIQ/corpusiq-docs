---
title: "Stock Market MCP Server — Integration Guide"
description: "Connect AI agents to 90+ free financial data tools — SEC filings, insider trades, FRED macro, 13F holdings, and more via the Equibles Stock Market MCP server."
category: mcp
tags: [mcp-server, finance, stocks, market-data, sec, investing]
last_updated: 2026-07-19
---

# Stock Market MCP Server — Integration Guide

**Source:** GitHub (daniel3303/stock-market-mcp-server)  
**Author:** daniel3303 / Equibles  
**Transport:** Local MCP (stdio) — `npx` runner  
**Auth:** Free tier (no card required); API key from Equibles for extended access  
**GitHub:** [github.com/daniel3303/stock-market-mcp-server](https://github.com/daniel3303/stock-market-mcp-server)  
**Stars:** ★2 (new)  
**Tools:** 90+

## What It Does

The Stock Market MCP Server is one of the **most comprehensive free financial MCP servers** on the market — 90+ tools exposing SEC filings, institutional holdings, insider and congressional trades, earnings call transcripts, short interest data, FRED macroeconomic indicators, and more. Built on the Equibles financial data platform.

AI agents can:

- **SEC Filings:** Retrieve company filings, financial statements, and disclosures directly from EDGAR
- **13F Holdings:** Query institutional investor portfolios — see what hedge funds and asset managers hold
- **Insider & Congressional Trades:** Track insider buying/selling and congressional stock trading activity
- **Earnings Calls:** Pull transcripts of quarterly earnings calls for any public company
- **Short Interest:** Monitor short interest data and borrow rates
- **FRED Macro:** Access Federal Reserve Economic Data — GDP, employment, inflation, interest rates
- **Stock Quotes:** Real-time and historical price data across global exchanges

Think of it as "Bloomberg Terminal light" — 90+ financial intelligence tools accessible through natural language conversation.

## Why This Matters for Operators

1. **Financial operators' single pane:** Instead of juggling SEC.gov, FRED, insider-trade trackers, and earnings transcripts across multiple websites, operators ask one question and get sourced answers.

2. **Free tier, no friction:** No credit card required for the free tier. Operators can start querying financial data in one terminal command.

3. **90+ tools = deep coverage:** Most financial MCPs offer 5-20 tools. Stock Market MCP's 90+ tools cover every major financial data surface operators need — from macro (FRED) to micro (individual filings).

4. **Complements the catalog:** Existing financial MCPs specialize (Alpha Vantage for stocks, Ko Financial for SEC/insider, FinData for quotes). Stock Market MCP bundles them all — making it the go-to for operators who want one financial MCP instead of three.

## Setup

### Prerequisites

- Node.js ≥18
- An MCP-compatible client (Claude, ChatGPT, Cursor, Hermes, etc.)
- (Optional) [Equibles API key](https://equibles.com) for extended access beyond free tier

### Quick Install

```bash
npx -y @equibles/stock-market-mcp-server
```

### MCP Client Configuration

Add this to your MCP client's server configuration:

```json
{
  "mcpServers": {
    "stock-market": {
      "command": "npx",
      "args": ["-y", "@equibles/stock-market-mcp-server"],
      "env": {
        "EQUIBLES_API_KEY": "your-key-here"
      }
    }
  }
}
```

For Claude Code:
```bash
claude mcp add stock-market -- npx -y @equibles/stock-market-mcp-server
```

For Hermes Agent (config.yaml):
```yaml
mcp_servers:
  stock-market:
    command: npx
    args: ["-y", "@equibles/stock-market-mcp-server"]
    env:
      EQUIBLES_API_KEY: your-key-here
```

### Usage

Once connected, ask your AI assistant:

- *"Show me Apple's latest 10-K filing"*
- *"What's the short interest on Tesla right now?"*
- *"Which hedge funds bought NVIDIA last quarter?"*
- *"Summarize Microsoft's last earnings call"*
- *"Show me congressional trades from the last month"*
- *"What's the current US unemployment rate from FRED?"*

## Tool Categories

| Category | Tools | Description |
|----------|-------|-------------|
| SEC Filings | 15+ | Company filings (10-K, 10-Q, 8-K), financial statements, exhibits |
| 13F Holdings | 10+ | Institutional investor portfolios, fund holdings, quarterly changes |
| Insider Trades | 8+ | Insider buying/selling, filing dates, transaction amounts |
| Congressional Trades | 5+ | Congressional stock trading activity, disclosure reports |
| Earnings Calls | 8+ | Transcripts, Q&A sections, sentiment analysis |
| Short Interest | 6+ | Short interest %, days to cover, borrow rates, fails-to-deliver |
| FRED Macro | 20+ | GDP, CPI, unemployment, interest rates, industrial production |
| Stock Data | 15+ | Quotes, historical prices, company profiles, fundamentals |
| Market Screens | 5+ | Pre-built screens and custom filters |

## Comparison to Other Financial MCPs

| Feature | Stock Market MCP | Alpha Vantage MCP | Ko Financial Data | FinData MCP |
|---------|-----------------|-------------------|-------------------|-------------|
| SEC Filings | ✅ Full EDGAR | ❌ | ✅ | ✅ |
| 13F Holdings | ✅ | ❌ | ✅ | ❌ |
| Insider Trades | ✅ | ❌ | ✅ | ❌ |
| Congressional Trades | ✅ | ❌ | ✅ | ❌ |
| FRED Macro | ✅ | ❌ | ✅ | ❌ |
| Earnings Transcripts | ✅ | ❌ | ❌ | ❌ |
| Short Interest | ✅ | ❌ | ❌ | ❌ |
| Stock Quotes | ✅ | ✅ | ❌ | ✅ |
| Technical Indicators | ❌ | ✅ | ❌ | ❌ |
| Free Tier | ✅ No card | ✅ Free tier | ✅ 200 calls/day | ❌ Pay-per-call |
| Total Tools | 90+ | ~15 | 24 | ~10 |

## Caveats

- **New project:** Only 2 GitHub stars — the server is days old. Expect rapid iteration and possible breaking changes.
- **Free tier limits:** The free tier has rate limits; check [equibles.com](https://equibles.com) for current pricing.
- **Financial data latency:** Real-time quotes may have 15-minute delays depending on exchange. SEC/FRED data is official and up-to-date.
- **Local only:** This is a stdio MCP server — it runs on your machine, not as a hosted remote endpoint.

---

*← [Back to External MCP Catalog](/hermes/mcp/servers/external/) | [View on GitHub](https://github.com/daniel3303/stock-market-mcp-server) →*
