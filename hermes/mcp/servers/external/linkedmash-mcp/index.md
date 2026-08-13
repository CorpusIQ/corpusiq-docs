---
title: "LinkedMash MCP — LinkedIn saved posts as an AI agent"
description: "Connect your LinkedIn saved-post library to AI agents. Search, organize, draft, schedule, publish, and analyze LinkedIn content — all through MCP. Hosted at"
category: mcp
tags: [mcp-server, social-media, linkedin, content-marketing, scheduling]
source: mcp.so GitHub issues (#3516)
discovered: 2026-08-11
stars: 0
author: LinkedMash (Ramya Chinnadurai)
github: null
mcp_endpoint: https://mcp.linkedmash.com/api/mcp
transport: Streamable HTTP
auth: Bearer token (API key)
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/linkedmash-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"

---

# LinkedMash MCP Server

**Turn your LinkedIn saved posts into an AI-powered content engine.** LinkedMash imports your saved-post library via a Chrome extension, then exposes it to AI agents through a hosted MCP server. Agents can search, cite, draft, schedule, publish, and analyze — all from the posts you already save.

## Why It Matters for Operators

Business operators save LinkedIn posts constantly — competitor announcements, industry insights, viral content formats, hiring strategies. But saved posts become a graveyard. LinkedMash turns them into a searchable, AI-accessible content library:

- **Search your saves:** *"Find my best saved posts on cold outreach from the last 6 months"*
- **Draft from inspiration:** *"Draft a LinkedIn post based on my top 3 saved posts about AI automation"*
- **Schedule & publish:** *"Schedule a post about our new feature for Tuesday at 9am"*
- **Analyze performance:** *"Which of my posts this month got the most engagement?"*
- **Cross-reference:** *"What do my saved posts say about pricing strategies in SaaS?"*

For founders and operators building personal brands, this turns passive consumption into active content creation.

## Technical Details

| Field | Value |
|-------|-------|
| **Transport** | Streamable HTTP |
| **Auth** | Bearer token (`lm_` prefix) |
| **Endpoint** | `https://mcp.linkedmash.com/api/mcp?token=lm_YOUR_TOKEN` |
| **REST API** | `https://api.linkedmash.com/v1` (for code-based access) |
| **Import method** | Chrome extension (one-time import of saved posts) |
| **Tools** | search_bookmarks, draft_post, schedule_post, publish_post, get_analytics |
| **Exports** | Notion, Google Sheets, Airtable, Miro, CSV, JSON, PDF |

## Setup

### Claude Desktop / Claude Code

```json
{
  "mcpServers": {
    "linkedmash": {
      "url": "https://mcp.linkedmash.com/api/mcp?token=lm_YOUR_TOKEN_HERE"
    }
  }
}
```

### ChatGPT / Cursor / VS Code / Windsurf / Codex

Same URL pattern — any MCP-compatible client connects with the hosted endpoint URL plus your token.

### Getting a token

1. Install the [LinkedMash Chrome extension](https://chromewebstore.google.com/detail/linkedmash/ldadjiiepooimpnjagjidpklcpbnamop) to import your saved posts
2. Create an API token at [linkedmash.com/integrations/api](https://www.linkedmash.com/integrations/api)
3. Paste the token into your MCP client config

### Claude Code skill (optional)

```bash
npx skills add linkedmash/agent-skills
```

This installs a Claude Code plugin that teaches your agent how to drive the LinkedMash API without extra prompting.

## CorpusIQ Integration

LinkedMash + CorpusIQ creates a powerful operator content loop: use LinkedMash to search your saved-post library for operator pain points and content gaps, then use CorpusIQ to pull actual business data (revenue trends, churn metrics, customer segments) to ground your LinkedIn content in real numbers. For growth operators, this means LinkedIn posts backed by real business intelligence, not generic thought leadership.

## Limitations

- Requires the LinkedMash Chrome extension to import saved posts (one-time)
- API token required for MCP access (free tier available, paid for higher volume)
- No public GitHub repository — documentation at [linkedmash.com/for-ai-agents](https://www.linkedmash.com/for-ai-agents)
- LinkedIn-only — doesn't cover other social platforms (pair with Xpoz for multi-platform)
- Token passed in URL query string (consider Bearer header for production)

## Verdict: ★★★

**Content operator essential.** For anyone building a LinkedIn presence, this transforms the "saved post graveyard" into a content engine. The search + draft + schedule workflow covers the full content lifecycle. Strong pairing with Xpoz (social listening) and SiteGuru (SEO) for a complete operator content stack.

## See Also

- [Xpoz MCP](/hermes/mcp/servers/external/xpoz-mcp/) — Multi-platform social media intelligence
- [SiteGuru MCP](/hermes/mcp/servers/external/siteguru-mcp/) — SEO audit + rankings
- [AfterLaunch MCP](/hermes/mcp/servers/external/afterlaunch-mcp/) — AI answer visibility + GEO
