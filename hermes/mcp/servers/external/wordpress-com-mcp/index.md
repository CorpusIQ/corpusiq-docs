---
title: "WordPress.com MCP - Manage Your Sites by Asking"
description: "The official WordPress.com MCP server from Automattic: run posts, pages, comments, media, stats and site settings from Claude or any MCP client."
category: Business Operations
stars: n/a (official Automattic server)
added: 2026-10-11
source: "mcp.so /feed (top card, Verified Featured) + Automattic developer docs; catalogued at the October 11, 2026 night sweep"
relevance: ★★★
tags: [wordpress, content-management, website, oauth, official, remote-mcp]
last_updated: "2026-10-19"
---

# WordPress.com MCP

**Automattic's official remote MCP server for WordPress.com** - one OAuth connection reaches every site on your account, and the same tool catalog serves WordPress.com-hosted and Jetpack-connected sites alike. An assistant can find a post, check the stats, draft a page that matches your theme, reply to comments, or read site settings, with your approval in front of every change. It ships with all paid WordPress.com plans and any Jetpack AI or Complete-connected site.

```
Server type: Remote (Streamable HTTP at https://public-api.wordpress.com/wpcom/v2/mcp/v1)
Auth: OAuth 2.1 (browser sign-in; only the sites you approve)
Tools: 60+ abilities across content authoring, site management, account and site structure
Category: Business Operations
Built by: Automattic (WordPress.com)
```

## Why This Matters for Operators

The website is where a lot of operator work quietly piles up: a typo on the pricing page, a comment that needs a reply, a stat someone wants before a meeting, a plugin that needs updating. This server puts that queue inside the assistant, and it can see the site's own design context - theme presets, applied styles, registered blocks - so content it drafts fits the site instead of looking bolted on. Unusually for a first-party MCP server, it also refuses to surprise you: every write, update and delete operation requires explicit user confirmation before it runs, destructive operations are surfaced for review first, and some deletes (categories, tags, media, taxonomy terms) are permanent by design. On a site that is a business asset, that confirmation discipline is the feature.

## Tools & Capabilities

The server exposes 60+ abilities in two shapes: STRAP facade tools that wrap a family of related operations behind one entry point (`action: list | describe | execute`) and standalone tools for one-off jobs. The exact set depends on the site's plan, the user's permissions and the account's tool settings, so `tools/list` against the server is the definitive answer.

| Group | What it covers |
|---|---|
| Content authoring (`wpcom-mcp-content-authoring`) | posts, pages, comments, media (with upload grants and AI image generation into the library), categories, tags, block patterns, synced patterns and site-wide content search; block-level section edits change one block in place; custom post types such as WooCommerce products and plugin fields ride along |
| Design context (`wpcom-mcp-site-editor-context`) | the active theme's color, font and spacing presets, applied styles and the blocks the site allows - read-only, and the recommended first call so new content uses preset slugs instead of hard-coded values |
| Site management | settings, statistics (published totals plus views and visitors for a range), plugins list, activity log, Jetpack Backup readiness and storage, Jetpack Scan (status and run), uptime Monitor, Newsletter settings and delivery status, Account Protection, launch and visibility |
| Plugins | search the WordPress.org and commercial catalogs, install, upload a ZIP, activate, deactivate, update or uninstall - plan-dependent, and pinned Jetpack and Akismet plugins stay put |
| Collaborators | list users and pending invites, invite by email (sends immediately), change roles and remove access, with previews before role and access changes |
| Site structure | block templates and template parts, block navigation and classic menus with their items, widgets and sidebars, and user-level global styles |
| Account (`wpcom-mcp-account`) | profile, notifications and inbox, domains and DNS records, connections, security status, subscriptions and billing (renewal stop and resume, payment method removal) |
| Standalone tools | `wpcom-user-sites` (find site IDs across WordPress.com and Jetpack sites), `wpcom-plans-list`, `wpcom-checkout-url`, `wpcom-domain-purchase`, `wpcom-ai-agent-sites-list` (public sites that opted into AI Agent Access), blog search that returns the blog's own voice guidelines, and a feedback tool straight to the server team |

## Installation

```json
{
  "mcpServers": {
    "wordpress-com": {
      "url": "https://public-api.wordpress.com/wpcom/v2/mcp/v1"
    }
  }
}
```

For Claude Code, one command: `claude mcp add wordpress-com --transport http https://public-api.wordpress.com/wpcom/v2/mcp/v1`. The same remote endpoint works in any MCP client that speaks Streamable HTTP (the docs show Cursor, VS Code and Codex snippets).

## Configuration and Safety

- OAuth on first connect: the client opens a browser sign-in and access is limited to the sites you approve; credentials are reused for later sessions.
- Write discipline: nothing writes without explicit confirmation, destructive operations are surfaced for review before confirmation, and some deletes are permanent by design.
- Data handling: the docs state data returned by the tools is used only as part of the current request and is not used to train AI models.
- Permissions are the ceiling: the tool set a connection sees depends on the plan, the user's role and the account's tool settings - a Contributor sees a smaller surface than an Administrator.
- Invites are real: `user.invite` and `user.resend-invite` send email immediately, so they should never be run to test.

## Business Relevance

- **Agencies and freelancers** managing client WordPress sites: report stats, draft updates and stage content edits from the same assistant that answers client questions.
- **Content teams**: article workflows end to end - draft, block-level edit, media, categories, tags and comments - without opening wp-admin.
- **Solo operators and small businesses**: keep the site moving (plugin updates, comment replies, a page edit) between everything else the assistant handles.

## Integration with CorpusIQ

The site is one surface; the business is bigger. Run the WordPress.com tools in chat, then ask CorpusIQ what the same business shows across its connectors - traffic and search data, revenue systems, support inboxes - with every number cited to its source. Site operations on one side, consistent business answers on the other, in one thread.

## Limitations

- The MCP surface is plan- and permission-gated; some features (plugin installation, Jetpack tools) require qualifying plans, and unavailable operations say so rather than failing silently.
- `statistics.get` returns site totals and range views, not top-posts, referrers or per-URL breakdowns.
- Block content survives the save pipeline in most cases but not always - the docs advise checking the `_content_warnings` field after writes.
- Some deletes are permanent with no trash (taxonomy terms, media), and role and access changes should be treated as serious.
- The server manages the WordPress side of the world; it is not a host console and does not replace wp-admin for edge-case administration.

## FAQ

### Does the WordPress.com MCP server cost extra?

It ships with all paid WordPress.com plans and works on any Jetpack AI or Complete-connected site using the same server and the same tool catalog.

### What can the assistant actually change?

Anything your role allows - posts, pages, comments, media, categories and tags, settings, plugins, menus and templates - but every write requires your explicit confirmation, and destructive operations are listed for review first.

### How is access scoped and revoked?

OAuth 2.1: the first connection opens a browser sign-in, and the assistant only reaches the sites you approve. Access can be withdrawn by disconnecting the client or changing the account's tool settings.

## See Also

- [Sitegoalie MCP - WordPress Operations for Agencies](/hermes/mcp/servers/external/sitegoalie-mcp/)
- [miniOrange WordPress MCP](/hermes/mcp/servers/external/miniorange-wordpress-mcp/)
- [Universally MCP - Site Translation Management](/hermes/mcp/servers/external/universally-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
