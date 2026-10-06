---
title: "ETFIQ MCP - US ETF Data for Model Portfolios"
description: "Independent US-listed ETF and benchmark data for model portfolios, with sources, as-of dates and citations on every figure, keyless and read-only."
category: Finance
stars: n/a (new listing)
added: 2026-10-06
source: "mcp.so feed (Oct 6, 2026 midday sweep)"
relevance: ★★★
tags: [etf, finance, investing, model-portfolios, market-data, remote-mcp, keyless]
---

# ETFIQ MCP

**Remote MCP server (Streamable HTTP, no API key)** - independent data on US-listed ETFs and benchmarks for model portfolios, recomputed nightly from public filings and prices. Every figure comes with its source and as-of date and a ready citation string, and the tools refuse rather than return a near match.

```
Server type: Remote (Streamable HTTP)
Auth: None (keyless, read-only)
Endpoint: https://mcp.etfiq.com
Tools: 14 read-only tools
Pricing: Free, no key
Built by: ETFIQ
Registry: via mcp.etfiq.com
```

## Why This Matters for Operators

Fund data usually comes from provider websites, stale factsheets, or an AI model doing mental maths from a training set. ETFIQ takes the opposite approach: the numbers are recomputed nightly from public filings and prices, and every answer ships with the source, the as-of date, and a citation string the model is instructed to show.

The refusal behavior is the sharpest design choice. A fund tool that cannot find a fund says so instead of returning the closest match, and `build_portfolio` says which construction choice to change rather than guessing. For anything an operator repeats to a client or an investment committee, "no near matches" is the difference between a citation and a correction.

The server is keyless and read-only: no account, no API key, no writes. `build_portfolio` takes choices about the portfolio only, never about the person, and its answers carry a not-advice line to show with them.

## Tools & Capabilities

| Area | What the agent can do |
|---|---|
| Fund lookup | Find US-listed ETFs by ticker, fund name or a word from the name; refuses rather than approximating |
| Fund profile | Issuer, desk, each figure with source and as-of date, plus a verdict against what the fund's own label promises |
| Holdings | What a fund holds by weight, with `lag_days` so an issuer-file read is never confused with a two-month-old filing |
| Themes | Every fund in a theme, largest first, with fees and S&P 500 overlap; the full published set, not a sample |
| Screening | Funds matching filters, largest first, each with net assets and the source and date of the figure |
| Page reader | Read any published ETFIQ page as text - themes, rankings, comparisons, methodology notes, dated studies - across 40,000 pages |
| Portfolio builder | Assemble a model portfolio from construction choices, with a not-advice line on every answer |

## Installation

```bash
claude mcp add etfiq --transport http https://mcp.etfiq.com
```

No sign-in and no key. Point any Streamable HTTP client at `https://mcp.etfiq.com` and the tools appear.

## Configuration

```json
{
  "mcpServers": {
    "etfiq": {
      "url": "https://mcp.etfiq.com"
    }
  }
}
```

## Business Relevance

- **Advisors and model-portfolio builders** check fees, holdings and label-promise verdicts with citations instead of factsheet archaeology.
- **Founders and operators** running a treasury or comp plan against ETFs can read a fund's holdings and fee stack in the conversation.
- **Analysts** use the 40,000-page reader to pull methodology notes and dated studies without leaving the chat.
- **Anyone** gets a citable answer with an as-of date - the format compliance-minded readers ask for.

## Integration with CorpusIQ

CorpusIQ's read-only connectors cover the operator's own numbers - QuickBooks, Stripe, Shopify, GA4 and the rest of the stack. ETFIQ covers the market side for questions that touch funds: what a fund charges, what it holds, and how it has done against its own label. Together an operator can ask one question and get both halves - the business's numbers and the market's, each with its source visible.

## Limitations

- US-listed funds only; no UCITS or non-US listings.
- Read-only research surface; it does not place, route or clear orders.
- Not advice: `build_portfolio` answers carry a not-advice line and never take personal input.
- New listing: no track record in this catalog yet.

## FAQ

### Do I need an API key?

No. The endpoint is keyless, read-only, and free to connect. Add the URL and start asking.

### What does a refusal mean?

It means ETFIQ does not publish that fund, or that a portfolio construction choice conflicts. The refusal text says which. It never substitutes a near match.

### Where do the numbers come from?

Public filings and prices, recomputed nightly. Every figure carries its source and as-of date, and every answer a citation string.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Silicon Floor MCP - AI and Chip Stock Research](/hermes/mcp/servers/external/silicon-floor-mcp/)
- [Zensei MCP - Sector Rotation Data for Agents](/hermes/mcp/servers/external/zensei-mcp/)
