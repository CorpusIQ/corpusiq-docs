---
title: "Charming MCP — Generate & Host Interactive Web Apps via AI Agents"
description: "Hosted MCP server that generates, hosts, and updates interactive web apps. Connect any MCP-compatible AI client, ask it to build an app, and get a live URL in seconds."
category: mcp
tags: [mcp, development, web-apps, hosted, ui-generation, charming, tambo-labs, hermes-agent]
github: https://github.com/tambo-labs/charming-mcp
stars: 9
verified: true
source: mcp.so
discovered: 2026-07-24
pricing: Free tier available · OAuth with Dynamic Client Registration
---

# Charming MCP — Generate & Host Interactive Web Apps via AI Agents

**Charming** is a hosted MCP server that generates, hosts, and updates interactive web apps. Connect it to any MCP-compatible AI client and ask it to build an app — you get back a live URL in seconds. OAuth with Dynamic Client Registration is automatic — clients that support it show a one-time consent screen.

Think of it as "Vercel for agents" — your AI can go from idea to deployed interactive web app without touching a CLI, managing hosting, or configuring DNS.

## What It Does

- **App generation**: AI agents describe an app and Charming builds + deploys it
- **Live hosting**: Every generated app gets a public URL immediately
- **Iterative updates**: Ask the agent to modify the app — Charming redeploys
- **OAuth-native**: No API keys to manage — Dynamic Client Registration handles auth
- **Interactive apps**: Full-stack web apps, not static pages

## Key Tools

| Tool | Description |
|------|-------------|
| `charming_create_app` | Generate and deploy a new interactive web app |
| `charming_update_app` | Modify and redeploy an existing app |
| `charming_list_apps` | List all apps created by this agent |
| `charming_delete_app` | Remove an app |
| `charming_get_app_url` | Get the live URL for an app |

## Quick Start

### 1. Add to MCP Client

```json
{
  "mcpServers": {
    "charming": {
      "url": "https://api.charming.mcp.so/mcp"
    }
  }
}
```

### 2. First App

Once connected, just ask your agent:
> "Build me a calculator app with a dark theme"
> "Create a markdown editor with live preview"
> "Make a poll/voting app for my team"

The agent calls `charming_create_app`, and Charming returns a live URL.

### 3. Iterate

> "Add a history panel to the calculator"
> "Change the theme to match our brand colors"

The agent calls `charming_update_app` with the existing app ID.

## Hermes Agent Integration

```yaml
# ~/.hermes/config.yaml
mcp_servers:
  charming:
    url: "https://api.charming.mcp.so/mcp"
```

First connection triggers OAuth consent in your browser — one-time only.

## Use Cases for Business Operators

1. **Rapid prototyping**: Describe a dashboard, CRM view, or data tool and get a working version in seconds
2. **Internal tools**: Build utility apps for your team without writing code — "make a PTO request form"
3. **Client demos**: Generate interactive demos during sales calls — "build a demo of what the analytics would look like"
4. **Landing pages**: Spin up event pages, waitlist forms, or micro-sites on demand
5. **A/B test variants**: Generate multiple page variants and iterate on winners

## Limitations

- **No custom domains (yet)**: Apps are served from Charming's domain
- **No backend persistence**: Apps are frontend-focused; persistent data requires external services
- **Early stage**: 9 GitHub stars as of July 2026 — feature set expanding
- **Hosted only**: No self-hosted option currently — apps live on Charming's infrastructure

## Example: Building a Dashboard

```
User: "Build me a sales dashboard with a bar chart showing monthly revenue"

Agent → charming_create_app({
  name: "Sales Dashboard",
  description: "Monthly revenue bar chart with filters",
  requirements: "Bar chart, dark theme, responsive, month filter"
})

Charming → { app_id: "abc123", url: "https://abc123.charming.app" }

User: "Add a line chart for customer growth and make the background white"

Agent → charming_update_app({
  app_id: "abc123",
  changes: "Add line chart overlay for customer growth, switch to light theme"
})

Charming → { url: "https://abc123.charming.app" }  // Updated live
```

## Category

**Development** — Charming bridges the gap between AI agent capabilities and deployed, interactive web applications. It's a "deploy target" for agents, similar to how Vercel is a deploy target for developers.

---

*Discovered via [mcp.so](https://mcp.so/servers/charming) on July 24, 2026. Verified listing. GitHub: [tambo-labs/charming-mcp](https://github.com/tambo-labs/charming-mcp). 9 stars.*
