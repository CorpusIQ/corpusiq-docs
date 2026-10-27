---
title: "Walmart Marketplace MCP"
description: "MCP server for Walmart Marketplace APIs (US 3P sellers) - 234 operations across 28 bundled OpenAPI specs with spec-driven discovery, automatic OAuth2 token handling, multi-seller credentials, feed upload and report download. Items, orders, inventory, prices, promotions, returns and fulfillment from any MCP client."
category: "Commerce & E-Commerce"
stars: 0
added: 2026-08-23
source: "mcpservers.org /all + GitHub README"
relevance: ★★★
tags: [walmart-marketplace, marketplace-ops, ecommerce, oauth2, openapi, multi-seller, self-hosted]
last_updated: "2026-10-24"
---

# Walmart Marketplace MCP

**A spec-driven MCP server for Walmart Marketplace APIs - 234 operations across 28 bundled OpenAPI specs covering items, orders, inventory, prices, promotions, feeds, reports, returns and fulfillment, with automatic OAuth2 token acquisition and multi-seller credential management.** The server exposes discovery tools (`list_endpoints`, `describe_endpoint`), a generic API proxy (`call_endpoint`), feed upload and file download helpers, and a runtime spec refresher, so the agent discovers endpoints from the bundled specs and calls them without code changes when the API evolves.

```
Server type: Local (stdio, Python package)
Auth: Walmart OAuth2 (client credentials per seller, auto-refreshed)
Package: pip install mcp-walmart-marketplace (PyPI)
Tools: 6 core (list_endpoints, describe_endpoint, call_endpoint, upload_feed, download_file, refresh_specs) over 234 operations
License: MIT, Python 3.13+
Category: Commerce & E-Commerce
Built by: alyiox (GitHub)
```

## Why This Matters for Operators

Walmart Marketplace is where many Amazon sellers expand next, and its API surface is notoriously heavy: dozens of specs, environment-specific base addresses, OAuth tokens that expire mid-batch, and required headers that fail calls when forgotten. This server takes that entire burden off the agent: tokens are fetched, cached per credential, refreshed before expiry, and retried once on a 401, and the client secret never leaves token acquisition. A seller running multiple storefronts configures many credential sets and the agent picks per call.

The discovery design is the differentiator: instead of hard-coded wrappers that break when Walmart ships an API update, the agent reads the bundled OpenAPI specs (refreshable at runtime) and calls any operation by operation id or raw method and path. That means the whole 234-operation surface is reachable on day one, not just the handful someone wrote wrappers for.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_endpoints` | Enumerate operations from the bundled OpenAPI specs |
| `describe_endpoint` | Show parameters and schema for a specific operation |
| `call_endpoint` | Call any operation by id or raw method and path |
| `upload_feed` | Upload item, price, inventory and promotion feeds |
| `download_file` | Download reports and files (verified against production) |
| `refresh_specs` | Reload specs at runtime when APIs evolve |

Coverage areas: items, orders, inventory, prices, promotions, feeds, reports, returns, fulfillment, plus advertising, insights and settings management. Multi-region and multi-environment (production and sandbox) with per-seller credentials.

**Verification honesty from the README:** five operation families have returned 200 against production (feed-management, advertising, fulfillment-management, insights-management, settings-management) including real Excel workbook downloads; the remaining ~227 are wired from the specs with unit-test coverage only. Sandbox behavior and end-to-end `upload_feed` are documented as unverified. This is an early project (repo created Aug 21, 2026) with unusually candid status notes.

## Installation

```bash
pip install mcp-walmart-marketplace
```

Then register the package with your MCP client (the README carries per-client config samples). The config file holds only credentials; base addresses are hardcoded per environment.

## Configuration

```json
{
  "mcpServers": {
    "walmart": {
      "command": "python",
      "args": ["-m", "mcp_walmart_marketplace"],
      "env": {
        "WM_CLIENT_ID": "your-client-id",
        "WM_CLIENT_SECRET": "your-client-secret"
      }
    }
  }
}
```

Walmart Marketplace credentials (client ID and secret per seller, plus region and environment selection) come from the Walmart Developer Portal. Sandbox credentials are issued separately from production.

## Business Relevance

- **Walmart 3P sellers** manage listings, pricing, promotions, orders and returns from the assistant they already use, with multi-seller setups in one config.
- **Marketplace operators** automate feed uploads and report pulls that normally take hours of clicking through Seller Center.
- **Agencies running multiple seller accounts** switch credentials per call instead of juggling tokens manually.
- **Integrators** get a discovery-driven client that survives Walmart API changes without redeploys.
