---
title: "PairBook MCP - Portfolio Risk and Correlation Analysis"
description: "Local stdio MCP server over the PairBook correlation and ETF-overlap engine: whole-portfolio risk analysis with Euler risk contributions and issuer-sourced overlap warnings, plus pair correlation, beta, and volatility for 4,700+ US stocks and ETFs. Free, no key."
category: Finance
stars: n/a (new listing, github.com/vj88-coder/pairbook-mcp)
added: 2026-08-29
source: mcpservers.org /all page 1
relevance: ★★
tags: [mcp-server, finance, portfolio, correlation, etf, risk-analysis, investing, self-hosted]
---

# PairBook MCP

**A local MCP server and CLI over the PairBook engine: whole-portfolio risk analysis and pair correlation for 4,700+ US stocks and ETFs, with issuer-sourced holdings overlap between funds - free, keyless, and refreshed every trading day after the US close.** Any of the 11.3 million possible pairs can be compared: 52,000+ popular pairs come precomputed with issuer-sourced overlap, and every other combination is computed on demand from weekly return series. The server runs entirely on your machine, is read-only, and sends nothing but public data requests.

```
Server type: stdio (local); data from the free PairBook API
Auth: None (free static API, no key)
Install: npx -y pairbook-mcp (npm 1.3.0)
Tools: analyze_portfolio plus CLI pair/profile/search commands
Data: 4,700+ US stocks and ETFs, 11.3M pairs, weekly returns, refreshed each trading day
Pricing: Free with attribution (MIT)
Category: Finance / Portfolio Analytics
Built by: VoidLab (pairbook.io); repo github.com/vj88-coder/pairbook-mcp
```

## Why This Matters for Operators

Founders, executives, and finance operators hold concentrated positions and diversified funds at the same time, and the portfolio tools they can afford answer the wrong question: "what did it do" instead of "how much of this is really one bet." PairBook answers the second question with sourced numbers - QQQ and VOO holding 53.5 percent of the same stocks is the kind of finding no other portfolio tool reports, and it changes whether a position is actually diversified.

The analyze_portfolio tool returns structured JSON with Euler risk contributions, diversification ratio and independent risk bets, correlation blocks that move together, drawdown versus SPY, and overlap warnings between held ETFs. Every formula is documented in the repo methodology, invariants are covered by tests, and nothing is a forecast or advice - the assistant gets evidence, not a sales pitch.

**Portfolio concentration and hidden overlap become machine-checkable facts instead of intuition.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| analyze_portfolio | Whole-portfolio analysis: volatility, beta vs SPY, max drawdown, per-holding risk budget (share of risk vs share of capital), Euler risk contributions, diversification ratio, correlation blocks, ETF overlap warnings |
| pairbook CLI | pair comparison (correlation 1/3/5-year, beta, volatility, overlap), single-asset profile, ticker search, JSON output |

## Installation

```bash
claude mcp add pairbook -- npx -y pairbook-mcp
```

Or use the CLI directly with no install: `npx -y -p pairbook-mcp pairbook QQQ VOO`.

## Configuration

```json
{
  "mcpServers": {
    "pairbook": {
      "command": "npx",
      "args": ["-y", "pairbook-mcp"]
    }
  }
}
```

No account, no API key. The server calls a single host (pairbook.io) for public market data, identifies itself with a version string, and sends no prompts, conversation content, or personal data.

## Business Relevance

- **Founders with concentrated equity** see the risk budget per holding - what share of portfolio risk each position carries versus its capital weight.
- **Financial operators** check whether held ETFs are secretly one bet through issuer-sourced overlap before adding a fund.
- **Analysts** pull pair correlation, beta, and volatility with sourced, dated data instead of model recall.
- **Compliance-adjacent teams** get methodology-documented, test-covered numbers - defensible in an investment memo.

## Integration with CorpusIQ

PairBook complements CorpusIQ's data-driven reporting: a CorpusIQ workflow can feed an operator's portfolio question into analyze_portfolio, get the structured risk JSON, and render it through the same recap-answer path CorpusIQ uses for business data answers. It also pairs with the fundable-data layer - CorpusIQ's investor and funding research can cite PairBook's dated, DOI-published dataset as evidence when an investment narrative depends on diversification claims. PairBook runs locally with no telemetry. Portfolio questions are processed on the machine running the server, and only the public market lookups needed for correlation data are network-bound.

## Limitations

- New listing (repo created Aug 28, 2026, 1 star) with a short track record.
- US-listed stocks and ETFs only - no international coverage yet.
- Correlations run on weekly returns; it is a risk-structure specialist, not a quotes, fundamentals, or news feed (pair it with a general market-data server).
- Explicitly not investment advice - outputs are data, not recommendations.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Jawz MCP - Live Macro Reads and a Disciplined Investing Loop](/hermes/mcp/servers/external/jawz-mcp)
- [Ice Juice Trading MCP - Automated Trading on Your Alpaca Account](/hermes/mcp/servers/external/ice-juice-trading)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
