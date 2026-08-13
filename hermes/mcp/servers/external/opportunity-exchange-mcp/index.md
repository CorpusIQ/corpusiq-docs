---
title: Opportunity Exchange MCP — Saskatchewan Labour-Market Data
description: "Setup and usage guide for Opportunity Exchange MCP — Saskatchewan Labour-Market Data. Part of the Hermes resource directory."
last_updated: 2026-08-12
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/opportunity-exchange-mcp/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# Opportunity Exchange MCP — Saskatchewan Labour-Market Data

**Priority:** HIGH | **Category:** Government / Procurement / HR  
**Transport:** Remote Streamable HTTP | **Auth:** None (keyless)  
**Website:** https://veilpoint.ca/agents  
**MCP Registry:** `ca.veilpoint/opportunity-exchange`  
**Discovered:** July 27, 2026 (chatmcp/mcpso #3316)

## What It Does for Operators

Opportunity Exchange exposes Saskatchewan (and Canadian) labour-market data with the economic context that makes it a decision. It covers measured wages for all 516 NOC 2021 occupations (Statistics Canada data), CMHC average rents and vacancy rates for 178 centres, provincial trade flows, occupation profiles, and discretionary-income outcomes.

**Every answer carries truth-state metadata** — agents always know whether a number is a live measurement, a statistical aggregate, a preview, or synthetic demonstration data. This is critical for operators making procurement, hiring, or government-contract decisions where data provenance matters.

## Installation

```bash
# Remote endpoint, no install required
# No auth needed — keyless, CORS-open
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "opportunity-exchange": {
      "url": "https://veilpoint.ca/mcp",
      "transport": "streamable-http"
    }
  }
}
```

## Tools (18)

Key tools include:
| Tool | Description |
|------|-------------|
| `list_roles` | All 516 NOC occupations with wage data |
| `get_role` | Detailed profile for one occupation |
| `compare_roles` | Side-by-side wage/outlook comparison |
| `search_jobs` | Job postings with wage context |
| `discretionary_income` | What a wage leaves after rent, tax, commuting |
| `pathway_evaluation` | Request-scoped career pathway analysis |

## Operator Use Cases

1. **Government RFP pricing:** When bidding on Canadian government contracts, pull occupation-level wage data to justify labour rates with StatCan-sourced evidence
2. **Office location planning:** Compare CMHC rent data + wage data across 178 centres to optimize where to open/expand operations
3. **Competitive hiring analysis:** Use `compare_roles` to benchmark your compensation against provincial averages for specific NOC codes
4. **Grant applications:** Pull occupation profiles with truth-state metadata to substantiate labour-market claims in funding proposals
5. **Immigration/relocation planning:** Use `discretionary_income` calculations to assess whether a salary in Saskatoon vs Vancouver actually leaves an employee better off

## CorpusIQ Angle

**Complementary — government vertical.** CorpusIQ's financial data sources (QuickBooks, Stripe) combined with Opportunity Exchange's labour-market data would let operators model total cost of workforce expansion across Canadian provinces. This is a differentiated capability for operators bidding on Canadian government contracts.

## Limitations

- Geographic scope: Saskatchewan-first, Canada-wide for some data
- CMHC data covers 178 centres (not all municipalities)
- Keyless access has per-client rate limiting (self-pacing via `RateLimit-*` headers)
- Operated by VeilPoint — single-entity dependency
