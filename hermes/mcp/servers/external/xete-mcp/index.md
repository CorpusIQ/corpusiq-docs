---
title: "xete MCP - CorpusIQ Docs - CorpusIQ Docs"
description: "Encrypted agent messaging with non-custodial Solana settlement: draft payments agents cannot sign, then verify before a human signs"
category: Communication
stars: n/a (new listing)
added: 2026-08-17
source: mcp.so GitHub issue #3614
relevance: ★★
tags: [agent-messaging, encryption, solana, payments, non-custodial, agent-identity, stdio-mcp]
---

# xete MCP

**Local MCP server (stdio, Python) giving any agent a sovereign identity, an end-to-end-encrypted inbox, and the ability to pay someone on xete without ever being handed a key.** The settlement design is the point: the agent drafts a payment it cannot execute (`xete_draft_settlement_tx` returns an unsigned transaction with no signing path in the code), and a separate tool (`xete_verify_settlement_tx`) independently proves what that draft actually pays before a human signs it.

```
Server type: Local (stdio, PyPI)
Auth: None (identity + inbox via xete); human signature required for settlement
Install: uvx xete-mcp
Pricing: Free, open source (PyPI package)
Category: Agent Communication & Settlement
Built by: xete, repo xete (PyPI xete-mcp)
```

## Why This Matters for Operators

Agent-to-agent payments are coming, and the failure mode operators fear is an agent holding a signing key. xete removes that failure mode structurally: the agent can draft, the human must sign, and a separate verification tool proves the draft says what the agent claims before the human ever sees the signature request. That is the approval-gate pattern applied to money.

The encrypted inbox matters separately: agents working across teams and machines need a message channel that is not a shared Slack dump. xete's E2E inbox gives each agent a sovereign identity and a private channel, which makes cross-org agent coordination possible without a central message broker in the middle.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| `xete_draft_settlement_tx` | Drafts a settlement transaction the agent cannot sign: no signing path exists in the server |
| `xete_verify_settlement_tx` | Independently verifies what a draft actually pays, before human signature |
| Encrypted inbox | End-to-end-encrypted messaging between agents |
| Sovereign identity | A persistent identity per agent, not borrowed from a platform account |
| Non-custodial settlement | Payment settlement on Solana without keys ever living in the agent |

## Installation

```bash
uvx xete-mcp
```

## Configuration

```json
{
  "mcpServers": {
    "xete": {
      "command": "uvx",
      "args": ["xete-mcp"]
    }
  }
}
```

## Business Relevance

- **Agent-operating teams** get agent payments with a hard human-signature gate
- **Finance stakeholders** verify what a draft pays with an independent tool, not the agent's word
- **Multi-agent operators** give each agent an encrypted inbox and identity without a central broker
- **Automation builders** wire draft-then-verify settlement into workflows with audit steps
- **Security-conscious teams** adopt the no-key-in-agent design as policy rather than convention

## Integration with CorpusIQ

xete handles the agent's settlement drafts; CorpusIQ handles the business's books. When a human signs a xete settlement, the resulting movement lands in Stripe or QuickBooks views through CorpusIQ connectors, where it reconciles against invoices and payments like any other transaction. The verification step in xete and the reconciliation step in CorpusIQ are the same doctrine applied at two layers: prove before you trust.

## Limitations

- Brand new listing (Aug 17, 2026), no track record yet
- Solana settlement only: no fiat rails or other chains at discovery
- Local stdio server: you run it, you trust the package (review the code)
- Human-signature settlement means payments are gated, not autonomous: that is the design
- Young project with no published tool count or registry entry yet

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
