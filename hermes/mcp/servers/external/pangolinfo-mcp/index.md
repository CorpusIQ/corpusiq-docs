---
title: "Pangolinfo Amazon Data MCP — Integration Guide"
description: "19 e-commerce and IP-compliance tools — Amazon product/review/search/niche/bestseller data, AI SERP & keyword trends, WIPO trademark search, and PACER patent litigation."
category: mcp
tags: [mcp-server, e-commerce, amazon, ip-law, trademark, patent, keyword-research, competitive-intelligence, hermes-agent]
last_updated: 2026-07-31
---

# Pangolinfo Amazon Data MCP — E-Commerce & IP Intelligence

**Rating:** ★★ | **Category:** E-Commerce | **Transport:** Streamable HTTP

## What It Does

Pangolinfo consolidates 19 tools spanning Amazon marketplace intelligence and IP compliance into a single MCP server. On the e-commerce side: Amazon product data, review analysis, search ranking data, niche research, and bestseller tracking. On the IP side: AI SERP and keyword trends, local Maps POI data, WIPO global trademark search, and PACER patent litigation lookups. One MCP endpoint gives your AI agent both marketplace research and IP legal tools.

## Why Business Operators Need This

E-commerce operators spend hours switching between tools — Jungle Scout for product research, Keepa for pricing history, USPTO for trademark search, PACER for patent litigation. Pangolinfo collapses all of this into one MCP that your AI agent can query. For Amazon sellers doing competitive research and IP due diligence, or IP lawyers handling e-commerce client work, this single integration replaces 4-5 separate platforms. The WIPO trademark search + PACER patent tools make it the first MCP that bridges marketplace operations and IP compliance.

## Quick Start

```
# Remote endpoint (Streamable HTTP)
Endpoint: https://mcp.pangolinfo.com/mcp

# Python client available
pip install pangolinfo-mcp
```

### Hermes Agent Configuration

```json
{
  "mcpServers": {
    "pangolinfo": {
      "transport": "http",
      "url": "https://mcp.pangolinfo.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_PANGOLINFO_API_KEY"
      }
    }
  }
}
```

### Environment Variables

```bash
export PANGOLINFO_API_KEY="pi_..."
```

### Get a Free API Key

Visit [tool.pangolinfo.com](https://tool.pangolinfo.com) to generate a free API key.

## Key Tools

| Category | Tools | Description |
|----------|-------|-------------|
| **Amazon Product** | Product lookup, reviews, pricing history, variations | Retrieve product details, review sentiment, and price trends |
| **Amazon Search** | Keyword search, rank tracking, search volume | Find products by keyword and track search positions |
| **Amazon Niche** | Niche analysis, bestseller lists, category trends | Identify profitable niches and trending categories |
| **AI SERP** | SERP analysis, keyword trends, content gaps | AI-powered search result analysis and keyword intelligence |
| **Maps POI** | Local business search, place details | Google Maps Points of Interest data for local research |
| **WIPO Trademark** | Global trademark search, classification lookup | Search trademarks across WIPO's global database |
| **PACER Patent** | Patent litigation search, case lookup | Search US patent litigation through PACER |

## Pricing

Free API key available at [tool.pangolinfo.com](https://tool.pangolinfo.com) with rate-limited access. Paid tiers for higher volume and commercial use. See [pangolinfo.com/amazon-data-mcp/](https://www.pangolinfo.com/amazon-data-mcp/) for current pricing.

## Authentication

API key-based authentication. Register for a free key at [tool.pangolinfo.com](https://tool.pangolinfo.com). Include the key as a Bearer token in your MCP client headers.

## Source

- **GitHub:** [github.com/Pangolin-spg/pangolinfo-mcp](https://github.com/Pangolin-spg/pangolinfo-mcp) (0★, created 2026-07-31)
- **Website:** [pangolinfo.com/amazon-data-mcp/](https://www.pangolinfo.com/amazon-data-mcp/)
- **Documentation:** [docs.pangolinfo.com](https://docs.pangolinfo.com)
- **MCP Endpoint:** `https://mcp.pangolinfo.com/mcp`
- **PyPI:** `pangolinfo-mcp` (Python client)

## Verdict: ★★ — Strong E-Commerce + IP Research Combo

Pangolinfo is a solid consolidation play — takes tools that e-commerce operators and IP lawyers typically use across 4-5 separate platforms and unifies them under one MCP endpoint. The Amazon + WIPO + PACER combination is genuinely unique in the MCP ecosystem. For Amazon sellers and e-commerce operators who need IP due diligence alongside marketplace research, this saves significant context-switching.

**Strengths:** Unique e-commerce + IP combo, 19 tools across marketplace intelligence and legal research, free API key available, Python client for programmatic use, good documentation.

**Limitations:** Brand new (0 stars, created July 31, 2026 — same day), Amazon data depth vs dedicated tools unknown, PACER integration depth unclear (full docket or summary only), no historical data guarantees.

**Best for:** Amazon sellers, e-commerce operators, IP lawyers, brand protection teams, competitive intelligence analysts working in e-commerce.
