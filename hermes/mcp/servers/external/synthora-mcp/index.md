---
title: "SYNTHORA MCP - Verified Multi-Source Intelligence Mesh"
description: "SYNTHORA Intelligence Mesh MCP server exposes 30 verified multi-source intelligence tools — sanctions screening, crypto market data, prediction markets, macro and maritime intel — with pay-per-call x402 USDC settlement on Base"
category: Intelligence & Compliance
stars: n/a (hosted service)
added: 2026-08-19
source: "mcp.so GitHub issue #3649"
relevance: ★★
tags: [intelligence, compliance, sanctions-screening, prediction-markets, macro-data, x402, remote-mcp, hosted]
---

# SYNTHORA MCP

**An intelligence agency for AI agents: 30 tools exposing verified multi-source data, paid per call in USDC on Base.** SYNTHORA crosses independent sources for every answer and each response declares its sources and is Ed25519-signed — crypto market data, OFAC/sanctions screening, smart-contract safety, prediction markets across Polymarket and Kalshi, maritime chokepoint intel, WHO health data, macro/FX, and weather.

```
Server type: Remote (Streamable HTTP, JSON-RPC 2.0)
Auth: None to browse tools; paid calls via x402 (USDC on Base)
Endpoint: https://mcp.hergertsynthora.com/mcp
Tools: 30
Pricing: Per-call x402 micropayments (free trial calls per wallet)
Category: Intelligence & Compliance
Built by: HERGERT SYNTHORA
```

## Why This Matters for Operators

Operators doing due diligence, compliance screening, or market research today query a dozen disconnected sources and then manually reconcile conflicts. SYNTHORA productizes the reconciliation: every answer is a multi-source verified analysis that declares which sources it crossed and its confidence, signed Ed25519 so the provenance is checkable after the fact.

The payment model removes the subscription barrier for occasional use: agents browse tools freely, pay per call in USDC over x402 on Base, and unpaid calls return a standard x402 payment challenge instead of failing silently. Compliance tools like sanctions screening and BIC/SWIFT checks sit beside market and macro data in one signed, auditable surface.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `sanctions_screen` | OFAC/EU/UN/UK sanctions screening for addresses and entities |
| `contractwatch` | Smart-contract risk and change signal for deployed contracts |
| `polymarket_markets` | Cross-platform prediction market search (Polymarket + Kalshi) |
| `daily_intel_brief` | Daily multi-source intelligence briefing |
| `gdelt_tension` | Conflict/event tension signals from GDELT |
| `chokepoint_transits` | Maritime chokepoint transit intelligence |
| `who_gho_timeseries` | WHO Global Health Observatory time series |
| `llm_fast` | Fast LLM utility endpoints |

The MCP surface exposes 30 tools drawn from a live catalog of 223 services (67 verified). Discovery: `catalog.hergertsynthora.com/catalog.json`, agent card at `api.hergertsynthora.com/.well-known/agent.json`, and `llms.txt` at `api.hergertsynthora.com/llms.txt`.

## Installation

```json
{
  "mcpServers": {
    "synthora": {
      "type": "http",
      "url": "https://mcp.hergertsynthora.com/mcp"
    }
  }
}
```

## Configuration

No API key is required to browse tools and list the catalog. Paid calls require an x402-aware wallet with USDC on Base mainnet (eip155:8453); settlement runs through the Coinbase CDP facilitator. Per-call prices are quoted live in each HTTP 402 response (example: AgentGuard pre-trade risk verdicts at 0.02 USDC). All services are scoring and analysis only — they return verdicts and never execute trades.

## Business Relevance

- **Compliance teams** run sanctions and counterparty screening from the agent session with signed, source-declared verdicts
- **Investors and analysts** cross prediction markets, macro, and market data in one verified surface
- **Crypto operators** screen addresses, contracts, and bridges before counterparty exposure
- **Researchers** pull WHO, GDELT, and chokepoint time series with provenance attached to every answer

## Integration with CorpusIQ

SYNTHORA is the external-intelligence and compliance layer; CorpusIQ is the internal business-data layer. A finance operator can screen a counterparty through SYNTHORA's sanctions and wallet-reputation tools, then pull the relationship's actual financial history through CorpusIQ's accounting and CRM connectors — external risk verdict plus internal books in one session. Both platforms share the agent-first payment philosophy: CorpusIQ's connector model and SYNTHORA's x402 per-call pricing both avoid forcing annual seat licenses for machine access.

## Limitations

- Hosted service, single provider (HERGERT SYNTHORA); no self-host option documented
- Paid calls require USDC on Base and an x402-aware client
- Crypto-heavy tool surface; classic business data (financials, CRM) is out of scope
- New on mcp.so (Aug 2026); no third-party reviews yet

## See Also

- [Profitelligence MCP — Financial Intelligence from SEC Data](/hermes/mcp/servers/external/profitelligence-mcp/)
- [Live Listing Proof MCP — Fail-Closed Listing Verification](/hermes/mcp/servers/external/live-listing-proof-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
