---
title: "micm.mx MCP - Spanish Posts With a Confirm Step"
description: "Spanish-first social scheduling for small businesses: an assistant drafts Instagram, Facebook and LinkedIn posts, the owner confirms."
category: Marketing
stars: ★★★ (401 + OAuth protected-resource verified)
added: 2026-10-29
source: "live probe of https://mcp.micm.mx/mcp answering HTTP 401, and its protected-resource document at /.well-known/oauth-protected-resource/mcp advertising three scopes, posts:read, metrics:read and posts:write; connector documentation at https://micm.mx/mcp updated 29 October 2026"
relevance: ★★★
tags: [social-media, scheduling, small-business, spanish, oauth, remote-mcp]
last_updated: "2026-10-29"
---

# micm.mx MCP

**Social scheduling tools are built for agencies and sold to small businesses, which is why so many of them sit unused. The one thing a shop owner needs is to see the post before it goes out.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.micm.mx/mcp
Auth:        OAuth 2.1 with PKCE
Discovery:   https://mcp.micm.mx/.well-known/oauth-protected-resource/mcp
Scopes:      posts:read, metrics:read, posts:write
Networks:    Instagram, Facebook, LinkedIn
Language:    Spanish
```

## Why This Matters for Operators

The scope list is the most informative part of this server. Three scopes, each naming a surface, and the third one is a write that schedules rather than a write that publishes: the documented flow is that the owner always confirms before something is scheduled.

That confirmation step is the difference between a tool a small business will use and one it will abandon. A restaurant owner will accept an assistant drafting a post about a new menu. That same owner will not accept a post appearing under the shop's name without them seeing it.

The audience is explicit: micm.mx is a Mexican platform for small businesses, and the connector is documented in Spanish, for Instagram, Facebook and LinkedIn. Metrics are their own scope (`metrics:read`) rather than being folded into post reads, which is the right separation for an owner who wants to know what worked without letting the assistant touch what goes out.

For an operator running several locations in a Spanish-speaking market, the practical value is the language. Asking for next week's posts in Spanish, with the platform's own tone, is a different task from translating English output, and it is the task this connector is built around.

## What Was Verified

A bare `initialize` POST to `https://mcp.micm.mx/mcp` returned **HTTP 401**.

The protected-resource document at `https://mcp.micm.mx/.well-known/oauth-protected-resource/mcp` returned **HTTP 200** with resource `https://mcp.micm.mx/mcp`, authorization server `https://mcp.micm.mx`, `resource_name` micm.mx MCP, bearer methods supported in the header, and exactly three scopes: `posts:read`, `metrics:read`, `posts:write`.

The connector documentation at `https://micm.mx/mcp` returned **200** through the reader proxy with a published timestamp of **29 October 2026**, states PKCE OAuth with no API keys required, presents the endpoint as the same URL for every assistant that can connect today, and states that the owner always confirms before anything is scheduled.

## Limits Worth Recording

The surface is credential gated, so no tool inventory was read this pass. The three scopes are the observed contract.

Three networks only: Instagram, Facebook and LinkedIn. No TikTok, no X, no YouTube.

The documentation is Spanish-only, and so is the product. An English-speaking operator can connect it but will be reading the docs through a translator.

Confirming before scheduling is documented behaviour, not an enforced guarantee this pass. Verify the confirmation step on the first scheduled post.

## FAQ

### What is the endpoint?

`https://mcp.micm.mx/mcp`, with OAuth discovery on the same host at `/.well-known/oauth-protected-resource/mcp`.

### Do I need API keys?

No. The connector uses OAuth 2.1 with PKCE and the documentation says no API keys are required, with access revocable at any time.

### Which networks are supported?

Instagram, Facebook and LinkedIn, with post metrics available under a separate read scope.

## See Also

- [Marketing servers in this catalogue](/hermes/mcp/servers/external/)
- [Connecting CorpusIQ to your own data sources](/hermes/mcp/)
