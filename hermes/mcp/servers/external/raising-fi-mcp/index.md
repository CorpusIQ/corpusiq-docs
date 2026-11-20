---
title: "Raising.fi MCP - Live Funding Rounds Behind OAuth"
description: "A funding-round and founder-data server with five named tools, a one-scope OAuth gate and an API key path for scripts. Plan-gated."
category: "Finance / Venture Data"
stars: "n/a (hosted vendor endpoint; no public repository)"
added: 2026-11-19
source: "the mcpservers.org sitemap map servers/12 (restamped 2026-11-19T18:10Z onward), the official MCP registry record fi.raising/raising 1.0.0 published 2026-11-19T04:36:21Z, a keyless initialize that returned 401 with a complete WWW-Authenticate challenge, the protected-resource document read to HTTP 200, the RFC 8414 authorization-server document read to HTTP 200, the vendor developer page read to HTTP 200 listing five tools, and the public OpenAPI spec and health route measured live. No credential is held, so no tool was driven and that is stated rather than implied"
relevance: ★★
tags: [fundraising, venture-capital, funding-rounds, investors, founder-data, startups, oauth, protected-resource, remote, plan-gated, documented-tier]
last_updated: "2026-11-19"
---

# Raising.fi MCP

**Funding rounds are public the day they are filed and useless the day they are old. The question is whether an agent can read the live register, and what it has to prove first.**

Raising.fi publishes recent startup funding rounds, the founders behind them and hiring trends across the companies that raised. The MCP surface sits in front of that dataset behind a single read scope, and this guide records the gate at its full depth because the gate is all that could be measured: the endpoint refused an anonymous `initialize`, and no credential is held by this catalog, so every claim below comes from a vendor surface rather than from a driven call.

```text
Server type:   remote Streamable HTTP, OAuth 2.1 with dynamic client registration
Endpoint:      https://raising.fi/api/mcp
Registry:      fi.raising/raising 1.0.0, published 2026-11-19T04:36:21Z
Vendor page:   https://raising.fi/mcp (HTTP 200, 97,262 bytes)
Developer doc: https://raising.fi/developers#mcp (HTTP 200, 62,862 bytes)
Scope:         raises:read (the only scope)
Plan:          Growth or Enterprise; MCP and REST share the same monthly token allowance
Evidence tier: documented from the vendor's own surfaces, not driven
```

## The refusal is informative

An anonymous `initialize` answers HTTP **401** with a JSON-RPC error and a complete challenge:

```text
HTTP/1.1 401
WWW-Authenticate: Bearer resource_metadata="https://raising.fi/.well-known/oauth-protected-resource/api/mcp", scope="raises:read"

{"jsonrpc": "2.0", "id": 1,
 "error": {"code": -32001, "message": "Sign in to Raising.fi to use this server."}}
```

The protected-resource document at that URL answers **200** and is 251 bytes of exactly what the spec asks for:

```json
{"resource": "https://raising.fi/api/mcp",
 "authorization_servers": ["https://raising.fi"],
 "scopes_supported": ["raises:read"],
 "bearer_methods_supported": ["header"],
 "resource_name": "Raising.fi",
 "resource_documentation": "https://raising.fi/developers#mcp"}
```

The issuer's RFC 8414 document resolves on the same host and completes the chain: authorization endpoint `/oauth/authorize`, token endpoint `/api/oauth/token`, a **dynamic registration endpoint** at `/api/oauth/register`, revocation at `/api/oauth/revoke`, authorization code with refresh and PKCE **S256**, token auth by `none`, `client_secret_post` or `client_secret_basic`, and `client_id_metadata_document_supported: true`. A client that supports DCR and PKCE needs no hand-issued client id, which is the difference between a server an agent can connect itself and one that waits on a support ticket.

One scope, and it is a read scope. Nothing on this surface can write, which is the right shape for a data product.

## The five tools, as the vendor names them

The developer page states the tool list plainly:

| Tool | What the vendor says it is for |
|---|---|
| `search_raises` | search live funding rounds |
| `get_founder` | founder records behind those rounds |
| `search_jobs` | hiring signal at the companies that raised |
| `get_trends` | funding trends over time |
| `get_account` | the caller's own account and token state |

Because `initialize` refused, none of the five has been listed by the server itself in this pass, so no schema, no annotation and no output shape is recorded here. That is a gap in this guide and it is labelled as one: the tool names are the vendor's, and the first agent to hold a key will be the first to read their `inputSchema`.

## Two ways in, priced the same way

The vendor documents both paths and is explicit that they share one allowance:

- **MCP**, with an OAuth sign-in from any MCP client, including the copy-paste configs the page prints for Claude, ChatGPT, Grok, Cursor, VS Code, Claude Code, Codex, Gemini CLI and Windsurf.
- **REST with an API key**, sent as `X-Api-Key` or as an `Authorization: Bearer` header, for servers and scripts that cannot open a browser.

Both need a **Growth or Enterprise** plan. Keys are created at Settings, API Keys, shown once. The REST surface is live and measurable without a key at the cheap end:

```text
GET https://raising.fi/api/v1/health        200  {"healthy":true,"authenticated":false,"requestId":"062d519e-..."}
GET https://raising.fi/api/v1/openapi.json  200  11,917 bytes, OpenAPI 3.1.0, "Raising.fi API" 1.0.0
```

The spec names the read routes the key unlocks: `/api/v1/me`, `/api/v1/raises`, `/api/v1/trends/tlds` and `/api/v1/trends/keywords`, with health and me free to call. A `trends/tlds` route beside `trends/keywords` is worth noting: the vendor ships domain-level trend data as its own endpoint, which is a growth signal rather than a funding one.

## What this entry can and cannot claim

- **Can:** the endpoint exists, refuses anonymously, and points a conforming client at a complete OAuth chain with dynamic registration and one read scope.
- **Can:** five tools are named by the vendor and the REST dataset behind them is exposed with an OpenAPI 3.1.0 spec.
- **Cannot:** the response shape of `search_raises`, the size of the round corpus, the freshness of the newest round, or whether `get_trends` returns counts, sectors or valuations. Every one of those needs a key.
- **Cannot:** any figure from the dataset. No number appears in this guide because no number was read.

## Add it to Hermes

```bash
hermes mcp add raising --url https://raising.fi/api/mcp --auth oauth
hermes mcp login raising
```

Hermes handles dynamic client registration and PKCE against the document above, so the login flow is the browser sign-in and one consent screen for `raises:read`. For a headless worker, use the key path instead and keep the key out of the command line:

```bash
hermes config set mcp_servers.raising.headers.X-Api-Key "rk_live_..."
```

Then the question this dataset answers: *which startups in the last 90 days raised a seed round and are now hiring engineers in Phoenix.* That answer is a funding query crossed with a hiring signal, which is why the two tools sit on the same server.

## Why it earns a slot

The catalog's investor entries are scraped funding records. This is the first entry that serves live rounds, founders and hiring trends through a spec-conforming OAuth surface with dynamic registration, and the vendor's plan-gated model is recorded beside the gate rather than hidden behind it. It ships at the documented tier, with the missing half named: a driven pass is owed the first time a key exists.
