---
title: "Adviserry MCP - Newsletter Search and Drafted Actions"
description: "Adviserry exposes 13 MCP tools over your newsletter knowledge base: panel search, upload context search, insight readback and drafted actions."
category: Research
stars: n/a (no public repo)
added: 2026-09-30
source: "mcpservers.org server page (adviserry.com)"
relevance: ★★
tags: [research, newsletters, knowledge-base, bearer-token, read-write, sso-free, remote-mcp]
---

# Adviserry MCP

**Your newsletter reading, turned into searchable context and finished drafts.** Adviserry collects the newsletters and YouTube channels you follow into topic panels, then synthesizes concrete actions from them. Its MCP server puts both layers in front of an assistant: raw source search, the observations Adviserry generated, and the drafted deliverables themselves.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer token from Settings, MCP Server Access (no OAuth 2.1, so ChatGPT custom connectors are not supported yet)
Endpoint: https://adviserry.com/api/mcp
Tools: 13
Rate limit: 500 tool calls per rolling hour, per user
Category: Research
Built by: adviserry.com
```

## What it exposes

The server publishes thirteen tools. Source search: `search_newsletters` (query, optional panel filter, limit up to 10) and `search_context` for PDFs, Word docs, spreadsheets, presentations and web pages you uploaded as context. Panel and issue reads: `list_panels`, `get_recent_issues` (days up to 30), `get_newsletter_summary` and `get_topics`.

Synthesis reads: `get_insights` returns the AI-generated connections, trends and action items across sources, filterable by unread, read, saved or all. The action layer is where it differs from a search tool: `search_actions` finds drafted deliverables by topic against each action's title, its "why now" rationale and the full draft, filterable by panel, by domain (project, investment, personal, learning), by effort (quick, medium, deep) and by status; `get_actions` lists the current batch newest-first; `get_action` returns one in full with every source it was built from, author and date included. `update_action_status` marks an action shipped, read, dismissed or back to unread, and shipped actions teach future synthesis.

Context writes: `get_user_context` returns the advisor profile (role, current projects, challenges, goals, freeform notes) and `update_context` changes it. Updates default to append because the profile spans more than one project; anything that would remove existing text returns a preview and saves nothing until you pass back the confirm token.

## Connecting

Copy your MCP token from Settings, MCP Server Access, then add the server to your client config with the endpoint and a bearer header. Claude Desktop, Claude Code, Cursor, Gemini CLI and OpenClaw are supported over the same HTTP endpoint. Two setup details matter: the endpoint must be the bare host `adviserry.com` because the `www.` host returns a 308 redirect most MCP clients will not follow, and the mobile app asks for your Adviserry user ID in a second field, which is not a credential, since requests are authenticated by the bearer token alone.

## Notes

The rate limit returns HTTP 200 with a JSON-RPC error inside the body (code -32000) rather than a 429, so a client that only inspects status codes will miss it. Regenerating a token invalidates the old one immediately, and clients read their config once at launch, so replace the token and fully restart the client rather than reloading. ChatGPT is not supported because its custom connectors require OAuth 2.1 with dynamic client registration.

## See Also

- [Research and knowledge MCP servers](/hermes/mcp/servers/external/)
- [Content research MCP servers](/hermes/mcp/servers/external/)
