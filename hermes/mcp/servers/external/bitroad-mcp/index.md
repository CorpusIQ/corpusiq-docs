---
title: "Bitroad MCP - CorpusIQ Docs - CorpusIQ Docs"
description: "Marketplace for AI agents over MCP: buy goods and services under spending caps with returns and disputes built into the protocol"
category: Commerce & E-Commerce
stars: n/a (new listing)
added: 2026-08-17
source: mcp.so homepage (new arrivals)
relevance: ★★
tags: [agent-economy, agent-commerce, marketplace, payments, spending-caps, remote-mcp, agent-transactions]
---

# Bitroad MCP

**Remote MCP server (Streamable HTTP) connecting AI agents to Bitroad, a marketplace where agents buy goods and services.** Every purchase runs under a spending cap, and the marketplace carries returns and disputes as protocol features rather than afterthoughts. An agent operating inside its budget can source what a task needs without a human pre-approving each line item.

```
Server type: Remote (Streamable HTTP)
Auth: Bitroad account (buy.bitroad.ai sign-up)
Endpoint: https://app.bitroad.ai/api/v1/mcp
Docs: bitroad.ai/docs
Pricing: Commercial (Bitroad marketplace)
Category: Agent Commerce
Built by: Bitroad (bitroad.ai), repo github.com/bitroadai/bitroad-mcp
```

## Why This Matters for Operators

Agent-to-agent commerce is becoming a procurement channel, and the open question for operators is control: how do you let an agent spend without giving it a card. Bitroad answers with the cap. The agent can buy up to its configured limit, and the marketplace handles returns and disputes, so a failed purchase is a process, not a loss.

For teams building agent workflows, Bitroad is the spending layer that keeps the human in the budget conversation instead of the approval queue. The same pattern applies to selling: any operator with a service agents need can list it and get paid through the marketplace's rails.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Marketplace discovery | Browse and search goods and services available to agents |
| Capped purchasing | Buy items within the account's spending caps |
| Returns | Initiate returns on purchases that did not satisfy |
| Disputes | Open and track disputes through the marketplace's resolution flow |

## Installation

```bash
claude mcp add --transport http bitroad https://app.bitroad.ai/api/v1/mcp
```

Create an account at buy.bitroad.ai, set spending caps, and authenticate the client.

## Configuration

```json
{
  "mcpServers": {
    "bitroad": {
      "type": "http",
      "url": "https://app.bitroad.ai/api/v1/mcp"
    }
  }
}
```

## Business Relevance

- **Agent-operating teams** give agents a capped spend path instead of a corporate card
- **Service providers** list agent-consumable services and get paid through marketplace rails
- **Finance stakeholders** keep agent spend bounded by cap configuration rather than post-hoc reconciliation
- **Procurement leads** get returns and disputes as protocol features, reducing vendor-management overhead
- **Automation builders** wire agent purchases into multi-step workflows with a budget ceiling per step

## Integration with CorpusIQ

Bitroad is the agent's wallet; CorpusIQ is the operator's ledger. An agent buys through Bitroad inside its cap, and the resulting spend flows into QuickBooks and Stripe views through CorpusIQ's connectors, where finance sees it next to every other expense. The cap lives in Bitroad, the accounting lives in CorpusIQ, and the two meet in the reconciliation the operator already runs.

## Limitations

- Brand new listing (Aug 17, 2026), no track record yet
- Marketplace liquidity is early: the catalog is only as deep as the sellers who have joined
- Commercial platform: no self-host option published
- Agent-initiated commerce is new territory for many compliance teams: check procurement policy before enabling
- No published tool-level documentation beyond the endpoint and sign-up path

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
