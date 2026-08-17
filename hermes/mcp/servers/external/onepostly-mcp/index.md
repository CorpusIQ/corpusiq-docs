---
title: "OnePostly MCP - CorpusIQ Docs"
description: Publish, schedule, and measure posts across X, Instagram, Facebook, Threads, LinkedIn, TikTok, YouTube, Pinterest, and Reddit from any MCP client
category: Content
stars: n/a (new listing)
added: 2026-08-13
source: mcpservers.org
relevance: ★★★
tags: [social-media, publishing, scheduling, marketing, analytics, remote-mcp]
---

# OnePostly MCP

**Remote MCP server (Streamable HTTP, API key) for Onepostly — one social surface for nine platforms.** Publish immediately, schedule ahead, and read normalized insights across X, Instagram, Facebook, Threads, LinkedIn, TikTok, YouTube, Pinterest, and Reddit — all through nine typed tools with the same per-platform validation as the REST API. Write tools debit a workspace wallet; `read_only` keys can list and inspect but never publish.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer API key (op_YOUR_KEY) — read_only keys supported; query-param access for keyless clients
Endpoint: https://mcp.onepostly.com
Tools: 9 (list_connections, publish_post, schedule_post, list_posts, get_post_status, get_insights, delete_post, get_pinterest_boards, get_tiktok_creator_info)
Pricing: Workspace plans; X usage billed pass-through from a wallet
Category: Social Media Management
Built by: Onepostly (onepostly.com)
```

## Why This Matters for Operators

Social publishing MCPs are arriving in a wave — the Aug 13 morning sweep counted 13+ tools in this category. What separates OnePostly is the enforcement model: every publish and schedule call runs the same validation as the REST API, a wallet makes spend explicit instead of metered silently, and read-only keys let an operator give the assistant visibility without giving it the publish button.

**The permission split is operator-grade.** Finance reviews dashboards with read_only keys while the growth lead runs publishing keys; the agent cannot overstep what the key allows, and X spend is capped by the wallet rather than discovered on the bill.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_connections` | List connected accounts, filterable by platform |
| `publish_post` | Publish immediately — all platforms, per-platform validation, wallet debit |
| `schedule_post` | Schedule for a future wall-clock time with timezone |
| `list_posts` | List posts, newest first |
| `get_post_status` | Per-destination delivery status |
| `get_insights` | Normalized engagement metrics per post |
| `delete_post` | Remove a published destination |
| `get_pinterest_boards` | List Pinterest boards before publishing |
| `get_tiktok_creator_info` | TikTok creator privacy options before publishing |

## Installation

```bash
claude mcp add onepostly --transport http https://mcp.onepostly.com --header "Authorization: Bearer op_YOUR_KEY"
```

Claude.ai web users append the key as a query parameter: `https://mcp.onepostly.com?access_key=op_YOUR_KEY`. Keys are minted in Dashboard → Settings → API keys.

## Configuration

```json
{
  "mcpServers": {
    "onepostly": {
      "type": "http",
      "url": "https://mcp.onepostly.com",
      "headers": {
        "Authorization": "Bearer op_YOUR_KEY"
      }
    }
  }
}
```

## Business Relevance

- **Growth operators** schedule cross-platform campaigns from chat and read normalized engagement per post without logging into nine dashboards.
- **Content teams** get the human gate for free — draft in chat, schedule, and let a second pair of eyes approve before the slot fires.
- **Finance or ops reviewers** run read_only keys for status and insights with zero publish risk.
- **Agencies** manage client rosters per workspace, with per-key platform reach.

## Integration with CorpusIQ

OnePostly moves content; CorpusIQ measures whether it worked. The clean composition: schedule and publish through OnePostly's tools, then let CorpusIQ connectors close the loop — GA4 shows which post drove sessions, Search Console shows the search lift, Klaviyo revenue attribution shows which campaign actually paid, and Ahrefs tracks the brand's rising visibility. CorpusIQ's own Postiz-based publishing remains the managed pipeline; OnePostly is the MCP-native alternative for teams that want publishing inside their assistant, with the business-data verification layer on top either way.

## Limitations

- Wallet debit model — X usage bills pass-through, so check Settings → Billing before heavy campaigns
- `402 INSUFFICIENT_WALLET` blocks publishes until the wallet is topped up
- No server-initiated notifications — poll get_post_status or wire webhooks
- Commercial platform, newer listing — no long track record yet

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
