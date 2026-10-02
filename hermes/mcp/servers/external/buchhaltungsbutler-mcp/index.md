---
title: Buchhaltungsbutler MCP - German Accounting for AI Agents
description: MCP server for BuchhaltungsButler, the German accounting SaaS. All 54 API v1 endpoints auto-generated from the official OpenAPI spec as safety-categorized tools (read, write, destructive) with readOnlyHint and destructiveHint annotations, stdio and Streamable HTTP transports, Docker deployment and built-in rate limiting. MIT.
category: Finance / Accounting
stars: n/a (new listing)
added: 2026-09-06
source: mcpservers.org
relevance: ★★★
tags: [accounting, german, bookkeeping, invoicing, receipts, openapi, mit, self-hosted]
---

# Buchhaltungsbutler MCP - German Accounting for AI Agents

**MCP server (stdio and Streamable HTTP, optional bearer token)** - a purpose-built bridge that exposes all 54 BuchhaltungsButler API v1 endpoints as MCP tools, generated automatically from the official OpenAPI specification (spec version 1.9.1). Every tool carries a safety category (read, write, destructive) and MCP annotations (`readOnlyHint`, `destructiveHint`) so hosts like Claude can auto-approve reads and demand confirmation before destructive actions. MIT-licensed, Docker-first, with built-in rate limiting that stays under BuchhaltungsButler's 100 requests per customer per minute cap.

```
Server type: stdio (local) or Remote (Streamable HTTP in Docker)
Auth: API credentials held server-side; optional bearer token on the HTTP endpoint
Endpoint: self-hosted (docker compose up)
Tools: 54 (full API v1 surface, grouped read / write / destructive)
Pricing: free (MIT) - requires a BuchhaltungsButler account
Category: Finance / Accounting
Built by: ohneben (github.com/ohneben/Buchhaltungsbutler-MCP)
```

## Why This Matters for Operators

German businesses that run their books on BuchhaltungsButler have 54 API endpoints available to them, but wiring a generic OpenAPI-to-MCP wrapper onto the spec means every operation looks identical to the model - a delete looks exactly like a read until it is too late. This server exists to make that handoff safe: each tool's description leads with a banner stating what the action does before it runs, the annotations flag reads and destructive operations to hosts that evaluate them, and credentials live in the server environment, injected per request, so they never reach the model.

**The safety categories are the whole point: read tools can run freely, write tools are marked as writes, and destructive tools (delete, cancel, reverse) announce themselves in three places - the tool name, the banner, and the annotation.** For an operator handing bookkeeping to an agent, that is the difference between "assistant that drafts an invoice" and "assistant that silently voids one".

The server is also production-ready in a way most hobby bridges are not: Docker plus docker-compose with a health check and auto-restart, self-throttling under the vendor's rate limit, and clean handling of batch payloads and HTML-cleaned descriptions.

## Tools & Capabilities

| Group | What the tools cover |
|---|---|
| Receipts (Eingangsbelege) | List open receipts from the last month, read and search receipt data |
| Invoices (Rechnungen) | Create invoice drafts, read, update and manage invoice documents |
| Transactions (Buchungen) | Read and post bank transactions to accounts (e.g. Sachkonto 4400) |
| Documents | Upload PDF receipts and attach them to the matching transactions |
| Master data | Read and create creditors (Kreditoren), customers and other master records |
| Evaluations (Auswertungen) | Generate the BWA (business evaluation) for a quarter, account sheets (Kontenblätter) |

All 54 endpoints are exposed, not a hand-picked subset - generated from the official OpenAPI spec so nothing is forgotten, with `$ref` resolution for batch payloads and HTML-cleaned descriptions. Each tool is categorized read (green), write (yellow) or destructive (red).

## Installation

```bash
git clone https://github.com/ohneben/Buchhaltungsbutler-MCP.git
cd Buchhaltungsbutler-MCP
docker compose up -d
```

Or run over stdio for Claude Desktop and other local launchers. The server reads BuchhaltungsButler credentials from its own environment and injects them per request; the assistant only ever sees tool inputs and API responses.

## Configuration

```json
{
  "mcpServers": {
    "buchhaltungsbutler": {
      "type": "http",
      "url": "http://localhost:8080/mcp"
    }
  }
}
```

For a server reachable beyond localhost, set the optional bearer token in the deployment environment and attach it as the authorization header in the client. The health check endpoint confirms the container is up before agents connect.

## Business Relevance

- **German SMEs and freelancers** get natural-language bookkeeping over their real BuchhaltungsButler data instead of API scripts
- **Accountants and tax advisors** let an assistant draft invoices, read receipts and prepare BWAs while destructive actions stay confirmation-gated
- **Operators who distrust agent writes** get annotation-aware hosts (Claude included) auto-approving reads and demanding confirmation on destructive tools
- **Self-hosting teams** get the whole thing in Docker with health checks, auto-restart and rate limiting built in

## Integration with CorpusIQ

Buchhaltungsbutler MCP complements CorpusIQ for German-market operators: CorpusIQ reads QuickBooks, Stripe and bank data for the international picture, while this server covers the BuchhaltungsButler bookkeeping surface that German accounting practices rely on. A composed workflow: an agent pulls bank transactions from CorpusIQ's bank and Stripe connectors, books them to the correct Sachkonto through the write tools, then generates the quarterly BWA and account sheet from the evaluation tools - with destructive operations refused until the host asks for human confirmation.

## Limitations

- German-market only: the API and tool descriptions target BuchhaltungsButler's German bookkeeping model
- Self-hosted: the server runs in your infrastructure and needs a BuchhaltungsButler account with API access
- New listing (September 2026) - a personal MIT project, no commercial support contract
- 100 requests per customer per minute is the upstream cap regardless of server configuration
- Generated from the vendor spec, so tool quality tracks the spec's completeness

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
