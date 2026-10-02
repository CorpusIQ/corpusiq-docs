---
title: AgentLedger MCP - Per-Agent Spend Management for Operators
description: Per-agent spend management for autonomous agents - track x402, MPP and API-key spend, enforce budget caps, catch anomalies and keep a full audit trail, with a free beta tier for up to 3 agents.
category: Finance
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★★
tags: [agent-spend, budget-control, cost-tracking, x402, mpp-payments, ai-operations, audit-trail, remote-mcp]
---

# AgentLedger MCP

**Remote MCP server (Streamable HTTP, agent-secret writes)** - the "Datadog for agent spending": track what every autonomous agent spends across x402, MPP and API-key payment rails, cap budgets per agent, and keep a full audit trail. Five tools on one hosted endpoint, free during beta for up to 3 agents.

```
Server type: Remote (Streamable HTTP)
Auth: agent_secret issued on first track call (reads are open)
Endpoint: https://agent-ledger-production-0ff8.up.railway.app/mcp/
Tools: 5 (ledger_track, ledger_set_budget, ledger_report, ledger_alerts, ledger_list_agents)
Pricing: Free beta (up to 3 agents); Pro $19/mo unlimited
Category: Finance
Built by: entradox (independent software service), registry io.github.entradox/agent-ledger
```

## Why This Matters for Operators

When agents start spending money autonomously - x402 micro-payments, MPP invoices, API keys handed to sub-agents - spend stops being a line item and becomes a stream of small, invisible transactions. **AgentLedger gives that stream a ledger**: every dollar and token an agent moves lands in one place, tagged by agent, rail and service.

The budget cap is the real control: a track() call that would cross a monthly cap is blocked with a 402, not just logged after the fact. And because every write requires the agent_secret issued on first registration, a rogue or compromised agent cannot silently inflate another agent's ledger.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `ledger_track` | Record a spend event (dollars and tokens) with agent_id, rail, service and model |
| `ledger_set_budget` | Set a monthly cap per agent; enforced at track time with a 402 |
| `ledger_report` | Pull a per-agent spend report |
| `ledger_alerts` | Anomaly alerts when spend spikes |
| `ledger_list_agents` | List all tracked agents |

A REST API mirrors the MCP surface: POST /v1/track, POST /v1/budget, GET /v1/report/{agent}, GET /v1/tokens/{agent}.

## Installation

```bash
claude mcp add agent-ledger --transport http https://agent-ledger-production-0ff8.up.railway.app/mcp/
```

## Configuration

```json
{
  "mcpServers": {
    "agent-ledger": {
      "type": "http",
      "url": "https://agent-ledger-production-0ff8.up.railway.app/mcp/"
    }
  }
}
```

No signup and no API key: the first track call for a new agent_id returns an agent_secret in the response. Save it - every later write to that agent_id must include it. Reads stay open with no secret.

## Business Relevance

- **Operators running fleets of agents** get one spend ledger across every payment rail instead of stitching together Stripe, x402 wallets and API-key invoices.
- **Finance teams** get a real audit trail - every dollar an autonomous agent moves is attributable to an agent, a rail and a service.
- **Engineering leads** get hard budget caps that fail closed (402) instead of post-hoc surprise invoices.
- **Anyone evaluating agent ROI** can compare per-agent spend against per-agent output with the token burn report.

## Integration with CorpusIQ

AgentLedger pairs with CorpusIQ's own agent operations: while CorpusIQ runs the business - Stripe revenue, QuickBooks books, HubSpot pipeline - AgentLedger tracks the agent side of the cost equation. A composed workflow: CorpusIQ reports monthly platform spend, AgentLedger reports monthly agent-rail spend, and the two feed the same monthly operating review. Operators can ask one assistant "what did automation cost us this month across platform and agents" and get a complete answer instead of two separate exports.

## Limitations

- Brand new - no track record yet; v0.1-era remote endpoint on a railway.app host.
- Beta free tier caps at 3 agents; real fleets need the $19/mo Pro plan.
- No self-host option published - the ledger lives on the vendor's endpoint.
- Write auth is a per-agent secret string, not scoped OAuth - treat the secret as a credential.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
