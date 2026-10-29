---
title: "Cobra MCP - Ecuador SRI Invoices From Chat"
description: "Issues, credits and retentions authorised by Ecuador's SRI from a conversation, with a free sandbox whose keys never produce real tax documents."
category: Financial Data
stars: ★★★ (401 plus API-key contract verified)
added: 2026-10-29
source: "live probe of https://facturacobra.com/mcp answering HTTP 401 with JSON-RPC error -32001 explaining the accepted API-key header forms, and a 404 on the protected-resource path confirming API key rather than OAuth; product detail from https://facturacobra.com/mcp"
relevance: ★★★
tags: [invoicing, e-invoicing, tax, ecuador, sri, api-key, remote-mcp]
last_updated: "2026-10-29"
---

# Cobra MCP

**Invoicing in Ecuador runs through the SRI, and the SRI does not care that the invoice was urgent. A document that is not authorised is not a document, which is why the last mile of every billing system in the country is a portal and an XML schema.**

```
Server type: Remote (Streamable HTTP), with a self-hostable stdio bridge
Endpoint:    https://facturacobra.com/mcp
Auth:        API key, sent as Authorization Bearer, X-API-Key, or ?APIkey= in the URL
Discovery:   no OAuth protected-resource document (returns 404)
Sandbox:     free, sandbox keys never issue real tax documents
```

## Why This Matters for Operators

Most of the world treats an invoice as a record. Ecuador treats it as a filing, authorised by the tax authority in real time and carrying an authorisation number that the buyer will check. That makes the gap between "the work is done" and "the invoice exists" a system boundary rather than a delay.

Cobra closes that boundary conversationally: issue an invoice, a credit note or a retention and have the SRI authorise it, in natural language, from Claude, ChatGPT or Cursor. The demo shown on the vendor's page is exactly the shape an operator wants, a request naming a customer and an amount answered with an authorisation number and the total with tax.

The retention document is the detail that marks this as built by someone who has done Ecuadorian billing rather than adapted a generic invoicing template.

The sandbox is the second thing worth copying. Sandbox keys are documented as never issuing real tax documents, which means a firm can test the whole flow, including the agent, before a single real filing exists.

## What Was Verified

A bare `initialize` POST to `https://facturacobra.com/mcp` returned **HTTP 401** with the JSON-RPC error code `-32001` and a message stating that the API key is missing and listing the three accepted forms: an `Authorization: Bearer` header, an `X-API-Key` header, or an `?APIkey=mfact_...` query parameter. The `mfact_` prefix is the key format to expect in the panel.

The OAuth discovery path at `https://facturacobra.com/.well-known/oauth-protected-resource` returned **404** with the vendor's own Spanish not-found page, so this is an API-key surface, not an OAuth surface. That matters for clients that only support OAuth connectors.

Product behaviour and the sandbox guarantee come from the vendor's MCP page, which presents the server as the first SRI billing MCP for Ecuador and shows real-time authorisation.

## Limits Worth Recording

The surface is key gated, so no tool inventory was read this pass. What is documented is the authentication contract and the vendor's stated behaviour.

One API key covers the account, with no published scope separation between reading a document and issuing one. Sandbox versus production is the only separation the vendor names.

Country scope is Ecuador and the SRI. The document types are invoices, credit notes and retentions, and nothing outside that set is claimed.

The panel is in Spanish and the error messages are in Spanish, which is correct for the market and worth knowing before handing the integration to someone who does not read it.

## FAQ

### Does it work with any MCP client?

It is a remote Streamable HTTP server, so any client that supports that transport and a bearer or header key can connect. Clients that require OAuth will not complete discovery here.

### Can I test without issuing real invoices?

Yes. A free sandbox is offered, and sandbox keys are documented as never issuing real tax documents.

### What can it issue?

Invoices, credit notes and withholding retentions, authorised by the SRI in real time.

## See Also

- [Financial data servers in this catalogue](/hermes/mcp/servers/external/)
- [Connecting CorpusIQ to your own data sources](/hermes/mcp/)
