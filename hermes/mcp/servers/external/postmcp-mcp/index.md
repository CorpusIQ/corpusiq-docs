---
title: PostMCP MCP - Social Publishing Pipelines for Agents
description: Connect social publishing to AI assistants - 15 tools for workspaces, connected accounts, brand kits, pre-flight checks and scheduled posts across LinkedIn, X, Facebook, Instagram, Threads, Bluesky and YouTube Shorts.
category: Marketing
stars: n/a (new listing)
added: 2026-09-02
source: mcp.so
relevance: ★★★
tags: [social-media, publishing, scheduling, linkedin, twitter, bluesky, remote-mcp]
last_updated: "2026-10-19"
---

# PostMCP MCP

**Remote MCP server (stdio or Streamable HTTP, API key or OAuth)** - the official PostMCP AI server that connects social media publishing pipelines directly into AI assistants, IDE workflows and web environments. Fifteen tools cover workspaces, connected accounts and their token health, brand kits, the post queue, pre-flight checks, create/schedule/publish/retry/delete, and image generation, across LinkedIn, X (Twitter), Facebook, Instagram, Threads, Bluesky and YouTube Shorts.

```
Server type: Remote (Streamable HTTP) or stdio (npx)
Auth: API key (env, query param or header) or OAuth 2.0 PKCE (RFC 9728)
Endpoint: self-hosted HTTP mode; stdio via npx -y @postmcpai/server
Tools: 15 (accounts, brand kits, post queue, pre-flight, publishing, image generation, batching)
Pricing: PostMCP AI workspace plans with credit-based post costs
Category: Marketing
Built by: PostMCP AI (MIT, github.com/postmcp/postmcp-mcp-server)
```

## Why This Matters for Operators

Publishing is where agents usually stop being useful: they draft the post and then a human copies it into a scheduler, per platform, per profile. PostMCP's server gives an agent the whole pipeline - connected accounts, brand kits, the queue and the publish action itself.

The tooling is designed for production use rather than demos. A `preflight_post` dry run checks character limits, unconnected profiles, missing media and credit cost before anything publishes. A `multicall` tool runs up to 20 operations in one request with tool names validated before anything executes, so a typo cannot leave half a batch written. **Every account's token health is queryable, so an agent can detect an expired connection before a scheduled post silently fails.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `get_user_info` | Authenticated user: plan, credit balance, AI tokens, active workspace |
| `list_workspaces` | Every workspace the user belongs to, with roles and connected platforms |
| `get_connected_accounts` | Connected social profiles with the profileId needed to target them |
| `get_account_health` | Connections whose token expired or is close to it |
| `list_brandings` | Brand kits: tone, audience, keywords, style images |
| `list_posts` / `get_post` | Post queue with per-profile delivery status, live URLs and per-profile errors |
| `preflight_post` | Dry run: character limits, unconnected profiles, missing media, credit cost |
| `create_post` | Draft, schedule or immediately publish; each profile becomes its own post |
| `publish_post_now` | Publish immediately; also retries failed posts, skipping delivered profiles |
| `update_post` / `reschedule_post` | Edit content, targets, schedule or media; move a post to a new slot |
| `reset_stuck_post` / `delete_post` | Release a post stuck mid-publish; cancel a scheduled or failed post |
| `generate_image` | Generate a post image and return its hosted URL for mediaUrl |
| `multicall` | Run up to 20 of the above in one ordered request |

## Installation

```bash
npx -y @postmcpai/server
```

For HTTP mode, set the `PORT` environment variable to launch the Streamable HTTP server. The API key is read from `POSTMCPAI_API_KEY`, a URL query parameter, or an `x-api-key` header.

## Configuration

```json
{
  "mcpServers": {
    "postmcpai": {
      "command": "npx",
      "args": ["-y", "@postmcpai/server"],
      "env": {
        "POSTMCPAI_API_KEY": "pmcp_sec_your_api_key"
      }
    }
  }
}
```

Claude.ai connects over OAuth 2.0 with PKCE (RFC 9728) dynamic client registration. Every tool accepts an optional `workspaceId`; the API key carries its own workspace by default.

## Business Relevance

- **Marketing operators** run multi-platform publishing from one agent conversation instead of five dashboards
- **Agencies** hold client brand kits in the workspace and pre-flight every post before it schedules
- **Founders** get token-health visibility so a lapsed connection never eats a launch announcement
- **Product teams** batch create and reschedule posts with the multicall tool

## Integration with CorpusIQ

PostMCP is the publishing rail; CorpusIQ is the measurement rail. An agent composing both can draft a launch post in PostMCP's queue while CorpusIQ connectors pull the numbers that make the post credible - Stripe revenue, GA4 signup growth, Shopify sales - and then pre-flight the post against per-platform limits before scheduling. After publication, CorpusIQ reads the traffic and revenue the campaign produced, and the agent decides what to retry or reschedule. The loop is draft, verify with real business data, publish, then measure.

## Limitations

- Brand new listing with no track record yet
- Publishing itself requires a PostMCP AI workspace and per-post credits
- YouTube Shorts is the video surface; no long-form publishing yet
- Self-hosted HTTP mode is the remote path; the npm package is the standard install
