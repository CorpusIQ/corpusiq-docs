---
title: KPI Depot MCP Server Integration Guide
description: KPI intelligence for AI agents — access 20,000+ corporate KPI definitions, formulas, and 30,000+ industry benchmarks. Build data-driven strategies with real benchmark data.
category: mcp
tags: [mcp, kpi, benchmarks, business-intelligence, strategy, analytics, metrics, hermes-agent]
last_updated: 2026-07-21
---

# KPI Depot MCP — KPI Intelligence for Hermes Agent

KPI Depot MCP gives your AI agent access to the world's largest structured KPI database — 20,000+ KPI definitions with formulas, 30,000+ industry benchmarks with source attribution. Plan strategies, set targets, and evaluate performance against real industry data.

## What It Does

KPI Depot MCP brings benchmark intelligence to agent workflows:

- **KPI definitions** — 20,000+ KPIs with exact formulas, data sources, and calculation methods
- **Industry benchmarks** — 30,000+ source-attributed benchmarks across sectors, company sizes, and regions
- **KPI discovery** — Search by business function, industry, or metric category
- **Target setting** — Set data-backed targets based on peer performance percentiles
- **Performance gap analysis** — Compare your metrics to industry quartiles

## Quick Setup

### Prerequisites
- **KPI Depot account:** Sign up at [kpidepot.com](https://kpidepot.com)
- **API key:** Generate from your KPI Depot dashboard
- **The MCP server is remote-hosted** — no local installation required

### Add to Hermes Agent

```json
{
  "mcpServers": {
    "kpidepot": {
      "command": "npx",
      "args": ["-y", "@kpidepot/mcp-server"],
      "env": {
        "KPIDEPOT_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

## Key Capabilities

| Tool | Description |
|------|-------------|
| `search_kpis` | Search 20,000+ KPI definitions by keyword, function, or industry |
| `get_kpi_detail` | Get full KPI detail: definition, formula, data sources, calculation guide |
| `get_benchmarks` | Pull industry benchmarks for a specific KPI (by sector, size, region) |
| `compare_to_benchmark` | Compare your metric to industry quartiles (25th/50th/75th percentile) |
| `list_categories` | Browse KPI categories: Marketing, Sales, Finance, Operations, HR, Product |
| `get_peer_group` | Find peer companies by industry, revenue band, employee count |
| `benchmark_report` | Generate a full benchmark report for a set of KPIs |

## Use Cases for Business Operators

### 1. Board Deck Data
Generate data-backed performance context:

```
Agent prompt: "I'm preparing our Q3 board deck. For our 5 core metrics
(CAC, LTV, churn, NPS, gross margin), pull SaaS industry benchmarks
for companies our size ($5-20M ARR). Show our actuals vs 50th and 75th
percentile. Format as a comparison table."
```

### 2. Investor Pitch Metrics
Validate your metrics against the market:

```
Agent prompt: "We pitch investors next week. Pull benchmarks for
B2B SaaS Series A companies: CAC payback period, net dollar retention,
gross margin, and magic number. Where do we need to improve to be
in the top quartile? What's table stakes for Series A?"
```

### 3. KPI Program Design
Design a measurement framework for a new initiative:

```
Agent prompt: "We're launching a customer success function. What are
the standard KPIs for B2B SaaS customer success? Pull the top 10 with
formulas and benchmarks. Recommend which 5 we should track first
and what good looks like at our stage."
```

### 4. Quarterly Business Review Prep
Automate QBR data preparation:

```
Agent prompt: "Pull benchmarks for all 12 KPIs in our Q3 scorecard.
For each, show: our Q3 actual, industry median, top quartile, and
our percentile rank. Flag any metric where we're below the 25th
percentile — those need a remediation plan."
```

## Integration with CorpusIQ

KPI Depot MCP + CorpusIQ = data-backed strategy execution:

1. **CorpusIQ GA4 connector** → pull your actual marketing metrics
2. **CorpusIQ Stripe connector** → pull your actual financial metrics
3. **KPI Depot MCP** → compare your actuals to industry benchmarks
4. **AI agent** → produce "where we stand" reports automatically

Your agent becomes a strategy analyst that doesn't just report your numbers — it tells you how your numbers compare to the market and what to do about it.

## Pricing

- **KPI Depot MCP:** Remote MCP server (no local install)
- **KPI Depot:** Check [kpidepot.com](https://kpidepot.com) for current API pricing
- **Free tier:** Typically offers limited benchmark access for evaluation

## Limitations

- Remote MCP server requires internet connectivity at all times
- Benchmark data currency depends on KPI Depot's update frequency
- Industry coverage strongest in: SaaS, ecommerce, financial services, healthcare
- Regional benchmarks primarily US and Western Europe; emerging markets have thinner data

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Overview](/hermes/mcp/)*
