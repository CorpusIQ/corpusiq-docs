---
title: Elementor MCP Server - WordPress Website Automation
description: Open-source Elementor MCP Server for WordPress (GPL). Connect Claude, ChatGPT, Codex or Cursor to build, edit, inspect and automate Elementor sites with 41 free Elementor Core abilities plus typed WordPress content, media, settings and administration workflows with capability checks and confirmations.
category: Business Operations
stars: n/a (new listing)
added: 2026-09-06
source: mcpservers.org
relevance: ★★
tags: [wordpress, elementor, website-builder, cms, gpl, automation, self-hosted]
---

# Elementor MCP Server - WordPress Website Automation

**MCP server (WordPress plugin, GPL-2.0-or-later)** - an open-source Elementor MCP Server for WordPress that connects Claude, ChatGPT, Codex, Cursor and other MCP-compatible agents to build, edit, inspect and automate Elementor websites through the Model Context Protocol. Ships 41 Elementor Core abilities in Free alongside a full WordPress MCP server for typed content, media, settings, diagnostics and controlled administration workflows.

```
Server type: self-hosted (WordPress plugin)
Auth: WordPress application passwords or nonce-based authentication
Endpoint: your-site WordPress REST route
Tools: 41 Elementor Core abilities (Free) plus WordPress MCP tools
Pricing: Free core - Pro adds advanced builder features
Category: Business Operations
Built by: wpFelix (github.com/wpFelix/elementor-mcp-server)
```

## Why This Matters for Operators

Elementor powers a large share of commercial WordPress sites, and every change to one currently goes through a human clicking in the builder. This plugin gives an agent typed access to the same structures - with the guardrails WordPress already has: capabilities, typed schemas, safety profiles, rate limits and explicit confirmations - so an agent can build a landing page, fix a broken responsive layout or run a WordPress SEO workflow without admin credential sharing.

**The safety model is production-minded: WordPress capabilities govern every action, typed schemas validate inputs, safety profiles and rate limits bound behavior, and explicit confirmations gate changes.** The plugin is GPL with public source, tests, release workflows and checksums, so operators can audit exactly what an agent is allowed to do.

For operators, it turns the website into another agent-addressable system - inspect before maintenance, modify with confirmation, automate the repetitive parts.

## Tools & Capabilities

| Area | What an agent can do |
|---|---|
| Elementor build | Build Elementor websites, modify existing pages, fix responsive design, work with Elementor 4 Atomic Elements (41 Elementor Core abilities in Free) |
| WordPress structure | Manage WordPress structure through the WordPress MCP server - typed content, media, settings and diagnostics |
| SEO workflow | Run a WordPress SEO workflow across pages and metadata |
| WooCommerce | Build WooCommerce landing pages and store surfaces |
| Inspection | Inspect the site before maintenance with structured read tools |
| Administration | Controlled administration workflows with capability checks |

The full tool list is served from the plugin once installed; the table above follows the vendor's published feature set. The vendor maintains a free industry prompt library of agent workflows alongside the plugin.

## Installation

Download the plugin from the WordPress.org directory or the project releases, upload through Plugins - Add New - Upload Plugin, activate, then connect any supported client (Claude, ChatGPT, Codex, Cursor and others have per-client setup walkthroughs published).

## Configuration

```json
{
  "mcpServers": {
    "elementor": {
      "type": "http",
      "url": "https://your-site.com/wp-json/elementor-mcp/v1"
    }
  }
}
```

Authentication methods include WordPress application passwords and nonce-based flows; safety and change control is enforced server-side by the plugin's safety profiles and confirmation gates.

## Business Relevance

- **Site owners** get agent-assisted page building and editing without handing over admin credentials
- **SEO operators** run metadata and content workflows through the assistant against the live site
- **WooCommerce teams** build and edit landing pages with agent help
- **Agencies** automate repetitive Elementor edits across client sites with typed, auditable operations

## Integration with CorpusIQ

Elementor MCP Server complements CorpusIQ the same way WPPilot does: CorpusIQ reads business performance (GA4, Shopify, Stripe) while this plugin executes on the owned website under WordPress capability checks. A composed workflow: an agent identifies the store pages with the biggest conversion drop through CorpusIQ's GA4 connector, inspects those pages through the Elementor MCP read tools, drafts the layout and copy changes with explicit confirmation gates, and the operator reviews before publish. No data write crosses from the business layer to the site layer without a human in the loop.

## Limitations

- Elementor-specific by design; Gutenberg content is covered by the WordPress MCP tools, other page builders are not
- Pro tier adds advanced builder features; the Free core carries 41 Elementor abilities
- New listing (September 2026) - no long track record yet
- Self-hosted plugin on your own WordPress install; capability safety depends on configured roles
- The WordPress.org build and the GitHub source may differ in packaging (vendor directory)

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
