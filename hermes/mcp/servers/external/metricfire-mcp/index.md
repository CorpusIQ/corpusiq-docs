---
title: "MetricFire MCP - Natural Language Infrastructure Monitoring"
description: "Official MetricFire MCP server for Hosted Graphite: search metrics by pattern, render Graphite output as JSON, CSV, PNG, or SVG, manage alerts with AND/OR criteria, notification channels, and scheduled mutes - all from an AI assistant."
category: DevOps
stars: n/a (no public repo)
added: 2026-08-26
source: mcpservers.org
relevance: ★★
tags: [mcp-server, monitoring, graphite, alerts, metrics, observability, remote-mcp]
---

# MetricFire MCP

**Your Hosted Graphite account, operated in natural language.** MetricFire's official MCP server connects AI assistants (GitHub Copilot, Cursor, Claude Code) to a Hosted Graphite account for metric discovery, Graphite rendering, alert management, notification channels, and scheduled mutes - without writing a single API call. The hosted endpoint is mcp.hostedgraphite.com, authenticated with a dedicated MCP token minted in the account.

```
Server type: Remote (Streamable HTTP)
Auth: X-HostedGraphite-MCP-Token header (read / write / delete scopes)
Endpoint: https://mcp.hostedgraphite.com/
Tools: Metric search, Graphite render, alerts, channels, scheduled mutes
Pricing: Hosted Graphite account (free trial, then paid tiers)
Category: DevOps / Observability
Built by: MetricFire (Hosted Graphite)
```

## Why This Matters for Operators

Monitoring is only useful when someone actually looks at it. The MetricFire MCP server lets an assistant search metrics by pattern, render a Graphite time series as JSON, CSV, PNG, or SVG, and create or mute alerts - so a developer or ops operator can ask "what is p95 latency doing right now" and get a rendered chart in chat. Alert management with composite AND/OR criteria, notification channels (Email, Slack, PagerDuty), and scheduled mute windows (e.g., weekends) round out the operational surface. **The assistant becomes the monitoring front-end that already knows the metric names.**

## Tools & Capabilities

| Area | What it does |
|---|---|
| Metrics | Standard and tagged search, busy metrics, invalid metrics, metric deletion |
| Graphite Render | Time-series data as JSON, CSV, raw, PNG, or SVG for a specified range |
| Alerts | Create, update, search, delete, mute/unmute - composite AND/OR criteria, status and history checks |
| Notification Channels | Retrieve, create, update, delete Email/Slack/PagerDuty/webhook channels and associate with alerts |
| Scheduled Mutes | Create and manage recurring mute windows and link them to alerts |

## Installation

```bash
claude mcp add metricfire --transport http https://mcp.hostedgraphite.com/
```

Mint a token in the account under Add-Ons → MetricFire MCP Server, selecting read-only (recommended) or write/delete scopes. Claude connects with the token in the URL: `https://<MF-MCP-TOKEN>@mcp.hostedgraphite.com`.

## Configuration

```json
{
  "mcpServers": {
    "mf-mcp-server": {
      "type": "http",
      "url": "https://mcp.hostedgraphite.com/",
      "headers": {
        "X-HostedGraphite-MCP-Token": "YOUR-MCP-TOKEN"
      }
    }
  }
}
```

## Business Relevance

- **DevOps operators** search and render metrics and manage alerts from chat during incidents.
- **SRE teams** create composite alerts and schedule weekend mutes without dashboard clicks.
- **Startup technical founders** keep a lightweight monitoring surface without hiring around it.
- **Support engineers** check service health and render charts while triaging customer reports.
- **FinOps-adjacent teams** watch resource metrics trends (via rendered series) alongside cost data.

## Integration with CorpusIQ

CorpusIQ brings the business numbers - revenue from Stripe, ad spend from Google Ads, pipeline from HubSpot - while MetricFire brings the infrastructure numbers. A composed workflow: the assistant reads GA4 traffic and Shopify orders through CorpusIQ to spot a demand spike, then asks MetricFire whether the web tier is under load or erroring at the same moment, then checks alerts for what fired. The two views together turn "traffic went up" into "traffic went up AND the API latency followed" - a complete operator story in one thread.

## Limitations

- Hosted Graphite account required; metrics must already be forwarded before MCP can search them.
- Token permissions are account-level - a write token can modify alerts, so mint read-only tokens by default.
- No dashboard management yet (vendor lists it as coming soon).
- Monitoring-focused: no business-data connectors - pairs with, rather than replaces, data connectors.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
