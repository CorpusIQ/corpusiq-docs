---
title: "Coderbuds MCP - Engineering Delivery Metrics for Agents"
description: "Remote MCP server that gives coding agents facts about how a team ships. Shipping standards, org map, review turnaround, queue blockers and deploy lag, plus 22 tools to act on them, scoped to the authenticated user's teams and limits."
category: Developer Tools
stars: n/a (new listing)
added: 2026-09-11
source: chatmcp/mcpso issues
relevance: ★★
tags: [engineering-analytics, delivery-metrics, developer-tools, oauth, remote-mcp]
---

# Coderbuds MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1)** - connects coding agents to Coderbuds, the delivery-intelligence layer for engineering teams. Instead of guessing at how a team ships, the agent can pull the team's size and scope standards, review turnaround, queue blockers and deploy lag - then act on them: assess a change before review, request reviews through the team's Slack, and record decisions.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 with browser authorization; bearer tokens accepted as a fallback for headless environments
Endpoint: https://coderbuds.com/mcp/insights
Tools: 22, grouped by delivery loop stage
Prompt: "Work Our Way" - primes a session with the team's standards, shipping norms and review-queue state
Category: Developer Tools
Built by: Coderbuds (registry namespace com.coderbuds/insights)
```

## Tools

The vendor documents 22 tools grouped by where they land in the delivery loop. Named examples from the docs:

| Tool | Purpose |
|---|---|
| assess-change-fit | Check whether a proposed change fits how the team ships, before a pull request is opened |
| get-team-context | Load the team's standards, shipping norms and org map at session start |
| record-change-fit-decision | Record the outcome when a change-fit assessment is acted on |
| report-ai-usage | Report agent usage back to the team's analytics |

Questions the docs suggest asking: what is blocking my pull requests right now, what has been merged but not shipped to production, ask the team for a review on a PR, why a PR was flagged poor, and whether a repo is ready for agents to work in.

## Connection

1. Add the endpoint from your agent. Claude Code - `claude mcp add --scope user --transport http coderbuds https://coderbuds.com/mcp/insights` (omitting the scope gives a local install). Codex - `codex mcp add coderbuds --url https://coderbuds.com/mcp/insights` then `codex mcp login coderbuds`. Cursor and other clients accept a `.mcp.json` entry with the same URL.
2. Authorize in the browser on first connect; the token renews in the background (30-day lifetime, re-authorization only after a year of no use).
3. Load the "Work Our Way" prompt at the start of a session, then ask in plain language - the agent picks the tool.

Scope and privacy notes from the vendor: everything is scoped to the authenticated user and their teams; personal insights are visible only to their owner; source code is never sent to Coderbuds, the tools answer from data Coderbuds already holds. Acting tools are deliberately narrow - deploys only run where the team has already configured a hook or workflow, posture changes are restricted to team admins, and review requests go to the team's own Slack channel. Access is revocable per machine from the API Tokens page.

## Verification (Sep 11, 2026 midday sweep)

Endpoint live-probed over JSON-RPC: anonymous initialize returned HTTP 401 with `"Not authenticated yet. Your MCP client should now open a browser so you can sign in to Coderbuds and click Authorize."` - live and OAuth-gated, with the remediation message quoted from the server itself. The listing carries an Official MCP Registry namespace (com.coderbuds/insights) and a Glama connector, and was submitted by the vendor via chatmcp/mcpso issue #4067.

## See Also

- [GitLab MCP - CorpusIQ Docs](/hermes/mcp/servers/external/gitlab-mcp)
- [Spike MCP - Incident Management and On-Call for AI Assistants](/hermes/mcp/servers/external/spike-mcp)
