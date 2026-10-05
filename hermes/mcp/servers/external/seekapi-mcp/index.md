---
title: SeekAPI MCP - China Supplier Screening for Agents
description: "Run a China Supply Check from any MCP client: three evidence-backed supplier candidates for RFQ, 2.99 USDC per check on Base."
category: Procurement
stars: n/a (new listing)
added: 2026-10-05
source: mcpservers.org /all (Oct 5, 2026 midday sweep)
relevance: ★★
tags: [sourcing, china-suppliers, procurement, supply-chain, x402, remote-mcp]
---

# SeekAPI MCP

**Public remote MCP server (Streamable HTTP, keyless discovery)** - SeekAPI runs a China Supply Check for agents: give it a product or model, a quantity and must-have specifications, and a successful check returns three distinct, evidence-backed China supplier candidates worth advancing to RFQ. Discovery and brief preparation are free; the paid check is 2.99 USDC on Base via live x402.

```
Server type: Remote (Streamable HTTP)
Auth: keyless for discovery and preparation; signed-wallet x402 for purchase and result reads
Endpoint: https://api.seekapi.ai/mcp
Server: seekapi-factory v0.1.2 (initialize + tools/list captured live, unauthenticated)
Tools: 6 (discover, prepare, purchase, run, status, result - each ..._china_supply_check_v0)
Price: 2.99 USDC on Base (x402 live); Stripe Checkout USD 2.99 being enabled
```

## Why This Matters for Operators

Sourcing from China is where spec sheets meet uncertainty: which three suppliers are even worth an RFQ, what do listings actually quote once MOQ and tier conditions are read, and how much of a candidate's identity is verified versus assumed. Cross-border sourcing agents usually answer with confident guesses. SeekAPI answers with a structured brief: observed listing prices as dated commercial evidence with currency, unit, tier and MOQ conditions; certification, company and production-versus-trade identity evidence per candidate when available; and explicit unknowns kept attached to their fields.

The agent flow is deliberately staged - discover, prepare, confirm, then purchase - so a person reviews the normalized Product Brief and its digest before anything is bought, and paid results are read back only through signed-wallet authentication bound to the settled order.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `discover_china_supply_check_v0` | Read the current availability, price and input contract before preparing or purchasing (free, read-only) |
| `prepare_china_supply_check_v0` | Build the normalized Product Brief and confirmation digest from text or a model/part number, a positive quantity and unit, up to five required attribute/value conditions, a product name, an optional reference and substitution permission. Free; contacts no supplier and buys nothing |
| `purchase_china_supply_check_v0` | Buy the exact confirmed brief for 2.99 USDC on Base via official x402. Requires a signed wallet invocation; no supplier execution in the purchase |
| `run_china_supply_check_v0` | Execute the settled check (x402 payment path) |
| `status_china_supply_check_v0` | Read order status - requires signed-wallet authentication bound to the settled order (a payment proof alone is not authentication) |
| `result_china_supply_check_v0` | Read the finished report: three RFQ-worthy candidates with price basis, MOQ fit, identity evidence and explicit unknowns |

## Installation

Add the endpoint to any MCP client - no key needed for public discovery:

```json
{
  "mcpServers": {
    "seekapi": {
      "type": "http",
      "url": "https://api.seekapi.ai/mcp"
    }
  }
}
```

Initialize the session and call `tools/list`, then `discover_china_supply_check_v0` with empty arguments to read the live availability, price and input contract before preparing or buying anything.

## Business Relevance

- **Screening before outreach**: three candidates worth an RFQ, not a list of fifty maybes - with the reasoning and gaps attached.
- **Evidence over vibes**: dated price basis, MOQ fit and identity evidence ships with every candidate; unsupported shortages are reported honestly.
- **Staged spend**: free discovery and preparation, one fixed-price check, and a confirmation step between preparation and purchase.
- **Agent-native payment**: the x402 flow settles in USDC on Base from a signed wallet, with results gated behind the same wallet authentication.

## Integration with CorpusIQ

Procurement and finance answers usually sit apart: what the business spent is inside the ERP, what a new component could cost is outside. An operator can source through SeekAPI's checks and ask CorpusIQ about spend and margins in the same conversation, keeping the supplier evidence one click from the P&L context, with CorpusIQ remaining read-only on the business systems.

## Limitations

- The check screens suppliers; exact product qualification is separate, and supplier outreach, sample follow-up, physical inspection and China-side coordination require separately agreed scope - the human-task API, MCP and WebMCP execution paths are not live.
- x402 is the live payment path (2.99 USDC on Base); Stripe Checkout USD 2.99 is being enabled and is not open for purchase.
- Result and status reads require signed-wallet authentication bound to the settled order; a payment proof or arbitrary order ID alone does not grant report access.
- The server prefers honest gaps over approximations: some candidates arrive with explicit unknowns rather than guessed answers.
- Hosted by SeekAPI and governed by its terms; initialize and tools/list return 200 unauthenticated by design.

## FAQ

### What does a China Supply Check return?

Three distinct, evidence-backed China supplier candidates worth advancing to RFQ, with observed price basis, MOQ fit, supplier identity evidence where available and explicit unknowns. RFQ-worthiness and exact product qualification are separate judgments.

### What can an agent do for free?

Initialize the public MCP endpoint, list tools, call `discover_china_supply_check_v0` and prepare a normalized Product Brief with `prepare_china_supply_check_v0`. Preparation does not buy a check or contact a supplier.

### How much does a check cost and how is it paid?

The existing x402 path is live at 2.99 USDC on Base. Stripe Checkout USD 2.99 is being enabled and is not available to buy. Payment scope is confirmed before the purchase and run flow.

### Does the check contact suppliers?

No. Supplier contact, RFQ execution and human China Desk work are separately scoped services; this server's purchase does not activate them.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
