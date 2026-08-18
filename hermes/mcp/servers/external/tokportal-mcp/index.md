---
title: "TokPortal MCP - CorpusIQ Docs - CorpusIQ Docs"
description: "Managed social infrastructure API for AI agents - real TikTok, Instagram and YouTube accounts created, warmed and operated by human account managers in 16+ countries, exposed through 91 MCP tools"
category: Marketing
stars: "n/a (new listing)"
added: 2026-08-18
source: "mcp.so GitHub issue #3625"
relevance: ★★★
tags: [social-media, tiktok, instagram, youtube, video-posting, managed-accounts, scheduling, analytics, marketing, remote-mcp]
---

# TokPortal MCP

**Managed social infrastructure API: real TikTok, Instagram and YouTube accounts created, warmed and operated by human account managers in 16+ countries, exposed as a REST API and an MCP server with 91 tools.** Create bundles of accounts and videos, upload and schedule videos at scale, retrieve delivered accounts, read cross-account analytics, follow the ban lifecycle and register webhooks — all from an agent, with no per-account OAuth, no 25-posts/day cap and no app review. Tools carry MCP annotations (`readOnlyHint`, `destructiveHint`, `idempotentHint`).

```
Server type: Remote (Streamable HTTP) or stdio via npm
Auth: OAuth 2.1 (browser sign-in) or Bearer API key (sk_...)
Endpoint: https://app.tokportal.com/api/ext/mcp
Install (stdio): npx -y tokportal-mcp with TOKPORTAL_API_KEY env
Tools: 91 across accounts, videos, scheduling, analytics, bans, webhooks
Pricing: credit-based (per account and per video); size costs with tokportal_get_credit_costs
License: MIT (client/server repo); commercial managed-account API
Category: Marketing / social infrastructure
Built by: TokPortal (tokportal.com) — registry com.tokportal/mcp
```

## Why This Matters for Operators

Social distribution at scale is the operator problem no scheduling tool solves. Postiz-class schedulers move content between your existing accounts; TokPortal sits one layer lower — it provisions the accounts themselves. Human account managers in 16+ countries create, warm and operate real accounts, so an agent can order a geo-targeted bundle (say, ten US TikTok accounts) and receive working credentials, then push video content across the bundle through the same API.

**The ban lifecycle is the honest feature.** Multi-account operations get flagged; TokPortal exposes that lifecycle as tools instead of leaving you blind — watch for bans, handle replacements, and let webhooks notify the agent when an account dies. For growth operators running dozens of accounts across markets, that visibility is the difference between a controlled channel and a pile of dead profiles.

## Tools & Capabilities

The 91 tools mirror the public REST API. Groups:

| Group | What it covers |
|---|---|
| Account bundles | Create geo-targeted bundles of accounts, retrieve delivered accounts and credentials |
| Video uploads | Upload, configure and schedule videos at scale across accounts |
| Analytics | Cross-account performance reads |
| Ban lifecycle | Track and handle platform bans on accounts |
| Webhooks | Register endpoints for account and video events |
| Credits | `tokportal_get_credit_costs` sizes any order before spending |

Remote transport (OAuth 2.1) is the default for claude.ai, ChatGPT, Cursor, VS Code, Codex, Gemini CLI and n8n; stdio via `npx -y tokportal-mcp` with a `TOKPORTAL_API_KEY` covers local hosts.

## Installation

Remote (recommended for hosted agents):

```bash
claude mcp add --transport http tokportal https://app.tokportal.com/api/ext/mcp
```

Then run `/mcp` inside Claude Code and authenticate in the browser. Local stdio alternative:

```bash
claude mcp add tokportal -e TOKPORTAL_API_KEY=sk_... -- npx -y tokportal-mcp
```

Cursor JSON (global `~/.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "tokportal": {
      "url": "https://app.tokportal.com/api/ext/mcp"
    }
  }
}
```

## Configuration

| Variable | Required | Description |
|---|---|---|
| OAuth 2.1 flow | remote mode | Browser sign-in; choose Full access or Read-only per connector |
| `TOKPORTAL_API_KEY` | stdio mode | API key from app.tokportal.com/developer/api-keys, `sk_` prefix |

Rate limit is 120 requests/minute per key; `RATE_LIMIT_EXCEEDED` responses carry `diagnostics.retry_after_seconds`.

## Business Relevance

- **Growth teams** run multi-market account fleets without an agency retainer per country
- **E-commerce operators** push product videos across dozens of accounts on one credit meter
- **Agencies** deliver "we run your social at scale" as an API-connected service
- **Automation operators** close the loop with webhooks feeding account and video events back into their stack

## Integration with CorpusIQ

CorpusIQ's 40+ connectors cover the measurement side of marketing — ad spend, store revenue, email, analytics. TokPortal covers the distribution side CorpusIQ does not: managed accounts and at-scale video publishing on TikTok, Instagram and YouTube. Composed, TokPortal answers "which accounts posted and which got banned" while CorpusIQ answers "what did those posts and campaigns actually earn" from GA4, Shopify and ad connectors — distribution and attribution in one agent session.

## Limitations

- Commercial credit-based pricing; no published free tier (per-request cost estimation via `tokportal_get_credit_costs`)
- Managed-account model carries platform ToS risk; ban lifecycle tooling exists precisely because platforms ban accounts — budget for churn
- New listing (repo created Aug 18, 2026); MIT license on the client, but the managed-account API is the paid product
- 16+ country coverage, but not all platforms in all countries — confirm geo coverage for your target market before ordering bundles
