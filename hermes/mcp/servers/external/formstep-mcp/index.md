---
title: "Formstep MCP - Requests and Forms for Agents"
description: "Agent-initiated requests: send one customer a branded prefilled form, collect files, signatures and answers back under field keys."
category: Business Operations
stars: n/a (new listing)
added: 2026-10-09
source: "mcpservers.org /all pages 1-5 (October 9, 2026 night sweep)"
relevance: ★★★
tags: [forms, requests, onboarding, data-collection, signatures, document-collection, oauth, remote-mcp]
---

# Formstep MCP

**Hosted MCP server for collecting verified customer information with one request** - your agent sends a form to one named person, prefilled with what you already know so they only confirm or correct it, and the answers come back keyed by field. Recipients upload files, sign, book or pay on the same page, with no account of their own.

```
Server type: Remote (Streamable HTTP at https://api.formstep.io/api/mcp)
Auth: OAuth 2.1 sign-in (dynamic client registration, PKCE) or an fs_ API token; one workspace per connection
Tools: Requests (fields_list, request_create, request_get, request_list, request_cancel, request_remind, request_replayCallback, document_create), forms lifecycle, a full form editor, share links, submissions and analytics, themes, settings, translations and workspace folders
Limits: 120 tool calls per minute per token; each request_create spends one unit of the workspace plan's monthly allowance; emailing recipients and analytics need Pro or Business
Category: Business Operations
Docs: docs.formstep.io (guides for sending a request and building a form with an agent)
```

## Why This Matters for Operators

The paperwork loop - supplier onboarding, tax forms, signed agreements, updated bank details - still runs on "please fill this in and reply". This server turns it into a tool call: the agent assembles the request from a published form, locks the fields it already knows, sends it to one person, and later reads the answers back as structured keys with your own external ID attached. Files arrive through a reserved upload, decision questions return an approve, decline or changes outcome, and an optional callback tells your system the moment the recipient submits instead of the agent polling.

## Tools & Capabilities

| Group | What it covers |
|---|---|
| Requests | List a form's field keys, create a request to one recipient with prefill, locked fields, context, delivery, expiry and callback; read, list, cancel and remind; replay a callback; reserve document uploads |
| Forms | Find, read, create, rename, publish, unpublish, trash and restore forms; folders, emoji, cover and logo |
| Editor | Read a form's full structure; insert text, contact, number, date, time, radio, checkbox, select, picture choice, switch, rating, linear scale, ranking, matrix, file, signature, payment and schedule questions; decision questions; headers, paragraphs, images, lists, tables, embedded content, dividers and document blocks; hidden fields, calculated fields, variables and logic rules |
| Sharing and results | Share links (including custom domains), completed submissions and drafts, and form analytics (views, submissions, completion rate, unique visitors by device, country, browser and source) |
| Appearance | Themes (light and dark), settings (notification emails, redirect, password, retention, language) and translated drafts |
| Guidance | Built-in guides and tool catalogs served over MCP (load_skill, load_tools) plus four prompts |

Destructive tools are marked and most clients confirm them; two actions cannot be undone at all (deleting a workspace folder, permanently revoking a share link).

## Installation

```bash
claude mcp add --transport http formstep https://api.formstep.io/api/mcp
```

The first call opens a Formstep sign-in in the browser: sign in, pick the workspace, authorize. A connection reaches that one workspace only; add Formstep again for another. Headless agents and scripts use an API token (`fs_...`) as a Bearer header instead, created under OAuth and API Keys in the workspace sidebar (tokens last 30 days).

## Configuration and Safety

- Every call needs a bearer token; without one the server answers 401 with a WWW-Authenticate header pointing to its OAuth protected-resource metadata (OAuth 2.1 with PKCE and dynamic client registration).
- Access is workspace-scoped; permission checks mirror the app (emailing recipients and analytics require Pro or Business plans).
- Monthly allowance: each request_create spends one unit on the workspace owner's plan; test requests (`test: true`) spend nothing.
- No file uploads through tool calls; document_create returns an upload URL valid for one hour (PDF and images only, 25 MB per file).
- The server never notifies your agent when a recipient submits; pass a callbackUrl or ask again later.
- Live probe: POST initialize returns 401 (authentication required).

## Example Prompts

- "Send our supplier onboarding form to Ada Lovelace, fill in the company name and lock it, use supplier-2041 as the external ID, and give me the link."
- "Has the supplier-2041 request been answered? Show me the answers."
- "Build a new form: contact details, a file upload and an approve or decline decision, then publish it."
- "Translate this form into Spanish as a draft and show me the changes before publishing."
- "How many views and submissions did the demo form get last month, and where did visitors come from?"

## Integration with CorpusIQ

Formstep collects the primary documents and answers; CorpusIQ keeps the business context around them. Start the request from chat, then ask CorpusIQ for the customer, invoice or project history from Stripe, HubSpot, QuickBooks or your storefront to check the answers against what the business already knows - one conversation from request to verified record.

## Limitations

- One workspace per connection; multi-workspace setups add the server once per workspace.
- Emailing the invitation and reminders, and reading analytics, need the Pro or Business plan.
- The agent is not told when a recipient submits unless you pass a callbackUrl to request_create.
- Images are set by URL or data URI; file uploads only arrive via document_create upload slots.
- Skills written inside Formstep's app chat do not travel over MCP; the server serves its own guides instead.

## FAQ

### Does the recipient need a Formstep account?

No. The recipient opens a branded form in their language, confirms or corrects the prefilled fields, and can upload files, sign, book or pay on the same page without signing in.

### What can the agent do without a paid plan?

Create, read and cancel requests within the plan's monthly allowance; emailing recipients and the analytics tool need Pro or Business.

### How does my system learn an answer arrived?

Read the request later by ID or external ID, or pass a callbackUrl to request_create so Formstep calls your endpoint on submission.

## See Also

- [SendNow MCP - Trackable Document Sharing for Agents](/hermes/mcp/servers/external/sendnow-mcp/)
- [PageProofer MCP - Website Feedback for Coding Agents](/hermes/mcp/servers/external/pageproofer-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
