---
title: "Intesta MCP - Attested Business Fact Passports"
description: "Keyless remote MCP registry of attested business fact passports with a trust ladder (A0 claimed to A4): 5 tools search entities, read passports and answer questions built only from attested facts, so agents never invent business data. No API key required."
category: Compliance
stars: n/a (hosted)
added: 2026-08-27
source: "chatmcp/mcpso issue #3801"
relevance: ★★
tags: [entity-verification, trust-ladder, business-data, attestation, fact-passports, kyv, remote-mcp]
---

# Intesta MCP

**Hosted remote MCP server (Streamable HTTP, no auth required) for attested business facts.** Intesta is a registry of attested business fact passports, each fact carrying a trust level on a published ladder: A0 claimed, A1 domain-verified, A2 payment-verified, A3/A4 higher attestation. Its five tools search entities, read passports and answer questions - and answers are built only from an entity's attested passport. If no matching attested fact exists, the agent is told so rather than fed a plausible invention.

```
Server type: Remote (Streamable HTTP)
Auth: None required
Endpoint: https://intesta.io/mcp
Tools: 5
Pricing: Public registry; see intesta.io
Docs: https://intesta.io/llms.txt · Registry: https://intesta.io/registry
Category: Compliance
```

## Why This Matters for Operators

The most expensive failure mode for agent-assisted business work is a confidently wrong fact about a counterparty - a fabricated registration number, a guessed ownership structure, a made-up address. Intesta attacks exactly that: every fact an agent retrieves carries an attestation level, and the server refuses to answer from anything but attested passport data. **For operators using agents on KYV-style questions ("is this vendor verified", "who owns this entity"), Intesta provides a trust ladder the agent can quote back - A1 domain-verified vs A2 payment-verified - instead of a bare claim.** No API key means a zero-setup verification source for agent workflows.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_entities` | Find entities in the registry by attested facts |
| `get_passport` | Read one entity's full fact passport with trust levels |
| `ask` | Ask a question; answered only from the entity's attested passport |
| `list_entities` | List registered entities |
| `get_trust_ladder` | The published A0-A4 trust ladder and what each level attests |

## Installation

```bash
claude mcp add intesta --transport http https://intesta.io/mcp
```

No key, no signup. Agent-facing docs are published at intesta.io/llms.txt for one-shot tool discovery.

## Configuration

```json
{
  "mcpServers": {
    "intesta": {
      "type": "http",
      "url": "https://intesta.io/mcp"
    }
  }
}
```

## Business Relevance

- **Procurement and finance teams** verify counterparty facts with an explicit trust level attached
- **Sales and BD** check prospect claims against attested passports instead of self-reported data
- **Compliance teams** get a registry-based fact source agents cannot silently embellish
- **Operators building agent workflows** add a zero-key verification layer to any MCP client

## Integration with CorpusIQ

Intesta verifies what CorpusIQ analyzes. An agent doing vendor or customer diligence can pull Intesta's attested passport for a counterparty, then reconcile it against CorpusIQ's QuickBooks payables and Stripe revenue to see whether the attested profile matches the actual commercial relationship. For KYC-adjacent workflows, Intesta's trust ladder supplies the verification evidence while CorpusIQ supplies the financial record - the pair gives an agent both "what is attested about them" and "what our books say about them".

## Limitations

- Brand new - no public track record yet; listing submitted Aug 27, 2026
- Registry coverage is the ceiling: answers exist only for entities with attested passports
- A0 facts are self-claimed; due diligence should weigh the ladder level, not treat all facts equally
- No auth means the surface is the public registry, not account-scoped data
- Trust ladder semantics (A0-A4) are vendor-defined

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [1Lookup MCP - Phone, Email and IP Verification](/hermes/mcp/servers/external/1lookup-mcp)
