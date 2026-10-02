---
title: Nebelus MCP - Governed Agent Building
description: "MCP server that exposes the Nebelus Construction API: about 48 tools giving an MCP client full agent build parity - create and update agents, edit agent graphs, attach knowledge bases and vector stores, wire connectors, set governance policies and locked guardrails, enable grounding-trace claim-to-source verification and read deployment wiring. Agents stay drafts by design; publishing happens in the Nebelus console. EU and GCC-KSA data residency, ISO 27001 / ISO 9001 / GDPR-aligned."
category: Developer Tools
stars: n/a (commercial platform)
added: 2026-09-14
source: "mcp.so feed (Sep 14 evening, submitted 1h before sweep) + vendor docs at nebelus.ai"
relevance: ★★
tags: [regulated-industries, governance, guardrails, grounding, audit, data-residency, eu, ksa, agent-building, oauth, remote-mcp]
---

# Nebelus MCP

**Build and govern real AI agents from your own assistant.** Nebelus is an enterprise agentic-AI platform for regulated industries (healthcare, insurance, finance, government). Its MCP server is a facade over the Nebelus Construction API: about 48 tools that give an MCP client full agent build parity - create, update and probe agents, edit multi-node agent graphs, attach knowledge bases and vector stores, wire connectors, set governance policies and locked guardrails, enable grounding-trace, and read deployment wiring.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (Claude clients, no key) or organization API key (scope api.construction.*)
Endpoint: https://api.nebelus.ai/api/v1/construction/mcp/ (401-verified live, Sep 14 2026)
Tools: ~48
Pricing: Nebelus platform account required; platform pricing at nebelus.ai
Category: Developer Tools / Enterprise Agent Platform
Residency: EU or GCC-KSA, enforced per region (KSA endpoint at api.ksa.nebelus.ai)
```

## Why This Matters for Operators

Regulated teams cannot ship agents that improvise. The block is rarely the model; it is everything around it - who can build agents, what guardrails are locked, where data resides, and whether an output claim can be traced back to a source. Nebelus makes the construction of agents a governed, auditable act: every agent is created as a **draft**, and there is deliberately **no deploy tool over MCP** - publishing happens in the Nebelus console, behind a human gate.

Two capabilities deserve attention:

- **Locked guardrails and governance policies** are set through the API, so the rules travel with the agent definition rather than living in a wiki.
- **Grounding-trace** verifies claim-to-source for regulated output, which is the difference between "the model said so" and "here is the filing, policy clause or record it came from".

## Tools & Capabilities

| Area | Coverage |
|---|---|
| Agents | create, update, probe; full lifecycle as drafts |
| Graphs | edit multi-node agent workflows |
| Knowledge | attach knowledge bases and vector stores |
| Connectors | wire APIs, databases and integrations |
| Governance | set policies and locked guardrails |
| Verification | enable grounding-trace (claim-to-source) |
| Deployment wiring | read REST / WebSocket / webhook / widget / MCP wiring |

## Installation

**Claude.ai / Claude Desktop** - add a remote MCP server by URL and complete the OAuth 2.1 flow; no API key needed:

```json
{
  "mcpServers": {
    "nebelus": {
      "type": "http",
      "url": "https://api.nebelus.ai/api/v1/construction/mcp/"
    }
  }
}
```

**Claude Code / Cursor** - connect with an organization API key (scope `api.construction.*`):

```json
{
  "mcpServers": {
    "nebelus": {
      "type": "http",
      "url": "https://api.nebelus.ai/api/v1/construction/mcp/",
      "headers": { "Authorization": "Bearer sk-ns-..." }
    }
  }
}
```

KSA-resident organizations use `https://api.ksa.nebelus.ai/api/v1/construction/mcp/`.

## Business Relevance

- **Regulated enterprises** give their builders a single governed path to create agents that stay inside residency and PII rules.
- **Compliance teams** get locked guardrails and an audit trail on every agent change, with grounding-trace on outputs.
- **Platform teams** wire knowledge, connectors and deployment surfaces programmatically instead of through console clicking.
- **Healthcare, insurance and finance operators** keep drafts drafts: nothing an agent builder does reaches production without the console step.

## Integration with CorpusIQ

Both systems treat verification as the product, not the wrapper: Nebelus verifies that an agent's output traces to its sources, and CorpusIQ verifies that the business numbers an AI reports trace to the actual systems that hold them (Stripe, Shopify, HubSpot, GA4, QuickBooks and 40+ more, read-only, source-cited). An agent built on Nebelus can use a CorpusIQ connection for its business-data reads, so the governed agent and the governed data share the same standard: every claim carries its source.

## Limitations

- **Commercial platform**: a Nebelus organization and account are required; platform pricing is not published on the MCP listing.
- **Construction API only** over MCP (roughly 48 tools); the rest of the platform is console-side.
- **Drafts only by design** - no deploy tool over MCP, which is a feature for governance but adds a console step for shipping.
- **Thin public docs** at catalog time beyond the listing; tool names are served from the authorized connection.
- **Regional scope**: EU and GCC-KSA residency; other regions are not documented.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [Helio MCP - Governance Proxy for AI Agent Tool Calls](/hermes/mcp/servers/external/helio-mcp)
- [Governance](/hermes/governance)
