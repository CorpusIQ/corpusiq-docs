---
title: "Rus.sh MCP - Short Links, QR Codes and Click Analytics"
description: "Create, find, pause and track short links and QR codes from Claude, ChatGPT or Cursor over OAuth 2.1, with per-connector permission approval and no permanent delete."
category: Marketing / Link Management
stars: n/a (works on every plan including Free)
added: 2026-10-26
source: "live MCP probe on rus.sh/mcp (initialize 401 without a token, RFC 9728 protected-resource and RFC 8414 authorization-server documents read live with six scopes and a registration endpoint) + vendor page rus.sh/pages/ai (tool verbs, permission model, limits) + official MCP registry entry sh.rus/mcp 1.0.0 + chatmcp/mcpso submission #6187"
relevance: ★★
tags: [short-links, qr-codes, click-analytics, campaign-tracking, utm, oauth, marketing-ops]
last_updated: "2026-10-26"
---

# Rus.sh MCP

**The link is the one marketing asset that is created mid-conversation, and an assistant that can mint it, name it and read its clicks closes a loop that otherwise ends in a copy-paste.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://rus.sh/mcp
Transport:   JSON-RPC over POST
Auth:        OAuth 2.1 with dynamic client registration and PKCE S256,
             or an API key as a bearer token
Scopes:      account:read, links:read, links:write, analytics:read, qr:read, qr:write
Tools:       16 verbs described by the vendor, read from rus.sh/pages/ai
Built by:    Sweent (rus.sh)
Registry:    sh.rus/mcp version 1.0.0
```

## Why This Matters for Operators

Link management looks like a utility until a campaign ships with the wrong destination, an old short link keeps sending traffic to a dead page, or nobody can say which channel produced the clicks. The three jobs that matter are: make the link with the right tags, be able to find it again months later, and read what it did without opening a dashboard.

Six resource scopes rather than one blanket grant is the part worth noting. An assistant that only needs to report can be given `links:read` and `analytics:read` and nothing else, which is not how most marketing connectors are shaped.

## What It Actually Does

`initialize` without a token returned HTTP 401. The discovery documents answer without an account:

- `/.well-known/oauth-protected-resource` returned HTTP 200 with `resource: https://rus.sh/mcp`, its own authorization server, header bearer tokens and `resource_name: Rus.sh`.
- `/.well-known/oauth-authorization-server` returned HTTP 200 with authorize, token and **register** endpoints, `protected_resources: ["https://rus.sh/mcp"]`, `code_challenge_methods_supported: ["S256"]`, grants for authorization code and refresh token, and the six scopes `account:read`, `links:read`, `links:write`, `analytics:read`, `qr:read`, `qr:write` - read and write split per object family.

The tool surface, as the vendor describes it:

| Group | Operations |
|---|---|
| Read | Get account, list links, get link, list QR codes, get QR code, get account analytics, get link analytics, get QR code analytics |
| Create | Create link (custom address, title and tags), new link counts toward the plan's monthly limit |
| Change and undo | Update link, archive link, restore link, pause link, resume link, archive QR code, restore QR code |

Connection shapes the vendor documents: Claude via the custom connector form at `https://rus.sh/mcp`, then a sign-in and a consent screen that lists what the app will be able to do, with individual permissions untickable. Claude Code, ChatGPT, Cursor, VS Code and Codex are named with their own steps. Any client that can add a remote MCP server and hold a bearer token can use an API key instead.

## How It Is Contained

- **Per-connector permissions.** The consent screen names the client and lists the actions; scopes can be removed before approval, and the vendor emails on every connection.
- **No permanent delete.** Nothing an assistant can reach deletes anything irreversibly: links and QR codes are archived and restorable, and every change can be undone.
- **Administrative surface is out of reach.** An assistant cannot create or revoke API keys, change the plan or billing, or change account settings.
- **Revocation is immediate.** Disconnecting the app in Settings, then Security, removes its access at once.

## Limitations Recorded

- No tool call was executed: every path requires an account, so the verb list above is the vendor's own description rather than a live `tools/list`.
- Argument shapes and response fields were not read from schemas.
- Analytics depth is not published on the pages read: the retention window, the attribution model and the bot filtering behind click counts are not stated, so a click number is not by itself a unique-visitor number.
- New links count toward the plan's monthly limit, so an agent that creates links freely spends a finite monthly budget.
- The redirect domain is Rus.sh's, not the customer's. A branded short domain is a separate product question.
- The registry entry is `sh.rus/mcp` version 1.0.0 while the endpoint advertises six scopes; the two were read separately.

## FAQ

### Can an assistant be given read-only access?
Yes. `links:read`, `qr:read`, `analytics:read` and `account:read` are separate scopes from the write pair, and the consent screen lets each be unticked.

### Can it break a live campaign?
Not permanently. Pausing and archiving are reversible, and pause is the operation to prefer over archive when a campaign is winding down, because the link keeps its history.

### Why connect this instead of pasting links into chat?
Because the object is created inside the tool rather than beside it. A link made in conversation carries its title, tags and analytics from the first click, and the tags are what make it findable a quarter later.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [Marketing and analytics servers in this catalog](/hermes/mcp/servers/external/)
- [CorpusIQ connectors for analytics and advertising](/hermes/mcp/)
