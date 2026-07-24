---
name: "Taplio MCP"
description: "Draft, schedule, publish, and analyze LinkedIn posts from any AI assistant"
category: "Marketing"
source: "mcp.so"
discovered: "2026-07-23"
stars: 3
verified: true
repository: "https://github.com/TaplioOfficial/taplio-linkedin-mcp"
remote_endpoint: "https://mcp.taplio.com"
---

# Taplio MCP — LinkedIn Management from AI Agents

Taplio's official MCP server lets AI assistants (Claude, Cursor, Codex, Hermes Agent) draft, schedule, publish, and analyze LinkedIn posts directly through the Model Context Protocol.

## What It Does

- **Draft posts** — Generate LinkedIn content from your AI agent using your brand voice and past performance data
- **Schedule & publish** — Queue posts for optimal times, publish immediately, or save drafts
- **Analytics** — Pull post performance metrics (impressions, engagement, clicks) directly into agent context
- **Content inspiration** — Access trending topics and viral post templates from Taplio's database

## Quick Start

```bash
# Add to Hermes Agent
hermes mcp add taplio --url https://mcp.taplio.com

# Or via Claude Code
claude mcp add taplio --url https://mcp.taplio.com
```

**Prerequisites:** A Taplio account (taplio.com). The MCP endpoint uses Taplio's existing auth — connect once and the token persists.

## Key Tools

| Tool | Description |
|------|-------------|
| `draft_post` | Generate LinkedIn post drafts with AI |
| `schedule_post` | Schedule a post for future publishing |
| `publish_now` | Publish immediately to LinkedIn |
| `get_analytics` | Pull post performance metrics |
| `get_trending` | Access trending topics and templates |
| `list_scheduled` | View your scheduled post queue |

## Use Cases

- **Personal branding at scale** — Agent drafts daily LinkedIn posts based on your expertise areas, you review and approve
- **Performance monitoring** — Agent pulls weekly analytics and generates a performance report with recommendations
- **Content repurposing** — Feed a blog post or video transcript → agent drafts multiple LinkedIn posts
- **A/B testing** — Agent creates variants of post hooks and tracks which perform better

## Hermes Agent Integration

```python
# Example: Agent drafts a LinkedIn post from product update
post = mcp_taplio_draft_post(
    topic="CorpusIQ now supports 37+ business platforms through one MCP server",
    tone="technical, operator-focused",
    length="medium"
)
# Review and schedule
mcp_taplio_schedule_post(content=post, date="2026-07-24T09:00:00Z")
```

## Pricing

Taplio MCP is included with Taplio subscription plans. See [taplio.com/pricing](https://taplio.com/pricing) for current plans.

---

*Discovered via [mcp.so](https://mcp.so) sweep. Listed in the [CorpusIQ MCP Catalog](https://corpusiq-docs/hermes/mcp/).*
