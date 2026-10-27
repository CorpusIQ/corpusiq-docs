---
title: "PR-CY MCP - 69 SEO Tools, Search Console and Yandex"
description: "Keyword demand, SERP, rank tracking, crawler audits, Search Console and Yandex Webmaster behind one API key, with schemas for all 69 tools."
category: SEO / Search Analytics
stars: n/a (PR-CY account and API key)
added: 2026-10-27
source: "live MCP probes on mcp-server.pr-cy.ru (initialize 401 invalid_token), official MCP registry entry io.github.vlad4vic-creator/pr-cy-mcp 1.30.0, and the public interface documentation at github.com/vlad4vic-creator/pr-cy-mcp-docs, whose README records 69 tools checked against the live tools/list on 2026-10-27"
relevance: ★★
tags: [seo, keyword-research, serp, rank-tracking, site-audit, search-console, yandex, webmaster, analytics]
last_updated: "2026-10-27"
---

# PR-CY MCP

**One key, 69 tools, and the only surface in this catalog that puts Google Search Console and Yandex Webmaster next to a crawler audit and a keyword demand figure in the same conversation.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp-server.pr-cy.ru
Transport:   JSON-RPC over POST
Auth:        Bearer PR-CY API key, your own account
Tools:       69, verified against the live tools/list on 2026-10-27
Built by:    PR-CY (pr-cy.ru)
Registry:    io.github.vlad4vic-creator/pr-cy-mcp version 1.30.0
```

## Why This Matters for Operators

SEO data is normally three subscriptions and three schemas: a keyword tool, a rank tracker, and whatever the search engines' own consoles will let you read. The reconciliation problem is the same one this whole catalog exists for - the same question gets three answers, and nobody can tell which one is the business's actual position.

What earns PR-CY a guide is not the tool count. It is `get_changed_crawler_pages`, which finds audited pages whose tracked field changed inside a date range. That turns an audit from a photograph into a diff, and a diff is the only version an operator can act on.

## What It Actually Does

`initialize` without a key returned HTTP 401 `{"error": "invalid_token", "error_description": "Authentication required"}`, and the `.well-known` path behind it is gated the same way. What is public is unusually good: the repository publishes input types, required fields, enum values, defaults, behavioural limits, a JSON-RPC example and an output schema for all 69 tools, and its README records the count checked against the live `tools/list`.

| Group | Tools | Notes |
|---|---|---|
| Account and projects | 5 | `get_user_limits`, `get_user_projects`, `get_user_project_by_domain`, keyword project settings |
| Keywords and rankings | 7 | `create_keywords`, `delete_keywords`, `check_positions` launches a rank check, `get_keywords_positions_history` |
| Keyword groups | 4 | Named groups inside a project |
| Search and demand | 5 | `get_wordstat` for monthly demand and related phrases, `get_serp`, `get_position` for several comma-separated phrases in one request, `get_keywords_by_url` |
| Crawler audits | 3 | Summary with health score and issue counts, `get_crawler_pages`, `get_changed_crawler_pages` |
| Search Console and Webmaster | 3 | Keyword and page summaries, plus historical clicks, impressions and positions by day, week or month |
| Yandex Metrika | 9 | Visits, goals, sources, search engines, page depth, conversions, device split, geography, time series, conversion by source and landing page |
| Articles and HTML artifacts | 24 | Article create and edit, artifact draft, read, search, overwrite, range and substring replace, finalize, revisions, diff, revert, validate, persistent storage |
| Page content | 2 | `get_page_content` with a `structure` format |

## How It Is Contained

- **Your key, your limits.** Every tool call runs against the operator's own PR-CY account, and `get_user_limits` is the first tool precisely because the agent should know what it may spend.
- **Read and write are distinguishable in the schema.** `create_keywords`, `delete_keywords`, `check_positions`, the article edit tools and the artifact overwrite tools change state; the audit, demand, ranking and analytics tools read it.
- **Artifacts are versioned.** Overwrites and range replaces require the current revision ID, revisions can be diffed and reverted, and validation reports errors before finalizing - which is the correct shape for an agent editing content it did not write.
- **Public schemas.** The documentation repository is English, separate from the account data, and states plainly that it contains no server implementation or user data.

## Limitations Recorded

- No tool call was executed: the endpoint requires a PR-CY API key, so the surface comes from the published schema and the vendor's own verification note.
- **`get_serp` is Russian.** The interface supports `google` and `yandexLive`, and the `language` parameter is fixed to `ru`. An operator targeting English SERPs should not read this as a general-purpose SERP tool.
- **The deepest analytics are Yandex.** Metrika is nine tools deep; the Google side is Search Console summaries and history. A Google-first business gets a thin half.
- **Write tools exist.** The token is all-or-nothing per account, so an agent wired to this server can also create keywords, launch rank checks and rewrite articles.
- No project is required for page extraction, search, demand and one-off rank lookups, which makes it usable for research before any setup.

## FAQ

### What is the one tool an operator should try first?
`get_changed_crawler_pages` over the last 30 days. It names what broke, when it broke, and on which pages, which is the question a monthly audit cannot answer.

### Is it a replacement for Search Console?
No. It reads Search Console through the operator's connected project, so it is a single surface over the console rather than a substitute for it.

### Does it work for English sites?
Partly. Keyword demand, crawler audits, Search Console and rank tracking are language-agnostic; the SERP tool is fixed to Russian, so English SERP reading has to come from somewhere else.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CitedBy MCP - AI crawler access and llms.txt checks](/hermes/mcp/servers/external/citedby-mcp/)
- [CorpusIQ connectors for search and analytics data](/hermes/mcp/)
