---
title: OpenCLI Skills — Agent CLI with Browser Automation Setup
description: "jackwener/opencli — 14 skills at 97.8K installs: opencli-usage, opencli-browser, opencli-autofix, smart-search, opencli-adapter-author, sitemap browsing, explorer, oneshot and operate modes for an agent command line."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/opencli-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "cli", "browser automation"]
---

# OpenCLI Skills — Setup Guide

**Source:** [jackwener/opencli](https://skills.sh/jackwener/opencli)
**GitHub:** [jackwener/opencli](https://github.com/jackwener/opencli)
**Skills:** 14 skills · 97.8K total installs
**Category:** Agent CLI & Browser Automation
**First Seen:** August 15, 2026 sweep (queued since June 19)
**Quality Tier:** 🟢 Production

OpenCLI is an agent command-line toolkit whose skill cluster teaches the CLI's usage, browser automation, autofix, and adapter authoring. The browser pair (opencli-browser 17.2K, opencli-browser-sitemap 5.2K) gives agents structured web navigation with sitemap-driven crawling, while opencli-autofix (15.6K) and smart-search (14.9K) cover automated fixes and search. It has sat in the sweep queue since the June 19 batch and is now guided with verified publisher-page counts.

---

## Installation

```bash
npx skills add jackwener/opencli
```

Individual skills:

```bash
npx skills add jackwener/opencli --skill opencli-browser
npx skills add jackwener/opencli --skill opencli-autofix
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the installer |
| **OpenCLI runtime** | The skills operate the OpenCLI tool itself |

## What It Provides

| Skill | Installs | Notes |
|---|---|---|
| opencli-usage | 18.6K | Core CLI usage patterns |
| opencli-browser | 17.2K | Browser automation via CLI |
| opencli-autofix | 15.6K | Automated code fixes |
| smart-search | 14.9K | Search workflow |
| opencli-adapter-author | 13.8K | Authoring adapters for the CLI |
| opencli-browser-sitemap | 5.2K | Sitemap-driven browsing |
| opencli-explorer | 4.1K | Exploration mode |
| opencli-oneshot | 4.0K | One-shot task execution |
| opencli-operate | 1.9K | Operational mode |
| opencli-sitemap-author | 1.5K | Sitemap generation |
| opencli-repair / opencli / opencli-generate | 668 / 373 / 70 | Repair, entry, generation |
| cross-project-adapter-migration | 4 | Adapter portability between projects |

## Quick Start

1. `npx skills add jackwener/opencli`
2. Start with `opencli-usage`, then add `opencli-browser` for web work
3. Ask: "open a browser via the CLI and navigate to this URL, then summarize the page"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Browser ops fallback** | opencli-browser as a CLI alternative to Playwright for lightweight page fetches |
| **Sitemap crawling** | opencli-browser-sitemap for structured site sweeps (docs, competitor pages) |
| **Autofix patterns** | opencli-autofix as a reference for self-healing script design |
| **Adapter patterns** | opencli-adapter-author + cross-project-adapter-migration for portable tool adapters |

## Limitations / Verification

- Skills target the OpenCLI tool; value outside it is pattern reference
- Browser capabilities depend on the OpenCLI runtime being installed

```bash
npx skills add jackwener/opencli --skill opencli-usage   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Chrome DevTools MCP Skills Setup](/hermes/skills/catalog/chrome-devtools-mcp-skills-setup/) — browser debugging

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
