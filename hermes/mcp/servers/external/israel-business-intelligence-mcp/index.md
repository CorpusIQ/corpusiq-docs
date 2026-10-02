---
title: Israel Business Intelligence MCP - Company Verification
description: "Hosted MCP server that verifies Israeli companies against structured public-registry evidence for supplier verification, due diligence, and counterparty research. Keyless discovery with x402 pay-per-verification."
category: Business Intelligence
stars: n/a (new listing, itzikhr18/israel-business-intelligence)
added: 2026-08-29
source: "chatmcp/mcpso issue #3826"
relevance: ★★
tags: [mcp-server, company-data, supplier-verification, due-diligence, israeli-registry, business-intelligence, x402, remote-mcp]
---

# Israel Business Intelligence MCP

**Agent-native Israeli company verification using structured public-registry evidence for supplier verification, due diligence, Israeli company registry research, and business intelligence.** The endpoint is keyless for discovery (the service description and schemas are free), and the verification call itself is paid per use through x402 v2 on Base Mainnet at 0.05 USDC per verify_company call. The service returns public-registry evidence and is explicit that it is not full regulatory KYB.

```
Server type: Remote (Streamable HTTP), hosted
Auth: None for discovery; x402 v2 (Base Mainnet) for verify_company at 0.05 USDC per call
Endpoint: https://israel-counterparty-intelligence.vercel.app/mcp
Tools: 3 (describe_service, get_schema, verify_company)
Pricing: Free discovery tools; 0.05 USDC per verification
Category: Business Intelligence / Company Data / Supplier Verification
Built by: itzikhr18; registry io.github.itzikhr18/israel-business-intelligence v1.0.1
```

## Why This Matters for Operators

Verifying an Israeli counterparty today means either paying a legacy KYB vendor for a country you rarely touch, or hand-checking the Israeli corporate registry and reconciling whatever you find against what the supplier told you. This server gives agents a structured registry-backed answer for a few cents per check, with the evidence surfaced alongside the verdict so a human reviewer can see what the answer is based on.

The x402 model fits the use case: you only pay when an agent actually verifies a company, and the free discovery tools let an agent check capabilities and pricing before committing a call. The vendor is explicit about scope - public-registry evidence, not full regulatory KYB - which is exactly the right boundary for supplier pre-screening and due-diligence triage.

**Operator agents get a structured Israeli company check with the registry evidence attached, for 0.05 USDC, without any subscription.**

## Tools & Capabilities

Live-probed August 29, 2026 (anonymous initialize returned all three tools).

| Tool | Purpose |
|---|---|
| `describe_service` | Free. Service capabilities, pricing, evidence scope, and limitations |
| `get_schema` | Free. Machine-readable input and output schemas for verify_company |
| `verify_company` | Verifies Israeli companies and resolves Israeli company numbers, returning structured public-registry evidence for supplier verification, due diligence, and business intelligence |

## Installation

```bash
claude mcp add --transport http israel-bi https://israel-counterparty-intelligence.vercel.app/mcp
```

The vendor publishes a plain-text README at the same origin (israel-counterparty-intelligence.vercel.app/README.md) and lists the server on Smithery and the official MCP registry.

## Configuration

```json
{
  "mcpServers": {
    "israel-bi": {
      "type": "http",
      "url": "https://israel-counterparty-intelligence.vercel.app/mcp"
    }
  }
}
```

Discovery calls need no authentication. The verify_company tool triggers an x402 payment challenge on Base Mainnet (0.05 USDC); a wallet-enabled MCP client settles it before the tool returns its evidence payload.

## Business Relevance

- **Procurement and supplier teams** get a registry-backed pre-screen of Israeli suppliers before contract work starts.
- **Due-diligence analysts** hand agents the first-pass check and keep the registry evidence for the file, reserving full KYB vendors for final sign-off.
- **Compliance operators** run cheap periodic re-verifications of Israeli counterparties instead of one expensive annual pass.
- **Agents in finance workflows** discover the service and its schemas for free, then pay only for actual verifications.

## Integration with CorpusIQ

The Israel Business Intelligence server slots into CorpusIQ's data-connector estate as a specialist counterparty check alongside the general accounting and CRM connectors. A CorpusIQ workflow reading a supplier from QuickBooks or a deal record from HubSpot can hand the supplier's Israeli company number to verify_company and write the registry evidence back into the CRM as a note, so the verification trail lives with the account. For operators with mixed international supplier bases, this pairs with the catalog's other regional verification servers (Korea Business Verify, Atlas Verified) to give one agent a per-country verification menu, with CorpusIQ holding the workflow together.

## Limitations

- Brand new listing - no track record yet; first sweep August 29, 2026.
- Not full regulatory KYB - the vendor states this explicitly; evidence is public-registry sourced.
- verify_company requires x402 payment (0.05 USDC, Base Mainnet) - the client must support x402 settlement.
- Single-country scope - Israel only.
- Hosted endpoint on Vercel - no self-host option published.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Korea Business Verify MCP - Live KYB Checks for Korean Companies](/hermes/mcp/servers/external/korea-business-verify)
- [QoreNext Trade Screening MCP - Sanctions and Restricted-Party Checks](/hermes/mcp/servers/external/qorenext-tradescreening-mcp)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
