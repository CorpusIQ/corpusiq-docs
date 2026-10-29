---
title: "Emailit MCP - Send, Deliver and Debug Email From Chat"
description: "Give an agent a real sending account: campaigns, domains, contacts, bounce forensics, scoped to the client workspaces you allow."
category: Communication
stars: ★★★ (401 + OAuth scopes verified, 135 tools published)
added: 2026-10-29
source: "live probe of https://api.emailit.com/mcp answering HTTP 401 Bearer-required with WWW-Authenticate resource_metadata pointing at https://api.emailit.com/.well-known/oauth-protected-resource/mcp, which advertises scopes sending and full; plus the vendor MCP documentation at emailit.com/docs/mcp (135 tools, updated 2 October 2026)"
relevance: ★★★
tags: [email, transactional-email, deliverability, campaigns, oauth, workspace-scoping, remote-mcp]
last_updated: "2026-10-29"
---

# Emailit MCP

**Email is the one channel every business owns and the one nobody can debug. A message bounces, a domain lands in spam, a campaign goes out with the wrong audience, and the fix lives in a dashboard three logins away.**

```
Server type: Remote (Streamable HTTP, stateless POST)
Endpoint:    https://api.emailit.com/mcp
Auth:        OAuth 2.1 with PKCE, or an API key as a bearer token
Discovery:   https://api.emailit.com/.well-known/oauth-protected-resource/mcp
Scopes:      sending, full
Tools:       135, covering the full API v2
Token life:  15 minutes, refresh token good for 60 days of inactivity
```

## Why This Matters for Operators

A business that sends email runs three systems at once: the sending platform, the DNS records that decide whether mail is trusted, and the list of people who should receive it. When those three disagree, the symptom is always the same and always late, which is that a customer says they never got it.

This server puts the sending account, the domain records, the audience, the campaign and the bounce diagnosis in one surface the agent can query. The vendor's own framing is the correct one: ask why a message bounced and the assistant calls the tool that answers it, rather than explaining to you how bounce codes generally work.

The detail that earns it a place in this catalogue is workspace scoping. One connection can cover several brands or client accounts, and each tool call can name the workspace it applies to, so an agency working two clients in two chats does not cross the streams. That is the shape a multi-client operator actually needs from a hosted connector, and most email servers here offer a single-account credential.

## What Was Verified

A bare `initialize` POST to `https://api.emailit.com/mcp` returned **HTTP 401** with the JSON-RPC error `Authorization Bearer token required`, and the `WWW-Authenticate` header carried `resource_metadata="https://api.emailit.com/.well-known/oauth-protected-resource/mcp"`. Following that pointer returned the protected-resource document: resource `https://api.emailit.com/mcp`, authorization server `https://api.emailit.com`, bearer methods supported in the header, and two scopes, **`sending`** and **`full`**.

The tool count of **135** and the transport description come from the vendor's documentation page, updated **2 October 2026**, and are recorded here as the vendor's published figure rather than a count taken from a live session, because the surface is credential-gated by design.

## What the Access Model Does

Three things are worth copying into whatever policy you write around it.

The scopes are coarse and honest. `sending` and `full` are the only two choices, so a read-mostly assistant should be granted the narrower one and the read tools it exposes, not `full` for convenience.

The token is short-lived and the refresh rotates. Access lasts **15 minutes**, the refresh token survives **60 days of inactivity**, and refresh tokens rotate on every use with reuse of an old one revoking the connection. That is the correct behaviour and it also means a broken integration usually shows up as a revoked connection rather than a silent failure.

Consent is per workspace. At sign-in you choose `All my workspaces`, which also picks up ones you create later, or tick specific ones. Every connection is listed under Account, Connected apps, so the inventory of what can send as you is readable rather than assumed.

## Limits Worth Recording

This is a credential-gated remote surface, so it was catalogue-able from discovery metadata and vendor documentation but could not be driven to a `tools/list` this pass. The 135 figure is the vendor's claim and should be re-counted on first authenticated use.

The scopes are binary at the top level. There is no per-tool grant, so separation between reading a list and sending to it comes from choosing `sending` versus `full` and from which workspaces you open, not from tool-level permissions.

Email deliverability is never a solved state. The surface answers questions about DNS, authentication and reputation at a moment in time, and the answer changes when a mailbox provider changes its rules.

## FAQ

### Do I need an API key?
No. OAuth sign-in is supported and is the documented default for every listed client, including ChatGPT, Claude, Claude Code, Cursor, Codex, Grok and any other MCP client that supports authorization. An API key works as a bearer token instead.

### How do I connect a generic MCP client?
Add a remote Streamable HTTP server with the URL `https://api.emailit.com/mcp`. Clients that support MCP authorization discover the sign-in from the protected-resource document, so the URL is the whole configuration.

### Can one connection cover several client accounts?
Yes. At consent you choose all workspaces or a subset, and any call can name a workspace by ID or exact name without changing the connection default, so parallel conversations can work on different accounts at once.

### What can the agent actually ask about a failed send?
Bounces and their reasons, sending domains and their verification state, audiences, campaigns and the account's own settings, within whichever scope was granted at sign-in.

### How is this different from other email entries in this catalogue?
Transactional-only surfaces such as AhaSend send a message and return a result. This one also carries the marketing side, the domain and authentication records, the contact lists and the bounce investigation, under one OAuth connection with workspace-level isolation.
