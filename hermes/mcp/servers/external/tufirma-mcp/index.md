---
title: "TuFirma MCP - Spanish Electronic Signatures for AI Assistants"
description: "Official remote MCP server from TuFirma: 24 tools over the public API let AI assistants consult documents and templates, create signature flows, upload PDFs and sign, send or cancel documents with scoped API-key auth."
category: Business Operations
stars: "n/a (no public repo)"
added: 2026-08-29
source: mcpservers.org /all
relevance: ★★
tags: [mcp-server, e-signature, documents, compliance, spain, business-ops, remote-mcp]
---

# TuFirma MCP

**Official remote MCP server from TuFirma, a Spanish electronic-signature platform.** 24 tools over the public API let an AI assistant consult the account, documents, templates and signature flows, create documents from templates or uploaded PDFs, and run the signing lifecycle: sign, request OTP, send reminders, cancel documents and reject transactions. The endpoint is a Streamable HTTP server with an API key delivered during an authorization flow, never in a config file, and scopes limit what each connection can read or write.

```
Server type: Remote (Streamable HTTP)
Auth: API key (tf_sk_*) delivered during the authorization flow, with scoped permissions
Endpoint: https://mcp.tufirma.digital/mcp
Tools: 24 (account and document queries, template-based creation, signature flows)
Pricing: TuFirma account plans; the MCP uses the public API
Category: Business Operations / Document workflow
Built by: TuFirma (tufirma.digital)
```

## Why This Matters for Operators

Signature chasing is a manual loop: generate the document, email it, follow up, resend, chase the OTP. TuFirma's MCP hands that loop to the assistant in Spanish-speaking operations: ask it to prepare an NDA from a template for a new supplier, launch the signature flow, and remind the lagging signer, all from the chat thread where the deal is being discussed.

Writes are deliberately separated from queries. The connector registers 24 tools over the public API, with signing actions (sign, request OTP, reminders, cancel, reject) exposed as explicit actions, and scopes can restrict a connection to read-only document access or to specific object types (documents, templates, transactions).

**Spanish SMEs get a full signing lifecycle in the assistant, from template to signed PDF, without a dashboard login.**

## Tools & Capabilities

TuFirma does not publish individual tool names in the MCP docs; the 24 tools map to the public API capability areas below (the live tool list is served from the endpoint after authorization):

| Area | Capability |
|---|---|
| Consult | Account status, documents, templates, recent contacts and available signature flows |
| Create | Upload a PDF, create documents from scratch or from a template, prepare batch transactions |
| Manage signatures | Sign, request OTP, send reminders, cancel documents and reject transactions with explicit actions |

## Installation

```bash
claude mcp add --transport http tufirma https://mcp.tufirma.digital/mcp
```

Run `/mcp` to open the authorization flow in the browser, enter your tf_sk_* API key and confirm the permissions. For Codex: `codex mcp add tufirma --url https://mcp.tufirma.digital/mcp` then `codex mcp login tufirma`.

## Configuration

```json
{
  "mcpServers": {
    "tufirma": {
      "type": "http",
      "url": "https://mcp.tufirma.digital/mcp"
    }
  }
}
```

Request the tf_sk_* credential for the account and organization that will operate the assistant. The key is delivered during the authorization flow rather than placed in the config file, and the connection grants only the selected permissions. The vendor docs are published in Spanish.

## Business Relevance

- **Spanish SMEs (PYMEs)** run quotes, NDAs and employment contracts from template to signature in chat.
- **Gestorías and accountants** prepare batch transactions and chase signatures with reminders instead of email threads.
- **Legal and HR teams** create signature flows with OTP confirmation and explicit cancel or reject actions.
- **International operators** with Spanish subsidiaries handle Spanish-law signing without a separate tool.

## Integration with CorpusIQ

TuFirma handles the signing lifecycle; CorpusIQ handles the money and CRM context around it. A composed workflow: the assistant reads open QuickBooks invoices through CorpusIQ connectors, prepares the corresponding contract from a TuFirma template, launches the signature flow and reminds the signer, then closes the loop by reading the signed document back and updating the HubSpot deal stage through CorpusIQ. CorpusIQ's read-only business data and TuFirma's read-write signing actions turn contract execution into one thread.

## Limitations

- Spanish-language service and docs; the product targets the Spanish market and Spanish-law workflows.
- No public repo and no self-host option; remote endpoint only.
- Individual tool names are not published; the 24-tool count and capability areas come from the vendor.
- API key auth requires requesting the credential from TuFirma and completing the authorization flow.
- Writes trigger real signature flows with legal effect; scopes gate them, but a misdirected prompt can still act.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [PolicyForge MCP - Legal Policies Generated and Audited from Your Codebase](/docs/hermes/mcp/servers/external/policyforge-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
