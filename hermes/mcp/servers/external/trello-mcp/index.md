---
title: "Trello MCP Server — Integration Guide"
description: "Official Atlassian Trello MCP server. Cloud-hosted bridge for AI tools to access Trello boards, lists, cards, and checklists. OAuth 2.0. Streamable HTTP."
category: mcp
tags: [mcp-server, trello, atlassian, project-management, official]
last_updated: 2026-07-17
---

# Trello MCP Server

**Provider:** Atlassian (Official)
**Endpoint:** `https://mcp.trello.com/v1`
**Auth:** OAuth 2.0
**Transport:** Streamable HTTP
**License:** Apache 2.0
**Status:** Available (Beta)
**Repository:** [github.com/atlassian/trello-mcp-server](https://github.com/atlassian/trello-mcp-server)

## Overview

The official Trello MCP server is a cloud-hosted bridge between your Trello account and any MCP-compatible AI assistant. Once connected, AI tools can read boards, lists, cards, and checklists — and take actions on your behalf based on the permissions you grant.

Atlassian now offers official MCP servers across their entire product suite: Jira, Confluence, and Trello. This makes MCP the standard integration layer for Atlassian's AI ecosystem.

## What You Can Do

- **Read boards, lists, cards** — Query Trello content from AI assistants
- **Create and update cards** — Manage tasks without switching apps
- **Manage checklists** — Add, update, and complete checklist items
- **Search across workspaces** — Find cards and boards by keyword
- **Archive (no delete)** — Cards and lists can be archived but not permanently deleted
- **Workspace-scoped access** — Each connection authorizes one workspace (multi-workspace planned)

## Use Cases for Business Operators

1. **Daily standup automation:** Ask your AI assistant "What's on my Trello board today?" and get a prioritized task list.
2. **Cross-tool workflows:** Connect Trello tasks to Slack alerts, email summaries, or GitHub issues through your AI agent.
3. **Project reporting:** Query Trello for project status, blocked cards, and upcoming deadlines — all from chat.
4. **Bulk operations:** Update multiple cards, reorder lists, or assign tasks without clicking through the Trello UI.

## Before You Connect

- A Trello account (any plan works — Free, Standard, Premium, or Enterprise)
- Access to a supported MCP client
- A modern browser for the OAuth authorization flow

## Setup

### Option 1: Claude (Desktop or claude.ai)

1. Open Claude → **Settings** → **Connectors**
2. Click **Add** → **Add custom connector**
3. Fill in:
   - **Name:** Trello
   - **URL:** `https://mcp.trello.com/v1`
4. Click **Add**, then click **Connect**
5. In the browser popup, choose your Trello workspace and review permissions
6. Click **Authorize**

Alternatively, install from the [Claude connector directory](https://claude.ai/directory/connectors/trello).

### Option 2: ChatGPT

Install directly from the [ChatGPT Trello listing](https://chatgpt.com/apps/trello/asdk_app_6a20b18a639081918c1b438f8381b27e).

### Option 3: Cursor

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "trello": {
      "url": "https://mcp.trello.com/v1"
    }
  }
}
```

Then go to **Customize** → **MCPs** → click **Authenticate** on the Trello server.

### Option 4: VS Code / GitHub Copilot

Add to your MCP configuration:

```json
{
  "mcpServers": {
    "trello": {
      "url": "https://mcp.trello.com/v1"
    }
  }
}
```

### Option 5: Gemini CLI

Refer to the [Gemini CLI MCP documentation](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md) and add the Trello endpoint.

## Security Model

- **OAuth 2.0** — Industry-standard authentication
- **Workspace-scoped** — AI tools only access the workspace you explicitly authorize
- **Permission-respecting** — All actions respect your existing Trello permissions; AI can't do anything you can't
- **No destructive deletes** — Cards and lists can be archived, never permanently deleted
- **Revocable** — Disconnect at any time from Trello or your AI client settings

## Limitations

- **Single workspace per connection** — Each MCP connection supports one Trello workspace. Multi-workspace is planned.
- **No permanent delete** — Archive-only for safety. Manual deletion still available in Trello directly.
- **Beta status** — The server is marked as beta; API surface may change.

## Comparison with Atlassian Jira/Confluence MCP

| Feature | Trello MCP | Atlassian MCP (Jira/Confluence) |
|---------|-----------|-------------------------------|
| **Focus** | Lightweight task management | Engineering + documentation |
| **Auth** | OAuth 2.0 | OAuth 2.0 |
| **Transport** | Streamable HTTP | Streamable HTTP |
| **Hosting** | Atlassian Cloud | Atlassian Cloud |
| **Primary audience** | Operators, marketers, teams | Engineers, product managers |
| **Multi-workspace** | Planned | Multi-project supported |

## FAQ

**Q: Does Trello MCP cost extra?**
A: No. It's included with any Trello plan, including Free.

**Q: Can I use this with multiple Trello workspaces?**
A: Currently, each MCP connection supports one workspace. Multi-workspace support is planned.

**Q: What happens if I disconnect?**
A: The AI assistant loses access immediately. Reconnect to restore — no data is lost.

**Q: Can the AI permanently delete my Trello cards?**
A: No. Destructive delete operations are not supported. The AI can archive cards and lists but cannot permanently delete them.

---

*← [Back to External MCP Catalog](/hermes/mcp/servers/external/) | [Atlassian MCP Guide](/hermes/mcp/servers/external/atlassian-mcp-server/) →*
