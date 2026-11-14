---
title: "Scrapling - Web Scraping Framework Skill"
description: "d4vinci/scrapling: 6.7K combined installs across 1 listing, a web scraping framework skill for fetching, parsing and crawling."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/scrapling-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "web scraping", "python", "crawling"]
---

# Scrapling - Setup Guide

**Source:** [d4vinci/scrapling](https://www.skills.sh/d4vinci/scrapling) via skills.sh - 6.7K combined installs across 1 indexed listing; first seen Nov 14, 2026 (this sweep)
**GitHub:** 102,654 stars, BSD-3-Clause license, `main` branch, last pushed 2026-11-11, 11 `SKILL.md` files across `agent-skill/` and localized `docs/` mirrors
**Category:** Web scraping framework skill
**Quality Tier:** 🟡 Yellow - the single sampled skill passes Gen Agent Trust Hub and Socket but warns Snyk.

Scrapling is a Python web scraping framework, and the scrapling-official skill teaches coding agents the library itself, so the code they write matches the current API instead of guessing from stale training data. The README positions the framework as handling the full workflow from a single request to a full crawl, with HTTP requests, stealth browsers, JavaScript rendering and concurrent crawling.

The skill follows the AgentSkills specification and is readable by Claude Code, OpenClaw and other agentic tools. It packages guides for fetching, parsing, crawls, MCP and RAG as Markdown references the agent loads on demand, together with ready-to-run examples, so it can answer most Scrapling questions without leaving the editor.

## Installation

The skill's own docs document three install paths. Install with the skills.sh CLI:

```bash
npx skills add D4Vinci/Scrapling --skill scrapling-official
```

Or with Clawhub for OpenClaw:

```bash
clawhub install scrapling-official
```

Or download the skill ZIP from the repo and extract it into your agent's skills directory (for Claude Code, `~/.claude/skills/`). Install the framework itself separately with `pip install scrapling`, or `pip install "scrapling[all]"` for the fetchers, spiders, shell and extras.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| scrapling-official | 6,733 | Scrape web pages with Scrapling: HTTP requests, stealth browsers, JavaScript rendering, browser actions and API capture. |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

The skill's stated purpose is to stop an agent from writing Scrapling code against an outdated API. Scraping libraries change their fetcher and parsing interfaces often, and a model's training data lags those changes. The skill loads current references for fetching, parsing, crawls, MCP and RAG only when the task needs them, so the agent gets an up-to-date API surface without holding it all in context.

The references cover the safety rules too, including always passing `--ai-targeted` to CLI commands for prompt-injection protection when the agent shells out. That is a real operational concern for a scraping agent, which reads third-party pages that may contain instructions aimed at the model.

Because the install figure of 6,733 applies to a single indexed skill, the number reflects one focused skill with broad reach rather than a fragmented suite.

## Usage

| You say | What happens |
|---|---|
| "Scrape this page for me" | Runs the skill to fetch the page and extract fields with CSS or XPath selectors. |
| "This site needs JavaScript" | Runs the skill to render the page with a stealth browser before parsing. |
| "Crawl the whole site" | Runs the skill to build a concurrent spider with retries and proxy rotation. |
| "Export the results as Markdown" | Runs the skill to turn parsed content into clean Markdown output. |
| "Capture the API responses behind the page" | Runs the skill to record background API calls for extraction. |
| "Check my scraping code against the current API" | Runs the skill to verify the code matches the library's current interface. |

## Verification

Probe the skill before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/d4vinci/scrapling/main/agent-skill/Scrapling-Skill/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/d4vinci/scrapling/main/agent-skill/Scrapling-Skill/SKILL.md
```

The canonical skill file is `agent-skill/Scrapling-Skill/SKILL.md` on `main`; the `docs/` tree also carries `docs/ai/agent-skill.md` and localized mirrors under `docs/locales/*/ai/agent-skill.md`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| scrapling-official | Pass | Pass | Warn |

The single indexed skill passes Gen Agent Trust Hub and Socket and warns Snyk. One sampled skill says nothing about the framework code itself, so the verdict covers the skill package only: the repo is a 699-file Python framework whose dependencies the skill-level scan does not assess. Re-check the security page on skills.sh before production use.

## Limitations

- Snapshot data, verified 2026-11-14: 6,733 combined installs across 1 indexed listing; 102,654 GitHub stars; BSD-3-Clause; last pushed 2026-11-11. Counts drift over time.
- The index shows 1 listing against a tree with 11 `SKILL.md` files (the localized `docs/locales/*/ai/agent-skill.md` mirrors and `docs/ai/agent-skill.md`), so the install figure covers only the indexed skill, not the doc mirrors.
- The sampled verdict covers one skill package only: Gen Agent Trust Hub and Socket pass, Snyk warns. The framework code and its dependencies are outside that scan.
- The anti-bot and adaptive-parsing capabilities (stealth browsers, Cloudflare Turnstile/Interstitial handling, adaptive element tracking) are the framework's own README claims; re-verify them against your target sites before relying on them.
- Installing the skill teaches the agent the API but does not install the library; add `pip install scrapling` for the runtime.

## Related

- [Playwright Skill - Code-First Browser Automation Setup](/hermes/skills/catalog/playwright-skill-setup)
- [Bright Data Agent Skills - Web Scraping & Research Setup](/hermes/skills/catalog/brightdata-agent-skills-setup)
- [Browser-Use Automation - AI Browser for Anti-Bot Sites Setup](/hermes/skills/catalog/browser-use-automation-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the library (`pip install "scrapling[all]"`) at the same time as the skill; the skill only teaches the API.
- Keep the skill's `--ai-targeted` flag on CLI commands the agent runs, for prompt-injection protection.
- Use the on-demand references rather than dumping the full skill into context for a small scraping task.
- Scrape responsibly: confirm a site's terms and robots policy before turning a single fetch into a full crawl.
- The MCP server is a separate offering from the skill; reach for the skill when you want the agent to write Scrapling code, not just extract data.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
