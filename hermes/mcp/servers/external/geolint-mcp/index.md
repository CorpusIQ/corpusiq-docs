---
title: "geolint MCP - AI Search Readiness Linter for Websites"
description: "ESLint for AI search. geolint audits a website for AI-search readiness: which of 51 known AI crawler tokens are allowed in robots.txt, llms.txt presence and structure, JSON-LD structured data, citability signals and technical foundations. 51 rules, scored report, a concrete fix for every finding, runnable in CI. MIT, npm @iliasabk/geolint 0.3.2, with a built-in stdio MCP server for AI assistants."
category: SEO
stars: open source (MIT, npm)
added: 2026-09-14
source: "mcpservers.org /all page 1 (Sep 14 evening crawl) + repo docs at github.com/iliasabk/geolint"
relevance: ★★★
tags: [seo, aeo, geo, ai-search, llms-txt, robots-txt, structured-data, json-ld, citability, cli, mcp-stdio, open-source]
---

# geolint MCP

**Lint your website for AI-search readiness.** AI answers are the new front page: ChatGPT, Perplexity, Claude, Copilot and Google AI Overviews send traffic, or do not, based on whether their crawlers can fetch and quote your pages. geolint fetches a page, its robots.txt and llms.txt, evaluates 51 known AI crawler tokens against the rules, runs 51 audit rules across five categories, and prints a scored report with a concrete fix for every finding.

```
Server type: Local CLI (npx) with built-in stdio MCP server mode
Auth: none (site audit tool)
Install: npx @iliasabk/geolint check yoursite.com
MCP mode: geolint mcp (stdio server for AI assistants)
Version: 0.3.2 (npm, verified)
License: MIT
Category: SEO / AEO / GEO
```

## Why This Matters for Operators

Most sites accidentally block or confuse AI crawlers: a stale `Disallow: /` left over from staging, a `noindex` that never got removed, a client-rendered page that looks empty to a bot that does not run JavaScript. Existing tools are blocklists or score-only web apps. They tell you to block everything, or give you a number with no path to improve it.

geolint is the linter: concrete findings, concrete fixes, runnable in CI on every pull request. Five categories cover the full AI-visibility surface:

| Category | Rules | Examples |
|---|---|---|
| AI Crawler Access | 10 | search-bots-blocked, wildcard-block-all, stale-tokens |
| llms.txt | 10 | missing, invalid-structure, broken-links, relative-links |
| Structured Data | 6 | no-jsonld, invalid-jsonld, missing-article-fields |
| Citability | 9 | thin-content, no-h1, missing-dates, no-question-headings |
| Technical Foundation | 10 | client-rendered, https, slow-response, sitemap-missing |

## What a Report Looks Like

Real output from the bundled demo site:

```
geolint v0.2.1 - AI-search readiness
http://localhost:4173/
200 OK - robots 200 - llms.txt 404

██████████████████████████░░░░  86/100  Grade B

FINDINGS
  AI Crawler Access
    ✗ ai-crawler/search-bots-blocked  PerplexityBot is blocked by robots.txt -
        Perplexity cannot use your pages as AI answer sources
        fix: Remove the Disallow covering PerplexityBot in robots.txt, or add
        an explicit "Allow: /" for it.
  llms.txt
    ⚠ llms-txt/missing  No llms.txt found
        fix: Create /llms.txt at the site root: an H1 title, a short blockquote
        summary, and ## sections linking to your key content.
```

Every finding carries a rule id, a severity, the matched evidence, and a fix. The crawler report groups all 51 tokens by vendor (OpenAI, Perplexity, Google and the rest) and shows whether each is allowed for training, search, or user-fetch.

## Commands

| Command | What it does |
|---|---|
| `geolint check <url>` | Audit one URL; `--compare` two pages head-to-head, `--baseline`, `--fail-under` |
| `geolint crawl <url>` | Crawl same-origin pages and audit the whole site |
| `geolint init <url>` | Crawl the site and generate an llms.txt |
| `geolint diff <old.json> <new.json>` | Score delta plus added and resolved findings |
| `geolint rules` | List the 51 audit rules |
| `geolint bots` | List the 51 known AI crawlers and the impact of blocking each |
| `geolint mcp` | Run an MCP server on stdio for AI assistants |

## Installation

No install, no config:

```bash
npx @iliasabk/geolint check yoursite.com
```

Run it in CI with the official GitHub Action:

```yaml
- uses: iliasabk/geolint@v1
  id: geolint
  with:
    url: https://example.com
    fail-under: 80
```

And for AI assistants, the MCP mode serves the same audit as tools:

```bash
claude mcp add geolint -- npx -y @iliasabk/geolint mcp
```

## Business Relevance

- **Marketing teams** find out why AI assistants skip their pages before blaming the model.
- **SEO and AEO agencies** add a scored, fix-per-finding audit to every client engagement, runnable on every deploy.
- **Publishers and content sites** protect the traffic that flows through AI answers by keeping crawler access, llms.txt and structured data healthy.
- **Product teams** get a CI gate that fails the build when a page ships with a stale noindex or a blocked search bot.

## Integration with CorpusIQ

geolint audits whether AI systems can read your public pages; CorpusIQ answers whether the numbers those pages promise are actually retrievable. An assistant connected to CorpusIQ reads authorized business data (GA4, Search Console, Shopify, Stripe, HubSpot) with source-cited answers, so the same session can pair a geolint fix list with the traffic and conversion data that shows which fix moved. For docs and content teams, the two cover both halves of AI visibility: technically readable, and factually answerable.

## Limitations

- **New project** (npm 0.3.2) with a single maintainer; the rule set is opinionated and evolving.
- **Heuristic scoring.** A grade is a summary of the rules, not a ranking guarantee from any AI vendor.
- **Node 22+ required** for the CLI.
- **Crawler token list** covers the 51 known bots at release time; new tokens can appear between versions.
- **The MCP mode is local stdio only** - there is no hosted remote endpoint.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [Attensira MCP - AI-Search Visibility Data for Agents](/hermes/mcp/servers/external/attensira-mcp)
- [Serp Sidekick MCP - Live SEO Data for AI Assistants](/hermes/mcp/servers/external/serp-sidekick-mcp)
