---
title: "B2B Creators MCP - LinkedIn Content Across Every Team Profile"
description: "Remote MCP server for LinkedIn content operations at team scale. Plan, route for approval and publish posts across every personal LinkedIn profile a team manages - 5 to 500 people - with per-profile reporting, company page analytics and LinkedIn Ads breakdowns. Streamable HTTP endpoint; first 2 profiles free."
category: "Social Media Management"
stars: n/a (new listing)
added: 2026-09-12
source: "mcp.so feed (b2b-creators) + vendor site b2b-creators.com"
relevance: ★★★
tags: [linkedin, content, social-media, sales, gtm, remote-mcp]
---

# B2B Creators MCP

**Remote MCP server (Streamable HTTP, workspace sign-in)** - the agent interface for B2B Creators, a LinkedIn content layer for outbound teams. Sales and GTM teams run outreach from their members' personal profiles, but those profiles usually sit empty; B2B Creators plans, routes for approval and publishes content across every profile the team manages (5 to 500 people) from inside Claude, and reports back on profiles, the company page and LinkedIn Ads.

```
Server type: Remote (Streamable HTTP)
Auth: Workspace sign-in through the connector flow (anonymous initialize answers HTTP 401)
Endpoint: https://mcp.b2b-creators.com/mcp
Pricing: First 2 profiles free; paid tiers beyond (workspace saves when you add your email)
Category: Social Media Management
Built by: B2B Creators (b2b-creators.com)
```

## What it does

- **Content across many profiles** - onboard a roster of people once, hold a brand voice per person, build content plans, schedule and publish to each individual's profile.
- **Client approval** - every content plan produces a public link where a client reviews posts, approves or requests changes, and leaves comments; no login needed.
- **Personal profile reporting** - impressions, engagement and current follower totals per person.
- **Company page reporting** - follower growth, page engagement, demographics and per-post reach.
- **LinkedIn Ads reporting** - per-ad breakdowns with spend, CTR, CPC, leads and cost per lead.
- **Canva import** - read a Canva planning document and turn it into a scheduled content plan.

## Connection

1. Add the endpoint in Claude (Settings, Connectors, Add custom connector) or any MCP-compatible client and complete the workspace sign-in.
2. Claude Code one-liner: `claude mcp add b2b-creators --transport http https://mcp.b2b-creators.com/mcp`
3. Onboard the roster: send each person a personal invite link; they connect their own LinkedIn account with no password sharing.
4. First 2 profiles are free; the workspace saves when an email is added.

## Verification (Sep 12, 2026 midday sweep)

Endpoint live-probed over JSON-RPC initialize: anonymous initialize returns HTTP 401 `{"error":"unauthorized"}` - the endpoint exists and is auth-gated through the connector sign-in flow (the directory listing's FAQ claims no auth; the live probe takes precedence). Tool names are not published; the vendor page documents the capability set above and a Canva import workflow.

## See Also

- [LinkedIn MCP by GTM API - Integration Guide](/hermes/mcp/servers/external/linkedin-mcp-gtm/)
- [LinkedIn Ghostwriter MCP - LinkedIn Posts in Your Voice](/hermes/mcp/servers/external/linkedin-ghostwriter-mcp/)
- [RedReplier MCP - Social Lead Monitoring and Reply Drafts for Agents](/hermes/mcp/servers/external/redreplier-mcp/)
