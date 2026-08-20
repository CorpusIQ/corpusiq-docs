---
title: "Taskfolk MCP - Project Management for Teams and AI Agents"
description: "First-party remote MCP server from Taskfolk exposing the same roughly 180-operation workspace surface as its REST API (issues, projects, sprints, comments, agents) to AI agents, with scoped API keys, webhooks, and per-call usage and audit views"
category: Productivity
stars: n/a (new listing)
added: 2026-08-20
source: "mcpservers.org (taskfolk-ai)"
relevance: ★★
tags: [project-management, task-management, remote-mcp, api, teams, sprints, productivity]
---

# Taskfolk MCP

**Project management for teams and their AI agents over a first-party remote MCP.** Taskfolk is a project-management platform (boards, backlogs, sprints, timelines, docs, reports, and workflows) whose developer platform exposes a versioned REST API of roughly 180 operations — and a first-party MCP server that exposes the same operations to AI agents, so an agent works through the exact API your own code does.

```
Server type: Hosted remote (Streamable HTTP)
Endpoint: https://taskfolk.ai/api/mcp/v1
Auth: API keys scoped to each integration's permissions
Tools: Mirrors the versioned REST API (~180 operations)
Built by: Taskfolk (taskfolk.ai)
```

## Why This Matters for Operators

Most MCP-to-project-management bridges wrap a subset of a platform and drift from its real API. Taskfolk's MCP server is first-party and sits on the same OpenAPI contract as its REST surface — the OpenAPI spec is the source of truth, giving a clean path to generated SDKs and identical semantics whether the caller is code or an agent. Usage and audit views show every call and change, so you can see what an integration did and when.

## Tools & Capabilities

| Surface | What it covers |
|---|---|
| Work | Issues, projects, sprints, comments, and agents across the workspace |
| REST parity | The MCP server exposes the same operations as the versioned `/api/v1` surface |
| Keys and webhooks | API keys scoped per integration; webhooks for events as they happen |
| Observability | Usage and audit views for every call and change |
| Developer dashboard | Keys, usage, audit, webhooks, and SDK guidance in one place |

## Installation

```json
{
  "mcpServers": {
    "taskfolk": {
      "type": "http",
      "url": "https://taskfolk.ai/api/mcp/v1",
      "headers": {
        "Authorization": "Bearer YOUR_TASFOLK_API_KEY"
      }
    }
  }
}
```

API keys are issued in the Taskfolk developer dashboard (taskfolk.ai/developer), scoped to the permissions each integration needs. The live OpenAPI reference lives at taskfolk.ai/api/v1/reference.

## Configuration

- Create an API key in the developer dashboard with the narrowest scope your agent needs
- Pass it as a bearer token on the MCP endpoint
- Subscribe to webhooks for the events your workflow reacts to
- Review usage and audit views after first runs to confirm scope and call volume

Pricing tiers are published at taskfolk.ai/pricing; the developer surface is available on the workspace plan you already run.

## Business Relevance

- **Teams running sprints and backlogs** let agents triage, create, and update issues through the same API their tooling uses
- **Ops leaders** get per-call audit trails for everything an agent changed
- **Agent builders** ship project-management workflows with one OpenAPI source of truth
- **Agencies** manage client boards through scoped keys per engagement

## Integration with CorpusIQ

Taskfolk covers team execution tracking — adjacent to, not overlapping, CorpusIQ's finance and analytics connectors. In one agent session, an ops team can have agents update sprints and issues through Taskfolk while CorpusIQ reports on the business layer: QuickBooks for budget, Stripe for payments, and GA4 for launch metrics — then join the two on project or client name. The scoped-key and audit-view design matches CorpusIQ's provenance discipline.

## Limitations

- Newer listing (Aug 2026) with a smaller community than the giants it compares against
- Requires a Taskfolk workspace and API key; no anonymous read surface
- MCP surface is a mirror of the REST API — no capabilities beyond the API contract

## See Also

- [Atono MCP Server — Agile Project Management for Agents](/hermes/mcp/servers/external/atono-mcp-server/)
- [MCPGRAM MCP — OAuth Connectivity Gateway for AI Agents](/hermes/mcp/servers/external/mcpgram-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
