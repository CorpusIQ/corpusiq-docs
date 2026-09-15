---
title: Slidingbox Hydrate/Dehydrate - Burn-After-Reading Secret
description: "MCP server that hands a secret from one agent, machine, or person to another without leaving a copy behind: store_secret encrypts locally with AES-256-GCM and returns one token; the first successful read delivers the secret and destroys it. ISC, stdio via npx, Node >=20."
category: Security
npm: "@slidingbox/hydrate-dehydrate-mcp (v0.1.5)"
added: 2026-09-02
source: "chatmcp/mcpso issue #3886 (Sep 2, 2026)"
relevance: ★★
tags: [mcp-server, security, secrets, encryption, handoff, agents, stdio]
---

# Slidingbox Hydrate/Dehydrate

**Hand a secret to another agent without leaving a copy behind.** Slidingbox Hydrate/Dehydrate is a local stdio MCP server that turns a secret into a single-use token: `store_secret` encrypts the value locally (AES-256-GCM) and returns a token; the first successful read delivers the secret and destroys it server-side, and a second read returns nothing. The server only ever holds ciphertext - the decryption key travels inside the token and is never stored or transmitted separately.

```
Server type: stdio (local)
Install: npx -y @slidingbox/hydrate-dehydrate-mcp (Node >=20)
Package: @slidingbox/hydrate-dehydrate-mcp v0.1.5 (npm, ISC license)
Stack: zod, viem, @x402/evm + @x402/fetch, @modelcontextprotocol/sdk
Homepage: slidingbox.ai | Docs: slidingbox.ai/developers
```

## Why This Matters for Operators

Secret handoff is the weak point in every agent pipeline.

First, **no shared vault needed for one-time transfers.** When an agent needs to pass an API key, a webhook URL, or a short-lived credential to another agent or to a person, the vault becomes a permanent copy with a permanent blast radius. Slidingbox's model is the paper envelope: encrypt locally, hand over the token, the recipient's first read consumes it.

Second, **ciphertext-only server state.** The server never sees the plaintext (encryption happens in the caller) and never sees the key (it travels in the token). A server compromise yields unusable ciphertext and expired tokens, not credentials.

Third, **the x402 stack underneath.** The dependency set includes `@x402/evm` and `@x402/fetch`, so the server rides on the x402 HTTP auth/verification layer rather than a bespoke protocol - relevant for agents that already negotiate pay-per-request or signed-request flows.

## Tools and Capabilities

| Capability | Description |
|-----------|-------------|
| `store_secret` | Encrypt a secret locally (AES-256-GCM) and return a one-time token |
| Read + destroy | First successful read delivers the secret and destroys it; a second read returns nothing |

## Verification (Sep 2, 2026)

- npm package verified published: @slidingbox/hydrate-dehydrate-mcp v0.1.5, bin `hydrate-dehydrate-mcp`, engines node >=20, ISC.
- Dependency stack verified (zod, viem, @x402/evm, @x402/fetch, MCP SDK).
- Submitted via chatmcp/mcpso issue #3886 with install config for stdio clients (Claude Desktop, Cursor).
- Local-only design (stdio): no remote endpoint to probe; verification is package + source level.
