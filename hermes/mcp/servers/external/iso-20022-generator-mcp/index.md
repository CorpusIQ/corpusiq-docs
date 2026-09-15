---
title: "ISO 20022 Generator MCP - SEPA XML and SWIFT MT103 from Chat"
description: "Hosted MCP server that generates XSD-validated SEPA pain.001/pain.008 XML and SWIFT MT103 messages from natural-language payment instructions, with validation against official schemas and banking rules."
category: Finance
stars: n/a (hosted, no public repo)
added: 2026-08-29
source: "chatmcp/mcpso issue #3821"
relevance: ★★
tags: [mcp-server, sepa, iso-20022, swift, payments, banking, treasury, remote-mcp]
---

# ISO 20022 Generator MCP

**A hosted MCP server that turns natural-language payment instructions into XSD-validated, bank-ready SEPA ISO 20022 XML (pain.001 credit transfers, pain.008 direct debits) and SWIFT MT103 wire messages.** Every generated file is validated against the official XSD plus blocking business rules (IBAN structure, EndToEndId format, charset). MCP access is included in the multi and business plans, and XML validation is open to all plans without consuming quota.

```
Server type: Remote (Streamable HTTP), hosted
Auth: API key - Authorization: Bearer header (create at iso20022generator.com/en/account)
Endpoint: https://mcp.iso20022generator.com/mcp
Tools: 4 (generate_sepa_xml, validate_sepa_xml, generate_mt103, list_supported_versions)
Pricing: Multi and business plans include MCP; validation open to all plans
Category: Finance & Commerce / Treasury
Built by: iso20022generator.com; registry com.iso20022generator/mcp v1.0.0
```

## Why This Matters for Operators

Hand-building a pain.001 file means holding the ISO 20022 message structure, the SEPA business rules, and the bank's acceptance criteria in your head - and one wrong character set or EndToEndId format gets the file rejected at the bank, usually after the payment run window has closed. This server removes the format fight: describe the payment in plain language and get back a file that already passed XSD validation and the blocking business rules.

The validation tool matters on its own: operators can feed existing XML from any source through validate_sepa_xml and get a definitive schema-and-rules verdict before the file reaches the bank. And because validation never consumes quota, an agent can iterate on generation without burning the paid plan.

**Payment files come back bank-ready with the schema and business-rule validation already passed, instead of failing at the bank.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `generate_sepa_xml` | Generate SEPA pain.001 (001.03 / 001.09) or pain.008 (001.02) XML, validated against the official XSD plus banking rules (IBAN, EndToEndId, charset) |
| `validate_sepa_xml` | Validate an existing XML against the official schema and blocking business rules; open to all plans, never consumes quota |
| `generate_mt103` | Generate a SWIFT MT103 international wire message (text format) |
| `list_supported_versions` | List supported formats and versions |

## Installation

```bash
claude mcp add --transport http iso20022 https://mcp.iso20022generator.com/mcp --header "Authorization: Bearer $ISO20022_API_KEY"
```

Full setup walkthroughs for Claude Code, Claude Desktop, and other clients are published at iso20022generator.com/en/mcp.

## Configuration

```json
{
  "mcpServers": {
    "iso20022": {
      "type": "http",
      "url": "https://mcp.iso20022generator.com/mcp",
      "headers": { "Authorization": "Bearer <your-api-key>" }
    }
  }
}
```

Create the API key in the account area at iso20022generator.com/en/account. The endpoint is API-key gated - an anonymous initialize returns 401, confirming the endpoint is live.

## Business Relevance

- **Finance and treasury teams** generate SEPA batches and MT103 wires from instructions instead of hand-editing XML templates.
- **Accountants and bookkeepers** pre-validate payment files against schema and business rules before submission, cutting bank rejections.
- **Ops teams running payment automation** get deterministic, versioned output (pain.001.03/001.09, pain.008.02) for audit-friendly file generation.
- **Developers integrating bank rails** use list_supported_versions to pin exactly what their bank accepts.

## Integration with CorpusIQ

ISO 20022 Generator sits at the execution end of a CorpusIQ payment workflow: an operator reconciles payables in QuickBooks through CorpusIQ connectors, has an agent draft the payment run, and hands the resulting instructions to this server for validated SEPA XML or MT103 generation. The generated files then flow to the bank, while CorpusIQ keeps the payment record and the reconciliation state. For European operators this closes the loop from ledger to bank-ready file inside one agent workflow, with the validation step as a free pre-flight check on every run.

## Limitations

- Paid plans required for generation via MCP (multi and business); free tier is validation-oriented.
- No public repo - hosted service only.
- SEPA and MT103 scope - not a general payments API (no instant-payment schemes beyond the listed versions).
- Brand new MCP surface - first sweep August 29, 2026.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Nacha MCP - ACH File Parsing and Validation](/docs/hermes/mcp/servers/external/nacha-mcp)
- [BeeL MCP - Spanish VeriFactu E-Invoicing Compliance](/docs/hermes/mcp/servers/external/beel-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
