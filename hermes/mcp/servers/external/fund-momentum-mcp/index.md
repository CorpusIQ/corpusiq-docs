---
title: "Fund Momentum MCP — VC Intelligence for AI Assistants"
server: fund-momentum-mcp
rating: ★★
category: Finance / Fundraising
transport: Remote HTTP
auth: API Key
added: 2026-08-10
source: mcp.so
---

# Fund Momentum MCP — Integration Guide

## Overview

Fund Momentum MCP gives AI assistants access to a database of 920+ active VC funds with live investor signals and AI-powered startup matching. For founders and operators raising capital, this replaces the manual process of searching CrunchBase, Angellist, and LinkedIn to find and qualify investors.

## Relevance to Business Operators

| Use Case | Value |
|----------|-------|
| Investor discovery | Find VCs actively investing in your sector/stage |
| Signal tracking | Monitor which funds are deploying capital vs. paused |
| Fundraising prep | Match your startup against active funds before outreach |
| Competitive fundraising intelligence | See who's backing competitors |

## Setup

Fund Momentum is a remote MCP server. Add to your MCP client:

```json
{
  "mcpServers": {
    "fund-momentum": {
      "type": "http",
      "url": "https://fundmomentum.vc/_api/mcp",
      "headers": {
        "X-API-Key": "YOUR_API_KEY"
      }
    }
  }
}
```

1. Get an API key at [fundmomentum.vc](https://fundmomentum.vc/)
2. Review pricing at [fundmomentum.vc/pricing](https://fundmomentum.vc/pricing/)

## Tools

Exact tools TBD — server uses PostgREST-generated endpoints. Expected capabilities:

| Tool | Description |
|------|-------------|
| `search_funds` | Search 920+ VC funds by sector, stage, geography, check size |
| `get_investor_signals` | Live deployment signals — who's actively writing checks |
| `match_startup` | AI-powered matching of a startup profile against active funds |
| `get_fund_profile` | Detailed fund profile: partners, portfolio, thesis, check size |

## Use Cases for Business Operators

### Fundraising Prep
```
> "Find US-based seed-stage funds actively investing in B2B SaaS with $500K-$2M check sizes. Rank by recent activity."
```

### Investor Due Diligence
```
> "Before my pitch to Acme Ventures, give me their portfolio, typical check size, and recent investments in my space."
```

### Market Intelligence
```
> "Which VCs have been most active in AI operations tools in the last 6 months?"
```

## Limitations

- **VC-only** — no angel investors, no debt financing, no grants
- **920 funds** — solid but not comprehensive (vs. CrunchBase's 50K+)
- **Paid** — API key required, pricing details on website
- **US/EU focus** — unclear coverage of emerging market VCs
- **Startup matching quality unknown** — AI matching is only as good as the data

## Verdict

★★ — **Valuable for founders actively fundraising.** Fund Momentum fills a gap — there's no other VC intelligence MCP server. For operators raising a round, this saves hours of manual investor research. For operators not currently fundraising, the utility is limited. Pair with akta.pro (company intelligence) for a complete due-diligence stack: Fund Momentum for VC/investor intelligence, akta.pro for company-level data.

## Related MCP Servers in Catalog

- **akta.pro** — Private company intelligence, headcount, web traffic (★★, catalogued Aug 10 morning)
- **Competitor Tracker & Co.** — Agentic competitor intelligence (★★★, catalogued Aug 10 morning)
- **Pangolinfo MCP** — Amazon data + IP compliance tools (★★)
