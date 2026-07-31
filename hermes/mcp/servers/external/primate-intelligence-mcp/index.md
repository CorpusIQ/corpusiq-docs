---
title: "Primate Intelligence MCP — Integration Guide"
description: "Real-time video analysis and scene understanding for AI agents via predictive world models — register videos by URL, ask questions in plain English, get deterministic answers with confidence scores and timestamps."
category: mcp
tags: [mcp-server, video-analysis, content-monitoring, media-intelligence, video-understanding, agent-tools, hermes-agent]
last_updated: 2026-07-31
---

# Primate Intelligence MCP — Video Scene Understanding for AI Agents

**Rating:** ★★ | **Category:** Media & Content | **Transport:** Streamable HTTP (OAuth 2.1 + Dynamic Client Registration + PKCE)

## What It Does

Primate Intelligence gives AI agents the ability to watch and understand video content at scale. Register a video by URL, ask questions in plain English, and get deterministic yes/no/indeterminate answers with confidence scores and clip timestamps. Unlike AI models that hallucinate video descriptions, Primate Intelligence uses predictive world models — it builds a structured understanding of what's actually happening in each scene and answers questions against that model. The result: reliable, auditable answers about video content without watching the video yourself.

## Why Business Operators Need This

Content monitoring teams spend hours manually checking competitor videos for claims, messaging changes, and compliance issues. Operations teams verifying user-generated content at scale can't watch every upload. Primate Intelligence lets your AI agent do this — "Does this competitor's product demo claim feature X?" or "Is there any adult content in these 200 user submissions?" — with deterministic answers and timestamps you can verify. For media companies, e-commerce operators monitoring competitor video content, brand safety teams, and compliance teams handling video submissions, this is a force multiplier. First MCP for AI video understanding with auditable, non-hallucinated results.

## Quick Start

```
# Install via npm (stdio transport)
npx @primate-intelligence/mcp

# Remote endpoint (Streamable HTTP with OAuth 2.1 + PKCE)
Endpoint: https://api.primateintelligence.ai/mcp
```

### Hermes Agent Configuration

```json
{
  "mcpServers": {
    "primate-intelligence": {
      "transport": "http",
      "url": "https://api.primateintelligence.ai/mcp",
      "auth": {
        "type": "oauth2",
        "authorization_url": "https://api.primateintelligence.ai/oauth/authorize",
        "token_url": "https://api.primateintelligence.ai/oauth/token",
        "client_id": "YOUR_CLIENT_ID",
        "scopes": ["video:read", "video:analyze"]
      }
    }
  }
}
```

### Environment Variables

```bash
export PRIMATE_INTELLIGENCE_CLIENT_ID="pi_..."
export PRIMATE_INTELLIGENCE_CLIENT_SECRET="pi_secret_..."
```

## Key Tools

Primate Intelligence exposes 10 tools with full MCP annotations:

| Tool | Description |
|------|-------------|
| `register_video` | Register a video by URL for analysis — supports YouTube, Vimeo, and direct MP4 links |
| `ask_question` | Ask a yes/no question about the video; returns answer + confidence score + timestamp |
| `ask_open_question` | Ask an open-ended question; returns most relevant scene + description |
| `list_videos` | List all registered videos and their analysis status |
| `get_video_status` | Check analysis progress for a registered video |
| `get_scene_at_timestamp` | Retrieve the scene understanding model at a specific timestamp |
| `get_all_scenes` | Retrieve all detected scenes with descriptions and timestamps |
| `compare_scenes` | Compare two scenes or two videos for differences |
| `search_across_videos` | Search for a concept or claim across all registered videos |
| `delete_video` | Remove a video and its analysis data |

## Pricing

Free tier available with limited video registrations and question quota. Paid tiers for higher volume, longer videos, and priority processing. Check [primateintelligence.ai](https://primateintelligence.ai) for current plans.

## Authentication

OAuth 2.1 with Dynamic Client Registration (RFC 7591) and PKCE. Register your MCP client at [primateintelligence.ai/developers](https://primateintelligence.ai/developers) to obtain a `client_id`. The OAuth flow includes PKCE for security. Sessions are scoped and refreshable.

Alternatively, use the npm package (`npx @primate-intelligence/mcp`) for local stdio transport with API key authentication.

## Source

- **GitHub:** [github.com/Primate-Intelligence/primate-intelligence-mcp](https://github.com/Primate-Intelligence/primate-intelligence-mcp) (0★, created 2026-07-26)
- **Website:** [primateintelligence.ai](https://primateintelligence.ai)
- **MCP Endpoint:** `https://api.primateintelligence.ai/mcp`
- **npm:** `@primate-intelligence/mcp`

## Verdict: ★★ — Pioneering Video Understanding for Agents

Primate Intelligence is the first MCP server for AI video understanding with auditable results. The predictive world model approach — deterministic answers instead of hallucinated descriptions — sets it apart from generic vision AI. For operators who need to monitor competitor video content, verify UGC at scale, or check video compliance without manual review, this is a genuinely new capability.

**Strengths:** Deterministic yes/no/indeterminate answers (no hallucination), confidence scores and clip timestamps for audit, cross-video search, OAuth 2.1 + PKCE security, 10 well-documented tools.

**Limitations:** Brand new (0 stars, created July 26, 2026), free tier limits unknown, video processing speed not documented, only yes/no questions are fully deterministic (open questions are probabilistic), requires videos to be publicly accessible by URL.

**Best for:** Content monitoring teams, brand safety operators, competitive intelligence analysts, compliance teams handling video submissions, media companies managing large video libraries.
