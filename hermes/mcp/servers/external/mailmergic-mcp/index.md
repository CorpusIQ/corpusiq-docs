---
title: "MailMergic MCP - PDF Mail Merge From a Chat, Ten Tools"
description: "Fills PDF, Word and Excel templates with spreadsheet rows and returns one document per row, with ten tools behind an OAuth chain."
category: "Business Operations"
stars: "n/a (documentation-only repository at github.com/mailmergic/mailmergic-mcp; the server is hosted by the vendor, star count not measured this pass)"
added: 2026-11-28
source: "appeared twice in one window: an mcp.so /feed card and the mcpservers.org slug mailmergic-com-ai-assistants on 2026-11-28; keyless initialize 401 with RFC 9728 protected-resource metadata, authorization-server metadata read, a dynamic client registration POST answering 201 with a client_id, the authorize endpoint answering 200 as the sign-in page, and the official registry record com.mailmergic/mailmergic 1.0.0 published 2026-11-27T12:26:02Z; the ten-tool surface is read from the vendor's public README because no token exists without an account"
relevance: "★★★"
tags: [mail-merge, documents, pdf, invoices, certificates, oauth, remote-mcp, german, smb]
last_updated: "2026-11-28"
---

# MailMergic MCP

**Every business of any size eventually produces the same document a thousand times: a certificate with a name on it, an invoice with a client's details, a badge, a receipt, a filled government form. The template exists; the rows exist in a spreadsheet; joining the two is either a Word mail merge that breaks on fonts or a PDF library that needs a developer. MailMergic sells that join as a product and now exposes it as a remote MCP server, and the split it chose is the interesting part: the assistant can pick a template, attach data, preview one row and start the merge, while designing the template and emailing a whole list stay in the web app where a person can see what is about to go out.**

```
Server type:  Remote (Streamable HTTP)
Endpoint:     https://api.mailmergic.com/v1/mcp
Registry:     com.mailmergic/mailmergic 1.0.0, published 2026-11-27T12:26:02Z
Auth:         OAuth 2.1, PKCE S256, dynamic client registration, no API key
Scopes:       templates:read, templates:write, merge, email:send
Tools:        10 (list_templates, get_template, upload_data_file, create_upload_link,
              set_recipient_data, preview_row, start_merge, get_merge_status,
              list_senders, send_test_email)
Vendor:       MailMergic GmbH, Eschborn, Germany
```

## The OAuth chain was walked, not quoted

A keyless `initialize` answers **401** with the header that tells a client everything it needs:

```
www-authenticate: Bearer realm="MailMergic",
  resource_metadata="https://api.mailmergic.com/.well-known/oauth-protected-resource/v1/mcp"
```

That document answers **200** naming the resource `https://api.mailmergic.com/v1/mcp`, the same host as the authorization server, header bearer only, the resource name **MailMergic**, and the four scopes above. The authorization-server metadata at `/.well-known/oauth-authorization-server` answers **200** with `response_types_supported: ["code"]`, `code_challenge_methods_supported: ["S256"]`, grants `authorization_code` and `refresh_token`, a `registration_endpoint`, a `revocation_endpoint`, and `token_endpoint_auth_methods_supported: ["none", "client_secret_post", "client_secret_basic"]`.

A registration POST to `https://api.mailmergic.com/v1/oauth/register` with a client name, a redirect URI, the code grant and `token_endpoint_auth_method: none` answered **201** and issued a `client_id` on the spot - so a client can self-register with no human and no vendor call, which is the property that separates a connector that works in ChatGPT and Claude from one that works in a screenshot. The `authorization_endpoint` then answered **200** rendering the MailMergic sign-in page for that client, which is the boundary: **the token requires a person.** No account was created for this entry, so the ten tools are documented from the vendor's own contract rather than driven.

## The ten tools, and the four scopes that gate them

| Tool | Permission | What it does |
|---|---|---|
| `list_templates` | templates:read | Templates with their fields and attached data |
| `get_template` | templates:read | One template's fields, data columns, unmatched fields, remaining credits |
| `upload_data_file` | templates:write | Attach a spreadsheet by file or by public https / Google Sheets link, up to 25 MB |
| `create_upload_link` | templates:write | A one-time upload page valid 30 minutes, for clients that cannot pass files |
| `set_recipient_data` | templates:write | Rows typed into the chat, up to 500 rows and 50 columns |
| `preview_row` | templates:read | A picture of the first page rendered for one row |
| `start_merge` | merge | Creates every document, spends one credit per document |
| `get_merge_status` | merge | Progress and download links, valid one hour |
| `list_senders` | email:send | Sender addresses and whether each is confirmed |
| `send_test_email` | email:send | One filled document to yourself, spends one credit |

The permission column is the design worth copying. A connection approved without `merge` can read templates and preview a document but cannot generate a thousand of them, and a connection without `email:send` cannot touch an outbound address. `preview_row` sitting beside `start_merge` is the same discipline this catalog rewards elsewhere: price the work, look at one unit, then commit.

## What it does not do in the chat, by design

Templates are built in the web app, not in the conversation, and a whole-list email send is a web-app action. The vendor states the reason as visibility - *"so you can see everything before it goes out"* - and it is the right call for a surface that produces documents carrying other people's names. The agent's job is the data and the run, not the layout.

## Five limits to plan around

1. **One credit per document, and one per test email.** A merge of 500 certificates costs 500 credits, the same as doing it in the app. The assistant is told to ask before creating documents, and `get_template` returns the remaining balance so a client can check before spending rather than after.
2. **No anonymous tier at all.** `initialize` is 401 and there is nothing to probe keylessly beyond the OAuth metadata. Unlike the servers in this catalog that answer discovery open and gate only the calls, this one gates the socket. That is legitimate for a document engine with customer data behind it, but it means an evaluation costs a signup, so the honest tier for this entry is documented rather than driven.
3. **Chat-typed rows cap at 500 rows and 50 columns.** Above that the path is a spreadsheet the client passes on, or the one-time upload page for clients like Claude that do not pass files. A client that ignores the cap will truncate silently at the tool boundary rather than at the merge.
4. **Uploads cap at 25 MB**, and the one-time upload page is valid **30 minutes**; the finished download links are valid **one hour**. A merge started and checked the next morning returns expired links.
5. **The data the assistant sees is the data you attach.** The vendor's privacy statement says the assistant receives template names and details, the column names of the list, one preview picture and download links. Column names are personal data when a column is called `patient_diagnosis`, so an operator should name columns by what they are, not by who they are about.

## Where it belongs

Beside the document and office entries already in this catalog, and it earns the place on the **output** side: those read and edit a document, this one produces thousands of them from one template and a spreadsheet. The business cases named by the vendor are the ones that actually recur in an SMB - certificates and awards, letters and notices, invoices and receipts, contracts, labels and badges, filled-in PDF forms, tax and HR forms, donation receipts. For a corpus of business data, a mail merge is the last mile of a report: the numbers are already in the spreadsheet, and what the customer wants is one PDF per account with the numbers in it.

```json
{
  "mcpServers": {
    "mailmergic": {
      "type": "http",
      "url": "https://api.mailmergic.com/v1/mcp"
    }
  }
}
```

## Also worth knowing

The product is German and the OAuth metadata is served from the API host rather than a separate identity domain, which keeps the chain short and auditable. The public repository is documentation only - there is nothing to install - and it carries the same ten tools, the same scopes and the same credit rules as the endpoint, which is why the entry can be specific without a token. One filing defect, recorded because this catalog records them: the mcpservers.org slug for this product is `mailmergic-com-ai-assistants`, a page path rather than a product name, so a search for the product on that directory finds a URL and a search for the vendor's own name finds nothing.
