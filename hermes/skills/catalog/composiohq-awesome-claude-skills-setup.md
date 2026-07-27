---
title: Composio — Awesome Claude Skills (28-Skill Suite for Hermes Agents)
description: Production-ready Claude Skills collection with 28 skills for lead research, invoice management, content creation, YouTube downloading, developer analytics, and more. 70.9K GitHub stars, 16.1K+ combined installs on skills.sh.
---

# Composio — Awesome Claude Skills Setup Guide

**Source:** [composiohq/awesome-claude-skills](https://skills.sh/composiohq/awesome-claude-skills) (16.1K+ combined installs)
**GitHub:** [composiohq/awesome-claude-skills](https://github.com/composiohq/awesome-claude-skills) (70,938 ⭐)
**Category:** Agent Tools / Multi-Utility
**Quality Tier:** 🟢 Production

A curated collection of 28 Claude Skills from Composio — the integration platform for AI agents. These skills span business operations (lead research, invoicing, content creation), developer tools (MCP builder, changelog generator, skill creator), creative work (canvas design, Slack GIFs, artifacts builder), and growth (competitive ads extraction, Twitter algorithm optimization). Each skill is self-contained and can be installed individually.

---

## Installation

```bash
# Install individual skills as needed:
npx skills add composiohq/awesome-claude-skills --skill lead-research-assistant
npx skills add composiohq/awesome-claude-skills --skill invoice-organizer
npx skills add composiohq/awesome-claude-skills --skill developer-growth-analysis
npx skills add composiohq/awesome-claude-skills --skill youtube-downloader
npx skills add composiohq/awesome-claude-skills --skill content-research-writer
npx skills add composiohq/awesome-claude-skills --skill competitive-ads-extractor
npx skills add composiohq/awesome-claude-skills --skill changelog-generator
npx skills add composiohq/awesome-claude-skills --skill mcp-builder
npx skills add composiohq/awesome-claude-skills --skill skill-creator
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **lead-research-assistant** | 4.2K | Research and qualify leads with company data |
| **invoice-organizer** | 3.9K | Organize and manage invoices, expenses |
| **developer-growth-analysis** | 3.3K | Analyze developer growth metrics and patterns |
| **youtube-downloader** | 4.7K | Download YouTube videos for offline analysis |
| **content-research-writer** | — | Research and write content with citations |
| **competitive-ads-extractor** | — | Extract competitor ads from Facebook/LinkedIn ad libraries |
| **changelog-generator** | — | Auto-generate user-facing changelogs from git commits |
| **mcp-builder** | — | Build MCP (Model Context Protocol) servers |
| **skill-creator** | — | Create and publish new Claude Skills |
| **artifacts-builder** | — | Build multi-component HTML artifacts (React, Tailwind, shadcn/ui) |
| **brand-guidelines** | — | Apply Anthropic brand colors and typography |
| **canvas-design** | — | Create visual art, posters, designs as PNG/PDF |
| **connect** | — | Connect to external services and APIs |
| **connect-apps** | — | Integrate with third-party applications |
| **domain-name-brainstormer** | — | Generate and evaluate domain name ideas |
| **file-organizer** | — | Organize and categorize files automatically |
| **image-enhancer** | — | Enhance and upscale images |
| **internal-comms** | — | Draft internal company communications |
| **langsmith-fetch** | — | Fetch data from LangSmith for LLM observability |
| **meeting-insights-analyzer** | — | Extract insights from meeting transcripts |
| **raffle-winner-picker** | — | Fair random winner selection for giveaways |
| **skill-share** | — | Share and distribute skills across teams |
| **slack-gif-creator** | — | Create custom GIFs for Slack |
| **tailored-resume-generator** | — | Generate tailored resumes for job applications |
| **template-skill** | — | Starter template for building new skills |
| **theme-factory** | — | Generate and apply visual themes |
| **twitter-algorithm-optimizer** | — | Optimize content for X/Twitter algorithm |
| **webapp-testing** | — | Test web applications end-to-end |

---

## Key Capabilities

### Lead Research & Business Operations
- **lead-research-assistant**: Qualify inbound leads with company research, technographics, and scoring
- **invoice-organizer**: Parse, categorize, and track invoices across formats
- **competitive-ads-extractor**: Pull competitor ad creatives from Facebook/LinkedIn ad libraries for campaign inspiration

### Developer & Engineering
- **changelog-generator**: Transform git commits into polished, customer-facing release notes
- **developer-growth-analysis**: Track and analyze developer growth metrics for PLG products
- **mcp-builder**: Scaffold MCP servers with tool definitions and transports
- **webapp-testing**: End-to-end testing of web applications with Playwright

### Content & Creative
- **content-research-writer**: Research topics and produce cited, publication-ready content
- **youtube-downloader**: Download YouTube videos with metadata extraction
- **canvas-design**: Generate posters, designs, and visual art programmatically
- **slack-gif-creator**: Create custom animated GIFs for team communication

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | 18+ (for `npx skills`) |
| **API Keys** | Some skills require external API access (LangSmith, Slack, Twitter) |
| **Git** | For changelog-generator (reads git history) |

---

## Quick Start

```bash
# 1. Install the most popular skills
npx skills add composiohq/awesome-claude-skills --skill lead-research-assistant
npx skills add composiohq/awesome-claude-skills --skill youtube-downloader

# 2. Use in Hermes — these skills auto-load when their trigger conditions match
# Example: "Research this lead for me" triggers lead-research-assistant
# Example: "Download this YouTube video" triggers youtube-downloader

# 3. List installed skills to verify
npx skills list | grep composiohq
```

---

## Verification

```bash
# Check skills are installed
npx skills list | grep -E "lead-research|youtube-downloader|invoice-organizer"

# Test a skill — ask Hermes a relevant question to trigger it
# "Research this company as a potential lead: stripe.com"
```

---

## Notes

- 28 skills total — install only what you need. Each skill is self-contained.
- GitHub repo is a curated list, not a monorepo — skills reference external tools and APIs
- The **lead-research-assistant** and **competitive-ads-extractor** are particularly valuable for growth operations
- **webapp-testing** overlaps with Anthropic's official webapp-testing skill (121.9K installs) — prefer the official one unless you need Composio-specific integration features
- Most skills require API keys for external services (LangSmith, Slack, Twitter) — configure before first use
