---
title: "LoomaScale Google Ads MCP - Google Ads Management with Guardrails"
description: "LoomaScale's Google Ads MCP server puts account management inside any MCP client: 42 tools over the Google Ads API for performance reads, keyword research, campaign and Performance Max creation, and budget or bidding changes, with spend caps, per-tool daily limits and a no-silent-activation design so a model cannot enable a campaign without passing the cap check."
category: Marketing
stars: 0
added: 2026-09-07
source: mcp.so feed
relevance: ★★★
tags: [google-ads, ppc, marketing, remote-mcp, oauth, self-hosted, spend-guardrails]
---

# LoomaScale Google Ads MCP - Google Ads Management with Guardrails

**Remote MCP server (Streamable HTTP, hosted at api.loomascale.com/mcp; MIT self-host option)** - LoomaScale's MCP connector is the engine behind an AI operator for Google Ads that has run live campaigns from inside ChatGPT since 2026. The same tools are published under MIT for self-hosting, so an agent can read performance, research keywords, create campaigns and change budgets with guardrails the model cannot talk its way past.

```
Server type: Remote (Streamable HTTP) or self-hosted (docker compose, MIT)
Auth: Hosted: OAuth connector flow via ai.loomascale.com; self-hosted: local consent screen + developer token
Endpoint: https://api.loomascale.com/mcp (hosted; probe-verified live, auth-gated)
Tools: 42 over the Google Ads API
Pricing: Free Google Ads waste audit to start; plans at ai.loomascale.com/pricing
Category: Marketing
Built by: LoomaScale (ai.loomascale.com); repo github.com/loomascale/ads-mcp
```

## Why This Matters for Operators

Google Ads accounts bleed money through stale keywords, wasted search terms and campaigns that drift from their targets. The human loop of pulling reports, exporting to a spreadsheet and re-keying changes into the Ads UI is slow, so the fixes happen late. LoomaScale MCP lets the agent read the account, find the waste and make the change in one conversation.

**The safety model is the product differentiator: campaign creation has no status field in its schema, activation is a separate tool, and only campaigns the server itself created can be activated - so a model can never silently push a campaign live, and every budget change is checked against an operator-set cap and refused rather than clamped.**

## Tools & Capabilities

| Group | What the agent does |
|---|---|
| Performance reads | Lists campaigns, ads, keywords, search terms, conversion actions, sitelinks and asset groups; pulls insights, pacing and billing checks |
| Keyword research | keyword_ideas, find_locations, get_audience_insights and get_geo_insights for account-specific research |
| Campaign building | create_campaign, create_ad_group, create_ad, create_pmax_campaign with full settings, targeting, negatives and conversion-goal controls |
| Budget and bidding | update_budget, update_campaign_bidding, update_account_budget and pacing checks against operator-set caps |
| Activation and status | set_status and activate_campaign, gated so only server-created campaigns with a checked budget can go live |

## Installation

Hosted: connect through the LoomaScale connector at ai.loomascale.com and point any Streamable HTTP client at https://api.loomascale.com/mcp. Self-hosted: download the docker-compose file from the repo, set the values in .env, and start with MCP_DEFAULT_MAX_DAILY_BUDGET_CENTS set low before pointing it at a live account. Full prerequisites, including the Google Ads developer token application, are in the repo's google-ads README.

```bash
curl -O https://raw.githubusercontent.com/loomascale/ads-mcp/main/docker-compose.yml
curl -O https://raw.githubusercontent.com/loomascale/ads-mcp/main/.env.example
cp .env.example .env
docker compose up
```

## Configuration

```json
{
  "mcpServers": {
    "loomascale": {
      "type": "http",
      "url": "https://api.loomascale.com/mcp"
    }
  }
}
```

Credentials are encrypted at rest with AES-256-GCM; authorization codes and refresh tokens are stored hashed and are single-use; model-supplied URLs pass an SSRF policy; tool arguments are never logged. Per-tool daily limits and a runaway-loop guard stop a stuck model from making hundreds of changes.

## Business Relevance

- **Performance marketers** get waste audits, keyword research and campaign changes inside the agent workflow instead of the Ads UI.
- **Agencies** can self-host one server per client account with per-account caps, keeping spend control with the account manager.
- **Founders** running their own ads get a free waste audit before paying anything, then the hosted plan.
- **RevOps teams** get pacing and billing checks the agent can act on without exporting reports.

## Integration with CorpusIQ

LoomaScale acts on spend; CorpusIQ measures revenue. A composed workflow: CorpusIQ connectors (Stripe, GA4, Shopify) show which campaigns converted into paying customers, and the LoomaScale agent then shifts budget, pauses losers or writes new ad groups in the same session. The two systems share the same operator-safe posture: CorpusIQ connectors are read-only, and LoomaScale refuses silent activations.

## Limitations

- Brand new listing (mcp.so feed, Sep 7, 2026); repo has 0 stars, MIT.
- Self-hosting requires a Google Ads developer token, which takes days to approve.
- Single-operator by default in the open-source build; multi-user dashboard is the hosted product's commercial half.
- Tool names come from the repo's google-ads README (42 tools); the hosted endpoint is auth-gated, so anonymous enumeration is refused.

## See Also

- [Ryze Google Ads MCP - Hosted Ads Reporting for Agents](/docs/hermes/mcp/servers/external/ryze-google-ads-mcp)
- [TrueClicks MCP - PPC Audit Intelligence for Agents](/docs/hermes/mcp/servers/external/trueclicks-mcp)
- [AdPlug LinkedIn Ads MCP - B2B Campaign Control for Agents](/docs/hermes/mcp/servers/external/adplug-linkedin-ads-mcp)
- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
