---
title: "license-verify MCP Server — Contractor License & Insurance Verification"
description: "Integration guide for lmaniraruta/license-verify-mcp: verify US contractor licenses, surety bonds, and insurance from official state data. WA L&I live, CA CSLB beta. Agent-payable pay-per-success."
category: legal
tags: [mcp, contractor-verification, license, insurance, compliance, operations]
source: awesome-mcp-servers
repo: lmaniraruta/license-verify-mcp
stars: 0
discovered: 2026-07-23
last_updated: 2026-07-23
---

# license-verify MCP Server — Contractor Verification

**Repo:** [lmaniraruta/license-verify-mcp](https://github.com/lmaniraruta/license-verify-mcp)
**Pricing:** Agent-payable, pay-per-success
**Category:** Legal / Operations / Compliance

## Overview

license-verify-mcp enables AI agents to verify a US contractor's license, surety bond, and insurance directly from official state data sources. Currently live for Washington State (L&I) with California (CSLB) in beta. Uses a pay-per-success model — you only pay when a verification succeeds.

## Why Business Operators Need This

For any business operator hiring contractors, managing vendors, or ensuring compliance:

1. **Instant Contractor Vetting** — Before signing a contract with a new contractor, your agent verifies their license, bond, and insurance against official state records in seconds.
2. **Compliance Automation** — Integrate license verification into onboarding workflows. No more manual state website lookups or waiting for contractors to provide documentation.
3. **Fraud Prevention** — Catch expired licenses, lapsed bonds, or fake insurance certificates before they become liabilities.
4. **Audit Trail** — Every verification returns a verifiability block with extraction confidence and source URL for your records.

## Installation

```json
{
  "mcpServers": {
    "license-verify": {
      "command": "npx",
      "args": ["-y", "license-verify-mcp"]
    }
  }
}
```

## Coverage

| State | Status | Data Source |
|-------|--------|------------|
| Washington | ✅ Live | WA L&I (Labor & Industries) |
| California | 🅱️ Beta | CA CSLB (Contractors State License Board) |
| Additional states | 🔜 Planned | — |

## Key Tools

| Tool | Function |
|------|----------|
| `verify_license` | Check contractor license validity, status, and expiration |
| `verify_bond` | Verify surety bond is active and meets state requirements |
| `verify_insurance` | Confirm insurance coverage is current |
| `full_verification` | Run all three checks in one call |
| `search_contractor` | Find a contractor by name or license number |

## Common Queries

### Contractor Verification

```
"Verify the license for contractor ABC Construction in Washington State. License #ABC123."
"Run a full verification (license, bond, insurance) on our new roofing contractor in California."
"Check if this contractor's bond is still active — they claim it renewed last month."
```

### Compliance Monitoring

```
"Check all our active Washington State contractors — flag any with expiring licenses in the next 30 days."
"Verify the insurance certificates for our 3 electrical subcontractors."
"Search for contractor license #XYZ789 — confirm it's in good standing."
```

### Audit & Documentation

```
"Pull the full verification report for contractor DEF Builders from last month's audit."
"Generate a compliance summary for all California CSLB contractors on our active projects."
```

## Best Practices

1. **Verify before contracting** — Run `full_verification` on every new contractor before signing
2. **Set renewal alerts** — Check licenses monthly; flag those expiring within 30-60 days
3. **Save verification reports** — The verifiability block includes source URLs and confidence scores — save for audit trails
4. **Verify bonds separately** — Bond requirements vary by state and project type. Verify bonds meet YOUR specific thresholds
5. **CA CSLB is beta** — Double-check California results manually until CSLB integration exits beta

## Limitations

- Currently only WA (live) and CA (beta) — limited state coverage
- Pay-per-success model means failed verifications still consume agent resources (though not cost)
- State data sources can have delays (WA L&I updates daily, CA CSLB updates vary)
- Insurance verification may require contractor cooperation for some carriers

## For Operators: Integration with CorpusIQ

- **CorpusIQ QuickBooks connector** + license-verify = Cross-reference contractor payments against verified license status
- **CorpusIQ cross-source analysis** + license-verify = Flag contractors with expiring licenses who have open invoices
- **CorpusIQ Slack connector** + license-verify = Auto-alert project managers when a contractor's license or bond lapses

## See Also

- [Correctover MCP Guide](/hermes/mcp/servers/external/correctover-mcp/) — Contract validation
- [QuickBooks MCP Guide](/hermes/mcp/#quickbooks)
- [Slack MCP Guide](/hermes/mcp/#slack)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)

---

*Discovered: July 23, 2026 · Source: awesome-mcp-servers PR #10348 · Category: Legal/Operations/Compliance*
