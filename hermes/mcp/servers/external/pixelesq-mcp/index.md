---
title: "Pixelesq MCP - Website Management and SEO for Agents"
description: "Official remote MCP server for Pixelesq website projects. Agents create and edit pages section by section, write entries into collections, set SEO metadata and JSON-LD, read Google Search Console and site analytics, manage redirects, forms, images and theme - with every edit landing in a draft until the agent publishes. 62 tools, OAuth 2.1 PKCE."
category: Business Operations
stars: n/a (new listing)
added: 2026-09-12
source: mcpservers.org official listing (pixelesq-mcp)
relevance: ★★★
tags: [website-management, cms, seo, google-search-console, analytics, content, remote-mcp]
---

# Pixelesq MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 PKCE)** - the official agent interface for Pixelesq websites. Agents manage a whole site from a conversation: create pages and build them section by section, write entries into collections, set SEO metadata and JSON-LD structured data, read Search Console performance and site analytics, manage redirects, forms, images and the theme. Every save lands in a draft; the live site changes only when the agent publishes, and a publish is bound to the revision it reviewed.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 with PKCE (Google sign-in, or Pixelesq email + 6-digit code)
Endpoint: https://mcp.pixelesq.app/mcp
Tools: 62 total (59 offered in Claude; 3 AI image tools client-gated)
Scopes: projects:read, content:read, content:write, publish, analytics:read
Pricing: Pixelesq plan (sign up at app.pixelesq.ai)
Category: Business Operations
Built by: Pixelesq (pixelesq.com)
```

## Tools

| Tool group | Purpose |
|---|---|
| list_projects, get_project, list_domains, search_content | Projects, custom domains and their verification state, cross-site search over pages, entries and collections |
| list_pages, get_page, get_page_content, get_page_revisions, create_page, duplicate_page, update_page_meta, save_page_content, publish_page, unpublish_page, delete_page, revert_page_revision, revert_page_revision_to_version | Page CRUD with SEO metadata (title, description, Open Graph image, indexing preference, JSON-LD patched key by key) and revision rollback |
| list_section_types, get_section_defaults, get_section_content, save_section_content, insert_section, remove_section, reorder_sections, bind_section_to_collection, unbind_section_from_collection | Section-level page building from the section catalog; connect a section to a collection so it lists entries |
| list_collections, get_collection, list_entries, get_entry, create_collection, update_collection_schema, create_entry, save_entry_content, update_entry, duplicate_entry, publish_entry, delete_entry | Collections and entries: blog posts, team members, case studies, products. The agent reads the schema first so content matches the fields |
| list_partials, get_partial_content, save_partial_content, publish_partial, unpublish_partial | Header and footer partials, reusable across every page |
| get_gsc_connection_status, get_search_performance, get_page_index_status, get_all_page_statuses, inspect_url, get_site_analytics, get_ai_referral_analytics | Search Console performance and page index status, site analytics, and AI referral analytics |
| list_redirects, create_redirect, update_redirect, delete_redirect, list_forms, get_form_submissions | Redirect management, forms and their submissions |
| list_assets, search_stock_images, upload_asset, upload_image, get_theme, update_theme | Asset library, stock photo search and import, uploads from chat, and theme variables (colors, fonts, spacing, radius) as draft or published at once |
| generate_image, get_image_job, get_imagegen_quota | AI image generation (not offered in Claude, available in other clients) |

The draft-first model is the safety layer: a tool outside the granted scope answers with a reconnect request, saves are refused as stale when the page changed since the last read, and publishing requires explicit confirmation.

## Connection

1. Sign up at app.pixelesq.ai first - the connector needs an existing account.
2. Claude: Settings, Connectors, Add custom connector, enter `https://mcp.pixelesq.app/mcp`, sign in with Google or your Pixelesq email, then approve the permission grants.
3. Claude Code: `claude mcp add --transport http pixelesq https://mcp.pixelesq.app/mcp`, then run `/mcp` to sign in.
4. Other clients (Cursor, VS Code, ChatGPT): add the server URL in the client's MCP config and complete the OAuth sign-in flow.
5. Optional plugin: `/plugin marketplace add pixelesq/pixelesq-skills`, then `/plugin install pixelesq@pixelesq` - adds seven skills and four specialist agents.
6. mcp.json form: `{"mcpServers": {"pixelesq": {"type": "http", "url": "https://mcp.pixelesq.app/mcp"}}}`

## Verification (Sep 12, 2026 morning sweep)

Endpoint live-probed over JSON-RPC initialize: HTTP 401 with OAuth protected-resource metadata and the exact scope string `projects:read content:read content:write publish analytics:read` - the auth gate the docs describe. The official directory listing carries a full 62-tool reference (grouped by projects, pages, sections, collections, partials, SEO/analytics, redirects/forms, images/theme) and best practices.

## See Also

- [WPPilot MCP - WordPress, Elementor and WooCommerce for Agents](/docs/hermes/mcp/servers/external/wppilot-mcp)
- [Elementor MCP Server - WordPress Website Automation](/docs/hermes/mcp/servers/external/elementor-mcp-server)
- [Encited MCP - SEO and AI Visibility for Agents](/docs/hermes/mcp/servers/external/encited-mcp)
