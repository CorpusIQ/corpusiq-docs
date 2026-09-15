---
title: "Domain MCP: Dynadot Domain, DNS and Transfer Management"
description: "stdio MCP server (npm) that groups 108 Dynadot API actions into 10 composite tools for domain portfolio management: registration, renewals, DNS records, nameservers, WHOIS contacts, transfers, folders and aftermarket auctions. MIT licensed, Zod-validated, requires a Dynadot API key."
category: Productivity
stars: 12
added: 2026-08-23
source: "mcp.so GitHub issue #3703"
relevance: ★★★
tags: [domains, dns, dynadot, whois, registrars, transfers, stdio-mcp, npm]
---

# Domain MCP

**Skip the registrar dashboard and brittle one-off scripts: Domain MCP groups 108 Dynadot API actions into 10 typed, composite MCP tools for managing a domain portfolio from an AI client.** Built on Dynadot's API, the server covers registration, renewals, DNS records, nameservers, WHOIS contacts, transfers, folders and aftermarket operations, with Zod input validation and a consistent response envelope. MIT licensed, published to npm as `domain-mcp`, with a companion Claude Code plugin (`domain-agent-kit`) that adds destructive-operation confirmations.

```
Server type: stdio (local, npm package)
Auth: Dynadot API key (DYNADOT_API_KEY env)
Install: npx -y domain-mcp (Node.js 18+)
Tools: 10 composite tools covering 108 Dynadot API actions
Sandbox: DYNADOT_SANDBOX=true with a sandbox key for testing
License: MIT · Registry: io.github.joachimBrindeau/domain-mcp
```

## Why This Matters for Operators

Domain portfolios are a classic manual-ops trap: renewal dates spread across a dashboard, DNS changes done under time pressure, transfer auth codes buried in email. **Domain MCP turns the registrar into an agent-callable surface: "find domains expiring this quarter and group them by urgency" or "add an A record for example.com" become plain-language requests with typed validation on every call.** The toolset deliberately composites - instead of 100+ separate MCP tool definitions (which exhaust client context windows), related Dynadot operations are grouped into 10 tools, so an agent stays small and fast while still reaching every action.

## Tools & Capabilities

The 10 composite tools map to Dynadot's API surface:

| Area | What you can do |
|---|---|
| Domains | Search availability, register, renew, delete, lock, push and inspect domains, with pricing |
| DNS | Read and update DNS records, forwarding, parking and email settings; DNSSEC management |
| Nameservers | Create, edit, list and assign registered nameservers and glue records |
| Transfers | Start transfers, check status, manage authorization steps |
| Contacts | Create and maintain WHOIS contact records |
| Portfolio | Folders, account data, bulk settings and renewal organization |
| Aftermarket | List domains, manage auctions, bids, backorders and marketplace operations |
| Agent workflows | Generate domain name ideas, run portfolio audits, diagnose DNS issues |

Zod validates every input, responses follow a consistent format, and errors explain what went wrong. The Claude Code companion plugin adds an extra confirmation hook for irreversible and paid operations.

## Installation

```json
{
  "mcpServers": {
    "domain-mcp": {
      "command": "npx",
      "args": ["-y", "domain-mcp"],
      "env": {
        "DYNADOT_API_KEY": "your-dynadot-api-key"
      }
    }
  }
}
```

Requires Node.js 18 or newer and a Dynadot API key (generate one in the Dynadot dashboard under API settings). For safe experimentation, set `DYNADOT_SANDBOX=true` with a sandbox key - the sandbox simulates the API without real registrations or charges.

## Configuration

- `DYNADOT_API_KEY` - required; the Dynadot account key the server acts on.
- `DYNADOT_SANDBOX=true` - optional; route all calls to the Dynadot sandbox.
- `DYNADOT_SANDBOX_KEY` - optional; sandbox credential, paired with the flag above.

## Example Prompts

- "Check whether example.com is available and show similar names."
- "Add an A record for example.com and point it to 203.0.113.10."
- "Find domains expiring this quarter and group them by urgency."
- "Enable auto-renew for every unlocked .com domain."
- "Show the current nameservers and WHOIS contacts for example.com."

## Business Relevance

For operators running multiple products, campaigns and landing pages, domains are business-critical infrastructure: a missed renewal takes down email and site, and a wrong DNS edit breaks checkout. Domain MCP brings registrar operations into the same agent that already handles the rest of the stack, with validation that catches malformed records before they hit the API. Renewal triage, DNS changes and transfer tracking stop being dashboard chores and become conversational, auditable tool calls.

## Integration with CorpusIQ

CorpusIQ reads business data across 40+ connectors; Domain MCP handles the domain layer underneath them. An agent can audit a portfolio (Domain MCP), spot expiring domains, and combine that with CorpusIQ analytics on which domains actually drive traffic and revenue - prioritizing renewals by business value instead of calendar order. Domain MCP is write-side infrastructure for domains; CorpusIQ remains the read-side authority for business metrics.

## Limitations

- Dynadot only: no other registrars are supported.
- Local stdio transport - each machine running the agent needs Node.js and its own key.
- Your client should still confirm before destructive or paid operations; the extra confirmation hook exists only in the Claude Code companion plugin.
- Composite tools trade granularity for context economy - some exotic API parameters may not be exposed one-to-one.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [Just Domain MCP](/docs/hermes/mcp/servers/external/just-domain-mcp) - read-only domain availability and pricing checks
- [MCP Integration Guide](/docs/hermes/mcp) - connecting MCP servers to Hermes Agent
