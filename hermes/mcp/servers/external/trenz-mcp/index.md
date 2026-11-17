---
title: "Trenz MCP - TikTok Shop Research and Publishing"
description: "OAuth remote MCP over 15 TikTok Shop markets: product research, AI video generation and scheduled publishing to four social platforms."
category: "Social Commerce / TikTok Shop"
stars: "n/a (hosted, OAuth; 15 documented tools)"
added: 2026-11-17
source: "the mcpservers.org sitemap shard servers/12.xml (slug www-trenz-ai-mcp) and the vendor's MCP page read 2026-11-17; the endpoint answered HTTP 401 to an anonymous handshake"
relevance: ★★
tags: [tiktok-shop, social-commerce, product-research, video-generation, scheduling, oauth, remote, mcp]
last_updated: "2026-11-17"
---

# Trenz MCP

**Product research and posting are the same loop with a tool boundary in the middle.** Someone reads what is selling, decides what to make, makes it, and publishes it, then reads what it sold. Every platform API separates those four steps into different consoles, which is why the loop usually runs weekly instead of daily.

Trenz collapses the four into one remote server: search TikTok Shop data across **15 markets**, generate the video, publish to TikTok, Instagram, YouTube or Facebook with the product linked, then read views, orders and GMV back. It is a TikTok Shop analytics product first and an MCP server second, and the tool names reflect that order.

```
Server type:   remote Streamable HTTP
Endpoint:      https://mcp.trenz.ai/mcp/oauth
Auth:          OAuth (sign in to a trenz.ai account, then grant the connector)
Tools:         15+ documented, research / create / publish / measure
Markets:       15 TikTok Shop markets
Listed on:     mcpservers.org, sitemap shard servers/12.xml
```

## The evidence tier

**Gated endpoint, documented surface.** An anonymous `initialize` to `https://mcp.trenz.ai/mcp/oauth` answered HTTP **401**, which is the auth gate rather than an absence: the route exists and refuses unauthenticated callers. No tool schema was read directly this pass, so the tool names and capabilities below are quoted from the vendor's own MCP documentation, read 2026-11-17, and are labelled as documentation rather than as measured behaviour.

The endpoint itself carries a `?src=website` parameter on the vendor's copy link, which suggests attribution is expected in the URL rather than in a header. Treat that as an observation about how the vendor publishes the address, not as a requirement.

## Tools & Capabilities

| Tool | Area | What it answers |
|---|---|---|
| `search`, `get_detail`, `get_related` | Research | Products, creators and shops across the markets, with full detail and relations |
| `get_top_selling_products` | Research | Leaderboards by market, category and window |
| `ai_generate`, `check_task` | Create | Video and image generation jobs and their status |
| `generate_canvas_node`, `list_assets` | Create | Canvas nodes on the Pro and Scale plans, and the asset library |
| `publish_social_post`, `list_published_posts`, `get_published_post` | Publish | Scheduled and published posts, including TikTok Shop videos with the product linked |
| `reply_to_comment`, `send_message` | Engage | Comment replies and direct messages |
| `get_social_overview`, `get_seller_daily_report` | Measure | Account performance and the daily seller report |

The vendor's own walkthrough sequences them: `get_top_selling_products`, then `ai_generate`, then `publish_social_post`, then `get_published_post` days later for views, orders and GMV.

## Installation

Add `https://mcp.trenz.ai/mcp/oauth` as a remote MCP server in Claude, Claude Code, Codex, ChatGPT or Cursor, then sign in to the Trenz account and grant access. The vendor also ships a skill for coding agents so the tool selection lands without a prompt describing it.

## Why This Matters for Operators

TikTok Shop data is the part that resists generalisation: the same product sells in one market and sits in another, and the difference is usually discoverable in a seven-day window rather than in a quarterly report. A server that answers "what sold more than 10,000 units in the US this week" and then publishes a video for the closest match in the same conversation compresses a research-to-publish cycle that normally spans three tools and two people.

The commercial shape is also legible before anyone connects: research is per-query, generation depends on plan tier, posting needs the account connected, and the vendor's own materials charge for generation on the upper plans.

## Questions operators ask

### Does it need my TikTok credentials?

Yes. The OAuth flow is against a Trenz account, and publishing runs through the accounts connected to that account. There is no keyless path, which is why this guide carries a documentation tier rather than a driven one.

### Can it post without approval?

`publish_social_post` schedules or publishes, and the vendor's own example prompt asks the assistant to hold until approval is given (*Don't post anything until I approve*), which is a prompt convention rather than an enforced gate. If approval must be structural, the review has to sit in the client workflow, not in the tool.

### What breadth does the research cover?

Fifteen TikTok Shop markets, with product, creator, shop, video and review detail. That is narrower than a general web data source and much deeper inside the one marketplace.

## Related

- [TikTok Transcript MCP](/hermes/mcp/servers/external/tiktok-transcript-mcp) - content-side extraction from public videos
- [Shopify Speed Check MCP](/hermes/mcp/servers/external/shopify-speed-check-mcp) - the storefront side of the same TikTok Shop to Amazon path
