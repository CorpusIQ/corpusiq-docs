---
title: "GridWhy MCP - Google Maps Geo-Grid Rank Tracking"
description: "A hosted MCP server that turns local Google Maps rank into a geo-grid history and names the reason a client's positions moved."
category: "SEO / Local Search"
stars: "0 (closed source; three tools documented, no keyless tier)"
added: 2026-11-14
source: "the mcp.so feed, which stamped this slug twice on 2026-11-14 at 16:14Z and 17:33Z, the official registry records com.gridwhy/gridwhy 1.0.0 and 1.1.0, and a measured handshake against https://gridwhy.com/mcp on the same day: initialize 401 with the challenge header, the protected-resource document 200, the authorization-server document 200, plus the vendor pages gridwhy.com/docs/mcp and gridwhy.com/pricing"
relevance: ★★★
tags: [seo, local-seo, google-maps, rank-tracking, geo-grid, google-business-profile, agencies, oauth, remote-mcp]
last_updated: "2026-11-14"
---

# GridWhy MCP

**A local business does not rank at one position on Google Maps. It ranks at a different position depending on where the searcher is standing, and the number in the rank tracker is one sample of that surface taken from an address the searcher does not have.** That is the failure an agency walks into: the dashboard says position 4, the owner drives to a client three miles away, searches the same term, and finds the business on page two. Neither number is wrong and the pair is unexplainable, because a single rank cannot describe a field.

GridWhy measures the field. It lays a grid of sample points around a tracked location, checks where the business appears at each one, and keeps the result as a history rather than a number: **how many grid points rank in the top 20 and the top 3**, the average and the best rank across the grid, and a one-line note on what changed since the previous scan. The interesting half is the second tool, which decomposes the change into named causes instead of asking the reader to guess.

```
Server type:   remote Streamable HTTP, JSON-RPC 2.0
Endpoint:      https://gridwhy.com/mcp
Server:        GridWhy, OAuth resource https://gridwhy.com/mcp
Registry:      com.gridwhy/gridwhy 1.0.0 published 2026-11-12T17:53:32Z,
               1.1.0 published 2026-11-12T19:27:04Z and marked latest
Auth:          OAuth 2.1 with dynamic client registration, or a gw_ API key
Scopes:        read, scan
Tools:         3 (get_history, explain_change, run_scan)
Listed on:     mcp.so, category Data & Analytics, last updated 2026-11-14,
               with no tool list published by the directory
Not affiliated with Google
```

## The evidence tier

Measured at the handshake, not driven. There is no keyless path to this server and no public demo credential, so what follows is the door and the documented surface rather than a session of tool calls, and the guide says which claims came from which of the two.

A keyless `initialize` to `https://gridwhy.com/mcp` answers **401** with a challenge that names everything needed to connect:

```
HTTP 401
Www-Authenticate: Bearer realm="gridwhy",
  resource_metadata="https://gridwhy.com/.well-known/oauth-protected-resource/mcp",
  scope="read scan"

{"jsonrpc":"2.0","id":null,"error":{"code":-32001,
 "message":"Missing or malformed API key. Send Authorization: Bearer ***
 (create one at /app/settings/api)."}}
```

That 401 is better than most: it points at the metadata document instead of making a client fail with a bare "unauthorized", and the error body names the page where a human creates a key. The protected-resource document answers **200** and is complete, which is the part that separates a real OAuth deployment from a server that merely answers 401:

```json
{"resource":"https://gridwhy.com/mcp",
 "authorization_servers":["https://gridwhy.com"],
 "bearer_methods_supported":["header"],
 "scopes_supported":["read","scan"],
 "resource_name":"GridWhy",
 "resource_documentation":"https://gridwhy.com/docs/mcp"}
```

The authorization-server document at `/.well-known/oauth-authorization-server` answers **200** with `issuer` `https://gridwhy.com`, `/oauth/authorize`, `/oauth/token`, `/oauth/register`, `/oauth/revoke`, `response_types_supported` `["code"]`, `grant_types_supported` `["authorization_code","refresh_token"]`, `token_endpoint_auth_methods_supported` `["none","client_secret_post","client_secret_basic"]`, `code_challenge_methods_supported` `["S256"]` and `authorization_response_iss_parameter_supported` true. `/.well-known/openid-configuration` answers **404**: this is an OAuth resource server, not an identity provider, and a client that only tries OIDC discovery will conclude the server has no metadata.

The registration endpoint matters for a practical reason. It is what lets Claude and ChatGPT connect from the URL alone, and the vendor says so in its own instructions: paste `https://gridwhy.com/mcp`, keep the authentication options the client marks "Detected", and the client registers itself. No key to copy, no support ticket.

**Two scopes, and the split is the design.** The consent screen separates `read` (locations, scan history, what changed) from `scan` (start scans, which spend the account's manual scan allowance). An agency that wants a client-facing assistant to answer questions about rankings can approve `read` alone and know the connection cannot burn the scan budget. That is a narrower grant than a read-write key, and it is the reason this server earns a guide while the rest of the local SEO shelf is GBP management and citation work.

## The tool surface

Three tools, all optional-argument, from the vendor's own MCP documentation page.

| Tool | Arguments | What it returns |
|---|---|---|
| `get_history` | `location`, `keyword`, `keyword_id`, `limit` | Locations, tracked keywords and their scans newest first: grid points ranking in the top 20 and top 3, average and best rank, a one-line "what changed", a report link. Called with no arguments it returns every keyword with its latest scan and the manual scans left. |
| `explain_change` | `scan_id`, or `location` plus `keyword` / `keyword_id` | Why the ranking moved between a scan and the one before it: findings on **coverage**, **competitors that rose or appeared**, **review velocity**, **rating**, and **category or name changes**, each with a line to paste to the client, plus next steps. |
| `run_scan` | `location`, `keyword`, `keyword_id` | Starts a grid scan for one tracked keyword now, on top of the schedule. Takes 15 to 30 seconds. Returns a `scan_id` for `explain_change`. A keyword's first scan is free. |

`explain_change` is the product. Five causes are named, and four of them are things a local business can act on inside a week: a competitor entered the grid, a competitor accumulated reviews faster, a rating dropped, or the primary category or the business name changed. The fifth, coverage, is the honest one: nothing about the business changed, the neighbourhood around the grid did. An agency that can say which of those five happened, with the client's own numbers attached, is doing a different job from the one that forwards a rank.

The scan is scheduled weekly or fortnightly by plan, so the history exists whether or not anybody calls a tool. That resolves the usual objection to scan-on-demand servers: the agent is not paying 30 seconds of scan latency to answer "how did last week go", it is reading a scan that already ran.

## What it costs, and the limits that shape the design

| Plan | Price | Locations | Grid | Manual scans on top of the schedule | MCP and API calls an hour |
|---|---|---|---|---|---|
| **Solo** | **29 dollars a month**, 290 a year | 5, 10 keywords each | **5x5** | 5 a day, 30 per 30 days | **100** |
| **Agency** | **69 dollars a month**, 690 a year | 10, up to 200 keywords | **7x7** | 20 a day, 100 per 30 days | **500** |
| **Agency+** | **129 dollars a month**, 1,290 a year | 25, up to 500 keywords | **7x7** | 50 a day, 250 per 30 days | **2,000** |

A 5x5 grid is **25 sample points** and a 7x7 grid is **49**, so the metric an agency quotes a client is "11 of 25 points in the top 3", not "position 4". Weekly scans on Solo and Agency, weekly or fortnightly on either, white-label reports from Agency up, history kept forever on every plan, run log for every scan.

Two facts belong beside the price rather than in a footnote. **The MCP server is included on every plan**, including Solo, so access is not an upsell and there is no per-call charge and no credit balance. And **scheduled scans are never limited by the API quota**: the 100, 500 and 2,000 calls an hour are a ceiling on agent traffic, not on the product doing its job.

Billing runs through Paddle as merchant of record, prices are in USD excluding tax, there is a 14 day trial, and refunds are 30 days from the first payment.

**One contradiction is worth recording rather than smoothing over.** The MCP documentation's limits section states "The free trial has Solo's limits", while the pricing page states the trial is "14 days with the full Agency feature set". A prospect reading both pages gets two different answers about what the trial includes, and a guide that picks one silently is guessing. Test the trial yourself before promising a client 7x7 during it.

## The REST surface mirrors the tools

The same three operations are served as JSON under `/api/v1` with the same key and the same quotas, which is the sensible shape for this class: a scheduled report generator on the agency's own box should not have to speak MCP to pull a history.

```
GET  https://gridwhy.com/api/v1/history?location=Wilson&keyword=plumber&limit=5
GET  https://gridwhy.com/api/v1/explain?scan_id=<scan id>
POST https://gridwhy.com/api/v1/scans   {"location":"...","keyword":"..."}   -> 202 Accepted
```

Errors arrive as `{"error": "..."}` with **400, 401, 403, 404, 409 or 429**, and the 429 carries `Retry-After`. A 409 on a scan start is the shape you want from a service that can already have a scan running for that keyword: it is a conflict, not a silent duplicate.

Keys start with `gw_` and are shown once, in Settings, API and MCP. A key acts for the whole workspace, so the key an agency hands a client-side assistant is the key that can reach every location in the account, which is the argument for OAuth with `read` only rather than a shared key. Connected apps and keys draw on the same limits, and disconnecting an app stops it at once.

## Where the grid idea stops

The honest limits, in the vendor's own numbers and in what the surface does not offer.

- **The grid is fixed per plan.** 25 points on Solo, 49 on Agency and Agency+, and the documentation exposes no argument to change the grid size, the radius or the point density. An urban client in a dense market and a rural client covering 40 miles are measured with the same geometry.
- **The cause list is bounded at five.** Coverage, competitors, review velocity, rating, category or name. A rank can also move because the searcher's device, the query intent or the map's own testing changed, and none of those appear among the findings.
- **Fifteen to thirty seconds per manual scan, one keyword at a time.** `run_scan` takes a single keyword, so a ten-keyword refresh is ten calls against the hourly quota.
- **No payload was measured.** Nothing in this guide describes the JSON shape of a `get_history` or an `explain_change` response, because the account behind this pass had no key. The fields above are the vendor's description of them.
- **The directory does not publish the tool list.** The mcp.so listing for this server says a tool list is not available yet and that discovery may require signing in, which is exactly the case here: the surface above came from the vendor's documentation, and a client that connects will get the authoritative schemas from `tools/list`.

## Frequently asked

### What does the MCP server actually return?

For `get_history`, a per-keyword row of scans with the count of grid points in the top 20 and the top 3, the average and the best rank, a short "what changed" sentence and a report link. For `explain_change`, a set of findings with client-ready lines and next steps. For `run_scan`, a scan identifier that `explain_change` accepts.

### Why does a geo-grid need 25 or 49 points?

Because rank on Google Maps is a distance function, not a position. Sampling one address gives you one number; sampling 25 points tells you how far the map pack extends around the business and which side of it is weak, which is the question a client is really asking when they say they dropped.

### Can a client connect read-only?

Yes, and it is the better path. The OAuth consent separates `read` from `scan`, so a connection approved for `read` can read locations, history and change explanations and cannot start a scan or spend the account's manual allowance. A key, by contrast, acts for the entire workspace.

### What happens when the trial ends or the plan is cancelled?

The vendor states that a key stops working and connected apps get a clear error until a plan is picked. The grid history is kept, and history is never deleted on any plan, so the data is not lost while the account is dormant.

### Does it work without an account?

No. Every path in is an account: OAuth through a GridWhy sign-in, or a `gw_` key created in settings. There is a free local rank checker on the vendor site for a one-off look, but the MCP server itself has no anonymous tier.

## What to check before you connect a client

1. Confirm the plan's grid size against the client's geography: 25 points on Solo is a tight radius.
2. Approve `read` if the assistant only answers questions, and `scan` only where somebody will actually press the button.
3. Compare the scan schedule to the promise being made. Weekly on Solo and Agency is a weekly story, not a live one.
4. Watch the hourly call ceiling on Agency (500) if several assistants share one key.
5. Decide who owns the client-facing wording. `explain_change` returns a line to paste; an agency's voice should still edit it.
