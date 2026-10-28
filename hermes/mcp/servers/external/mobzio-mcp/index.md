---
title: "Mobzio MCP - Marketplace Deeplinks and Attributed Orders"
description: "Wildberries, Ozon, Yandex Market and Kaspi seller links with click statistics and orders attributed to each link."
category: Ecommerce / Marketplace Attribution
stars: ★★ (OAuth, seller workspace)
added: 2026-10-28
source: "live probe of https://app.mobz.io/mcp returning HTTP 401 with no bearer token, plus submission issue chatmcp/mcpso #6302 and the vendor docs at app.mobz.io/docs/mcp"
relevance: ★★★
tags: [ecommerce, marketplace, attribution, deeplinks, wildberries, ozon, yandex-market, kaspi, sellers, streamable-http]
last_updated: "2026-10-28"
---

# Mobzio MCP

**A seller who cannot say which link produced which order is not running a channel, they are guessing at one and paying for the privilege.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://app.mobz.io/mcp (401 without a token)
Auth:        OAuth or bearer token, workspace scoped
Markets:     Wildberries, Ozon, Yandex Market, Kaspi
Tools:       8 read, 1 write, no delete
Docs:        app.mobz.io/docs/mcp
```

## Why This Matters for Operators

Marketplace sellers advertise in places the marketplace never reports on: a Telegram channel, a video, an influencer post, a QR code on packaging. The marketplace credits the order to itself and the seller has no thread back to the thing that caused it. That is the attribution hole that makes a marketing budget unarguable.

This server closes it with deeplinks. Each link is attributable, so clicks and the orders that follow can be read per link, per workspace, with amounts, and the whole thing is exposed to an agent rather than to a dashboard somebody has to remember to open.

## What It Returns, Verified

The endpoint is live and gated: a bare `POST initialize` on `https://app.mobz.io/mcp` returned **HTTP 401**, the expected shape for a seller-scoped surface. The neighbouring paths do not pretend to be the same thing (`/api/mcp` answered 403), so the working route is the documented one.

The published surface, from the submission:

- List workspaces and links
- Read daily click statistics per link
- Read orders attributed to each link, with amounts
- Get a daily account overview
- Diagnose a link when something is not counting
- Create new links, available only when write access is granted
- Eight read tools and one write tool in total, and nothing can be deleted

The markets covered are Wildberries, Ozon, Yandex Market and Kaspi, which is the Russian and CIS marketplace set rather than the Amazon and Etsy set most attribution tools assume. Tool descriptions are in English and the returned data is in Russian, which is worth knowing before an agent is asked to summarise it.

## Limits Worth Recording

The attribution is link-level, not person-level, so it answers which link produced an order and not which customer touched which other link first. The delete surface is deliberately absent, which is the right default for an attribution ledger and a constraint to know before planning any cleanup. And the read scope sits behind OAuth or a bearer token, so a shared team token removes exactly the per-user separation that makes the numbers auditable.

## FAQ

### Which marketplaces does it cover?
Wildberries, Ozon, Yandex Market and Kaspi. It is built for the Russian and CIS seller market rather than for Amazon or Etsy.

### Can an agent create links?
Yes, but only when write access is granted. Read tools work at eight, the write surface is one tool, and nothing can be deleted.

### Does it show which link produced an order?
Yes. Orders attributed to each link are returned with amounts, alongside daily click statistics per link and a daily account overview.

### What language is the data in?
Tool descriptions are in English and the returned data is in Russian, so plan for that in any downstream summary step.
