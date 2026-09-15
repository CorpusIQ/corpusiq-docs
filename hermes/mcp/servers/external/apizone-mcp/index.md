---
title: APIzone MCP - Live API Status and Uptime Monitoring for Agents
description: "Keyless remote MCP server from APIzone monitoring 294 popular third-party APIs (Stripe, OpenAI, AWS, GitHub, Twilio and more) with independent probes every ~5 minutes. Current status, batch dependency checks, 24h/7d/30d/90d uptime history and recent incident feeds, live-verified over JSON-RPC."
category: Business Operations
stars: 0
added: 2026-09-10
source: "chatmcp/mcpso issue #4035"
relevance: ★★★
tags: [uptime, monitoring, status-pages, outages, incident-response, remote-mcp, keyless]
---

# APIzone MCP - Live API Status and Uptime Monitoring for Agents

**Remote MCP server (Streamable HTTP, keyless)** - APIzone answers "is that API down right now?" from its own probe infrastructure, not scraped vendor status pages. It monitors 294 popular third-party APIs across 19 categories, re-probing every ~5 minutes, and exposes the full picture to agents: current status, batch dependency checks, uptime history over 24h/7d/30d/90d, and recent incident feeds. Live-verified during the Sep 10, 2026 sweep: an unauthenticated `initialize` and `tools/list` returned the full tool schema (server apizone 1.0.0, protocol 2024-11-05), and a live `get_api_status` call for Stripe returned "operational (last response 59ms)" with structured data.

```
Server type: Remote (Streamable HTTP, stateless)
Auth: None - public endpoint, no API key, no sign-up
Endpoint: https://apizone.io/api/mcp
Server: apizone 1.0.0, protocol 2024-11-05 (probe Sep 10, 2026)
Coverage: 294 popular APIs in 19 categories, probed from APIzone's own infrastructure every ~5 minutes
Registry: io.github.HappyMealSteak/apizone namespace (per the mcp.so submission)
Tools: 5, all read-only and idempotent
Built by: APIzone (apizone.io); no public repository found
```

## Why This Matters for Operators

"Is it us or is it them" is the most expensive question in incident response, and most operator stacks depend on a chain of third-party APIs - payments, AI, cloud, email, auth. APIzone lets an agent check the whole chain in one batch call (`check_apis` accepts up to 25 APIs) and tell which dependency is the culprit before the team opens a war room. Every answer carries the current status, the last measured latency, the last-check timestamp, and a link to the per-API status page, so the agent can cite measurements instead of guessing. Because probes run from APIzone's own infrastructure every ~5 minutes, the data is independent of vendor status pages - which often lag or stay green during partial outages.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_apis` | List all monitored APIs and their current status, optionally filtered by one of 19 categories (payments, ai, cloud, communication, email, auth, analytics, commerce, finance, shipping, and more) |
| `get_api_status` | Current status (operational/degraded/down/unknown) for one API by name or slug, with last measured latency and last-check time |
| `check_apis` | Batch-check up to 25 APIs in a single call - diagnose which dependency is failing in a multi-service stack |
| `get_api_uptime` | Uptime percentage plus median and p95 latency for one API over the last 24 hours, 7 days, 30 days, and 90 days |
| `list_recent_incidents` | Recent outages and degradations detected by APIzone, newest first, optionally filtered by category |

All five tools are read-only, idempotent, and non-destructive - safe to hand to any agent.

## Installation

```bash
claude mcp add apizone https://apizone.io/api/mcp
```

No key, no sign-up, no headers. The endpoint is stateless Streamable HTTP, so it works in Claude Desktop, Claude Code, Cursor, or any MCP client that speaks the HTTP transport. Human-readable status pages for every tracked API live at apizone.io/status/<slug> (for example apizone.io/status/stripe).

## Configuration

```json
{
  "mcpServers": {
    "apizone": {
      "type": "http",
      "url": "https://apizone.io/api/mcp"
    }
  }
}
```

No authentication block is needed. The server negotiates protocol version 2024-11-05 and advertises `listChanged: true`, so client tool registries refresh when the monitored set changes.

## Business Relevance

- **SRE and ops teams** get "is it us or them" answers with measurement citations before paging anyone.
- **Support teams** check third-party service status while triaging customer tickets instead of opening vendor status pages manually.
- **E-commerce and fintech operators** monitor payment and shipping dependencies (Stripe, Twilio, carrier APIs) that directly gate revenue.
- **Builders** get a free, credential-less dependency-health surface for every tool their stack depends on - useful inside agents, alert workflows, and pre-flight deployment checks.

## Integration with CorpusIQ

APIzone tells the agent whether a dependent service is down; CorpusIQ tells it whether the business felt it. A composed workflow: the agent checks APIzone status and incident feeds for Stripe, OpenAI, or AWS, then pulls revenue, order, and traffic data from CorpusIQ's Stripe, Shopify, and GA4 connectors to quantify the business impact of an outage and feed the incident postmortem with hard numbers.

## Limitations

- Brand new listing (chatmcp/mcpso issue #4035, Sep 10, 2026). No public repository exists, so this guide relies on the vendor's documented surface and live JSON-RPC probes.
- Coverage is a curated set of 294 popular APIs; niche, internal, or long-tail endpoints are not tracked.
- Readings are independent probes and can differ from a vendor's official status page by design.
- Uptime history windows cap at 90 days.

## See Also

- [RealUptime MCP - Uptime, Status and Outage Intelligence for Agents](/docs/hermes/mcp/servers/external/realuptime-mcp)
- [healthchecks-mcp - Cron Job Health and Failure Forensics for Agents](/docs/hermes/mcp/servers/external/healthchecks-mcp)
- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
