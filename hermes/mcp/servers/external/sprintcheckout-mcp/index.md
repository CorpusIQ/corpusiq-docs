---
title: SprintCheckout MCP - Payment Links and Orders
description: "Official remote MCP for SprintCheckout, a crypto-first payment platform: 6 tools let a coding agent read payment settings and paid orders, pull receipts, create payment links and mint API keys, under OAuth 2.1 PKCE with scoped, instantly revocable consent. POST-only Streamable HTTP."
category: Commerce & E-Commerce
stars: n/a (hosted)
added: 2026-08-27
source: "mcpservers.org /all page 1 (docs-sprintcheckout-com-mcp-server)"
relevance: ★★★
tags: [payments, payment-links, orders, receipts, usdc, oauth, remote-mcp]
---

# SprintCheckout MCP

**Official remote MCP server (Streamable HTTP, POST-only, OAuth 2.1 with PKCE) for SprintCheckout payments.** SprintCheckout runs a hosted MCP endpoint so a coding agent - Claude Code, Cursor, VS Code or any MCP client - can operate the account the way a human would in the dashboard: read payment settings, list paid orders, pull receipts, create payment links and mint API keys. Authorization is scoped consent in the browser, revoked from Dashboard → Developers, and the server re-checks the grant on every call, so revocation takes effect immediately.

```
Server type: Remote (Streamable HTTP, POST-only; protocol 2026-07-28 with 2025-11-25 fallback)
Auth: OAuth 2.1 authorization code + PKCE (S256), browser sign-in with Google; Client ID Metadata Documents (no DCR)
Endpoint: https://mcp.sprintcheckout.com/mcp
Tools: 6 + 1 quickstart resource
Pricing: Vendor-platform feature; see sprintcheckout.com
Docs: https://docs.sprintcheckout.com/mcp-server
Category: Commerce & E-Commerce
```

## Why This Matters for Operators

Sellers of digital goods run payments through a dashboard: settings, orders, receipts, links and keys. SprintCheckout puts that dashboard into the agent that is already building and operating the product, so "create a payment link for the new tier" and "pull yesterday's receipts" happen in the same conversation as the code. **Every mutating tool is scoped - settings:read and orders:read are granted at sign-in, while sessions:write and keys:write are opt-in per scope - and the consent screen shows exactly what the agent can see.** Access tokens are audience-bound to this server and worthless against the regular API, with short-lived rotation and refresh-token rotation.

## Tools & Capabilities

| Tool | Scope | Purpose |
|---|---|---|
| `get_payment_settings` | settings:read | Business details, configured chains and accepted tokens (never returns the payout wallet address) |
| `list_orders` | orders:read | Paid orders, newest first, paged |
| `get_receipt` | orders:read | A public receipt by publicOrderId |
| `list_api_keys` | keys:read | API keys masked to last four characters, with count |
| `create_payment_session` | sessions:write | Creates a real payment link: amount, currency, editable buyer-chosen amounts with a floor, chain/token narrowing |
| `create_api_key` | keys:write | Mints one API key, returned exactly once |

A `sprintcheckout://quickstart` resource renders a live quickstart from the account's actual chains, tokens and payout state. Unknown tool arguments are refused by name, never silently ignored.

## Installation

```bash
claude mcp add --transport http sprintcheckout https://mcp.sprintcheckout.com/mcp
```

Then run `/mcp` and authenticate; the browser consent flow handles everything. Cursor, VS Code and repo-level `.mcp.json` setups are documented with one-click deeplinks on the vendor docs page.

## Configuration

```json
{
  "mcpServers": {
    "sprintcheckout": {
      "type": "http",
      "url": "https://mcp.sprintcheckout.com/mcp"
    }
  }
}
```

No API key, no local process - the server is a URL. Discovery documents (RFC 9728 protected-resource metadata, RFC 8414 authorization server metadata, JWKS) are all published, so compliant clients configure nothing by hand.

## Business Relevance

- **Digital-product sellers** create and manage payment links from the agent that ships the product
- **Finance ops** pull paid orders and receipts in chat instead of the dashboard
- **Platform teams** mint API keys through the same scoped, revocable consent model they grant the agent
- **Crypto-first businesses** get chain-and-token narrowing per session (Base/USDC and other configured tokens)

## Integration with CorpusIQ

SprintCheckout covers the payment-link layer that CorpusIQ's financial connectors read back. Where CorpusIQ pulls Stripe or QuickBooks revenue into analysis, SprintCheckout lets the agent create the actual payment sessions for new offers; the resulting orders flow back into finance reporting through CorpusIQ's connectors, closing the loop from "make the offer" to "the revenue landed". For operators selling digital goods to AI agents, SprintCheckout's x402-compatible buying path pairs with CorpusIQ's agent-facing business data for a full sell-and-report stack.

## Limitations

- New listing - no public adoption track record yet
- POST-only endpoint (GET returns 405) - requires an up-to-date MCP client
- No dynamic client registration by design (MCP spec 2026-07-28 deprecation)
- Payment-link creation is live-account real; consent scoping is the only gate
- USDC/chain payment rails are vendor-platform-specific

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
