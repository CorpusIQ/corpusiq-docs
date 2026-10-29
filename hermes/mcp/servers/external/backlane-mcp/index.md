---
title: "Backlane MCP - EU Marketplace Seller Ops for Agents"
description: "Connect OTTO Market, Kaufland and Mirakl marketplaces to an assistant: check stock and prices, and find out why a listing is not live, over OAuth."
category: Commerce & E-Commerce
stars: ★★ (401 with OAuth metadata verified, vendor docs read 2026-10-23)
added: 2026-10-28
source: "live probe of https://app.getbacklane.com/mcp returning HTTP 401 with WWW-Authenticate resource_metadata, the protected-resource document at app.getbacklane.com/.well-known/oauth-protected-resource, the vendor setup file getbacklane.com/en/setup.md marked checked 23 October 2026, and chatmcp/mcpso issue #6345"
relevance: ★★★
tags: [ecommerce, marketplaces, otto, kaufland, mirakl, seller-ops, oauth, remote-mcp]
last_updated: "2026-10-28"
---

# Backlane MCP

**A seller running four marketplaces answers the same question four ways. One listing is live, one is under review, one has a price that did not sync, and nobody can say which is which without opening four back offices.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://app.getbacklane.com/mcp
Auth:        OAuth 2.1, discovered automatically by the client
Markets:     OTTO Market, Kaufland, 50+ Mirakl marketplaces
Not yet:     Amazon
Pricing:     Free during open beta
Built by:    Backlane (getbacklane.com), repository pschlieker/getbacklane
```

## Why This Matters for Operators

The marketplace work that consumes an operator's week is not the selling, it is finding out why something is not selling. A listing that has not gone live, a stock figure that disagrees between channels, a price that changed on one marketplace and not another, an order that needs an answer before the cut-off.

This server puts those questions in the chat, against the seller's own accounts, with the marketplace connection and the permissions deciding what the assistant can see and do. It covers the German and Mirakl half of European marketplace selling, which is the half that European operators actually run on: OTTO Market, Kaufland, and the Mirakl marketplaces available in the Backlane app, which the vendor names as home24, Decathlon, XXXLutz, MediaMarktSaturn and Leroy Merlin among others.

The catalogue already carries the Russian marketplace cluster (`marketplaces-mcp-ru` across WB, Ozon, Yandex Market and Avito, and `Ozon MCP Server` alone), US seller compliance (`Tiana & Co.`) and Amazon-specific tooling. None of them speaks to OTTO, Kaufland or Mirakl, so this entry closes the Western European gap rather than repeating a covered one.

## What It Returns, Verified

A bare `initialize` on `https://app.getbacklane.com/mcp` returned **HTTP 401** with

```
WWW-Authenticate: Bearer resource_metadata="https://app.getbacklane.com/.well-known/oauth-protected-resource"
```

and the resource document names the authorization server `https://passionate-meadow-36.authkit.app`, `resource_name` **backlane**, and resource documentation `https://app.getbacklane.com/app#mcp`. That is the correct gated shape: a live endpoint refusing an anonymous call and publishing where to authenticate.

The vendor's own setup file, marked checked **23 October 2026**, gives the endpoint, the transport, the OAuth requirement and the connection steps for ChatGPT, Claude, Claude Code, Cursor and VS Code, and names `list_integrations` as the tool that confirms a working connection. The vendor describes the server as marketplace APIs for **orders, offers and inventory**, and states plainly that data and actions depend on the connection and permissions, and that **Amazon is not available yet**.

## Limits Worth Recording

Open beta, so the free period is a beta period and not a pricing promise. The full tool list is account-scoped and not published, which is why this entry records one named tool and the vendor's three data families rather than inventing a tool count; the probe carries a 401, not a tools listing. Amazon is out of scope today. A 401 in a browser is expected and is not a connection test, which the vendor says explicitly because it is the most common false alarm.

## FAQ

### Do I need to pay for Backlane?
No. The vendor states all available features are free during open beta, with any AI assistant or marketplace account costs billed separately.

### Which marketplaces are supported?
OTTO Market, Kaufland and the Mirakl marketplaces available in the app. Amazon is explicitly not supported yet.

### How does an assistant sign in?
OAuth, discovered automatically from the MCP server URL. Credentials go into the client's connection dialog, never into the chat.

### How do I know the connection works?
Ask which marketplaces are connected. The vendor names `list_integrations` as the tool that answers it, and an empty list means a marketplace still needs connecting rather than that the connection failed.

### Does this replace the marketplace back office?
No. It exposes the seller's connected accounts to an assistant for checking and acting within the granted permissions. The marketplaces remain the system of record.
