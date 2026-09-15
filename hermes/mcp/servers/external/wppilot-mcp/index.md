---
title: WPPilot MCP - WordPress, Elementor and WooCommerce for Agents
description: WordPress MCP server as a free plugin. 133 typed abilities cover content, media, menus, plugins and settings, plus 16 free Elementor editing abilities, with WooCommerce MCP in Pro. Capability-governed, draft-first publishing and an audited change ledger.
category: Business Operations
stars: n/a (new listing)
added: 2026-09-06
source: mcpservers.org
relevance: ★★
tags: [wordpress, elementor, woocommerce, cms, page-builder, plugins, self-hosted]
---

# WPPilot MCP - WordPress, Elementor and WooCommerce for Agents

**MCP server (WordPress plugin, free)** - turns a WordPress site into an MCP server through the WordPress Abilities API and the official WordPress MCP Adapter, exposing 133 typed abilities on a fresh install instead of hundreds of one-off endpoints. Covers content, taxonomies, media, comments, menus, users, settings, plugins, Gutenberg and a 16-ability Elementor editor that works on the real element tree. WPPilot Pro extends the same endpoint into WooCommerce MCP and page-builder servers (Bricks, Divi, Oxygen, WPBakery and more).

```
Server type: self-hosted (WordPress plugin)
Auth: WordPress application passwords or capability-based credentials
Endpoint: your-site/wp-json or the MCP adapter route
Tools: 133 free abilities (16 Elementor) - 1,042 plugin-aware abilities in Pro
Pricing: free plugin - WPPilot Pro paid
Category: Business Operations
Built by: WPPilot Labs (github.com/wppilot-labs/wordpress-mcp-elementor-wppilot)
```

## Why This Matters for Operators

WordPress sites get built and maintained through the admin console, and agents pointed at the raw REST API either flood their context with endpoints or get write access without any guardrails. WPPilot's approach is the WordPress Abilities API: AI clients discover, inspect and execute typed abilities through a compact three-tool interface, and every ability runs under the WordPress capability system that already governs the human user.

**Safety is layered: content creation is draft-first (an absent or malformed status resolves to draft before any capability check, so nothing publishes by accident), destructive actions demand explicit confirmation, the change ledger records which agent credential made each write and can roll it back, and the Developer abilities (PHP execution, WP-CLI, filesystem) are blocked outside Developer Full Access and excluded entirely from the WordPress.org build.** Commenter email and IP are withheld below the `moderate_comments` capability, and user reads are privacy-minimized.

For operators, that means an agent can build pages, edit Elementor layouts and manage content on the same site they already run - with the same permission model, not a parallel one.

## Tools & Capabilities

| Domain | Abilities | What they cover |
|---|---|---|
| Content | 8 | List, search and read posts, pages and public custom post types; create, update, trash, restore, delete with explicit confirmation |
| Taxonomies | 7 | Discover taxonomies, list and read terms, create, update, delete with confirmation, assign terms to content |
| Media | 10 | List, read, import from URL, search openly-licensed stock, metadata and alt text, featured images, delete with confirmation |
| Comments | 6 | List and read (email and IP withheld below moderation), reply, edit, approve, hold, spam, trash, restore |
| Menus | 10 | Create, rename, delete menus; add, update, reorder, remove items; assign to theme locations |
| Revisions | 3 | List with autosaves distinguished, read against the live post, restore |
| Users | 4 | Privacy-minimized reads; email requires `edit_users` |
| Site | 2 | Site information and an explicit settings allowlist |
| Plugins & themes | 12 | Search the WordPress.org directory, activate, deactivate, update, switch themes with confirmation; install and delete are Developer-only |
| Gutenberg | 11 | Block-editor content, staged pending changes, browser finalization |
| Elementor | 16 | Read a document, inspect widgets and style properties, edit the element tree (add, edit, move, duplicate, reorder, delete), page settings |
| Design system | 19 | Typed design tokens, saved designs, contrast and composition checks |
| Preview | 2 | Compute what a write would change before applying |
| Skills | 4 + prompts | Reusable skills and site-wide instructions, each registering an MCP prompt |
| Changes | 3 | Read the redacted change ledger and roll a change back |
| Diagnostics | 3 | Scoped health, performance and configuration-security checks |
| Developer | 13 | PHP execution, WP-CLI, filesystem - Developer Full Access only |

Elementor abilities load only when Elementor 3.6 or newer is active and stay unregistered otherwise, so an agent is never offered a tool that cannot work on the site. Pro adds whole-page composition (`elementor-build-page`), templates, theme parts, popups, dynamic tags, global classes and the WooCommerce surface.

## Installation

Upload the plugin zip from the releases page through Plugins - Add New - Upload Plugin (the GitHub source zip is not installable - it has no vendor directory). Then connect any client that speaks the official WordPress MCP adapter.

## Configuration

```json
{
  "mcpServers": {
    "wppilot": {
      "type": "http",
      "url": "https://your-site.com/wp-json/mcp/v1"
    }
  }
}
```

Authentication uses WordPress application passwords tied to a real WordPress user, so every ability the agent runs resolves through that user's capabilities. Developer abilities stay blocked unless the site opts in.

## Business Relevance

- **Site owners** let an agent draft and edit content without publishing rights, by capability design
- **WooCommerce operators** (Pro) manage products, orders and store surfaces from the same endpoint
- **Agencies** roll back agent-made changes from the change ledger instead of restoring backups
- **Elementor users** get real tree-level editing (v4 atomic elements and v3 widgets) that free editing covers

## Integration with CorpusIQ

WPPilot complements CorpusIQ by adding the owned-website execution layer to the governed data layer. CorpusIQ reads the business (Shopify, GA4, Stripe) while WPPilot acts on the WordPress site itself under WordPress's own capability model. A composed workflow: an agent finds the underperforming landing pages through CorpusIQ's GA4 connector, drafts the revised page content and Elementor layout through WPPilot's draft-first abilities, and the operator publishes after review - analytics-driven site work with no write that bypasses approval.

## Limitations

- WordPress only, and the Pro surface (WooCommerce, full page composition) is paid
- The free Elementor abilities edit existing pages; whole-page composition is Pro
- New listing (September 2026) - fresh release cadence (1.10.0+), no long track record
- Capability-based safety is only as good as the WordPress user roles configured on the site
- Self-hosted plugin: you run it on your own WordPress install

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
