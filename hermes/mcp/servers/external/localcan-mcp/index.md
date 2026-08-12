---
title: "LocalCan MCP — Public URLs & Traffic Inspection for Localhost"
description: "Give AI agents public URLs (tunnels) for localhost, live HTTP traffic inspection, snapshot publishing, and access control. ngrok alternative for Mac, Windows, Linux."
date: 2026-08-12
source: mcp.so
source_url: https://mcp.so/servers/localcan
category: Developer Tools
rating: ★
status: active
---

# LocalCan MCP Server

## What is LocalCan?

LocalCan gives AI agents public URLs (tunnels) for localhost, live HTTP traffic inspection, snapshot publishing, and access control. Part of LocalCan, the ngrok alternative for Mac, Windows and Linux. Free plan available.

**Category:** Developer Tools  
**Author:** LocalCan  
**Added:** August 12, 2026

## Why It Matters for Operators

While primarily a developer tool, LocalCan has operational use cases for business operators:
- **Demo sharing**: Expose a local development/staging site with a public URL for client demos
- **Webhook testing**: Inspect incoming webhooks from Stripe, Shopify, etc. during integration testing
- **Temporary landing pages**: Publish a quick prototype without deploying to production

## Connection Details

```json
{
  "mcpServers": {
    "localcan": {
      "type": "streamable-http",
      "url": "https://mcp.localcan.com"
    }
  }
}
```

**Transport:** Streamable HTTP (remote)  
**Auth:** LocalCan account (free tier available)  
**Pricing:** Free plan → paid tiers for custom domains, team features

## Key Tools

| Tool | Description |
|------|-------------|
| `create_tunnel` | Create a public URL tunnel to localhost |
| `inspect_traffic` | Live HTTP traffic inspection |
| `publish_snapshot` | Publish a static snapshot of current state |
| `manage_access` | Access control for tunnels |

## CorpusIQ Integration Opportunity

**Priority: LOW.** Useful for development workflows (demoing features, testing webhooks) but not a core operational tool for business operators. The Hermes stack already has equivalent capabilities through Cloudflare Tunnels.

## Verdict

**★★☆☆☆ Solid ngrok alternative.** For operators who regularly demo local work or test integrations, LocalCan provides an MCP-native tunnel experience. However, it's a utility, not a business-growth tool.

## Resources

- **Homepage:** https://localcan.com/
- **Repository:** https://github.com/LocalCan/localcan-mcp
- **mcp.so:** https://mcp.so/servers/localcan
