---
title: "WatchCron MCP - Know When a Job Stops Reporting"
description: "Nine tools to create, pause and read cron job monitors from an assistant, with a ping URL per job and incidents across nine alert channels."
category: Operations / Monitoring
stars: n/a (WatchCron subscription, API key)
added: 2026-10-27
source: "the published npm package watchcron-mcp 1.0.0 with its bin entry and repository README listing all nine tools, the vendor site watchcron.com with its feature and channel pages, and the mcpservers.org official listing"
relevance: ★★★
tags: [cron-monitoring, scheduled-jobs, uptime, alerting, incidents, ops, api-key, stdio]
last_updated: "2026-10-27"
---

# WatchCron MCP

**A scheduled job fails quietly. Nothing crashes, nothing pages: the report simply does not arrive, and the first person to notice is usually the customer. Dead man's switch monitoring exists for exactly this and is almost never wired up, because wiring it means another dashboard, another login and another set of schedules to keep in sync.**

```
Server type: Local (stdio)
Install:     npx -y watchcron-mcp
Auth:        WATCHCRON_API_KEY environment variable
Tools:       9, listed below
Alerting:    email, Slack, Discord, Google Chat, Matrix,
             Mattermost, ntfy, Opsgenie, PagerDuty, RocketChat,
             SMS and webhook channels
Built by:    WatchCron (watchcron.com)
Package:     watchcron-mcp 1.0.0 on npm, repo watchcron/watchcron-mcp
```

## Why This Matters for Operators

The monitors an operator actually needs are the ones nobody looks at: the nightly reconciliation, the invoice sync, the backup, the feed refresh. Each one is a line in a crontab and each one fails silently.

WatchCron inverts the check. The job pings a URL when it finishes, and silence past a grace period is the alert. An assistant holding this server can create the monitor, get the ping URL back, add it to the job, and then answer what is failing without anyone opening the dashboard. That is the difference between monitoring that exists and monitoring that gets used.

## What It Actually Does

The npm package `watchcron-mcp` version 1.0.0 publishes a `watchcron-mcp` binary and its README documents nine tools:

| Tool | What it does |
|---|---|
| `list_monitors` | Every cron job monitor in the project with current status, optionally filtered by tag. |
| `get_monitor` | Detail on one monitor by `uuid`. |
| `create_monitor` | Creates a monitor from a simple interval or a cron expression and returns the ping URL to add to the job. Also takes name, grace period and tags. |
| `update_monitor` | Changes schedule, grace period or tags. |
| `pause_monitor` | Pauses or resumes a monitor. |
| `delete_monitor` | Removes a monitor permanently. |
| `get_pings` | The ping history for a monitor, which is how you see a job that runs late rather than never. |
| `get_incidents` | Incidents raised, so the answer to what broke is a query rather than a memory. |
| `list_channels` | The configured alert channels available to attach. |

Setup is a stdio entry with `npx -y watchcron-mcp` and `WATCHCRON_API_KEY` from the WatchCron account, documented for Claude Desktop, Claude Code, Cursor and Windsurf. The platform's other monitors run on the same account: uptime, domain and SSL expiry, port, blocklist and cloud cron, with alerts routed to the channels listed above.

## The Part That Costs You Something

This is a control surface for alerting, and misconfiguration is silent in both directions.

- **A monitor with no ping looks healthy.** The monitor only knows what the job tells it. Wire the ping first and confirm one successful ping before trusting the status.
- **A grace period that is too tight is worse than none.** A job that usually takes 40 minutes with a 30 minute grace period pages every night, and a team that learns to ignore the page has no monitoring at all.
- **`delete_monitor` is permanent.** Removing the monitor removes its history, so pause a monitor you might want back.
- **The agent holds a write key.** Create, update, pause and delete are all available, so the API key given to this server is an operational credential and should be scoped and rotated like one.

## How It Is Contained

- **Local process, your own key.** Nothing is proxied: the server runs on the operator's machine with an API key, and the trust boundary is that key.
- **Ping URLs are outbound only.** The job sends one HTTP request; the job never exposes a port, and curl, wget or any HTTP client works.
- **Pause exists as a first-class tool.** A monitor can be silenced without deleting its history, which is the correct shape for maintenance windows.
- **Status is a query, not a dashboard.** `list_monitors` and `get_incidents` mean the state is readable from wherever the work happens.

## Limitations Recorded

- The published surface is local stdio through npm. No remote endpoint is documented, so a web-only client cannot attach it.
- `mcp.watchcron.com` does not resolve and `watchcron.com/mcp` refuses a POST, so do not invent an endpoint for a remote client.
- Alert channel coverage is the operator's own account configuration; `list_channels` reports what is wired, not what should be.
- Monitoring is only as good as the schedules: a monitor created with the wrong cron expression reports the wrong silence.

## FAQ

### Does the job need WatchCron installed?
No. The job sends one HTTP request to its ping URL when it finishes, from any language or shell, and the absence of that request is the alert.

### Can an assistant create monitors on its own?
Yes, and that is the useful part: create the monitor, take the ping URL, add it to the scheduled task, then verify a first ping. Keep creation behind a person until the naming and grace-period conventions are settled.

### What should I test first?
One monitor for the job whose failure would cost the most, with a grace period set from the job's real runtime, and an alert channel the team actually reads.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [World Monitor MCP - global event monitoring](/hermes/mcp/servers/external/)
- [CorpusIQ connectors for operational data](/hermes/mcp/)
