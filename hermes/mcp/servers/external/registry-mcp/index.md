---
title: registry-mcp - Company Registry Data for AI Agents
description: Company data from national business registries served over MCP and REST. Five tools look up companies by national identifier, search by name, check VAT registration, validate identifier checksums offline, and compute statutory filing deadlines. First module covers Norway (Bronnoysundregistrene / Enhetsregisteret by orgnr), with more countries planned.
category: Business Operations
stars: n/a (new listing)
added: 2026-09-04
source: "mcp.so GitHub issue #3927"
relevance: ★★★
tags: [company-registry, business-verification, vat, norway, brreg, company-lookup, remote-mcp, keyless]
---

# registry-mcp

**Remote MCP server (Streamable HTTP) with a stdio twin** - company data for AI agents from national business registries. Norway first (Bronnoysundregistrene / Enhetsregisteret by organisasjonsnummer), with the interface built to span more countries. Five tools confirmed by live probe (serverInfo registry-mcp v0.2.0) in this sweep; the catalog surface is keyless.

```
Server type: Remote (Streamable HTTP) or local (uvx registry-mcp / npx registry-mcp)
Auth: None on the catalog surface
Endpoint: https://api.foretak.dev/mcp
Tools: 5 (lookup_company, search_company, company_deadlines, validate_company_id, list_countries)
License: MIT (code) / NLOD 2.0 (data)
Registry: io.github.foretak/registry-mcp (also published as brreg-mcp)
```

## Why This Matters for Operators

Vendor verification, counterparty diligence and compliance checks all start with the same question: is this company real, active and registered where it says it is? registry-mcp answers that from the primary source - the national register itself - with the identifier checksum validated before any network call. **An agent checking a new Norwegian supplier can confirm legal form, status, address and VAT registration in one lookup, and then ask for the company's next statutory filing deadlines.**

The `company_deadlines` tool is the differentiator: it computes the next occurrence of each statutory deadline (annual accounts, VAT, etc.) a company faces, which turns registry data from a lookup into a compliance calendar an operator can act on.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `lookup_company` | Full CompanyReport by national identifier: legal form, status, address, VAT registration |
| `search_company` | Search the register by name (country=NO searches Bronnoysundregistrene) |
| `company_deadlines` | Next occurrence of each statutory filing deadline the company faces |
| `validate_company_id` | Well-formedness and checksum check of an identifier, no network call |
| `list_countries` | Every national registry currently served, with id_scheme and id_example per country |

## Installation

```bash
claude mcp add --transport http registry-mcp https://api.foretak.dev/mcp
```

For local use: `uvx registry-mcp` or `npx registry-mcp` (stdio). The hosted endpoint answers anonymous initialize and tools/list, verified live this sweep.

## Configuration

```json
{
  "mcpServers": {
    "registry-mcp": {
      "url": "https://api.foretak.dev/mcp"
    }
  }
}
```

No key required on the catalog surface. The same data is available as a REST API at api.foretak.dev for non-MCP integrations.

## Business Relevance

- **Finance and procurement teams** verify Norwegian suppliers and customers against the primary register.
- **Compliance workflows** get statutory deadline computation instead of a manual calendar.
- **Vendor due diligence** confirms VAT registration status as part of onboarding checks.
- **Data-quality pipelines** validate organisasjonsnummer checksums offline before submitting lookups.

## Integration with CorpusIQ

CorpusIQ connectors read company records from accounting and CRM systems; registry-mcp is the verification layer against the national source of truth. A CorpusIQ agent onboarding a new Norwegian entity can look up the register entry, confirm VAT status, and schedule the entity's filing deadlines into the operator's calendar - closing the loop between the system of record and the government register.

## Limitations

- Single-country coverage today (Norway); the multi-country interface is in place but only one module ships.
- Project is days old (repo created Sep 4, 2026, 0 stars) - API stability is unproven.
- Register data quality follows the source register; deadlines computed for Norway are country-specific and need review as modules expand.
- No write operations by design - lookup and validation only.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [Factanker MCP - Evidence-Backed Company and Bank Facts](/docs/hermes/mcp/servers/external/factanker-mcp)
- [NeuralVerge MCP - B2B People and Company Data](/docs/hermes/mcp/servers/external/neuralverge-mcp)
