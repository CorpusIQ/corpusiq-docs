---
title: "DialNexa MCP - CorpusIQ Docs"
description: Voice AI agent platform over MCP — create and manage voice agents, place outbound calls, run campaigns, and read metrics with OAuth 2.1
category: Communication
stars: n/a (new listing)
added: 2026-08-13
source: mcpservers.org
relevance: ★★★
tags: [voice-ai, telephony, outbound-calls, sales, campaigns, remote-mcp]
---

# DialNexa MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 PKCE) from DialNexa.** The first full voice-AI-agent platform observed with a production MCP surface: create, inspect, configure, and remove voice agents; find call records and place confirmed outbound calls; manage campaigns, leads, and batch calls; build workflow graphs; search and purchase phone numbers; and read dashboard metrics — all from chat, behind explicit safety levels.

```
Server type: Remote (Streamable HTTP, stateless)
Auth: OAuth 2.1 PKCE (mcp:read / mcp:write / offline_access scopes) or workspace API key
Endpoint: https://api.dialnexa.com/v1/mcp
Tools: 20+ (voice agents, calls, campaigns, workflows, knowledge bases, phone numbers, templates, billing, webhooks, metrics, integrations, prompt improvements)
Pricing: Commercial (DialNexa plans; billable tools marked)
Category: Voice AI / Sales
Built by: DialNexa (dialnexa.com)
```

## Why This Matters for Operators

Voice agents are moving from demo to operations, and the missing piece has been control — most platforms expose a dashboard, not a protocol. DialNexa exposes the whole lifecycle as MCP tools, and it classifies every tool as read only, state changing, destructive, or billable. **Tools that place calls, spend money, or permanently delete resources require explicit approval before they run** — the same human-gate architecture this sweep cycle keeps finding in production-grade servers.

**The consent model is workspace-scoped.** OAuth 2.1 with PKCE lets the user pick the workspace on the consent screen; tool arguments cannot switch workspaces afterwards. Read scope exists separately from write scope, so an assistant can watch metrics without ever touching the dialer.

## Tools & Capabilities

| Area | Capabilities |
|---|---|
| Voice agents | Create, inspect, configure, remove; AI-generated prompt improvements |
| Calls | Find call records, place confirmed outbound calls |
| Campaigns | Inspect campaigns, review leads, control batch calls |
| Workflows | Build workflow graphs, manage execution |
| Knowledge bases | Inspect and manage KB containers |
| Numbers | Search, purchase, inspect, configure phone numbers |
| Platform | Billing plans and rates, webhook config, workspace inspection, dashboard metrics, integrations, templates |

## Installation

```bash
claude mcp add --transport http dialnexa https://api.dialnexa.com/v1/mcp
```

OAuth-capable clients bootstrap from the `WWW-Authenticate` challenge and open the browser flow automatically. For API-key clients, send `Authorization: Bearer YOUR_API_KEY` on every request.

## Configuration

```json
{
  "mcpServers": {
    "dialnexa": {
      "type": "http",
      "url": "https://api.dialnexa.com/v1/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

## Business Relevance

- **Sales operators** build and tune voice agents from chat, then read call outcomes and weekly dashboards without leaving the assistant.
- **RevOps teams** scope read-only assistants for forecasting while write assistants run the dialer.
- **Support leaders** manage knowledge bases and workflows behind the same approval gates as outbound campaigns.
- **Multi-entity operators** keep workspaces isolated through the OAuth consent screen.

## Integration with CorpusIQ

DialNexa handles the voice channel; CorpusIQ owns the business data the voice channel feeds and reads. The composed pipeline: HubSpot or Close contacts (CorpusIQ CRM connectors) seed the campaign lists, DialNexa runs the confirmed outbound calls, and outcomes land back in the CRM — pipeline movement and revenue close through CorpusIQ's QuickBooks and Stripe connectors. Attribution mirrors CallRail-style tracking: call data from DialNexa, revenue truth from CorpusIQ, matched on the customer record.

## Limitations

- Commercial platform — billable tools (calls, number purchases) require per-action approval and budget discipline
- No self-host option — cloud API with workspace-scoped OAuth
- Safety classifications are vendor-defined; review destructive tool docs before granting write scope
- Newer listing — track record still forming

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
