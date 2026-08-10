---
title: "Stoxly MCP — Free Stock & ETF Fundamental Analysis"
server: stoxly
rating: ★★
category: Finance
transport: Remote HTTP
auth: None (free)
added: 2026-08-10
source: mcp.so
---

# Stoxly MCP — Integration Guide

## Overview

Stoxly is a free remote MCP server providing stock and ETF fundamental analysis. It delivers a 10-point score, verdict, and key metrics for any ticker symbol — no API key, no account, no subscription required.

For business operators who need quick equity research without paid Bloomberg/FactSet subscriptions, Stoxly provides instant fundamental intelligence directly in their AI assistant.

## Relevance to Business Operators

| Use Case | Value |
|----------|-------|
| Competitor analysis | Quick fundamental score on publicly traded competitors |
| Investment screening | Filter stocks/ETFs by fundamentals before deeper research |
| Portfolio check | Get health scores on holdings without switching tools |
| Market landscape | Understand sector fundamentals at a glance |

## Setup

Stoxly is a remote MCP server — no local installation required. Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "stoxly": {
      "type": "http",
      "url": "https://mcp.stoxly.dev/mcp"
    }
  }
}
```

> **Note:** The exact endpoint URL may vary. Check the [Stoxly page on mcp.so](https://mcp.so/servers/stoxly) for the latest configuration.

## Tools

Stoxly provides fundamental analysis tools (exact tools TBD — server is brand new, added Aug 10, 2026):

| Tool | Description |
|------|-------------|
| `get_fundamentals` | Returns 10-point score, verdict, and key metrics for a ticker |
| `compare_stocks` | Side-by-side fundamental comparison of multiple tickers |

## Use Cases for Business Operators

### Competitor Financial Health Check
```
> "Get the Stoxly fundamental score for SHOP, WIX, and SQSP. Which e-commerce platform looks healthiest?"
```

### ETF Sector Analysis
```
> "Score the top 5 semiconductor ETFs by fundamentals."
```

### Quick Diligence
```
> "Before my call with Acme Corp (ACM), give me their Stoxly fundamental score and any red flags."
```

## Limitations

- **Brand new** (Aug 10, 2026) — tool surface may be limited initially
- **Fundamentals only** — no technical analysis, no real-time pricing
- **Unknown coverage** — unclear how many tickers/exchanges are supported
- **Free tier sustainability** — monitor for pricing changes as server matures

## Verdict

★★ — **Worth connecting for quick fundamental checks.** Stoxly fills the gap between "no financial MCP" and paid financial data services. Its free, no-auth model makes it zero-friction to try. For operators who do occasional equity research, this is an instant upgrade. For heavy financial users, pair with Sugra API MCP (1,500+ endpoints) or Fintel MCP for comprehensive coverage.

## Related MCP Servers in Catalog

- **Sugra API MCP** — 1,500+ endpoints across 36 data domains (★★★)
- **Fintel MCP** — Hosted financial data, real-time + historical (★★★)
- **Capital.com MCP** — CFD trading, forex, indices, commodities (★★)
- **InvestSights MCP** — Indian stock market (NSE/BSE) research (★★)
