---
title: "HTML Pub MCP — Integration Guide"
description: "Publish AI-generated HTML to live pages on your own domain. MCP server by Leadpages."
category: mcp
tags: [mcp-server, content-publishing, html, leadpages, cms]
last_updated: 2026-07-13
---

# HTML Pub MCP — Integration Guide

**Provider:** Leadpages
**Remote endpoint:** `https://mcp.htmlpub.com/mcp`
**Category:** Content Publishing
**Listing:** mcp.so (July 13, 2026)

## Overview

HTML Pub is an MCP server by Leadpages that lets AI agents (Claude, ChatGPT, Cursor) publish AI-generated HTML to a live page on your own domain. This bridges the gap between AI content generation and web publishing — agents create the page and deploy it in one workflow.

## Why This Matters for Operators

- **No-code publishing:** AI agents can create and publish landing pages, announcements, and microsites without touching a CMS
- **Own domain:** Published pages live on your domain, maintaining brand control and SEO value
- **Leadpages ecosystem:** Backed by Leadpages, an established martech company — signals long-term maintenance
- **First major martech MCP:** Leadpages is one of the first established SaaS companies to ship an MCP server for content publishing

## Installation

This is a remote MCP server — no local installation required.

```json
{
  "mcpServers": {
    "htmlpub": {
      "url": "https://mcp.htmlpub.com/mcp"
    }
  }
}
```

## Available Tools

*Remote server — full tool list to be confirmed from Leadpages documentation:*
- HTML page creation and publishing
- Domain configuration
- Page management (update, unpublish, list)

## Use Cases

1. **Landing Pages:** AI agents generate and publish campaign landing pages directly from conversation context
2. **Documentation:** Publish auto-generated API docs, changelogs, and release notes as live pages
3. **Announcements:** Create and publish company announcements, product updates, and event pages
4. **Microsites:** Rapidly deploy single-purpose microsites for experiments and campaigns

## Complementary to CorpusIQ

CorpusIQ provides the business data layer — operators can pull metrics, generate reports, and then publish them as live dashboards or status pages via HTML Pub. The combination enables end-to-end data-to-publishing workflows entirely through AI agents.

## Status

⚠️ **New listing (July 13, 2026)** — by Leadpages. Strong backing from an established company suggests this will be maintained. Monitor the remote endpoint for availability and rate limits.
