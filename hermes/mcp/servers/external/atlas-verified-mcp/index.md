---
title: "Atlas Verified MCP: Supply Chain Compliance and Trade"
description: "Official-registry MCP server for global trade verification - organic certification checks against the USDA Organic Integrity Database, OFAC sanctions screening, FDA import controls, document authentication with 30+ automated checks, and structured trade intelligence from 50+ attributed sources. OAuth 2.0 + PKCE, hosted at api.atlasverified.ai/mcp."
category: Compliance
stars: n/a (new listing)
added: 2026-08-23
source: "mcp.so GitHub issue #3711 + official MCP registry record"
relevance: ★★★
tags: [supply-chain, compliance, ofac, fda, organic-certification, oauth, remote-mcp, trade-verification]
---

# Atlas Verified MCP

**AI-powered supply chain verification for global trade - organic certification checks, OFAC sanctions screening, FDA import controls and trade-document authentication - exposed as an official-registry MCP server.** Atlas Verified (atlasverified.ai) publishes `ai.atlasverified/atlas-mcp` v1.0.0 on the official MCP registry (active since Jul 21, 2026), served from `https://api.atlasverified.ai/mcp` over Streamable HTTP with OAuth 2.0 + PKCE. The endpoint is auth-gated: an anonymous probe returned HTTP 401 "Authorization header required", confirming the server is live and the OAuth flow is enforced.

```
Server type: Remote (Streamable HTTP, hosted)
Auth: OAuth 2.0 + PKCE (auth-gated; anonymous probe returned HTTP 401)
Endpoint: https://api.atlasverified.ai/mcp
Registry: ai.atlasverified/atlas-mcp v1.0.0 (official MCP registry, active Jul 21, 2026)
Tools: Capability-level (auth-gated; see table caveat)
Repo: None published (hosted remote endpoint only)
```

## Why This Matters for Operators

Global trade compliance is a multi-source puzzle: an organic certifier checks USDA registries, an importer checks FDA FSVP status, a compliance officer screens denied parties against OFAC lists, and a broker verifies trade documents - each in a different system. Atlas Verified consolidates those checks into one MCP surface, so an agent can ask plain-English questions about any supplier, shipment, or document and get answers synthesized from 50+ attributed data sources. For operators, that turns a supplier onboarding checklist that took days of tab-switching into a single agent conversation with an audit trail.

## Tools & Capabilities

The MCP surface mirrors the platform's verification products. Because the endpoint requires OAuth, this table is capability-level from atlasverified.ai/products - exact tool names require a signed-in client, and anonymous enumeration is refused by design.

| Capability | What it does |
|---|---|
| Supplier Verification | Persistent supplier profiles aggregating certification validation, sanctions screening, trade history, and document verification into a single trust record |
| Certification Verification | Verifies organic certifications and NOP credentials against the USDA Organic Integrity Database and global certification registries |
| Document Authentication | Extracts structured data from trade documents, classifies them, and runs 30+ automated verification checks across multiple OCR engines |
| Atlas Verified Score | 0-1000 trust score quantifying verification completeness across certifications, sanctions, trade history, and documentation |
| Chain of Custody | Digital provenance for organic commodity lots, linking documents, shipments, suppliers, and verification results into one traceability chain |
| Structured Trade Intelligence | Tariffs, commodity prices, exchange rates, port activity, and import/export records from WTO, IMF, UN Comtrade, US Census and other authoritative sources |

Compliance frameworks covered include USDA Organic, FDA FSVP, OFAC, EU TRACES, JAS (Japan) and GLEIF LEI. All intelligence reports carry full source attribution.

## Installation

```json
{
  "mcpServers": {
    "atlas": {
      "type": "http",
      "url": "https://api.atlasverified.ai/mcp"
    }
  }
}
```

For the Claude Code CLI: `claude mcp add --transport http atlas https://api.atlasverified.ai/mcp`

## Configuration

On first call the server returns 401 with OAuth metadata; the client registers itself (OAuth 2.0 + PKCE), the user signs in at atlasverified.ai to authorize, and the client stores the token it is handed. No API key to manage. Revocation is handled on the Atlas Verified side, and every request re-resolves authorization against the account's scope.

## Example Prompts

- "Screen this supplier for OFAC exposure and verify their organic certification status."
- "Authenticate this bill of lading and summarize the 30+ verification checks it passed."
- "What is the current tariff picture for this commodity route, and how has port activity trended?"
- "Build a verification profile for this importer - certifications, sanctions, trade history, and documents."

## Business Relevance

- **Importers and brokers** run FDA FSVP and OFAC screening inside the agent that writes the shipment documentation
- **Organic brands and growers** verify NOP credentials and certification status against USDA and global registries
- **Certifiers** authenticate trade documents with multi-OCR checks and produce audit-ready records
- **Compliance teams** get persistent supplier trust records with a 0-1000 verification score

## Integration with CorpusIQ

CorpusIQ answers questions about the business's own data (revenue, customers, contracts). Atlas Verified adds the external compliance layer: an agent can screen a counterparty's certifications, sanctions exposure and trade documents (Atlas Verified) and cross-check the findings against that counterparty's commercial history in CorpusIQ - verification data from Atlas, business truth from CorpusIQ. The same split CorpusIQ already runs with Truth Bear and Corpus Law.

## Limitations

- Auth-gated: exact tool names are not publicly enumerable; the capability table above is derived from vendor product documentation and should be confirmed after OAuth sign-in.
- Hosted-only service with no public open-source repository (new listing, Aug 23, 2026).
- Focused on organic and global-trade verification - not a general-purpose business screening service.
- Pricing is not published; access terms are set at sign-in.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [Truth Bear GAUGE MCP](/docs/hermes/mcp/servers/external/truth-bear-gauge) - verifiable government data with cryptographic proof
- [FluentEDI MCP](/docs/hermes/mcp/servers/external/fluentedi-mcp) - hosted X12 EDI processing for supply-chain agents
- [MCP Integration Guide](/docs/hermes/mcp) - connecting MCP servers to Hermes Agent
