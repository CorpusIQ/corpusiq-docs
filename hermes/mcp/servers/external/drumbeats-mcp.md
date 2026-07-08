---
title: "Drumbeats MCP — Uptime & Cron Monitoring for AI Agents"
description: "Operate Drumbeats monitoring from any AI client — create cron/heartbeat monitors, triage incidents, and manage status pages without leaving your agent. DevOps observability over MCP."
category: mcp
tags: [mcp-server, monitoring, uptime, cron, heartbeat, devops, sre, observability]
last_updated: 2026-07-08
---

# Drumbeats MCP — Uptime & Cron Monitoring

## What It Is

Drumbeats MCP (`drumbeats-io/mcp`) brings cron/heartbeat monitoring, uptime checks, and incident management to AI agents over MCP. DevOps teams can create monitors, triage alerts, and manage status pages directly from their AI assistant — turning "Is the API down?" into an instant query with diagnostic context.

## Tools Available

| Tool | Description |
|------|-------------|
| Monitor CRUD | Create, read, update, delete cron and heartbeat monitors |
| Incident triage | View active incidents, acknowledge, resolve |
| Status pages | Manage public/private status page components |
| Uptime query | Check current status of any monitored endpoint |

## Quick Start

```bash
DRUMBEATS_API_KEY={key} npx -y @drumbeats/mcp
```

## Business Use Cases

1. **Incident response**: "Show me all active incidents — what's impacted and who's the on-call?"
2. **Postmortem prep**: "What monitors triggered before the 3:14 AM outage? Timeline the alerts"
3. **Status automation**: "Update the status page to reflect the CDN issue — mark as investigating"
4. **Health checks**: "Run a health check on all production endpoints and flag any with response time > 500ms"

## Limitations

- **Drumbeats-specific**: Requires a Drumbeats account and API key
- **No metric queries**: Focused on uptime/heartbeat — not a full APM (no CPU, memory, latency percentiles)
- **Local-only transport**: API-key based, not remote SSE

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Infrastructure Monitoring](/hermes/governance/monitoring/)
