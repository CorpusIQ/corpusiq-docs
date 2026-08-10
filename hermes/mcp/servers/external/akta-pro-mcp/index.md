---
title: "akta.pro MCP — Integration Guide"
description: "Private company intelligence MCP — company search, structured profiles, news monitoring, and alternative signals (headcount, traffic, reviews) for AI agents."
category: mcp
tags: [mcp-server, company-intelligence, market-research, business-intelligence, due-diligence, hermes-agent]
last_updated: 2026-08-10
---

# akta.pro MCP — Private Company Intelligence for AI Agents

**Rating:** ★★ | **Category:** Business Intelligence | **Transport:** Streamable HTTP

## What It Does

akta.pro MCP connects AI assistants to a company-intelligence stack including company search, structured company profiles, news monitoring, and alternative signals like headcount trends, web traffic estimates, and review data. Published by Wokelo AI, the platform behind AI-powered due diligence. Remote server, no local install required.

## Why Business Operators Need This

Traditional company research for due diligence, partnership evaluation, or competitive analysis involves checking 5+ different data sources (LinkedIn for headcount, SimilarWeb for traffic, news for recent developments, review sites for sentiment). akta.pro consolidates these into a single MCP connection — your agent can pull a comprehensive company profile with structured data and alternative signals in one call. For operators evaluating vendors, partners, acquisition targets, or competitors, this compresses hours of manual research into seconds.

**Competitive landscape:** Similar to Fund Momentum MCP (VC intelligence, also new this sweep) but broader — Fund Momentum focuses on VC/investor signals while akta.pro covers general company intelligence. More structured than Sugra API MCP (catalogued earlier, 1,500+ endpoints across 36 domains) but narrower in scope — Sugra covers macroeconomic data while akta.pro focuses on company-level intelligence.

## Quick Start

### Connection Details

| Field | Value |
|-------|-------|
| **Transport** | Streamable HTTP (Remote) |
| **Endpoint** | `https://mcp.akta.pro/mcp` |
| **Authentication** | OAuth (Claude/ChatGPT web) or `x-api-key` header (Cursor, VS Code, Claude Code) |
| **Publisher** | Wokelo AI ([wokelo.ai](https://wokelo.ai)) |
| **GitHub** | `akta-pro/akta.pro-mcp` |

### Claude Desktop / ChatGPT (OAuth)

OAuth sign-in on first tool call. The consent screen shows access scope before approval.

### Claude Code / Cursor / VS Code (API Key)

```json
{
  "mcpServers": {
    "akta-pro": {
      "transport": "http",
      "url": "https://mcp.akta.pro/mcp",
      "headers": {
        "x-api-key": "your_api_key_here"
      }
    }
  }
}
```

```bash
claude mcp add --transport http akta-pro https://mcp.akta.pro/mcp \
  -H "x-api-key: your_api_key_here"
```

## Key Tools

| Category | Capability | Description |
|----------|-----------|-------------|
| **Company Search** | Natural language and structured search | Find companies by name, industry, location, size, funding stage |
| **Company Profiles** | Structured data retrieval | Company overview, founding date, HQ, employee count, funding history, business model |
| **News Monitoring** | Real-time and historical news | Recent developments, press mentions, product launches, leadership changes |
| **Alternative Signals** | Headcount trends | Employee growth/decline trends (LinkedIn-derived) |
| | Web traffic estimates | Monthly visits, traffic sources, engagement metrics |
| | Review data | Aggregate review scores and sentiment from Glassdoor, G2, Trustpilot |
| **Competitive Landscape** | Industry positioning | Competitive set, market category, differentiation signals |

## Example Usage

### Due Diligence on a Vendor

Ask your agent: *"Give me a full profile on VendorX — headcount, funding, recent news, and any red flags."*

The agent pulls structured company data, recent news, headcount trends, and review sentiment. Flags unusual patterns (headcount decline + negative review spike + recent leadership departure).

### Competitive Landscape Scan

Ask your agent: *"Profile the top 5 companies in AI-powered analytics — compare headcount, funding, and traffic trends."*

The agent searches for companies in the AI analytics category, pulls profiles for the top 5, and structures a comparison table with headcount, funding, and traffic.

### Partnership Qualification

Ask your agent: *"Is PartnerCo stable enough for an enterprise integration partnership? Check their size, growth signals, and recent news."*

The agent evaluates headcount trends (growing? shrinking?), recent news sentiment, and funding recency to assess stability.

## Pricing

akta.pro requires a subscription. Check [akta.pro](https://akta.pro) for current plans. Published by Wokelo AI — the platform also offers AI-powered due diligence reports.

## Repository & Resources

| Resource | URL |
|----------|-----|
| **GitHub** | [github.com/akta-pro/akta.pro-mcp](https://github.com/akta-pro/akta.pro-mcp) |
| **Website** | [akta.pro](https://akta.pro) |
| **Docs** | [docs.akta.pro](https://docs.akta.pro/) |
| **Publisher** | [wokelo.ai](https://wokelo.ai) |
| **MCP Endpoint** | `https://mcp.akta.pro/mcp` |

## Verdict: ★★ — Strong for Due Diligence & Market Research

akta.pro consolidates company research that normally requires 5+ separate tools into a single MCP connection. The alternative signals (headcount trends, traffic, reviews) provide a more complete picture than traditional company databases that only show firmographic data. Published by Wokelo AI, a company with existing due diligence expertise, which adds credibility.

**Strengths:** Consolidates multiple company intelligence sources, alternative signals (headcount, traffic, reviews) beyond basic firmographics, OAuth + API key auth, backed by Wokelo AI (established due diligence platform), remote HTTP (no install).

**Limitations:** Requires paid subscription, data freshness depends on provider refresh cycles, alternative signals are estimates (not primary source data), GitHub repo is a listing only (server runs remotely).

**Best for:** Operators conducting vendor due diligence, partnership evaluation, competitive landscape analysis, or investment research who want company intelligence integrated into their AI agent workflows.
