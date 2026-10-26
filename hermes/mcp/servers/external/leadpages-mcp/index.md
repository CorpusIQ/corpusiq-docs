---
title: "Leadpages MCP - Pages, Sites, Blogs and Ads by OAuth"
description: "Leadpages' own remote MCP server at mcp.leadpages.com, with OAuth scopes for pages, sites, blogs and ads so an agent can build and publish marketing work."
category: Marketing / Landing Pages
stars: n/a (commercial, OAuth required)
added: 2026-10-25
source: "mcp.so feed card 2026-10-26T01:38:44Z + live probes on mcp.leadpages.com (401 on initialize and tools/list) + RFC 9728 protected resource and authorization server metadata + mcp.so listing categories"
relevance: ★★★
tags: [leadpages, landing-pages, marketing, oauth, websites, blogs, ads, publishing, conversion]
last_updated: "2026-10-25"
---

# Leadpages MCP

**A martech vendor opening its own production surface to agents, not a wrapper around it.** Leadpages sells landing pages, sites, blogs and ad campaigns to small businesses. This server exposes those four objects over OAuth instead of asking an operator to copy work out of a chat window and into a builder.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.leadpages.com/mcp
Transport:   JSON-RPC 2.0 over HTTP
Auth:        OAuth 2.1 authorization code with dynamic client registration
Scopes:      pages:read, pages:write, sites:read, sites:write,
             blogs:read, blogs:write, ads:read, ads:write
Built by:    Leadpages (leadpages.com)
Registry:    not listed in the official MCP registry
```

## Why This Matters for Operators

The landing page is where a paid campaign either pays back or does not. The work around it is repetitive: change the headline, duplicate the page for a new audience, publish, then check whether the ad copy still matches the page.

An assistant that can read and write those objects closes the loop. Ask which pages exist for a campaign, get the list, rewrite the one that underperforms, publish it, and keep the change inside the account's own permissions rather than in a screenshot and a to-do note.

## What It Actually Runs On

The connection is gated, and that gate is the evidence. Both `initialize` and `tools/list` on `https://mcp.leadpages.com/mcp` returned HTTP 401 `{"error":"Unauthorized"}` without a token, so this is a live production endpoint rather than a documented shell.

What it exposes is published in its own discovery documents, which is the part worth reading.

`https://mcp.leadpages.com/.well-known/oauth-protected-resource` returned the resource `https://mcp.leadpages.com/mcp`, a single authorization server at `https://mcp.leadpages.com`, bearer tokens in a header, and eight scopes: `pages:read`, `pages:write`, `sites:read`, `sites:write`, `blogs:read`, `blogs:write`, `ads:read`, `ads:write`.

`https://mcp.leadpages.com/.well-known/oauth-authorization-server` returned issuer `https://mcp.leadpages.com`, an authorization endpoint at `https://leadpages.com/api/mcp/oauth/authorize`, a token endpoint and a registration endpoint on the MCP host, `response_types_supported: ["code"]`, and grants for `authorization_code` and `refresh_token`.

Those eight scopes are the feature list: four object families, each with a read side and a write side. Anything an operator does in the builder appears in that set, and nothing outside it is claimed.

The mcp.so listing classifies the server as AI Landing Page Builder, Marketing Automation, Lead Generation, Website Builder and Conversion Rate Optimization, and states that it requires authentication and has no published tool list yet, which matches the 401 reading rather than contradicting it.

## What Was Not Verifiable

- **The tool list.** Discovery needs a signed-in account, so the exact tool names and arguments were not read in this sweep. The scopes are the vendor's own claim about capability; the schemas are not.
- **Pricing.** The server sits inside a Leadpages subscription. No separate MCP fee is published, and none is assumed here.
- **Registry presence.** Searches of the official MCP registry for `leadpages` returned nothing, so this connection comes from the vendor's own endpoint and not from a registry listing.
- **Relationship to the earlier entry.** This catalog already carries HTML Pub at `mcp.htmlpub.com/mcp`, an HTML publishing endpoint attributed to Leadpages. That is a narrow publishing surface. `mcp.leadpages.com` is the product's own MCP host, with sites, blogs and ads behind it, so the two are different servers rather than a replacement.

## FAQ

### What can an agent do once it is connected?
Read and write pages, sites, blogs and ads, bounded by the eight scopes the server publishes. An account that grants only read scopes gives an assistant a research surface; write scopes give it the builder.

### How does the connection get authorised?
OAuth authorization code against `https://leadpages.com/api/mcp/oauth/authorize`, with dynamic client registration at `https://mcp.leadpages.com/api/mcp/oauth/register`, so a client can register itself instead of waiting for a manual app review.

### Is this the same server as HTML Pub?
No. HTML Pub publishes a single generated HTML page to a URL on your domain. This server works on Leadpages objects: pages, sites, blogs and ad campaigns. Both are Leadpages properties; only one of them can edit a site.

### Does adding it let the agent spend ad budget?
The `ads:write` scope means the agent can write to ad objects through this server. Whether a campaign can be launched or a budget changed is decided inside Leadpages by the permissions of the account that approved the connection, so the grant is the place to be careful.

## The Operator Test

Connect it read-only first and ask which landing pages exist per campaign and which ones have not been touched since launch. That answer alone justifies the connection, because stale pages behind live spend are the cheapest revenue leak in small business marketing.
