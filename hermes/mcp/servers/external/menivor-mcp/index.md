---
title: "Menivor MCP - AI Video Ads and Reels for Agents"
description: "Menivor lets an AI agent write vertical reels and product video ads, check costs first, then schedule posts and read performance."
category: Marketing
stars: n/a (new listing)
added: 2026-09-28
source: "mcpservers.org server page (menivor.com)"
relevance: ★★
tags: [video-ads, reels, video-marketing, content-creation, social-video, marketing, remote-mcp]
---

# Menivor MCP

**Short vertical video ads produced inside your agent workflow.** Menivor runs a remote MCP server that lets an AI assistant write a reel, turn a product page into ads, check what a render will cost before committing, schedule the post and read performance back.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer API key (minted at menivor.com/account/api-keys)
Endpoint: https://menivor.com/api/mcp
Tools: reel writing, product-to-ad conversion, cost checks, scheduling, performance
Pricing: vendor pricing (menivor.com)
Category: Marketing / Video
Built by: Menivor (menivor.com)
```

## Why This Matters for Operators

Video ads are the highest-leverage format operators skip because production is slow: write a script, source footage, edit, render, schedule. Menivor collapses that into prompts the agent already knows how to write, with one unusual safeguard: the agent checks the price of a render before it commits, so a speculative creative test cannot silently burn budget.

The manifest at menivor.com/server.json keeps registry integrations honest, and the Bearer key model means no browser OAuth dance for scripted pipelines.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Reel writing | Draft vertical video scripts for short-form platforms |
| Product-to-ad | Turn a product page into ad creative |
| Cost checks | Quote a render before committing |
| Scheduling | Schedule finished posts from the agent |
| Performance | Read back post performance |

Tool names are served from the endpoint; the table reflects the vendor's published capability set.

## Installation

```bash
claude mcp add --transport http menivor https://menivor.com/api/mcp \
  --header "Authorization: Bearer YOUR_MENIVOR_API_KEY"
```

A registry manifest is published at menivor.com/server.json and Cursor config examples are on the server page.

## Configuration

```json
{
  "mcpServers": {
    "menivor": {
      "url": "https://menivor.com/api/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_MENIVOR_API_KEY"
      }
    }
  }
}
```

## Business Relevance

- **E-commerce operators** turn product pages into video ads without an editor
- **Marketing teams** test reels with cost quotes before committing budget
- **Agencies** schedule client video posts from agent workflows
- **Content operators** read performance back into the same session

## Integration with CorpusIQ

Menivor fits the content leg of a CorpusIQ-driven growth stack. Product feeds from the Shopify connector become ad source material, Meta Ads and Google Ads connectors measure what the ads produce, and GA4 closes the loop on landing behavior.

An operator can run the full cycle in one agent session: pull best sellers from Shopify, brief Menivor creative, approve the quoted cost, schedule, then compare Meta Ads spend against revenue.

## Limitations

- New listing, no track record yet
- Tool names are not published; live catalog is served from the endpoint
- Video renders are paid per use with undisclosed pricing
- No self-host option disclosed

## FAQ

### How is the cost handled?

The agent quotes the render cost first, so you approve spend before anything is produced.

### What platforms does it target?

Short vertical formats for reels-style distribution; scheduling details are vendor-specific.

### Do I need a browser login for scripts?

No. You mint a Bearer key at menivor.com/account/api-keys and pass it as an authorization header.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
