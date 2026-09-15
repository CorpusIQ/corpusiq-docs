---
title: "GrowSurf MCP - Referral and Affiliate Program Operations"
description: "Official GrowSurf MCP server that lets an AI assistant create referral and affiliate programs, configure rewards, install tracking, manage participants, and read analytics through safe REST API wrappers. npm package plus a hosted remote connector at mcp.growsurf.com."
category: Marketing
stars: n/a (new listing, github.com/GrowSurf/growsurf-mcp)
added: 2026-08-29
source: mcpservers.org /all page 1
relevance: ★★★
tags: [mcp-server, referral-marketing, affiliate, growth, rewards, webhooks, analytics, remote-mcp]
---

# GrowSurf MCP

**The official GrowSurf MCP server puts referral and affiliate program operations under agent control: create programs, configure rewards, install tracking, manage participants, and read campaign analytics through guided REST API wrappers.** GrowSurf is an established referral-marketing platform, and this server is its vendor-built integration surface - it ships as an npm package for local stdio clients and as a hosted remote connector at mcp.growsurf.com for browser-only assistants. The wrappers steer the agent through the safe path (guided integration steps, starter content review, preview screenshots) instead of exposing the raw API.

```
Server type: stdio (npm) and hosted remote (Streamable HTTP)
Auth: GrowSurf API key (created from the assistant, no existing credentials needed)
Endpoint: https://mcp.growsurf.com (hosted); npx @growsurfteam/growsurf-mcp (local)
Tools: REST wrappers over accounts, teams, campaigns, programs, rewards, config, webhooks, analytics
Pricing: GrowSurf platform plans (free trial via growsurf.com); the MCP server itself is open source
Category: Marketing / Growth
Built by: GrowSurf (growsurf.com); repo github.com/GrowSurf/growsurf-mcp
```

## Why This Matters for Operators

Referral programs are the highest-leverage growth channel most operators under-invest in, because standing one up means integrating tracking, configuring rewards, wiring webhooks, and reading analytics across a SaaS dashboard. GrowSurf MCP moves that whole loop into conversation: an agent can create a campaign, set reward rules, install the tracking snippet or SDK, add participants, and pull analytics (totals, time series, email metrics, status counts, and rates) with plain-language prompts.

The guided-integration design is what makes it operator-safe. The server ships agent recipes and an installable skill bundle that walk through the universal code install, iOS/Android SDK guidance, signup and qualifying-action flows, affiliate sale tracking, and webhooks - and it steers review of starter design, emails, options, and installation content before patching anything. One-shot program-creation evals with acceptance checks mean an assistant proposes a complete program and the operator approves the diff.

**Referral and affiliate programs become a conversational workflow with review gates, not a dashboard project.**

## Tools & Capabilities

Capability-level from the repo's documented wrapper surface (exact tool names are discovered after connecting).

| Tool group | Capability |
|---|---|
| Account and team | Create an account and get an API key with no existing credentials; read and rename the bound team; request team verification |
| Campaigns | List and get campaigns; create, update, and clone programs; read campaign analytics (totals, optional per-period time series, email metrics, previous-period totals, status counts, rates) |
| Rewards | List, create, update, and delete campaign rewards |
| Program config | Get and update Design, Emails, Options, and Installation config |
| Webhooks | List, create, update, delete, and test program webhooks |
| Visual proof | Capture temporary GrowSurf preview screenshots when explicitly asked |

## Installation

Local stdio (Claude Code, Cursor, Codex, any MCP client that runs a local server):

```bash
claude mcp add growsurf -- npx -y @growsurfteam/growsurf-mcp
```

Browser-only assistants (ChatGPT, Claude web, Claude Desktop) use the hosted remote connector at https://mcp.growsurf.com instead. Full per-client setup: docs.growsurf.com/build-with-ai.

## Configuration

The assistant creates the account and API key itself on first run - no pre-existing credentials required. The key binds the MCP session to your GrowSurf team and is the same key used with the GrowSurf REST API.

```json
{
  "mcpServers": {
    "growsurf": {
      "command": "npx",
      "args": ["-y", "@growsurfteam/growsurf-mcp"],
      "env": { "GROWSURF_API_KEY": "key-from-growsurf-dashboard" }
    }
  }
}
```

## Business Relevance

- **Growth operators** stand up referral and affiliate programs from chat and iterate rewards without touching the dashboard.
- **E-commerce and SaaS founders** get the tracking install (universal code, SDKs, GrowSurf Window) handled as a guided flow with review gates.
- **Agencies** clone proven program templates across clients and read analytics per campaign without login-switching.
- **Agent fleets** wire webhooks and participant management into automated referral ops with the API-key path.

## Integration with CorpusIQ

GrowSurf MCP complements CorpusIQ's growth surface directly: CorpusIQ already runs affiliate and creator outreach (Dub and Whop workflows, creator contact verification), and GrowSurf adds the program mechanics those partnerships need - campaign creation, reward configuration, participant tracking, and analytics. A CorpusIQ-driven workflow can read referral attribution from GrowSurf's analytics wrappers, match it against signup attribution in GA4 and Stripe revenue from CorpusIQ connectors, and decide which affiliate rewards to adjust. The webhook tools let CorpusIQ's inbound-communication monitoring subscribe to referral events the same way it does email and social signals.

## Limitations

- New listing with no stars; the server is vendor-maintained but young.
- The npm package is a wrapper layer - deep customization still lands in the GrowSurf dashboard.
- Platform plans and reward payouts are GrowSurf's commercial territory; the MCP server removes the plumbing, not the cost.
- Campaign data lives in GrowSurf's cloud - no self-host option.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Alison AI MCP - AI Marketing Copywriting](/docs/hermes/mcp/servers/external/alison-ai-mcp)
- [n8n MCP Server - Workflow Automation](/docs/hermes/mcp/servers/external/n8n-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
