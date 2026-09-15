---
title: "AstroFabric MCP - Agentic Growth Missions for Operators"
description: "Streamable HTTP MCP from AstroFabric, an agentic OS for growth, revenue and digital operations: one mission_agent tool (or the granular catalog via ?tools=all) runs objectives across SEO site audits, AI-visibility checks, email deliverability audits, Google Search Console data, LinkedIn and Google Ads research and HubSpot CRM writes, with scoped keys and a hard per-run cost cap."
category: Marketing
stars: n/a (hosted)
added: 2026-08-27
source: "mcpservers.org /all page 2 (www-astrofabric-ai-docs) - upgraded from Aug 26 thin-docs skip, endpoint now verified"
relevance: ★★★
tags: [growth-ops, seo-audit, geo, ai-visibility, email-deliverability, hubspot, remote-mcp]
---

# AstroFabric MCP

**Hosted remote MCP server (Streamable HTTP, scoped bearer keys or native OAuth) for agentic growth and revenue operations.** AstroFabric is an agentic operating system for growth, revenue and digital operations. Over MCP it exposes exactly one tool by default - `mission_agent` - which takes a plain-language objective, plans the steps, routes work across the platform's tool catalog and model tiers, and returns the finished result or a single clarifying question. Appending `?tools=all` to the server URL exposes the granular catalog with schemas: on-page SEO audits, AI-search visibility checks, email deliverability audits, Google Search Console data, LinkedIn and Google Ads research, and HubSpot CRM writes. Everything is metered against a hard per-run cost cap with published status semantics (401/402/403/409/422/429/502) an agent can self-correct against.

```
Server type: Remote (Streamable HTTP); also a full REST API at /api/v1
Auth: Bearer API key (ek_live_* with scopes) or native OAuth (DCR + PKCE S256); key-embed URL variant for non-header clients
Endpoint: https://www.astrofabric.ai/api/mcp
Tools: 1 by default (mission_agent); granular catalog via ?tools=all
Pricing: Metered, per plan envelope; see astrofabric.ai/pricing
Docs: https://www.astrofabric.ai/docs · OpenAPI: /api/openapi.json
Category: Marketing
```

## Why This Matters for Operators

Growth work today is a pile of disconnected tools: one for SEO audits, one for AI-visibility checks, one for deliverability, plus GSC and ads consoles. AstroFabric compresses this into objectives - "build a list of 100 companies showing high interest in building insulation", "verify these emails", "format them for LinkedIn Ads" - executed by a mission agent that plans, spends against a hard per-run cost cap, and delivers into the operator's systems. **Missions are threads with memory: brand, ICP, competitors and sender identity persist in the workspace, results ship as downloadable CSV lists, and contacts write directly into a connected HubSpot CRM.** Long missions continue themselves in batches, each batch delivered by signed webhook, until the objective is met.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `mission_agent` | The default single tool: objective in, planned multi-step mission out, with clarifying questions continued via history or thread_id |
| `site_audit` | On-page SEO audit of one URL: 0-100 score with per-check findings (meta, headings, canonicals, OG, structured data, speed) |
| `ai_visibility_check` | AI-search readiness audit: per-bot robots.txt matrix, llms.txt presence, citability score 0-100 |
| `email_auth_check` | SPF/DKIM/DMARC/MX/BIMI/MTA-STS audit scored against Gmail/Yahoo/Microsoft bulk-sender rules |
| `gsc_list_sites` / `gsc_search_analytics` | Connected Google Search Console properties and query data |
| `mcp_tools` / `mcp_call` | Roster of the workspace's own connected MCP servers, and invocation of their tools |
| Linkedin/Google ads tools | Competitor ad research by domain or page id, with media-type and country filters |

Plus webhooks (signed, at-least-once delivery with test events), file attachments in chat surfaces, and per-run cost confirmations at the workspace threshold.

## Installation

```bash
astrofabric connect claude-code
```

The CLI prints the exact setup for claude-code, cursor, codex, gemini, vscode or windsurf. OAuth-capable clients paste the bare URL and walk through sign-in; non-header clients use the console-generated key-embedded URL.

## Configuration

```json
{
  "mcpServers": {
    "astrofabric": {
      "url": "https://www.astrofabric.ai/api/mcp?tools=all",
      "headers": {
        "Authorization": "Bearer ek_live_..."
      }
    }
  }
}
```

Keys carry scopes (e.g. `tools:site_audit`, `agents:*`) and per-minute rate limits; the secret is shown once and stored only as a hash.

## Business Relevance

- **Growth operators** run SEO, AI-visibility and deliverability audits as one objective instead of three subscriptions
- **Sales teams** get verified-email prospect lists delivered as CSV, with contacts written straight into HubSpot
- **Marketers** research competitor LinkedIn and Google ads by domain from the same thread they plan campaigns in
- **Agencies** inherit per-workspace memory (brand, ICP, competitors) so every mission starts informed

## Integration with CorpusIQ

AstroFabric's mission outputs land where CorpusIQ's connectors read. A mission that builds and verifies a prospect list can write contacts into HubSpot - which CorpusIQ already connects - so the pipeline appears in CorpusIQ's CRM analytics without manual import. SEO and AI-visibility audit results complement CorpusIQ's GA4 and Google Ads connectors: CorpusIQ answers "what traffic and spend did we actually see" while AstroFabric answers "what should we fix to get cited by AI engines". Together they form a measure-and-act loop for AI-era growth: AstroFabric proposes and executes, CorpusIQ's 40+ connectors verify the business impact.

## Limitations

- New listing, upgraded from a thin-docs skip only after endpoint verification - no public adoption track record yet
- Default MCP surface is a single tool; granular tools require the ?tools=all URL variant
- Metered cost model with per-run caps - objectives spend workspace credits
- Some tools require connected third-party accounts (Google Search Console, HubSpot)
- Growth-ops platform, not a raw data API - results arrive through the mission layer

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [1Lookup MCP - Phone, Email and IP Verification](/docs/hermes/mcp/servers/external/1lookup-mcp)
