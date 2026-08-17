---
title: Cliometry MCP
description: Measured Korean market data over MCP — SK Hynix ADR premium, realized leverage multiples, VIX regime and semiconductor relative rotation, pre-computed daily with no API key.
category: Finance
stars: n/a (new listing)
added: 2026-08-17
source: mcp.so
relevance: ★★
tags: [korean-market, market-data, sk-hynix, etf-leverage, vix, semiconductors, finance, remote-mcp]
---

# Cliometry MCP

**Remote MCP server (Streamable HTTP, no auth)** — Cliometry exposes measured Korean market data as MCP tools: values a model cannot derive on its own, already computed daily, in structured form. Four read-only tools covering the SK Hynix ADR premium, realized leverage multiples, the VIX regime, and Korean semiconductor relative rotation.

```
Server type: Remote (Streamable HTTP)
Auth: None
Endpoint: https://mcp.cliometry.com
Tools: 4 (read-only, pre-computed daily)
Pricing: free
Category: Finance
Built by: Cliometry (cliometry.com) — data CC BY 4.0
```

## Why This Matters for Operators

Market-measurement questions are where models hallucinate most confidently: a model knows what an ADR premium is, but it does not know today's number for KRX:000660, and it cannot compute a 252-trading-day decomposition from memory. Cliometry answers exactly those gaps with mechanical decompositions of past realized returns and daily-accumulated Korean series, delivered structured so no parsing is needed.

**Every response carries its own source URL, as-of date, and stated limits** — the evidence-handle pattern done right for market data. The realized-multiple tool withholds its ratio when the benchmark return is near zero because the ratio diverges there, and the VIX tool returns a fixed-threshold regime label (calm / watch / fear) that explicitly does not forecast direction. The service states plainly that it is delayed reference data for research and education, not investment advice.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `get_realized_multiple` | How many times a leveraged or inverse ETF actually moved versus its daily target, over 20/60/252-day windows — KODEX Leverage, KODEX 200 Futures Inverse 2X, SOXL, TQQQ |
| `get_adr_premium` | SK Hynix ADR (SKHY) premium or discount versus the Seoul-listed share (KRX:000660), converted to KRW |
| `get_vix_band` | CBOE VIX close with a fixed-threshold regime label |
| `get_sector_rrg` | Relative Rotation Graph snapshot for Korean semiconductor-related sectors — relative-strength ratio, momentum, quadrant |

## Installation

```bash
claude mcp add cliometry --transport http https://mcp.cliometry.com
```

No key, no account, no OAuth. One tool ships an interactive MCP Apps widget (SEP-1865), verified on mobile, web, and desktop clients.

## Configuration

```json
{
  "mcpServers": {
    "cliometry": {
      "type": "http",
      "url": "https://mcp.cliometry.com"
    }
  }
}
```

## Business Relevance

- **Semiconductor supply-chain analysts** get a daily Hynix ADR premium series without building one
- **ETF operators** can decompose leverage drift across four leveraged products with one call
- **Risk teams** get a current VIX regime label with no dashboard login
- **Korea-focused investors** get sector rotation context from a single structured endpoint

## Integration with CorpusIQ

Cliometry slots into the CorpusIQ financial-data stack as the Korea specialist. Operators running market research across the CorpusIQ connectors can treat Cliometry's pre-computed series as structured inputs alongside the cross-source analytics layer: semiconductor-cycle context beside GA4 demand signals, or VIX regime beside Stripe and QuickBooks revenue volatility for planning. Because the server is keyless and free, it works as a standing research tool an agent can query any time a Korea-adjacent question appears, with every reading carrying its source URL for the evidence trail CorpusIQ reporting requires.

## Limitations

- Brand new — no track record yet; submitted to mcp.so August 17, 2026
- Korean market only — no US or other regional coverage
- Delayed reference data, not real-time quotes; explicitly not investment advice
- Four tools only — no screening, backtesting, or portfolio functions
- Free service with no SLA; treat as research convenience, not a trading dependency

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
