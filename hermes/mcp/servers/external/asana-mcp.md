---
title: "Asana MCP V2 — Project Management for AI Agents"
description: "Official Asana MCP V2 server connecting AI agents to tasks, projects, and workspaces via OAuth 2.0. Hosted at mcp.asana.com/v2/mcp. Requires pre-registered OAuth app credentials."
category: mcp
tags: [mcp-server, project-management, asana, official, productivity, team-operations]
last_updated: 2026-07-17
---

# Asana MCP Server V2 ★ Official — New July 17

Asana's official MCP V2 server connects AI agents to your Asana workspace — tasks, projects, workspaces, and team coordination — through OAuth 2.0 authentication. The hosted server at `https://mcp.asana.com/v2/mcp` requires pre-registration in the Asana Developer Console.

This launch puts Asana alongside Atlassian (Jira/Confluence), Linear, and Notion as major productivity platforms with official MCP servers — making project management accessible to AI agents across the ecosystem.

**Source:** mcp.so (discovered July 17, 2026)
**Category:** Productivity / Project Management / Team Operations
**Author:** Asana (Official)
**Docs:** https://developers.asana.com/docs/connecting-mcp-clients-to-asanas-v2-server
**Endpoint:** https://mcp.asana.com/v2/mcp
**MCP Tools Reference:** https://developers.asana.com/docs/mcp-tools-reference
**Status:** Production (V2)

## What It Does

- **Tasks** — create, read, update, and search tasks across projects
- **Projects** — list projects, view project details, manage project structure
- **Workspaces** — access workspace-level information and organization
- **Rich interaction** — comments, assignments, due dates, custom fields, and attachments

## Setup

### Prerequisites

1. **Create an Asana MCP app** in the [Asana Developer Console](https://developers.asana.com/docs/integrating-with-asanas-mcp-server)
2. Save your `client_id` and `client_secret`
3. Configure OAuth redirect URL based on your client:
   - Claude Code: `http://localhost:8080/callback`
   - Cursor: `cursor://anysphere.cursor-mcp/oauth/callback`
   - VS Code: `http://127.0.0.1:33418/` or `https://vscode.dev/redirect`
   - Windsurf/Kiro/Codex: `http://localhost:3334/oauth/callback`
4. Install Node.js and npm

### Claude Code (Native OAuth Support)

Claude Code has native support for pre-configured OAuth — no third-party tools needed:

```bash
claude mcp add --transport http \
  --client-id YOUR_CLIENT_ID \
  --client-secret \
  --callback-port 8080 \
  asana https://mcp.asana.com/v2/mcp
```

Claude Code will prompt for your client secret (hidden input) and open a browser for Asana OAuth authorization.

### Other Clients (via mcp-remote)

For Cursor, VS Code, Windsurf, Kiro, and Codex, use the `mcp-remote` npm package:

```bash
npx mcp-remote https://mcp.asana.com/v2/mcp \
  --client-id YOUR_CLIENT_ID \
  --client-secret YOUR_CLIENT_SECRET \
  --redirect-uri http://localhost:3334/oauth/callback
```

**⚠️ Note:** `mcp-remote` is experimental community software. Asana does not provide support for it. Claude Code is recommended for production use.

### Environment Variables

```bash
export ASANA_CLIENT_ID="YOUR_CLIENT_ID"
export ASANA_CLIENT_SECRET="YOUR_CLIENT_SECRET"
```

### Verification

After setup, test the connection:

```
Show me my Asana tasks due this week
```

Claude (or your MCP client) should fetch your Asana tasks using the MCP tools.

## Business Relevance

1. **Project management without context switching:** Operators can manage Asana tasks, check project status, and update assignments directly from their AI workspace — no tab switching.

2. **Team coordination at scale:** AI agents can surface overdue tasks, identify blocked work, and generate status reports across multiple projects simultaneously.

3. **Workflow automation:** Combine Asana MCP with other MCP servers (GitHub, Slack, Google Calendar) to create cross-platform workflows — e.g., "create an Asana task for every GitHub issue labeled 'bug'."

4. **Enterprise PM suite:** Asana joins Atlassian (Jira/Confluence), Linear, and Notion in the MCP ecosystem. Teams can now choose their PM tool without losing AI agent integration.

## Use Cases for Business Operators

- **Daily standup prep:** "What tasks are due today across all my projects?"
- **Blocker detection:** "Find all tasks that have been in 'In Progress' for more than 5 days."
- **Status reports:** "Generate a status update for the Q3 launch project."
- **Task triage:** "Create tasks for the 3 action items from yesterday's meeting notes."
- **Cross-project visibility:** "Show me all high-priority tasks assigned to the engineering team this sprint."
- **Deadline tracking:** "Which projects have milestones due in the next 2 weeks?"

## Security Best Practices

- Use unique credentials per developer — don't share client IDs/secrets
- Rotate credentials regularly
- Never commit credentials to version control
- For production, use a secrets manager (HashiCorp Vault, AWS Secrets Manager, 1Password CLI)
- Monitor which MCP clients have OAuth access via Asana's app management console

## Limitations

- **OAuth pre-registration required:** Unlike simpler MCP servers, Asana V2 requires app registration before use
- **Third-party dependency for some clients:** Cursor/VS Code users need `mcp-remote` (experimental)
- **No unauthenticated access:** All MCP operations require valid OAuth tokens

## See Also

- [Mercury MCP](/hermes/mcp/servers/external/mercury-mcp/) — banking MCP
- [Atlassian MCP](/hermes/mcp/servers/external/) — Jira/Confluence MCP
- [External MCP Catalog](/hermes/mcp/servers/external/)
