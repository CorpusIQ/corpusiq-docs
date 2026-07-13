---
title: "Financial News MCP — Real-Time Market Data for AI Agents"
description: "Real-time financial news search by ticker, source, and language with sentiment analysis and entity extraction for AI agents."
category: mcp
tags: [mcp-server, finance, news, sentiment, market-data]
last_updated: 2026-07-12
---

# Financial News MCP Server ★ New (July 12)

Real-time financial news for AI agents — search by ticker, source, and language, with sentiment and entity data. Provides live market context for trading, research, and financial analysis workflows.

**Source:** mcp.so (submitted July 12, 2026)

## What It Is

A community MCP server delivering real-time financial news headlines and articles to AI agents. Supports search by stock ticker, news source, and language. Includes sentiment analysis scores and named entity recognition for companies, people, and financial instruments mentioned in articles.

## Business Relevance

- **Financial operators** get live news context alongside portfolio data
- **Trading teams** can correlate breaking news with price movements
- **Research analysts** can surface sentiment trends across industries
- **CorpusIQ complement** for businesses with financial data workflows

## Tools Available

| Tool | Description |
|------|-------------|
| `search_news` | Search by ticker, keyword, source, language |
| `get_sentiment` | Sentiment score for articles or tickers |
| `get_entities` | Extract companies, people, tickers from articles |
| `list_sources` | Available news sources and coverage areas |

## Quick Start

```bash
# Install via npx
npx @financial-news/mcp-server

# Or add to MCP client config
{
  "mcpServers": {
    "financial-news": {
      "command": "npx",
      "args": ["@financial-news/mcp-server"],
      "env": {
        "NEWS_API_KEY": "your-api-key"
      }
    }
  }
}
```

## Business Use Cases

1. **Market monitoring:** "Show me all news about AAPL from the last hour with sentiment scores"
2. **Competitive intelligence:** "Search for news about my top 5 competitors this week, summarize sentiment"
3. **Risk assessment:** "What's the sentiment trend on energy sector over the past 48 hours?"
4. **Earnings prep:** "Find all recent analyst mentions of MSFT ahead of earnings"

## Limitations

- Requires API key from news provider
- Sentiment analysis accuracy varies by source and language
- Real-time = minutes delay (not tick-level)
- Community-maintained; verify provider uptime

## See Also

- [Seiche Finance MCP](/hermes/mcp/servers/external/seiche-finance-mcp/) — US money market stress testing
- [AlphaVantage MCP](/hermes/mcp/servers/external/alphavantage-mcp/) — Stock fundamentals and technical data
