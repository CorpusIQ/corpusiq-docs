---
title: "AgentTrust MCP - Trust Decisions for Agent Endpoints"
description: "Remote MCP that checks an agent endpoint against observed monitoring, reliability and ownership evidence and returns a trust decision."
category: "Business Operations"
stars: n/a (hosted platform, getagenttrust.com)
added: 2026-10-03
source: "mcpservers.org server page (getagenttrust-com)"
relevance: ★★
tags: [agent-trust, security, reliability, a2a, agent-registry, remote-mcp]
---

# AgentTrust MCP

**Remote MCP server (Streamable HTTP)** - AgentTrust sits between finding an agent and calling it. An endpoint URL goes in, the evidence AgentTrust has already observed for that exact URL is read, and a machine-readable trust decision comes out, all without contacting the endpoint itself.

```
Server type: Remote (Streamable HTTP)
Auth: See getagenttrust.com (key per account)
Endpoint: https://getagenttrust.com/api/mcp
Tools: check_agent_trust (returns a trustDecision object)
Pricing: See getagenttrust.com
Category: Business Operations
Built by: AgentTrust (getagenttrust.com)
```

## Why This Matters for Operators

As agents start calling other agents, the missing step is the one a human does instinctively: deciding whether the counterpart is worth trusting before the call. AgentTrust fills that gap with evidence it has already collected about an endpoint, so the decision is based on observed history rather than a hopeful first request.

**The differentiator is that it answers without touching the endpoint.** A lookup reads stored evidence, so checking trust cannot itself trigger a slow, hostile or broken counterpart. The decision rule is deterministic and published: recommended when the endpoint is healthy and its current score is 50 or above, with confidence banded high at 90-plus and medium at 50-plus when ownership is verified, and low otherwise.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `check_agent_trust` | Takes an `endpointUrl`, reads the evidence AgentTrust has observed for that URL, and returns a `trustDecision` with health, reliability score, evidence freshness and endpoint ownership |

The returned decision carries `recommended` plus confidence and reasons, so a caller can act on the recommendation or apply its own policy to the raw signals. AgentTrust returns what it has observed; it is explicitly not a community rating and not a security guarantee.

## Installation

```bash
npx add-mcp 'https://getagenttrust.com/api/mcp'
```

The same endpoint installs into Claude Code, Codex, Cursor and other clients through the standard MCP add flow.

## Configuration

```json
{
  "mcpServers": {
    "agenttrust": {
      "type": "http",
      "url": "https://getagenttrust.com/api/mcp"
    }
  }
}
```

Check the AgentTrust documentation for the authentication scheme on your account. A public test agent is available to try a lookup before wiring a real endpoint at `https://getagenttrust.com/check-agent-trust?endpointUrl=https://agenttrust-umber.vercel.app/api/test-agent`.

## Business Relevance

- **Platform teams building agent-to-agent workflows** gate a call on a trust decision instead of invoking every discovered endpoint blind.
- **Operators running multi-agent orchestrations** screen a newly discovered endpoint for health and reliability before assigning it work.
- **Security and risk teams** add an evidence-based pre-call check in front of third-party agents, complementing their own policy.
- **Marketplace and registry operators** attach a trust signal to listed agents so consumers see observed behavior, not just a description.
- **Anyone auditing an agent supply chain** records the trust decision that preceded each external agent call.
