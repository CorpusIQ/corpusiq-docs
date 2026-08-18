---
title: "Waldo MCP - CorpusIQ Docs - CorpusIQ Docs"
description: Live marketing data for AI agents. Ad libraries across Meta, Google, LinkedIn and TikTok, social listening, share of voice, audience insights, and trends with every answer cited.
category: Marketing
stars: n/a (new listing)
added: 2026-08-14
source: mcpservers.org
relevance: ★★★
tags: [marketing-intelligence, ad-libraries, social-listening, audience-insights, brand-monitoring, competitive-intel, marketing, remote-mcp]
---

# Waldo MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 or API key)** — Waldo's Brand Intelligence API turned into MCP tools. Ad libraries across Meta, Google, LinkedIn and TikTok, social listening, share of voice, audience insights and category landscapes, with every answer linked to its source. Connect once and your assistant gets the full Waldo surface as tools.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (auto) or API key
Endpoint: https://mcp.waldo.fyi
Tools: Brand search, mentions, paid media, audiences, categories, key management
Pricing: Commercial subscription (credit-metered usage)
Category: Marketing
Built by: Waldo (waldo.fyi)
```

## Why This Matters for Operators

Ad library research today means sitting in platform UI: Meta Ad Library, Google Ads Transparency Center, LinkedIn and TikTok screens, all separate, none scriptable. Social listening means another subscription and another dashboard.

**Waldo MCP collapses competitive ad research and listening into one cited, queryable surface inside your assistant.** The citation discipline is the point — every answer links back to its source, so marketing decisions rest on verifiable data rather than model memory. Because the REST API maps one-to-one to MCP tools, anything the API can do, the agent can do.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `brand_search` | Find brands and their media footprint |
| `brand_mentions_summary` | Social listening rollups with sources |
| `brand_paid_media_ads_list` | Paid ad creatives across platforms |
| `audience_insights` | Audience composition and overlap |
| `category_landscape` | Category-level competitive view |
| `api_key_create` / `api_key_list` / `api_key_revoke` | Manage API keys from inside the assistant |
| Workspace switching | Move between workspaces, check credits and usage |

A strategy plugin variant at `https://mcp.waldo.fyi/strategy` bundles specialized strategy skills with a curated connector.

## Installation

```bash
claude mcp add waldo --transport http https://mcp.waldo.fyi
```

Most clients handle OAuth automatically — add the URL and authorize when prompted. For clients without OAuth support, generate an API key in the Waldo console instead.

## Configuration

```json
{
  "mcpServers": {
    "waldo": {
      "type": "http",
      "url": "https://mcp.waldo.fyi"
    }
  }
}
```

Individual tools can be toggled on or off from the MCP Settings page — only enabled tools appear in your client.

## Business Relevance

- **Growth leads** compare competitor paid media without touching four ad libraries
- **Brand managers** track mentions and share of voice from one query surface
- **Media buyers** pull audience and category insights before committing budget
- **Agencies** run cited client reporting from the assistant instead of exported PDFs

## Integration with CorpusIQ

Waldo's ad library and listening data feeds the same workflows CorpusIQ connectors cover on the first-party side: Meta Ads and Google Ads connectors own your own spend performance, while Waldo MCP adds the competitive layer — what rivals are running, where the category is moving, which audiences overlap. A composed workflow asks Waldo for the category landscape, cross-references your Meta Ads spend by campaign, and produces a cited positioning brief. Research feeds in, publishing flows out through Postiz.

## Limitations

- Commercial subscription with credit-metered usage
- Tool visibility must be managed per workspace (toggle defaults)
- No self-host option
- Brand new listing — no track record yet

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
