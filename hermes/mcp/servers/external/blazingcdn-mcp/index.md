---
title: "BlazingCDN MCP - CorpusIQ Docs"
description: CDN operations for AI agents. Purge cache, query bandwidth metrics, manage domains, Cloud Storage and Video CDN across the BlazingCDN Anycast network from Claude, Cursor or Windsurf.
category: DevOps
stars: n/a (new listing)
added: 2026-08-14
source: mcp.so
relevance: ★★
tags: [cdn, content-delivery, cache-purging, video-cdn, cloud-storage, bandwidth-metrics, infrastructure, self-hosted]
---

# BlazingCDN MCP

**Self-hosted MCP server (npx, API token)** — the official BlazingCDN connector for AI agents. Manage CDN resources, purge cache, query metrics, domains, Anycast CDN, Video CDN, and Media CDN from Claude, Cursor, or Windsurf. 52 tools talking directly to the BlazingCDN API, with writes gated behind an explicit env flag.

```
Server type: Self-hosted (stdio via npx, HTTP transport option)
Auth: API token (BLAZINGCDN_API_TOKEN)
Repo: https://github.com/BlazingCDN/BlazingCDN-MCP (MIT)
Tools: 52 — Anycast CDN, cache operations, metrics, custom domains, Cloud Storage, Video CDN
Pricing: BlazingCDN account (usage-based CDN pricing)
Category: DevOps / Infrastructure
Built by: BlazingCDN (blazingcdn.com)
```

## Why This Matters for Operators

CDN consoles are click-heavy and incident-hostile: a cache purge during a broken deploy is the worst time to hunt through dashboards. BlazingCDN MCP moves those operations into the assistant that deploys the site or publishes the video.

**Operators get CDN control in the same conversation as the release** — purge by path, read bandwidth by day, add domains, and manage Video CDN without leaving the agent loop. The `BLAZINGCDN_ALLOW_WRITE` gate means a read-only agent can be fielded safely and write access granted per agent.

## Tools & Capabilities

| Area | Purpose |
|---|---|
| Anycast CDN | Manage CDN resources and zones |
| Cache operations | Purge paths and resources on demand |
| Metrics | Bandwidth and traffic queries, day-level breakdowns |
| Custom domains | Add and manage domain mappings |
| Cloud Storage | Storage resource operations |
| Video CDN / Media CDN | Video delivery resources and settings |

## Installation

```bash
claude mcp add blazingcdn --env BLAZINGCDN_API_TOKEN=your-token -- npx -y @blazingcdn/mcp
```

The README includes an HTTP-transport config (`--transport http --port 8462`) for clients that prefer a local endpoint.

## Configuration

```json
{
  "mcpServers": {
    "BlazingCDN-MCP": {
      "command": "npx",
      "args": ["-y", "@blazingcdn/mcp", "--transport", "http", "--port", "8462"],
      "env": {
        "BLAZINGCDN_API_TOKEN": "your-token",
        "BLAZINGCDN_ALLOW_WRITE": "1"
      }
    }
  }
}
```

Omit `BLAZINGCDN_ALLOW_WRITE` (or set it to 0) for a read-only agent.

## Business Relevance

- **Site owners and ecommerce operators** purge stale cache during releases and pull bandwidth reports in the release conversation
- **Video-heavy content teams** manage Video CDN resources alongside publishing workflows
- **DevOps operators** fold CDN checks and purges into deploy and incident runbooks

## Integration with CorpusIQ

BlazingCDN MCP complements CorpusIQ analytics connectors on the delivery layer. An agent watching GA4 sessions or Stripe checkout events can, in the same conversation, check BlazingCDN bandwidth by day and purge a bad asset — incident response without console hopping. For ecommerce operators on Shopify or SHOPLINE, cache purges after catalog updates and bandwidth reads during campaign spikes become agent-native steps in the operations loop.

## Limitations

- Brand new listing — submitted hours before this sweep; no track record yet
- Requires a BlazingCDN account (usage-based CDN pricing applies)
- Self-hosted npx model, not a hosted remote endpoint
- API-token auth only; no OAuth
- Write tools require an explicit env flag — a feature, but easy to misconfigure

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
