---
title: "Localnord MCP - Manage Google Business Profiles"
description: "Manage Google Business Profiles from Claude: listings, reviews, posts and local SEO audits with approval-first drafts and scoped OAuth permissions."
category: Marketing
stars: n/a (new listing)
added: 2026-10-11
source: "mcpservers.org /all (Oct 11, 2026 midday sweep)"
relevance: ★★
tags: [local-seo, google-business-profile, reviews, agencies, oauth, remote-mcp]
last_updated: "2026-10-24"
---

# Localnord MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 with PKCE)** - connects Claude or any MCP client to a local marketing workspace: Google Business Profile listings, reviews, stats, posts and photos across an organization's locations, with audits and rank scans, behind granular per-scope permissions.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 with PKCE (Sign in with Localnord; scopes chosen at consent)
Endpoint: https://app.localnord.io/api/mcp/mcp
Tools: listings, reviews, stats, audits, drafts, posts, photos
Pricing: Localnord plans (paid actions consume credits)
Built by: Localnord
Listing: mcpservers.org (Oct 2026)
```

## Why This Matters for Operators

For a local business, or an agency running many of them, the Google Business Profile is the front door: hours, services, photos, posts and review replies are what customers see before the website. Localnord is the management platform for that surface, and its MCP server turns the work into chat: pull the listing and review state, draft replies and posts, run local SEO audits and rank scans, then publish what the owner approves.

The design keeps the risky parts safe: drafts are created first and nothing is published without approval, write actions are split into their own scopes, paid actions are confirmed before running, and every connection is scoped to a single organization and revocable from Settings.

## Permissions (Scopes)

| Scope | Grants |
|---|---|
| `mcp:read` | Read-only: listings, reviews, stats; run audits |
| `mcp:write:drafts` | Create post and reply drafts (nothing is published without approval) |
| `mcp:write:reviews` | Post replies to reviews directly on Google |
| `mcp:write:content` | Publish posts; upload and delete photos |
| `mcp:write:listing` | Edit hours, description, services and attributes of the listing |
| `mcp:write:paid` | Full audits, rank scans and websites (consume credits) |
| `mcp:admin` | Everything above plus sensitive actions (SMS, webhooks, portal) |

## Installation

```bash
claude mcp add --transport http localnord https://app.localnord.io/api/mcp/mcp
```

Or declare the remote server in any MCP client (Cursor, VS Code, others); the OAuth flow starts on first connection. The consent screen lists the scopes, hierarchical and granular, so you only grant what you need.

## FAQ

### What can the agent do without publishing anything?
Read listings, reviews and stats, run audits, and create drafts of posts and review replies. Publishing requires the write scopes.

### Is one connection enough for multiple locations?
Yes, within your organization. Each connection is scoped to it, no other agency's data is reachable, and demo organizations cannot connect the server.

### Which actions are rate limited?
Sensitive or paid actions (full audits, rank scans, SMS, webhooks) are rate-limited against abuse and confirmed before running; paid actions consume credits.

### How do I disconnect or revoke access?
Settings, API and MCP. Every connection is individually revocable, and permissions are chosen per connection at sign-in.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - all catalogued business-relevant servers
