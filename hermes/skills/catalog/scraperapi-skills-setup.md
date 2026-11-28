---
title: "ScraperAPI Skills - Web Scraping and Proxy Suite"
description: "scraperapi/scraperapi-skills: 2.5K combined installs. Official ScraperAPI skills for scraping, SERP, crawling and SDKs on its billed proxy."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/scraperapi-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "scraping", "proxy", "web data"]
---

# ScraperAPI Skills - Setup Guide

**Source:** [scraperapi/scraperapi-skills](https://www.skills.sh/scraperapi/scraperapi-skills) via skills.sh - 2.5K combined installs across 23 indexed listings; first documented 2026-11-27 (evening sweep)

**GitHub:** [scraperapi/scraperapi-skills](https://github.com/scraperapi/scraperapi-skills) - 10 stars, MIT, branch main, last pushed 2026-11-25; 20 skill directories live under `plugin/skills/<name>/SKILL.md`, with a `.claude-plugin/marketplace.json` listing and an `openclaw.plugin.json` manifest at the root.

**Category:** Web scraping, SERP and market data, SDKs and no-code workflows on the ScraperAPI commercial proxy

**Quality Tier:** 🟠 Orange - Snyk fails six sampled listings and warns on fourteen more; Socket and the Gen Agent Trust Hub pass every sampled listing.

ScraperAPI Skills is ScraperAPI's official agent-skill plugin, published as a Claude Code plugin with a companion skills.sh listing. It teaches an agent the full ScraperAPI surface: onboarding and product routing, the Standard API, Async Jobs, Crawler and DataPipeline primitives, best-practice guides for the Python, Node.js, Ruby, PHP and Java SDKs, the `sapi` command-line tool, and ready-to-run workflows for scraper building, lead enrichment, research, market research, SEO audits, SERP intelligence and price monitoring.

Using the suite requires a ScraperAPI account and API key, and every call the skills make is billed by the vendor. The README documents the data flow explicitly: the plugin sends only your API key plus the URLs, search queries and parameters you ask it to scrape to ScraperAPI's hosted MCP server and APIs, and the research-agent script additionally uploads scraped content to the Anthropic Files API.

## Installation

The README splits installation by runtime. Sign up at the ScraperAPI dashboard for an API key first, then export it and install the plugin on the runtime you use:

```bash
export SCRAPERAPI_API_KEY="your-key-here"
```

Claude Code installs from the community marketplace with slash commands:

```text
/plugin marketplace add scraperapi/scraperapi-skills
/plugin install scraperapi@scraperapi-skills
```

The Claude Plugin Hub and OpenClaw (ClawHub) installs are one-liners:

```bash
export SCRAPERAPI_API_KEY="your-key-here"
npx claudepluginhub scraperapi/scraperapi-skills --plugin scraperapi
```

```bash
export SCRAPERAPI_API_KEY="your-key-here"
openclaw plugins install clawhub:@scraperapitech/scraperapi-skills
```

The plugin ships with ScraperAPI's hosted MCP server (`mcp.scraperapi.com`) so all 28 MCP tools become available to the agent. Once installed, the skills load automatically; start an agent session and use one of the Usage prompts below.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| scraperapi-mcp | 213 | Knowledge base for the ScraperAPI MCP tools: scrape, Google, Amazon, Walmart, eBay, Redfin, the crawler and the AI Parser. |
| scraperapi-agent-onboarding | 131 | Entry point for new ScraperAPI users: pick the right product, get an API key, set up the MCP server. |
| scraperapi-python-sdk | 128 | Best-practices reference for the Python SDK: client setup, escalation ladder, async jobs, structured data, error handling. |
| scraperapi-async | 127 | Async Jobs REST API: submit background scraping jobs and get results by polling or webhook, including batches. |
| scraperapi-price-monitoring | 125 | Check, track and alert on Amazon, Walmart and Google Shopping prices with baseline change reports. |
| scraperapi-crawler | 125 | Crawl a whole site or section by following links when target URLs are not known up front. |
| scraperapi-cli | 125 | The official sapi command-line tool: install, auth, commands, JSON and piping, cost checks. |
| scraperapi-scraper-builder | 124 | Build a new scraper from scratch, generating Python or Node.js code with retries, pagination and credit estimates. |
| scraperapi-datapipeline | 124 | Managed, scheduled scraping projects that run automatically and deliver to a webhook or dashboard download. |
| scraperapi-research-agent | 122 | Run a standalone Python research script: plan searches, scrape, upload to the Anthropic Files API, cited report. |
| scraperapi-market-research | 121 | Market research from live web data: sentiment, demand trends, pricing, competitive landscape. |
| scraperapi-serp-intelligence | 120 | SERP landscape analysis: AI Overview presence, feature composition, intent, competitor visibility. |
| scraperapi-nodejs-sdk | 120 | Best-practices reference for the Node.js SDK: CommonJS and ESM, async/await, POST/PUT, error handling. |
| scraperapi-seo-audit | 119 | Audit a website's SEO health from live SERP and page data, with prioritized fixes. |
| scraperapi-lead-enrichment | 118 | Enrich one contact or company from any seed into a structured contact card. |
| scraperapi-php-sdk | 115 | Best-practices reference for the PHP SDK: Composer setup, request parameters, error handling. |
| scraperapi-java-sdk | 115 | Best-practices reference for the Java SDK: Maven/Gradle setup, fluent builder, escalation ladder. |
| scraperapi-ruby-sdk | 113 | Best-practices reference for the Ruby SDK: gem setup, escalation ladder, status-code error handling. |
| scraperapi-n8n | 113 | Generate n8n workflows using the official ScraperAPI community node. |
| scraperapi-zapier | 62 | Build Zaps with the official ScraperAPI Zapier integration: scraping, SERP and e-commerce data. |
| serp-intelligence | 1 | Indexed listing with no counterpart in the current plugin/skills tree. |
| seo-audit | 1 | Indexed listing with no counterpart in the current plugin/skills tree. |
| market-research | 1 | Indexed listing with no counterpart in the current plugin/skills tree. |

All 23 indexed listings appear above.

## Why This Matters for Hermes Agents

ScraperAPI Skills is a clean example of the vendor-suite pattern: a single plugin bundles 20 skills plus a hosted MCP server that exposes 28 tools, so installing it gives an agent both the knowledge and the live tooling in one step. The onboarding skill is the documented entry point, deciding which product fits a job before routing to the narrow skill, which keeps an agent from opening the wrong listing out of 23 names. The SDK split is the useful discipline: five language-specific references (Python, Node.js, Ruby, PHP, Java) each carry the same escalation ladder (standard, render, premium, ultra_premium), so an agent reasons about proxy tiers and credit cost consistently across languages. The workflow recipes (SEO audit, SERP intelligence, market research, lead enrichment, price monitoring) are opinionated end-to-end paths that each point back at the primitives they need. Cost discipline is explicit throughout: skills document credit costs and how to keep them down, and the README states exactly which services receive which data. For a builder routing vendor tooling, the key caveat is that every call is billed, so a routing layer should surface the cost note before an agent proposes a heavy scrape.

## Usage

| You say | What happens |
|---|---|
| "I'm building an agent that needs web data. How do I use ScraperAPI?" | Loads scraperapi-agent-onboarding to pick the product and API key, then routes to the right skill. |
| "Scrape this URL and give me clean text" | Uses the ScraperAPI MCP scrape tool, picking parameters to keep credit cost down. |
| "Submit these 5,000 URLs as an async batch and call me back" | Uses scraperapi-async to submit a background job with webhook delivery. |
| "Write a Python script that scrapes this site with premium proxies" | Uses scraperapi-python-sdk for client setup, the escalation ladder and retries. |
| "Crawl example.com and list every product URL" | Uses scraperapi-crawler to follow links and scrape each page automatically. |
| "Audit the SEO of my site" | Uses scraperapi-seo-audit against live SERP and page data from the MCP server. |
| "Enrich this contact: jane@example.com" | Uses scraperapi-lead-enrichment to build a structured contact card. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/scraperapi/scraperapi-skills/main/plugin/skills/scraperapi-mcp/SKILL.md
```

After a clone, confirm the plugin layout and the in-tree skill count:

```bash
git clone --depth 1 https://github.com/scraperapi/scraperapi-skills.git /tmp/scraperapi-skills
ls /tmp/scraperapi-skills/plugin/skills/ | wc -l
head -3 /tmp/scraperapi-skills/plugin/skills/scraperapi-mcp/SKILL.md
```

The count should print 20 skill directories, and head should show the scraperapi-mcp frontmatter. The index names 23 listings, so the three unprefixed names (serp-intelligence, seo-audit, market-research) have no directory in the current tree.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| scraperapi-mcp | Pass | Pass | Warn |
| scraperapi-agent-onboarding | Pass | Pass | Fail |
| scraperapi-python-sdk | Pass | Pass | Warn |
| scraperapi-async | Pass | Pass | Warn |
| scraperapi-price-monitoring | Pass | Pass | Warn |
| scraperapi-crawler | Pass | Pass | Fail |
| scraperapi-cli | Pass | Pass | Fail |
| scraperapi-scraper-builder | Pass | Pass | Fail |
| scraperapi-datapipeline | Pass | Pass | Warn |
| scraperapi-research-agent | Pass | Pass | Warn |
| scraperapi-market-research | Pass | Pass | Warn |
| scraperapi-serp-intelligence | Pass | Pass | Warn |
| scraperapi-nodejs-sdk | Pass | Pass | Fail |
| scraperapi-seo-audit | Pass | Pass | Warn |
| scraperapi-lead-enrichment | Pass | Pass | Warn |
| scraperapi-php-sdk | Pass | Pass | Warn |
| scraperapi-java-sdk | Pass | Pass | Fail |
| scraperapi-ruby-sdk | Pass | Pass | Warn |
| scraperapi-n8n | Pass | Pass | Warn |
| scraperapi-zapier | Pass | Pass | Warn |

skills.sh sampled 20 of the 23 listings; the three unprefixed listings (serp-intelligence, seo-audit, market-research) carry no verdict cells. This guide is Orange because Snyk fails six sampled listings (scraperapi-agent-onboarding, scraperapi-crawler, scraperapi-cli, scraperapi-scraper-builder, scraperapi-nodejs-sdk and scraperapi-java-sdk) and warns on the other fourteen, while Socket and the Gen Agent Trust Hub pass every sampled listing. The repository is documentation plus JSON manifests and an SVG icon with no shipped executable scripts, so the six Snyk Fail verdicts are worth reading on the skills.sh security pages rather than dismissing the suite as inert. Note also that this is a billed vendor service: it sends your API key and scrape parameters to ScraperAPI's hosted MCP server and APIs.

## Limitations

- Snapshot data, verified 2026-11-27: 2,463 combined installs across 23 indexed listings; 10 GitHub stars; MIT; last pushed 2026-11-25. Counts drift over time.
- Every call is billed: using the suite requires a ScraperAPI account and API key, and the skills make live calls to ScraperAPI's hosted MCP server and APIs at the vendor's credit rates.
- The install index outruns the tree: three listings (serp-intelligence, seo-audit, market-research) carry install counts but have no SKILL.md in the current plugin/skills tree; the other 20 map one-to-one.
- skills.sh sampled only 20 of the 23 listings for security verdicts; the three unprefixed listings have no verdict cells.
- The suite is a plugin for Claude Code and ClawHub (OpenClaw), not a bare skills-CLI install, so the hosted MCP server and its 28 tools arrive through the plugin marketplace.

## Related

- [X/Twitter Scraper - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/x-twitter-scraper-setup)
- [Instagram Scraper Skill - Social Data Extraction](/hermes/skills/catalog/skillify-instagram-scraper-setup)
- [Apify Ultimate Scraper](/hermes/skills/catalog/apify-ultimate-scraper-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load scraperapi-agent-onboarding first. It is the documented entry point that picks the right product and API key, then routes to the narrow skill, so the agent does not open the wrong listing from 23 names.
- Surface the cost note before a heavy scrape. The skills document credit costs and how to keep them down, and every call is billed, so a routing layer should flag cost before an agent proposes a big crawl or batch.
- Treat the three unprefixed listings as drift. serp-intelligence, seo-audit and market-research are indexed but have no SKILL.md in the tree; the prefixed scraperapi-* equivalents are the ones that install.
- Use the language SDK skill for existing code, and scraperapi-scraper-builder only for a new scraper from scratch; the skills cross-reference each other on this boundary.
- Review the Snyk Fail verdicts on the skills.sh security pages before installing into a production profile, since six of twenty sampled listings fail that scanner.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
