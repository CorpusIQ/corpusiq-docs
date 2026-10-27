---
title: "AXL MCP - Courses, CRM and Checkout in One Surface"
description: "Run an AXL account from Claude, ChatGPT or Cursor: courses, CRM pipelines, checkout, booking and email automation behind OAuth 2.1, with 21 sensitive operations removed from the agent surface."
category: Sales & Marketing / All-in-one Platform
stars: n/a (included with an AXL plan, free plan with no card)
added: 2026-10-26
source: "live MCP probe on app.axl.tech/mcp (initialize 401 without a token, GET 405 with the server's own stateless explanation, RFC 9728 protected-resource and RFC 8414 authorization-server documents read live) + vendor developer page axl.tech/developers/mcp + chatmcp/mcpso submission #6192 + official MCP registry searched, no entry found"
relevance: ★★★
tags: [crm, sales-pipeline, courses, checkout, email-automation, booking, oauth, all-in-one, smb]
last_updated: "2026-10-26"
---

# AXL MCP

**An all-in-one platform that can be operated from the assistant itself is a different product from an all-in-one platform with a documented API, and the difference is measurable in what the agent is allowed to touch.**

```
Server type: Remote (Streamable HTTP, stateless)
Endpoint:    https://app.axl.tech/mcp
Transport:   JSON-RPC over POST only, no GET stream, no Mcp-Session-Id
Auth:        OAuth 2.1, dynamic client registration, PKCE S256, single scope "mcp"
Tools:       a small fixed tool set over roughly 1,100 account operations (vendor figure)
Built by:    AXL EdTech Booster, LLC (axl.tech)
Registry:    no entry found in the official MCP registry at probe time
```

## Why This Matters for Operators

The tool stack a small business actually runs on is a course platform, a CRM, a checkout, a booking calendar and an email tool that were bought separately and reconciled by hand. The pain is not the price of five subscriptions, it is the gap between them: a webinar attendee who never becomes a contact, a booking that never triggers a follow-up, a page that converts but does not feed the pipeline.

An assistant wired into the whole account can close those gaps in one request, because the platform already holds every object. What decides whether that is safe is the containment: which operations were removed from the agent's reach, what the token is scoped to, and what happens when a write is refused.

## What It Actually Does

The endpoint is stateless and POST-only, and it says so rather than failing obscurely. A GET returned HTTP 405 with its own explanation:

```
Method Not Allowed: this MCP server is stateless - it exposes no GET SSE stream
and no DELETE session termination. Send JSON-RPC over POST.
```

`initialize` without a token returned HTTP 401. The discovery documents answer without the application, which is where the contract is readable:

- `/.well-known/oauth-protected-resource` returned HTTP 200: `resource: https://app.axl.tech/mcp`, one authorization server at `https://app.axl.tech`, header bearer tokens, `scopes_supported: ["mcp"]`.
- `/.well-known/oauth-authorization-server` returned HTTP 200 with authorize, token, **register** (`/oauth/register`, RFC 7591 public client) and revoke endpoints, `response_types_supported: ["code"]`, grants for authorization code and refresh token, `code_challenge_methods_supported: ["S256"]` and `token_endpoint_auth_methods_supported: ["none"]`.

Vendor-stated surface, read from the developer page rather than from a schema: roughly 1,100 admin API operations behind a small fixed tool set that the agent navigates to the right operation itself, and each successful write returns a link to the new record in the admin so the result can be inspected rather than trusted.

| What the agent can do | Where it lands in the account |
|---|---|
| Launch a page | Website builder, form, checkout, preview link returned |
| Build a course | Lessons, hosted video, enrolment, certificates |
| Organise sales | Pipeline, contacts, deals, CRM filters |
| Connect a journey | Automations, triggers, branches, messages across nine channels |
| Book and follow up | Appointments, availability, paid sessions, booking-triggered follow-up |
| Run webinars and community | Live rooms, evergreen sessions, memberships |
| Read the numbers | Analytics and attribution for what a campaign earned |

## How the Agent Is Contained

This is the part worth reading before connecting anything.

- **21 sensitive operations are removed from the AI surface in the server, not filtered in a prompt.** Billing writes, token minting, permission changes and admin creation are named as the removed set.
- **The token is an ordinary admin token.** The vendor states the production flow advertises one coarse scope, so a completed OAuth flow carries the approving admin's rights including per-field permissions. A field the approver cannot read is a field the agent cannot read.
- **Read-only is not a browser-flow scope.** The documented route to a narrower connection is an API key with read rights only, sent as a bearer token.
- **Publishing and sending stay separate actions.** The agent returns work for review rather than shipping it.
- **Writes to HTML content require the agent to echo a guide token first**, so page bodies and course-step theory refuse a write until the guide has been read.

## Limits Stated by the Vendor, and What They Mean

- **Concurrency, not rate.** A fixed number of requests in flight; sequential calls are unlimited. Over the cap the server returns 429 with `Retry-After: 1` and an `X-Concurrency-Limit` header. An agent that fans out parallel calls will meet this, and the header is the correct source rather than a hard-coded number.
- **Uploads leave the MCP surface for one step.** A begin call, a raw PUT to a pre-signed URL with no auth header, then a complete call. An agent restricted to MCP tools cannot finish an upload alone.
- **Long responses truncate at roughly 200,000 characters** with a hint to narrow the fields. The REST API is not capped this way.
- **Account scope.** The token scopes to one account, so an account in a bad billing state answers everything except billing reads, which return 403 `lockedSchoolAccessDenied`.

## Limitations Recorded

- No tool call was executed: connecting requires an AXL account, so the tool names and argument shapes in this guide are the vendor's own description and were not read from a live `tools/list`.
- The scope is coarse by design. A business that needs an agent with less than admin rights must use a read-rights API key, which the vendor documents rather than advertises.
- The ~1,100 operation figure is the vendor's count and was not enumerable without a session.
- No entry in the official MCP registry at probe time, so the registry is not a second source for this endpoint.
- Stateless transport means no server-initiated messages and no session resumption; a client that requires an SSE stream needs a bridge such as `mcp-remote`.

## FAQ

### Is this the same as pointing an agent at the REST API?
No. The REST API exposes the same surface, but an agent on MCP gets a curated tool set with 21 sensitive operations removed at the server, concurrency limiting and a write that returns a link to the created record. The REST surface has none of those guards built in.

### Can the agent take a payment or change billing?
Not through this endpoint. Billing writes are in the removed set, and billing reads return 403 on an account with a billing problem.

### Does the assistant see customer data?
It sees what the approving user can see, field by field, because the token is the admin's own. That is the trade the vendor makes for a single coarse scope.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CRM and pipeline servers in this catalog](/hermes/mcp/servers/external/customermates-mcp/)
- [CorpusIQ connectors for CRM, email and analytics](/hermes/mcp/)
