---
title: "Qiaomu OpenCLI Skills - Social Site CLI Setup"
description: "joeseesun/qiaomu-opencli-skills on skills.sh: 9.4K combined installs across 7 listings; turn 79+ sites and desktop apps into CLI commands for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/qiaomu-opencli-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "opencli", "browser automation", "web scraping"]
---

# Qiaomu OpenCLI Skills - Setup Guide

**Source:** [joeseesun/qiaomu-opencli-skills](https://www.skills.sh/joeseesun/qiaomu-opencli-skills) via skills.sh - 9.4K combined installs across 7 indexed listings; first seen 2026-11-05 (Nov 5, 2026 morning sweep)
**GitHub:** 998 stars, MIT licence, last pushed 2026-04-09, 6 SKILL.md directories at the repository root (no skills/ prefix)
**Category:** CLI-first website and desktop app control: reusable browser sessions, search routing and adapter generation
**Quality Tier:** 🟡 Beta - Warn verdicts on every sampled skill; MIT; 998 stars.

This repository is a skills collection built on top of `jackwener/opencli`, a CLI that turns 79+ websites and desktop applications into command-line interfaces an agent can call. It covers social and content platforms (Bilibili, Twitter/X, Reddit, Xiaohongshu, Zhihu, YouTube, Weibo, V2EX, HackerNews), Electron desktop apps (Cursor, Notion, ChatGPT, Codex) and public APIs, with the README written in Chinese.

Six skills divide the work: a command reference, browser automation over Chrome's existing login sessions, a smart search router, two adapter-authoring skills for turning a new site into a CLI, and an autofix skill that diagnoses and patches an adapter when a command fails. Authentication is tiered from public endpoints up through browser cookies, headers, request interception and CDP control of desktop apps.

## Installation

Install the OpenCLI CLI itself first, since every skill shells out to it:

```bash
npm install -g @jackwener/opencli
```

Then install the browser extension. Download `opencli-extension.zip` from the upstream releases page, unzip it, load the unpacked folder at `chrome://extensions`, and make sure Chrome is already logged in to the sites you want to drive.

Install all skills:

```bash
npx skills add joeseesun/qiaomu-opencli-skills
```

Or install selected skills only:

```bash
npx skills add joeseesun/qiaomu-opencli-skills --skill qiaomu-opencli-usage
npx skills add joeseesun/qiaomu-opencli-skills --skill qiaomu-smart-search
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| opencli | 3,264 | The upstream OpenCLI command surface itself: 79+ site adapters and JSON output (this listing has no matching directory in the skills repo) |
| qiaomu-opencli-browser | 1,055 | Driving Chrome with existing logins: navigate, click, type, extract and wait, with no LLM API key |
| qiaomu-opencli-usage | 1,038 | Command reference for 79+ adapters, desktop apps and public APIs, plus installation and output formats |
| qiaomu-smart-search | 1,036 | Routing a search request to the best source, from social, news and technical content to shopping, jobs and finance |
| qiaomu-opencli-oneshot | 1,031 | Generating a single adapter from a URL and a goal: open the page, capture the API, write a TypeScript adapter, test it |
| qiaomu-opencli-explorer | 1,006 | Building a new adapter from scratch: exploring a site's API in DevTools and generating a CLI for a new platform |
| qiaomu-opencli-autofix | 994 | Diagnosing a failed command through OPENCLI_DIAGNOSTIC, patching the adapter and retrying |

All 7 indexed listings clear the 500-install threshold and appear in the table above, so there is no below-threshold tail.

## Why This Matters for Hermes Agents

Most web-facing agent work runs through a headless browser that arrives with no cookies, so every task begins with a login wall. OpenCLI inverts that: it drives the Chrome profile you already use, so a logged-in session on a social platform becomes a callable command rather than a scraping problem.

The command surface is also more compact than browser automation. `opencli bilibili hot --limit 10 -f json` returns structured data in one call, where a browser agent would need a navigation, a scroll and an extraction step, and would break the moment the layout shifted.

The adapter skills are the part with real leverage. `qiaomu-opencli-explorer` and `qiaomu-opencli-oneshot` document a repeatable path from a URL to a working CLI adapter, and `qiaomu-opencli-autofix` handles the inevitable decay when a site changes its API.

The fifth authentication tier, desktop app control over CDP, extends the same pattern to apps that have no web API at all, which is where most browser automation tooling stops.

## Usage

| You say | What happens |
|---|---|
| "Pull the top 20 HackerNews posts as JSON" | qiaomu-opencli-usage issues the hackernews command with a limit and JSON output |
| "Search Bilibili for AI videos" | qiaomu-opencli-usage issues the search command with a keyword and JSON format |
| "Find the latest AI papers from several sources" | qiaomu-smart-search routes the query across AI and specialist sources |
| "Build a CLI for this new site" | qiaomu-opencli-explorer walks the API exploration and adapter generation steps |
| "Just get me one command for this URL" | qiaomu-opencli-oneshot runs the four-step open, capture, write, test loop |
| "This adapter stopped working" | qiaomu-opencli-autofix reads the diagnostic output, patches the adapter and retries |
| "Log into this dashboard and click through it" | qiaomu-opencli-browser drives Chrome with the existing session |

## Verification

The README's own smoke test after installing the CLI and the skills:

```bash
opencli doctor
opencli list
opencli hackernews top --limit 5
```

`doctor` reports the CLI and browser extension state, `list` prints the adapters that are available, and the third command proves end-to-end retrieval works through the extension. To read a skill before installing it:

```bash
curl -fsSL https://raw.githubusercontent.com/joeseesun/qiaomu-opencli-skills/main/qiaomu-opencli-usage/SKILL.md | head -8
```

The skill directories sit at the repository root, not under `skills/`, so confirm the install landed as `ls ~/.claude/skills | grep qiaomu`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| opencli | Warn | Warn | Warn |
| qiaomu-opencli-browser | Warn | Pass | Warn |
| qiaomu-smart-search | Pass | Pass | Warn |

## Limitations

- Snapshot data, verified 2026-11-05: 9,424 combined installs across 7 indexed listings; 998 GitHub stars; MIT; last pushed 2026-04-09. Counts drift over time.
- Every sampled skill carries at least one Warn verdict, and the browser skill is the one that can act inside your logged-in Chrome profile. Review the source before giving an agent unattended use.
- The install index outruns the tree: 7 listings against 6 skill directories, and `opencli` (3,264 installs) has no matching directory in this repo because it documents the upstream CLI.
- The repository was last pushed on 2026-04-09 and describes itself as a Skills wrapper around `jackwener/opencli`, whose README badge tracks version 1.6.9. Adapters age quickly when target sites change, so expect autofix work on older installs.
- Installation is three-part: a global npm CLI, a manually loaded Chrome extension, and a Chrome profile logged in to the target sites. A headless server with no interactive Chrome cannot use most of the suite.
- The README and many skill descriptions are written in Chinese. Agents handle them, but human review of the command semantics is harder for non-Chinese readers.

## Related

- [Apify Ultimate Scraper - Universal Web Scraping for 15+ Platforms Setup](/hermes/skills/catalog/apify-ultimate-scraper-setup)
- [Bright Data Agent Skills - Web Scraping & Research Setup](/hermes/skills/catalog/brightdata-agent-skills-setup)
- [Firecrawl Skills - Web Scraping, Research & Workflow Suite Setup](/hermes/skills/catalog/firecrawl-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `opencli doctor` before debugging any skill behavior. Half of the reported failures are an unloaded extension or a logged-out Chrome profile, not an adapter bug.
- Load `qiaomu-opencli-usage` first and let it teach the command grammar. The other five skills all assume you can read the output format.
- Reach for `-f json` on every command. The plain-text output is for humans; an agent wants the structured form.
- Treat a broken adapter as expected maintenance rather than an incident: `qiaomu-opencli-autofix` exists because target sites change their endpoints without notice.
- Keep desktop app control on a separate machine or profile from general browsing. It runs through CDP against a live app session, which is not something to share with unrelated tasks.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
