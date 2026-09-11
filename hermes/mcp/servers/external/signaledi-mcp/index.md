---
title: "SignalEDI MCP - X12 EDI Workflows for Agents"
description: "Developer MCP server from SignalEDI that connects AI assistants to X12 EDI integration work: public docs discovery, synthetic fixtures, parse and validate 850/810/856/837P transactions, and profile-gated sandbox or production connections with least-privilege scopes and QuickBooks adapters."
category: ERP
stars: n/a (new listing)
added: 2026-09-11
source: mcpservers.org /all via r.jina.ai
relevance: ★★★
tags: [edi, x12, supply-chain, b2b-integration, quickbooks, erp, self-hosted]
---

# SignalEDI MCP

**Self-hosted MCP server (stdio, npm package, profile-gated)** - SignalEDI's AI-native developer experience for X12 EDI. Instead of hand-reading implementation guides, an agent searches the bundled docs, generates synthetic fixtures, parses and validates 850/810/856 and 837P transactions, and works governed connections up through a go-live handoff, with the model confined to the capability profile you activate.

```
Server type: Self-hosted (stdio over npm; Node 22+)
Auth: Keyless docs profile by default; sandbox and production profiles need provisioned keys
Package: @signaledi/mcp-server (npm)
Registry: io.github.SignalEDI/mcp-server
Profiles: docs (keyless) / sandbox / production
Category: ERP
Built by: SignalEDI
```

## Tools

| Tool / group | What the agent can call |
|---|---|
| search_docs | Search the bundled public developer index and return resource URIs with provenance |
| get_document_schema | Public starter for the local X12 inventory: 850/810/856 baseline or 837P partial |
| Parse / validate | X12 transaction parsing and validation against the platform contract |
| Transaction tools | 850/810/856/837P transaction reads under document scopes |
| Partner-kit | Generic partner-kit discovery and sandbox-gated kit reads |
| QuickBooks adapters | QBO status, entity browsing, sync, and dry-run or live export with production-gated scopes |

## Connection

1. `npm install @signaledi/mcp-server` (Node 22+), or run via npx from your MCP client.
2. Set SIGNALEDI_MCP_PROFILE. Leave it unset (or `docs`) for keyless documentation and local fixtures; `sandbox` and `production` need separately provisioned platform keys.
3. The profile is a least-capability boundary: the model cannot pick it, tool discovery is restricted to the active profile, and production delivery requires an active immutable production version.

Domain scopes stay least-privilege: connection inventory needs platform:connections:read, drafts add platform:connections:write, production config and go-live handoff add platform:connections:production, and QuickBooks entity rows require platform:data:sensitive. Deprecated umbrella-only credentials are rejected by domain-scoped operations.

## Verification (Sep 11, 2026 night sweep)

Not live-probed (stdio package, no public endpoint). Directory listing published by SignalEDI carries the full profile matrix, the scope table and the MCP SDK 1.30.0 dependency; the npm package resolves and the registry entry io.github.SignalEDI/mcp-server is documented. The docs profile is keyless by design, so the first install works with zero credentials.

## See Also

- [Wafeq MCP - Accounting Books for Agents](/hermes/mcp/servers/external/wafeq-mcp/)
- [Soprano Connect MCP - Multi-Channel Business Messaging for Agents](/hermes/mcp/servers/external/soprano-connect-mcp/)
