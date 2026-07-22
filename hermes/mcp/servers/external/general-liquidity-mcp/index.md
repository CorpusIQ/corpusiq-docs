---
title: General Liquidity MCP Server
subtitle: Machine economy API — resolve, pay, verify, disclose
source: general-liquidity-mcp
github: https://github.com/general-liquidity/general-liquidity-mcp
created: 2026-07-22
category: Fintech / Payments
stars: 0
tags: [payments, machine-economy, fintech, api, settlement]
---

# General Liquidity MCP Server

MCP server for the **General Liquidity machine economy API**. Enables AI agents to resolve, pay, verify, and disclose — autonomous payment operations over the machine economy.

## What It Does

General Liquidity is a machine-to-machine payment protocol. This MCP server wraps their OpenAPI 3.1 spec into agent-callable tools:

- **Resolve** — Look up accounts, counterparties, and payment rails
- **Pay** — Execute payments between machine-economy participants
- **Verify** — Confirm transaction settlement and reconciliation
- **Disclose** — Share verifiable credentials and transaction proofs

## Business Operator Use Cases

| Use Case | Value |
|----------|-------|
| **Autonomous Treasury** | Agent-managed payments between corporate entities with verification |
| **Machine Payments** | IoT/automated system payments (energy trading, logistics settlement) |
| **Cross-Border Settlement** | Machine-economy rails for cross-border B2B payments |
| **Verifiable Disclosure** | Share payment proofs and credentials without exposing full transaction data |

## Installation

```bash
git clone https://github.com/general-liquidity/general-liquidity-mcp
cd general-liquidity-mcp
npm install
```

## Configuration

```json
{
  "mcpServers": {
    "general-liquidity": {
      "command": "node",
      "args": ["path/to/general-liquidity-mcp/index.js"],
      "env": {
        "GL_API_KEY": "your-api-key",
        "GL_API_URL": "https://api.general-liquidity.com"
      }
    }
  }
}
```

## Tools Provided

- `resolve_account` — Look up account details and capabilities
- `initiate_payment` — Create a payment instruction
- `verify_settlement` — Confirm transaction finality
- `disclose_credential` — Share verifiable proofs
- `get_rails` — List available payment rails and fees

## Limitations

- **0 stars, brand new** — Created July 22, 2026. Barely documented.
- **Machine economy focus** — Not a general-purpose payment API. Optimized for automated/machine payments.
- **API key required** — General Liquidity access needed.
- **Unclear regulatory status** — Machine-to-machine payments may have different regulatory treatment than consumer payments. Verify with legal counsel.

## Operator Verdict

★★★ **Forward-looking, not yet operational.** The machine economy concept is real (IoT payments, autonomous settlement) but adoption is early. General Liquidity MCP is an infrastructure play — valuable if you're building in the machine economy space, but not yet a drop-in replacement for traditional payment processing.
