---
title: Agent Watch MCP - Endpoint Monitoring for the Agent Economy
description: Continuous liveness, latency, schema-drift and price-integrity monitoring for MCP endpoints, with a free tier for 5 endpoints and a public census of registry liveness.
category: DevOps
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★
tags: [mcp-monitoring, uptime, latency-tracking, schema-drift, endpoint-health, observability, ai-operations, remote-mcp]
---

# Agent Watch MCP

**Remote MCP server (Streamable HTTP)** - continuous monitoring for the endpoints your agents depend on: liveness, latency, schema drift, auth posture and price integrity for MCP and paid agent services. Free tier covers 5 endpoints, and a free probe API checks any endpoint before you pay.

```
Server type: Remote (Streamable HTTP)
Auth: watchlist tied to checkout email; probe is open
Endpoint: https://agent-watch-api-production.up.railway.app/mcp/
Tools: watchlist and probe operations for MCP endpoint health
Pricing: Free 5 endpoints; Builder $19/mo (50); Team $99/mo (500 + API + alerts); Data API metered
Category: DevOps
Built by: entradox (sibling of Perimeter Watch and AgentLedger)
```

## Why This Matters for Operators

Every production agent now leans on third-party MCP endpoints, and those endpoints fail silently: the vendor's own census found roughly two-thirds of registry-declared MCP endpoints do not answer, and an arXiv census found 47.9% of advertised x402 paid hosts dead. **Agent Watch is the monitoring layer that directory listings never had** - when an endpoint your agents pay for goes dark, drifts its schema, or starts charging differently than advertised, you get an alert instead of a failed workflow.

For buyers of agent services, the free probe is the due-diligence step before committing: POST any endpoint URL and get a liveness answer in seconds.

## Tools & Capabilities

| Capability | What it checks |
|---|---|
| Liveness | MCP handshake + tool list |
| Latency | p50/p95 response time |
| Schema drift | Tool-list hash changes between probes |
| Auth posture | RFC 9728 metadata presence |
| Price integrity | 402 challenge vs advertised price (Phase 1) |

REST equivalents are documented: POST /v1/probe for free checks and POST /v1/watch to add endpoints.

## Installation

```bash
claude mcp add agent-watch --transport http https://agent-watch-api-production.up.railway.app/mcp/
```

## Configuration

```json
{
  "mcpServers": {
    "agent-watch": {
      "type": "http",
      "url": "https://agent-watch-api-production.up.railway.app/mcp/"
    }
  }
}
```

Watchlist endpoints are tied to the email from checkout; the probe endpoint works without auth.

## Business Relevance

- **Operators running agent fleets** get one dashboard for every MCP endpoint in the stack instead of discovering failures from users.
- **Teams buying paid agent services** verify liveness and price integrity before signing up, and keep verifying after.
- **Platform builders** get the metered Data API to fold endpoint health into their own routers and marketplaces.
- **Security leads** see schema drift - an unexpected tool-list change is an early signal of a compromised or silently-updated endpoint.

## Integration with CorpusIQ

Agent Watch monitors the plumbing CorpusIQ runs on: as CorpusIQ's connector ecosystem grows, operators can watchlist the MCP endpoints behind critical automations and surface alerts next to CorpusIQ's own health dashboards. A composed workflow: CorpusIQ flags a connector error mid-workflow, Agent Watch confirms whether the underlying endpoint was alive at that moment - separating vendor outages from configuration bugs in one look.

## Limitations

- Brand new - no track record yet; early-stage pricing and endpoint on a railway.app host.
- Free tier caps at 5 endpoints; real fleets need Builder or Team.
- Price-integrity monitoring is labeled Phase 1 - expect coverage gaps.
- No published self-host option; monitoring data lives on the vendor's endpoint.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
