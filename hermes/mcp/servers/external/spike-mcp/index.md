---
title: "Spike MCP - Incident Management and On-Call for AI Assistants"
description: "Official hosted MCP server from Spike: 59 tools (51 with an API key) that let AI assistants query incidents, analyze alerts, manage on-call rotations, route alerts and tune escalation policies without leaving chat."
category: DevOps
stars: "n/a (closed source)"
added: 2026-08-29
source: mcpservers.org /all
relevance: ★★★
tags: [mcp-server, incident-management, on-call, alerting, monitoring, webhooks, devops, remote-mcp]
---

# Spike MCP

**Official hosted MCP server from Spike, the incident management and on-call platform.** 59 tools with OAuth (51 with an API key) cover the full incident loop: stats and MTTA/MTTR reporting, incident create/ack/resolve, on-call rotations and overrides, alert routing rules, outbound webhooks, and escalation policy configuration. The server is a stateless bridge at one Streamable HTTP endpoint that stores no data, keeps no credentials, and by design cannot delete, archive or restore anything.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (interactive) or x-api-key plus x-team-id headers (automation)
Endpoint: https://mcp.spike.sh/mcp
Tools: 59 with OAuth, 51 with an API key (8 write tools are OAuth only)
Pricing: Free plan for small teams; paid plans for larger organizations
Category: DevOps / Incident management
Built by: Spike (spike.sh)
```

## Why This Matters for Operators

Incident response normally means context-switching between a pager, a dashboard and a war room. The Spike MCP puts the whole loop in the assistant: ask for this week's MTTR, see every open sev1 and its owner, acknowledge an incident and add a note, then check who is on call next, without leaving the chat thread you already have open.

Two design choices make it safe for production. The server keeps no data and no credentials; every request forwards your key or token and forgets it. And there are no destructive tools: nothing can archive, delete or restore, so a misdirected prompt cannot wipe escalation policies. Eight write tools (reassign, add or remove responders, add note, mute, unmute) require OAuth because they must be attributed to a real person in the timeline.

**The assistant can reason about an incident with the get_incident eight-part briefing instead of raw JSON.**

## Tools & Capabilities

| Area | Tools |
|---|---|
| Discovery | `list_teams`, `list_users`, `list_integrations`, `list_integration_types`, `list_escalation_policies`, `list_services`, `get_integration` |
| Incidents | `incident_stats` (totals, MTTA/MTTR, top offenders), `list_incidents`, `search_incidents`, `get_incident` (eight-part briefing: assessment, raw alert payload, execution timeline, routing, blast radius, repeat pattern, suggested next tools), plus create, acknowledge, resolve, unacknowledge, escalate, priority/severity, and OAuth-only reassign, add or remove responders, add note, mute, unmute |
| On-call | `who_is_on_call`, `who_is_on_call_next`, `get_active_shift`, `list_schedules`, `get_schedule`, `get_user_upcoming_shifts`, `check_user_on_call`, `list_overrides`, `create_override`, `remove_override` |
| Alert routing | `list_alert_routing_rules`, `get_alert_routing_rule`, `update_alert_routing_rule`, `create_alert_routing_rule` (OAuth only) |
| Outbound webhooks | `list_outbound_webhooks`, `get_outbound_webhook`, `update_outbound_webhook`, `test_outbound_webhook`, `create_outbound_webhook` (OAuth only) |
| Configuration | Create and update escalation policies, services, integrations, and on-call schedules, plus add, update and remove rotation layers |

## Installation

```bash
claude mcp add spike --transport http https://mcp.spike.sh/mcp
```

The first connection opens a browser for OAuth. The vendor also publishes walkthroughs for claude.ai, Cursor, Claude Desktop, ChatGPT and Codex.

## Configuration

```json
{
  "mcpServers": {
    "spike": {
      "type": "http",
      "url": "https://mcp.spike.sh/mcp",
      "headers": {
        "x-api-key": "YOUR_API_KEY",
        "x-team-id": "YOUR_TEAM_ID"
      }
    }
  }
}
```

Interactive use authenticates with OAuth and actions run with your role's permissions. For programmatic agents, generate an API key under Settings - API in the dashboard, find the team ID, and pass both headers. The team ID is required for incident write tools so requests are always scoped to your organization; a curl initialize call to the endpoint returns a JSON-RPC authentication-required error when no credential is sent (verified live).

## Business Relevance

- **SRE and DevOps leads** get incident stats, MTTA/MTTR and top-offender reports in chat instead of exporting dashboard data.
- **On-call engineers** acknowledge, escalate, note and resolve incidents from the assistant they already use, with actions attributed to them.
- **Engineering managers** review open sev1s, ownership and escalation paths without a dashboard login.
- **Platform teams** set up day/night rotations, overrides and alert routing rules as single natural-language requests.
- **Operations teams** wire outbound webhook tests and integration configuration into runbooks without navigating the UI.

## Integration with CorpusIQ

Spike handles the incident side; CorpusIQ handles the business context around it. A composed workflow: when the payments API degrades, the assistant creates and tracks the sev2 in Spike, then reads Stripe transaction volume and refund counts through CorpusIQ connectors in the same thread to quantify revenue impact, and finally joins MTTR from Spike with GMV from CorpusIQ for a post-incident review that connects engineering response to business cost. CorpusIQ's read-only financial data and Spike's read-write incident loop cover both halves of an outage.

## Limitations

- API-key connections see 51 of 59 tools; eight write tools that must be attributed to a person are OAuth only.
- Closed source and hosted: no self-host option, and the MCP requires a Spike account.
- No destructive actions by design; deleting or archiving incidents still happens in the dashboard.
- The team ID header is mandatory for incident writes; a missing header is refused.
- Tool identifiers are not interchangeable (service counterId vs integration token vs entity IDs); the tool descriptions carry the mapping.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [HostTracker MCP - Uptime Monitoring from 300+ Locations](/docs/hermes/mcp/servers/external/hosttracker-mcp)
- [healthchecks-mcp - Cron Job Health and Failure Forensics for Agents](/docs/hermes/mcp/servers/external/healthchecks-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
