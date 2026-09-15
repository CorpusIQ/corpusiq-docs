---
title: PostBazooka MCP - Social Publishing with Commit Proof
description: Remote OAuth MCP server for social publishing across eight networks. A workflow-gated 26-tool schema covers sourced ideas, drafts, media, reactions, feedback and scheduling, with structured commit confirmation on every mutation so agents can verify a post actually persisted before reporting success.
category: Social Media Management
stars: n/a (new listing)
added: 2026-09-05
source: mcpservers.org
relevance: ★★★
tags: [social-media, publishing, scheduling, content-ops, oauth, remote-mcp, approvals]
---

# PostBazooka MCP

**Remote MCP server (OAuth)** - a text/data and action interface for sourced social ideas, team feedback, scheduling and publishing approved posts across eight networks. Agents research, create, edit, analyze, react, comment, schedule and publish conversationally, with structured commit proof on every mutation.

```
Server type: Remote (OAuth)
Auth: OAuth (connect your agent to postbazooka.com/mcp)
Endpoint: https://postbazooka.com/mcp
Tools: 26 (workflow-gated schema; core tools named below)
Pricing: Free plan plus paid plans (limits surfaced inside tool results)
Category: Social Media Management
Built by: PostBazooka
```

## Why This Matters for Operators

The classic failure mode of agent-driven social publishing is the silent miss: the agent drafts a post, claims success, and nothing went out. PostBazooka removes the ambiguity with an explicit commit protocol. A mutation is complete only when the direct tool result carries the matching operation name and requestId, `operationCommitted: true`, and the text `POSTBAZOOKA COMMIT CONFIRMED`. Anything else means the change did not run, and the agent must say so.

Publishing is decision-based per destination: each network connection can be automatic, scheduled, or held, and `publish_post_now` is a separate explicit action that creates immutable Publication snapshots. Human reactions and comments become feedback for later agent review, while agent actions never create feedback loops.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `get_workflow` | Mandatory first call; returns the complete current workflow plus an opaque workflowVersion that every later call must carry |
| `create_ideas` | Persist sourced social ideas; research and drafts are intermediate until ideas commit |
| `create_posts` | Create posts with media attachments, with provenance rules enforced on media |
| `edit_post` | Revise an existing post, including media replacement |
| `set_post_publishing` | Per-destination publishing decisions: automatic, scheduled or held |
| `set_connection_schedule` | Schedule reads for upcoming and past publishing |
| `publish_post_now` | Immediate publishing, creating immutable Publication snapshots |
| Reaction and feedback tools | Likes and dislikes are feedback signals; automatic publishing uses reaction scores, explicit schedules are never silently cancelled |
| Media tools | Pass library media, generated image data, or licensed public media with source, license and attribution evidence |

The schema is workflow-gated: if a workflow names a tool the connected client does not have, the agent refreshes the connection to receive the current 26-tool schema. If PostBazooka reports a stale workflowVersion, the rejected action did not run and the agent retries once after re-fetching the workflow.

## Installation

```bash
claude mcp add --transport http postbazooka https://postbazooka.com/mcp
```

Complete the OAuth connect flow. The PostBazooka Feed and Scheduled views in the app let humans browse and visually manage what the agent proposes.

## Configuration

```json
{
  "mcpServers": {
    "postbazooka": {
      "url": "https://postbazooka.com/mcp"
    }
  }
}
```

Auth notes: the server is the system of record. Research, drafts and generated images made with an agent's native tools are intermediate results until the matching PostBazooka mutation commits.

## Business Relevance

- **Solo operators** get an agent that researches, drafts and schedules with proof of what actually went out.
- **Agencies** use sourced ideas and team feedback so humans approve before anything publishes, per destination.
- **Content teams** run per-network scheduling modes - automatic, scheduled or held - from one workflow.
- **Media compliance** is built in: post media must be AI-generated, user-provided, or carry verifiable source, license and attribution evidence.

## Integration with CorpusIQ

CorpusIQ tells the agent what to publish - product data, performance metrics, audience insights from its 40+ connectors - and PostBazooka executes the publishing with verifiable commits and feedback loops. The agent drafts from CorpusIQ data, humans approve in PostBazooka, and the commit protocol confirms what actually went live.

## Limitations

- Eight networks, subject to social-provider limits on paid and free plans alike.
- workflowVersion expiry means an outdated action is rejected, not silently applied.
- Free plan capacity limits are surfaced in tool results.
- The commit protocol requires the direct tool result as proof; a later read cannot substitute for it.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [PurrPlan MCP - Agent-Driven Social Scheduling and Inbox](/docs/hermes/mcp/servers/external/purrplan-mcp)
- [PostMCP MCP - Social Publishing Pipelines for Agents](/docs/hermes/mcp/servers/external/postmcp-mcp)
- [BulkPublish MCP - Multi-Platform Social Publishing for Agents](/docs/hermes/mcp/servers/external/bulkpublish-mcp)
