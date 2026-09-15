---
title: "PostNitro MCP - AI Carousels and Social Publishing for Agents"
description: "Official PostNitro MCP server that lets AI assistants create, manage and schedule carousels, single-image posts and short videos for LinkedIn, Instagram, TikTok and Threads. Agents pick templates, generate AI images, apply brand kits, manage connected social accounts and schedule publishing without leaving the conversation."
category: Social Media Management
stars: n/a (hosted connector)
added: 2026-09-07
source: mcp.so feed
relevance: ★★★
tags: [social-media, carousels, scheduling, brand-kits, ai-image-generation, linkedin, instagram, tiktok, remote-mcp]
---

# PostNitro MCP - AI Carousels and Social Publishing for Agents

**Remote MCP server (Streamable HTTP, API key / OAuth)** - PostNitro's official MCP connector puts the carousel-generation platform (postnitro.ai) inside any MCP client: an agent can go from a topic sentence to a designed, scheduled LinkedIn or Instagram carousel in one conversation, using the account's own templates, brand kits and connected social accounts instead of a copy-paste workflow into a web editor.

```
Server type: Remote (Streamable HTTP)
Auth: API key (starts with pn-, minted in the PostNitro dashboard); endpoint also advertises OAuth protected-resource metadata
Endpoint: https://mcp.postnitro.ai/mcp
Tools: 35 (carousel, image and video post creation, AI image generation, audio library, template browsing, brand and social account management, scheduling)
Pricing: Free tier available; paid plans on postnitro.ai
Category: Social Media Management
Built by: PostNitro Inc. (postnitro.ai)
```

## Why This Matters for Operators

Social content ops still runs on a human copy-paste loop: write in a doc, import into a design tool, export, upload, schedule. Every step is a place where a post stalls. PostNitro MCP collapses the loop - the agent writes slide copy, picks a template, renders the carousel and schedules it, all inside the chat that produced the content idea.

**Because the connector works against the account's real library - templates, brand kits, presets and connected accounts - output stays on-brand without a human babysitting the design step.** One-and-done defaults mean the operator configures the preferred template and brand once, and every future request uses them automatically.

## Tools & Capabilities

| Group | What the agent does |
|---|---|
| Carousel generation | Generates multi-slide carousels from free-text topics, article URLs or X/Twitter posts, with AI-written slide copy |
| Single-image posts | Creates announcement and quote graphics as designed one-image posts |
| Custom content import | Renders headings, descriptions and images (including infographic data columns) into professionally designed posts |
| AI image generation | Passes visual briefs to generateImages; AI images are baked into the design before rendering |
| Template and brand browsing | Lists the workspace's templates, brand colors and AI presets so requests use real library assets |
| Brand kit and account management | Creates and updates brand kits, lists connected LinkedIn, Instagram, TikTok and Threads accounts |
| Scheduling and publishing | Schedules finished posts with per-platform captions, and lists the existing calendar |
| One-step convenience | _and_wait variants run whole creation flows in one call; generate_and_schedule goes from topic to scheduled post |

## Installation

Get an API key (Log in to postnitro.ai, open the profile menu, choose Embed, whitelist your domains and generate the key - it starts with pn-), then add the endpoint to any MCP client that speaks Streamable HTTP. Claude Desktop, Claude Code, Claude Cowork and Cursor are documented as native-supported clients.

```bash
claude mcp add postnitro --transport http https://mcp.postnitro.ai/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "postnitro": {
      "type": "http",
      "url": "https://mcp.postnitro.ai/mcp"
    }
  }
}
```

Attach the API key as the bearer authorization header on requests. The endpoint is live and auth-gated: an unauthenticated initialize probe returns HTTP 401 with bearer error metadata and OAuth protected-resource information for the token endpoint (scope postnitro, offline_access).

## Business Relevance

- **Founders and solo marketers** get a full carousel pipeline from a single prompt, including scheduling, without hiring a designer.
- **Content teams** keep every post on-brand via shared brand kits and templates instead of per-post design QA.
- **Marketing agencies** run higher post volume per account manager - the agent does generation and scheduling, the human does direction.
- **Social media managers** manage multiple connected accounts (LinkedIn, Instagram, TikTok, Threads) from one assistant conversation.

## Integration with CorpusIQ

PostNitro turns analytics into shipped content; CorpusIQ supplies the analytics. A composed workflow: the agent pulls revenue, traffic and conversion signals from CorpusIQ's Stripe, GA4 or Shopify connectors to identify what performed this month, then hands the winning topic to PostNitro to generate, design and schedule the carousel in the same session. Both systems keep the human as the operator: PostNitro ships drafts to the calendar, and CorpusIQ connectors stay read-only.

## Limitations

- New to this catalog (mcp.so listing created Sep 7, 2026; no public repo to assess - hosted connector).
- Tool names are not published in vendor docs; the 35-tool list is served from the endpoint after authentication.
- Requires a PostNitro account and API key; output quality depends on the plan's AI generation limits.
- Coverage is limited to the four supported platforms (LinkedIn, Instagram, TikTok, Threads).
- Hosted service - no self-host option; the account's assets and schedule live in PostNitro's cloud.

## See Also

- [PurrPlan MCP - Agent-Driven Social Scheduling and Inbox](/docs/hermes/mcp/servers/external/purrplan-mcp)
- [PostBazooka MCP - Social Publishing with Commit Proof](/docs/hermes/mcp/servers/external/postbazooka-mcp)
- [BulkPublish MCP - Multi-Platform Social Publishing for Agents](/docs/hermes/mcp/servers/external/bulkpublish-mcp)
- [Abyssale MCP - Ad Creative Production for Agents](/docs/hermes/mcp/servers/external/abyssale-mcp)
- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
