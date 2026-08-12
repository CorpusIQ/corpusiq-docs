---
title: "Apiosk MCP — AI-Native Payments for Tools & APIs"
description: "Discover, pay for, execute, and publish monetized APIs directly from AI agents. Per-call settlement in USDC over x402. 42 tools including wallet management, API discovery, and publishing."
date: 2026-08-12
source: mcp.so
source_url: https://mcp.so/servers/apiosk
category: Developer Tools / Commerce
rating: ★★
status: active
---

# Apiosk MCP Server

## What is Apiosk?

AI-native payments infrastructure for tools and APIs. Agents discover, pay for, execute, and publish monetized APIs directly through MCP, settled per call in USDC over x402 protocol. Think "Stripe for AI agents" — 42 tools covering discovery, wallet management, payment execution, and API publishing.

**Category:** Developer Tools / Commerce  
**Author:** obcraft  
**Added:** August 12, 2026

## Why It Matters for Operators

Apiosk is the most complete agent-payments infrastructure observed to date. While FiatDock is a marketplace, Apiosk is the *payment rail* — the layer that makes per-call API monetization work.

For operators, the significance is:
1. **Monetization path for tools** — Operators could publish their own APIs and get paid per call by other agents
2. **Pay-as-you-go data** — Instead of monthly SaaS subscriptions, agents pay $0.001–$0.01 per data call
3. **Federated discovery** — `apiosk_discover` searches across Apiosk catalog + external x402 listings
4. **No platform lock-in** — Non-custodial wallets; agent holds its own keys

## Connection Details

```json
{
  "mcpServers": {
    "apiosk-mcp": {
      "command": "npx",
      "args": ["-y", "@apiosk/mcp"]
    }
  }
}
```

**Transport:** stdio (local)  
**Auth:** Local wallet or Apiosk dashboard account  
**Pricing:** Varies by API called. Wallet management tools are free.

## Key Tools (42 total)

| Category | Key Tools |
|----------|-----------|
| **Discovery** | `apiosk_explore`, `apiosk_search`, `apiosk_discover`, `apiosk_get_api` |
| **Execution** | `apiosk_execute`, `apiosk_inspect_x402`, `apiosk_get_started` |
| **Wallet** | `apiosk_wallet_create`, `apiosk_wallet_list`, `apiosk_wallet_select`, `apiosk_wallet_fund` |
| **Publishing** | `apiosk_publish_api`, `apiosk_update_api` |
| **Dashboard** | `apiosk_create_account`, `apiosk_sign_in`, managed wallet tools |
| **Payments** | `apiosk_payment_guide`, payment tracking, transaction history |

## Verified Use Cases

1. **Paid Data APIs** — Agent pays $0.01 for live market data, company financials, or SEO metrics
2. **Tool Monetization** — Developer publishes a data-enrichment API; earns USDC per call from other agents
3. **Autonomous Budget Management** — Agent manages its own wallet with spending limits and transaction history
4. **Federated Discovery** — One `discover` call searches multiple marketplaces for the best-priced API

## CorpusIQ Integration Opportunity

**Priority: LOW (monitor only).** Apiosk, like FiatDock, is an ecosystem infrastructure play. It's not directly useful for CorpusIQ operations today, but the pattern matters:

- **Future opportunity**: Publish CorpusIQ research/reports as paid MCP endpoints
- **Competitive moat**: If operators can pay $0.01 for a competitive brief via Apiosk, that changes the competitive landscape
- **API economy**: Watch for mainstream business APIs (Clearbit, ZoomInfo, Semrush) to list on Apiosk

## Verdict

**★★★☆☆ Best-in-class agent payments infrastructure.** 42 tools, federated discovery, non-custodial wallets, and API publishing make this the most complete agent-payments solution. Currently populated with developer/DeFi APIs; business-data APIs are the missing piece that would make this operational for CorpusIQ.

## Resources

- **Homepage:** https://apiosk.com/
- **Documentation:** https://docs.apiosk.com/
- **Repository:** https://github.com/obcraft/apiosk-mcp
- **mcp.so:** https://mcp.so/servers/apiosk
