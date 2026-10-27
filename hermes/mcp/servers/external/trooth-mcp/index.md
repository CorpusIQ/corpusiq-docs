---
title: "Trooth Network MCP - Witnessed Company Trust Records"
description: "Remote read-only, no-auth MCP server checking a company's witnessed trust record: identity, security, privacy and AI practices with source-labeled provenance, plus a live outside-in read of a domain's public security surface. Endpoint api.trooth.co/public/mcp, live-verified."
category: Security
stars: "n/a (hosted, no public repo)"
added: 2026-08-31
source: "mcpservers.org /all (newest-first page, Aug 31 midday sweep)"
relevance: ★★★
tags: [mcp-server, trust, security, due-diligence, provenance, remote]
last_updated: "2026-10-24"
---

# Trooth Network MCP

**A company's witnessed trust record, answerable from any MCP client.** Trooth runs a remote, read-only MCP server that lets an AI assistant check a company's Trust Profile, take a neutral read of a domain's public security surface, verify a signed Trust Ledger Token, or ask about Trooth itself. Every answer names its source and date; witnessed evidence is labeled apart from what a company declares, and unsettled subjects come back marked unknown rather than guessed.

```
Server type: Hosted, remote (Streamable HTTP), public and read-only
Endpoint: https://api.trooth.co/public/mcp
Auth: none (no account, no token)
Registry: io.github.trooth-eng/trooth-network
Tools: trooth_public_trust_profile, trooth_outside_in_read, trooth_verify, trooth_ask
Built by: Trooth (trooth.co)
```

## Why This Matters for Operators

Vendor and partner checks are normally a private-investigator workflow. Trooth turns the public trust layer into live agent context.

First, **provenance is structural.** Witnessed Trust Profiles and Trust Ledger Tokens are signed evidence; outside-in reads are live neutral observations. The server returns honest absences for unknown subjects instead of inventing a rating, which matters when an agent's answer feeds a procurement decision.

Second, **zero friction.** The endpoint needs no account or token, so any MCP client (ChatGPT custom connector, Claude connector, Cursor, Cline, VS Code) can add it in one paste.

Third, **it is a different data class.** Identity, security, privacy and AI-practice signals with source labels complement the financial and operational connectors an agent already has, giving diligence answers a second axis.

## Tools and Capabilities

| Tool | What it returns |
|------|-----------------|
| `trooth_public_trust_profile` | A company's witnessed Trust Profile or Network standing, with provenance |
| `trooth_outside_in_read` | A live, neutral read of a domain's public security surface |
| `trooth_verify` | Re-verify a signed Trooth Trust Ledger Token |
| `trooth_ask` | Ask about Trooth (products, methodology, pricing) |

## Verification (Aug 31, 2026)

- **Live JSON-RPC initialize verified**: POST to `https://api.trooth.co/public/mcp` returned `trooth-mcp v1.1.0` with tools/resources/prompts capabilities and instructions describing the read-only trust layer.
- README documents the endpoint, the four tools, and official MCP Registry record `io.github.trooth-eng/trooth-network`.
