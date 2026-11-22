---
title: "TinyFish Cookbook - Web Agent Recipe Suite Setup"
description: "tinyfish-io/tinyfish-cookbook: 26 agent skills and recipes for the TinyFish web agent, from search to job-market tracking - 4.5K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tinyfish-cookbook-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "web agent", "web scraping", "job search"]
---

# TinyFish Cookbook - Setup Guide

**Source:** [tinyfish-io/tinyfish-cookbook](https://www.skills.sh/tinyfish-io/tinyfish-cookbook) via skills.sh - 4.5K combined installs across 26 indexed listings; first catalogued Nov 21, 2026 (Nov 21, 2026 evening sweep)

**GitHub:** [tinyfish-io/tinyfish-cookbook](https://github.com/tinyfish-io/tinyfish-cookbook) - 2,334 stars, MIT license, main branch, last pushed Nov 21, 2026; skills live under `skills/<name>/SKILL.md` with `README.md` and `INSTALL.md` at the root, plus `plugins/tinyfish/skills/` for the agent, doctor, feedback, fetch and search skills and a large set of standalone recipe apps.

**Category:** Web Agent and Browser Automation

**Quality Tier:** 🟡 Yellow - 0 Fail cells in the 20-skill sample; Snyk Warns on all 20 sampled skills, plus 3 Gen Agent Trust Hub Warns and 3 Socket Warns.

TinyFish is a web layer for AI agents with four endpoints - Search, Fetch, Agent and Browser - that turn any website into programmable data. The TinyFish Cookbook is the official recipe collection: sample apps, automations and a set of installable agent skills that teach an agent when and how to reach for each endpoint. The flagship skill, use-tinyfish, carries 3,621 of the 4,510 combined installs and covers search, fetch, page reading, extraction and browser automation.

The rest of the suite is a career and market-research toolkit: freelance and salary scanners, interview prep, an interviewer-research skill, a job-market snapshot, competitor and product monitoring, npm package comparison, open source alternatives and developer pain-point mining. Beyond the skills, the repository ships dozens of standalone Next.js and Python recipe apps plus n8n workflows, an MCP server and a CLI, so the skills are one entry point into a much larger ecosystem.

## Installation

The README's one-line skill install:

```bash
npx skills add github.com/tinyfish-io/tinyfish-cookbook --skill use-tinyfish
```

The CLI, which every recipe skill leans on:

```bash
npm install -g @tiny-fish/cli
tinyfish auth login
```

The Python and TypeScript SDKs install with `pip install tinyfish` and `npm install @tiny-fish/sdk` respectively, covering Search, Fetch, Browser, Agent and Vault.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| use-tinyfish | 3,621 | core TinyFish web-agent skill: search, fetch URLs, read pages, extract and automate websites with source-backed answers |
| freelance-gig-finder | 56 | find fresh freelance and contract gigs across platforms for any skill set |
| oss-alternatives | 49 | find actively maintained open source alternatives to paid SaaS tools and APIs |
| salary-market-scanner | 45 | scan live job boards and salary databases for real-time compensation by role and location |
| project-idea-validator | 45 | validate a project idea against live GitHub and Dev.to data to surface what exists and where the gap is |
| npm-package-comparator | 45 | compare npm packages side by side on downloads, bundle size, stars, vulnerabilities and sentiment |
| competitor-product-monitor | 41 | monitor competitor product releases and feature announcements into a release report |
| leetcode-coach | 40 | find coding practice problems for your weak areas and set up local files to solve them |
| tech-stack-detective | 38 | reverse-engineer a company's tech stack from job listings, StackShare, GitHub and its live site |
| self-improve-with-tinyfish | 37 | index-only listing with no counterpart directory in the current tree |
| tinyfish-social-listening | 36 | monitor brand mentions, sentiment and industry chatter across the web with linked sources |
| interview-prep | 36 | build a company interview prep guide from real candidate experiences on Glassdoor, Blind and Reddit |
| dev-pain-finder | 36 | mine developer complaints from Reddit, Hacker News, dev.to and GitHub Discussions into a ranked opportunity map |
| stalk-my-interviewer | 35 | research an interviewer online before a meeting and return a structured prep report |
| kb-builder | 35 | build an Obsidian-compatible knowledge base from public web sources using the TinyFish CLI |
| job-market-intel | 35 | get a live job-market snapshot with salary data, in-demand skills and remote ratios from live postings |

The remaining 10 indexed listings range from 11 to 34 installs.

## Why This Matters for Hermes Agents

TinyFish packages the web as a callable API, which is exactly the surface most agents are missing. An agent that only reads its own context knows only what it was trained on; the use-tinyfish skill teaches it to reach for Search, Fetch, Agent or Browser at the right moment and to return source-backed answers instead of guesses. The job-market skills show the same discipline in a second domain: salary-market-scanner reads live postings rather than survey averages, and interview-prep compiles real candidate experiences rather than generic advice. For builders, the cookbook is a reference implementation of an agent product: dozens of full Next.js and Python apps show how to wire the same endpoints into shipping software, and the n8n workflows and MCP server show the integration patterns in between. The one caveat sits in the security sample: every one of the 20 sampled skills carries a Snyk Warn, so install and review each skill before letting it run unattended.

## Usage

| You say | What happens |
|---|---|
| Search the web for current pricing | Routes to the TinyFish Search endpoint and returns structured JSON results with sources |
| Summarize this URL | Fetches the page to clean markdown and feeds it to the model |
| Find me freelance React work this week | Runs freelance-gig-finder across gig platforms and returns fresh postings |
| Is my salary competitive in London? | Scans live job boards and salary databases for real-time compensation for the role and location |
| What does Stripe use under the hood? | Reverse-engineers the company's tech stack from public signals |
| Should I build this idea? | Validates the idea against GitHub and Dev.to and returns a gap analysis |
| Watch my competitors' launches | Monitors competitor product releases and feature announcements into a report |

## Verification

Review the flagship skill before install:

```bash
curl -sL https://raw.githubusercontent.com/tinyfish-io/tinyfish-cookbook/main/skills/use-tinyfish/SKILL.md | head -60
```

Read the install and getting-started notes:

```bash
curl -sL https://raw.githubusercontent.com/tinyfish-io/tinyfish-cookbook/main/INSTALL.md | head -40
```

Confirm the skill landed in the host's skill directory after install:

```bash
ls ~/.claude/skills 2>/dev/null || ls ~/.codex/skills
```

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| use-tinyfish | Pass | Warn | Warn |
| freelance-gig-finder | Pass | Pass | Warn |
| oss-alternatives | Pass | Pass | Warn |
| salary-market-scanner | Pass | Pass | Warn |
| project-idea-validator | Pass | Pass | Warn |
| npm-package-comparator | Pass | Warn | Warn |
| competitor-product-monitor | Warn | Pass | Warn |
| leetcode-coach | Pass | Pass | Warn |
| tech-stack-detective | Pass | Pass | Warn |
| self-improve-with-tinyfish | Pass | Pass | Warn |
| tinyfish-social-listening | Warn | Pass | Warn |
| interview-prep | Pass | Pass | Warn |
| dev-pain-finder | Pass | Pass | Warn |
| stalk-my-interviewer | Pass | Pass | Warn |
| kb-builder | Pass | Pass | Warn |
| job-market-intel | Pass | Pass | Warn |
| hackathon-finder | Pass | Pass | Warn |
| academic-research-mapper | Warn | Pass | Warn |
| tenders-finder | Pass | Warn | Warn |
| summer-school-finder | Pass | Pass | Warn |

The sample is warning-dense: Snyk Warns on all 20 sampled skills, Gen Agent Trust Hub Warns on competitor-product-monitor, tinyfish-social-listening and academic-research-mapper, and Socket Warns on use-tinyfish, npm-package-comparator and tenders-finder.

## Limitations

- Snapshot data, verified Nov 21, 2026: 4,510 combined installs across 26 indexed listings; 2,334 GitHub stars; MIT license; last pushed Nov 21, 2026. Counts drift over time.
- The install index and the tree drift in places: self-improve-with-tinyfish and tunneling carry install counts but have no directory in the current tree, and some directories use different names than their listings (competitor-product-monitor lives under `skills/competitor-update`, project-idea-validator under `skills/project-idea-validator-skill`, company-hiring-intelligence under `skills/company-hiring-intel`).
- Every one of the 20 sampled skills carries a Snyk Warn, and six more carry a Gen Agent Trust Hub or Socket Warn, so review each skill before relying on it unattended.
- The README ships a legal disclaimer: community contributions are provided "as is" with no warranty and no obligation to maintain, and users are responsible for vetting code before production use.
- The install index is dominated by a single flagship: use-tinyfish holds 3,621 of the 4,510 combined installs, so the long tail of career and research skills is lightly installed by comparison.

## Related

- [Firecrawl Agent - AI-Powered Structured Data Extraction Setup](/hermes/skills/catalog/firecrawl-agent-setup)
- [Browser-Use Automation - AI Browser for Anti-Bot Sites Setup](/hermes/skills/catalog/browser-use-automation-setup)
- [Tavily Search - Official LLM-Optimized Web Search CLI Setup](/hermes/skills/catalog/tavily-search-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with use-tinyfish: it teaches the agent when to reach for Search versus Fetch versus Agent versus Browser, which is the routing discipline every other skill in the repo leans on.
- Most recipe skills need the TinyFish CLI and an API key, so run `tinyfish auth login` after installing the CLI before invoking any of them.
- Search and Fetch are free with generous rate limits and no credit card, so wire those first and reserve the metered Agent and Browser endpoints for multi-step flows.
- Treat the career and research skills as templates: each runs parallel TinyFish agents over live sources, a pattern that is easy to adapt to a new vertical.
- Install one skill at a time with `npx skills add github.com/tinyfish-io/tinyfish-cookbook --skill <name>` instead of pulling the whole repository.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
