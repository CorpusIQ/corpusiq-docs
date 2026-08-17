---
title: "Alireza Rezvani Claude Skills — 341 production"
description: Massive collection of 341+ skills across engineering (37 advanced), marketing, design, analytics, and agent workflows. 23.3K GitHub stars, 9K+ installs. Covers MCP servers, RAG, CI/CD, agent loops, SEO, A/B testing, and more.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/alirezarezvani-claude-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Alireza Rezvani Claude Skills — Setup Guide

**Source:** [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) (23,266⭐, 9,000+ combined installs)
**Category:** Engineering & Marketing
**Quality Tier:** 🟢 Production

One of the largest and most comprehensive skill collections on skills.sh — 341 skills spanning advanced engineering, marketing operations, design systems, analytics, and agent workflow automation. Originally built for Claude Code but compatible with any skills.sh-enabled agent (Hermes, Codex, OpenClaw, Cursor).

The engineering tier alone contains 37 "POWERFUL" skills covering agent design, RAG implementation, MCP server building, CI/CD pipelines, database design, observability, security auditing, changelog automation, and platform reliability engineering.

---

## Installation

Install the entire collection or cherry-pick categories:

```bash
# Full collection (341 skills)
npx skills add alirezarezvani/claude-skills

# Or install specific high-value skills:
npx skills add alirezarezvani/claude-skills --skill engineering-advanced-skills
npx skills add alirezarezvani/claude-skills --skill loop-library
npx skills add alirezarezvani/claude-skills --skill browser-automation
npx skills add alirezarezvani/claude-skills --skill marketing-ops
npx skills add alirezarezvani/claude-skills --skill self-improving-agent
```

---

## Skill Categories

### 🔧 Engineering (37 POWERFUL-tier skills)

| Skill | Installs | Purpose |
|---|---|---|
| **engineering-advanced-skills** | 2.0K | Index of 37 advanced skills: agent design, RAG, MCP, CI/CD, database, observability, security, SLO/chaos/reliability |
| **loop-library** | — | Discover, design, audit, and repair AI agent loops — triggers, actions, verification, guardrails, handoffs |
| **self-improving-agent** | 973 | Framework for agents that learn from their own execution history, refine strategies, and improve over time |
| **senior-backend** | 1.3K | Backend architecture patterns, API design, database optimization, caching strategies |
| **aws-solution-architect** | 1.5K | AWS Well-Architected patterns, cost optimization, multi-region deployment, serverless design |

### 📊 Marketing & Growth

| Skill | Installs | Purpose |
|---|---|---|
| **marketing-ops** | 671 | End-to-end marketing operations — campaign setup, tracking, attribution, budget management |
| **ab-test-setup** | — | Plan, design, and implement A/B tests with statistical rigor |
| **ad-creative** | — | Generate and iterate ad copy, headlines, and creative variations at scale |
| **aeo** | — | Answer Engine Optimization — optimize content to be cited by LLMs (ChatGPT, Perplexity, Claude) |
| **analytics-tracking** | — | GA4, GTM, event taxonomy, conversion tracking setup and audit |
| **app-store-optimization** | — | ASO toolkit for Apple App Store and Google Play — keyword research, metadata, ranking |
| **campaign-analytics** | — | Analyze marketing campaign performance across channels |

### 🎨 Design & Brand

| Skill | Installs | Purpose |
|---|---|---|
| **brand-guidelines** | — | Apply and enforce brand guidelines — colors, typography, logo, voice, tone |
| **promote** | 1.6K | Promotion and launch strategy for products and features |

### 🤖 Agent Infrastructure

| Skill | Installs | Purpose |
|---|---|---|
| **loop** | 1.5K | Create and manage repeatable agent workflows with bounded execution |
| **browser-automation** | 595 | Browser-based automation using Playwright — scraping, testing, form filling |
| **agentic-workflow-automation** | — | Multi-step agent workflows with conditional branching and error recovery |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **GitHub stars** | 23,266⭐ — actively maintained, MIT licensed |
| **Skills.sh** | `npx skills` CLI installed |
| **Python 3.10+** | Required for analytics, AEO, and data-processing skills |
| **Node.js 18+** | Required for browser-automation and some marketing tools |

---

## Quick Start

```bash
# Browse all available skills
npx skills add alirezarezvani/claude-skills --list

# Install the engineering index (recommended first step)
npx skills add alirezarezvani/claude-skills --skill engineering-advanced-skills

# Verify
npx skills list | grep alirezarezvani
```

---

## Verification

```bash
# Check installed skills from this publisher
npx skills list 2>&1 | grep -i "alirezarezvani\|claude-skills"

# Count total installed
npx skills list 2>&1 | grep -c "alirezarezvani"
```

---

## Notes

- **341 total skills** — the largest single-publisher collection on skills.sh. Install selectively by category rather than the full set
- **MIT licensed** — safe for commercial use and modification
- **Compatible agents**: Claude Code, Codex CLI, Hermes Agent, OpenClaw, Cursor, Gemini CLI
- The engineering tier (37 skills) is particularly strong for Hermes agents building MCP servers, RAG pipelines, and observability systems
- Marketing skills complement existing CorpusIQ catalog entries for copywriting, SEO, and content strategy
- Some skills have YAML frontmatter parse warnings on install — cosmetic only, skills function correctly
- The loop-library skill is uniquely suited for Hermes agent automation — it formalizes the trigger → action → verify → stop pattern that Hermes natively supports
