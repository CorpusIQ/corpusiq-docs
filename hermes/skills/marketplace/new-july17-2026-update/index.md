---
title: "July 17, 2026 (Evening Update) — Security, Apify Growth, Sentry Monitoring"
description: "7 additional Hermes-relevant skills discovered in evening sweep: addyosmani security-hardening (13.1K), Apify growth triad (18.7K combined), and Sentry AI monitoring suite (6K combined)."
---

# 🆕 July 17, 2026 — Evening Update: 7 Additional Skills

**Date:** July 17, 2026 (Evening sweep — supplement to [morning discovery](/hermes/skills/marketplace/new-july17-2026/))
**New Repos:** 3 | **New Skills:** 7 | **Combined Installs:** 37,800+

Evening sweep across 15 search terms on skills.sh surfaced 7 additional skills missed in this morning's 35-term sweep. The headline finds: **addyosmani/security-and-hardening** (13.1K, Addy Osmani of Google) — the first comprehensive security hardening guide designed for AI agents; **Apify's growth triad** (18.7K combined) — production lead gen, brand monitoring, and ultimate scraping; and **Sentry's AI monitoring suite** (6K combined) — error tracking purpose-built for agent deployments.

---

## New Skills at a Glance

| # | Skill | Installs | Category | Source |
|---|-------|:--------:|----------|--------|
| 1 | **security-and-hardening** | 13,100 | Security | addyosmani/agent-skills |
| 2 | **apify-ultimate-scraper** | 13,400 | Web Scraping | apify/agent-skills |
| 3 | **apify-lead-generation** | 2,800 | Growth | apify/agent-skills |
| 4 | **apify-brand-reputation-monitoring** | 2,500 | Growth | apify/agent-skills |
| 5 | **sentry-feature-setup** | 2,700 | Monitoring | getsentry/sentry-for-ai |
| 6 | **sentry-node-sdk** | 2,600 | Monitoring | getsentry/sentry-for-ai |
| 7 | **sentry-setup-ai-monitoring** | 616 | Monitoring | getsentry/sentry-agent-skills |

---

## Category Breakdown

### Security (1 skill)

#### security-and-hardening (13,100 installs) ⭐ Setup Guide Available
**Repo:** [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

Comprehensive security hardening guide for AI agent deployments from Addy Osmani (Engineering Lead, Google Chrome). Covers 12 hardening domains: prompt injection defense, tool call authorization, filesystem sandboxing, network egress controls, credential management, dependency auditing, telemetry minimization, and runtime integrity verification. The first security skill explicitly designed for the agent threat model — not retrofitted from web/server security patterns.

**Why it matters for Hermes:** Every Hermes deployment with tool access (terminal, browser, file system) needs hardening. This skill provides the threat-modeling framework and implementation patterns that the ClawSec suite (June 30) addresses from the OpenClaw side — together they form a complete agent security posture.

**Setup Guide:** [Security Hardening — Full Setup Guide](/hermes/skills/catalog/security-and-hardening-setup/)

```bash
npx skills add addyosmani/agent-skills@security-and-hardening
```

---

### Web Scraping & Growth — Apify Triad (3 skills)

The [apify/agent-skills](https://github.com/apify/agent-skills) repo (documented in the [July 16 sweep](/hermes/skills/marketplace/new-july16-2026/)) expanded with three new production-grade sub-skills for growth operations. Combined 18,700 installs across the triad.

#### apify-ultimate-scraper (13,400 installs)
The flagship Apify scraping skill. Handles any website — JS-rendered SPAs, infinite scroll, pagination, login-walled content. Built-in proxy rotation (residential + datacenter), CAPTCHA solving, and rate-limit evasion. Returns structured JSON with full CSS selector support. The go-to skill when simpler scrapers hit walls.

```bash
npx skills add apify/agent-skills@apify-ultimate-scraper
```

#### apify-lead-generation (2,800 installs) ⭐ Setup Guide Available
Automated lead discovery and enrichment. Scrapes business directories (Google Maps, Yelp, LinkedIn), extracts contact information, enriches with company size/funding/industry data, and outputs CRM-ready CSV/JSON. Domain-filtered targeting with built-in deduplication.

**Setup Guide:** [Apify Growth Skills — Full Setup Guide](/hermes/skills/catalog/apify-growth-skills-setup/)

```bash
npx skills add apify/agent-skills@apify-lead-generation
```

#### apify-brand-reputation-monitoring (2,500 installs)
Continuous brand monitoring across web, social, and review platforms. Tracks mentions, sentiment shifts, competitor comparisons, and review velocity. Configurable alert thresholds with Slack/email/webhook delivery. Essential for the "help-first community engagement" growth strategy — catch every mention before it goes unanswered.

```bash
npx skills add apify/agent-skills@apify-brand-reputation-monitoring
```

---

### Monitoring — Sentry AI Suite (3 skills)

Sentry, the industry-standard error tracking platform (4M+ developers), released a dedicated AI agent monitoring suite. Three skills covering setup, instrumentation, and dedicated agent monitoring — purpose-built for the unique failure modes of autonomous agents (infinite loops, tool timeouts, context corruption, credential rotation failures).

#### sentry-feature-setup (2,700 installs) ⭐ Setup Guide Available
Feature flag and release monitoring for agent deployments. Track which agent versions, model configurations, and skill combinations correlate with errors. Progressive rollout support — ship new skills to 10% of agent instances, monitor error rates, then expand.

**Setup Guide:** [Sentry AI Monitoring — Full Setup Guide](/hermes/skills/catalog/sentry-ai-monitoring-setup/)

```bash
npx skills add getsentry/sentry-for-ai@sentry-feature-setup
```

#### sentry-node-sdk (2,600 installs)
Sentry's Node.js SDK instrumented for agent runtimes. Auto-captures unhandled promise rejections, tool call failures, and MCP connection errors with full stack traces and agent context (current skill, tool chain, model, token usage). Drop-in replacement for generic error logging.

```bash
npx skills add getsentry/sentry-for-ai@sentry-node-sdk
```

#### sentry-setup-ai-monitoring (616 installs)
Purpose-built AI monitoring dashboard and alerting. Agent-specific metrics: tool call latency distributions, model response times, context window utilization, skill invocation counts, and error categorization by failure type. Ships with pre-built dashboards for common agent failure patterns.

```bash
npx skills add getsentry/sentry-agent-skills@sentry-setup-ai-monitoring
```

---

## Setup Guides Added

This sweep produced three new setup guides:
- **[Security Hardening Setup Guide](/hermes/skills/catalog/security-and-hardening-setup/)** — 12 hardening domains, threat model, implementation patterns
- **[Apify Growth Skills Setup Guide](/hermes/skills/catalog/apify-growth-skills-setup/)** — Lead gen, brand monitoring, ultimate scraper workflows
- **[Sentry AI Monitoring Setup Guide](/hermes/skills/catalog/sentry-ai-monitoring-setup/)** — Agent error tracking, dashboards, alerting

---

## Discovery Method

Evening supplement to the morning's 35-term sweep. 15 additional search terms queried: security, hardening, lead generation, brand monitoring, reputation, sentry, monitoring, error tracking, deploy, backup, API integration, social scheduling, desktop plugin, image generation, github actions.

85+ unique repos surfaced. Cross-referenced against 112 existing catalog entries and all 13 prior marketplace discovery pages (June 9 — July 17 morning, 2026). 7 new skills identified across 3 repos. All confirmed absent from prior sweeps via `grep -rl` across the full `hermes/skills/` directory.

---

*← [July 17 Morning](/hermes/skills/marketplace/new-july17-2026/) | [Marketplace Home](/hermes/skills/marketplace/) →*
*Powered by CorpusIQ*
