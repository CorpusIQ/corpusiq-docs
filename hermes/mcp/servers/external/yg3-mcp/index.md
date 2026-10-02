---
title: "YG3 MCP - Marketing Operations for Autonomous Agents"
description: "Remote MCP server that puts content, SEO, outbound, LinkedIn, and Google Ads operations under agent control with 197 tools. Agents provision a sandbox workspace with one unauthenticated POST and get a bearer token back; humans connect with OAuth."
category: Marketing
stars: n/a (new listing, github.com/YG3-ai/yg3-mcp)
added: 2026-08-29
source: "mcp.so GitHub issue #3811"
relevance: ★★★
tags: [mcp-server, marketing, seo, linkedin, google-ads, outbound, content, remote-mcp]
---

# YG3 MCP

**Remote MCP server that hands a marketing operations platform to AI agents: content and SEO, outbound email, LinkedIn posting, and paid search, through 197 tools at mcp.yg3.ai.** The differentiator is the provisioning model - an autonomous agent posts one unauthenticated JSON call to create a sandbox workspace and receives a bearer token back, with no signup and no human in the loop. Humans with a YG3 account connect the same endpoint through OAuth. The live catalog endpoint (`/api/health`) confirms 197 tools, 15 resources, and 9 skills on server version 0.2.0 (protocol 2025-06-18).

```
Server type: Remote (Streamable HTTP), hosted
Auth: Bearer token (agent provisioning) or OAuth (human account)
Endpoint: https://mcp.yg3.ai/mcp
Provision: POST https://agency.yg3.ai/api/v1/workspaces (no auth; returns token, mcp_endpoint, claim_endpoint)
Health: https://mcp.yg3.ai/api/health (public; tool count, server version)
Tools: 197 (client snapshots, brand, blog content, LinkedIn, Google Ads PPC, outbound, approvals)
Pricing: Free sandbox tier (14-day expiry); paid tiers after claiming
Category: Marketing
Built by: YG3 (yg3.ai); repo github.com/YG3-ai/yg3-mcp, MIT, created Aug 28, 2026
```

## Why This Matters for Operators

Agency operators juggle the same loop every day: check how a client is doing, write the post, schedule the LinkedIn piece, watch the ads, catch the replies. YG3 moves that loop into a single agent-addressable surface. Instead of five dashboards, an assistant reads one client snapshot (traffic breakdown, wins report, competitor standing, at-risk clients, pending decisions) and acts on it: draft and publish a blog post, approve or reschedule a LinkedIn post, pause a losing PPC keyword, reply to an outbound lead.

The provisioning model is the operator-relevant part. A no-signup workspace means an agency can spin up a marketing sandbox for a new client from a CI job or an agent runtime in one call, build the site and voice profile, and only later hand it to a human owner through the claim endpoint. Unclaimed workspaces stay safely bounded - no ad spend, no email sends, no social posting, publishing only to a free subdomain - and expire in 14 days.

**One agent surface replaces the multi-dashboard marketing loop, and sandboxes are provisionable without human setup.**

## Tools & Capabilities

Tool names verified from the public health catalog and the repo's tool reference; anonymous enumeration is refused (401 confirmed live), so representative groups are shown.

| Tool group | Representative tools |
|---|---|
| Client intelligence | get_client_snapshot, get_client_wins_report, show_traffic_breakdown, list_clients, get_client, list_at_risk_clients, get_competitor_standing, add_competitor, get_daily_checkin |
| Brand and positioning | set_business_profile, set_brand, show_brand |
| Blog content | list_posts, create_post, edit_post, edit_carefully, publish_post, archive_post |
| LinkedIn | list_linkedin_posts, approve_linkedin_post, reject_linkedin_post, edit_linkedin_post, reschedule_linkedin_post, get_linkedin_post_metrics, get_linkedin_resonance, list_linkedin_comments, approve_linkedin_comment |
| Google Ads (PPC) | list_ppc_campaigns, list_ppc_budgets, get_ppc_performance, list_ppc_keywords, create_ppc_search_campaign, create_ppc_pmax_campaign, update_ppc_campaign_budget, pause_ppc_keyword, add_ppc_negative_keyword, add_ppc_location_target, add_ppc_sitelink, add_ppc_callout, set_ppc_conversion_tracking |
| Outbound | get_outbound_lead, list_leads, list_replies, get_reply, list_close_sessions, get_close_session |
| Human-approval rail | list_pending_decisions, list_comms_events, approve_comms_event, suppress_comms_event |
| Platform docs | read_platform_doc (getting-started, agent-integration, tools-reference) |

## Installation

Agent path (no account, no OAuth):

```bash
curl -s -X POST https://agency.yg3.ai/api/v1/workspaces \
  -H "Content-Type: application/json" \
  -d '{"domain":"acme.com","industry":"Plumbing","location":"Tampa, FL"}'
```

The response carries the workspace token, the MCP endpoint, and a claim endpoint. Attach the token as a bearer Authorization header on all MCP calls.

Human path (existing YG3 account):

```bash
claude mcp add --transport http yg3 https://mcp.yg3.ai/mcp
```

Then sign in when the browser OAuth flow opens. Setup guide: yg3.ai/connect.

## Configuration

```json
{
  "mcpServers": {
    "yg3": {
      "type": "http",
      "url": "https://mcp.yg3.ai/mcp",
      "headers": {
        "Authorization": "Bearer <workspace-token>"
      }
    }
  }
}
```

Unclaimed sandboxes are bounded: they build the site, voice, and articles and publish to a free blog subdomain, but cannot attach a custom domain, send email, spend on ads, or post to social. Unclaimed workspaces expire after 14 days; the claim endpoint (POST /api/v1/workspaces/claim with an email and password) converts one into a permanent human-owned account.

## Business Relevance

- **Agency operators** get one agent surface across client snapshots, content, LinkedIn, ads, and outbound - and can stand up a new-client sandbox with a single call.
- **Growth teams** run the brand profile, competitor tracking, and daily check-in loop without switching dashboards.
- **Marketing engineers** provision workspaces from CI or agent runtimes, then hand the owner credentials to humans only when the account is ready.
- **Autonomous agent fleets** get a marketing rail with a human-approval gate (pending decisions, comms events) instead of open write access.

## Integration with CorpusIQ

YG3 pairs with CorpusIQ's marketing and content stack rather than replacing it. CorpusIQ's social cadence engine and Postiz publishing handle organic distribution while YG3 MCP drives the paid and outbound layer: an agent can read campaign performance from YG3's PPC tools, compare it with GA4 signup attribution from CorpusIQ's connectors, and shift budget inside the same workflow. The client-snapshot tools give a CorpusIQ-driven ops loop a single read on account health (traffic, wins, competitors, at-risk clients) that feeds the weekly operator report. For agencies running CorpusIQ across multiple clients, the one-POST workspace provisioning matches CorpusIQ's multi-tenant connector model: one sandbox per client, claimable by the client's owner when the engagement starts.

## Limitations

- Brand new - the repo was created Aug 28, 2026 with no stars and no track record yet.
- The 197-tool surface is large; most tool names are only discoverable after connecting (the public health endpoint lists them, but anonymous calls are refused).
- Unclaimed sandboxes are deliberately capped: no ads spend, no email, no social, 14-day expiry.
- YG3 is a commercial platform; the long-term pricing model past the free sandbox tier is not yet published.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Askline MCP - AI Search Visibility and Brand Monitoring](/hermes/mcp/servers/external/askline-mcp)
- [AstroFabric MCP - Agentic Growth Missions for Operators](/hermes/mcp/servers/external/astrofabric-mcp)
- [Alison AI MCP - Ad Creative Performance Analytics](/hermes/mcp/servers/external/alison-ai-mcp)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
