---
title: "BriefPanel MCP - Watch a Page and Read the Field"
description: "An agent watches a pricing page, docs page or changelog and reads back the exact field that moved, with the previous value kept."
category: Marketing
stars: ★★★ (401 + OAuth protected-resource verified)
added: 2026-10-29
source: "live probe of https://actions.briefpanel.com/mcp answering HTTP 401 unauthorized, and its protected-resource document at /.well-known/oauth-protected-resource/mcp advertising the resource, authorization server and two scopes, read and write; product detail from https://briefpanel.com/mcp"
relevance: ★★★
tags: [monitoring, web-change, competitive-intelligence, oauth, remote-mcp]
last_updated: "2026-10-29"
---

# BriefPanel MCP

**A competitor changes a price and the first anyone notices is a customer asking why the quote does not match the website. Watching a page is easy. Reading the field that moved, with its previous value, is the part that turns a notification into a decision.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://actions.briefpanel.com/mcp
Auth:        OAuth 2.1
Discovery:   https://actions.briefpanel.com/.well-known/oauth-protected-resource/mcp
Scopes:      read, write
Free start:  credits on signup, no card required
```

## Why This Matters for Operators

Page monitoring tools all promise an alert. The alert is rarely the problem. The problem is that a diff of a rendered pricing page is unreadable: a banner rotates, a currency selector reflows, a cookie strip appears, and the notification says the page changed without saying what a human cares about.

BriefPanel's model is to name the fields up front and return them as typed values per check, carrying both the previous and the current value. That is a different contract from a screenshot comparison, and it is the one that fits an agent: ask what the enterprise tier costs, get a number and the number it replaced, not a wall of markup.

The pages named by the vendor are the right ones for an operator audience: pricing, docs, changelogs, competitor sites. A pricing page watched weekly is a competitive signal. A changelog watched daily is a product-release feed. A docs page watched continuously is an early warning that an integration you depend on is moving.

The two scopes are the other honest detail. `read` and `write` are separated, so an assistant that only reports movement can be granted `read` alone while the connection that creates and edits monitors holds `write`.

## What Was Verified

A bare `initialize` POST to `https://actions.briefpanel.com/mcp` returned **HTTP 401** with the body `{"error":"unauthorized"}`, which is a live, credential-gated endpoint.

The protected-resource document at `https://actions.briefpanel.com/.well-known/oauth-protected-resource/mcp` returned **HTTP 200** and advertised the resource as `https://actions.briefpanel.com/mcp`, the authorization server as `https://actions.briefpanel.com`, bearer methods supported in the header, and two scopes, `read` and `write`.

The same discovery path on the marketing host `https://briefpanel.com/.well-known/oauth-protected-resource/mcp` returns 404, so the discovery host is the `actions` subdomain, not the apex. That distinction matters when configuring a client that guesses the apex.

Product behaviour is taken from the vendor's MCP page: monitoring any page, reading back each item's fields, the previous and current value on every check, working with Cursor, Claude, ChatGPT and Windsurf, and free credits to start with no card.

## Limits Worth Recording

The surface is credential gated, so the tool inventory was not read this pass. What is documented here is the authentication contract and the vendor's stated behaviour, not a live tool list.

Pricing above the free credits is not published on the page read, so cost per monitor and per check is unknown until the account is created.

A watched field is only as good as the selector behind it. When a site redesigns, the field is what breaks, and the break looks like a change.

There is no evidence in this pass of alerting channels beyond the agent itself, so treat delivery as pull-based until the tool list says otherwise.

## FAQ

### What is the endpoint?

`https://actions.briefpanel.com/mcp`, with OAuth discovery at the same host under `/.well-known/oauth-protected-resource/mcp`.

### What is the difference between the read and write scopes?

`read` covers retrieving monitored items and their field values and history. `write` covers creating and editing monitors.

### Is there a free tier?

The vendor offers free credits at signup with no card required. The paid schedule is not published on the page read this pass.

## See Also

- [Marketing servers in this catalogue](/hermes/mcp/servers/external/)
- [Connecting CorpusIQ to your own data sources](/hermes/mcp/)
