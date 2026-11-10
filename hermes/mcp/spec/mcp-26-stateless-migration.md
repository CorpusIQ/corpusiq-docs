---
title: "MCP '26 - The Stateless Protocol Migration Guide"
description: "July 28, 2026 MCP spec revision: stateless protocol, session IDs removed, refresh token rules clarified, extensions formalized. Migration checklist"
category: "MCP"
tags: ["mcp", "model context protocol", "stateless mcp", "mcp migration", "session id", "refresh token"]
last_updated: "2026-11-10"
canonical: "https://www.corpusiq.io/docs/hermes/mcp/spec/mcp-26-stateless-migration/"
robots: "index,follow"
---

# MCP '26 - The Stateless Protocol Migration Guide

On **July 28, 2026**, MCP shipped the largest spec revision since launch. The headline: the core protocol moves from stateful to stateless, and session IDs go away. This page summarizes the change, what breaks, and the migration path.

## What Changed

| Area | Before (2025-11-25) | After (2026-07-28) |
|------|---------------------|--------------------|
| Sessions | `initialize` handshake mints a session ID, sent on every request | No session. Client identifies itself on every request (like a user-agent header) |
| Capabilities | Negotiated once at initialize | Client capabilities travel in `_meta` on every request; servers expose theirs via new `server/discover` |
| Refresh tokens | Spec silent; clients behaved inconsistently | Spec now carries OAuth/OIDC refresh token guidance explicitly |
| Extensions | Undefined; developers stuffed custom behavior in `meta` | Formalized: official / experimental / unofficial tracks, reverse-DNS identifiers |
| Tasks | Experimental core feature | Moved out of core into an official extension (`io.modelcontextprotocol/tasks`) |
| Removed methods | `ping`, `logging/setLevel`, `notifications/roots/list_changed` all live | Gone. Log level is set per request via `io.modelcontextprotocol/logLevel` in `_meta` |
| Subscriptions | HTTP GET stream plus `resources/subscribe` / `resources/unsubscribe` | One long-lived `subscriptions/listen` POST-response stream, opted in per notification type |
| Discovery | Capabilities known only after `initialize` | `server/discover` is a must-implement RPC advertising supported versions, capabilities, and identity |
| Elicitation | Server could send a request at any time | Only as an embedded input request inside an `InputRequiredResult` (Multi Round-Trip Requests) |

## Why Stateless

Stateful sessions were the hidden tax of multi-user scale. A session belongs to one server instance; replicas and load balancers then need a shared session store or sticky sessions just to receive requests. The web solved this decades ago with stateless applications. MCP is adopting the same pattern: the client sends everything the server needs on every request, so any replica can answer any request.

The short-term cost is fragmentation: a client built for 2025-11-25 cannot talk to a 2026-07-28 server without version negotiation. The escape hatch: a client can declare its protocol version, and a dual-stack server can serve both. The long-term payoff is scale and stability - delete the session-handling code and a whole class of bugs goes away.

## Migration Checklist (7 Steps)

1. **Expect weird traffic.** New-protocol clients will probe your old-protocol server. Respond gracefully; watch for log floods. Nothing breaks on day zero if you handle unknown traffic well.

2. **Augment or rewrite.** Either extend your server to speak both protocols or run two implementations side by side. Keep the old code path for the dual-stack era.

3. **Inventory removed features.** `ping`, `logging/setLevel`, and `notifications/roots/list_changed` are gone, and so are the HTTP GET stream and `resources/subscribe`. If you use `roots`, `sampling`, or elicitation, they now arrive as input requests inside an `InputRequiredResult`; nothing can be pushed at the client unprompted.

4. **Implement the new protocol.** On an official SDK this is close to free - upgrade the SDK. The real work: anything that depended on the session ID (analytics, routing, per-user state) needs a new mechanism.

5. **Run the conformance suite.** The MCP project publishes an open-source conformance suite. Point it at your server. SDK users are typically green; homegrown implementations must run it.

6. **Plan the dual-stack era.** Internet-facing servers speak both protocols until old-client traffic tapers off. Enterprises that control client versions can force the upgrade and skip this.

7. **Clean up.** Delete the session store (no more Redis for session IDs), drop session-management code. Large operators report deleting more code than they added.

## What Breaks Day One

- Long-running work: servers no longer push updates on their own. The server returns a handle; the client polls it (`tasks/get`) - closer to REST. Polling logic moves to the client.
- Analytics that leaned on the session ID to identify clients must read client identity from per-request fields instead.
- Old transport habits: an HTTP GET or DELETE to the MCP endpoint now gets `405 Method Not Allowed`, a stray `Mcp-Session-Id` header is ignored rather than echoed, and `Last-Event-ID` resumption is gone - streams do not resume.

## Refresh Token Rules (New)

MCP now writes down what OAuth and OpenID Connect already documented: clients should request refresh tokens, store them, and rotate access tokens silently instead of re-prompting users. The gap showed up in production: demos work, then the next morning the refresh path breaks. The clarification makes authentication behavior consistent across clients, servers, and coding agents that generate implementations.

## Fragmentation Reality

Extensions now ship on their own cadence with their own breaking changes - a client and server can disagree on extension versions independently of the core protocol. Expect a growing support matrix: "if the client supports extension X version 3, do this; if not, do that." Something in your stack has to manage graceful degradation; the protocol will not.

## Source

Primary: the MCP specification's own [Key Changes for 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/changelog) and the [Streamable HTTP transport page](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http). Secondary: Arcade.dev, "The Complete Guide To MCP '26" - explainers by Nate Barbettini, Wils Dawson, Eric Gustin, Sterling Dreyer. 10,000+ tracked MCP servers, 97M+ monthly SDK downloads cited.
