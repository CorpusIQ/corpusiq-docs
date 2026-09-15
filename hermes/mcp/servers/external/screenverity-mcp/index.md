---
title: ScreenVerity MCP - U.S. Exclusion and Debarment Screening
description: Free MCP server for U.S. exclusion, debarment and licence screening that returns structured results plus an Ed25519-signed receipt naming the exact list snapshots checked, so a clear result stays auditable.
category: Compliance
stars: n/a (new listing)
added: 2026-08-26
source: "mcp.so GitHub issue #3769"
relevance: ★★
tags: [compliance, screening, debarment, sanctions, vendor-due-diligence, audit, stdio, self-hosted]
---

# ScreenVerity MCP

**Self-hosted MCP server (stdio via npx)** - ScreenVerity is a free MCP server for U.S. exclusion, debarment and licence screening. It returns structured JSON results plus an Ed25519-signed receipt naming the exact list snapshots checked, so a "clear" verdict can be audited after the fact. Three tools, no API key, no account: `screen`, `sources` and `verify_receipt`. MIT licensed, published in the official MCP registry as `io.github.williamblakecunningham-max/screenverity-mcp`.

```
Server type: Self-hosted (stdio)
Auth: None - no API key, no account
Install: npx screenverity-mcp
Tools: 3 (screen, sources, verify_receipt)
Pricing: Free
Category: Compliance
Built by: ScreenVerity (screenverity.com)
```

## Why This Matters for Operators

Vendor onboarding normally ends at a spreadsheet check: someone searched an exclusion list once, wrote "clear" and moved on. Six months later there is no evidence the check happened, which lists were loaded, or what snapshot was current.

**ScreenVerity makes screening self-auditing.** Every result carries an Ed25519-signed receipt naming the exact list snapshots checked, so a clear verdict can be verified later with `verify_receipt` - or kept as compliance evidence. The `sources` tool reports which lists are loaded and which are not, so coverage is explicit instead of implied. The vendor is honest about scope: it does not claim nationwide coverage.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `screen` | Screen an entity against loaded exclusion, debarment and licence lists |
| `sources` | Report exactly which lists are loaded and which are not |
| `verify_receipt` | Cryptographically verify a previous screen's signed receipt |

## Installation

```bash
npx screenverity-mcp
```

## Configuration

```json
{
  "mcpServers": {
    "screenverity": {
      "command": "npx",
      "args": ["screenverity-mcp"]
    }
  }
}
```

No credentials or account setup - the server runs locally against its packaged list snapshots.

## Business Relevance

- **Procurement teams** get auditable screening evidence for every vendor before contract signature.
- **Compliance officers** run ad-hoc checks during due diligence without portal logins.
- **Operations teams** keep signed receipts as evidence trails for audits and renewals.
- **SMB owners** screen subcontractors and partners for free, inside their existing agent workflows.

## Integration with CorpusIQ

ScreenVerity adds a free compliance gate to CorpusIQ's vendor-facing workflows. A CorpusIQ agent reading QuickBooks vendor lists or Stripe payout recipients can run ScreenVerity's screen tool over each new counterparty and store the signed receipt alongside the vendor record - turning every payment workflow into a documented screening pass. It pairs with the catalog's GovGazette and 1Lookup guides for a broader U.S. vendor-intelligence stack.

## Limitations

- Brand new - zero stars, no track record yet.
- U.S. lists only; the vendor states plainly it does not claim nationwide coverage - the sources tool is the authority on what is loaded.
- Local stdio server - results depend on the packaged list snapshots being current.
- Three tools - screening, source reporting and receipt verification only, no monitoring or alerts.
- npm delivery requires a Node runtime in the agent's environment.

## See Also

- [1Lookup MCP - Phone, Email and IP Verification](/docs/hermes/mcp/servers/external/1lookup-mcp)
- [GovGazette MCP - Federal Contract and Award Intelligence](/docs/hermes/mcp/servers/external/govgazette-mcp)
- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
