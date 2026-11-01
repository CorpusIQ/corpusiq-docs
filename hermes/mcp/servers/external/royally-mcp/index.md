---
title: "Royally MCP - WordPress Fleet Changes With Approvals"
description: "A cloud command layer for a WordPress fleet: an agent asks, Royally holds the change for approval, applies it across sites and returns a receipt you can undo."
category: Business Operations
stars: n/a (commercial, from $89 per year)
added: 2026-11-01
source: "The mcpservers.org /all newest page on 2026-11-01 under the slug royally-mcp, the official MCP registry record io.royally/royally at version 0.0.898 with status active and the remote https://app.royally.io/mcp, a keyless JSON-RPC initialize against that endpoint answering HTTP 401 missing_bearer_token, and the vendor pricing and documentation pages read through the r.jina.ai reader proxy"
relevance: ★★★
tags: [wordpress, agency-ops, approvals, audit-trail, undo, fleet-management, woocommerce, elementor, client-portal, commercial]
last_updated: "2026-11-01"
---

# Royally MCP

**An agency does not have one website. It has twenty, each with its own admin login, its own plugin set and its own owner who has to agree before anything changes. Royally turns that fleet into one command surface for an agent, and puts an approval queue, a receipt and an undo button between the agent and every site.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://app.royally.io/mcp
Auth:        account sign-in, API tokens per agent
Tools:       vendor-published, not measured (401)
Cost:        Solo $89/yr (3 sites) to Studio $390/yr (25 sites)
Registry:    io.royally/royally 0.0.898, status active
```

## What it does

Royally is two pieces. A plugin runs on each WordPress site, and the command layer runs in the cloud, so an agent talks to **one** connection instead of twenty site endpoints and nothing has to be hosted or patched on your side. The site plugin is what lets Royally read a site and make a change it can reverse afterwards.

The change flow is the product:

- **A request becomes a change request, not a write.** The agent asks for work, Royally records the request with who asked and which sites it touches, and holds it.
- **An approval window.** Nothing applies until a named person approves it, and the window can expire rather than waiting forever.
- **Two-person approval** for the changes a business would not want one person to make alone.
- **Site group rules** so the rule can differ by client: this group auto-approves cache purges, that group needs a second approver for WooCommerce price changes.
- **Safe jobs skip the queue.** A page cache purge after a menu edit runs without approval, on the same reasoning that keeps a rollback fast.
- **A receipt per change.** Who asked, who approved, what changed on which site, and the one click that puts it back. The receipts sit in a fleet-wide audit log described as tamper-evident, so an edit to the record itself shows, and the log is exportable on a signed path.
- **Only Royally makes changes.** The plugin supervises what reaches the site, so a second MCP server connected to the same site is governed by the same queue rather than writing around it.

## What the fleet jobs cover

The agent surface is deliberately wide because the work is wide, and each of these is a fleet operation rather than a single-site chore.

- **Updates** for plugins, themes and WordPress core, with a backup taken first, one item at a time, and automatic rollback of anything that breaks the site.
- **Security** scans and vulnerability alerts per site, plus alerts on a new administrator or an extra permission, working through GuardPress, Wordfence or Kadence Security where those are installed.
- **Backup health** across the fleet, reading SiteVault or UpdraftPlus, with an alert when a backup fails or never reaches cloud storage.
- **Monitoring**: uptime every five minutes, certificate and domain expiry, page speed and PHP fatal errors, routed to email, Slack, Discord or a signed webhook.
- **Bulk changes** previewed once and applied everywhere: SEO titles and descriptions, menu items, custom CSS, a page template copied to other sites, plugin and theme installs, users, maintenance mode, database clean-up, AI bot policies.
- **WooCommerce** prices, stock, orders and coupons across client stores, previewed first, approved once, with a seven-day undo.
- **Elementor** page builds from a brief, sections and global classes and display conditions, each build waiting on approval with a preview link handed over first.
- **SEO and speed** audits across sites for missing descriptions, schema, duplicate headings and broken links, pulling Search Console and Analytics data through Rank Math, SEOSbolt, Search Console and Analytics, and clearing caches fleet-wide without waiting on approval.
- **Client reports** weekly or monthly in the agency's brand as a link, a PDF or an email, plus a read-only portal per client.

## What this pass measured

The official MCP registry carries `io.royally/royally` at version **0.0.898**, status **active**, with `statusChangedAt` on **2026-11-01T04:1xZ** and a `streamable-http` remote at `https://app.royally.io/mcp`, and the same endpoint answered a keyless JSON-RPC `initialize` with **HTTP 401** and `{"error":"missing_bearer_token"}`, so the surface is live and gated rather than absent.

Two URL shapes are worth recording because both read like a delisting and neither is one: `royally.io/mcp` returns **404** (the endpoint is on the `app.` host), and `app.royally.io/.well-known/oauth-protected-resource` returns **404** with no protected-resource document, so the auth shape is established by the 401 body and the vendor documentation rather than by discovery metadata.

Pricing was read directly: Solo at **$89 a year** (regular $99) for 3 sites and 2 seats, Freelancer at **$249 a year** for 5 sites and 3 seats, Studio at **$390 a year** for 25 sites and 5 seats, with an Agency plan adding white-label and developer extras. Every plan includes the site plugin and the same approvals, receipts, undo and fleet jobs.

## The operator decision this answers

The question an agency principal actually asks is not "can an agent edit a page". It is "who changed this on the client's site, who agreed to it, and can I put it back before the client notices". Royally answers that at fleet scale: the log is the deliverable, and the agent is useful precisely because the log exists around it.

There is a second decision underneath it. Once several MCP servers can reach one WordPress site, the risk stops being "the agent does something wrong" and becomes "nothing records what any of them did". Sitting a governance layer in front of the site plugin, and routing other MCP servers through it, is the shape this catalogue has been arguing for since the tool-call audit entries appeared.

## Where it sits in this catalogue

The WordPress entries here are single-site: the official Automattic server works on WordPress.com hosted sites, and the SSO connector handles identity on one installation. Neither carries an approval queue, neither applies one change across a fleet, and neither leaves a receipt per change.

Royally is also the first entry in this catalogue that governs **other MCP servers** rather than only its own tools. Its documentation covers connecting the WordPress MCP Adapter, Easy MCP AI and Elementor MCP behind the same connection, with the stated rule that only Royally makes the change. That is a supervision layer, not a plugin list, and it is the reason this earns a guide at fleet scale rather than a hold beside the single-site editors.

## What this pass did not establish

The endpoint is gated, so the **tool count and tool names are the vendor's publication and not a measured list**, and no `tools/list` was driven. No OAuth authorization-server metadata was readable, so the exact sign-in flow is documented rather than observed. The site plugin, the backup-first update path, the automatic rollback, the seven-day WooCommerce undo and the tamper-evident log are all vendor claims that this pass could not execute against a live site. The homepage states plainly that its example sites and receipts are invented, so nothing on that page is evidence. The registry record is at **0.0.898**, which reads as a pre-1.0 surface that changes often, and the Agency tier price was not on the page this pass read.

## FAQ

### Does it need a plugin on every site?
Yes. Royally runs in the cloud and each WordPress site runs the site plugin, which is included in every plan. That plugin is what lets a change be applied and then reversed.

### What stops an agent pushing a bad change to a client site?
The approval queue, an approval window that can expire, optional two-person approval, per-group rules that can demand a reviewer for one class of change, previews before Elementor or WooCommerce writes, a receipt per change and one-click undo. Safe jobs such as a cache purge are the documented exception.

### Does it replace the WordPress.com connector in this catalogue?
No. That one is the official Automattic server for WordPress.com hosted sites. Royally works on self-hosted sites you or your clients run, and its unit is the fleet rather than the site.

### Can it sit in front of other MCP servers on the same site?
That is what its documentation describes: the WordPress MCP Adapter, Easy MCP AI and the Elementor MCP can be connected behind Royally, with the stated rule that only Royally makes the change. Treat it as documentation until a connected fleet proves it.

### What does it cost?
Solo $89 a year for 3 sites and 2 seats, Freelancer $249 a year for 5 sites and 3 seats, Studio $390 a year for 25 sites and 5 seats, each including the site plugin, approvals, receipts, undo and the fleet jobs. The Agency tier is priced separately.

### Is it useful for one website?
It is priced by fleet size rather than by seat, so a single owner with three sites sits at the entry plan. The value it sells, an audit trail and a client portal, is worth more to someone who works for other people's sites.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the full catalogue this entry belongs to
- [WordPress.com MCP - Manage Your Sites by Asking](/hermes/mcp/servers/external/wordpress-com-mcp/) - the official Automattic server for WordPress.com hosted sites
- [GLP Audit Proxy MCP - Tamper-Evident Tool-Call Trail](/hermes/mcp/servers/external/mcp-glp-audit-proxy/) - the same audit idea applied to the tool call instead of the site change
