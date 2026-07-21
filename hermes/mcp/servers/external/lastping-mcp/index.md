---
title: "LastPing MCP — AI Agent Monitoring & Uptime"
description: "Monitoring by AI agent. Connect LastPing to your MCP client and let AI agents monitor services, check uptime, and alert on incidents."
source: github.com/tp322d/lastping-app
stars: 0
language: Unknown
transport: stdio
auth: None / API Key
category: DevOps & Monitoring
last_updated: 2026-07-21
---

# LastPing MCP — AI Agent Monitoring & Uptime

**Service monitoring accessible through MCP.** LastPing lets AI agents check service health, monitor uptime, and respond to incidents. Instead of configuring dashboards, operators can ask their AI agent "Is everything up?" and get real answers.

## What It Does for Operators

- **Uptime monitoring** — Check if services, APIs, and websites are responding
- **Incident detection** — AI agents can detect and report outages
- **Agent-native** — Monitoring queries happen in the same conversation as other operations
- **Lightweight** — No heavy monitoring infrastructure to manage

## Installation

```bash
git clone https://github.com/tp322d/lastping-app.git
cd lastping-app
# Follow repo instructions for setup
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "lastping": {
      "command": "node",
      "args": ["path/to/lastping/server.js"]
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `check_status` | Check current status of monitored services |
| `ping_service` | Ping a specific service endpoint |
| `get_uptime` | Retrieve uptime history and SLA metrics |
| `list_incidents` | List recent incidents and outages |

*Note: Tool names are approximate. Full documentation pending at github.com/tp322d/lastping-app.*

## Operator Use Cases

1. **Solo Operators** — "Is my SaaS up right now?" → instant status check from AI agent
2. **DevOps Teams** — Include service health in daily AI standup reports
3. **Agency Owners** — Monitor client sites without leaving the AI conversation
4. **On-Call Engineers** — First-line incident triage through AI agent

## CorpusIQ Angle

LastPing fills a simple but essential need: "is everything working?" For operators running businesses on AI agents, service monitoring through the same MCP interface reduces context switching. Pair with CorpusIQ for business metrics + LastPing for technical health in one unified AI dashboard.

## Limitations

- Early-stage project — limited documentation and community
- Unknown scalability for large service fleets
- No integrations with PagerDuty/OpsGenie yet
- Installation instructions sparse as of July 2026
