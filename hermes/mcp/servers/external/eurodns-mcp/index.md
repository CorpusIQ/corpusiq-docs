---
title: EuroDNS MCP - Domain, DNS and SSL Registrar Operations
description: MCP server for the EuroDNS User API covering domains, DNS zones, contacts, subscriptions, SSL certificates, invoices and orders. 82 tools generated from the OpenAPI document plus three safe DNS workflow tools, with guardrails that refuse billing and destructive operations, a hash-chained audit log, and OAuth 2.1 or shared-token auth over stdio or streamable HTTP.
category: DevOps
stars: 1
added: 2026-09-04
source: mcpservers.org
relevance: ★★★
tags: [domains, dns, ssl-certificates, registrar, infrastructure, dns-management, stdio, streamable-http]
---

# EuroDNS MCP

**MCP server (stdio or streamable HTTP)** - the full EuroDNS User API (Luxembourg registrar) as 82 agent tools: domains, DNS zones, contacts, subscriptions, SSL certificates, invoices and orders. Independent open-source project, not affiliated with EuroDNS, with two independent authorization gates and an audit log fed by every call including refusals.

```
Server type: Self-hosted (npx @jigsawfr/eurodns-mcp) or shared HTTP deployment (container)
Auth: OAuth 2.1 or shared token on HTTP; EuroDNS Application ID + API key for the upstream API
Tools: 82 (79 OpenAPI-generated + 3 DNS workflow tools)
Guardrails: read-only / billing / destructive refusals with the setting named in the error
License: MIT · Node.js 22+
Repo: JigSawFr/eurodns-mcp
```

## Why This Matters for Operators

Registrar consoles are where domain portfolios live, and the operations are boring, risky and frequent: renewals, DNS record edits, SSL subscription checks, contact updates. This server makes them agent-operable with the safety rails a registrar API demands. **The three dedicated DNS workflow tools exist because editing a zone replaces it - the diff tool shows what would change before anything is written, and upsert edits a single record instead of the whole zone.**

The guardrail system is the differentiator: a deployment can refuse whole risk classes (read-only, billing, destructive) and the error names the exact setting to change, so an operator can ship a read-only deployment to a junior agent and a full one to an admin. Every call - including refusals - lands in a hash-chained audit log queryable via `eurodns_audit_query`, because the upstream API authenticates with one shared key and cannot attribute calls itself.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `eurodns_domain_check_availability` | Is a domain available in a TLD |
| `eurodns_domain_search` | Search the portfolio (e.g. which domains have DNSSEC enabled) |
| `eurodns_dns_get_zone` | Read a DNS zone |
| `eurodns_dns_upsert_record` | Add or update a single record without replacing the zone |
| `eurodns_dns_diff_zone` | Preview what would change before a zone edit |
| `eurodns_ssl_list_subscriptions` | SSL certificate subscriptions and expiry |
| `eurodns_account_get_prepaid_balance` | Prepaid account balance |
| `eurodns_audit_query` | What was done, by whom, and what was refused and why |

Plus the remaining OpenAPI-generated surface: contacts, subscriptions, invoices and orders. A deployment resource lists what the deployment allows and why a tool may be absent.

## Installation

```bash
npx -y @jigsawfr/eurodns-mcp
```

Set `EURODNS_APP_ID` and `EURODNS_API_KEY` (created in the EuroDNS dashboard). The public IP of the machine running the server must be allowlisted in the dashboard - a 403 from the API is almost always a missing allowlist entry, not bad credentials. For a shared HTTP deployment, use the container image; the package also ships `eurodns-mcp-http` for the HTTP transport.

## Configuration

```json
{
  "mcpServers": {
    "eurodns": {
      "command": "npx",
      "args": ["-y", "@jigsawfr/eurodns-mcp"],
      "env": {
        "EURODNS_APP_ID": "your-application-id",
        "EURODNS_API_KEY": "your-api-key"
      }
    }
  }
}
```

Optional 1Password Connect integration can source any secret via `op://` references at startup. The HTTP transport adds OAuth 2.1 or a shared bearer token with scope gating on top of the deployment guardrails.

## Business Relevance

- **Domain portfolio managers** run renewals, DNS edits and SSL checks from an agent.
- **SRE and DevOps teams** get zone diffs and safe record upserts instead of full-zone replaces.
- **Finance operations** read prepaid balance and invoices through the same interface.
- **Compliance** gets a hash-chained audit log of every registrar action, including refusals.

## Integration with CorpusIQ

CorpusIQ covers the financial and business-data layer; EuroDNS MCP covers the domain infrastructure layer operators run beside it. A CorpusIQ agent auditing a company's tech footprint can check domain availability, DNSSEC coverage and SSL expiry through this server while CorpusIQ supplies the business context - a natural pairing for due-diligence and M&A workflows.

## Limitations

- Independent project (1 star); not supported by EuroDNS itself.
- Self-hosted: the operator runs and updates the server and manages the IP allowlist.
- Requires EuroDNS API credentials; no anonymous or read-only public mode.
- Node.js 22+ required; the container image runs Node 24 LTS.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [CTlogs.io MCP - Certificate Transparency Search for Agents](/hermes/mcp/servers/external/ctlogs-mcp)
- [Helixar MCP - Supply-Chain Security Scanning for MCP Servers](/hermes/mcp/servers/external/helixar-mcp)
