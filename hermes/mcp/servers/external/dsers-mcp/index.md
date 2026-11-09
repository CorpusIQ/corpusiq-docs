---
title: "DSers MCP - The Dropshipping Loop Behind a Chat"
description: "AliExpress supplier products, listings, supplier orders and shipment tracking, exposed under 23 OAuth scopes by the platform itself."
category: Commerce & Marketplace Operations
stars: "n/a (hosted by the vendor; OAuth only, no API keys)"
added: 2026-11-08
source: "the mcp.so feed card dsers-official-mcp-server stamped 2026-11-09T03:21:17.720Z; the endpoint at ai.dsers.com/mcp/mcp-so, where a keyless initialize answered 401 with the OAuth error body; and the vendor's own OAuth metadata documents, which carry the full scope list"
relevance: ★★★
tags: [dropshipping, aliexpress, ecommerce, supplier-orders, fulfillment, tracking, oauth, remote-mcp]
last_updated: "2026-11-08"
---

# DSers MCP

**Dropshipping is two businesses wearing one storefront: selling to a customer, and buying from a supplier. The selling side is where the chat window has been useful so far. This is the buying side.** DSers is the ordering platform between AliExpress suppliers and a seller's store, and its official MCP endpoint exposes supplier product discovery, listing preparation, supplier order placement and shipment tracking to an assistant.

```text
Server type: Remote (Streamable HTTP)
Endpoint:    https://ai.dsers.com/mcp/mcp-so
Auth:        OAuth 2.1 with PKCE, no API keys
Scopes:      23, from product:import to order:write and tracking:read
Registry:    the mcp.so listing is marked verified by the vendor account
Protocol:    2025-11-25 advertised on the refusal
```

## What the endpoint says about itself

A keyless `initialize` answers **401** with a machine-readable refusal rather than a login page:

```json
{"error":"invalid_request","error_description":"Authorization required. This endpoint uses OAuth 2.1 + PKCE (no API keys).",
 "mcp_protocol_version":"2025-11-25",
 "oauth_metadata":"https://ai.dsers.com/.well-known/oauth-authorization-server",
 "protected_resource_metadata":"https://ai.dsers.com/.well-known/oauth-protected-resource/mcp/mcp-so"}
```

That is a well-built gate, and it is also the evidence tier this entry stands on: **live and gated by the vendor, documented from its own metadata, not driven.** Two details are worth recording because they are better practice than most of this catalogue sees. The refusal names a protocol version (`2025-11-25`) newer than the `2025-06-18` most servers still advertise, and it carries a `correlation_id` so a support ticket can be matched to a failed handshake.

The authorization server document is public and complete: authorization code with PKCE over `S256`, refresh tokens, dynamic client registration at `/oauth/register`, RS256 identity tokens with a published JWKS, and the issuer on the same host.

## The scope list is the product document

Nobody at a dropshipping company has to guess what this connector can do, because the vendor publishes **23 scopes**, and they describe the workflow more precisely than a feature page would:

```text
user:read/write          store:read/write        theme:read/write
staff:read/write         supplier:read
product:read/write       product:import          product:push
product:mapping          order:read/write        tracking:read
settings:read/write      notification:read       billing:read      plan:read
```

Read as a sequence, that is the dropshipping loop: find a supplier product (`supplier:read`), import it into the store's catalogue (`product:import`), map the supplier variant to the store variant (`product:mapping`), publish it (`product:push`), and then, once it sells, place the supplier order (`order:write`) and read the tracking that comes back (`tracking:read`). A seller can grant `product:read` alone and let an assistant analyse the catalogue without letting it touch an order, which is the right default and is only possible because the scopes are this fine-grained.

## The class it enters, and the distinction that earns the entry

This catalogue already carries a dropshipping entry: [Hustle Got Real](/hermes/mcp/servers/external/hustle-got-real-mcp/) lists **170** tools over a dropshipping back office, covering listings, stock, pricing rules, orders and auto-ordering behind one broad `hgr` scope. It is the store's own nervous system. DSers is the other half of the same business: the supplier relationship, the AliExpress product catalogue, the purchase order that has to be placed with a supplier and the tracking that comes back from it. A seller running a store on one side and a supplier on the other needs both, and the reason to record this one is that the purchase path is where an assistant can actually save a day of clicking.

The rest of the neighbourhood is different in kind: [Sellfy](/hermes/mcp/servers/external/sellfy-mcp/) is a storefront, WordPress.com is a site builder, and neither places a supplier order.

## What it cannot tell you

There is no tool list behind the 401, so this guide cannot quote tool names or schemas, and a reader should treat the scope names as the contract rather than as the interface. Pricing is not published on the endpoint and is not repeated here. The store platform matters: the tags name Shopify, and a seller on another platform should confirm the order path before connecting. And the fundamental caution of this category applies in full: an agent with `product:push` and `order:write` can publish a wrong product and spend real money on a real supplier, so the scopes should be granted by task, and the catalogue price should be read by a person before the first push.

## Frequently asked questions

### Can an assistant place a supplier order on its own?

`order:write` is in the scope list, so the surface exists, and whether it executes depends on the scope granted at consent. The safe pattern is to grant `product:*` first, let the agent do catalogue work, and add `order:write` only after the mapping has been checked on a sample.

### Why does the endpoint advertise a newer protocol version?

It answers `2025-11-25` on the refusal, which is ahead of the `2025-06-18` that most servers here still negotiate. A client that only speaks the older revision should still connect, since MCP negotiates down, but the header is worth knowing when debugging a handshake.

### Is there an API key path?

No, and the vendor says so in the refusal: OAuth 2.1 with PKCE only. That removes the usual leak vector of a long-lived key pasted into a config file.

### What does the connector need from the seller?

A DSers account. The consent screen is the vendor's own, and the scope list above is what a seller is asked to approve, which is the part to read before pressing allow.
