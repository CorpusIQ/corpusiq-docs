---
title: Watchgoose MCP - Cron Monitoring and Failure Forensics for Agents
description: Hosted Watchgoose MCP server for monitoring cron jobs and recurring work. Ten tools let agents list checks, read status flips and pings, and create, update, pause or resume checks under OAuth 2.1 PKCE with read-only access selected by default.
category: Business Operations
stars: n/a (new listing)
added: 2026-09-04
source: mcpservers.org
relevance: ★★★
tags: [cron-monitoring, uptime, alerts, reliability, devops, oauth, pkce, remote-mcp]
---

# Watchgoose MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 PKCE)** - a project-scoped connection from Watchgoose, the cron and recurring-work monitoring service. Ten tools expose checks, status flips and pings, plus the full check lifecycle, with read-only access selected by default on the consent screen.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1, PKCE, Dynamic Client Registration
Endpoint: https://mcp.watchgoose.com/mcp
Tools: 10 (read plus write under mcp:write scope)
Pricing: Watchgoose plans (project-scoped connections)
Category: Business Operations
Built by: Watchgoose
```

## Why This Matters for Operators

Operators run automations that fail silently: backup jobs, report crons, invoice syncs. The value of monitoring is knowing first, and Watchgoose's MCP server puts that knowledge in the same conversation where the fix gets planned. **An agent can list flips since yesterday, identify which check went down, read the schedule and pause it before the retry storm starts.**

The consent model is unusually tight. Each connection is limited to one project, the consent screen always starts at read-only, and write scope is only offered when the client requests mcp:write and the user has permission to modify that project. Private fields like ping URLs, source IPs, user agents and ping bodies are never returned to the client.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_checks` | List checks with optional slug or tag filters |
| `get_check` | Get one check, its current state and schedule |
| `list_flips` | List retained status changes with up and down history |
| `list_pings` | List recent signals without source or body data |
| `list_channels` | List integration names and kinds for assignments |
| `create_check` | Create a simple, cron or OnCalendar check |
| `update_check` | Change selected fields on a check |
| `pause_check` | Pause monitoring without deleting a check |
| `resume_check` | Resume a paused check |
| `delete_check` | Permanently delete a check and its retained history |

## Installation

```bash
claude mcp add --transport http --scope user watchgoose https://mcp.watchgoose.com/mcp
```

Complete the browser authorization when prompted, then run `claude mcp get watchgoose` to inspect the saved connection. Any remote client with OAuth 2.1, PKCE and Dynamic Client Registration support works.

## Configuration

```json
{
  "mcpServers": {
    "watchgoose": {
      "url": "https://mcp.watchgoose.com/mcp"
    }
  }
}
```

Auth notes: no API key is pasted into a remote client. The OAuth issuer is the endpoint itself, the consent screen picks exactly one project, and read-only is the default. Write access requires a new authorization and permission on the selected project.

## Business Relevance

- **Automation operators** ask what flipped overnight instead of grepping email alerts.
- **Agency teams** give each client one project-scoped connection with read-only default.
- **Incident responders** pause a flapping check from the same thread where they diagnose it.
- **Reliability leads** keep audit events for 90 days and revoke connections from account settings.

## Integration with CorpusIQ

Watchgoose watches the automations; CorpusIQ watches the business. When a nightly data sync cron goes down, Watchgoose surfaces the flip and the schedule while CorpusIQ's connectors confirm the blast radius, whether yesterday's Stripe or Shopify numbers still arrived. Monitoring and business context land in one conversation, and the operator pauses, fixes and verifies without switching tools.

## Limitations

- One connection is scoped to one project; multi-project setups need multiple connections.
- Write tools require the mcp:write scope plus project permission, so agent-driven changes are deliberately slow to grant.
- Rate limits and audit retention (90 days) are service-defined; no self-host option.
- Brand new listing; Watchgoose's MCP surface launched recently.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [healthchecks-mcp - Cron Job Health and Failure Forensics for Agents](/docs/hermes/mcp/servers/external/healthchecks-mcp)
- [HostTracker MCP - Uptime Monitoring from 300+ Locations](/docs/hermes/mcp/servers/external/hosttracker-mcp)
