---
title: "Korea Business Verify MCP - Live KYB Checks for Korean Companies"
description: "Hosted no-auth MCP server that verifies Korean companies in real time against the National Tax Service. Send a 10-digit business registration number and get registration status, tax type, and representative-name matching. Two tools: check_korean_business_status and verify_korean_business. Free during pilot."
category: Compliance
stars: 0
added: 2026-08-25
source: "mcp.so GitHub issue #3741"
relevance: ★★★
tags: [mcp-server, korea, kyb, business-verification, compliance, nts, due-diligence]
---

# Korea Business Verify (KBV) MCP

**Real-time Korean business verification with zero setup.** KBV is a hosted MCP server that checks any Korean company against the Korea National Tax Service (NTS) live per request. Give it a 10-digit business registration number (사업자등록번호) and it returns the registration status (active / suspended / closed), tax type, and optionally whether the number matches a representative name and opening date. No account, no API key, no installation: connect any MCP client to one URL.

```
Server type: Remote Streamable HTTP (Google Cloud Run, Seoul)
Auth: None required
Endpoint: https://kbv-server-f7vfitmlkq-du.a.run.app/mcp
Health: GET /health returns {"ok":true}
Repo: github.com/Wonderfulian/kbv-server (MIT, Aug 2026)
Tools: 2 verified by live probe (check_korean_business_status, verify_korean_business)
Price: Free during pilot; pay-per-call planned
Data: Korea National Tax Service open data, no usage restrictions
```

## Why This Matters for Operators

KYB checks on Korean counterparties normally mean navigating the Korean-language NTS portal or paying a compliance vendor per lookup. KBV turns it into a single tool call: procurement teams validating a new supplier, marketplaces onboarding Korean sellers, finance teams confirming a payment recipient, and e-commerce operators screening dropship vendors can all run an instant status check with English-normalized JSON output. Because the data is queried live from the NTS open-data API on every request, results reflect the current register, not a stale snapshot.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `check_korean_business_status` | Checks the registration status of a Korean business by its 10-digit business registration number; hyphens and spaces are normalized; returns active / suspended / closed status plus tax type |
| `verify_korean_business` | Full verification: matches the number against a representative name and opening date to confirm the registration belongs to the business you think it does |

Both tools return clean JSON with the queried number echoed back, so results can be logged directly into a due-diligence or onboarding workflow.

## Installation

No installation. Connect any MCP client to the Streamable HTTP endpoint:

```bash
claude mcp add --transport http kbv https://kbv-server-f7vfitmlkq-du.a.run.app/mcp
```

For Cursor, add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "korea-business-verify": {
      "url": "https://kbv-server-f7vfitmlkq-du.a.run.app/mcp"
    }
  }
}
```

## Configuration

No credentials, no environment variables. The endpoint is region-hosted in Seoul (asia-northeast3) for low latency from Asia. Query contents are never logged by the vendor. Use `/health` for a visual liveness check; note that opening `/mcp` in a browser returns "Method not allowed" by design (MCP uses POST, browsers use GET).

## Business Relevance

- **Supplier and vendor onboarding:** verify a Korean manufacturer or distributor before issuing a PO.
- **Marketplace seller screening:** confirm seller registration status for Korean marketplace integrations.
- **Payment compliance:** validate the tax type of a payment counterparty.
- **Cross-border due diligence:** English-normalized output removes the Korean-language barrier from NTS lookups.

## Integration with CorpusIQ

Pair KBV with CorpusIQ's QuickBooks or Stripe connectors during AP workflows: verify the Korean vendor's registration status, then pull the invoice or charge record from QuickBooks or Stripe to complete the review loop. Results are clean JSON, so they drop directly into a KYB checklist or a Google Sheet via CorpusIQ's Google Workspace connector.

## Limitations

- Free during the pilot phase; pay-per-call pricing is planned but not yet published.
- Covers Korean business registration only; no credit, court, or beneficial-ownership data.
- No batch API documented; one number per call.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Acquisition.gov MCP - FAR Overhaul and Agency Deviations](/docs/hermes/mcp/servers/external/acquisition-gov-mcp)
- [SAM.gov MCP - Federal Procurement Data](/docs/hermes/mcp/servers/external/sam-gov-mcp)
- [GovTrade MCP](/docs/hermes/mcp/servers/external/govtrade-mcp)
