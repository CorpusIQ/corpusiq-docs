---
title: "GoLogin MCP Server - CorpusIQ Docs"
description: "Browser profile management for multi-account operations — create, configure, and control GoLogin profiles through AI"
stars: 18
language: JavaScript
auth: "API Token"
transport: "Remote HTTP"
status: "Official"
created: 2025-06-18
repository: "https://github.com/gologinapp/gologin-mcp"
category: "Social Media / Automation"
priority: "★★"
last_updated: 2026-07-27
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/gologin-mcp/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# GoLogin MCP ★★ Official

The official GoLogin MCP server. Lets AI agents create, configure, and control GoLogin browser profiles — the anti-detect browser infrastructure used by operators managing multiple social media, e-commerce, and advertising accounts. 18 stars, from GoLogin themselves.

## What It Does

GoLogin is an anti-detect browser that creates isolated browser profiles with unique fingerprints (canvas, WebRTC, fonts, etc.). Platforms that ban or limit accounts based on browser fingerprinting cannot link GoLogin profiles to each other. The MCP server puts this infrastructure under AI agent control.

**Key capabilities:**
- Create and delete browser profiles
- Configure fingerprint parameters (canvas, WebGL, fonts, geolocation)
- Launch profiles programmatically
- Manage proxy assignments per profile
- Multi-account orchestration at scale

## Why It Matters for Operators

Operators running multiple brand accounts, ad accounts, or marketplace seller accounts face constant ban risk from platform fingerprinting. GoLogin + MCP means your AI agent can manage dozens of isolated browser profiles without manual setup. Combined with x-use MCP (X/Twitter automation) or Postiz (social scheduling), this creates a fully autonomous multi-account social media operation.

**Use cases:**
- Multi-brand social media management across platforms
- E-commerce marketplace seller accounts (Amazon, eBay, Etsy)
- Ad account management across Google Ads, Meta Ads, TikTok Ads
- Competitive research without detection

## Auth

API token from your GoLogin account. Free tier available; paid plans for more profiles and team features.

## Setup

```json
{
  "mcpServers": {
    "gologin": {
      "type": "url",
      "url": "https://api.gologin.com/mcp",
      "headers": {
        "Authorization": "Bearer <your-gologin-api-token>"
      }
    }
  }
}
```

Or via stdio with npx:
```bash
npx @gologinapp/gologin-mcp
```

## Tools

- `create_profile` — Create a new browser profile with specified fingerprint
- `delete_profile` — Remove a profile
- `list_profiles` — List all profiles in your account
- `update_profile` — Modify fingerprint parameters
- `launch_profile` — Start a browser session with the profile
- `assign_proxy` — Attach a proxy to a profile

## Limitations

- Requires a GoLogin account (free tier available but limited profiles)
- API rate limits apply
- Not all fingerprint parameters are exposed through MCP tools yet (evolving)
- 18 stars, still maturing

## Verdict

Niche but powerful for the specific use case of multi-account management. If you operate 5+ social media accounts or marketplace seller profiles, GoLogin + MCP eliminates the manual profile setup bottleneck. Combine with Postiz (scheduling), x-use MCP (X automation), and CorpusIQ (analytics) for end-to-end autonomous social operations.
