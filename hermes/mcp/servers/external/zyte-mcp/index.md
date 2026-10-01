---
title: "Zyte MCP - Web Data Extraction for Agents"
description: "Official Zyte remote server giving agents unblocked HTTP fetching, browser rendering, structured AI extraction, web search and Scrapy Cloud job control."
category: Data & Extraction
stars: n/a (hosted platform, zyte.com)
added: 2026-10-01
source: "mcp.so feed + server page (zyte-mcp)"
relevance: ★★★
tags: [web-scraping, data-extraction, browser-automation, search, scrapy-cloud, remote-mcp]
---

# Zyte MCP

**Official web data extraction from Zyte, as a remote server.** Zyte MCP lets an agent fetch pages without getting blocked, render them in a browser, pull structured fields out with AI, search the web, and drive Scrapy Cloud projects. It is the vendor's own server rather than a community wrapper, which matters for an extraction surface an operator will point at production sites.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in
Endpoint: https://mcp.zyte.com/v1/mcp
Tools: 34
Pricing: server use is free; Zyte API and Scrapy Cloud usage bills to your Zyte account
Category: Data extraction
Built by: Zyte
```

## Why This Matters for Operators

Every agent that touches the open web hits the same wall: pages that block it, pages that need a browser to render, and pages whose useful content is buried in markup. The usual answer is a homegrown scraper that quietly breaks. Zyte already sells the unblocking and rendering layer as an API, and this server puts it behind a single MCP connection, so the agent asks for a page and gets one.

The extraction surface is the second half. Rather than returning raw HTML for the model to sift, the server can pull a product, article or job posting into fields, list the items on a listing page, and suggest the links to follow next. For an agent assembling competitive or catalogue data, that removes a whole parsing stage.

Scrapy Cloud control rounds it out: list projects and spiders, start and cancel jobs, read logs and items, and manage schedules, all from the same connection. That makes the server usable as both the scraper and the console for it.

## Key Capabilities

- **Fetch pages.** Plain HTTP requests for static pages, APIs and forms, with any method, headers and body. Zyte handles bans.
- **Use a browser.** Render a page, click, type, scroll, wait for an element, run JavaScript and take screenshots, enough to log in and continue.
- **Extract data.** Product, article or job fields, listing-page items, or links to follow; anything else by describing the fields in plain words.
- **Search the web.** Structured results from a chosen country and language.
- **Check cost and usage.** See whether Zyte API supports a site, what a request costs, and usage by date, domain or feature.
- **Run Scrapy Cloud.** Manage projects, spiders, jobs, logs, items, schedules, settings and collections.

## Setup

Claude Code:

```
claude mcp add --transport http zyte https://mcp.zyte.com/v1/mcp
claude mcp login zyte
```

Any MCP client that supports remote servers can connect with the endpoint URL. The vendor docs cover Codex CLI, GitHub Copilot CLI, VS Code and claude.ai.

## Considerations

Scrapy Cloud tools can change things, not just read them. An agent can start and cancel jobs, create and change schedules, alter project settings, and write or delete collection records, and deleting a schedule, collection or its records cannot be undone. Read what the agent proposes before approving it, and set a spending limit on the `mcp_access_key`, because one agent request can fan out into many billed Zyte API requests. New accounts get 5 USD of trial credit for one month.

## FAQ

### What does Zyte MCP do?
It gives an AI agent Zyte's web data extraction through one MCP connection: unblocked HTTP fetching, browser rendering, structured AI extraction, web search and Scrapy Cloud job control.

### Is Zyte MCP free?
The MCP server itself is free. What your agent does through it, Zyte API requests and Scrapy Cloud jobs, bills to your own Zyte account at standard prices.

### How many tools does the Zyte MCP server have?
34 tools, covering fetching, browser rendering, extraction, search, cost and usage reporting, and Scrapy Cloud operations.

### Does Zyte MCP support remote connections?
Yes, it is a remote Streamable HTTP server at https://mcp.zyte.com/v1/mcp with OAuth sign-in.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ](https://corpusiq.io) - 40+ business data connectors for AI agents
