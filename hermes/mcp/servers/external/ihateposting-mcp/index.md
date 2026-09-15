---
title: iHatePosting MCP - Cross-Platform Social Publishing
description: "Official remote MCP server for the iHatePosting scheduler. Agents check per-platform publishing rules, validate a post against every target network before creating anything, save drafts or schedule posts, and list account health - 14 platforms, one campaign adapted per channel."
category: Marketing
stars: n/a (new listing)
added: 2026-09-11
source: mcpservers.org /all
relevance: ★★★
tags: [social-media, scheduling, publishing, marketing, remote-mcp]
---

# iHatePosting MCP

**Remote MCP server (Streamable HTTP, API key)** - the official connector to the iHatePosting scheduler ("Create Once Post Everywhere"). An agent plans one campaign, adapts it per channel with the platform rule book, validates it before creating anything, and keeps a publishing rhythm across 14 platforms without living inside every app. The validation tool runs the same checks the publisher runs seconds before it posts, so the answer is what will really happen.

```
Server type: Remote (Streamable HTTP, stateless)
Auth: API key (vendor account)
Endpoint: https://ihateposting.com/mcp
Tools: 6 live-probed (whoami, get_platform_rules, validate_post, create_post, list_posts, list_accounts)
Pricing: 90 days free, no credit card required to start
Category: Marketing
Built by: iHatePosting
```

## Tools

| Tool | Purpose |
|---|---|
| whoami | Which login the API key belongs to (email and account name) |
| get_platform_rules | Per-platform limits and requirements - character counts, media requirements, mandatory options (Pinterest board, YouTube title) - call before writing a post |
| validate_post | Check a post against every target platform without creating anything - the same checks the publisher runs pre-send |
| create_post | Create a post - action 'draft' saves it (the safe default), 'schedule' sets a publish time |
| list_posts | The 50 most recent posts with per-platform status (draft/scheduled/published/failed) |
| list_accounts | Connected social accounts - platform, handle, health - and what is available for posting |

The rule-book + validate-first design is the difference between composing something that publishes and something a platform rejects.

## Connection

1. Create an iHatePosting account (Google or email sign-in, no credit card for the 90-day free tier) and connect social accounts in the dashboard.
2. Add the endpoint to any MCP client as a remote Streamable HTTP server with the API key.
3. Claude Code one-liner - `claude mcp add ihateposting --transport http https://ihateposting.com/mcp` (then supply the key per the vendor's setup).
4. First moves - `get_platform_rules`, then `validate_post` on the draft, then `create_post` with action draft.

## Verification (Sep 11, 2026 evening sweep)

Endpoint live-probed over JSON-RPC: `initialize` returned serverInfo ihateposting v0.3.0 with tools capability, and a stateless `tools/list` (no session header required) returned all 6 tools with full input schemas - live and responding as documented.

## See Also

- [Chirpie MCP - Unified Social Posting Across 14 Platforms](/docs/hermes/mcp/servers/external/chirpie-mcp)
- [TimeToPost MCP - Social Scheduling with Draft Approval and AutoSEO](/docs/hermes/mcp/servers/external/timetopost-mcp)
- [PostNitro MCP - AI Carousels and Social Publishing for Agents](/docs/hermes/mcp/servers/external/postnitro-mcp)
