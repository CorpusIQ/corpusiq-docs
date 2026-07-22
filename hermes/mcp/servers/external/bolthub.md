---
title: "Bolthub MCP — Bitcoin Lightning L402 Paid-API Marketplace for AI Agents"
description: "Bolthub is an API marketplace where AI agents discover and pay for tools per call over Bitcoin Lightning using L402. Agents autonomously purchase API access without credit cards or subscriptions."
category: mcp
tags: [mcp-server, bitcoin, lightning, l402, api-marketplace, payments, agent-economy]
last_updated: 2026-07-19
---

# Bolthub MCP — L402 Paid-API Marketplace

Bolthub is an API marketplace where AI agents discover and pay for tools on a per-call basis using Bitcoin Lightning payments via the L402 protocol. No credit cards, no subscriptions, no human in the loop — agents autonomously purchase API access with micropayments.

**Source:** awesome-mcp-servers PR #9900 (discovered July 19, 2026)
**Category:** Finance & Fintech / API Marketplace
**Author:** TamasCsernyanszky
**Repo:** https://github.com/TamasCsernyanszky/bolthub
**Status:** Active

## Why This Matters

The agent economy needs a payment rail. Current API billing is built for humans — monthly subscriptions, credit cards, usage tiers decided in dashboards. L402 enables agents to make autonomous micro-purchases: "I need this data once, I'll pay $0.002 for it." Bolthub aggregates L402-enabled APIs into a discoverable marketplace, letting agents shop for tools the way humans browse app stores.

## Installation

```bash
# Remote MCP — connect directly
# Or run locally:
npm install -g bolthub-mcp
npx bolthub-mcp
```

## Claude Desktop / Hermes Configuration

```json
{
  "mcpServers": {
    "bolthub": {
      "command": "npx",
      "args": ["bolthub-mcp"],
      "env": {
        "L402_WALLET_PATH": "~/.l402/wallet"
      }
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `search_apis` | Discover L402-enabled APIs by category and price |
| `purchase_access` | Buy single-call access to an API via Lightning |
| `check_balance` | View available Lightning wallet balance |
| `list_purchases` | Review past API purchases and their outcomes |

## L402 Protocol

L402 is the Lightning Network's HTTP 402 Payment Required standard. It enables:
- **Per-call micropayments** — pay $0.001-$0.01 per API call
- **No accounts** — cryptographic auth via Lightning wallet keys
- **Instant settlement** — payments clear in seconds on Lightning

## CorpusIQ Relevance

As CorpusIQ scales its MCP server to more operators, L402-based billing could be an alternative to traditional subscription pricing — especially for operators who only need occasional API access. Bolthub demonstrates the marketplace model: CorpusIQ's MCP server could be listed as an L402-enabled API, allowing agents to purchase business data queries on-demand.

## See Also

- [[sweeps/sweep-july19-2026]]
- Setell MCP
