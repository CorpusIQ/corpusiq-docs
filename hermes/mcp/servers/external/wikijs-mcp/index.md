---
title: Wiki.js MCP - Self-Hosted Wiki Knowledge Operations
description: "MCP server for self-hosted Wiki.js 2.x instances: 62 tools that search, read and edit pages, version history, tags, assets, comments, users and groups through the Wiki.js GraphQL API, with content grep, compare-and-swap updates and confirmation tokens for destructive operations. stdio via npx @ni-c/wikijs-mcp, MIT."
category: Knowledge Management
stars: "n/a (new listing, ni-c/wikijs-mcp)"
added: 2026-08-30
source: "mcp.so GitHub issue #3840"
relevance: ★★
tags: [mcp-server, wiki, knowledge-base, self-hosted, documentation, stdio, npm]
---

# Wiki.js MCP

**MCP server that gives an agent the run of a self-hosted Wiki.js 2.x instance.** 62 tools read and edit pages, version history, tags, assets, comments, users, groups, system settings and maintenance tasks through Wiki.js' GraphQL API. The headline design decisions are about safety on a shared knowledge base: content-level grep to compensate for Wiki.js' weak default search, compare-and-swap page updates so an agent cannot silently overwrite a colleague's edit, and server-issued confirmation tokens for every destructive or administrative operation.

```
Server type: Local (stdio via npx, or ghcr.io/ni-c/wikijs-mcp container)
Auth: Wiki.js API token (WIKIJS_API_TOKEN) + instance URL (WIKIJS_URL)
API: your self-hosted Wiki.js 2.x GraphQL API
Tools: 62 over pages, version history, tags, assets, comments, users, groups, system settings and maintenance
Safety: WIKIJS_READ_ONLY (read tools only), WIKIJS_ALLOWED_PATHS (confine writes to path prefixes)
Registry: io.github.ni-c/wikijs-mcp v0.1.2 (official MCP registry)
Pricing: Free (open source; you bring the Wiki.js instance)
License: MIT · Repo: github.com/ni-c/wikijs-mcp (created Aug 30, 2026)
Built by: ni-c (also ships healthchecks-mcp, google-search-console-mcp and imap-mcp)
```

```json
{
  "mcpServers": {
    "wikijs": {
      "command": "npx",
      "args": ["-y", "@ni-c/wikijs-mcp"],
      "env": { "WIKIJS_URL": "https://wiki.example.com", "WIKIJS_API_TOKEN": "your token here" }
    }
  }
}
```

## Why This Matters for Operators

Company wikis are where process knowledge actually lives, and Wiki.js is a popular self-hosted choice. Three design decisions make this server workable for an agent that shares the wiki with people.

First, **it can actually find text inside pages.** Wiki.js' default search engine indexes only titles and descriptions, so a question like "find the page that explains the refund policy" fails on stock tooling. `search_pages` reports which search engine is active, and `grep_pages` fetches pages and matches their content locally - the agent can answer questions that title-only search never could.

Second, **edits cannot clobber a colleague.** `update_page` compares against the moment the caller read the page and refuses to overwrite an edit somebody saved in between, rather than silently discarding it. Surgical find-and-replace edits must match exactly once instead of quietly changing the first occurrence. On a shared knowledge base, that contract is the difference between an agent that helps and one that destroys.

Third, **admin operations are token-gated.** Administering a wiki is not harmless, so every destructive and administrative operation needs a two-step, server-issued confirmation token bound to the exact target. `WIKIJS_READ_ONLY` registers only the read tools, `WIKIJS_ALLOWED_PATHS` confines writes to page path prefixes, and there is deliberately no tool that can mint an API key.

## Tool Groups (62 tools)

- **Pages (read):** page listing, page fetch, title and description search (`search_pages` with active-engine reporting)
- **Pages (search):** `grep_pages` - local full-content matching across pages
- **Pages (write):** create, update (compare-and-swap, exact-once find-replace), move, delete, restore from history
- **Version history:** list and diff page revisions, revert to an earlier version
- **Tags:** list, create, update, assign and remove tags
- **Assets:** list, fetch and upload page assets
- **Comments:** list, create, update and moderate page comments
- **Users and groups:** list and manage users, groups and permissions
- **System and maintenance:** locale, navigation, theme and site-configuration settings; cache and rebuild tasks
- **Safety toggles:** `WIKIJS_READ_ONLY=true` (6-tool read surface), `WIKIJS_ALLOWED_PATHS` path-prefix confinement

## Verification (Aug 30, 2026)

- npm registry: @ni-c/wikijs-mcp v0.1.2 published Aug 30, 2026
- Official MCP registry: io.github.ni-c/wikijs-mcp listed at v0.1.0, v0.1.1 and v0.1.2
- GitHub repo live (MIT, created Aug 30, 2026); submission body enumerates the contracts above
- Author's sibling servers (healthchecks-mcp, google-search-console-mcp, imap-mcp) are already catalogued and verified in this catalog

## Notes and Caveats

- stdio only: no hosted remote endpoint; the server runs where the client starts it and calls your Wiki.js GraphQL API
- Wiki.js 2.x line: check compatibility before pointing it at a different major version
- Brand new listing (repo created Aug 30, 2026, zero stars): treat as early-adopter tooling
- Confirmation tokens require a client that supports two-step tool calls; check your client's elicitation support before wiring destructive tools
- No API-key minting by design: key rotation stays a human task

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [healthchecks-mcp - Cron Job Health and Failure Forensics for Agents](/hermes/mcp/servers/external/healthchecks-mcp)
- [Google Search Console MCP (ni-c) - Property Setup and Search Analytics](/hermes/mcp/servers/external/google-search-console-ni-c-mcp)
