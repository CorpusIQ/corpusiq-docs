---
title: "Logo.dev MCP - Brand Lookup by Domain, Ticker or ISIN"
description: "Logo.dev exposes its brand index as MCP tools: search brands, resolve a logo or brandmark by domain, ticker, ISIN or crypto symbol, and manage webhooks."
category: "Business Operations"
stars: n/a (vendor-hosted)
added: 2026-11-20
source: "mcpservers.org feed card 2026-11-20 + mcp.so detail page + logo.dev/docs/mcp/tools.md (16 tools) + keyless initialize, protected-resource and authorization-server probes on 2026-11-21"
relevance: ★★★
tags: [brand, logo, company-data, enrichment, design, webhooks, remote-mcp, oauth]
last_updated: "2026-11-20"
---

# Logo.dev MCP

**Remote MCP server (Streamable HTTP, OAuth)** - the Logo.dev brand index as tools. An agent can search brands by name, resolve one brand by a single identifier (`domain`, `ticker`, `isin`, `crypto` or `name`), fetch its logo or brandmark image, subscribe to update events, and manage webhook endpoints.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth against mcpauth.logo.dev, or an API key in the Authorization header
Endpoint: https://mcp.logo.dev/mcp
Protected resource: https://mcp.logo.dev/.well-known/oauth-protected-resource
Authorization server: https://mcpauth.logo.dev
Docs for agents: https://www.logo.dev/docs/llms.txt
Tools: 16
Category: Business Operations / Design data
```

## Why This Matters for Operators

Brand identity is the join key nobody documents. A CRM row has a domain, an invoice has a company name, a deck has a ticker, and every one of them needs the same two things before a report or a page looks finished: the correct logo, and confirmation that two records describe the same company. Logo.dev answers both from one identifier, which turns a list of accounts into cards, a competitor table into logos, and a customer page into a brand block.

The MCP surface is also honest about its own limits. A lookup that is still indexing returns `{"object": "brand", "status": "not_indexed"}` with `metadata.pending`, and an unknown brand returns `status: "not_found"`, so an agent can tell "not yet" from "never" instead of rendering an empty box.

## Tools

Every `/v2` route has a tool. Sixteen of them, from the vendor's own tools document:

| Tool | REST route | What it does |
|---|---|---|
| `search` | `GET /v2/search` | Finds candidate brands by name |
| `brand` | `GET /v2/brands` | Looks up one brand by a single identifier |
| `logo` | `GET /v2/brands/logo` | Returns a brand's logo image |
| `brandmark` | `GET /v2/brands/brandmark` | Returns a brand's brandmark image |
| `subscription` · `subscribe` · `unsubscribe` | `/v2/brands/{id}/subscription` | Reads, starts or stops `brand.updated` events |
| `create_webhook_endpoint` · `webhook_endpoints` · `webhook_endpoint` · `update_webhook_endpoint` · `delete_webhook_endpoint` | `/v2/webhook_endpoints` | Full endpoint lifecycle |
| `webhook_endpoint_secret` · `rotate_webhook_endpoint_secret` | `/v2/webhook_endpoints/{id}/secret` | Reads or rotates the signing secret |
| `account` | `GET /v2/account` | Plan and API credit balances |
| `flag` | `POST /v2/flag` | Submits domains for review |

`brand`, `logo` and `brandmark` each take **exactly one** identifier, so a call is `{"ticker": "AAPL", "nosubscribe": true}` or `{"domain": "stripe.com"}`, never a bundle. Tool results carry the same `data` and `metadata` as the REST route but no response headers, so credit and rate-limit detail stays a REST-only reading.

## Measured Authentication Behaviour

A keyless `initialize` answers **HTTP 401** with a short body and a complete challenge:

```text
www-authenticate: Bearer resource_metadata="https://mcp.logo.dev/.well-known/oauth-protected-resource"
{"docs_url":"https://www.logo.dev/docs/platform/api-keys","error":"missing or malformed bearer token"}
```

The protected-resource document answers **200** at the bare path and **404** when the `/mcp` suffix is appended:

```json
{"authorization_servers": ["https://mcpauth.logo.dev"],
 "bearer_methods_supported": ["header"],
 "resource": "https://mcp.logo.dev"}
```

The authorization server advertises itself at `https://mcpauth.logo.dev/.well-known/oauth-authorization-server` (**200**) with authorization code, refresh, device code and token exchange grants, `code_challenge_methods_supported: ["S256"]`, and `client_id_metadata_document_supported: true`. So both paths are real: an OAuth sign-in through `mcpauth.logo.dev`, and a bearer key per the linked key documentation. **No tool was called**; the probe establishes the gate and the surface, not a lookup result.

## Installation

```bash
claude mcp add logo-dev --transport http https://mcp.logo.dev/mcp
```

```json
{
  "mcpServers": {
    "logo-dev": {
      "url": "https://mcp.logo.dev/mcp"
    }
  }
}
```

Sign in through the client when it prompts, or attach a Logo.dev API key as a bearer token where the client supports a static header.

## Pricing and Attribution

Logo.dev bills in three separate units and the vendor asks that they not be conflated: the CDN at `img.logo.dev` charges **CDN requests**, the JSON API at `api.logo.dev/v2` charges **API credits**, and the MCP server's usage is **MCP usage**, which spends API credits. `account` returns the plan and the credit balance.

Attribution is a licensing term, not a suggestion: a commercial project on the free Community plan must show a visible `Logos provided by Logo.dev` link on its production site, while personal projects and paid plans need none.

## Honest Limits

- **It does not design logos.** The vendor's agent instructions say so directly: Logo.dev serves brands that already exist. For logo generation the catalog's creative entries are the right surface.
- **Index coverage is not guaranteed.** Never assert that a specific brand is missing; the correct move is a search, then `not_indexed` / `not_found` as the answer.
- **Subscription tooling needs webhooks enabled.** `subscribe`, `unsubscribe` and the endpoint tools fail when webhooks are off for the account, and endpoint changes need the owner or admin role on a team.
- **Credit exhaustion arrives as a tool error**, not a `402`, so an agent must read the error text rather than branch on HTTP status.
- **Deprecated routes.** The vendor says never to recommend `/search`, `/brand`, `/describe` or `/logo/*` from v1; the tools already target `/v2`.
- **The OAuth path is measured, not driven.** The gate and the authorization-server document are verified; a full sign-in and a first `brand` call are not.

## Integration with CorpusIQ

This is an enrichment primitive for the operator's own first-party data. CorpusIQ knows the customer list, the invoice counterparties and the campaign accounts; Logo.dev turns each identifier into a brand record and an image, so a dashboard can group revenue by parent brand or a report can render a competitor set correctly. Pair it with the company-registry entries in the catalog when the question is who owns whom rather than what a company looks like.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [The Company Atlas MCP - Trade Data and Company Registries](/hermes/mcp/servers/external/company-atlas-mcp)
- [3dlogo MCP Server - 3D Logos and Coins from Your AI](/hermes/mcp/servers/external/3dlogo-mcp)
