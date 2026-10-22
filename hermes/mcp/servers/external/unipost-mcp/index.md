---
title: "UniPost MCP - LinkedIn and X Publishing With Approval"
description: "Schedule posts to LinkedIn profiles, X and TikTok from an agent, with a human approval step before anything publishes and X credits priced per post."
category: Marketing
stars: n/a (hosted platform; the agent skill package is MIT)
added: 2026-10-21
source: "mcpservers.org /all page 1 (ajhous44/unipost-agent, newest first)"
relevance: ★★
tags: [social-publishing, linkedin, x, tiktok, scheduling, approval-gate, x-credits, marketing-ops, remote-mcp]
---

# UniPost MCP

**An agent can draft a week of posts in a minute and still not be trusted to publish one. UniPost takes the publishing decision away from the agent on purpose: every post it schedules lands in `pending_approval`, and nothing goes out until a person approves it.**

```
Server type: Remote (Streamable HTTP)
Endpoint: https://mcp.unipost.ai/mcp
Auth: OAuth in the browser, or a workspace API key for scripts and CI
Live check: unauthenticated POST initialize returned HTTP 401 {"error":{"code":-32001,"message":"Sign in to UniPost, or create an API key in UniPost → API keys."}}
Tools: 7, named in the vendor's tool reference with parameters and results
Vendor: UniPost (unipost.ai)
```

## Why This Matters for Operators

The social publishing class here is already deep, and this entry does not close a gap in it. It is worth reading for two facts that decide what an agent-assisted publishing routine actually costs and what it is allowed to do.

The first is the X credit economy. A plain X post costs 1 credit. An X post containing a link costs 13. The free allowance is 10 credits a month, so one link post a month already exceeds it, and a paid workspace gets 50 credits for each of its first ten X accounts and 20 after that. Any plan built on "we will post the link to X" is a plan built on the most expensive call in the product.

The second is the approval model, which is narrower than most. Scheduling and approving are separate tools. `schedule_post` creates the post in `pending_approval` and returns an approval link; `approve_post` approves the pending destinations in that group. A post that was created by a different person's agent cannot be approved through the tool at all, and TikTok posts can only be approved on the UniPost screen because their privacy settings live there.

## What It Actually Does

Seven tools:

- `list_accounts` returns the publishable accounts in the authorized workspace with platform, username and a `needs_reconnect` flag. A personal Facebook connection used only to grant Page access is excluded from destinations.
- `list_posts` reads posts in scheduled-time order, filterable by `pending_approval`, `scheduled`, `publishing`, `posted` or `failed`, up to 50 at a time. There is no pagination cursor, so the limit is a real limit.
- `schedule_post` takes 1 to 10 account IDs, 1 to 3,000 characters, a timezone-aware ISO 8601 time within one year, and up to 10 public HTTPS media URLs. It always creates a pending group and never publishes.
- `approve_post` approves the pending posts in one group. If the scheduled time has already passed, approval triggers publication immediately.
- `cancel_post` deletes posts in a group that are `pending_approval`, `scheduled` or `failed`. A post that is publishing or published cannot be cancelled.
- `get_analytics` returns views, likes, comments and shares totalled by platform plus top posts, for 1 to 365 days, default 30. LinkedIn profiles and X do not report these metrics back, so a missing number is not a zero.
- `get_x_allowance` reports the owner's remaining monthly X credits and each connected X account's remaining hourly and daily posting allowance.

Per-account X limits are 10 posts an hour and 25 a day, enforced at publish time rather than at schedule time, so a scheduled queue can fail later when the allowance has been spent elsewhere.

## Installation

```bash
claude mcp add unipost --transport http https://mcp.unipost.ai/mcp
```

The vendor also ships a skill package for agents that read markdown skills, which includes Hermes:

```bash
npx skills add ajhous44/unipost-agent
```

Setup pages exist per client, including ChatGPT as a custom MCP app on OAuth, Codex, Cursor, Claude Code and Gemini CLI, at https://unipost.ai/agents.

## Configuration

```json
{
  "mcpServers": {
    "unipost": {
      "type": "http",
      "url": "https://mcp.unipost.ai/mcp"
    }
  }
}
```

For scripts, create a key in the workspace API keys screen and send it as a bearer token. Tool calls made with a key still spend the workspace's monthly agent allowance.

## Limits Worth Knowing

- Agent tool calls are 500 a month on the free plan and 1,000 per purchased account on a paid plan, shared across the workspaces the owner has. MCP requests are capped at 60 a minute per workspace.
- Media is fetched by UniPost from the supplied links, so the links must be publicly downloadable over HTTPS. Local files, authenticated links and private network URLs do not work. Images are capped at 8 MB and video at 1 GB.
- Platforms live today are LinkedIn profiles, X and TikTok. Facebook Pages and YouTube are in beta, Instagram and LinkedIn company Pages are marked coming soon. An operator who needs Instagram or a company Page cannot use this yet.
- LinkedIn profiles and X report no post analytics, so the analytics tool is effectively a TikTok and Facebook surface today.
- The tool count and behaviour above come from the vendor's published tool reference. The endpoint authenticates before it will answer `tools/list`, so an unauthenticated probe confirms only that it is live and gated.

## Pricing

Billing is by connected account capacity, graduated, with the first two accounts free.

| Total account position | Monthly price per account in that tier |
|---|---|
| Accounts 1-2 | Free |
| Accounts 3-10 | $3 |
| Accounts 11-30 | $1 |
| Accounts 31 and above | $0.50 |

Five accounts therefore cost $9 a month before tax, and yearly billing is ten times the monthly base, so $90 a year for the same five. Paid capacity runs from 3 to 1,000 accounts and is bought through Stripe-hosted checkout with Stripe as merchant of record.

## FAQ

### Can the agent publish without a person?
Only by calling `approve_post` on a group it created in the same workspace. `schedule_post` cannot publish on its own, and another person's agent-created post requires the UniPost approval screen. A workspace that wants a hard stop keeps approval on the dashboard side.

### What does one link post a day actually cost on X?
Thirteen credits a day against an allowance of 50 credits a month per X account on a paid plan, which is roughly four days of daily link posts before the account runs dry. The same content without the link is 1 credit a day. Check `get_x_allowance` before planning a link-heavy calendar.

### Why catalogue this when six social publishers are already here?
It is a packaged addition, not a gap. The class here is carried by PendPost, TimeToPost, BulkPublish, Blog2Social, Chirpie and Maeve Social. What distinguishes this entry is the pricing shape rather than the capability: per-account graduated billing with two free accounts, an X credit model that prices link posts at thirteen times a plain post, and an approval step that is a separate tool the agent must call.

## See Also

- [PendPost MCP - Local-First Social Publishing with Approval](/hermes/mcp/servers/external/pendpost-mcp/)
- [TimeToPost MCP - Social Scheduling with Draft Approval](/hermes/mcp/servers/external/timetopost-mcp/)
- [BulkPublish MCP - Multi-Platform Social Publishing](/hermes/mcp/servers/external/bulkpublish-mcp/)
