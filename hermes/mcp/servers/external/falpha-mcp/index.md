---
title: "fAlpha MCP - Read-Only US Equity Research for Agents"
description: "Read-only US equity research for AI agents: model signal, drivers, screener, news sentiment, analyst coverage, SEC filings, FRED macro and fundamentals."
category: Finance
stars: 0 (MIT, techbammoney/falpha-agent-kit)
added: 2026-09-29
source: "mcp.so server page (falpha.ai)"
relevance: ★★★
tags: [finance, equity-research, stocks, signals, sec-filings, macro, read-only, remote-mcp]
---

# fAlpha MCP

**Model-scored US equity research for agents, strictly read-only.** fAlpha serves its own model signal for a stock together with the drivers behind it, plus the public data around it: signal history and flips, news sentiment, analyst coverage, SEC filings, FRED macro and fundamentals. Every result states which source produced it and the date the data is for. The server never places orders.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (fAlpha account) or personal access token
Endpoint: https://agent.falpha.ai/mcp
Tools: 17, all read-only
Pricing: no-card trial token; account plans after
Category: Finance
Built by: fAlpha (falpha.ai); agent kit on GitHub (MIT)
```

## Why This Matters for Operators

Equity research workflows usually mean juggling terminals, EDGAR and news feeds. fAlpha packages them behind one endpoint with a distinctive addition: the vendor's own model signal with the drivers behind it, signal history and flips, and a screener over the covered universe. Each result is dated and source-attributed, and the server is read-only by design, so an agent cannot trade.

For operators and advisors, the practical workflows are comparison and monitoring: compare two tickers, check when a signal last flipped and what changed, screen sectors with a positive signal and improving sentiment, and summarize a 10-Q alongside its signal. No-card trial tokens are available, which keeps first-run evaluation free.

## Tools & Capabilities

| Capability group | What it covers |
|---|---|
| Signal | Current card, compare two tickers, history on a past date, performance, flips, term structure |
| Screener | Screen the covered universe, coverage check |
| News sentiment | News sentiment and its trend |
| Analyst coverage | Analyst coverage and price targets |
| SEC filings | Filings and XBRL company facts |
| FRED macro | Macroeconomic backdrop |
| Company profile | Company profile and ratios |
| Glossary | fAlpha terms, and a link to open the view on falpha.ai |

Data sources: fAlpha's own model signal and news sentiment, Financial Modeling Prep (prices, analyst targets, fundamentals), SEC EDGAR (filings, XBRL) and FRED (macro).

## Installation

```bash
claude mcp add --transport http falpha https://agent.falpha.ai/mcp
```

Then run /mcp to sign in, or attach the account token in the Authorization header (Bearer scheme). A no-card trial token is issued at falpha.ai/mcp/trial. Claude Desktop connects via Customize, then Connectors; ChatGPT via Developer mode, then Plugins.

## Configuration

```json
{
  "mcpServers": {
    "falpha": {
      "type": "http",
      "url": "https://agent.falpha.ai/mcp"
    }
  }
}
```

## Business Relevance

- **Operators and founders** track a watchlist against model signal and news sentiment
- **Advisors** compare tickers and summarize filings alongside their signal in one call
- **Analysts** screen sectors by signal and sentiment before deeper work
- **Compliance-conscious teams** get read-only access by construction: the server cannot place orders

## Integration with CorpusIQ

fAlpha adds public-market context to the private business data CorpusIQ answers from. A composed workflow: CorpusIQ reports revenue and margin trends from QuickBooks or Stripe, and fAlpha supplies the same company's public signal, analyst coverage and latest 10-Q summary. The operator reads private and public pictures side by side in one session.

## Limitations

- Read-only by design: no trading, no portfolio actions
- US equity coverage only
- The signal is model output, not investment advice
- Ongoing use requires an fAlpha account beyond the trial token

## FAQ

### Does fAlpha trade?

No. All 17 tools are read-only and the server never places orders.

### Is there a free way to try it?

Yes. A no-card trial token is issued at falpha.ai/mcp/trial; ongoing use needs an fAlpha account.

### Is the signal investment advice?

No. The signal is model output and every result states which source produced it and the date the data is for.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Gloom MCP - Bloomberg-Style Financial Terminal for AI Agents](/hermes/mcp/servers/external/gloom-mcp/)
- [SEC EDGAR MCP - Full-Text Filing Search for Agents](/hermes/mcp/servers/external/sec-edgar-mcp/)
