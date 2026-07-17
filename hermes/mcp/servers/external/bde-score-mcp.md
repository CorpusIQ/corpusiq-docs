---
title: "BDE Score MCP — Multi-Factor Stock Scoring API for AI Agents"
description: "Open-source multi-factor stock scoring MCP server (0-100) covering US, Hong Kong, and China A-Share markets. Essential for operators who need AI-accessible quantitative investment research."
category: mcp
tags: [mcp-server, finance, stocks, quantitative-analysis, investment-research, scoring]
last_updated: 2026-07-16
---

# BDE Score MCP Server ★ New (July 16)

An open-source MCP server that provides multi-factor stock scoring (0-100) across 74 stocks in US, Hong Kong, and China A-Share markets. Operators can get quantitative investment scores directly in AI conversations — no terminal, no spreadsheet, just natural language queries for stock analysis.

**Source:** GitHub (created July 10, 2026)
**Category:** Finance
**Author:** hbhqq9 (community)
**Repo:** github.com/hbhqq9/bde-score
**Stars:** 5 ⭐

## Key Features
- **Multi-Factor Scoring:** Composite 0-100 score incorporating multiple financial factors for each stock
- **Cross-Market Coverage:** US equities, Hong Kong stocks, and China A-Shares — 74 stocks total
- **Open Source:** Free and open-source — inspect the scoring methodology, modify factors
- **MCP-Native:** Built as an MCP server for direct AI agent consumption
- **Quantitative Approach:** Rules-based scoring rather than AI-generated opinions — reproducible and auditable

## Business Relevance

Essential for operators managing cross-market investments or researching Chinese equities alongside US stocks. The MCP interface makes quantitative stock research accessible without specialized financial terminals.

**Use cases:**
- Quick stock screening across US, HK, and China markets
- Quantitative investment research in AI conversations
- Portfolio risk assessment using multi-factor scores
- Cross-market comparison — evaluate US vs HK vs China A-Share opportunities
- Integration into automated investment research pipelines

## Integration with CorpusIQ

BDE Score MCP adds quantitative investment research to CorpusIQ's financial intelligence:

```
BDE Score MCP → Quantitative stock scores and cross-market comparison
Stock Trade MCP → Real-time prices and news for scored stocks
CorpusIQ Financial → Combine with QuickBooks for portfolio vs business performance
CorpusIQ Analytics → Track market trends alongside operational metrics
```

## Limitations
- Only 74 stocks covered — limited universe focused on major names
- Early-stage project (5 stars) — verify scoring methodology before relying on it
- No real-time updates — scores are computed on-demand, not streaming
- US/HK/A-Share only — no European, Japanese, or emerging market coverage
- Scoring methodology not independently audited

*Back to [External MCP Catalog](/hermes/mcp/servers/external/)*
