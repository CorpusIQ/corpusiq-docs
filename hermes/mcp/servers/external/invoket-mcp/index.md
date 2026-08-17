---
title: "Invoket MCP - CorpusIQ Docs"
description: 68 pay-per-call verification endpoints — IBAN validation, sanctions screening, phone validation and EU legal data — as typed MCP tools, paid in USDC on Base with non-custodial spend caps.
category: Finance
stars: n/a (new listing)
added: 2026-08-17
source: mcpservers.org
relevance: ★★
tags: [compliance, iban-validation, sanctions-screening, pay-per-call, x402, verification, legal-data, self-hosted]
---

# Invoket MCP

**Self-hosted MCP bridge (stdio, pay-per-call)** — `@invoket/mcp` turns the Invoket x402 gateway's 68 paid endpoints into typed tools an agent can call directly: IBAN validation, sanctions screening, phone validation, French and EU law in force, weather and climate, and medication data. Payments happen automatically over x402 in USDC on Base — the agent never has to know the protocol, and your key never leaves your machine.

```
Server type: Self-hosted (stdio, launched by your MCP host)
Auth: none for discovery-only mode; optional EVM payer key (PAYER_PRIVATE_KEY, read once from env, used only for local EIP-712 / EIP-3009 signatures)
Endpoint: Invoket x402 gateway via INVOKET_BASE_URL (tools generated live from gateway discovery)
Tools: 68 typed tools generated from the gateway's discovery surfaces
Pricing: pay-per-call in USDC on Base; first call per day to trial endpoints free; discovery-only mode free
Category: Compliance
Built by: Invoket (github.com/Invoket/mcp)
```

## Why This Matters for Operators

Pre-action checks — is this IBAN real, is this counterparty on a sanctions list, is this phone number valid — are exactly the kind of work agents should do before a payment or a contract. Until Invoket, wiring them in meant per-provider API keys and per-provider billing.

**The trust model is the product**: three independent checks run before any payment signature — `MAX_PRICE_USD` (per-call ceiling), `SESSION_BUDGET_USD` (per-session budget), and a challenge-amount check against the gateway's published price, so the gateway cannot quietly overcharge. Every request goes to a single configured origin; nothing is written to disk; a global output scrubber redacts key-shaped material from logs. The agent gets paid capabilities with the spending bounded before any signature exists.

## Tools & Capabilities

Tools are generated live from the gateway's discovery surfaces — endpoints added or removed upstream appear or disappear on their own. Published endpoint families:

| Area | Purpose |
|---|---|
| IBAN validation | Bank account verification before payouts |
| Sanctions screening | Counterparty screening before onboarding or payment |
| Phone validation | Number verification for outreach and KYC |
| French and EU law in force | Legal-state checks with citation |
| Weather & climate | Operational and logistics context |
| Medication data | Health-adjacent verification |

## Installation

```bash
npx -y @invoket/mcp
```

Runs on your machine over stdio, launched by your MCP host. Invoket hosts nothing and never sees your key or your funds.

## Configuration

```json
{
  "mcpServers": {
    "invoket": {
      "command": "npx",
      "args": ["-y", "@invoket/mcp"],
      "env": {
        "PAYER_PRIVATE_KEY": "your_evm_key",
        "MAX_PRICE_USD": "0.50",
        "SESSION_BUDGET_USD": "20"
      }
    }
  }
}
```

Without a key the server runs in discovery-only mode: browse the catalog and read schemas without paying. With a key, the first call each day to a trial-enabled endpoint is free (`PREFER_TRIAL` defaults to true) and reports `paid: false`.

## Business Relevance

- **Finance operators** get IBAN validation and sanctions screening before every payout — as tool calls, not manual lookups.
- **EU-facing teams** get French and EU law-in-force checks their agent can cite in decisions.
- **Compliance leads** get spending bounded per call and per session, with refusal guaranteed on any breach.
- **Ops teams** get verification endpoints with per-call pricing instead of per-provider subscriptions.

## Integration with CorpusIQ

Invoket slots into CorpusIQ payment and compliance workflows as the verification layer. Before paying a vendor, the agent validates the IBAN through Invoket and screens the counterparty, then executes the record through QuickBooks vendors and bills or Stripe payouts — the check and the ledger staying in separate, auditable systems. The pay-per-call model mirrors GovTrade's x402 pattern already in the catalog, so CorpusIQ operators can treat verification data as a metered input with spend caps rather than a fixed subscription.

## Limitations

- Brand new — no track record yet; listing appeared August 17, 2026.
- Requires holding and funding a Base EVM wallet (USDC) for paid calls.
- stdio/local only — the payer key stays on your machine, so remote agents need their own instance.
- Per-call costs are metered; budgets must be set deliberately or calls refuse.
- x402 rail is USDC on Base in v1 — no other chains or assets yet.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
