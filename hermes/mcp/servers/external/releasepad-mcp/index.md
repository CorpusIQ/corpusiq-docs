---
title: "ReleasePad MCP - Publish Your Changelog From Chat"
description: "A complete OAuth chain behind one URL: draft, schedule and publish changelog posts from any assistant, with read-only or full access and drafts by default."
category: "Productivity"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-24
source: "An mcp.so feed card for /servers/releasepad stamped 11/24/2026 07:07 PM UTC, captured 2026-11-25T04:02Z; keyless initialize refused 401 on https://pro.releasepad.io/mcp with a WWW-Authenticate bearer challenge naming resource_metadata, read 2026-11-25; the protected-resource document and the RFC 8414 authorization-server document read at their published paths the same day, with /.well-known/openid-configuration answering 404; capability statements, client setup steps and the read-only versus full-access choice read from https://www.releasepad.io/features/mcp-server/ on 2026-11-25; plan prices and the MCP entitlement read from https://www.releasepad.io/pricing the same day; registry record io.releasepad/mcp 1.0.0 read the same day"
relevance: "★★★"
tags: [changelog, release-notes, product-updates, publishing, oauth, pkce, remote-mcp, drafts, scheduling, analytics]
last_updated: "2026-11-24"
---

# ReleasePad MCP

**The changelog is the page nobody writes and every buyer reads.** It is also the page an assistant can write better than a person at 6pm on release day, because the pull request, the ticket and the last three posts are already in the conversation. ReleasePad's MCP server puts the changelog behind one URL with a complete OAuth chain, and the safety property that makes it usable is that every post starts as a draft.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://pro.releasepad.io/mcp
Auth:        OAuth 2.1, PKCE S256, scopes read and write
Tools:       not readable without an account (401 before initialize)
Pricing:     MCP access requires Pro, USD 35 a month per product;
             Free is USD 0 with 20 posts and 20 AI requests, no MCP
```

## The gate, measured

`initialize` with no credential answers **401** with a plain JSON body and a full bearer challenge:

```
HTTP/2 401
www-authenticate: Bearer resource_metadata=
  "https://pro.releasepad.io/.well-known/oauth-protected-resource"

{"message":"Missing or invalid authorization token","status":"error"}
```

**The `resource_metadata` pointer resolves.** This is the part that separates a usable OAuth server from a documented one. The protected-resource document answers **200**:

```json
{"resource":"https://pro.releasepad.io",
 "authorization_servers":["https://pro.releasepad.io"],
 "scopes_supported":["read","write"],
 "bearer_methods_supported":["header"]}
```

And the RFC 8414 authorization-server document on the same host answers **200** with the whole flow:

```json
{"issuer":"https://pro.releasepad.io",
 "authorization_endpoint":"https://pro.releasepad.io/oauth/authorize",
 "token_endpoint":"https://pro.releasepad.io/oauth/token",
 "registration_endpoint":"https://pro.releasepad.io/oauth/register",
 "revocation_endpoint":"https://pro.releasepad.io/oauth/revoke",
 "response_types_supported":["code"],
 "grant_types_supported":["authorization_code","refresh_token"],
 "code_challenge_methods_supported":["S256"],
 "response_modes_supported":["query"],
 "token_endpoint_auth_methods_supported":["none","client_secret_basic","client_secret_post"],
 "revocation_endpoint_auth_methods_supported":["none","client_secret_basic","client_secret_post"],
 "scopes_supported":["read","write"],
 "service_documentation":"https://releasepad.io/docs"}
```

Three details are worth an integrator's afternoon. **Dynamic client registration and PKCE S256 are both present**, with `none` accepted as a token endpoint auth method, which is what a desktop or web assistant needs and what a strict client will look for first. **The issuer is the MCP host**, so there is no second hostname to discover, unlike the split-host pattern this catalog records elsewhere. And **the only response mode offered is `query`**, with no `form_post`, and the only response type is `code`: a client that defaults to a form-post callback or to an implicit flow will fail at the authorization endpoint rather than at token exchange. `/.well-known/openid-configuration` answers **404 with an HTML page**, so this server is OAuth with no OIDC layer, and a client that insists on an OIDC discovery document will refuse to connect to a server that would otherwise work.

## What the assistant can do, per the vendor

The tool schema is unreadable without an account, so this section is the vendor's product description and not a measured response. The documented surface is the changelog itself:

- list the **products** in the account,
- **search and read** published and draft posts,
- **create and edit** release notes, picking a category and matching the tone of recent posts,
- **publish** a post, or **schedule** it for later,
- manage **categories**,
- read **view analytics** for published posts,
- and fire the account's **webhooks** on every post event, which is how the changelog reaches the rest of a stack.

The product pages states three permission behaviours that matter more than the tool list. **Every post starts as a draft and nothing goes public until a person says so.** The OAuth grant offers **full access or read-only**, so an assistant that only answers questions can be given the read-only scope and nothing else. And **destructive tools are flagged** so that clients such as Claude ask for confirmation before deleting. Revocation is per-app from **Connected Apps** in the account, which means the answer to "how do we turn this off" is a settings page and not a support ticket.

## One URL, and the clients that already take it

The same address serves every client, which is worth stating because most hosted servers in this catalog need a client-specific setup block:

1. **Claude.ai**: Settings -> Connectors -> Add custom connector, name it ReleasePad, paste `https://pro.releasepad.io/mcp`, connect and sign in.
2. **Claude Code**: `claude mcp add --transport http releasepad https://pro.releasepad.io/mcp`, then `/mcp` inside a session and follow the login link.
3. **Cursor**: install from the ReleasePad listing in the Cursor directory, or add `{"mcpServers":{"releasepad":{"url":"https://pro.releasepad.io/mcp"}}}` to `~/.cursor/mcp.json`.
4. **Anything else** that supports Streamable HTTP with OAuth: the first tool call opens a browser, the user approves, and the token is revocable from the account.

The vendor also names **ChatGPT, Codex and Grok** on the page, which for this catalog is a statement about client compatibility rather than a claim of native integration anywhere.

## What it costs, and what the free tier actually includes

| Plan | Price | What MCP needs |
| --- | --- | --- |
| Free | USD 0 | 1 product, 20 posts including drafts, 20 AI requests, no MCP |
| Pro | USD 35 a month per product | MCP access, REST API and webhooks, analytics, custom domain |

The plan is per **product**, not per seat: unlimited team members, no MAU count and no usage tiers. The pricing page states **153+ teams** use it. For an operator the relevant line is that **MCP is a Pro entitlement**, so a free account cannot connect the server at all; the trial-and-error path of adding the connector and discovering the wall at the first tool call is avoidable by reading the plan table first.

## Where it stops

- **The tool schema is unmeasured.** A keyless `initialize` is refused with 401, so there is no `tools/list` in this pass and no tool name is published anywhere on the product pages. Everything about capability above is the vendor's own description, dated **2026-11-25**. Re-probe with a Pro account before publishing a schema or writing prompts that call a named tool.
- **Closed source.** There is no repository to read, so the server behaviour cannot be audited ahead of use; the registry record (`io.releasepad/mcp` **1.0.0**, remote `streamable-http`) and the product page are the whole public surface.
- **No OIDC discovery.** `openid-configuration` is a 404 and the token response is not documented as carrying an identity token, so an SSO-only enterprise that requires OIDC claims from every connector will have to make an exception.
- **`query` is the only response mode.** A client with a fixed form-post callback will not complete the flow, and the failure will look like a client bug rather than a server constraint.
- **Publishing is the point.** Read-only scope exists, but the reason to connect this server is to write. An operator granting write scope to an agent is trusting the draft-then-publish sequence, and the vendor's own framing is that the human says "publish" rather than the agent deciding.

## How to connect it

1. Take a **Pro** plan on the product you want the assistant to write to. The free plan has no MCP.
2. Add `https://pro.releasepad.io/mcp` in the client. The client registers itself through `/oauth/register` and completes PKCE S256.
3. Choose **read-only** on the consent screen if the first job is questions about what shipped, and **full access** only when you want drafting and publishing.
4. Bring a pull request description or three bullets, ask for a draft against your last three published posts, and read the draft as a reviewer rather than an author. The value of the server is the draft you can edit in the conversation, not the published post.
5. Ask for a scheduled post before you ask for a published one. A scheduled post is the cheapest way to prove the write scope, the timezone handling and the category selection in one call.
