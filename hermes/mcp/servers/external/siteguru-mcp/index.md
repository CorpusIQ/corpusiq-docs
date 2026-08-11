---
title: "SiteGuru MCP — SEO audit, ranking, and backlink data for AI agents"
description: "Connect SiteGuru's full SEO dataset — prioritized to-do lists, audit data, rankings, backlinks, and indexation status — directly to AI agents via MCP. Remote MCP with OAuth or API key auth."
category: mcp
tags: [mcp-server, seo, marketing, analytics, google-search-console]
source: mcp.so
discovered: 2026-08-11
stars: 0
author: SiteGuru (Rick van Haasteren)
github: null
mcp_endpoint: https://mcp.siteguru.co/mcp
transport: Streamable HTTP
auth: OAuth (one-click) or Bearer API key
---

# SiteGuru MCP Server

**SEO audit data meets AI agents.** SiteGuru's MCP server connects your full SEO dataset — crawl audits, Google Search Console rankings, Google Analytics traffic, backlink profiles, and indexation status — directly to Claude, ChatGPT, Cursor, and any MCP-compatible client.

## Why It Matters for Operators

For business operators managing websites, SEO data lives across multiple tools (GSC, GA, Ahrefs, crawlers). The SiteGuru MCP unifies this into a single conversational interface. Instead of opening 4 dashboards, you ask:

- *"What should I fix first on my site?"*
- *"Which pages lost the most traffic last month?"*
- *"What are my top keywords and where do I rank for each?"*
- *"Which pages are missing meta descriptions or have titles that are too long?"*
- *"Which keywords am I ranking just below page one for — the easiest wins?"*
- *"Draft new meta descriptions for the pages that are missing one."*

This is operational SEO — not just reporting, but prioritization and action from natural language.

## Technical Details

| Field | Value |
|-------|-------|
| **Transport** | Streamable HTTP |
| **Auth** | OAuth (one-click) or Bearer API key |
| **Endpoint** | `https://mcp.siteguru.co/mcp` |
| **Data available** | SEO audit, rankings, backlinks, indexation, page speed, structured data |
| **Plan required** | SiteGuru plan with MCP access |
| **Access scope** | Tied to your SiteGuru account — only sites you can access |
| **Request model** | Access re-checked on every request |

## Setup

### Claude Desktop / Claude Code

```json
{
  "mcpServers": {
    "siteguru": {
      "url": "https://mcp.siteguru.co/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_SITEGURU_API_KEY"
      }
    }
  }
}
```

**One-click setup (recommended):** Paste the server URL into Claude Desktop or Claude.ai. SiteGuru opens a browser page where you click **Allow** — no key to copy.

**API key setup:** Create an API key in your SiteGuru account settings and pass it as a Bearer token. Best for Claude Code, scripts, or CI.

### ChatGPT

Add as a remote MCP connector at `https://mcp.siteguru.co/mcp` — one-click OAuth connection, no key to copy.

### Cursor / VS Code

```json
{
  "mcpServers": {
    "siteguru": {
      "url": "https://mcp.siteguru.co/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_SITEGURU_API_KEY"
      }
    }
  }
}
```

## CorpusIQ Integration

CorpusIQ can complement SiteGuru MCP by providing business context alongside SEO data — connecting SEO performance (traffic, rankings) with business metrics (revenue, conversions, customer acquisition cost). For operators running e-commerce or SaaS, the combination of SEO intelligence + business financials in one agent session closes the loop between traffic and revenue.

## Limitations

- Requires a paid SiteGuru plan with MCP access (not available on free tier)
- No public GitHub repository — documentation at [siteguru.co/seo-academy/siteguru-mcp-setup](https://www.siteguru.co/seo-academy/siteguru-mcp-setup)
- Data is limited to sites connected in your SiteGuru account
- No write operations — read-only SEO intelligence
- Access re-verified on every request (site removed from account = connection can't reach it)

## Verdict: ★★★

**Strong operator tool.** For any business with a website, this MCP makes SEO data instantly conversational. The "one-click OAuth" setup is frictionless, and the ability to ask for prioritized fixes + drafts for missing meta descriptions makes it genuinely actionable. Pair with CorpusIQ for revenue context, AfterLaunch for GEO/AI-search visibility, and Ahrefs MCP for competitive keyword research.

## See Also

- [AfterLaunch MCP](/hermes/mcp/servers/external/afterlaunch-mcp/) — AI answer visibility + GEO
- [Ahrefs MCP](/hermes/mcp/servers/external/ahrefs-mcp/) — Competitive keyword research
- [Pangolinfo MCP](/hermes/mcp/servers/external/pangolinfo-mcp/) — Amazon + e-commerce intelligence
