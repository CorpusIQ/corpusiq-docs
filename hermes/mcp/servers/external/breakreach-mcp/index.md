---
title: "Breakreach MCP - AI-Native Social Media Scheduling Across 12 Platforms"
description: "Remote MCP server for creating, scheduling and analyzing social posts across 12 platforms (X, Instagram, TikTok, LinkedIn, Bluesky, Reddit, Telegram, Discord and more): best-time slots, media upload, unified analytics, Bearer API key auth."
category: Social Media Management
stars: n/a (new listing)
added: 2026-08-22
source: "mcp.so GitHub issue #3691"
relevance: ★★★
tags: [social-media, scheduling, publishing, analytics, multi-platform, remote-mcp]
---

# Breakreach MCP

**Schedule and analyze social posts across 12 platforms directly from an MCP client - create, schedule, publish, and read back unified analytics with one tool surface.** Breakreach is an AI-native social media scheduling server: 9 tools to create, schedule and analyze posts for X, Instagram, TikTok, LinkedIn, Bluesky, Reddit, Telegram, Discord and more, with best-time slot suggestions, media upload support, and unified analytics across platforms. The endpoint (`api.breakreach.com/mcp`) is live and returns an HTTP 401 auth gate for anonymous callers, confirming the server is reachable; authenticated use requires a Bearer API key.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer API key (api.breakreach.com)
Endpoint: https://api.breakreach.com/mcp
Tools: 9 (create, schedule, analyze posts; best-time slots; media upload; unified analytics)
Pricing: See breakreach.com (API key required)
Built by: Breakreach (breakreach.com); repo github.com/samuelrondot/breakreach-mcp
```

## Why This Matters for Operators

Social scheduling tools exist in abundance, but most are either human-first UIs or single-platform APIs. **Breakreach puts the full scheduling loop - draft, schedule, publish, measure - inside the agent's tool surface across 12 platforms.** For operators running multi-platform distribution (the standard for agencies, ecommerce brands and content teams), this removes the per-platform API integration work and the copy-paste captions problem: one tool call schedules the same campaign to X, LinkedIn, Instagram and Telegram with platform-appropriate settings.

The best-time slot and unified analytics pieces close the loop that pure schedulers leave open. An agent can propose a posting window from historical engagement, schedule the batch, then read back cross-platform performance and adjust the next batch - a genuinely autonomous distribution workflow.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| Post creation | Draft posts for any of the 12 supported platforms |
| Scheduling | Schedule posts with best-time slot support |
| Publishing | Publish immediately or on schedule |
| Analytics | Unified engagement analytics across platforms |
| Media upload | Attach images and video to scheduled posts |

Nine tools total, all accessed through the remote endpoint with a Bearer API key.

## Installation

```json
{
  "mcpServers": {
    "breakreach": {
      "type": "http",
      "url": "https://api.breakreach.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

For the Claude Code CLI: `claude mcp add breakreach --transport http https://api.breakreach.com/mcp --header "Authorization: Bearer YOUR_API_KEY"`

## Configuration

Generate an API key at breakreach.com and pass it as a Bearer header. The server rejects anonymous calls with HTTP 401 - the key is required for every request.

## Example Prompts

- "Schedule this week's LinkedIn posts for Tuesday and Thursday at the best times."
- "Create an X thread announcing the product launch and schedule it for Friday 9 AM."
- "Pull unified engagement analytics for last week across all connected platforms."

## Integration with CorpusIQ

CorpusIQ answers questions about business data - what campaigns earned, which channels convert, where revenue comes from - while Breakreach executes the posting side. Used together, an agent can read the analytics that matter (CorpusIQ) and schedule the next distribution batch (Breakreach) in one workflow. Breakreach overlaps with CorpusIQ's social scope only at the scheduling surface; CorpusIQ's 40+ connectors remain the read-side authority for business data.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - curated third-party MCP servers for operators
- [Antwork MCP](/hermes/mcp/servers/external/antwork-mcp/) - hosted social publishing with learned brand voice
- [MCP Integration Guide](/hermes/mcp/) - connecting MCP servers to Hermes Agent
