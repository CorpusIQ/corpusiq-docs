---
title: "Antwork MCP - Social Publishing with Learned Brand Voice"
description: "Hosted MCP server for drafting, scheduling, publishing and analyzing social posts to LinkedIn, X, Instagram, Facebook, Threads, TikTok, Pinterest and YouTube. 35 tools across seven categories, per-platform voice profiles learned from existing content, OAuth 2.1 with PKCE and granular scopes."
category: Social Media Management
stars: n/a (new listing)
added: 2026-08-22
source: mcpservers.org
relevance: ★★★
tags: [social-media, publishing, scheduling, analytics, brand-voice, oauth, multi-platform, remote-mcp]
---

# Antwork MCP

**A hosted social publishing server with 35 tools across identity, workspaces, social accounts, voice profiles, posts, publishing, analytics and media.** Antwork lets an AI agent draft on-brand posts for LinkedIn, X, Instagram, Facebook, Threads, TikTok, Pinterest and YouTube, schedule or publish them, then read engagement metrics back. Voice profiles are learned per account from your existing content, so the agent writes in a tone that matches each platform's audience rather than a generic one. The endpoint (`api.antwork.io/mcp`) is live (HTTP 401 auth gate confirmed for anonymous callers) and implements OAuth 2.1 with PKCE and dynamic client registration.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (PKCE + DCR) - scoped read / write / publish / media
Endpoint: https://api.antwork.io/mcp
Tools: 35 (identity, workspaces, social accounts, voice profiles, posts, publishing, analytics, media)
Pricing: Free plan available; Pro and Business tiers (antwork.io/pricing)
Built by: Antwork (antwork.io), Spain - public release v1.0 May 2026
```

## Why This Matters for Operators

Social media execution sits in a gray zone: the strategy is human, but the daily work is repetitive enough that operators end up copy-pasting captions across platforms and guessing posting times. **Antwork moves the whole execution loop - drafting, scheduling, publishing and read-back - into the agent while keeping destructive steps behind explicit OAuth scopes.** The `publish` scope is only granted when you approve it, and every publish returns per-platform status, so a failed LinkedIn post does not silently vanish.

The voice-profile mechanic is the practical piece. Instead of prompting "write in my brand voice" on every call, the agent pulls a stored profile that Antwork learned from your existing posts per platform. The X post is punchy, the LinkedIn post is measured, and neither needs a style paragraph every time.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `whoami`, `list_workspaces`, `set_default_workspace` | Identity and workspace context for multi-brand setups |
| `get_workspace_settings`, `update_workspace_settings` | Brand identity, content guidelines and target audience per workspace |
| `list_social_accounts`, `get_connection_urls`, `disconnect_social_account` | Connect, inspect and revoke social accounts with health status |
| `get_voice_profiles`, `get_voice_profile`, `fetch_platform_posts` | Per-platform tone and vocabulary learned from existing content |
| `list_posts`, `search_posts`, `get_post`, `get_post_history` | Read drafts, scheduled, published and failed posts with metrics |
| `create_post`, `update_post`, `duplicate_post`, `delete_post` | Draft management - create_post makes a draft only, never publishes |
| `publish_post`, `schedule_post`, `retry_failed_post` | The destructive trio behind the publish scope, with per-platform results |
| `get_performance`, `get_engagement_history`, `get_optimal_posting_times` | Aggregates, timeseries and suggested posting windows per platform |
| `list_media`, `get_media`, `upload_media`, `attach_media`, `delete_media` | Workspace media library for images, video and PDFs |

Four MCP Apps (posts-table, post-preview, calendar, connections-panel) render interactive UI in hosts that support the MCP Apps spec; other clients get the same data as raw tool output.

## Installation

```bash
claude mcp add antwork --transport http https://api.antwork.io/mcp
```

Per-client walkthroughs are published for Claude, ChatGPT, Claude Code, Cursor, VS Code, Windsurf, Gemini CLI and OpenClaw at antwork.io/docs/mcp.

## Configuration

```json
{
  "mcpServers": {
    "antwork": {
      "type": "http",
      "url": "https://api.antwork.io/mcp"
    }
  }
}
```

Sign up at antwork.io/connect first (free plan available). The first tool call triggers browser OAuth; approve scopes on the consent screen. Access tokens are short-lived JWTs (5 minute TTL) with server-side refresh tokens, revocable per client.

## Business Relevance

- **Agency operators** run multiple client workspaces from one server, each with its own voice profiles and connected accounts.
- **Founders without a social team** hand the drafting and scheduling loop to an agent while the publish scope stays behind an explicit grant.
- **E-commerce brands** keep Pinterest, TikTok and Instagram feeds publishing from one content plan with per-platform copy.
- **Content leads** get per-day engagement history and suggested posting windows instead of exporting CSVs from five dashboards.

## Integration with CorpusIQ

Antwork pairs with CorpusIQ's business data connectors to make content decisions data-backed rather than vibes-backed. An agent can pull last week's Shopify revenue or GA4 traffic spike through CorpusIQ, then use Antwork's `get_optimal_posting_times` and `create_post` to schedule the announcement post that explains it. Stripe or QuickBooks data on a new pricing tier becomes a publish-ready post drafted in the brand's learned voice without a human copy pass.

The loop closes in both directions: Antwork's `get_post_history` and `get_performance` feed engagement numbers back into the same conversation where CorpusIQ surfaces revenue and traffic, so an operator can ask one question and see whether a post drove actual business, then schedule the follow-up in the same session. CorpusIQ's own social scheduling covers CorpusIQ-brand channels; Antwork is the operator-facing complement for teams that want OAuth-scoped publishing for their own brands.

## Limitations

- Brand new: first public release May 2026, no independent track record yet.
- Commercial SaaS: posting accounts and voice profiles live in Antwork's cloud, not self-hosted.
- Soft rate limit of 60 tool calls per minute per workspace; downstream platform limits still apply.
- Origin allowlist for browser-based clients (first-party hosts plus claude.ai and Anthropic domains).
- Publishing still rides each platform's own rate limits and review processes.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
