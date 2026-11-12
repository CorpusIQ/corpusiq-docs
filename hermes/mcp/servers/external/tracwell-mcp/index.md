---
title: "Tracwell MCP - Analytics Answered Inside the Chat"
description: "OAuth measured end to end: four scopes, dynamic registration, PKCE S256, owner-approved websites, and plans from 9 USD a month with MCP on every tier"
category: "Data and Analytics"
stars: "not applicable (hosted service)"
added: 2026-11-12
source: "the mcp.so feed card stamped 2026-11-12 08:40Z, the official registry record app.tracwell/analytics 1.0.0 declaring the same remote, both OAuth metadata documents read the same day, the vendor's AI-assistants documentation and pricing page, and a live keyless probe of https://tracwell.app/mcp"
relevance: ★★★
tags: [analytics, product-analytics, funnels, attribution, sessions, oauth, mcp, remote]
last_updated: "2026-11-12"
---

# Tracwell MCP

**The dashboard answers the question you knew to ask, and the question that matters arrives as a sentence in a conversation.** How many trial signups came from the launch post, which step of the funnel loses the most people this week, whether the revenue attributed to paid search moved after the price change - each one is three clicks into a reporting tool, or one question when the analytics sits behind an MCP endpoint. Tracwell is a web and product analytics platform that exposes traffic, funnels, goals, revenue attribution and session timelines to an agent, with the connections approved per website by the workspace owner.

```text
Server type:  remote Streamable HTTP, OAuth 2.1
Endpoint:     https://tracwell.app/mcp
Auth:         sign-in through the client, or Bearer YOUR_MCP_KEY for API-key clients
Registry:     app.tracwell/analytics 1.0.0, remote declared as the same URL
Scopes:       analytics:read, definitions:write, websites:write, offline_access
Access:       an active plan, including trials; MCP stops when the plan lapses
Probe:        keyless initialize, then both OAuth metadata documents
```

## The evidence tier

A keyless `initialize` answered **401** with `{"error":{"code":"UNAUTHORIZED","message":"Sign in through OAuth or provide an API key."}}` and the header `WWW-Authenticate: Bearer resource_metadata="https://tracwell.app/.well-known/oauth-protected-resource/mcp"`. That header is the difference between a wall and a door: a client that follows it can onboard itself.

The protected-resource document answered **200** and named one resource, one authorization server at `https://tracwell.app/api/auth`, and four scopes: **`analytics:read`**, **`definitions:write`**, **`websites:write`** and **`offline_access`**. The authorization-server document answered on both the RFC 8414 path and the issuer-suffixed path with the same content: `authorization_code` and `refresh_token` grants, **`code`** as the only response type, **`S256`** as the only PKCE challenge method, a **registration endpoint** for dynamic client registration, introspection and revocation endpoints, `none`, `client_secret_basic` and `client_secret_post` as token auth methods, and the issuer response parameter supported.

That scope set is the security story and it is a good one. **Reading analytics is one scope.** Writing is split in two, and neither of the write scopes is about the data itself: `definitions:write` covers goals and funnel definitions, `websites:write` covers the site configuration. There is no scope that edits or deletes analytics events, which is what a reporting assistant should not be able to do.

Two honest limits on this entry: the tool list was not measured, because the endpoint answers 401 without a connection and no account was created for this pass. Everything about tool names and returns is the vendor's documentation, labelled as such.

## What the vendor documents

From `tracwell.app/docs/agents` and the pricing page, read on 2026-11-12. A connection is added by URL to any OAuth-capable client, the user signs in, and **only workspace owners can approve** a connection. At approval you choose **which websites** the connection can see and **what it can do**; reading analytics is always included. Connections are revoked in Settings → MCP, which is the operator's kill switch when a client goes stale or a laptop is lost. An API key is accepted as an alternative for clients that cannot do OAuth, and the docs state that **all MCP access requires an active plan, including trials and complimentary access** - when a plan expires the dashboard history stays but MCP stops until renewal, a clean boundary between "your data is still there" and "the agent can reach it".

The Free plan allows one custom connector. The product is European-hosted analytics with campaign tracking, custom events, funnels, goals, revenue attribution and session timelines, and the docs publish DPAs and GDPR support.

Published pricing, USD, read the same day:

```text
monthly events   monthly   annual   websites   seats   history
300,000          9         90       5          1       365 days
1,000,000        15        150      5          1       365 days
2,000,000        29        290      20         10      730 days
5,000,000        49        490      20         10      730 days
10,000,000       79        790      50         30      1460 days
20,000,000       149       1490     50         30      1460 days
```

**API and MCP access is listed as included at every allowance**, not as an add-on, and each workspace gets one 7-day trial with no card. That single line is the reason this entry is worth a page: analytics vendors commonly meter the API separately, and here the agent surface is part of the same plan ladder.

## Why the scope design matters to an operator

Most "connect your analytics" arrangements are a read-only API key pasted into a tool, and the key sees every property the account owns. The arrangement here is the other shape: an owner approves a connection, names the websites it may see, and the grant is carried in a token with four scopes that cannot touch the event stream. An assistant asked *why did conversion drop last week* needs `analytics:read` and nothing else, and the connection can be built that way and revoked without rotating a credential the rest of the stack depends on.

## Where it sits

[Cookieless Analytics MCP](/hermes/mcp/servers/external/cookiefreeanalytics-mcp/) answers the same family of questions from a privacy-first platform over its own OAuth flow; [Analytics Legends MCP](/hermes/mcp/servers/external/analytics-legends-mcp/) is market intelligence rather than your own traffic. This is the first entry here where the grant is scoped to named websites before any question is asked.

### Does reading analytics require a write scope?

No. `analytics:read` is its own scope, and the two write scopes cover goal and funnel definitions and site configuration - not the events or the reports.

### What happens when the plan lapses?

The documentation states the dashboard history stays and MCP access stops until renewal, so an agent connection is not a way to keep querying analytics after a subscription ends.

### Can a connection be limited to one website?

Yes - at approval the owner chooses which websites the connection may see, and the scope list carries `websites:write` separately for configuration changes. Per-website approval is the vendor's stated behaviour; the token grant is the measured part.
