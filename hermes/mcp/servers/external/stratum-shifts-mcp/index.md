---
title: "Stratum Shifts MCP - Next Week's Rota in Chat"
description: "Staff scheduling through an assistant: availability, hour limits, clash flags, and one link the team can read, free for ten staff."
category: Productivity
stars: ★★★ (401 + OAuth protected-resource verified)
added: 2026-10-29
source: "live probe of https://shifts.stratumics.com/mcp/signin answering HTTP 401 with JSON-RPC error Sign in to Stratum Shifts to continue, and its protected-resource document at /.well-known/oauth-protected-resource/mcp/signin naming authorization server, scopes openid email shifts, and resource documentation; product and pricing from https://shifts.stratumics.com"
relevance: ★★★
tags: [scheduling, workforce, rota, small-business, oauth, remote-mcp]
last_updated: "2026-10-29"
---

# Stratum Shifts MCP

**The weekly rota is the smallest recurring decision in a business and the one most often made badly, because the person making it holds the constraints in their head: who cannot work Tuesday, who is at their hour limit, who has already done three closes.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://shifts.stratumics.com/mcp (sign-in path /mcp/signin)
Auth:        OAuth 2.1, sign in with a Stratum Shifts account
Discovery:   https://shifts.stratumics.com/.well-known/oauth-protected-resource/mcp
Scopes:      openid, email, shifts
Free plan:   one workplace, up to 10 staff
```

## Why This Matters for Operators

Scheduling software is a form. You type the constraints in, it draws a grid, and you fix the grid by hand because it does not know that Ana cannot do mornings twice in a row. The interesting thing about a conversational surface here is that the constraints are already in the conversation, in the same words the manager would use with a person.

The vendor's own description is the accurate one: tell the assistant who works for you and what each day needs, and it fills the week within each person's availability and hour limits, flags every clash, and produces one link the team can read.

Three properties make that more than a demo. The fill is bounded by availability and hour limits rather than by preference, so the output is legal before it is pleasant. Every clash is surfaced rather than resolved silently, which keeps the manager as the decision maker. And the result is a link, not a screenshot, so the team reads the same artifact the manager approved.

For a cafe, a clinic, a retail floor or a small kitchen, that is the whole product. A sample week shown on the vendor's site carries a shift count, a total hours figure, an open-shifts count and a checks count, which is the right summary: the honest measure of a rota is not how it looks but how many gaps and conflicts remain.

## What Was Verified

A bare `initialize` POST to `https://shifts.stratumics.com/mcp/signin` returned **HTTP 401** with the JSON-RPC error `Sign in to Stratum Shifts to continue.`, which is a live server answering rather than a placeholder.

Following the standard discovery path returned a protected-resource document at `https://shifts.stratumics.com/.well-known/oauth-protected-resource/mcp/signin` giving the resource as that same endpoint, the authorization server as `https://shifts.stratumics.com`, bearer methods supported in the header, three scopes (`openid`, `email`, `shifts`), the resource name `Stratum Shifts`, and a resource documentation URL at `/support`. A second document at `/.well-known/oauth-protected-resource` names the resource as `/mcp` with the same three scopes.

Pricing and plan shape come from the vendor's site: free for one workplace and up to 10 staff, with paid plans above that. A Claude connector directory entry is published as `stratum-shifts`; the equivalent ChatGPT listing is described on the site as coming soon.

## Limits Worth Recording

The surface is credential gated, so the tool list could not be read this pass. What is documented here is the product's described behaviour and the OAuth contract, not a live tool inventory.

The scope set is coarse: `shifts` covers the scheduling surface without separating reading a rota from writing one. There is no read-only scope published in the discovery document, so an assistant that only needs to answer questions about next week still receives the write scope.

Small teams only on the free plan. Above 10 staff, cost applies.

The marketplace listing situation is asymmetric across assistants, so check the directory for the assistant you actually use before promising a colleague it works there.

## FAQ

### Does it work in ChatGPT and Claude?

The vendor documents use in both, with a Claude connector directory listing live and the ChatGPT plugin directory entry described as coming soon.

### What does it do about conflicts?

It flags them. The vendor's description is that every clash is surfaced in the output rather than resolved silently, so the manager sees the trade-off instead of inheriting it.

### Is it free?

For one workplace and up to 10 staff, yes. Paid plans start above that.

## See Also

- [Productivity servers in this catalogue](/hermes/mcp/servers/external/)
- [Connecting CorpusIQ to your own data sources](/hermes/mcp/)
