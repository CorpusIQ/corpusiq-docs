---
title: "pipeworx-io Business Data Suite — Industrial MCP Wrappers"
description: "Connect Tradier, EODHD, Diffbot, Coresignal, PeopleDataLabs, Shodan, SEO Backlinks, Emailable to Hermes Agent. Systematic API wrapping for business intelligence."
category: mcp
tags: [mcp-server, pipeworx, business-intelligence, finance, market-data, company-data, security]
last_updated: 2026-07-08
---

# pipeworx-io Business Data Suite — MCP Servers

## What It Is

pipeworx-io shipped 18+ MCP servers on July 2, 2026 — the single largest one-day batch in MCP ecosystem history. Their business data suite wraps major APIs for finance, business intelligence, security, marketing, real estate, and logistics.

**Pattern**: Every business API gets a clean MCP wrapper. Single dependency (TypeScript), consistent tool naming, shared configuration pattern.

## Business Data Servers

### Finance

| Server | API | Use Case |
|--------|-----|----------|
| **mcp-tradier** | Tradier Brokerage API | Real-time stock & options market data, quotes, chains |
| **mcp-eodhd** | EOD Historical Data | Global equities historical data, fundamentals, dividends |

### Business Intelligence

| Server | API | Use Case |
|--------|-----|----------|
| **mcp-diffbot** | Diffbot Knowledge Graph | Company enrichment, web content extraction, KG queries |
| **mcp-coresignal** | Coresignal API | LinkedIn-adjacent company profiles, employee insights |
| **mcp-peopledatalabs** | People Data Labs | Person/company enrichment, professional data |

### Security

| Server | API | Use Case |
|--------|-----|----------|
| **mcp-shodan** | Shodan REST API | Internet scanning, exposed services, IoT discovery |
| **mcp-pulsedive** | Pulsedive API | Threat intelligence IOC enrichment, malware analysis |

### Marketing

| Server | API | Use Case |
|--------|-----|----------|
| **mcp-seo-backlinks** | DataForSEO Backlinks | Backlink intelligence, domain authority, link profiling |
| **mcp-emailable** | Emailable API | Email verification, deliverability scoring |

### Maps & Location

| Server | API | Use Case |
|--------|-----|----------|
| **mcp-here** | HERE Maps API | Geocoding, reverse geocoding, routing, POI search, map tiles |

## Quick Start (Any Server)

```bash
# Clone
git clone https://github.com/pipeworx-io/mcp-tradier.git
cd mcp-tradier
npm install
npm run build

# Add to Hermes
hermes mcp add tradier --command "node" --args "dist/index.js" --workdir "$(pwd)" \
  --env TRADIER_API_KEY="your-key"
```

## Manual Configuration (Example: Tradier)

```json
{
  "mcpServers": {
    "tradier": {
      "command": "node",
      "args": ["dist/index.js"],
      "workdir": "/path/to/mcp-tradier",
      "env": {
        "TRADIER_API_KEY": "your-tradier-api-key"
      }
    }
  }
}
```

**All pipeworx MCPs follow this pattern** — replace `tradier` with the server name and set the appropriate API key.

## Recommended Stack for Business Operators

For a complete business intelligence workflow, combine:

```
Market Intelligence:
├── SentiSense (market sentiment, analyst ratings)
├── mcp-tradier (real-time stock/options data)
├── mcp-eodhd (historical financial data)
└── HPSILab Quant (options analytics, Monte Carlo)

Company Intelligence:
├── mcp-diffbot (web-scale company enrichment)
├── mcp-coresignal (LinkedIn-adjacent professional data)
└── mcp-peopledatalabs (person/company enrichment)

Security/Infra:
└── mcp-shodan (internet asset discovery)
```

## API Key Requirements

| Server | API Key Source | Free Tier? |
|--------|---------------|-----------|
| mcp-tradier | [tradier.com](https://tradier.com) | 30-day trial |
| mcp-eodhd | [eodhd.com](https://eodhd.com) | Yes (20 calls/day) |
| mcp-diffbot | [diffbot.com](https://diffbot.com) | Yes (1,000 calls/month) |
| mcp-coresignal | [coresignal.com](https://coresignal.com) | No |
| mcp-peopledatalabs | [peopledatalabs.com](https://peopledatalabs.com) | Yes (1,000 records/month) |
| mcp-shodan | [shodan.io](https://shodan.io) | Yes (limited) |
| mcp-seo-backlinks | [dataforseo.com](https://dataforseo.com) | No ($0.003/call) |
| mcp-emailable | [emailable.com](https://emailable.com) | Yes (250 verifications/month) |

## Why pipeworx-io Matters

The "every API gets an MCP wrapper" industrialization signals that MCP server creation is shifting from artisanal (one-off, hand-crafted) to industrial (systematic, templated). This is the same pattern that made npm/pip successful — a low-friction packaging format enables an explosion of integrations.

## Limitations

- All pipeworx MCPs are single-API wrappers — no cross-source intelligence
- Require individual API keys (no unified auth)
- New servers — limited battle-testing, expect bugs
- No TypeScript SDK abstractions — each MCP is standalone

## See Also

- SentiSense MCP — for market sentiment (zero API key)
- HPSILab Quant Finance MCP — for options analytics
- SEOforGPT MCP — for AI visibility and GEO
