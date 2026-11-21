---
title: "Hushdrop MCP - Private Share Links for Agent Output"
description: "Hushdrop turns pages and files an agent makes into private share links with passwords, expiry, burn-after-view, view stats and lead capture."
category: "Business Operations"
stars: n/a (MIT, self-hostable)
added: 2026-11-20
source: "chatmcp/mcpso submission #7730 + hushdrop.dev/docs remote MCP section (66 tools) + hushdrop.dev/pricing + keyless initialize and protected-resource probes on 2026-11-21"
relevance: ★★★
tags: [sharing, artifact-hosting, secure-links, expiry, lead-capture, self-hosted, remote-mcp, oauth]
last_updated: "2026-11-20"
---

# Hushdrop MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 with PKCE) plus a local stdio package** - the delivery step of the agent loop. An agent publishes a page or a file it just made, and Hushdrop returns a private, revocable link with optional password, expiry, burn after one view, view statistics, a lead-capture form and per-recipient access.

```
Server type: Remote (Streamable HTTP) + local stdio via npm
Auth: OAuth 2.1 with PKCE (GitHub or email sign-in); each approval issues a key labelled mcp:<client>
Endpoint: https://hushdrop.dev/mcp
Protected resource: https://hushdrop.dev/.well-known/oauth-protected-resource/mcp
Local package: npx hushdrop-mcp
Self-hosting: free, MIT, on your own domain
Tools: 66 documented
Category: Business Operations / Delivery
```

## Why This Matters for Operators

An agent that produces a report, a proposal or a rendered page has nowhere to put it. Attaching the file to an email is how a draft escapes into a thread; pasting it into chat history is how a client sees a half-finished revision three scrolls up. Hushdrop's job is the missing verb: publish, with the controls a business document actually needs, and a receipt that says whether the client opened it.

The controls are the product. A password for a document that should not be forwarded, an expiry for a quote that stops being valid at month end, burn-after-view for something confidential, an email gate that captures the reader, and version history with rollback when the second draft supersedes the first.

## Tools

The vendor documents **66 tools** on the docs page. The families, with the names it publishes:

| Family | Tools |
|---|---|
| Publish and update | `publish_html`, `update_site`, `publish_file`, `start_upload` / `finish_upload`, `rollback_site`, `list_versions`, `delete_site` |
| Access control | `set_password`, `set_expiry`, `set_email_gate`, `set_nda`, `set_open_alerts`, `list_recipients` / `invite_recipients`, `set_team_domain` |
| Collaboration | `drop_comments` / `resolve_comments`, editors, teams, `create_portal` / `add_to_portal`, `page_rules` |
| Measurement | `drop_stats`, `lead_capture`, `set_analytics_tag`, `search_drops`, `list_sites` |
| Infrastructure | `data_store`, `set_secret` (a secrets proxy), `add_webhook`, custom domains, `billing_status`, `upgrade_pro` / `upgrade_team`, `whoami`, `get_template` |

When a call hits a plan limit the result names what to ask the user and which upgrade tool starts the free trial, which is the right shape for an agent running on someone else's account.

## Measured Authentication Gate

A keyless `initialize` on `https://hushdrop.dev/mcp` answers **HTTP 401** with a scope in the challenge and a JSON-RPC error a client can act on:

```text
www-authenticate: Bearer resource_metadata="https://hushdrop.dev/.well-known/oauth-protected-resource/mcp", scope="drops"
{"jsonrpc":"2.0","error":{"code":-32001,"message":"Sign in to Hushdrop to use this server. It's free: connect again and your app opens the sign-in page."},"id":null}
```

The protected-resource document answers **200** at the suffixed path:

```json
{"resource": "https://hushdrop.dev/mcp",
 "authorization_servers": ["https://hushdrop.dev"],
 "scopes_supported": ["drops"],
 "bearer_methods_supported": ["header"],
 "resource_name": "Hushdrop",
 "resource_documentation": "https://hushdrop.dev/docs#remote-mcp"}
```

Note the path: this server publishes the document under `/mcp`, where Logo.dev publishes at the bare route and 404s with the suffix. Read the `WWW-Authenticate` header rather than guessing. **No tool was called**; publishing a link would put a real page on a real account, which a documentation pass has no business doing.

## Installation

```bash
# Remote, any client with Streamable HTTP
claude mcp add --transport http hushdrop https://hushdrop.dev/mcp

# Codex
codex mcp add hushdrop --url https://hushdrop.dev/mcp
codex mcp login hushdrop

# Local stdio, no hosted account
npx -y hushdrop-mcp
```

```json
{
  "mcpServers": {
    "hushdrop": {
      "url": "https://hushdrop.dev/mcp"
    }
  }
}
```

The first call opens a sign-in page. Approving it issues the client a key labelled `mcp:<client>` that can be revoked like any other API key, so a device that is lost does not mean an account is lost.

## Pricing

Read from the pricing page on 2026-11-21: **Free $0 forever** for sharing your own work (private drops encrypted before upload, passwords, expiry, revocable links, version history and rollback, CLI, MCP server and agent skill), and **Team $29 a month flat** with unlimited members, one shared handle, owner/admin/editor roles and 50 GB of storage, against the page's own comparison of $120 to $290 a month for 10 seats at per-seat tools. The trial is 14 days with no card. The page's banner also mentions a **Pro** tier at $9 that the two plan cards do not detail, so read the live plan grid before quoting that number.

## Honest Limits

- **Encryption is location-dependent.** The docs say passwords protect a drop and that encryption happens before upload when you use the CLI or the local server; drops locked through the remote server are described as encrypted server-side. If zero-knowledge is a requirement, self-host or use the local package.
- **Custom domains on hosted links are "coming".** Your own domain works today only when you self-host, which is free and MIT. A managed link lives on `hushdrop.dev`.
- **66 tools is a large surface.** Plan-limit errors and role requirements arrive as tool errors, and endpoint-changing operations need owner or admin on a team, so an agent working inside a team space will hit permission walls by design.
- **The managed service is young** (documentation dated June 2026, one author) even though the code is open. Self-hosting is the durable path; the hosted plan is the convenient one.
- **Measured gate, undriven tools.** The challenge, the scopes and the tool list are from the vendor document and a live probe; no publish, password or expiry was exercised in this pass.

## Integration with CorpusIQ

This is the last mile of an operator's reporting loop. CorpusIQ produces the answer (a monthly review, a customer health page, a proposal with the numbers already joined); Hushdrop delivers it with an expiry and a read receipt. Pair `drop_stats` with the CRM record and a team stops guessing whether the client saw the report before the follow-up call.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [DropCue MCP - Music Catalog, Pitches and Royalties](/hermes/mcp/servers/external/dropcue-mcp)
