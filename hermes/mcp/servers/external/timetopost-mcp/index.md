---
title: TimeToPost MCP - Social Scheduling with Draft Approval
description: "TimeToPost MCP lets agents draft, schedule, publish and cancel social posts, manage a human approval queue and read engagement metrics through the TimeToPost API, with AutoSEO content workflows included. Hosted Streamable HTTP endpoint with browser OAuth, plus a local stdio adapter; 30+ tools documented in the vendor README."
category: Social Media Management
stars: 0
added: 2026-09-07
source: "chatmcp/mcpso issue #3970"
relevance: ★★★
tags: [social-media, scheduling, approvals, autoseo, analytics, remote-mcp, oauth]
---

# TimeToPost MCP - Social Scheduling with Draft Approval and AutoSEO

**Remote MCP server (Streamable HTTP, browser OAuth; local stdio adapter)** - TimeToPost's official MCP server runs the whole social pipeline inside the agent: draft, schedule, publish, cancel, a human approval queue for drafts, engagement metrics, plus AutoSEO workflows that connect a site and generate SEO posts from topic proposals.

```
Server type: Remote (Streamable HTTP) with local stdio adapter (npm timetopost-mcp)
Auth: Browser OAuth against a TimeToPost account; API-token configuration documented
Endpoint: https://api.timetopost.co/mcp (probe-verified live; 401 unauthorized without auth)
Tools: 30+ (scheduling, drafts and approvals, boards and brands, engagement, AutoSEO)
Pricing: TimeToPost plans at timetopost.co
Category: Social Media Management
Built by: TimeToPost (timetopost.co); repo github.com/MelMayssonOwen/timetopost-mcp
```

## Why This Matters for Operators

Scheduling and publishing are half the job; the other half is knowing whether the content worked and feeding that back. TimeToPost MCP covers both directions in one tool surface: outbound posting with a draft-approval queue, and inbound engagement metrics with per-tag and optimal-time analysis - plus the AutoSEO half that turns a connected site into scheduled SEO content.

**The draft-first design is the control story: the agent prepares (create_drafts, create_digest_drafts), the human approves or rejects from the queue (approve_draft, reject_draft), and only approved drafts reach schedule and publish tools.**

## Tools & Capabilities

| Group | Tools |
|---|---|
| Scheduling and publishing | schedule_post, publish_post, cancel_post, publish_thread, scheduler_status |
| Drafts and approvals | create_drafts, create_digest_drafts, list_drafts, approve_draft, reject_draft, list_approvals |
| Boards and brands | list_boards, list_posts, get_post, list_brands |
| Engagement analytics | get_engagement_summary, get_optimal_times, get_post_metrics, get_engagement_by_tag |
| AutoSEO | autoseo_connect_site, autoseo_verify_site, autoseo_list_sites, autoseo_configure, autoseo_auto_configure, autoseo_propose_topics, autoseo_generate_post |
| Discovery | get_capabilities, list_integrations, get_tiktok_creator_info |

## Installation

Hosted: connect through the browser OAuth flow from any OAuth-capable MCP client. Local: npm install timetopost-mcp for the stdio adapter documented in the repo.

```json
{
  "mcpServers": {
    "timetopost": {
      "type": "http",
      "url": "https://api.timetopost.co/mcp"
    }
  }
}
```

## Configuration

OAuth clients complete the browser sign-in against the operator's TimeToPost account; the repo also documents API-token configuration for non-interactive setups. The endpoint probe confirms auth enforcement with a 401 unauthorized response.

## Business Relevance

- **Content teams** run draft-approval-publish loops inside the agent with an audit trail.
- **Growth teams** fold AutoSEO topic generation into the same tool that schedules socials.
- **Solo founders** combine scheduling, approval and metrics without stitching tools together.
- **Agencies** manage client boards and brands from one connector.

## Integration with CorpusIQ

TimeToPost schedules and measures the social layer; CorpusIQ measures the business layer. A composed workflow: the agent reads engagement summaries from TimeToPost, correlates them with conversions in CorpusIQ's GA4 and Stripe connectors, and uses the result to brief the next draft batch.

## Limitations

- Brand new listing (issue #3970, Sep 6, 2026); 0-star repo, MIT.
- Requires a TimeToPost account; the OAuth flow needs a browser-capable client.
- Tool names come from the vendor README (30+); the endpoint is auth-gated so anonymous enumeration is refused.

## See Also

- [PostNitro MCP - AI Carousels and Social Publishing for Agents](/hermes/mcp/servers/external/postnitro-mcp)
- [PurrPlan MCP - Agent-Driven Social Scheduling and Inbox](/hermes/mcp/servers/external/purrplan-mcp)
- [PostBazooka MCP - Social Publishing with Commit Proof](/hermes/mcp/servers/external/postbazooka-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
