---
title: ReelsFarm MCP
description: AI short-form social content operations — avatars, product scenes, UGC videos and slideshows, with scheduling and approval-gated publishing over MCP.
category: Content
stars: n/a (new listing)
added: 2026-08-17
source: mcpservers.org
relevance: ★★
tags: [social-media, ugc-video, avatars, content-automation, scheduling, publishing, approval-gates, remote-mcp]
---

# ReelsFarm MCP

**Remote MCP server (Streamable HTTP, OAuth or API key)** — ReelsFarm gives an agent the full short-form content loop: generate AI avatars, product scenes, UGC videos, hooks, and slideshows, then schedule and publish across connected social accounts — with every mutation behind a `confirm_action` approval gate in Review mode. Built by ReelsFarm (reelsfarm.com).

```
Server type: Remote (Streamable HTTP)
Auth: OAuth or API key (Authorization: Bearer rfmcp_xxx)
Endpoint: https://mcp.reelsfarm.com/mcp
Tools: ~30 across 7 groups (account, assets, generation, slideshows, publishing, automations, events)
Pricing: account plans with per-generation pricing exposed via get_generation_pricing
Category: Content
Built by: ReelsFarm
```

## Why This Matters for Operators

Short-form video is the highest-leverage channel most operators underuse, because production and posting both bottleneck on humans. ReelsFarm moves the whole loop into MCP: the agent generates the creative, stages the post, and — critically — does not publish without approval.

**The approval gate is the differentiator**: prepare tools return a `confirmationId` and the agent must call `confirm_action` after human approval in Review mode. Idempotency keys make retries safe. This is the exact pattern operators need before handing an agent the keys to their brand's social presence: the agent proposes, the human confirms, the audit trail records.

## Tools & Capabilities

| Group | Common tools |
|---|---|
| Account | get_account, get_mcp_server_info, get_queue_status, get_generation_pricing |
| Assets | list_assets, search_assets, create_product_upload_sessions, import_media_from_url, bulk_import_media |
| Generation | prepare_generate_avatar, prepare_generate_product_scene, prepare_generate_ugc_video, prepare_generate_hook, prepare_ai_clone_job |
| Slideshows | list_slideshows, get_slideshow, create_slideshow, prepare_generate_slideshow_text, prepare_finalize_slideshow, prepare_export_slideshow_video |
| Publishing | list_connected_accounts, prepare_schedule_post, prepare_publish_now, get_publish_status, list_scheduled_posts |
| Automations | list_automations, prepare_create_automation, prepare_update_automation |
| Events | get_recent_events |

## Installation

```bash
claude mcp add reelsfarm --transport http https://mcp.reelsfarm.com/mcp
```

OAuth for browser-authorized clients; API keys (`rfmcp_...`) for CLI and agent config files. Keys are shown once at creation in the ReelsFarm account MCP tab.

## Configuration

```json
{
  "mcpServers": {
    "reelsfarm": {
      "type": "http",
      "url": "https://mcp.reelsfarm.com/mcp",
      "headers": {
        "Authorization": "Bearer rfmcp_xxx"
      }
    }
  }
}
```

First-check prompt the vendor recommends after connecting: inspect the account, list connected publishing accounts, and list scheduled posts — before creating or publishing anything.

## Business Relevance

- **Marketing teams** get a complete avatar-to-publish pipeline that still requires a human yes on every post.
- **E-commerce operators** can generate product-scene creative and stage it to social without a designer or editor.
- **Agencies** running multiple brands get connected-account isolation and per-account scheduling from one MCP surface.
- **Founders** get short-form production that runs on agent time, with pricing visible before generation via `get_generation_pricing`.

## Integration with CorpusIQ

ReelsFarm complements the CorpusIQ social layer end to end. The agent generates and stages content in ReelsFarm's Review mode, the human approves, and Postiz handles the channels CorpusIQ already syndicates — with the TikTok and YouTube connectors measuring how the published creative actually performed. The approval-gate design matches CorpusIQ's own pre-flight doctrine, so a ReelsFarm workflow slots into the existing governance gates rather than bypassing them.

## Limitations

- Brand new — no track record yet; listing appeared August 17, 2026.
- OAuth or single-show API keys — key rotation requires re-creating keys in the account tab.
- Generation is credit-based; per-generation pricing is only visible through the account's pricing tool.
- In Creator or Autopilot modes some prepare tools may execute immediately — the approval gate is strongest in Review mode.
- Platform coverage depends on the accounts you connect; the listing does not enumerate supported networks.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
