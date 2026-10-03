---
title: "RankOrg MCP - SEO Content Engine for Agents"
description: "MCP that runs keyword research, topical maps, Search Console performance and scheduled article publishing through OAuth."
category: "Marketing"
stars: n/a (hosted platform, rankorg.com)
added: 2026-10-03
source: "mcpservers.org server page (rankorg-com-docs-mcp)"
relevance: ★★★
tags: [seo, content-marketing, keyword-research, search-console, publishing, topical-map, remote-mcp]
---

# RankOrg MCP

**Hosted MCP server** - RankOrg runs an SEO content pipeline from the agent: keyword research, a topical map of clusters and subtopics, Google Search Console performance, article drafting, scheduling and publishing, all against a site profile the operator already configured.

```
Server type: Hosted (remote MCP)
Auth: OAuth 2.0 (RFC 8414 discovery, RFC 7591 Dynamic Client Registration, PKCE) or a personal access token
Endpoint: https://rankorg.com/api/mcp
Tools: 12 (6 read, 6 write)
Category: Marketing
Built by: RankOrg (rankorg.com)
```

## Why This Matters for Operators

SEO work fails on coordination, not on any single step: the keyword research lives in one tab, the topical map in a spreadsheet, the drafts in a CMS and the Search Console numbers in another report. RankOrg puts the whole loop behind one MCP endpoint, and the split between read and write tools is explicit in the schema - a read-only client can pull `getSiteContext`, `listContent`, `getContent`, `getSearchPerformance` and `getTopicalMap` without being able to touch published content.

`getTopicalMap` is the interesting one for planning: it returns clusters to topics to subtopics to keywords with demand (volume and CPC), keyword difficulty, rankability scores, and it flags which keywords already have scheduled or published articles, so an agent can answer "which keywords are still open" from live state rather than a stale export.

`publishContent` is called out in the server's own docs as public and effectively irreversible, to be used only after explicit confirmation - a sane default for any tool that can put a page live.

## Tools

**Read**

| Tool | What it does |
| --- | --- |
| `getSiteContext` | The user's site (domains) and business/niche profile; call this first to ground everything else |
| `listContent` | Articles, filterable by `today`, `scheduled`, `published` or `all` |
| `getContent` | One article's full HTML, title, meta description, status and schedule by id |
| `getSearchPerformance` | Google Search Console performance - clicks, impressions, CTR, average position, top pages, top queries and a daily trend |
| `getTopicalMap` | Clusters to topics to subtopics to keywords with demand, difficulty, rankability and coverage status |
| `mergeContent` / `unmergeContent` | Combine or split content records |

**Write**

| Tool | What it does |
| --- | --- |
| `researchKeywords` | Generate a keyword profile (head terms plus long-tail) from the business profile and save it |
| `generateArticle` | Write the next SEO article from the highest-priority keyword on the topical map and schedule it into the next open slot |
| `updateContent` | Edit title, HTML content and meta description; the title is locked once published |
| `rescheduleContent` | Move a planned article to a new future date, or skip it to free the day |
| `publishContent` | Publish a scheduled article live immediately - public and effectively irreversible |
| `mergeContent` / `unmergeContent` | Combine or split content records |

## Connect

```
Endpoint: https://rankorg.com/api/mcp

Claude or ChatGPT: add https://rankorg.com/api/mcp as a Remote MCP server.
OAuth discovery happens automatically via /.well-known/oauth-protected-resource.

CLI tools (Codex, Cursor, scripts): generate a personal token at
Settings -> API access (MCP) and send it as Authorization: Bearer <token>.
```

Example prompt once connected: *"First get my site context, then list my scheduled articles for the next 7 days with title, publish date, status, slug and article ID."*

## FAQ

### Does RankOrg need a human to authorize?
For Claude and ChatGPT, no manual token handling: the server exposes OAuth 2.0 discovery and the client prompts for a one-click consent. Headless CLI environments use a personal access token created in Settings instead.

### Can an agent publish to a live site?
Yes, through `publishContent`, which the vendor documents as public and irreversible-ish and instructs callers to invoke only after explicit user confirmation. Scope the credential to read-only tools where publishing authority is not wanted.

### How does it tie content to business results?
`getSearchPerformance` reads the site's Google Search Console data directly, so published articles can be assessed against real clicks, impressions, CTR, average position, top pages and top queries rather than an assumed outcome.

## See Also

- [External MCP Server Catalog](https://www.corpusiq.io/docs/hermes/mcp/servers/external/) - the full curated list
- [CorpusIQ](https://corpusiq.io) - 40+ built-in business data connectors with OAuth 2.1 PKCE
