---
title: "Laplace MCP - Korean Ecommerce Analytics in Chat"
description: "An OAuth-gated analytics server for brands selling on Coupang, Naver, Cafe24, Shopify and Amazon, with contribution profit after channel fees and ad spend."
category: "Ecommerce / Analytics"
stars: "0 (hosted Streamable HTTP at https://gateway.laplacetec.com/mcp/, OAuth with a published protected-resource document, tool surface not measured because the endpoint is credential gated)"
added: 2026-11-17
source: "the mcp.so submission queue entry 7537 filed 2026-11-18T01:10:31Z, the registry record io.github.laplacetec/ecommerce-analytics, and a probe session on 2026-11-17 that read the 401 challenge and the protected-resource metadata"
relevance: ★★
tags: [ecommerce, analytics, korea, coupang, naver, roas, oauth, remote, mcp]
last_updated: "2026-11-17"
---

# Laplace MCP

**A brand that sells in Korea and abroad does not have one sales number. It has six: Coupang says one thing, Naver Smart Store another, Cafe24 another, and the ad platforms disagree with all of them.** Laplace is an ecommerce analytics product built for exactly that shape, and this is its official MCP server.

The channel list is the part worth noting: Coupang, Naver Smart Store, Cafe24, Olive Young, Shopify and Amazon, with the ad channels beside them. That is a Korean and cross-border merchant stack, not a Western one with Korea bolted on.

```
Server type:   remote Streamable HTTP (hosted)
Endpoint:      https://gateway.laplacetec.com/mcp/
Server:        uvicorn (Python), name not disclosed before auth
Registry:      io.github.laplacetec/ecommerce-analytics
Auth:          OAuth with a Laplace account, or a Laplace API key header
Docs:          analytics-docs.laplacetec.com/guide/mcp/start
```

## The evidence tier

Auth gated, and the gate is well published. This guide states what was measured and refuses to invent the rest.

`initialize` and `tools/list` both returned **401** with no body. The challenge header names the metadata document that describes the resource:

```text
WWW-Authenticate: Bearer resource_metadata=
  "https://gateway.laplacetec.com/.well-known/oauth-protected-resource/mcp/"
```

That document answered 200 with a complete RFC 9728 protected-resource record: resource `https://gateway.laplacetec.com/mcp/`, authorization server `https://gateway.laplacetec.com/mcp`, scopes `email`, `openid`, `phone`, `profile`, and bearer token in a header. A client that follows the challenge can find the authorization server without being told out of band.

The error tier is the weak part. A request carrying an obviously invalid API key also returned 401, with an **empty body** and no error text. An integrator cannot tell a wrong key from an expired one, a missing scope, or a disabled account. Compare that against servers that answer with a named error and a route forward.

## What this server is for

The vendor's description, which is the only statement of the product surface available before a credential:

- **Sales truth per channel**, with contribution profit computed after COGS, channel fees and ad spend, so ROAS is a result rather than a separate dashboard.
- **First versus repeat purchases**, cohorts and cross-sell, which is the analysis a marketplace seller cannot do inside any single channel's console.
- **Setup by chat with a preview and a change history**: product matching, ad matching rules, Google Sheets lookups and custom formula columns, dashboard charts and Slack alerts. The description is explicit that the AI only suggests, and a person confirms.

That last point is a good design sign. A server that proposes a matching rule and shows the change before applying it is treating the merchant's catalogue as production data.

## Why this earns a page

CorpusIQ readers are operators who already run one business question across several systems. Cross-border commerce is the same problem with currency and channel semantics added: the question "what did I actually make on that campaign" needs sales, fees and ad spend from four systems that do not share an identity model.

Laplace is the first server on this list whose product is that reconciliation for Korean and global channels, and the MCP server is official rather than a wrapper. It is a two-star entry because the tool surface could not be measured from this host: the endpoint is credential gated, so the tool list, schemas and return shapes are recorded as unknown rather than guessed.

## Installation

Add the remote endpoint and let the client perform the OAuth flow:

```json
{
  "mcpServers": {
    "laplace": {
      "url": "https://gateway.laplacetec.com/mcp/"
    }
  }
}
```

The trailing slash is part of the endpoint as published, and the protected-resource document names the same URL with the slash, so keep it.

## Configuration

Two supported paths, per the vendor:

- **OAuth with a Laplace account.** The client follows the 401 challenge to the metadata document, then to the authorization server.
- **A Laplace API key** in a `Laplace-Api-Key` header, for developer tools that do not implement the OAuth flow.

Scope requests resolve against `email`, `openid`, `phone` and `profile`, so an integration should expect an account-level identity to be part of the token, not only a data scope.

## Limitations

- Tool names, count and return shapes are **not measured**. The endpoint refuses anonymous `tools/list`, and this guide does not infer them from marketing copy.
- The 401 body is empty for both a missing credential and an invalid key, so error handling has to be defensive on the client side.
- The product is credential-bound to a merchant account. Nothing here can be demoed without one.
- Korean and cross-border channels are the stated strength. A brand selling only in the US or EU should check channel coverage before choosing it.

## FAQ

### Does Laplace MCP work without an account?

No. `initialize` and `tools/list` return 401 without a credential. The published protected-resource document is the intended onboarding path.

### Which sales channels does it cover?

The vendor lists Coupang, Naver Smart Store, Cafe24, Olive Young, Shopify and Amazon, with their associated ad channels, and analytics for contribution profit after COGS, channel fees and ad spend.

### Can an agent change the account?

The vendor describes setup actions such as product matching and matching rules as proposals with a preview and a change history, confirmed by a person. Treat any write path as human approved.

### What auth methods are supported?

OAuth against a Laplace account, with an API key header as the alternative for developer tools.

## See Also

- [Edwin MCP - Shopping Prices From Merchant Feeds](/hermes/mcp/servers/external/edwin-mcp/)
- [Sellfy MCP - Store Operations Inside the Chat](/hermes/mcp/servers/external/sellfy-mcp/)
- [DSers MCP - The Dropshipping Loop Behind a Chat](/hermes/mcp/servers/external/dsers-mcp/)
