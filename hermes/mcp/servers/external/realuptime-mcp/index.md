---
title: "RealUptime MCP - Uptime, Status and Outage Intelligence for Agents"
description: "RealUptime MCP exposes four connected products through one server: public status pages, multi-region uptime monitoring, application error tracking and free third-party outage checks. A keyless public endpoint serves 7 probe-backed outage tools with no account, and a keyed endpoint manages the operator's own monitors, incidents and status pages."
category: Business Operations
stars: 0
added: 2026-09-07
source: "chatmcp/mcpso issue #3975"
relevance: ★★★
tags: [uptime, monitoring, status-pages, outages, incident-management, remote-mcp, keyless]
---

# RealUptime MCP - Uptime, Status and Outage Intelligence for Agents

**Remote MCP server (Streamable HTTP; keyed and keyless endpoints)** - RealUptime wraps four products in one MCP surface: Status (public status pages and incident communication), Monitor (multi-region uptime monitoring), Errors (application error tracking) and Outages (free "Is X down?" checks on roughly 200 popular third-party services). The keyless public endpoint is probe-verified and served 7 tools with no signup.

```
Server type: Remote (Streamable HTTP, stateless)
Auth: Keyed endpoint (API key) for account operations; keyless public endpoint for outage intelligence
Endpoints: https://mcp.realuptime.io/mcp (keyed, probe-verified 401) and https://mcp.realuptime.io/public (keyless, probe-verified with 7 tools)
Tools: 7 public outage tools; account-scoped tools for monitors, incidents, status pages and errors
Pricing: Free read access included with every account; plans at realuptime.io
Category: Business Operations
Built by: RealUptime (realuptime.io); no public repo (private monorepo)
```

## Why This Matters for Operators

"Is it us or is it them" is the most expensive question in incident response. RealUptime answers it from its own scheduled probe measurements - never scraped from vendor status pages - with every answer carrying its measurement time and a citation URL. The agent can check whether a third-party service, a shared-infrastructure layer or the internet at large is degraded before the team opens an internal war room.

**The keyless endpoint is a genuine differentiator: an agent can answer outage questions with zero setup, and every account gets free read access to monitor status, incidents and third-party outage data before any paid plan.**

## Tools & Capabilities

| Group | What the agent does |
|---|---|
| Outage checks (public) | is_service_down and get_regional_readings with per-region status, latency and measurement detail |
| Report volume | get_report_volume: how many people are reporting problems, by region, against trailing baselines |
| Incident history | list_recent_incidents with the most recent closed outage per service |
| Stack and internet health | get_stack for named service stacks; internet_weather and is_the_internet_down for shared-infrastructure incidents |
| Account operations (keyed) | Create and manage monitors, incidents, status pages and maintenance windows; search error issues |

## Installation

Keyless: point any Streamable HTTP client at the public endpoint with no headers. Keyed: create an API key in the RealUptime dashboard and use the account endpoint.

```json
{
  "mcpServers": {
    "realuptime-public": {
      "type": "http",
      "url": "https://mcp.realuptime.io/public"
    }
  }
}
```

## Configuration

```json
{
  "mcpServers": {
    "realuptime": {
      "type": "http",
      "url": "https://mcp.realuptime.io/mcp"
    }
  }
}
```

Attach the API key as the bearer authorization header on the keyed endpoint. Both endpoints are stateless Streamable HTTP with no SSE or session cookies; health checks run at https://mcp.realuptime.io/health.

## Business Relevance

- **SRE and ops teams** get "is it us or them" answers with citations before paging anyone.
- **Support teams** check third-party service status while triaging customer tickets.
- **Agencies** operate status pages and incident communication for clients from the agent.
- **Founders** get a free, credential-less outage intelligence surface for the tools their stack depends on.

## Integration with CorpusIQ

RealUptime tells the agent whether a dependent service is down; CorpusIQ tells it whether the business felt it. A composed workflow: the agent checks RealUptime outage signals, then pulls revenue, order and traffic data from CorpusIQ's Stripe, Shopify and GA4 connectors to quantify incident impact and feed the incident postmortem.

## Limitations

- Brand new listing (issue #3975, Sep 6, 2026); no public repository exists (private monorepo), so the guide relies on the vendor's documented surface and live probes.
- The public endpoint covers the outage product; monitor, status page and error management require an account key.
- Outage coverage is limited to the roughly 200 services RealUptime tracks plus its own internet-weather probes.

## See Also

- [healthchecks-mcp - Cron Job Health and Failure Forensics for Agents](/hermes/mcp/servers/external/healthchecks-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
