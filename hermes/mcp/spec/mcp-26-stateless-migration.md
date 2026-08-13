---
title: "MCP '26 — The Stateless Protocol Migration Guide"
description: "July 28, 2026 MCP spec revision: stateless protocol, session IDs removed, refresh token rules clarified, extensions formalized. Migration checklist, breaking changes, and what it means for servers and gateways."
category: "MCP"
tags: ["mcp", "model context protocol", "stateless mcp", "mcp migration", "session id", "refresh token"]
last_updated: "2026-08-12"
canonical: "https://www.corpusiq.io/docs/hermes/mcp/spec/mcp-26-stateless-migration/"
robots: "index,follow"
---

# MCP '26 — The Stateless Protocol Migration Guide

On **July 28, 2026**, MCP shipped the largest spec revision since launch. The headline: the core protocol moves from stateful to stateless, and session IDs go away. This page summarizes the change, what breaks, and the migration path.

## What Changed

| Area | Before (2025-11-25) | After (2026-07-28) |
|------|---------------------|--------------------|
| Sessions | `initialize` handshake mints a session ID, sent on every request | No session. Client identifies itself on every request (like a user-agent header) |
| Capabilities | Negotiated once at initialize | Client capabilities travel in `_meta` on every request; servers expose theirs via new `server/discover` |
| Refresh tokens | Spec silent; clients behaved inconsistently | Spec now carries OAuth/OIDC refresh token guidance explicitly |
| Extensions | Undefined; developers stuffed custom behavior in `meta` | Formalized: official / experimental / unofficial tracks, reverse-DNS identifiers |
| Tasks | Experimental core feature | Moved out of core into an extension |
| Deprecated | - | `roots`, `sampling`, `logging` slated for deprecation |
| Elicitation | Server could send at any time | Only in response to a client request, with new constraints |

## Why Stateless

Stateful sessions were the hidden tax of multi-user scale. A session belongs to one server instance; replicas and load balancers then need a shared session store or sticky sessions just to receive requests. The web solved this decades ago with stateless applications. MCP is adopting the same pattern: the client sends everything the server needs on every request, so any replica can answer any request.

The short-term cost is fragmentation: a client built for 2025-11-25 cannot talk to a 2026-07-28 server without version negotiation. The escape hatch: a client can declare its protocol version, and a dual-stack server can serve both. The long-term payoff is scale and stability - delete the session-handling code and a whole class of bugs goes away.

## Migration Checklist (7 Steps)

1. **Expect weird traffic.** New-protocol clients will probe your old-protocol server. Respond gracefully; watch for log floods. Nothing breaks on day zero if you handle unknown traffic well.

2. **Augment or rewrite.** Either extend your server to speak both protocols or run two implementations side by side. Keep the old code path for the dual-stack era.

3. **Inventory deprecated features.** If you use `roots`, `sampling`, or `logging`, plan a path off them. If you use elicitation, check the new constraints (request-response only).

4. **Implement the new protocol.** On an official SDK this is close to free - upgrade the SDK. The real work: anything that depended on the session ID (analytics, routing, per-user state) needs a new mechanism.

5. **Run the conformance suite.** The MCP project publishes an open-source conformance suite. Point it at your server. SDK users are typically green; homegrown implementations must run it.

6. **Plan the dual-stack era.** Internet-facing servers speak both protocols until old-client traffic tapers off. Enterprises that control client versions can force the upgrade and skip this.

7. **Clean up.** Delete the session store (no more Redis for session IDs), drop session-management code. Large operators report deleting more code than they added.

## What Breaks Day One

- Long-running work: servers no longer push updates on their own. The server returns a handle; the client polls it - closer to REST. Polling logic moves to the client.
- Analytics that leaned on the session ID to identify clients must read client identity from per-request fields instead.

## Refresh Token Rules (New)

MCP now writes down what OAuth and OpenID Connect already documented: clients should request refresh tokens, store them, and rotate access tokens silently instead of re-prompting users. The gap showed up in production: demos work, then the next morning the refresh path breaks. The clarification makes authentication behavior consistent across clients, servers, and coding agents that generate implementations.

## Fragmentation Reality

Extensions now ship on their own cadence with their own breaking changes - a client and server can disagree on extension versions independently of the core protocol. Expect a growing support matrix: "if the client supports extension X version 3, do this; if not, do that." Something in your stack has to manage graceful degradation; the protocol will not.

## Source

Arcade.dev, "The Complete Guide To MCP '26" - explainers by Nate Barbettini, Wils Dawson, Eric Gustin, Sterling Dreyer. 10,000+ tracked MCP servers, 97M+ monthly SDK downloads cited.
