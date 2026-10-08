---
title: "Market Eyes Live MCP - Stock Ratings and Mortgage Rates"
description: "Keyless stock and ETF ratings plus a daily mortgage-rate read: conviction tiers, factor scores and public validation records."
category: Finance
stars: n/a (new listing)
added: 2026-10-07
source: "mcpservers.org /all page 2 (Oct 7, 2026 evening sweep)"
relevance: ★★
tags: [stocks, etfs, ratings, mortgage-rates, market-data, research]
---

# Market Eyes Live MCP

**Free keyless MCP server that returns Market Eyes Live's MELANY ratings for U.S.-listed stocks and ETFs** - more than 11,000 tickers - plus a daily read of U.S. mortgage-rate conditions. Three read-only tools, structured output, and a public record: published ratings are graded daily against later market moves, and both the methodology and the validation feed are open.

```
Server type: Remote (Streamable HTTP at https://marketeyeslive.com/mcp)
Auth: None (free, keyless)
Docs: https://marketeyeslive.com/mcp-server
Tools: get_stock_rating, compare_stocks, get_mortgage_rate_context
Coverage: U.S.-listed stocks and ETFs only; crypto, futures and non-U.S. listings return a not-covered result
Category: Finance
Built by: Market Eyes Live
```

## Why This Matters for Operators

Most market data tells you a number; this server tells you a conviction and shows its work. A rating is a tier plus a 0 to 100 composite built from eight factor scores (valuation, quality, momentum, earnings, sentiment, catalyst, risk-adjusted, macro fit), and every result carries a source, an as-of date and a disclaimer. For operators, the mortgage-rate tool is the daily-use piece: 10-year Treasury yield and direction, MBS momentum and the rate environment, useful for anything from real-estate decisions to pricing conversations. And because published ratings are graded against what actually happened, you can judge the signal instead of trusting it.

## Tools & Capabilities

| Tool | Returns |
|---|---|
| `get_stock_rating` | conviction tier (Unfavorable, Hold, Favorable, Highest Conviction, plus Promising, Very Promising, Rising Star, Runner! and Catalyst Watch for earlier-stage names), 0 to 100 composite, the eight factor scores, flagged risks, theme context and as-of date |
| `compare_stocks` | side-by-side tiers, composites and valuation, quality and momentum scores for 2 to 5 symbols |
| `get_mortgage_rate_context` | today's read: 10-year Treasury yield and direction, MBS momentum, rate environment (falling, stable or rising) and what moves mortgage rates |

All three tools are read-only, declare an output schema and return structured content alongside the text. Class shares work in either spelling (BRK-B or BRK.B); leveraged and inverse funds never read above Hold.

## Installation

```bash
claude mcp add --transport http market-eyes-live https://marketeyeslive.com/mcp
```

claude.ai and the Claude desktop app: Settings, Connectors, add a custom connector with the URL and no authentication. ChatGPT: Plugins, then Add custom MCP server with the same URL. Gemini CLI users can install the vendor's extension.

## Business Relevance

- **Operators with real-estate exposure:** a keyless daily mortgage-rate read (Treasury direction, MBS momentum, environment) in whichever assistant you already use.
- **Investors and analysts:** tiered ratings with factor-level breakdowns and a published grading record, for quick screens before deeper diligence.
- **Advisors and finance teams:** consistent, sourced, dated rating context for client conversations, with methodology links in every result.

## Integration with CorpusIQ

CorpusIQ keeps your own numbers consistent across AI clients - revenue, customers, cash. Market Eyes adds the outside view: ask your assistant what the rate environment looks like and how a public competitor is rated, in the same conversation where CorpusIQ reads your books.

## Limitations

- U.S.-listed stocks and ETFs only; crypto, futures and non-U.S. listings return a not-covered result, and five symbols shared with futures or coins (CORN, GOLD, WTI, BTC, ETH) are deliberately not rated.
- Ratings are an informational product, not advice; every result carries a source and a disclaimer.
- Brand new listing - no third-party track record yet; the vendor's own validation feed is public and machine-readable at marketeyeslive.com/api/validation-status.

## FAQ

### Is this investment advice?

No. It is a ratings product: conviction tiers and factor scores with sources and disclaimers, and a public record of how published ratings performed.

### Does it need an API key?

No - the server is free and keyless, with stateless responses.

### Which tickers are covered?

More than 11,000 U.S.-listed stocks and ETFs. Class shares work either way; tickers outside coverage return a result that says so instead of guessing.

### How is a rating built?

A tier plus a 0 to 100 composite from eight factor scores (valuation, quality, momentum, earnings, sentiment, catalyst, risk-adjusted, macro fit). The methodology page and the grading feed are both public.

## See Also

- [ETFIQ MCP - US ETF Data for Model Portfolios](/hermes/mcp/servers/external/etfiq-mcp/)
- [AdvisorIQ MCP - Advisor CE and RIA Firm Data](/hermes/mcp/servers/external/advisoriq-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
