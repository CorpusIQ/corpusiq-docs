---
title: "Taskade MCP - Official AI Workspace Connector"
description: "Official Taskade MCP server with 62 tools over workspaces, projects, tasks, AI agents, agent chat, webhooks, knowledge bases, templates, media and sharing. Hosted with OAuth 2.0 PKCE at taskade.com/mcp or run locally with npx from npm."
category: Productivity
stars: n/a (new listing)
added: 2026-09-11
source: "chatmcp/mcpso GitHub issue #4061"
relevance: ★★★
tags: [taskade, workspace, project-management, tasks, ai-agents, productivity, remote-mcp]
---

# Taskade MCP

**Official MCP server (Streamable HTTP with OAuth 2.0 PKCE, or local npm package)** - Taskade's first-party Workspace MCP. Sixty-two tools hand your AI client the workspace: create and triage tasks, manage projects, spin up and train AI agents, run automations across 100+ services, read knowledge bases, wire webhooks and share media, all against the same Taskade workspace your team already uses.

```
Server type: Remote hosted (OAuth 2.0 PKCE) + local npm package
Auth: OAuth 2.0 PKCE (hosted); TASKADE_API_KEY (local)
Endpoint: https://www.taskade.com/mcp
Tools: 62 (workspaces, projects, tasks, AI agents, chat, webhooks, knowledge bases, templates, media, sharing)
Pricing: Free workspace tier; some endpoints gated on paid plans
Category: Productivity
Built by: Taskade
```

## Tools

| Group | What the agent can call |
|---|---|
| Workspaces & projects | Create, read and manage workspaces, projects and folders |
| Tasks | Full task lifecycle - create, update, assign, due dates, status |
| AI agents | Create, train and deploy Taskade AI agents from the MCP client |
| Agent chat | Chat with Taskade agents and pull conversation context |
| Webhooks & automations | Wire webhooks and run multi-step automations |
| Knowledge bases | Read and query workspace knowledge bases |
| Templates, media & sharing | Template library, media handling and sharing controls |

## Connection

1. Hosted: open https://www.taskade.com/mcp and complete the OAuth 2.0 PKCE flow once (Claude, Cursor, Claude Code, Windsurf, Zed). An unauthenticated initialize returns 401 by design.
2. Local: `npx -y @taskade/mcp-server` with TASKADE_API_KEY set from your Taskade account. Full task-level writes live in the local package.
3. Registry identifier io.github.taskade/mcp-server; a Glama listing covers the same package.

## Verification (Sep 11, 2026 night sweep)

Hosted endpoint live-verified: anonymous initialize at https://www.taskade.com/mcp returns HTTP 401 Unauthorized, matching the documented OAuth 2.0 PKCE design (401-by-design liveness class). The npm package @taskade/mcp-server and repo taskade/mcp both resolve; the README documents the 62-tool surface and per-client quick starts. Submission reviewed from chatmcp/mcpso issue #4061 (official resubmission after prior PR #512 closed without merge).

## See Also

- [Taskfolk MCP - Project Management for Teams and AI Agents](/docs/hermes/mcp/servers/external/taskfolk-mcp)
- [ConnectMachine MCP - Digital Business Cards and Contact CRM for Agents](/docs/hermes/mcp/servers/external/connectmachine-mcp)
