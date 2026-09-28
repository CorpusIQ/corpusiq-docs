---
title: ZTDS Data Sanitizer MCP - PII De-Identification for Agents
description: "ZTDS is a zero-trust data sanitization MCP server: local PII de-identification and deterministic surrogate tokenization."
category: Security
stars: n/a (new listing)
added: 2026-09-27
source: "mcpservers.org + github.com/moxno/ztds.ai"
relevance: ★★
tags: [pii, data-sanitization, tokenization, privacy, zero-trust, compliance, self-hosted]
---

# ZTDS Data Sanitizer MCP

**A reference zero-trust sanitization layer between raw data and the model.** ZTDS is a zero-trust data sanitization MCP server for Cursor and Claude Desktop: local in-memory PII de-identification and deterministic surrogate tokenization under an RFC v1.0 spec, Apache-2.0 licensed. It ships from the ztds.ai repository under packages/ztds-mcp.

```
Server type: Local (stdio, self-hosted)
Auth: none (local process)
Endpoint: repo package (packages/ztds-mcp)
Tools: PII de-identification, deterministic surrogate tokenization
Pricing: free and open source (Apache-2.0)
Category: Security / Privacy
Built by: ZTDS (github.com/moxno/ztds.ai)
```

## Why This Matters for Operators

Sending raw customer or employee data into an agent is a leak vector, and most mitigations are ad hoc regex scripts nobody maintains. ZTDS provides a reference implementation of deterministic surrogate tokenization: PII is replaced in memory with stable surrogates, so the model gets structure and relationships without the identifiers, and the same input always maps to the same surrogate for downstream joining.

Deterministic tokenization matters operationally: you can de-identify a dataset, run agent workflows on it, and join results back to real identifiers on the operator side.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| PII de-identification | Strip identifiers in memory before data reaches the model |
| Surrogate tokenization | Deterministic replacements that preserve joins |
| Local execution | All processing in memory, nothing leaves the machine |

## Installation

```bash
git clone https://github.com/moxno/ztds.ai
```

Install the ztds-mcp package from the repo and add it as a stdio server in Cursor or Claude Desktop per the README.

## Configuration

```json
{
  "mcpServers": {
    "ztds": {
      "command": "<per-repo-launch-command>"
    }
  }
}
```

## Business Relevance

- **Compliance teams** get a reference sanitization layer for agent workflows
- **Data teams** de-identify before analysis while preserving joins
- **Founders handling customer data** reduce PII exposure to models
- **Security leads** get an auditable, spec-based tokenization path

## Integration with CorpusIQ

ZTDS pairs with CorpusIQ data connectors as a pre-processing gate: before CSV or JSON data from Stripe, QuickBooks or the CRM flows into an agent workflow, ZTDS can tokenize the PII fields. CorpusIQ's verification discipline can then check that downstream recaps carry no raw identifiers.

## Limitations

- Reference implementation; production hardening is on the operator
- Local stdio server; every agent host needs the package
- Single-purpose (PII sanitization), not a full DLP platform
- New listing with no adoption track record

## FAQ

### What is deterministic surrogate tokenization?

PII is replaced with stable surrogates, so the same input always maps to the same surrogate and results can be joined back on the operator side.

### Where does processing happen?

Entirely in local memory; nothing leaves the machine.

### What license does it use?

Apache-2.0 under an RFC v1.0 spec, shipped from the ztds.ai repository.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
