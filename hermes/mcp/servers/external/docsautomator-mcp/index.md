---
title: "DocsAutomator MCP - Documents That Render the Same"
description: "Templates in Google Docs or Word, data from Airtable or SmartSuite, and an e-signature lifecycle in one call, with scopes split read and write."
category: Productivity / Document Automation
stars: n/a (commercial, 1,200+ businesses, 4.9/5 on 15+ G2 reviews)
added: 2026-10-27
source: "live probe on https://mcp.docsautomator.co/mcp returning HTTP 401 with a message naming Bearer key, X-API-Key or OAuth plus an oauth_discovery URL, the RFC 9728 protected-resource document at mcp.docsautomator.co/.well-known/oauth-protected-resource naming two scopes and api.docsautomator.co as the authorization server, and the vendor pages at docsautomator.co/features/ai-and-agents read at 04:06Z on 2026-10-28"
relevance: ★★★
tags: [documents, pdf, templates, esignature, approvals, airtable, google-docs, oauth, hosted, back-office]
last_updated: "2026-10-27"
---

# DocsAutomator MCP

**An agent asked to produce an invoice will produce something that looks like an invoice. The question a business asks is whether it produces the same one, with the right tax id and the right line items, every time.**

```
Server type:  Remote (Streamable HTTP), hosted
Endpoint:     https://mcp.docsautomator.co/mcp
Auth:         OAuth, Bearer API key or X-API-Key header
Scopes:       docsautomator:read, docsautomator:write
Auth server:  https://api.docsautomator.co
Templates:    Google Docs or Word, owned by the customer
Data:         Airtable, SmartSuite, Google Sheets
Built by:     DocsAutomator (docsautomator.co)
```

## Why This Matters for Operators

Ask a model for a contract, an invoice or a certificate and you get a document that is probably right. Probably is not the standard for a document that carries a tax id, a payment term and a signature line. The failure is not that the model writes badly, it is that generation is creative by nature: layout, field order, currency format and footer drift between runs, and a drift that nobody notices until a client does.

This server removes the writing entirely. The document is a template the customer already owns, in Google Docs or Word. The data comes from the system of record, with linked fields expanded and line items nested up to three levels. The agent's job is to choose the template, choose the record and trigger the render. Everything that must be identical is not generated, which is the correct answer to the problem rather than a better prompt.

The second half is that a document is not finished when it is rendered. It is finished when it is signed. Generation, sending for signature and tracking completion sit behind one primitive with a legally recognised e-signature and an audit trail, so an agent can take a quote to acceptance without handing off to a mail client and losing the thread.

## What Was Verified

The endpoint is real and account-gated, which is what a document service should be. A bare `initialize` returns **HTTP 401** with a body that names all three auth paths at once: `Provide your DocsAutomator API key via Authorization header (Bearer <key>) or X-API-Key header, or use OAuth`, plus a pointer to `https://mcp.docsautomator.co/.well-known/oauth-protected-resource`.

That discovery document is the part worth recording because it is machine-readable and precise. It names the resource as `https://mcp.docsautomator.co/mcp`, the authorization server as `https://api.docsautomator.co`, and exactly two scopes: **`docsautomator:read`** and **`docsautomator:write`**. Two scopes is a better containment surface than one, because a read-only connection can list templates and render into a preview while the write scope is the one that sends for signature.

The vendor's own positioning is unusually specific about the failure being solved: agents are good at reasoning and orchestration and bad at producing the same invoice byte for byte, and templates remove creative drift. It also states the connected surfaces plainly: Claude through the Claude directory, ChatGPT through plugins, and any MCP client at `mcp.docsautomator.co`. Underneath, a paid product with 1,200+ business customers and a 4.9 rating across 15+ G2 reviews, which is context for maturity rather than evidence of quality.

An approvals feature is promoted at the top of the vendor site, where a team approves documents before they go out. For an operator wiring an agent to client-facing documents, that ordering matters more than the render: the agent produces, a person releases, and the signature request is the step that cannot be taken back.

## Limits Worth Recording

- **No tool was executed.** Every path needs an account, so the tool names, the record limits and the signature flow are the vendor's documentation and the discovery document. No render was performed in this pass.
- **Data comes from named sources.** Airtable, SmartSuite and Google Sheets are the connectors the vendor documents. A business whose data lives in something else is not served by the template path without an intermediate.
- **The template is the customer's.** Which is the point, and it also means a badly built template produces a consistently bad document. The deterministic render preserves whatever the template says, including a wrong field.
- **Two scopes, no per-document granularity.** `docsautomator:write` covers sending for signature, so a connection that can render can also send. Scope granularity is at the read or write level, not per template.
- **E-signature geography was not verified.** Legally recognised in which jurisdictions is a question for the vendor contract, and nothing on the pages read in this pass settles it.

## Wiring It Up

Connect over OAuth from the client if it supports dynamic registration, otherwise create an API key and send it as `Authorization: Bearer <key>` or `X-API-Key`. Start with the read scope and render a draft of a document already produced by hand, then compare the two before the write scope is enabled.

## FAQ

### Why use a template instead of letting the model write the document?

Because the requirement is sameness, not quality. A template fixes layout, branding, tax id, footer and field order, and the model only selects data. The vendor's framing is that the agent handles the trigger and the service handles the render, which is the division that survives a hundred runs.

### Can it send a document for signature?

Yes, as part of the same lifecycle: generate, send for signing, track completion, with an audit trail. That is what the write scope covers, which is why a read-only connection is the right starting point.

### Where does the data come from?

Airtable, SmartSuite or Google Sheets, with linked fields expanded and line items up to three levels deep. A system not on that list needs an intermediate step rather than a direct connection.

### Is it hosted or self-hosted?

Hosted, with nothing to install. That makes it easy to attach from any client and means the documents and templates live in the vendor's system, which is a data-residency decision an operator should make deliberately.
