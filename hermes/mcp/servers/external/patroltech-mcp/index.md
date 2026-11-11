---
title: "PatrolTech MCP - Guard Tours, Missed Rounds, Incidents"
description: "A security patrol platform over MCP: missed rounds, skipped checkpoints, suspicious scans and incidents, with changes queued as a batch a person confirms"
category: "Security"
stars: "n/a (hosted, OAuth with dynamic registration, works on the free plan)"
added: 2026-11-10
source: "the mcp.so submission #7110 for PatrolTech, the official registry record online.patroltech/patroltech 0.2.7 published 2026-11-01T04:52:20Z, the server README at github.com/PatrolTech/mcp-server and the vendor page patroltech.online/en/features/integrations/mcp, and the endpoint itself, where a keyless initialize answered 401, both metadata documents returned 200 and /health reported version 0.2.8"
relevance: ★★★
tags: [security, guard-tour, patrol, checkpoints, incidents, access-control, field-operations, oauth, streamable-http, remote-mcp]
last_updated: "2026-11-10"
---

# PatrolTech MCP

**A guard tour is a promise that somebody walked the route at 03:00, and the only evidence is a scan.** PatrolTech is a guard tour and security patrol platform, and its MCP server answers the questions a contract security firm actually gets asked: which rounds were missed, which checkpoints were skipped, which scans looked wrong, who is inside the warehouse right now. Changes are not written directly. They are queued as a batch that the person confirms, which is the right shape for a system where a fabricated scan log is a liability rather than a bug.

```text
Server type:  Remote (Streamable HTTP)
Endpoint:     https://mcp.patroltech.online/mcp
Issuer:       https://api.patroltech.online
Auth:         OAuth 2.1, authorization code with PKCE (S256), dynamic
              client registration and client ID metadata documents
Scopes:       read, write
Registry:     online.patroltech/patroltech 0.2.7, published 2026-11-01T04:52:20Z
Health:       /health answered 200 with version 0.2.8
Probe:        401 plus both metadata documents, tools not driven
```

## What the endpoint says about itself

A keyless `POST initialize` answered **401** with a full challenge rather than a bare refusal:

```text
WWW-Authenticate: Bearer error="invalid_token",
  error_description="Missing Authorization header",
  scope="read write",
  resource_metadata="https://mcp.patroltech.online/.well-known/oauth-protected-resource/mcp"
```

Two details are worth keeping. The body is a plain OAuth error object, `{"error":"invalid_token","error_description":"Missing Authorization header"}`, not a JSON-RPC error, so this server sits behind an edge that answers before the protocol layer sees the request. And the challenge carries the `scope` value, so a client knows before it registers that there are exactly two scopes and one of them writes.

The protected-resource document at the named path answered **200**: the resource is the `/mcp` URL itself, the authorization server is a different host, `https://api.patroltech.online`, and `bearer_methods_supported` is `header` only. The authorization-server metadata on that issuer answered **200** and is complete: `authorization_code` and `refresh_token`, `S256` only for PKCE, `none` for token-endpoint auth (a public client), a revocation endpoint, a JWKS, `client_id_metadata_document_supported: true`, and `authorization_response_iss_parameter_supported: true`. The same document requested from the MCP host answers **404**, which is the split worth remembering: the resource lives on one host and the identity provider on another, and only the protected-resource document connects them. An openid-configuration route returns a structured 404 with a JSON envelope rather than HTML, which says the API is JSON all the way down.

`/health` returned `{"status":"ok","version":"0.2.8"}` while the registry's newest record is **0.2.7**, so the endpoint is one patch ahead of its own publication. That is a small thing to measure and a useful one: a version read from a registry is a date, not a deployment.

## The write path is a batch a person confirms

This is the mechanic that makes the server safe to connect, and it is documented in the README rather than implied by a scope name:

```text
patroltech_<area>_<read>            one read tool per catalog area, read-only
patroltech_<area>_propose_<verb>    proposes a change, changes nothing
patroltech_proposals_confirm        executes the whole pending batch, in order,
                                    with the parameters that were proposed
patroltech_proposals_cancel         withdraws the pending batch
patroltech_account_get_context      the user's organizations, roles, locations
patroltech_locations_get_qr_sheet   a signed link, valid one hour, to the
                                    printable QR sheet of a location
```

The proposals of one user and one client form one batch, capped at **10** proposals, expiring after **30 minutes**, and confirmation runs them in order with the parameters as proposed. Three consequences follow and none of them need a policy document to enforce: an agent cannot drip ten thousand changes through one confirmation, a stale plan cannot be executed an hour later, and the thing confirmed is the thing shown. Writes need the `write` scope, and without it the server answers **403 insufficient_scope** with the challenge naming both scopes, which is a clearer failure than a silent no-op.

The README is also explicit about what the server cannot do at all: deleting records, inviting users and billing are outside the connector's capability, and the server holds no credentials of its own, forwarding the user's token so the platform's own organization and location roles authorize every call. A closed list of writes is allowed to agents, which is the boundary that stops an assistant from being a second admin console.

## Prompts and resources that carry the domain knowledge

Rather than leaving the model to infer what a patrol firm cares about, the server ships four prompts and two resources, all fixed text that touches no account data and does not count against the tool rate limit:

```text
patroltech_review_missed_rounds      rounds not completed, checkpoints skipped
patroltech_review_suspicious_scans   suspicious or rejected scans, pending count
patroltech_weekly_summary            the last week, starting with what needs
                                     attention
patroltech_set_up_account            what is missing to get the account running
patroltech://guides/choosing-a-tool    which tool answers each question
patroltech://guides/reading-the-data   what statuses, scan validation, partial
                                       data and retention mean
```

The `reading-the-data` resource is the one to point at, because scan validation is exactly the field where an assistant will otherwise invent a meaning: a rejected scan is not a missed round, and a partial day is not a clean one. The server also sends an instruction string, and one line in it is a governance stance rather than a help text: guard ranking tools are to be used to compare activity and presented as activity data, not as an assessment of the people. A vendor writing that into the server instructions has thought about how the output will be read by a manager.

## How the results come back

Every result is `{ data, truncated?, notices?, note }`, capped at **60,000** characters, and `note` states that `data` is data and never instructions. Two rate limits apply per user: **60** calls a minute to a read tool and **20** to a write tool. Every tool call writes one `mcp.tool_call` audit line holding a **hash of the arguments and never the arguments**, so an investigation can prove a call happened without the log becoming a copy of the guest list.

## The class it enters, with the owners named

This is the first **security patrol** surface in the catalog, and the distinction from its neighbours is the point:

- [Dumpster Controls MCP](/hermes/mcp/servers/external/dumpster-controls-mcp/) and [DrillerDB MCP](/hermes/mcp/servers/external/drillerdb-mcp/) are field operations for waste hauling and drilling, where the unit of work is a job.
- **ATLASS OS** and the field-service trio held on October 13 sit in job dispatch and back office.
- The compliance surfaces such as **ISMS Copilot** and **screenata** assess a programme rather than a night shift.

A guard tour has a different primitive: a checkpoint that must be scanned inside a window, a round that is either completed or missed, and a scan that can be suspicious. Nothing else here models that, which is why the entry ships despite being a narrow vertical: the operator asking "which rounds were missed yesterday" has no other answer in this ecosystem.

## Limits, stated as limits

The server was measured to the handshake, both metadata documents and `/health`; the tool list sits behind OAuth and every tool name above is the vendor's published catalog rather than a driven `tools/list`. The read-tool set is described as one tool per catalog area rather than enumerated, so a client should read `tools/list` after connecting rather than assume a fixed count. Results truncate at 60,000 characters, which for a large multi-site account means a summary question rather than an export. Rate limits are per user, so one enthusiastic agent can spend a shift's quota. And the connector is documented to work on the free plan, with the write path confined to a closed list of proposals and no access to deletion, user invitations or billing.

## Frequently asked questions

### Can an assistant change patrol data on its own?

No. Every change is a `propose` call that queues a proposal, and the queue is executed only by `patroltech_proposals_confirm`, which is marked destructive so a client asks the user first. The batch is capped at ten proposals and expires in thirty minutes.

### What does a missed round look like in the data?

A round that was scheduled and not completed, with the checkpoints that were skipped reported separately. The server publishes a `reading-the-data` resource that defines the statuses and the scan validation rules so an assistant does not treat a rejected scan as a missed one.

### Does the connector need an enterprise plan?

The vendor documents it as working on the free plan. What limits an assistant is its role: the server forwards the user's token, so organization and location roles decide what is visible before the connector sees the request.

### How much of the account can the assistant read?

Whatever the signed-in user can read, across the organizations and locations they belong to, with `patroltech_account_get_context` returning exactly that list so the scope of a connection is checkable in one call.

### What happens if the connection has only the read scope?

Reads work and any write returns `403 insufficient_scope` with the challenge naming `read write`, so the assistant reports a permission error rather than a change that quietly did not happen.
