---
title: AgenticRail Gate MCP
description: Deterministic step-order enforcement for AI agents — ALLOW or DENY before every step, with Ed25519-signed, hash-chained compliance receipts
category: Compliance
stars: n/a (no public repo)
added: 2026-08-13
source: mcpservers.org
relevance: ★★
tags: [agent-governance, compliance, audit-trail, receipts, sequence-enforcement, verification, remote-mcp]
---

# AgenticRail Gate MCP

**Remote MCP server (Streamable HTTP, no auth on the public demo key) from AgenticRail — deterministic step-order enforcement for AI agents.** Call `evaluate_step` before each step runs and the gate returns ALLOW or DENY; call `verify_receipt` after and it proves the Ed25519-signed, hash-chained receipt chain is intact. The same gate answers the engineering question (did the right steps run in the right order) and the compliance question (can we prove it later).

```
Server type: Remote (Streamable HTTP)
Auth: Bearer header — public demo key works without signup (rate-limited)
Endpoint: https://mcp.agenticrail.nz
Tools: 2 (evaluate_step, verify_receipt)
Pricing: Demo key free; production keys via agenticrail.nz
Category: Compliance / Agent Governance
Built by: AgenticRail (agenticrail.nz)
```

## Why This Matters for Operators

When an agent is allowed to move money, publish, or edit records, "trust me" is not an audit trail. AgenticRail inserts a gate between the agent and every consequential step: the agent POSTs its current step, a nonce, and a timestamp before acting, and only proceeds on ALLOW. Every ALLOW writes a cryptographic receipt — signed, chained, timestamped, and stored in R2 as a tamper-evident record — before the action executes.

**The receipt chain is the compliance artifact.** If a regulator, auditor, or customer later asks "what exactly did the agent do, in what order, and can you prove it," the operator has structural proof rather than a chat log. The published enforcement spec is versioned and frozen, and AgenticRail ships sector briefs for NZ health and NZ education showing how the receipts map to provable-safeguard requirements.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `evaluate_step` | Validate the current step against the policy before it runs: step order, nonce replay check, function and action-type checks, sequence-seal status. Returns ALLOW with a receipt, or DENY with a reason code. |
| `verify_receipt` | Prove a stored sequence's receipt chain is intact — Ed25519 signatures and hash chaining verified end to end. |

Three steps, no magic: send the request, the gate enforces the sequence, you get a receipt or a halt. The agent only proceeds on ALLOW.

## Installation

```bash
claude mcp add --transport http agenticrail https://mcp.agenticrail.nz
```

Omit the bearer token to run against the public demo key, or set one for a production key. Full docs: `agenticrail.nz/docs` with an llms.txt mirror for agents.

## Configuration

```json
{
  "mcpServers": {
    "agenticrail": {
      "type": "http",
      "url": "https://mcp.agenticrail.nz"
    }
  }
}
```

## Business Relevance

- **Compliance officers** get structural proof of what an agent ran, in what order — not a transcript to argue about
- **Fintech and payments operators** put ALLOW/DENY gates in front of money-moving steps with nonce replay protection
- **Agencies running client work through agents** can hand auditors a receipt chain per engagement
- **Operators in regulated verticals** (health, education, finance) get a vendor that publishes sector-specific safeguard briefs

## Integration with CorpusIQ

AgenticRail is a wrapper, not a data source — it composes around the CorpusIQ connector stack. A governed workflow: the agent's step "read QuickBooks invoices" goes through `evaluate_step` before the CorpusIQ call fires, and the receipt chain records exactly which connector was read, when, and in what order. Since CorpusIQ connectors are read-only with OAuth-granted scopes, the pair gives operators both sides of the governance equation: scoped access (CorpusIQ) plus provable sequence integrity (AgenticRail).

For teams building agent workflows on top of CorpusIQ data — collections runs, month-end close, marketing attribution recaps — the gate turns "the agent did it" into "here is the signed, chained record of what it did."

## Limitations

- Brand new — no public repo, no track record yet (listed Aug 2026)
- Two tools only — a gate, not a full policy engine; step policies must be defined on the AgenticRail side
- Demo key is public and rate-limited; production use requires a key and signup
- Receipts stored in the vendor's R2 — you are trusting their storage for the audit record
- New Zealand-centric sector briefs today; other jurisdictions are generic

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
