---
title: "Silicon Floor MCP - AI and Chip Stock Research"
description: "Ask about 220 AI and semiconductor stocks with every figure tied to an SEC filing, plus ownership, insider trades and fund flows."
category: Finance
stars: n/a (new listing)
added: 2026-10-06
source: "mcpservers.org /all"
relevance: ★★
tags: [finance, stocks, sec-filings, ownership, insider-trading, semiconductors, free, remote-mcp]
---

# Silicon Floor MCP

**Remote MCP server (Streamable HTTP, no account, no key)** - the AI and semiconductor stock terminal, opened to agents. Eighteen read-only tools cover prices, financials, ownership, fund flows, insider trading, filings, dividends and signals across 200+ listed companies, and every figure carries the date of the data behind it and the filing it came from. Free, rate-limited, and honest about unknowns: a null means unknown, never an estimate.

```
Server type: Remote (Streamable HTTP)
Auth: None
Endpoint: https://siliconfloor.com/mcp
Tools: 18 (read-only)
Coverage: 200+ companies - chips, memory, equipment, networking, power, neoclouds, AI software, cloud giants
Pricing: Free, rate-limited
Built by: Silicon Floor
```

## Why This Matters for Operators

Anyone selling to, buying from, investing in or competing with the AI economy eventually needs the numbers behind the companies in it: who owns NVIDIA, what Broadcom's margins are doing, which funds are buying, what founders and directors are selling, whether Microchip's cash covers its dividend. That research normally means tab-hopping between filings, fund trackers and finance sites, each with its own freshness clock.

**Every answer arrives with its source and its data date, and the tools distinguish what is filed from what is inferred.** Ownership is reported as a range because two managers can report the same shares; a holder that falls below 5% stops reporting and that is not a sale; a person has one figure on Form 4 and another on Schedule 13D/G. The server says which one it is quoting - exactly the discipline a business conversation needs when someone asks "how much does Musk actually own".

The tool set is deep where it matters: `screen_companies` filters by growth, margins, valuation, size and trend; `get_figure_history` shows one number over time with restatements flagged; `get_fund_flows` reads what hedge funds and institutions did each quarter; `what_changed` answers "what happened since a date". Sources include SEC XBRL filings, Forms 13F, 13D/G and 3/4/5, Form N-PORT fund holdings, FINRA short interest and second-by-second prices while markets are open.

## Tools & Capabilities

| Tool | What it answers |
|---|---|
| `list_companies` / `get_company` | Which companies are tracked; one company at a glance - price, valuation, fundamentals, short interest |
| `get_financials` / `get_figure_history` | Income statement, balance sheet and cash flow as filed; one figure over time with the filing behind each period |
| `compare_companies` / `screen_companies` | Two to twelve companies side by side; the companies meeting your criteria |
| `get_ownership` / `get_holders` | Who owns a company and who moved; what a fund or person holds, down to restricted shares and options |
| `get_fund_flows` / `get_insider_trading` | Quarterly institutional flows, most bought and sold; CEO, founder and director purchases and sales |
| `get_filings` / `what_changed` | Recent SEC filings, classified and linked; what happened since a date |
| `get_dividends` / `get_market_overview` / `get_market` | Dividend coverage; sector breadth, leaders and segments; the sector as one market over time |
| `get_signals` / `get_price_history` / `get_news` | Technical signals with their historical return record; split-adjusted daily prices; recent headlines, marked third-party |

## Installation

```bash
claude mcp add --transport http siliconfloor https://siliconfloor.com/mcp
```

Claude web, desktop and mobile support custom connectors; ChatGPT uses developer mode and a public endpoint; Cursor, VS Code, Gemini, Grok, Perplexity and Le Chat accept the same address.

## Configuration

```json
{
  "mcpServers": {
    "siliconfloor": {
      "url": "https://siliconfloor.com/mcp"
    }
  }
}
```

Nothing personal is requested: calls are counted by tool and by day, no IP address and no conversation content. A JSON API mirror lives at `siliconfloor.com/api/v1/schema`.

## Business Relevance

- **Founders and executives** read the public comparables around them - margins, growth, ownership - without a terminal subscription.
- **Sales and BD teams** prep account conversations with current, sourced numbers about their prospects' public peers.
- **Investors and analysts** screen the sector, track insider and fund moves, and cite the filing behind each figure.
- **Content and IR teams** check a number and its date before it goes into anything public.

## Integration with CorpusIQ

CorpusIQ stays inside the business: Stripe, QuickBooks, Shopify and GA4 answer what is actually happening in the operator's own numbers. Silicon Floor covers the listed world around it - the suppliers, customers, competitors and partners that show up in those same conversations. Composed, an operator can line their own growth and margins against the public market's, with both halves sourced and date-stamped.

## Limitations

- Sector-only: 200+ AI-economy names, not the whole market.
- Read-only research, not investment advice; nothing here trades.
- Free and rate-limited to stay fast for everyone.
- Headlines are third-party text returned as data.
- Ownership history starts at the end of 2019; some fields are simply unavailable (nulls, not estimates).

## FAQ

### Where does the data come from?

SEC filings for financials and ownership (XBRL, 13F, 13D/G, Forms 3/4/5, N-PORT), FINRA for short interest, and live prices while US markets are open. Every figure carries the date behind it.

### Does it cost anything or need an account?

No. The server is free, asks for nothing personal and only reads.

### Why is ownership shown as a range?

Two managers can report the same shares, so the data comes as a range on purpose. The tools also explain when a holder dropping below 5% stops reporting, which is not a sale.

### Can the agent take actions?

No. All eighteen tools are read-only research.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [X1 Wealth MCP - Cited Family Office and Investment Records](/hermes/mcp/servers/external/x1-wealth-mcp/)
- [Zensei MCP - Keyless Sector Rotation Index](/hermes/mcp/servers/external/zensei-mcp/)
