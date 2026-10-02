---
title: "HostTracker MCP - Uptime Monitoring from 300+ Locations"
description: "Official HostTracker MCP server for uptime monitoring: run synchronous HTTP, ping, port, DNS, and whois checks from 300+ locations across 158 cities, list what is down, manage monitors, incidents, and status pages from any AI assistant."
category: DevOps
stars: 1
added: 2026-08-25
source: mcp.so feed
relevance: ★★
tags: [mcp-server, monitoring, uptime, alerts, status-pages, incidents]
---

# HostTracker MCP

**Your monitoring account, operable from chat.** HostTracker has run external website and infrastructure checks since 2004 for more than 500,000 websites. Its official MCP server puts 65 tools in front of an AI assistant: run a synchronous check from 300+ locations, see what is down, create or pause a monitor, schedule a maintenance window, review incidents, manage alert recipients, wire webhooks, and publish status page updates. The synchronous in-chat check is the headline: ask whether a site is up right now from Europe and Asia, and get a live answer.

```
Server type: Remote Streamable HTTP (hosted) with stdio Docker bridge
Endpoint: https://mcp.host-tracker.com/mcp
Auth: Authorization: Bearer <HostTracker API token>
Tools: 65 across 9 groups, plus a generic api_request door
Instant-check types: 10 (HTTP, Ping, Port, Trace, DNS, DNSBL, Whois, WebRisk, Crawl, Waterfall)
Repo: github.com/HostTracker/mcp (MIT)
```

## Why This Matters for Operators

Incident response is a context problem: by the time a human has the monitoring dashboard open, the assistant already knows the alert fired. HostTracker's MCP closes that gap with tools that operate the account directly. One API token powers the REST API, the SDKs, ht-cli, and the MCP server, so the assistant can check, pause, and document without a second credential surface.

## Tools & Capabilities

| Group | What it does |
|---|---|
| Instant checks | Synchronous HTTP, ping, port, traceroute, DNS, DNSBL, whois, web risk, crawl, and waterfall checks from 300+ checkpoints |
| Monitors | List what is down, create, edit, pause, and delete monitors |
| Maintenance | Schedule and manage maintenance windows |
| Incidents | Open, review, and resolve status-page incidents |
| Alerting | Manage who gets alerted and how |
| Webhooks | Wire and test webhook endpoints |
| Status pages | Publish and update status page content |
| Account | Monitor groups, tags, and account settings |
| `api_request` | Generic door to the full API v2 surface |

## Installation

Mint a token at Integrations → API (start with `check` and `monitor:read` scopes), then connect:

```json
{
  "mcpServers": {
    "hosttracker": {
      "type": "http",
      "url": "https://mcp.host-tracker.com/mcp",
      "headers": { "Authorization": "Bearer YOUR_HOSTTRACKER_API_TOKEN" }
    }
  }
}
```

The repo also ships a stdio Docker bridge for clients that cannot open a remote connection.

## Configuration

One HostTracker API token with the scopes you want the assistant to have. 30-day free trial, no credit card. The repo (`HostTracker/mcp`) is the public face of the hosted server: connection metadata, per-client setup guide, and security policy.

## Business Relevance

- **Incident triage:** ask what is down and check it live from chat.
- **Ops automation:** pause staging monitors during deploys, resume after.
- **Evidence:** synchronous check receipts with location detail for SLA debates.
- **Status comms:** publish incidents to the status page from the same flow.

## Integration with CorpusIQ

HostTracker's check results and incident state pair with CorpusIQ connectors for reporting: log incidents to Airtable or Notion for postmortems, correlate outage windows with traffic dips in GA4, and render uptime dashboards alongside business metrics.

## Limitations

- Requires a HostTracker account and API token; the 65-tool surface needs an active subscription after trial.
- The hosted server's full source is not public; the repo documents the interface and bridges.
- Monitoring only your own configured targets; not a discovery scanner.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [PingCheck MCP - Status Page Monitoring for Agents](/hermes/mcp/servers/external/pingcheck-mcp)
- [World Monitor MCP](/hermes/mcp/servers/external/world-monitor-mcp)
