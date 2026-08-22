---
title: "Sprkly MCP - Shortform Publishing with Approval Gates"
description: "Hosted MCP server for publishing shortform content to TikTok, Facebook, Instagram, YouTube and Threads via natural language. Queue-based scheduling with optional human approval, scoped API keys, soft-delete and per-account visibility limits. OAuth or API key."
category: Social Media Management
stars: n/a (new listing)
added: 2026-08-22
source: mcpservers.org
relevance: ★★
tags: [shortform, tiktok, instagram, youtube, scheduling, publishing, approval-workflow, remote-mcp]
---

# Sprkly MCP

**A hosted shortform publishing server: draft, schedule and manage TikTok, Facebook, Instagram, YouTube and Threads posts from any MCP client, with everything flowing through the same queue and approval path as a human's posts.** Sprkly's endpoint (`sprkly.app/api/mcp`) is live and served 16 tools to an anonymous probe. Two auth paths exist - OAuth for hosted clients like Claude and ChatGPT, or a scoped `sk_live_` API key for scripts - and the safety model is structural: there is no publish-now tool, agents only ever see the accounts you grant, and published posts cannot be touched by an agent at all.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (PKCE, DCR) or scoped API key (sk_live_)
Endpoint: https://sprkly.app/api/mcp
Tools: 16 (media, drafts, scheduling, accounts, analytics, approvals, billing)
Pricing: Included in every paid Sprkly plan; free trial includes MCP
Built by: sprkly.app
```

## Why This Matters for Operators

Shortform publishing is where AI assistants cause the most damage when they go wrong - a bot posting straight to a brand's TikTok with no review loop is a reputation incident waiting to happen. **Sprkly inverts that: the agent drafts and schedules, but nothing hits a platform without walking the same queue and plan limits as your own posts.** You can require human approval so anything an agent queues waits for your sign-off, and published posts are permanently out of the agent's reach.

For teams already running a shortform operation, the MCP layer turns "what do I have queued this week?" into a question you can ask the assistant instead of opening the dashboard. Account-scoped keys keep a contractor's agent pointed at exactly the accounts it should touch.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `sprkly_list_profiles`, `sprkly_list_connected_social_accounts` | See which accounts and profiles the agent can reach |
| `sprkly_add_media_from_url` | Pull an image or video from a public link into the media library |
| `sprkly_draft_post`, `sprkly_update_scheduled_post`, `sprkly_delete_scheduled_post` | Draft and edit scheduled content (soft delete, undoable 30 days) |
| `sprkly_schedule_post` | Queue a post through the normal plan limits |
| `sprkly_request_post_approval`, `sprkly_get_post_approval_status` | Ask for human sign-off and check where it stands |
| `sprkly_get_post_status`, `sprkly_validate_post_policy` | Track post state and validate content against policy |
| `sprkly_get_account_summary`, `sprkly_get_analytics`, `sprkly_get_billing_summary` | Account, engagement and plan readouts |
| `sprkly_get_tiktok_posting_options` | Platform-specific posting configuration for TikTok |

## Installation

```bash
claude mcp add sprkly --transport http https://sprkly.app/api/mcp
```

Per-client setup guides cover Claude Cowork, Claude Desktop, Claude Code, ChatGPT and Codex at sprkly.app/docs/mcp.

## Configuration

```json
{
  "mcpServers": {
    "sprkly": {
      "type": "http",
      "url": "https://sprkly.app/api/mcp"
    }
  }
}
```

OAuth scopes are `profile`, `mcp:read` and `mcp:write` (plus `offline_access` for a refresh token). API keys can be scoped to `sprkly:*` or per-action (`post:read`, `post:write`, `account:read`, `approval:request`) and to specific accounts only.

## Business Relevance

- **DTC brands** keep a TikTok-first shortform cadence running with an approval step between the agent and the audience.
- **Agency content managers** scope contractor agents to specific client accounts with read-only or draft-only keys.
- **Founders without a content team** get a queue, a schedule and a policy check in one connector.
- **Ops leads** answer "what is live this week" from the assistant instead of the dashboard.

## Integration with CorpusIQ

Sprkly slots into a CorpusIQ-driven content operation as the shortform execution layer. An agent can mine revenue and product signals through CorpusIQ's Shopify, Stripe and GA4 connectors, draft the corresponding shortform post with Sprkly's draft tools, run it through `sprkly_validate_post_policy`, and hand it to the approval queue, all in one session. The approval gate becomes the single human checkpoint between business data and public content.

For teams that already run CorpusIQ's own social scheduling, Sprkly is the shortform-specialist complement: its queue discipline and account scoping are built for TikTok and Shorts workflows where approval-before-publish matters most.

## Limitations

- New listing: no independent track record as an MCP server yet.
- Shortform platforms only - no LinkedIn or X publishing here.
- No publish-now tool by design; everything rides the normal queue and plan limits.
- When a trial ends without a plan, calls return 403 `plan_required`.
- Published posts are read-only to agents forever - by design, but worth knowing before you build a workflow around it.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
