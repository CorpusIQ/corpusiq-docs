---
title: Countersignatory MCP - Verified Human Judgment Markets
description: "A spot market for verified human judgment. Agents quote a task before committing to it - a screened human check, a consensus of several humans, a named professional who signs, or a regulated act such as remote notarisation - and get back an indicative price, a band, urgency and off-hours multipliers, and the implied rate per human minute. Three keyless tools, a published wage floor, and every seeded number's derivation made public."
category: Business Operations
stars: n/a (new listing)
added: 2026-09-07
source: mcp.so feed
relevance: ★★
tags: [human-in-the-loop, approvals, verification, notarisation, spot-pricing, judgment, remote-mcp]
---

# Countersignatory MCP - Verified Human Judgment Markets

**Remote MCP server (Streamable HTTP, no auth)** - a UK-operated exchange where AI agents price, and when the market opens, purchase verified human judgment at live spot prices rather than off a rate card. Today it publishes the Countersignatory Spot Index and a quote engine: an agent learns what a verified human would cost for a task, at a given urgency and stake, before committing. Listed in the official MCP registry as `com.countersignatory/mcp`.

```
Server type: Remote (Streamable HTTP, stateless)
Auth: None (optional free key from POST https://countersignatory.com/v1/keys counts a caller as one caller)
Endpoint: https://countersignatory.com/mcp
Tools: 3 (countersignatory_quote, countersignatory_register_interest, countersignatory_spot_index)
Pricing: Quotes are indicative; nothing is fulfilled or charged through the server while the demand-measurement window runs
Category: Business Operations
Built by: Countersignatory Ltd, UK (countersignatory.com)
```

## Why This Matters for Operators

Every agent workflow eventually hits a step it should not take alone: approving a refund, verifying a document, signing off a decision that will carry someone's name. Today those steps are either automated anyway (no accountability) or stalled on a human who is never available at the right moment (no throughput). Countersignatory prices the human step the way a market prices anything else - by what the responder has at stake.

**The four tiers make the accountability explicit**: Check (one screened human, a quality score at stake), Consensus (several humans who must agree), Countersign (a named, register-verified professional who signs the record), and Seal (a regulated act such as remote notarisation, partner-fulfilled). A published wage floor of USD 0.25 net per active minute is in force, responders are never charged, and the derivation of every seeded number in the index is public.

The tool schemas were probe-verified live with no credentials: `countersignatory_quote` accepts task type, SLA deadline, tier, an odd consensus quorum of 3-9, an unassisted-human-perception flag, a two-letter jurisdiction and a maximum bid in USD, and returns whether the bid clears.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `countersignatory_quote` | Price a task at current spot. Returns an indicative price, a band, multipliers applied, alternatives that would clear a lower bid, and the implied rate per human minute. |
| `countersignatory_register_interest` | Record that a quoted price would clear your use case. This is the demand signal that decides which markets open first. |
| `countersignatory_spot_index` | The full public index, with the published wage floor and the derivation of every seeded number. |

The quote parameters: `task_type` (judgment, verification, approval, physical, signature), `sla_seconds` (deadline), `tier` (check, consensus, countersign, seal), `consensus_n` (odd number 3-9), `unassisted` (premium for unassisted human perception), `jurisdiction` (ISO 3166-1 alpha-2 code), `max_price` (USD bid; the response says whether it clears).

## Installation

```bash
claude mcp add countersignatory --transport http https://countersignatory.com/mcp
```

No authentication is required. The endpoint is stateless Streamable HTTP, so any MCP client can connect directly.

## Configuration

```json
{
  "mcpServers": {
    "countersignatory": {
      "type": "http",
      "url": "https://countersignatory.com/mcp"
    }
  }
}
```

Methodology is published at countersignatory.com/methodology and the launch essay at countersignatory.com/essay.

## Business Relevance

- **Agent builders** wire a quote call before approval steps, so refunds, escalations and sign-offs carry a real cost and a real human record.
- **Compliance teams** price verification and countersignature tasks per SLA instead of negotiating rate cards per vendor.
- **Operations leads** benchmark what verified human judgment actually costs across urgency levels, using the spot index.
- **Marketplaces and platforms** register demand interest for the tiers their use cases need, shaping which markets open first.

## Integration with CorpusIQ

Countersignatory slots into the approval gates of CorpusIQ agent workflows: before a CorpusIQ agent approves a refund or sends a high-stakes outbound message, it calls `countersignatory_quote` to surface the cost of a verified human check, then `register_interest` so the demand is recorded against the operator's use case. The spot index feeds CorpusIQ's operational reporting as a benchmark line - what a human approval gate costs per decision - which operators can compare against the error rate of fully automated approvals. When the market opens, the same wiring upgrades from quoting to purchasing without changing the workflow shape.

## Limitations

- Pre-launch: the quote engine and index are live, but the market itself opens after the current demand-measurement window; nothing is fulfilled or charged through the server today.
- Every quote is indicative until the first real clears.
- Human fulfillment depends on responder supply in each jurisdiction and tier once the market opens.
- Brand new listing with no track record yet.
- No self-host option - hosted endpoint only.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
