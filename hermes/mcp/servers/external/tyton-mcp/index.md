---
title: Tyton MCP - Meta Pixel and Conversions API Audits
description: "Tyton audits a Meta Pixel and Conversions API setup, finds the break and installs the fix with the agent."
category: Marketing
stars: n/a (new listing)
added: 2026-09-27
source: "mcp.so server page (usetyton.com)"
relevance: ★★★
tags: [meta-pixel, conversions-api, tracking-audit, meta-ads, deduplication, marketing-analytics, remote-mcp]
---

# Tyton MCP

**The Meta tracking audit an agent can run and fix in one conversation.** Tyton is a Meta tracking MCP that audits a site's Meta Pixel and Conversions API setup, finds the break, and installs the fix with the AI agent. The audit is free and needs no Tyton account; an account is only needed when the operator wants the working setup. Tyton provides the server gateway that receives the browser pixel and the server events, then sends them to Meta through the Conversions API deduplicated so the same conversion is counted once.

```
Server type: Remote
Auth: none for the free audit (account for the installed setup)
Endpoint: https://mcp.usetyton.com/audit
Tools: pixel and CAPI audit, install, deduplication setup
Pricing: audit free; working setup requires a Tyton account
Category: Marketing / Meta Ads
Built by: Tyton (usetyton.com)
```

## Why This Matters for Operators

Broken Meta tracking is expensive in a specific, silent way: ad spend keeps flowing while conversion data undercounts or double-counts, and optimization runs on garbage. The traditional fix is a specialist call that costs money and calendar time. Tyton's MCP lets the operator's own agent run the audit, explain what is broken, and then install the pixel, the server events and the deduplication with the agent doing the setup on the site.

The guardrail is sensible: the agent walks the operator through the Meta screens (business, dataset, website, Conversions API token, test events) and does not sign in to Meta on anyone's behalf.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Audit | Free audit of Pixel and CAPI setup, no account required |
| Fix | Agent installs pixel, server events and deduplication |
| Gateway | Tyton-hosted server receives browser pixel and server events |
| Deduplication | Same conversion counted once through the Conversions API |
| Walkthrough | Agent guides the Meta screens without signing in for the operator |

## Installation

```json
{
  "mcpServers": {
    "tyton": {
      "url": "https://mcp.usetyton.com/audit"
    }
  }
}
```

Connect the server to any MCP-compatible client and start with a free audit of the site.

## Configuration

```bash
claude mcp add tyton https://mcp.usetyton.com/audit
```

## Business Relevance

- **Performance marketers** verify tracking before scaling spend
- **E-commerce operators** fix undercounted or double-counted conversions
- **Agencies** run client tracking audits without a specialist retainer
- **Founders** get a clean CAPI setup without building the gateway

## Integration with CorpusIQ

Tyton pairs with CorpusIQ's Meta Ads connector: clean Pixel and CAPI data improves the conversions Meta reports, and CorpusIQ reads that performance through facebook campaign insights for recaps. Cross-source ads analysis in CorpusIQ can compare Google Ads spend against Meta and GA4 sessions with more trustworthy conversion signals once Tyton's deduplication is in place.

## Limitations

- The agent does not sign in to Meta; operator completes the Meta screens
- Working setup requires a Tyton account
- Scope is Meta tracking; other ad platforms are out of scope
- New listing; long-term reliability unproven

## FAQ

### Is the audit really free?

Yes. The audit needs no Tyton account; an account is only needed to install the working setup.

### Does the agent sign into Meta?

No. The agent walks the operator through the Meta screens and never signs in on anyone's behalf.

### What does the gateway do?

Receives the browser pixel and server events, then sends them to Meta through the Conversions API deduplicated.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
