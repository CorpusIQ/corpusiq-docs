---
title: "Coldrig MCP - CorpusIQ Docs - CorpusIQ Docs"
description: "Agent-native cold email infrastructure with 28 MCP tools - buy domains, provision mailboxes, run warmup, launch campaigns and monitor deliverability"
category: Marketing
stars: n/a (new listing)
added: 2026-08-18
source: mcp.so GitHub issues
relevance: ★★★
tags: [cold-email, outreach, deliverability, warmup, sales-ops, remote-mcp, sequences]
---

# Coldrig MCP (agent-cold-email)

**Agent-native cold-email infrastructure exposed as 28 MCP tools — an AI agent operates the entire stack end to end: buy domains, provision mailboxes, run warmup, launch sequences and campaigns, handle replies, and monitor deliverability.** Built by the platform vendor as the official implementation. Remote streamable HTTP with Bearer auth plus a local stdio path via npm. Sandbox mode is free; live sending is $99/month.

```
Server type: Remote (Streamable HTTP) + local stdio
Auth: Bearer token via POST /signup (free, no card) for remote; npx for stdio
Endpoint: https://agent-cold-email-api.yaakovscher.workers.dev/mcp
Tools: 28
Pricing: Sandbox free; live sending $99/month
Category: Marketing / Sales Operations
Built by: Coldrig (npm: agent-cold-email, repo: YS-projectcalc/agent-cold-email)
```

## Why This Matters for Operators

Outbound email normally requires three roles — domain provisioning, deliverability engineering, and sequence management — before the first reply arrives. Coldrig collapses them into tool calls an agent can run, so a single agent owns the funnel from "no sending infrastructure" to "campaign live with monitored deliverability" without a sales-ops hire.

**The isolation model is the point.** Provisioned domains and mailboxes keep sending reputation separated from the main business domain; warmup runs before volume; and deliverability monitoring is a first-class tool rather than an afterthought. The $99/month live tier buys the infrastructure that would otherwise cost a sales-ops contractor more in the first week.

## Tools & Capabilities

| Tool area | What it does |
|---|---|
| Domain purchasing | Buy isolated branded sending domains |
| Mailbox provisioning | Create mailboxes per domain |
| Warmup | Run automated warmup before sending volume |
| Sequences / campaigns | Define and launch multi-step sequences |
| Replies | Handle inbound replies from the agent |
| Deliverability | Monitor placement, spam signals, and reputation |

28 tools total across the lifecycle. Sandbox mode exercises the full surface without spending on live sending.

## Installation

```bash
# stdio via npm (sandbox or live with token)
npx agent-cold-email
```

```json
{
  "mcpServers": {
    "coldrig": {
      "type": "http",
      "url": "https://agent-cold-email-api.yaakovscher.workers.dev/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_TOKEN"
      }
    }
  }
}
```

Remote tokens are issued by `POST /signup` (free, no card). Live sending requires the $99/month plan.

## Configuration

Sandbox mode is the default entry point and is free. Moving to live sending attaches a billing plan and unlocks the provisioning and warmup tools against real domains. Standard cold-email discipline still applies: warmup before volume, low daily send counts per mailbox, and reply handling to protect deliverability — the tools enforce the workflow, but the operator sets the cadence.

## Business Relevance

- **Founders without sales ops** get a complete outbound stack operated by the agent they already run
- **Agencies** stand up isolated sending infrastructure per client without touching client domains
- **Sales teams** get sequence launches and reply loops in chat rather than in a separate tool
- **Deliverability-conscious senders** get monitoring and warmup as built-in tools, not bolt-ons

## Integration with CorpusIQ

CorpusIQ's email connectors (Gmail via media@ and info@) are the inbound intelligence layer — lead identification, response tracking, and triage. Coldrig is the outbound execution layer — domains, warmup, sequences, sending.

The composed workflow: CorpusIQ mines and qualifies targets from inbound and market signals; Coldrig's agent runs the outbound sequence on isolated infrastructure; replies land back in the monitored inbox where CorpusIQ's triage picks them up. The two surfaces never share a domain, so outreach reputation stays separate from business-critical inbox reputation.

## Limitations

- Live sending is $99/month — sandbox only on free tier
- Brand new listing (submitted Aug 17, 2026); package at v0.2.1
- Remote endpoint runs on a Cloudflare Workers URL (vendor-managed)
- Cold email compliance (CAN-SPAM, GDPR) remains the operator's responsibility
- No published track record of deliverability outcomes yet
