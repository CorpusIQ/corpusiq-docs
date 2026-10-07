---
title: "Raposa Aval MCP - Human Approval Gates with Audit Chains"
description: Give AI agents a human approval gate for high-stakes actions - refunds, payouts, deploys, deletions - where approved is true only when a named person presses Approve, sealed in a SHA-256 hash-chained audit log you can export and verify
category: Compliance
stars: n/a (new listing)
added: 2026-09-03
source: "mcp.so GitHub issue #3914"
relevance: ★★★
tags: [approval-gate, human-in-the-loop, audit-log, governance, compliance, stdio, api-key]
---

# Raposa Aval MCP

**Stdio MCP server that gives an agent one honest tool: ask a human.** `request_human_approval(action, context, risk)` returns `{ approved: true }` only when a named person pressed Approve - in a web console, from a signed email link, a Telegram card or a Slack message. A timeout, an expiry or a rejection all return `approved: false`: silence is not consent. Every decision is appended to a SHA-256 hash-chained audit log that the customer can export and verify, and the service is EU-hosted (Germany) with a DPA available.

```
Server type: Local (stdio via uvx)
Auth: RAPOSA_API_KEY (free sandbox key: 100 approvals/month)
Default base URL: https://dcescrypt.com/api (override via RAPOSA_API_BASE)
Tools: 3 (request_human_approval, create_approval, get_approval)
Pricing: Free sandbox (100 approvals/month, no expiry); paid plans for volume
Category: Governance / Approvals
Built by: DC ESCRYPT SL (raposa.group)
```

## Why This Matters for Operators

Most "agent safety" is prompt-wishful thinking: the model is told to ask before it acts, and nothing enforces it. Raposa makes the approval a protocol primitive the agent must call, and the answer a verifiable fact: who decided, when, and which action they authorized. That is the difference between "the agent asked" and "we can prove the agent asked" - which is what auditors, insurers and boards actually want when agents start touching payouts, refunds, deploys and deletions.

**The audit chain is the moat.** Each decision appends to a hash-chained log where tampering with one entry breaks every later hash. Export it, verify it, show it to an auditor. Named approvers, N-of-M signatures, reminders and escalation routes keep the gate human in practice, not just in design.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `request_human_approval(action, context, risk, ...)` | Creates the request and waits for a human decision; returns approved, decided_by, and timing |
| `create_approval(...)` | Returns the id immediately; decision arrives on an HMAC-signed webhook or via get_approval |
| `get_approval(approval_id)` | Reads one approval's status and decision |

Risk levels are `low | medium | high`. The API key is read from `RAPOSA_API_KEY` only and never appears in tool inputs or outputs.

## Installation

```json
{
  "mcpServers": {
    "raposa": {
      "command": "uvx",
      "args": ["raposa-mcp"],
      "env": { "RAPOSA_API_KEY": "<your key>" }
    }
  }
}
```

Claude Code: `claude mcp add raposa -e RAPOSA_API_KEY=<your key> -- uvx raposa-mcp`. Get the free sandbox key at raposa.group/start - it arrives by email in about a minute.

## Configuration

Approvers get a scoped console login; optionally their email, and every request also reaches them as a mail with signed Approve / Reject links. Their name is recorded on the decision. Set wait and expiry windows per call (default wait 600 seconds), and wire `create_approval` webhooks for async flows.

## Business Relevance

Agent-driven finance and operations teams get a single, auditable gate for high-stakes writes: refund approvals, payout holds, production deploys, destructive data operations. Because the gate is a standalone primitive, it layers on top of any agent or MCP stack without rebuilding vendor approval features, and the EU hosting plus DPA covers the compliance conversation from day one.

## Integration with CorpusIQ

CorpusIQ-connected agents answer from read-only business data, but the moment an operator lets an agent ACT (refund in Stripe, discount in Shopify, adjust a Google Ads budget), a gate like Raposa turns those writes from autonomous to governed. The pattern: CorpusIQ supplies the context, the agent proposes the action, Raposa holds the action until a named human approves, and the audit chain records it.

## Limitations

- One primitive, done well - no workflow engine or policy DSL; orchestration stays with the calling agent
- Free sandbox caps at 100 approvals/month
- Sandbox API calls go to the vendor's EU-hosted service, not fully self-hosted

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CampaignStack MCP - Safe LinkedIn and Email Outreach](/hermes/mcp/servers/external/campaignstack-mcp)
- [BulkPublish MCP - Multi-Platform Social Publishing for Agents](/hermes/mcp/servers/external/bulkpublish-mcp)
- [OSIR Domain MCP - Registrar Operations for Agents](/hermes/mcp/servers/external/osir-domain-mcp)
- [SEOmatic MCP - Real Search Console Data with Approval-Gated Fixes](/hermes/mcp/servers/external/seomatic-mcp)
