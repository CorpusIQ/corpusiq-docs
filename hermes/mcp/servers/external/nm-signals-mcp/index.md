---
title: "NM Signals MCP - AI Crawler Visibility Audits"
description: "NM Signals audits any URL's AI crawler access from an MCP client, with a bounded audit, fix and verification workflow for coding agents."
category: SEO
stars: n/a (new listing)
added: 2026-09-29
source: "mcpservers.org server page (app.nyman.media)"
relevance: ★★★
tags: [seo, aeo, geo, ai-crawlers, audit, llms-txt, remote-mcp]
---

# NM Signals MCP

**Audit any URL's AI crawler access in three lines.** NM Signals exposes an MCP server at /api/mcp with two tools - audit_url and get_quota - so an assistant can check how AI crawlers see a site and whether the site is visible to AI answers, from Claude Desktop, Cursor or any MCP client.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer key (nms_live_ production keys)
Endpoint: https://app.nyman.media/api/mcp
Tools: audit_url, get_quota
Pricing: API access requires Premium or Partner plan
Category: SEO
Built by: Nyman Media (nyman.media)
```

## Why This Matters for Operators

AI search engines and assistants are now a material traffic channel, and the failure mode is silent: a site that ranks fine on Google can be invisible to ChatGPT, Perplexity and their crawlers, and the operator never sees a warning. NM Signals turns that blind spot into a two-tool audit an assistant can run on demand.

The vendor's designed workflow pairs the MCP server with a coding agent: the agent runs the audit, inspects the codebase for every actionable finding, makes the smallest safe fix and re-runs the audit, summarizing anything that needs content, infrastructure or human review instead. That makes AI-crawler visibility a routine check rather than a quarterly project.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| audit_url | Audit a webpage's AI crawler access and visibility, returning evidence for the agent workflow |
| get_quota | Check remaining audit quota on the account |

Tool names and behavior come from the vendor's published MCP documentation.

## Installation

```bash
claude mcp add nyman-media --transport http https://app.nyman.media/api/mcp --header "Authorization: Bearer nms_live_..."
```

Get the key from Account settings, then API access on the web app. Premium or Partner plan required; production keys start with nms_live_.

## Configuration

```json
{
  "mcpServers": {
    "nyman-media": {
      "type": "http",
      "url": "https://app.nyman.media/api/mcp",
      "headers": {
        "Authorization": "Bearer nms_live_..."
      }
    }
  }
}
```

## Business Relevance

- **Operators of content and commerce sites** verify their pages are visible to AI crawlers before a traffic channel silently disappears
- **Agencies** run audits across client sites from one MCP connection with the same key and billing
- **SEO teams** pair the audit with a coding agent for bounded fix-and-verify loops
- **Marketing leads** get evidence-backed answers to the question of whether the brand appears in AI answers

## Integration with CorpusIQ

NM Signals audits the visibility layer while CorpusIQ answers the business question underneath. An assistant can run an AI-crawler audit on a page, then pull Search Console traffic, GA4 sessions and revenue through CorpusIQ connectors to show what AI visibility actually converts to - the audit finds the gap, and the CorpusIQ data proves whether it matters.

## Limitations

- Brand new listing, no track record yet
- API access gated behind Premium or Partner plans; pricing tiers not published on the listing
- Two-tool surface: audits and quota only, fixes happen in the coding agent
- Audit evidence covers the crawler-access layer, not full SEO scoring

## FAQ

### What exactly does it audit?

An audit_url call checks a webpage's AI crawler access and AI visibility, returning the evidence a coding agent needs to fix issues, then re-runs the audit to verify.

### What plan do I need?

API access requires a Premium or Partner plan on the web app. Production keys start with nms_live_; localhost and preview keys start with nms_test_.

### How do coding agents use it?

The vendor's workflow gives the agent a bounded loop: audit a URL, inspect the codebase for each actionable finding, make the smallest safe fix, and re-run the audit, summarizing anything that needs human review.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
