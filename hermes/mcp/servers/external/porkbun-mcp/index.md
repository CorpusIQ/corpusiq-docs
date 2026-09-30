---
title: "Porkbun MCP - Official Domain and DNS Management"
description: "Official Porkbun registrar MCP: domain availability, registration, transfers, DNS records, DNSSEC, URL forwarding and static hosting with dry-run safety."
category: Business Operations
stars: n/a (npm package @porkbunllc/mcp-server)
added: 2026-09-29
source: "mcp.so server page (porkbun.com)"
relevance: ★★
tags: [domains, dns, registrar, hosting, dnssec, remote-mcp, official]
---

# Porkbun MCP

**The registrar's own MCP server, built for agents.** Porkbun's official MCP server gives assistants direct, scoped access to a Porkbun account: domain availability and pricing, registration, renewal and transfers, DNS records, nameservers, glue records, DNSSEC, URL forwarding and static hosting. It is designed for agent safety: idempotent writes, dry-run first on risky operations, and stable error codes.

```
Server type: Remote (Streamable HTTP), plus local npx option
Auth: OAuth (Porkbun account sign-in) hosted; API keys for local use
Endpoint: https://mcp.porkbun.com/mcp
Tools: grouped capability set from the listing (domains, DNS, hosting, safety nets)
Pricing: Porkbun account (domain costs apply)
Category: Business Operations
Built by: Porkbun (official)
```

## Why This Matters for Operators

Domains and DNS are business infrastructure that breaks at the worst times, usually after a manual change. Porkbun's MCP server moves that surface into the assistant with guardrails built in: preflight a risky change to see what would break, roll a DNS zone back to an earlier restore point, and dry-run billable or destructive operations before they execute.

Writes are idempotent so a retry never double-charges or double-applies, money is handled in integer cents, and every error carries a stable code with a suggested next step. Operators who already manage Porkbun domains get this without a second vendor.

## Tools & Capabilities

| Capability group | What it covers |
|---|---|
| Domains | Check availability and pricing, register, renew and transfer domains, see renewal dates |
| DNS | Create, edit and delete records, change nameservers, manage glue records and DNSSEC |
| Safety nets | Preflight a risky change to see what would break, roll a DNS zone back to an earlier restore point |
| Hosting | Set up Porkbun Secure Static Hosting and deploy a site straight from the assistant |
| More | URL forwarding, domain contacts, webhooks, and domains connected to your own Cloudflare account |

## Installation

```bash
claude mcp add porkbun --transport http https://mcp.porkbun.com/mcp
```

Local option for coding agents that manage their own keys:

```bash
npx -y @porkbunllc/mcp-server
```

Set PORKBUN_API_KEY and PORKBUN_SECRET_API_KEY from the Porkbun API settings page.

## Configuration

```json
{
  "mcpServers": {
    "porkbun": {
      "type": "http",
      "url": "https://mcp.porkbun.com/mcp"
    }
  }
}
```

The hosted endpoint signs in with your Porkbun account and approves access; no API key is required for the hosted mode.

## Business Relevance

- **Operators** delegate domain renewals, transfers and DNS changes with dry-run safety
- **Web shops** ship DNS records and static hosting deploys from one assistant session
- **Teams** get a scoped, idempotent registrar surface instead of shared console logins
- **Agencies** manage client domains with preflight checks before risky changes

## Integration with CorpusIQ

Porkbun handles the domain plumbing around the assets CorpusIQ tracks. A composed workflow: CorpusIQ reports a store's health from Shopify or Stripe, the assistant drafts the fix, and Porkbun executes the DNS or hosting change with a preflight first - domain changes stay safe while business data drives the decision.

## Limitations

- Requires a Porkbun account; the server only reaches your own account
- Listing does not publish a static tool table; capabilities above are the vendor's published groups
- Local npx mode needs API key management on the client side
- Domain and hosting costs remain standard Porkbun pricing

## FAQ

### What are the two connection modes?

Hosted: add mcp.porkbun.com/mcp as a custom connector and sign in with your Porkbun account, no API keys. Local: run npx -y @porkbunllc/mcp-server with PORKBUN_API_KEY and PORKBUN_SECRET_API_KEY.

### How does it protect against mistakes?

Billable and destructive operations support a dry run first, writes are idempotent so retries never double-apply, and DNS zones can roll back to an earlier restore point.

### Can it spend money without my approval?

The server performs the account operations you approve during sign-in. Its own safety design is dry-run first on billable operations, with money always in integer cents and stable error codes for every failure.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
