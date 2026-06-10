---
title: June 11, 2026 Discoveries
description: 38 new high-value skills discovered across 5 new repositories. Hermes agent ecosystem, platform integrations, and communication bots.
---

# June 11, 2026 — New Skills Discoveries

Automated discovery sweep found **38 new high-value skills** across **5 previously uncatalogued repositories**. All with direct relevance to Hermes agents — from the `aradotso/hermes-skills` ecosystem (20 skills) to platform communication bots (10 skills), new Nous Research variants (2 skills), and standalone community contributions.

*Previously cataloged: coreyhaines31/marketingskills, nousresearch/hermes-agent, vercel-labs/agent-browser, vercel-labs/agent-skills, anthropics/skills, xixu-me/skills, browser-use/skills, mcp-use/mcp-use, github/awesome-copilot, obra/superpowers, apify/agent-skills, wshobson/agents, googleworkspace/cli, firecrawl/cli, and others.*

---

## aradotso/hermes-skills — 20 skills (2,656 total installs)

The definitive community Hermes agent skill collection. Covers agent evolution, UI frameworks, desktop companions, mission control, observability, and multi-agent orchestration.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `aradotso/hermes-skills@hermes-webui-agent` | 193 | Web-based UI for Hermes agent interaction |
| `aradotso/hermes-skills@hermes-agent-self-evolution` | 186 | Self-improvement loops for Hermes agents |
| `aradotso/hermes-skills@hermes-agent-framework` | 164 | Base framework for building Hermes agents |
| `aradotso/hermes-skills@awesome-hermes-agent-ecosystem` | 160 | Curated ecosystem map of Hermes tools/skills |
| `aradotso/hermes-skills@hermes-workspace-ai-agent-ui` | 155 | Workspace UI for AI agent management |
| `aradotso/hermes-skills@hermes-desktop-companion` | 152 | Desktop companion app for Hermes |
| `aradotso/hermes-skills@hermes-web-ui-dashboard` | 150 | Dashboard UI for Hermes monitoring |
| `aradotso/hermes-skills@hermes-atlas-ecosystem-map` | 138 | Ecosystem visualization and mapping |
| `aradotso/hermes-skills@hermes-desktop-os1-native-macos-client` | 137 | Native macOS client for Hermes |
| `aradotso/hermes-skills@hermes-agent-mission-control` | 137 | Central mission control for agent coordination |
| `aradotso/hermes-skills@oh-my-hermes-workflow` | 134 | Opinionated Hermes workflow presets |
| `aradotso/hermes-skills@hermes-hudui-consciousness-monitor` | 132 | Agent consciousness/state monitoring |
| `aradotso/hermes-skills@minions-hermes-mission-control` | 129 | Minions workers + Hermes coordination |
| `aradotso/hermes-skills@runbookhermes-aiops-agent` | 128 | AIOps runbook automation for Hermes |
| `aradotso/hermes-skills@hermes-paperclip-adapter` | 109 | Paperclip plugin adapter for Hermes |
| `aradotso/hermes-skills@hermesclaw-wechat-multi-agent` | 106 | WeChat multi-agent via OpenClaw + Hermes |
| `aradotso/hermes-skills@hermes-agent-control-room` | 100 | Agent control room / operations center |
| `aradotso/hermes-skills@hermes-swift-mac-app` | 95 | Native Swift macOS app for Hermes |
| `aradotso/hermes-skills@hermes-agent-optimization` | 93 | Agent performance optimization toolkit |
| `aradotso/hermes-skills@hermes-labyrinth-observability` | 101 | Labyrinth observability framework |

**Setup:**

```bash
npx skills add aradotso/hermes-skills@hermes-agent-self-evolution
npx skills add aradotso/hermes-skills@hermes-agent-framework
npx skills add aradotso/hermes-skills@oh-my-hermes-workflow
# Skills auto-register with Hermes after install.
# Some require API keys (Paperclip, OpenClaw) — see individual skill docs.
```

---

## membranedev/application-skills — 10 skills (13.7K total installs)

Turn Hermes agents into interactive bots on 10 major platforms. Each skill wraps a platform's API into a ready-to-use agent toolset.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `membranedev/application-skills@google-drive` | 2.2K | Google Drive file operations from Hermes |
| `membranedev/application-skills@confluence` | 1.4K | Atlassian Confluence wiki integration |
| `membranedev/application-skills@microsoft-sharepoint` | 1.3K | SharePoint document management |
| `membranedev/application-skills@salesforce` | 1.3K | Salesforce CRM from Hermes |
| `membranedev/application-skills@box` | 1.2K | Box cloud storage operations |
| `membranedev/application-skills@dropbox` | 1.2K | Dropbox file management |
| `membranedev/application-skills@shopify` | 204 | Shopify store operations |
| `membranedev/application-skills@airtable` | 217 | Airtable database operations |
| `membranedev/application-skills@telegram` | 153 | Telegram bot integration |
| `membranedev/application-skills@discord` | 132 | Discord bot integration |

**Setup:**

```bash
npx skills add membranedev/application-skills@telegram
npx skills add membranedev/application-skills@discord
npx skills add membranedev/application-skills@shopify
# Each skill requires platform OAuth. Run the auth flow after install.
# Telegram: Bot Token from @BotFather
# Discord: Bot Token from Discord Developer Portal
# Shopify: Store API key + admin access token
```

---

## nousresearch/hermes-agent — 2 new variants (283 total installs)

New official Hermes agent variants from Nous Research.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `nousresearch/hermes-agent@arxiv` | 152 | ArXiv paper discovery and research via Hermes |
| `nousresearch/hermes-agent@claude-code` | 131 | Claude Code integration for Hermes coding |

**Setup:**

```bash
npx skills add nousresearch/hermes-agent@arxiv
npx skills add nousresearch/hermes-agent@claude-code
# arxiv: No API key needed. Searches arxiv.org directly.
# claude-code: Requires Anthropic API key and Claude Code CLI.
```

---

## aradotso/trending-skills — 1 skill (135 installs)

| Skill | Installs | Use Case |
|-------|----------|----------|
| `aradotso/trending-skills@hermes-labyrinth-observability` | 135 | Alternative observability framework (also in hermes-skills) |

**Setup:**

```bash
npx skills add aradotso/trending-skills@hermes-labyrinth-observability
```

---

## Community Standalone — 5 skills (352 total installs)

Independent community contributions with Hermes integration.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `dandacompany/hermes-skill@hermes` | 51 | General Hermes skill wrapper from D&DA Company |
| `chujianyun/skills@hermes-ops` | 46 | Hermes operations and DevOps toolkit |
| `skills.volces.com@hermes-agent` | 27 | ByteDance/Volces Hermes agent integration |
| `affaan-m/everything-claude-code@hermes-imports` | 1.9K | Claude Code → Hermes skill importer |
| `ar9av/obsidian-wiki@hermes-history-ingest` | 1.6K | Obsidian wiki history → Hermes ingest |

**Setup:**

```bash
npx skills add dandacompany/hermes-skill@hermes
npx skills add chujianyun/skills@hermes-ops
npx skills add affaan-m/everything-claude-code@hermes-imports
npx skills add ar9av/obsidian-wiki@hermes-history-ingest
```

---

## Summary

| Repository | Skills | Total Installs | Category |
|-----------|--------|----------------|----------|
| aradotso/hermes-skills | 20 | 2,656 | Hermes Ecosystem |
| membranedev/application-skills | 10 | 13,739 | Platform Bots |
| nousresearch/hermes-agent | 2 | 283 | Official Variants |
| aradotso/trending-skills | 1 | 135 | Observability |
| Community Standalone | 5 | 3,674 | Mixed |
| **Total** | **38** | **20,487** | — |

**Catalog update:** Added to `hermes/skills/catalog/index.md` under Hermes Ecosystem (20) and Platform Bots (10) sections. Hermes Variants section updated with 2 new entries.

---

*← [June 10 Discoveries](/hermes/skills/marketplace/new-june10-2026/) | [Skills Catalog](/hermes/skills/catalog/) →*
*↑ [Marketplace Home](/hermes/skills/marketplace/)*
