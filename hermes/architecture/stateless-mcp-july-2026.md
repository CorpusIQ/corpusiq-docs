---
title: Stateless MCP — What the July 2026 Spec Means for Business AI
description: "Setup and usage guide for Stateless MCP — What the July 2026 Spec Means for Business AI. Part of the Hermes resource directory."
last_updated: 2026-08-12
canonical: "https://www.corpusiq.io/docs/hermes/architecture/stateless-mcp-july-2026/"
robots: "index,follow"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Stateless MCP — What the July 2026 Spec Means for Business AI

The MCP specification update on July 28, 2026 eliminated sessions, handshakes, and persistent connections. MCP is now fully stateless — every request carries its own protocol version, method, and authentication.

This matters for business operators because it removes the single biggest barrier to connecting real business data to AI: infrastructure complexity.

## The Old Way (Pre-July 2026)

MCP required a persistent WebSocket or SSE connection. The server had to maintain session state. If the connection dropped, the session was lost. This meant:

- Servers needed to be always-on, stateful processes
- Load balancing was difficult (sticky sessions required)
- Scaling meant managing connection pools
- Every new connector added connection overhead

## The New Way (Post-July 2026)

A single HTTP POST carries everything. No handshake. No session ID. No persistent connection.

```
POST /mcp HTTP/1.1
MCP-Protocol-Version: 2026-07-28
Mcp-Method: tools/call
Mcp-Name: search
Authorization: Bearer <token>

{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"search","arguments":{"q":"current revenue"}}}
```

This is the same pattern REST APIs have used for decades. Any HTTP server can serve MCP. Any load balancer can distribute requests. Any CDN can cache where appropriate.

## Why This Matters for Business Data

Stateless MCP means business data connectors can be:

**Read-only and ephemeral.** Each request authenticates independently. No data is stored on the MCP server between calls. The connector fetches live data, returns it, and forgets.

**Per-user scoped.** Each user's OAuth token travels with the request. Shopify data stays in Shopify's tenant. QuickBooks data stays in QuickBooks. The MCP layer never aggregates or stores.

**Infrastructure-independent.** No WebSocket servers to maintain. No session state to manage. Standard HTTP infrastructure works — Cloudflare, AWS ALB, nginx.

**Cross-AI compatible.** The same connector serves ChatGPT, Claude, Perplexity, and any other MCP-compatible AI. The user chooses their AI. The data layer stays consistent.

## What CorpusIQ Adds

Stateless MCP solves the transport problem. But business operators need more than transport:

- **40+ pre-built connectors** for Shopify, QuickBooks, Stripe, GA4, Meta Ads, HubSpot, and more
- **Metric definitions** that ensure revenue means the same thing across every AI and every connector
- **Source-of-truth validation** that traces every answer back to the original system
- **Read-only OAuth** so no AI can modify your business data
- **Zero data storage** — the connectors fetch and return, nothing persists

The stateless MCP spec makes this architecture possible at scale. No connection pools. No session affinity. No state to lose.

## The Industry Shift

Amazon Bedrock AgentCore adopted stateless MCP immediately. Google published scaling guidance. Simon Willison called it the update that "recaptured his interest" in MCP.

The direction is clear: AI data access is moving toward stateless, authenticated, per-request patterns. The same architecture that made REST APIs the backbone of the web is now coming to AI tool access.

For business operators, this means your QuickBooks, Shopify, and Stripe data can reach any AI you use — without building infrastructure, managing connections, or storing data in intermediate systems.

## Learn More

- [MCP 2026-07-28 Specification](https://modelcontextprotocol.io/specification/2026-07-28)
- [Stateless MCP Blog Post](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
- [Simon Willison on Stateless MCP](https://simonwillison.net/2026/Jul/31/stateless-mcp/)
- [Google Cloud: Scaling AI Agent Infrastructure](https://developers.googleblog.com/scaling-ai-agent-infrastructure-with-the-mcp-stateless-updates/)
