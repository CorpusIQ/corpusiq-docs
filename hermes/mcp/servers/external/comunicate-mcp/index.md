---
title: Comunicate MCP - Press Release Distribution for Agents
description: 19-tool MCP server for press-release distribution - search a publication catalogue, draft and SEO-check articles, build editorial plans and order publications, with two independent spend locks so an agent cannot drain the account.
category: Marketing
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★
tags: [pr, press-release, publishing, editorial, marketing, content, remote-mcp]
---

# Comunicate MCP

**Press-release distribution with a money switch** - any MCP client (Claude, ChatGPT, Cursor, Gemini) can search the publication catalogue, write drafts, prepare editorial plans and order publications through Comunicate.top. Two independent locks (a permission switch plus API-key scopes) mean an assistant cannot spend unless the operator explicitly allows it.

```
Server type: Remote (stateless Streamable HTTP)
Auth: API key in Authorization header, or OAuth 2.1 (metadata at /.well-known/oauth-authorization-server)
Endpoint: https://app.comunicate.top/mcp
Tools: 19
Pricing: Catalogue and articles free to prepare; publication orders priced per placement (RON)
Built by: Comunicate.top
```

## Why This Matters for Operators

PR outreach is high-effort, low-frequency work that usually falls off the calendar. **Comunicate makes it a plain-language workflow an agent can run end to end** - "find ten health sites under 60 RON", "write a draft about X", "prepare the October editorial plan". The default posture is read-only: searches, drafts and plans run freely, while every order for publication or writing is refused with an explanation until the operator flips the switch. Every switch change lands in the audit log, and key scopes still apply on top, so a misconfigured assistant cannot overspend.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_catalog` | Find publications by niche, domain rating and price |
| `list_publications` / `get_site` / `get_publication` | Catalogue browsing and placement detail |
| `check_article_fit` / `check_article_seo` | Pre-flight checks before drafting or ordering |
| `create_article` / `update_article` / `list_articles` / `get_article` | Draft and iterate articles |
| `create_campaign` / `update_campaign` / `list_campaigns` | Editorial campaigns |
| `order_publication` | Order a placement (spend-gated) |
| `order_writing` / `list_writing_orders` | Order paid writing (spend-gated) |
| `get_balance` / `report_summary` / `whoami` | Account state and reporting |

## Installation

```bash
claude mcp add --transport http comunicate https://app.comunicate.top/mcp --header "Authorization: Bearer bk_live_..."
```

## Configuration

```json
{
  "mcpServers": {
    "comunicate": {
      "type": "http",
      "url": "https://app.comunicate.top/mcp",
      "headers": { "Authorization": "Bearer bk_live_..." }
    }
  }
}
```

Issue the API key under Integrations in your Comunicate.top account, choosing "catalogue and articles only" for a preparation-only assistant or "publications too" for one that can order. The same key works across all integrations.
