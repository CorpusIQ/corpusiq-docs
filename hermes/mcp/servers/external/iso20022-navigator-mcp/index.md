---
title: "ISO 20022 Navigator MCP - Payment Code Lookups"
description: "Free keyless answers on ISO 20022 bank transaction codes, message details and legacy mappings like MT103 to pacs.008."
category: Finance
stars: n/a (new listing)
added: 2026-10-12
source: "mcpservers.org /all (Oct 12, 2026 midday sweep)"
relevance: ★★
tags: [iso-20022, payments, banking, swift, sepa, reference-data, keyless, remote-mcp]
last_updated: "2026-10-24"
---

# ISO 20022 Navigator MCP

**Remote MCP server (Streamable HTTP, open access)** - grounded answers about ISO 20022 financial messaging: what a bank transaction code means, the details recorded for a message, which legacy message it replaces (MT103 to pacs.008) and which payment schemes use it. Free and public; the endpoint URL is all a client needs.

```
Server type: Remote (Streamable HTTP)
Auth: None (open access)
Endpoint: https://mcp.isonavigator.io/iso20022 (health check at /iso20022/health)
Tools: 3 (transaction codes, message details, legacy and scheme mappings)
Pricing: Free
Built by: ISO 20022 Navigator (repo github.com/kreativeManish/iso20022-navigator-mcp, MIT)
Data baseline: a provenance block on every response names the baseline quarter (for example 4Q2025)
Listing: mcpservers.org /all (Oct 12, 2026 midday sweep)
```

## Why This Matters for Operators

ISO 20022 is the standard behind the migration every bank and treasury team is in the middle of, and the questions it generates are reference questions: what does PMNT-RCDT-ESCT mean, what replaced MT940, which schemes run on pacs.008. During a migration those questions are constant, and the answers live in code lists and mapping tables that are not where the conversation is.

The Navigator puts the reference data behind three tools, with a provenance block on every response so an answer can be traced to a data load. The standards covered include SWIFT MT, SEPA, CIPS, NACHA / ACH, AFT, Lynx, RTR, CHAPS, Elixir, iDEAL, SIC, Bankgirot, NPP, MEPS+, RENTAS and BAHTNET.

## Tools & Capabilities

| Tool | What it answers |
|---|---|
| iso20022_bank_transaction_codes | What a bank transaction code (domain, family, subfamily) means, and which codes exist under a domain or family; partial codes like PMNT-RCDT or /RCDT/ESCT resolve at the right level |
| iso20022_message_details | The details recorded for an ISO 20022 message on the live tool surface |
| iso20022_legacy_and_scheme_mappings | Which ISO 20022 message replaces a legacy message (SWIFT MT, NACHA, CHAPS), for example MT103 to pacs.008, and which payment schemes use a message |

## Installation

```
claude mcp add --transport http iso20022 https://mcp.isonavigator.io/iso20022
```

The vendor publishes per-client setup for Claude (web and desktop), Claude Code, VS Code with Copilot, Cursor, ChatGPT (developer mode), Codex CLI and Gemini CLI; any client that supports remote Streamable HTTP works with the same URL.

## Configuration

```json
{
  "mcpServers": {
    "iso20022": {
      "type": "http",
      "url": "https://mcp.isonavigator.io/iso20022"
    }
  }
}
```

## Business Relevance

- **Treasury and payments teams** resolve code and mapping questions during ISO 20022 migration without leaving the conversation
- **Bank operations and reconciliation** teams look up what a statement code means and trace which scheme it belongs to
- **Fintech and ERP engineers** check the message a legacy flow maps to before building against it
- **Compliance and audit** read answers that carry a provenance block naming the data baseline

## Integration with CorpusIQ

The Navigator covers the standard's reference layer, complementing the catalogued message tools (camt053 parsing, pacs.008 generation and the ISO 20022 Generator). CorpusIQ answers the operator question from connected sources such as accounting and banking exports, so a payments question can pull the code reference alongside the transaction data.

Used together: ask CorpusIQ for the transaction view from connected systems and ask the Navigator for the standard's view of the code or message. The Navigator stays the reference of record; CorpusIQ remains the place the rest of the question is answered alongside.

## Limitations

- Reference data, not processing: it answers questions about codes and messages rather than parsing or generating them
- The scheme list is a selection (SWIFT MT, SEPA, CIPS, NACHA / ACH, AFT, Lynx, RTR, CHAPS, Elixir, iDEAL, SIC, Bankgirot, NPP, MEPS+, RENTAS, BAHTNET); schemes such as T2, FedNow and Fedwire are not recorded
- Latest message version only; combination descriptions are AI-generated and validated against the official ISO definitions, so verify against the official source for production use
- Shared rate limit of 600 calls a minute across all users

## FAQ

### Is it free?

Yes. The endpoint is open access with no key; a shared rate limit applies (600 calls a minute across all users).

### What is the provenance block?

Every response carries one, naming the data baseline quarter (for example 4Q2025) the answer was loaded from, so a mapping can be traced to a load rather than taken on trust.

### What does it not cover?

Bank-proprietary (non-external) codes, schemes outside the recorded list, and message versions other than the latest. A code that is not found comes back with where each part exists and the closest codes.

### How does it relate to message-processing servers?

It is the reference layer: the catalogued camt053, pacs008 and ISO 20022 Generator servers parse and generate messages, while the Navigator answers what codes and messages mean and how they map.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - all catalogued business-relevant servers
