---
title: healthchecks-mcp - Cron Job Health and Failure Forensics
description: "Open-source stdio MCP server for Healthchecks: see which cron jobs and scheduled tasks are down, read the failing job's output, and create or adjust checks against the hosted or self-hosted service."
category: Business Operations
stars: n/a (new listing, ni-c/healthchecks-mcp)
added: 2026-08-29
source: "chatmcp/mcpso issue #3822"
relevance: ★★
tags: [mcp-server, cron-monitoring, uptime, healthchecks, ops, devops, alerts, self-hosted]
---

# healthchecks-mcp

**An open-source stdio MCP server for Healthchecks, the dead man's switch for cron jobs and scheduled tasks: an agent can see which jobs stopped checking in, read the output the failing job reported, and create or adjust checks - against the hosted service or a self-hosted instance alike.** Fourteen tools cover the Management API v3, with the killer one being get_ping_body: it returns the actual traceback or log line a job posted with its ping, which is the failure's own explanation.

```
Server type: Local (stdio) - npm package healthchecks-mcp
Auth: Healthchecks API key (read-only keys fully supported)
Endpoint: n/a (stdio; talks to Healthchecks API v3, hosted or self-hosted)
Tools: 14 (9 read, 5 write)
Pricing: Free open source (MIT); Healthchecks account for hosted use
Category: Business Operations / Monitoring
Built by: ni-c/healthchecks-mcp; MIT; docs at healthchecks-mcp.ni-c.de
```

## Why This Matters for Operators

"One of the crons is down" is the start of an investigation, not the answer - you still have to find which job, since when, how often, and why, and the why usually lives in the job's own log output. healthchecks-mcp turns that investigation into questions: list_checks shows what is healthy, get_ping_body returns the failing job's last output with the traceback intact, and list_flips shows the history of state changes.

Read-only API keys are supported end to end, which matters: Healthchecks returns a different object shape for read-only keys (no uuid or ping_url, a 40-character unique_key instead), and this server addresses checks by unique_key where that is all there is. Write tools sit behind a confirmation token and can be switched off entirely.

**The agent reads the failure's own output, not just the alert - and read-only keys work correctly end to end.**

## Tools & Capabilities

14 tools, narrowable via HEALTHCHECKS_ALLOW_TOOLS (essential = curated seven).

| Tool | Purpose |
|---|---|
| `list_checks`, `get_check` | Enumerate and read checks and their status |
| `list_pings`, `get_ping_body` | Read ping history and the failing job's posted output (traceback or log line) |
| `list_flips` | State-change history: which check flipped, when, how often |
| `list_integrations`, `list_badges` | Read notification integrations and badge configs |
| `get_status`, `get_api_key_info` | Instance status and API-key capability probe |
| `create_check`, `update_check` | Create and adjust checks (confirmation-token gated) |
| `pause_check`, `resume_check`, `delete_check` | Lifecycle controls (confirmation-token gated) |

## Installation

```bash
claude mcp add healthchecks --env HEALTHCHECKS_ALLOW_TOOLS=essential -- npx -y healthchecks-mcp
```

Works against healthchecks.io and any self-hosted instance. Full per-client docs at healthchecks-mcp.ni-c.de; a container image is published at ghcr.io/ni-c/healthchecks-mcp.

## Configuration

```json
{
  "mcpServers": {
    "healthchecks": {
      "command": "npx",
      "args": ["-y", "healthchecks-mcp"],
      "env": {
        "HEALTHCHECKS_API_KEY": "your-project-read-only-key",
        "HEALTHCHECKS_ALLOW_TOOLS": "essential"
      }
    }
  }
}
```

Prefer a read-only project key for agent use; escalate to a write key only when the agent should create or adjust checks, and keep the confirmation-token flow enabled.

## Business Relevance

- **Ops teams** ask the agent which cron is down and read the failing job's traceback in the same conversation.
- **Founders running their own infra** get cron health without leaving chat or building a dashboard.
- **Teams with compliance needs** keep read-only keys on agents, so monitoring can be inspected but not modified.
- **Self-hosters** use the same server against a private Healthchecks instance.

## Integration with CorpusIQ

healthchecks-mcp gives CorpusIQ-driven workflows an ops feedback loop: a CorpusIQ agent running scheduled reports or connector syncs can check its own cron health through Healthchecks, read the failure body when a job breaks, and file the fix in the same session. For operators running both stacks, the CorpusIQ connectors hold the business data while Healthchecks holds the schedule truth - and the agent that reads the books can also watch the jobs that update them.

## Limitations

- Brand new - repo created August 27, 2026, zero stars; npm and container artifacts are published.
- stdio only - no hosted endpoint.
- Requires a Healthchecks account (free tier exists) or a self-hosted instance.
- Monitoring scope is Healthchecks checks specifically - not a general infrastructure monitor.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [HostTracker MCP - Uptime Monitoring from 300+ Locations](/docs/hermes/mcp/servers/external/hosttracker-mcp)
- [Centipid ISP Billing MCP - Subscriber and Network Operations Data](/docs/hermes/mcp/servers/external/centipid-billing-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
