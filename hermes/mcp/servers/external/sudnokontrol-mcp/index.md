---
title: "SudnoKontrol MCP: Ukrainian Vessel Registry Search"
description: "Keyless read-only MCP server over the Ukrainian national vessel registries: search vessels by registration number, name, or owner, pull full registry records, and query aggregate statistics. Every result links to an official registry excerpt with QR verification."
category: Compliance & Regulatory
stars: n/a (new listing)
added: 2026-08-24
source: "chatmcp/mcpso issue #3733"
relevance: ★★
tags: [maritime, vessels, ship-registry, trade-compliance, ukraine, due-diligence, remote-mcp]
---

# SudnoKontrol MCP

**Keyless read-only MCP server over the Ukrainian national vessel registries.** Built on the SudnoKontrol registry platform, it searches the Державний судновий реєстр України (State Ship Registry of Ukraine) and Суднова книга України (Ship Book of Ukraine) by registration number, name, or owner, returns full registry records, and answers "how many vessels" questions with aggregate statistics. No API key, no signup, pure public data.

```
Server type: Remote (Streamable HTTP)
Auth: None (read-only public data)
Endpoint: https://api.sk.ukrfish.org/mcp
Tools: 4 (search_vessel_registries, lookup_vessel, get_registry_stats, get_dataset_metadata)
Pricing: Free
Category: Compliance / Maritime Trade
Built by: ailubes (repo: ailubes/sudnokontrol-mcp, MIT)
```

## Why This Matters for Operators

Black Sea shipping moves a large share of global grain and agricultural freight, and Ukrainian-flagged or Ukrainian-registered vessels show up in trade counterparty checks, sanctions screening, and maritime due diligence. Before this server, checking a vessel meant manual form queries on the registry site in Ukrainian, one vessel at a time. **SudnoKontrol MCP turns the registry into agent-callable data**: search by number, name, or owner, pull the full record, and get the source URL for an official excerpt with a QR-verified PDF.

The registration-number normalization is the hidden engineering win: `УПС-0129`, `УПС 0129`, and `UPS-0129` are treated as the same vessel across Cyrillic and Latin forms, so lookups do not silently miss on keyboard layout.

## Tools & Capabilities

All four tools verified by live probe (server v1.0.0):

| Tool | Purpose |
|---|---|
| `search_vessel_registries` | Free-text plus structured search across both Ukrainian registries, separator-insensitive Cyrillic/Latin registration numbers |
| `lookup_vessel` | Exact vessel lookup by normalized registration number |
| `get_registry_stats` | Aggregate public vessel counts for "how many vessels" questions |
| `get_dataset_metadata` | Dataset sources, import dates, record counts, and fields |

Every result includes a `web_url` to order an official registry excerpt (PDF with QR verification) at sk.ukrfish.org/registry.

## Installation

```bash
claude mcp add --transport http sudnokontrol https://api.sk.ukrfish.org/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "sudnokontrol": {
      "type": "http",
      "url": "https://api.sk.ukrfish.org/mcp"
    }
  }
}
```

No credentials and no configuration. The server is read-only over public registry data, so there is nothing to provision before the first call.

## Business Relevance

- **Trade compliance teams** verify vessel ownership and registry status on Black Sea counterparties
- **Maritime due diligence** pulls full registry records plus an orderable official excerpt with QR verification
- **Grain and agri-commodity operators** check vessels tied to Ukrainian export logistics
- **Insurance and chartering teams** run quick registry lookups without manual form queries

## Integration with CorpusIQ

CorpusIQ covers the commercial ledger (contracts, invoices, payments via the QuickBooks and Stripe connectors). SudnoKontrol adds the vessel layer: an agent can verify the vessel named in a trade contract against the Ukrainian registry, then attach that record to the counterparty file in CorpusIQ's CRM and document stores. Same split already running with Normi DVF (French property market data) and OffenderSearch (registry screening): public registry data from the specialist server, commercial truth from CorpusIQ.

## Limitations

- Ukrainian registries only; other flag states need their own sources.
- Brand new listing (Aug 24, 2026); repo has no star history yet.
- Registry data is only as fresh as the underlying dataset (import dates are exposed via `get_dataset_metadata`).
- The official excerpt PDF is ordered through the vendor site, outside the MCP flow.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
