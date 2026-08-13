---
title: "FiatDock MCP — Agent Marketplace with x402 Payments"
description: "AI agents discover and pay each other per call in USDC over x402. 24+ live MCP services, non-custodial settlement, on/off-ramp to fiat."
date: 2026-08-12
source: mcp.so
source_url: https://mcp.so/servers/fiatdock
category: Finance & Commerce
rating: ★★
status: active
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/fiatdock-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# FiatDock MCP Server

## What is FiatDock?

A marketplace where AI agents discover and pay each other per call in USDC over x402 protocol. Settlement goes directly to the seller's wallet — no accounts, no API keys, no subscriptions. 24+ live MCP services for purchase, plus on/off-ramp between USDC and fiat (EU/EEA).

**Category:** Finance & Commerce  
**License:** MIT  
**Author:** fiatdock  
**Added:** August 12, 2026

## Why It Matters for Operators

FiatDock represents the emergence of an *agent-native economy* — where AI agents autonomously discover, pay for, and consume services from other agents. This is not a theoretical concept; 24 services are live and purchasable.

For operators, this signals:
1. **Agent-to-agent commerce is real** — Your growth agent could pay a competitor-research agent $0.01 for a report
2. **Per-call pricing works** — No subscriptions; pay only for what you use
3. **Non-custodial settlement** — Funds go directly to seller's wallet; no platform holds your money
4. **On/off-ramp exists** — Agents can convert USDC to fiat in the owner's bank account (EU/EEA)

## Connection Details

```json
{
  "mcpServers": {
    "fiatdock": {
      "command": "npx",
      "args": ["-y", "fiatdock-mcp"],
      "env": {
        "AGENT_PRIVATE_KEY": "0x...",
        "FIATDOCK_TOOLS": "all"
      }
    }
  }
}
```

**Transport:** stdio (local)  
**Auth:** Agent private key (EVM wallet on Base)  
**Pricing:** Most tools are paid ($0.001–$0.01 USDC per call via x402). Free tools: `get_quote`, `search_services`, `get_service`, `token_price`.

## Key Tools (18 total)

| Tool | Description | Cost |
|------|-------------|------|
| `search_services` | Find paid + free MCP services on marketplace | Free |
| `get_service` | Full detail for one listing | Free |
| `call_service` | Execute a paid service via x402 gateway | Paid (varies) |
| `token_price` | Real-time price for any EVM token | Free |
| `token_safety` | On-chain safety verdict (honeypot, taxes, liquidity) | $0.01 |
| `stablecoin_intel` | USDC supply, peg health, per-chain breakdown | $0.002 |
| `gas_price` | Current Base gas price | $0.001 |
| `usdc_balance` | USDC balance of any Base address | $0.001 |
| `create_offramp_session` | Convert USDC to fiat in owner's bank (EU/EEA) | $0.01 |
| `create_onramp_session` | Buy USDC with owner's fiat | $0.01 |

## Verified Use Cases

1. **Agent-Paid Competitive Research** — Growth agent pays a market-intel agent $0.01 for a competitor report
2. **Autonomous Treasury Operations** — Treasury agent checks stablecoin health, gas prices, and on/off-ramp rates
3. **Token Due Diligence** — Agent checks token safety before any transaction
4. **Fiat Settlement** — Agent converts earned USDC to owner's bank account autonomously

## CorpusIQ Integration Opportunity

**Priority: LOW (monitor only).** FiatDock is an ecosystem signal — agent-to-agent commerce is emerging — but not yet directly useful for CorpusIQ operations. Key things to watch:
- When competitor-research, SEO audit, or content-generation services appear on FiatDock, they become purchasable programmatically
- The x402 payment standard could become the Stripe of AI agents
- On/off-ramp capability means autonomous agents can eventually earn AND spend real money

## Verdict

**★★★☆☆ Ecosystem signal, not yet operational tool.** FiatDock demonstrates that the agent economy is forming, but as a marketplace of 24 services (mostly crypto/DeFi), it's not yet relevant for business operators. The architecture — non-custodial, per-call, no-subscription — is the right model. Watch for mainstream business services to list here.

## Resources

- **Homepage:** https://fiatdock.com/
- **Documentation:** https://fiatdock.com/docs.html
- **Repository:** https://github.com/fiatdock/fiatdock
- **mcp.so:** https://mcp.so/servers/fiatdock
