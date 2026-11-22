---
title: "KitScout MCP - Vetting a Tool Before It Gets Your Keys"
description: "Four keyless tools over 94,077 indexed agent tools that return a dated verdict on any MCP server, skill or plugin before it is installed."
category: "Developer Tools"
stars: n/a (vendor-hosted index)
added: 2026-11-22
source: "mcp.so submission queue #7802 on 2026-11-22T09:03:29Z; the official MCP registry record dev.kitscout/kitscout, four versions from 1.0.0 at 2026-11-15T01:57:05Z to 1.0.3 at 2026-11-19T01:12:39Z; keyless initialize, tools/list and nine tools/call requests on 2026-11-22"
relevance: ★★★★
tags: [tool-discovery, vetting, supply-chain, mcp-directory, agent-skills, maintenance, remote-mcp, keyless]
last_updated: "2026-11-22"
---

# KitScout MCP

**Every MCP server a business installs is a dependency with no package manager behind it: no lockfile, no advisory feed, and no way to tell an abandoned repository from a maintained product until it stops answering.** KitScout indexes 94,077 agent tools and answers one question about any of them, with a date attached.

```
Server type: Remote (Streamable HTTP, no session id)
Endpoint:    https://mcp.kitscout.dev/mcp
Auth:        none for all four tools
Tools:       4 (search_tools, get_tool, check_tools, list_categories)
Handshake:   kitscout 1.0.2 on protocol 2025-06-18
Registry:    dev.kitscout/kitscout, latest 1.0.3 published 2026-11-19T01:12:39Z
Source:      https://github.com/kitscout-dev/kitscout-mcp
Index size:  61 categories, 94,077 tools, counted from list_categories on 2026-11-22
```

## Why This Matters for Operators

An operator connecting an agent to a business system is making a supply-chain decision, and the information needed to make it is scattered across a GitHub star count, a last-commit date, a registry record and a URL that either answers or does not. KitScout gathers those four into one call and returns a verdict: `ok`, `caution` or `avoid`, with the facts behind it.

The mechanism is small and the middle of it is the useful part. `search_tools` finds candidates; `check_tools` judges tools found anywhere else, including ones KitScout has never indexed; `get_tool` returns the install line. It is the check step that this catalog had no entry for: forty-plus guides here recommend servers, and until this one nothing in the catalogue could weigh a server against its own maintenance record.

## The Index, Measured

`list_categories` returned **61 categories** across twelve groups, whose counts sum to **94,077**. The largest rows are the ones this catalogue writes about most:

```text
Multi-agent, orchestration & workflows   8,782
Web search engines & search APIs         4,959
Market data, stocks & crypto             3,994
Files, spreadsheets, CSV & PDFs          3,862
Code search, analysis & refactoring      3,750
E-commerce & marketplaces                3,608
Unusual, one-of-a-kind tools             3,522
Project & task management                2,825
```

The index is not only MCP servers. `search_tools` returned four result types in one response, and a query written as a sentence rather than a keyword worked: `when a customer pays an invoice in quickbooks` returned **52 matches** and ten results, the first of which is a *skill* carrying a `context_tokens` figure of **60**, meaning the number of tokens it costs in every conversation while installed. That is the field a cost-conscious operator needs and the one nothing else here supplies.

`prestashop orders inventory` returned **4** matches, and the four names are the honest answer to a question this pass asked separately: PrestaShop has four MCP entries in the index, not one.

## The Verdict, Driven on Five Targets

`check_tools` accepts up to five inputs, each a GitHub URL, an npm or PyPI id, a remote MCP URL or a name. Five were driven, and the verdicts span the whole range:

| Target | Verdict | Reason returned |
|---|---|---|
| `https://mcp2.corpusiq.io/mcp` | ok | made by the product's own company |
| `https://mcp.notion.com/mcp` | ok | made by the product's own company |
| `github.com/novalo-dev/prestashop-mcp-server` | caution | little adoption (2 GitHub stars) and not made by the product's maker |
| `github.com/oneshopmanager/prestashop-mcp` | caution | little adoption (0 GitHub stars) and not made by the product's maker |
| `github.com/modelcontextprotocol/servers-archived` | avoid | repository is archived (no longer maintained), no code changes for 543 days |

The `avoid` case is the one to study: an official reference repository with **307** stars, a MIT licence and **543** days since the last commit, refused on two stated grounds rather than a score. The `caution` cases show the limit just as clearly, because both PrestaShop entries are actively developed (nine and ten days since the last push) and were still held back for having two stars and no first-party badge.

The facts block is dated, and that is what makes it worth calling at all:

```text
CorpusIQ   first_party true  verified_publisher true  last_push_days 27
           daily_check "live (2026-11-21)"  live_now "answers"
           repo github.com/corpusiq/mcp-manifest
           badges verified_publisher, first_party, live
           tools listed: get_connector_status, resolve_connector, ask_corpusiq,
           select_runbook, list_runbooks, run_runbook, list_skills …
```

An operator asking "is this still alive" gets a *dated* liveness reading, not a reputation. On a remote server KitScout calls it during the check, so `live_now: "answers"` and `live_now: "answers, sign-in or key required"` are statements about that minute rather than about a badge someone earned.

## Where the Verdict Stops

The response says it itself, in a `note` returned with every check: *"ok is not a security or code review: read the code or check the publisher before giving a tool secrets or write access."* The three reasons it can cite are maker identity, maintenance and adoption, plus live status. A tidy, well-starred, actively pushed server that reads your environment on import passes.

Two other behaviours are recorded rather than smoothed:

- **No zero-result floor.** `search_tools` with the query `zzzz nonexistent tool qqq` returned `total_matches: 125` and a first result with **13,771** stars, so a nonsense query falls back to sheer popularity instead of returning nothing. Read the match count, not the presence of results.
- **Ten results maximum.** The QuickBooks query reported 52 matches and returned ten. There is no pagination argument in the schema, so the ranking is the whole answer.

## Install

```bash
claude mcp add --transport http kitscout https://mcp.kitscout.dev/mcp
```

No key, no account, no rate-limit notice in the responses. The vendor also ships a free Claude Code plugin that checks installed tools at session start and warns when one fails to start, is archived, deprecated or down (`https://kitscout.dev/watch`); it is a separate artifact and was not installed on this pass.

## Version Drift Worth Recording

The registry carries four records, and the descriptions narrate the index growing in public: **84k tools** in 1.0.0 on 2026-11-15T01:57:05Z, **88k** in 1.0.1 the same day at 17:25:57Z, then 1.0.2 and 1.0.3 on 2026-11-19T01:12:39Z. The handshake on 2026-11-22 answers `kitscout 1.0.2` while the registry's latest record is 1.0.3, and the server's own instructions read **~94,000** tools against the **94,077** counted here. A version string that lags its own registry is a small thing, and it is the sort of thing this tool exists to surface in others.

## When to Use It

- Before adding any third-party MCP server to an agent that holds credentials: pass the URL or repo to `check_tools` and read the reason, not the verdict alone.
- When auditing what is already installed: the inputs accept a bare name, and the Claude Code plugin does the same check on a schedule.
- When looking for a capability rather than a product: `search_tools` returns MCP servers, skills and plugins side by side, with the token cost of a skill shown.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [MCP Server Discovery - November 22, 2026 (Night)](/hermes/mcp/sweeps/sweep-november22-2026-night)
