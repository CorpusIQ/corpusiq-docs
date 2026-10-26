---
title: OSIR Domain MCP - Registrar Operations for Agents
description: Register, renew, transfer and manage domains, DNS, VPS, email hosting and one-page sites through an ICANN-accredited registrar's 105-tool hosted MCP endpoint.
category: DevOps
stars: n/a (new listing)
added: 2026-09-02
source: mcp.so
relevance: ★★★
tags: [domains, dns, registrar, vps, email-hosting, domain-registration, remote-mcp]
last_updated: "2026-10-19"
---

# OSIR Domain MCP

**Remote MCP server (Streamable HTTP, none required to connect)** - the full domain lifecycle from OSIR, an ICANN-accredited registrar (IANA ID 4332). Search, register, renew, transfer and manage domains across 450+ extensions, then keep going into DNS, WHOIS privacy, VPS, email hosting, app hosting and one-page website publishing. One hundred and five tools, eleven guided prompts, and the same surface over the A2A protocol for autonomous agents.

```
Server type: Remote (Streamable HTTP)
Auth: None to connect; device login for account operations
Endpoint: https://be.osir.com/mcp/http
Tools: 105 (domains, suggestions, DNS, contacts, VPS, hosting, email, billing, account)
Pricing: Free to connect; pay only for domains and services ordered
Category: DevOps
Built by: OSIR (Apache-2.0, github.com/Osir-Inc/mcp-a2a)
```

## Why This Matters for Operators

Registering a domain is the single most common administrative action a business takes online, and it is surrounded by friction: registrar dashboards, DNS consoles, email hosting setup and billing pages that each speak a different language. An agent with OSIR's MCP handles the entire lifecycle in conversation.

The safety model matters as much as the coverage. **Every purchase is quoted first and executed only after explicit confirmation, so an agent never spends money silently** - destructive and financial operations stage behind an `executeConfirmedAction` gate. Availability checks, pricing and name suggestions need no login at all.

## Tools & Capabilities

| Group | Tools | Examples |
|---|---|---|
| Domains and transfers | 23 | `checkDomainAvailability`, `registerDomain`, `renewDomain`, `transferDomain`, `lockDomain`, `updateNameservers` |
| Domain suggestions | 6 | `generateDomainSuggestions`, `bulkDomainSuggestions`, `spinDomainWords` |
| DNS | 6 | `listDnsRecords`, `createDnsRecord`, `initializeDnsZone` |
| Nameserver hosts | 4 | `createHost`, `getHostsForDomain` |
| Contacts | 6 | `createContact`, `updateContact`, `getContactsForDomain` |
| VPS and servers | 16 | `listVpsPackages`, `orderVps`, `buildVpsInstance`, `addSshKey` |
| Apps and hosting | 13 | `osirAppDeploy`, `osirSitePublish`, `osirSiteDesignBrief` |
| Email hosting | 11 | `enableMailDomain`, `createMailbox`, `getMailDnsRecords` |
| Billing and payments | 8 | `previewPaymentFees`, `payInvoice`, `listInvoices` |
| Account and platform | 12 | `loginWithDevice`, `getAccountSummary`, `getMyAuditLogs` |

Eleven prompts guide multi-step flows such as finding and registering a name, moving a domain in, and a `website_designer` flow that interviews you, writes a one-page site and publishes it at `name.osir.app`.

## Installation

```bash
claude mcp add osir --transport http https://be.osir.com/mcp/http
```

The vendor publishes exact snippets for Claude Code, Codex, Cursor, VS Code, Claude web, ChatGPT and Gemini CLI, including headless device-login instructions.

## Configuration

```json
{
  "mcpServers": {
    "osir": {
      "type": "http",
      "url": "https://be.osir.com/mcp/http"
    }
  }
}
```

No credentials are needed to connect. Availability checks, pricing and name suggestions work immediately; account operations sign in once through a device login link that also works for headless agents.

## Business Relevance

- **Founders** search, register and secure a name plus DNS and email hosting in one conversation, without learning three dashboards
- **Agencies** manage many client domains, transfers and DNS records from one MCP surface with a full audit trail per domain
- **Operators** get VPS and dedicated-server catalogues with pricing quoted before anything is ordered
- **Autonomous agent teams** can run the same operations over A2A with confirmation-gated spending

## Integration with CorpusIQ

OSIR's domain and hosting lifecycle is the infrastructure layer next to CorpusIQ's business-data layer. An agent composing both can register the domain for a new venture, stand up email hosting, then pull the entity's financial picture from CorpusIQ connectors to feed the launch plan. For e-commerce operators, the flow is concrete: OSIR handles the storefront's domain and DNS while CorpusIQ reads Shopify, Stripe and Google Ads to measure what the storefront earns.

## Limitations

- Brand new listing with no track record yet
- Purchases flow through staging plus explicit confirmation, which adds a step to agent-driven orders
- Self-hosting the server requires running the open-source repo yourself; the hosted instance is the primary path
- Domain products are Registrar-specific - pricing competes with other accredited registrars
