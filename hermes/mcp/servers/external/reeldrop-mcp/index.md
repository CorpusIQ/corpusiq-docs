---
title: "ReelDrop MCP - Instagram Reel Scheduling and Analytics"
description: "Hosted MCP server that operates your own Instagram account: schedule reels from video links or file uploads, read real analytics, and manage comment-to-DM automations. OAuth browser sign-in, no API key. Verified live (anonymous initialize returns 401, OAuth-gated endpoint at mcp.reeldrop.io/mcp)."
category: Social Media Management
stars: "n/a (hosted)"
added: 2026-09-02
source: "mcpservers.org /all listing"
relevance: ★★
tags: [instagram, reels, scheduling, analytics, social-media, dm-automation]
---

# ReelDrop MCP - Instagram Reel Scheduling and Analytics

**Hosted Streamable HTTP MCP server** - operates your own Instagram account from an assistant: schedule reels from a video link or file, answer performance questions from real analytics, and manage comment-to-DM automations. OAuth browser sign-in replaces API keys entirely.

## Spec Block

| Field | Value |
|---|---|
| Server name | ReelDrop |
| Endpoint | https://mcp.reeldrop.io/mcp |
| Transport | Streamable HTTP, OAuth browser sign-in |
| Auth | OAuth with your ReelDrop account (no API key) |
| Directory | Glama connector io.reeldrop/reeldrop |
| Docs | https://www.reeldrop.io/features/mcp |
| Repo | none public |

## Why This Matters for Operators

Instagram operations for small brands live in one person's phone. ReelDrop's MCP surface moves scheduling, analytics questions and DM automations into the agent loop: paste a video link into chat, the assistant drafts captions, picks a slot from your own posting schedule and schedules the reel, then can report on last month's performance from real numbers.

## Tools & Capabilities

| Capability | Description |
|---|---|
| Reel scheduling | Upload a video (link, Google Drive share, or local file), draft captions, pick a slot from your posting schedule, schedule the reel |
| Analytics | Answer performance questions about your reels from real account analytics |
| DM automation | Attach comment-to-DM automations to scheduled posts |

Capability-level table from the vendor's feature documentation; the exact tool names are exposed after OAuth sign-in, and anonymous enumeration is refused (401 verified).

## Installation

Connect once from the app: open the "Connect your AI assistant" page in ReelDrop and copy the server URL. Claude Desktop adds it as a custom connector; Claude Code is one command:

```bash
claude mcp add --transport http reeldrop https://mcp.reeldrop.io/mcp
```

The first call opens a browser window for ReelDrop account sign-in. That is the whole setup: no API key to generate and nothing to paste except the URL.

## Configuration

None beyond the one-time OAuth approval. Works with Claude Desktop, Claude Code, Cursor, VS Code, Windsurf, Gemini CLI, ChatGPT and any MCP client.

## Business Relevance

Useful for: social media managers consolidating Instagram operations into an agent workflow, creators who want scheduling and analytics in one chat, and small marketing teams automating comment-to-DM engagement loops on reels.

## Integration with CorpusIQ

Complements CorpusIQ's analytics connectors: ReelDrop executes Instagram publishing and engagement automation while CorpusIQ supplies the cross-channel business metrics that frame the content strategy.

## Limitations

Instagram (reels) focus; no public repository or tool list; OAuth account access required. Analytics and scheduling operate on your own connected account, not competitor research.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Mysocial MCP - Your Real Social Media History as Agent Memory](/hermes/mcp/servers/external/mysocial-mcp)
- [PostMCP MCP - Social Publishing Pipelines for Agents](/hermes/mcp/servers/external/postmcp-mcp)
