---
title: BulkPublish MCP - Multi-Platform Social Publishing
description: "MCP server for the BulkPublish social publishing API across 11 platforms: create, schedule, retry and approve posts, upload media, manage RSS autoposting, channel sets and labels, and read engagement analytics and quota usage. About 50 README-documented tools via npx @bulkpublish/mcp-server, plus a multi-tenant hosted HTTP transport and MCP Apps UI widgets."
category: Marketing
stars: 1
added: 2026-09-02
source: "mcp.so GitHub issue #3893"
relevance: ★★
tags: [social-media, publishing, scheduling, analytics, multi-platform, content]
---

# BulkPublish MCP - Multi-Platform Social Publishing for Agents

**Stdio MCP server (npx) plus a hosted HTTP transport** - lets AI assistants run the BulkPublish social publishing API: create and schedule posts across 11 platforms, manage media uploads, RSS autoposting, channel sets and labels, and read engagement analytics, all through natural conversation.

## Spec Block

| Field | Value |
|---|---|
| Server name | @bulkpublish/mcp-server |
| Repo | github.com/azeemkafridi/bulkpublish-api (mcp-server/ subdir) |
| npm | @bulkpublish/mcp-server v1.18.0 |
| Transport | stdio (npx) or Streamable HTTP (dist/http.js) |
| Hosted endpoints | POST /mcp, GET /.well-known/mcp/server-card.json, GET /health |
| Auth | BULKPUBLISH_API_KEY env var, bp_ key from app.bulkpublish.com/developer |
| License | MIT |
| Stars | 1 |

## Why This Matters for Operators

Social publishing for agents has matured into full operations: BulkPublish covers the whole post lifecycle with team approval (approve_post, reject_post), failure recovery (retry_post, bulk_posts), recurring schedules, RSS autoposting with draft or publish modes, and channel token health checks. The hosted transport is multi-tenant and lets discovery run keyless while tool calls require the caller's own key.

## Tools & Capabilities (~50 README-documented tools)

| Group | Tools |
|---|---|
| Posts | create_post, compose_post, update_post, get_post, list_posts, delete_post, publish_post, retry_post, approve_post, reject_post, get_post_metrics, publish_story, bulk_posts, get_queue_slot |
| Channels | list_channels, get_channel_health, get_channel_options, search_mentions |
| Channel sets | list_channel_sets, create_channel_set, update_channel_set, delete_channel_set |
| RSS autopost | list_rss_feeds, create_rss_feed, update_rss_feed, delete_rss_feed |
| Media | upload_media, get_media, list_media, delete_media, create_media_upload, finalize_media_upload, create_multipart_upload, complete_multipart_upload, abort_multipart_upload |
| Labels | create_label, list_labels, update_label, delete_label |
| Analytics & account | get_analytics, get_quota_usage |
| Schedules | list_schedules, create_schedule, update_schedule, delete_schedule |
| MCP Apps UI | view_analytics, view_posts, view_channels, view_media, view_quota |

## Installation

```bash
npx @bulkpublish/mcp-server
```

Claude Desktop config adds the package with the BULKPUBLISH_API_KEY environment variable. Claude Code: `claude mcp add bulkpublish -- npx -y @bulkpublish/mcp-server`.

For claude.ai custom connectors or Smithery's gateway, deploy the bundled Streamable HTTP transport and connect to `https://<host>/mcp?key=bp_...`. A Dockerfile is included.

## Configuration

- Get a bp_ API key at app.bulkpublish.com/developer
- initialize, tools/list and resources need no key; a tools/call without one returns 401
- The compose_post and view_* tools render interactive MCP Apps widgets in hosts that support them, falling back to plain text elsewhere

## Business Relevance

Useful for: marketing operators running multi-platform content calendars through an agent, agencies handling many client accounts with channel sets and approval flows, and content teams automating RSS-to-social pipelines with draft review gates.

## Integration with CorpusIQ

Complementary to CorpusIQ's business-data connectors: BulkPublish handles the publishing execution layer while CorpusIQ supplies the analytics and operational data that decides what to publish.

## Limitations

API key required for all writes. Analytics read depends on platform-provided metrics; unsupported metric keys are stored as 0, not measured. Requires Node 20.19+ for the stdio server.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [PostMCP MCP - Social Publishing Pipelines for Agents](/hermes/mcp/servers/external/postmcp-mcp)
- [Mysocial MCP - Your Real Social Media History as Agent Memory](/hermes/mcp/servers/external/mysocial-mcp)
