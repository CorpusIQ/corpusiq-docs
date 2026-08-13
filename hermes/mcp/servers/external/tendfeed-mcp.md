---
title: TendFeed MCP Server Integration Guide
description: Bid/no-bid intelligence for EU public tenders — competition density, price corridors, SME fit, and beachhead rankings over 592,000 real TED contract awards. Connect procurement intelligence to Hermes Agent.
category: mcp
tags: [mcp, procurement, eu-tenders, bid-intelligence, public-contracts, ted, hermes-agent]
last_updated: 2026-07-26
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/tendfeed-mcp/"
robots: "index,follow"

---

# TendFeed MCP — EU Procurement Intelligence for Hermes Agent

TendFeed MCP gives AI agents structured intelligence on EU public tenders — observed competition density, price corridors, SME-fit scoring, and beachhead rankings for every open tender on TED (Tenders Electronic Daily). Stop guessing whether to bid and start bidding where you win.

## What It Does

TendFeed turns 592,000+ real EU contract awards into agent-actionable intelligence:

- **Competition density** — See how many bidders typically compete for tenders like yours
- **Price corridor** — Know the winning bid range before you price yours
- **SME fit scoring** — Assess whether a tender is designed for small/medium enterprises
- **Beachhead ranking** — Identify the tenders where you have the best chance of winning
- **Multi-language** — Query in your language; TED data spans all 24 EU official languages
- **Free guest tier** — Explore expired tender data with no signup or API key

## Quick Setup

### Prerequisites
- **For guest access:** Nothing — free, no signup
- **For live board:** API key from [tendfeed.eu](https://tendfeed.eu) (99 EUR/month)

### Add to Hermes Agent

```json
{
  "mcpServers": {
    "tendfeed": {
      "type": "streamableHttp",
      "url": "https://tendfeed.eu/api/mcp/tendfeed",
      "headers": {
        "x-api-key": "your_api_key"
      }
    }
  }
}
```

For guest access (expired tender board only), omit the `x-api-key` header.

### Self-Hosted (MIT License)

```bash
git clone https://github.com/tendfeed-eu/tendfeed-mcp
cd tendfeed-mcp
npm install
node index.js
```

## Key Capabilities

| Tool | Description |
|------|-------------|
| `search_tenders` | Search TED tenders by keyword, CPV code, country, value range |
| `competition_density` | Observed bidder count and win-rate stats for similar tenders |
| `price_corridor` | Winning bid range (p25-p75) for comparable contracts |
| `sme_fit` | SME suitability score based on contract size, requirements, and past awards |
| `beachhead_rank` | Rank open tenders by your estimated win probability |
| `tender_detail` | Full tender notice with deadlines, criteria, and buyer profile |

## Use Cases for Business Operators

### 1. Bid/No-Bid Decision
Stop bidding on everything — bid where the data says you win:

```
Agent prompt: "We're an SME cybersecurity consultancy in Berlin.
Show me all open EU tenders in our space this quarter. For each,
what's the typical competition, where do winning bids land on price,
and what's our beachhead ranking?"
```

### 2. Price-To-Win Analysis
Price your bid inside the observed corridor:

```
Agent prompt: "I'm bidding on a €500K IT infrastructure tender in France.
Show me the price corridor for similar contracts — what's the
p25, median, and p75 winning bid? How many bidders typically compete?
Am I pricing too high or too low?"
```

### 3. Market Entry Strategy
Find your beachhead in a new EU market:

```
Agent prompt: "We want to expand from Germany into the Dutch public
sector. What tenders in our category (CPV 72000000 — IT services)
are open in the Netherlands? Which ones have high SME-fit scores?
Show me a beachhead ranking sorted by our likely win probability."
```

### 4. Competitive Landscape Monitoring
Track what your competitors are winning:

```
Agent prompt: "Which companies have won the most cybersecurity
tenders in the EU this year? Show me their win patterns —
countries, contract sizes, competition levels. Are there
underserved segments where we'd face less competition?"
```

## Integration with CorpusIQ

TendFeed + CorpusIQ = complete procurement operations:

1. **CorpusIQ email connector** → Auto-alert when new tenders match your profile
2. **CorpusIQ QuickBooks connector** → Compare bid pricing against your actual cost structure
3. **AI agent** → Generate bid documents pre-populated with competition intelligence
4. **CorpusIQ calendar** → Track tender deadlines and submission windows

This replaces the manual "check TED daily, download PDFs, build spreadsheet, guess on price" workflow with real-time, data-driven bid intelligence.

## Pricing

- **Guest tier:** Free — expired tender board, no signup, no API key
- **Live board:** 99 EUR/month — real-time open tenders, full intelligence suite
- **Self-hosted:** MIT license, requires own TED data pipeline
- **TED data:** Public (free) from [ted.europa.eu](https://ted.europa.eu)

## Limitations

- EU-focused — no US (SAM.gov), UK (Find a Tender), or other procurement systems yet
- Live board requires paid subscription (99 EUR/month)
- Self-hosting requires building your own TED data ingestion pipeline
- Guest tier limited to expired tenders (historical analysis only)
- 0 GitHub stars — very new, watch for API stability

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Overview](/hermes/mcp/)*
