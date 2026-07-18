---
title: "Nexly Analytics MCP — Integration Guide"
description: "Connect AI tools to Nexly product analytics via MCP. Read-only access to traffic, funnels, reports, and anomalies. OAuth 2.0. Streamable HTTP."
category: mcp
tags: [mcp-server, analytics, nexly, product-analytics, read-only]
last_updated: 2026-07-17
---

# Nexly Analytics MCP Server

**Provider:** Nexly (Official)
**Endpoint:** `https://api.nexly.to/mcp`
**Auth:** OAuth 2.0
**Transport:** Streamable HTTP
**Access:** Read-only
**Documentation:** [nexly.to/help/api/mcp](https://nexly.to/help/api/mcp)

## Overview

Nexly provides a hosted MCP server that lets AI tools like Claude, Cursor, and Codex securely read your Nexly analytics — traffic, reports, funnels, and property details — directly inside the chat or editor. There is nothing to install and no tokens to copy: you connect with OAuth and authorize access with your Nexly account.

Access is **read-only** — connected tools can query analytics but can never change anything in your account.

## What You Can Do

- **Query traffic analytics** — Ask AI assistants about visitor counts, page views, and traffic sources
- **Pull funnel data** — Get conversion rates and drop-off points for marketing funnels
- **Read reports** — Access saved reports and their data
- **Monitor anomalies** — Query anomaly detection results
- **AI-traffic insights** — Access AI-generated traffic insights
- **Property details** — Retrieve site/property configuration

## Use Cases for Business Operators

1. **"How's our traffic today?"** — Ask your AI assistant instead of logging into a dashboard.
2. **Funnel debugging** — "Where are users dropping off in the signup funnel this week?"
3. **Anomaly detection** — "Did anything unusual happen with our traffic yesterday?"
4. **Meeting prep** — Pull traffic stats, top pages, and conversion data into a pre-meeting briefing.
5. **Cross-tool analysis** — Combine Nexly analytics with Stripe revenue, Shopify orders, or HubSpot leads through multi-source MCP queries.

## Before You Connect

- A Nexly account ([sign up](https://app.nexly.to/sign-up))
- Access to a supported MCP client
- A modern browser for the OAuth flow

**Important:** The MCP server accepts OAuth connections only. Personal API tokens (`nxp_…`) are for the read API and do not work with MCP.

## Setup

### Option 1: Claude (Desktop or claude.ai)

1. Open Claude → **Settings** → **Connectors**
2. Click **Add** → **Add custom connector**
3. Fill in:
   - **Name:** Nexly
   - **URL:** `https://api.nexly.to/mcp`
   - Leave OAuth client fields empty
4. Click **Add**, then click **Connect**
5. In the browser popup, sign in to Nexly and review the read-only permissions
6. Click **Authorize**

### Option 2: Cursor

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "nexly": {
      "url": "https://api.nexly.to/mcp"
    }
  }
}
```

Then go to **Customize** → **MCPs** → click **Authenticate** on the Nexly server. Review the read-only permissions and click **Authorize**.

### Option 3: Codex

In the Codex app:
1. **Settings** → **Plugins** → **MCPs** tab
2. Click **Add server** → fill in:
   - **Name:** Nexly
   - **Type:** Streamable HTTP
   - **URL:** `https://api.nexly.to/mcp`
3. Click **Save** → authorize in browser when prompted

Or add to `~/.codex/config.toml`:

```toml
[mcp_servers.nexly]
url = "https://api.nexly.to/mcp"
```

Then run `codex mcp login nexly` to authorize.

### Option 4: Any MCP Client

Add the endpoint URL `https://api.nexly.to/mcp` to your MCP client's configuration. Nexly uses standard OAuth 2.0 with Streamable HTTP — supported by all major MCP clients.

## Security Model

- **OAuth 2.0** — Standard secure authentication
- **Read-only** — Connected tools can query analytics but never modify your account
- **No API tokens needed** — OAuth flow handles authentication without copying secrets
- **Revocable** — Disconnect from Nexly or your MCP client at any time

## Available Tools

Nexly exposes tools for:
- **Analytics** — Traffic, page views, sources, visitor data
- **Reports** — Saved reports and report data
- **Funnels** — Conversion funnels and drop-off analysis
- **Properties** — Site and property configuration
- **Anomalies** — Anomaly detection results
- **AI Insights** — AI-generated traffic insights

All tools are read-only and respect your Nexly plan's data access level.

## Limitations

- **Read-only** — No configuration changes, event creation, or property management via MCP
- **OAuth only** — API tokens (`nxp_…`) cannot be used for MCP connections
- **Plan-dependent** — Available data depends on your Nexly plan tier

## Comparison with Other Analytics MCP Servers

| Feature | Nexly MCP | Google Analytics (Community) |
|---------|-----------|------------------------------|
| **Auth** | OAuth 2.0 | Service account / API key |
| **Transport** | Streamable HTTP | Varies |
| **Hosting** | Cloud (managed) | Self-hosted |
| **Read-only** | Yes, enforced | Depends on implementation |
| **Setup complexity** | 2 minutes (OAuth) | Requires GCP project setup |
| **AI-traffic insights** | Yes (built-in) | No |

---

*← [Back to External MCP Catalog](/hermes/mcp/servers/external/) | [Competitor Tracker MCP Guide](/hermes/mcp/servers/external/competitor-tracker-mcp/) →*
