---
title: BioFlow MCP - Content, Analytics and Publishing for Agents
description: "OAuth remote MCP server with 13 scoped tools for reading pages, analytics, contacts and files, drafting, and publishing with two-step confirmation."
category: Marketing
stars: n/a (hosted service, getbioflow.com)
added: 2026-10-01
source: "mcpservers.org /all (getbioflow-com-mcp)"
relevance: ★★
tags: [marketing, content, bio-pages, analytics, publishing, oauth, remote-mcp]
---

# BioFlow MCP

**A link-in-bio and content page an agent can read, draft and publish.** BioFlow exposes its pages, analytics, contacts and files over MCP with 13 tools, each guarded by a single OAuth scope. An agent can read performance, draft edits and publish - but publishing is off by default and every publish is a two-step confirm.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1, per-tool scopes, tokens scoped to one workspace
Endpoint: https://app.getbioflow.com/api/mcp
Tools: 13 (read pages, analytics, contacts, files; create and edit drafts; publish)
Pricing: requires a BioFlow account
Category: Marketing
Built by: BioFlow
```

## Why This Matters for Operators

An agent with write access to a live page is a liability unless the platform designs against surprise. BioFlow does: tokens are scoped to one workspace so an agent only sees what it was connected to; publish-class tools are disabled per workspace until an explicit settings toggle is flipped; and even then a publish is two calls, the first returning only a preview. Draft writes are guarded by optimistic concurrency, so a stale edit is refused rather than clobbering newer work, and writes take an idempotency key so a retry cannot run twice.

For an operator running a bio page or content hub, that means the agent can do the reading and the drafting and the measuring, while the moment something goes live stays a deliberate, confirmed step. Denials are typed and actionable - a missing scope, a disabled dangerous operation with a deep link to the setting, a plan limit, a stale draft - so the agent can tell the person what to change instead of failing silently.

## Tools & Capabilities

| Capability | Purpose |
|---|---|
| Page reads | Read the workspace's pages |
| Analytics | Read page and link performance |
| Contacts | Read captured contacts |
| Files | Read workspace files |
| Draft edits | Create and edit drafts, blocks and page metadata |
| Publishing | Publish, behind a per-workspace toggle and a two-step confirm |

Thirteen tools total, one scope each. The vendor publishes the count and scope model on the connecting-assistants page.

## Installation

```
claude mcp add --transport http bioflow https://app.getbioflow.com/api/mcp
```

Works with Claude (web, desktop, as a custom connector), ChatGPT, Copilot, MCP Inspector and any client supporting remote MCP with OAuth discovery.

## Configuration

```json
{
  "mcpServers": {
    "bioflow": {
      "type": "http",
      "url": "https://app.getbioflow.com/api/mcp"
    }
  }
}
```

## Business Relevance

- **Growth and content teams** can have an agent read performance, draft copy edits and stage a publish without handing over unattended write access.
- **Solopreneurs and creators** can keep a bio page current through the agent they already use, with analytics read in the same breath.
- **Marketing ops** get a concrete consent and revocation model: every connection starts on a scope-listing consent screen, any app can be revoked, and the same screen shows a full audit trail of every tool call.
- **AI agents** get a publishing surface designed for them, with typed denials and optimistic concurrency rather than silent overwrites.

## Integration with CorpusIQ

CorpusIQ supplies the business and audience data; BioFlow supplies the destination page and its performance. An agent can read which campaigns are driving traffic from CorpusIQ's connectors, check the landing page's analytics through BioFlow, and draft the change that closes the gap - measurement and content update composed in one workflow, with the publish gated on confirmation.

## Limitations

- Requires a BioFlow account; tokens are scoped to a single workspace.
- Publishing is off by default per workspace and every publish is a two-step confirm, so it is not an unattended publish path.
- Focused on bio pages and content hubs, not a full CMS.
- Thirteen tools with one scope each means narrow, composable access rather than a broad API surface.

## FAQ

### What does the BioFlow MCP server do?

It gives an AI agent 13 scoped tools to read pages, analytics, contacts and files, draft content, and publish - with publishing off by default and confirmed in two steps.

### Can an agent publish without confirmation?

No. Publish-class tools are disabled per workspace until a setting is flipped, and every publish is a two-step confirm where the first call returns only a preview.

### How is access controlled?

OAuth 2.1 with per-tool scopes, tokens scoped to one workspace, a plain-language consent screen and a revocable connection with a full audit trail of tool calls.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ](https://corpusiq.io) - 40+ business data connectors for AI agents
