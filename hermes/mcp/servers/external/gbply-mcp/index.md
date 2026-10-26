---
title: "GBPly MCP - Google Business Profile With Approval Gates"
description: "Google Business Profile over MCP: reviews, posts, Q&A, ranks and citations to read, and every write behind a request that expires in fifteen minutes."
category: Marketing / Local Business
stars: n/a (paid platform, connector included with a GBPly account)
added: 2026-10-26
source: "live MCP probe on mcp.gbply.net/v1 (HTTP 401 unauthorized, tools/list 401) + RFC 9728 protected resource + authorization server metadata from the vendor's own OAuth server + vendor AI connector documentation + mcpservers.org card"
relevance: ★★★
tags: [google-business-profile, local-seo, reviews, local-marketing, approval-queue, oauth, multi-location, agencies]
---

# GBPly MCP

**The permission model most agent integrations are missing: the assistant can prepare anything and commit almost nothing.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.gbply.net/v1
Transport:   JSON-RPC 2.0 over HTTP
Auth:        OAuth 2.1 with dynamic client registration, no API key needed
Tools:       not readable without a session
Built by:    GBPly (gbply.net)
Registry:    not listed in the official MCP registry
```

## Why This Matters for Operators

Google Business Profile is where a local business is actually judged: hours, photos, review replies, the posts nobody has time to write. An assistant that can read the profile and draft the replies removes most of that work. An assistant that can also *publish* them is the point where most operators stop, correctly, because a wrong reply under the business name is public within seconds.

GBPly resolves that by making the write path a request rather than a tool call: the assistant proposes, the operator approves, and the proposal carries an expiry and a single use. This is the closest thing in this catalog to an approval contract that a business owner can reason about without reading the source.

## What It Actually Does

`initialize` on the endpoint returned **HTTP 401** with `{"error":"unauthorized"}`, and `tools/list` returned 401 as well, so the tool schemas were not read directly. The capability below comes from the vendor's own connector documentation and from the discovery documents the server publishes about itself, and each claim is labelled by where it came from.

The `WWW-Authenticate` header points at `https://mcp.gbply.net/functions/v1/mcp/.well-known/oauth-protected-resource`, which itself answers `{"error":"not_found","use":"https://mcp.gbply.net/v1"}`; the live protected resource document sits at the ordinary path, `/.well-known/oauth-protected-resource`, and returns `resource: https://mcp.gbply.net/v1`, a single authorization server at `https://mcp.gbply.net/oauth`, header bearer tokens, and `resource_name: GBPly`. **No `scopes_supported` field is published for the resource.**

The authorization server metadata at `https://mcp.gbply.net/oauth/.well-known/oauth-authorization-server` is explicit about what a token is for: `scopes_supported: ["email","profile","offline_access"]`, `response_types_supported: ["code"]`, authorization code and refresh grants, PKCE `S256`, and `token_endpoint_auth_methods_supported: ["none","client_secret_basic","client_secret_post"]` against a registration endpoint.

That is the interesting finding: the token carries **identity scopes only**, not `reviews:write` or `posts:write`. Authorization granularity for business data lives in the product's own approval system rather than in the OAuth grant, which is a legitimate architecture and the opposite of the eight resource scopes `Leadpages MCP` publishes. It means the access token can never be the whole story, and the audit trail has to be the request record.

### The capability, as the vendor documents it

| Layer | What happens |
|---|---|
| Read | Workspaces and profiles, profile details and completeness, performance insights (Google's data runs 2-3 days behind), monthly search terms, reviews and rating stats, posts, photos, Q&A, Profile Guard changes, Rank Tracker scans and results, citation scans, analysis reports, credit balances |
| Draft | AI review replies and AI Q&A suggestions, and cost previews for a Rank Tracker scan. Nothing is saved or posted |
| Ask approval | Publishing, scheduling, editing or deleting a review reply or a post; publishing a saved FAQ; editing description, phone, website, hours, special hours, services or categories; accepting, dismissing or reverting a Profile Guard change; running a Rank Tracker scan, a citation scan or an industry analysis |
| Direct | Syncing a profile from Google, a few times an hour |

Billing, plan changes, workspace members, connecting Google accounts, review-request contact lists, account deletion and data export are deliberately **not** exposed to the connector.

### The approval mechanics

A write creates a request with a link. The request shows exactly what will happen: the reply or post text, the image, the current and the new value of a field, or the credit cost. Approve or reject individually, or approve all when a week of posts is waiting. Requests **expire after fifteen minutes and can only run once**, and on approval GBPly re-checks that the operator still has permission, has enough credits, and is inside plan limits and the daily post cap. A post that fails the post-policy check is kept as flagged, not published.

There is an opt-out per action class, and it is scoped rather than global. On the Connected assistants tab an operator can switch on *Always allow* for: publish to Google (posts, post edits, review replies, FAQs), change my Google profile, spend credits, and delete things that are not live yet. The spend class carries a **most-per-request and a most-per-24-hours limit**. Settings belong to one assistant in one workspace, a second app or workspace starts with everything off, and a workspace owner can switch off members' use of Always allow entirely. In a 2FA-required workspace, Always allow can only be turned on from a 2FA sign-in. Every auto-approved action is labelled *Auto-approved* in the activity record.

Permissions are inherited rather than granted: the assistant gets exactly the operator's permissions in each workspace, so viewers can read and draft but cannot create requests, staff and admin features are never reachable through the connector, and demo profiles are read-only. Usage is rate-limited per person, and when a limit is hit the assistant is told how many seconds to wait instead of being handed an opaque error.

## What It Does Not Do

- No tool list was read, so no argument names appear in this guide; everything above is vendor documentation plus discovery documents.
- It is not a generic Google Business Profile reader. Read-only access already exists in this catalog as `Localith MCP`, and citations across directories as `Listings API MCP`; the reason to pick this one is the write path and the approval trail.
- Nothing here manages spend outside GBPly credits, and the connector itself cannot touch billing or plan changes.
- Google performance data lags two to three days, which matters if an operator wants to judge a post by the next morning.
- A self-hosted alternative exists for teams who will not send profile data to a vendor: `OpenGMB` runs the same class of function from Docker, with Google API approval of its own.

## FAQ

### Why does the token have no business scopes?
Because the vendor enforces authorization per action inside the product. Identity scopes plus a same-tenant account is enough to establish who is asking; what may be done is decided per request against the operator's own role and plan limits. It is a defensible design, and it makes the request record the authoritative audit rather than the consent screen.

### What stops an assistant from publishing something wrong while I am away?
The default. Every write waits on the Assistant requests page with a fifteen-minute expiry, and nothing publishes until an approve click that re-validates permission, credits and caps at that moment.

### Can a whole week of posts be handled in one sitting?
Yes: draft them, then approve all when the batch is waiting. Each request still runs once and still expires, so a stale queue cannot publish itself later.

### Is the $ per action a credit system?
Credits are the vendor's own usage currency, and actions that spend them are in the approval class with a per-request and per-24-hour ceiling, so an agent cannot drain a balance in a loop.

## The Operator Test

Ask it which reviews have gone unanswered and have it draft the replies. Read the drafts on the request screen before approving anything, then decide whether the writes are good enough to switch on *Always allow* for review replies only - not for the profile fields.

Pairs with `listings-api-mcp` for citations and `localith-mcp` for read-only profile analysis, and with the AI visibility entries in this catalog, because local answers are increasingly assembled from exactly this surface.
