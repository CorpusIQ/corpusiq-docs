---
title: "Electronics RFQ Agent MCP: RFQ-to-Quote ERP Automation"
description: "Python CLI and MCP server that reads electronics RFQ documents in PDF, Excel or Word, looks up every line item against an ERP catalog, and outputs a draft quote with a fill-rate audit. Connects to SAP, Epicor, Oracle and Microsoft Dynamics through MCP; tools include quote_rfq, audit_quote, check_inventory, get_part and get_price. MIT licensed."
category: ERP
stars: n/a (new listing)
added: 2026-08-24
source: mcpservers.org /all page 2
relevance: ★★
tags: [procurement, rfq, quoting, erp, electronics, supply-chain, python]
---

# Electronics RFQ Agent MCP

**AI quoting for electronics distributors: RFQ in, draft quote out.** Electronics RFQ Agent is a Python library and CLI that reads RFQ documents (PDF, Excel, Word), parses them with Claude, looks up every line item against an ERP catalog, and outputs a draft quote with a fill-rate audit. It connects to SAP, Epicor, Oracle, and Microsoft Dynamics through MCP servers, so it works with Claude, GPT-4, or any agent framework that speaks MCP. Sales engineers spending 2-4 hours turning RFQ documents into quotes get the same result in seconds.

```
Server type: CLI plus MCP tools (Python 3.10+, stdio)
Auth: None for the tool itself; ERP access via your existing ERP connectors
Install: pip install electronics-rfq-agent-cli
Repo: github.com/rudrendupaul/electronics-rfq-agent (MIT, Jun 2026)
Tools: 9 verified (get_part, get_price, lookup_part, search_parts, check_inventory, quote_rfq, audit_quote, quote_file, not_found)
```

## Why This Matters for Operators

Quoting is the highest-cost step in electronics distribution: a five-line RFQ can consume an afternoon of part lookups, price checks, and availability calls across the ERP. Electronics RFQ Agent compresses that loop into a single command that produces both the draft quote and a fill-rate report showing exactly which lines were found, priced, or missing, so a sales engineer reviews exceptions instead of transcribing line items.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `get_part` | Fetches a part record from the connected ERP catalog |
| `get_price` | Returns the current price for a part or price book |
| `lookup_part` | Resolves a parsed RFQ line item to its catalog match |
| `search_parts` | Searches the ERP catalog by part number, description, or manufacturer |
| `check_inventory` | Returns availability for a part or list of parts |
| `quote_rfq` | Parses an RFQ document and generates a draft quote from catalog matches |
| `audit_quote` | Produces a fill-rate report showing matched, priced, and not-found lines |
| `quote_file` | Writes or exports the generated quote document |
| `not_found` | Reports line items with no catalog match for manual review |

## Installation

```bash
pip install electronics-rfq-agent-cli
```

Then run the CLI (`erfa --help` shows the subcommands) or expose the tools over MCP:

```bash
erfa mcp
```

## Configuration

Wire the agent to your ERP through its MCP server (SAP, Epicor, Oracle, or Microsoft Dynamics connectors), point the catalog configuration at your parts and pricing data, and the quote and audit commands run against live ERP data. A mock ERP backend ships for evaluation without touching production systems.

## Example Prompts

- "Parse this RFQ PDF and produce a draft quote from our SAP catalog."
- "Audit this quote against inventory and show me the fill-rate report."
- "Which line items in this RFQ have no catalog match, and what are they?"
- "Price this five-line RFQ and flag every line below our target margin."

## Business Relevance

- **Electronics distributors** cut RFQ turnaround from hours to seconds per document
- **Sales engineers** review exception lines instead of transcribing parts
- **Component suppliers** keep quotes consistent with live ERP pricing and stock
- **Procurement teams** pre-flight RFQs against catalog and inventory before committing

## Integration with CorpusIQ

Electronics RFQ Agent converts RFQ documents into structured quote lines; CorpusIQ turns those quotes into business truth. An agent can generate the draft quote from the RFQ, then log the opportunity, check the counterparty's order history and payment behavior, and track the quote-to-order conversion through CorpusIQ, joining the quoting workflow with the revenue pipeline in one conversation.

## Limitations

- New open-source project (zero stars at listing time, Jun 2026) with a single maintainer.
- ERP integration depends on the ERP vendor's own MCP connectors, which vary in quality.
- Domain-specific to electronics component quoting; other RFQ verticals would need adaptation.
- Parsing accuracy depends on document quality; audited exceptions still need human review.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [FluentEDI MCP](/hermes/mcp/servers/external/fluentedi-mcp) - hosted X12 EDI processing for supply-chain agents
- [Oracle MCP](/hermes/mcp/servers/external/oracle-mcp) - Oracle database access for agents
- [QuickBooks MCP](/hermes/mcp/servers/external/quickbooks-mcp) - accounting and financial operations
