---
title: "WeCom Unified Skill — WeChat Work Routing Suite Setup"
description: "wecomteam/wecom-unified — 1 skill, 4.4K installs: the official intent-routing layer that maps natural language to correct WeCom CLI business domains before any command runs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/wecom-unified-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-18"
tags: ["hermes skill", "agent skill", "skill setup", "wecom", "wechat work", "routing", "enterprise"]
---

# WeCom Unified Skill — Setup Guide

**Source:** [wecomteam/wecom-unified](https://skills.sh/wecomteam/wecom-unified)
**GitHub:** [wecomteam/wecom-unified](https://github.com/wecomteam/wecom-unified)
**Skills:** 1 skill · 4.4K total installs
**Category:** Enterprise Productivity
**First Seen:** catalogued August 18, 2026 sweep (on skills.sh since April 22, 2026)
**Quality Tier:** 🟡 Trusted — official WeCom team org; Gen Agent Trust Hub Warn and Snyk Warn (both named), Socket Pass

The official WeCom Unified skill is the intent-routing layer for the wecom-cli suite. It maps a natural-language request to the correct business domain, loads that domain's reference file, and constructs the exact wecom-cli command from the documented parameter spec. Its core rule forbids guessing parameters from the routing table or from model memory, which makes it the guardrail layer for the whole 153.4K-install WeCom ecosystem.

---

## Installation

```bash
npx skills add wecomteam/wecom-unified
```

Explicit single-skill form:

```bash
npx skills add https://github.com/wecomteam/wecom-unified --skill wecom-unified
```

## Prerequisites

| Requirement | Details |
|---|---|
| **wecom-cli CLI** | `npm install -g @wecom/cli`, version 1.1.0 or higher (`wecom-cli --version` check is the skill's mandatory pre-flight) |
| **Node.js + npx** | For the skill installer and CLI runtime |
| **wecom-cli skills** | The routing targets — install `wecomteam/wecom-cli` for the domains this skill routes to |

## What It Provides

| Capability | Details |
|---|---|
| **Business-domain routing table** | Judges intent against the WeCom domain map before any command runs |
| **Reference-driven command construction** | Loads the per-domain reference file and builds commands from documented parameter specs |
| **Version pre-check** | Blocks operation if `wecom-cli --version` is missing or below 1.1.0, and reports the error instead of failing silently |
| **No-guessing enforcement** | Explicitly forbids constructing parameters from the routing table description or from model memory |

The unified skill and the per-domain wecom-cli skills are complementary: unified decides where to route and enforces the pre-checks, while the 28 domain skills carry the actual command specifications.

## Quick Start

1. Install the CLI: `npm install -g @wecom/cli`, verify 1.1.0+
2. Install: `npx skills add wecomteam/wecom-unified`
3. Install the domain skills: `npx skills add wecomteam/wecom-cli`
4. Ask in natural language; the routing table resolves the domain and the reference files drive exact commands

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Guardrailed WeCom automation** | The no-guessing rule matches our verification-before-assertion discipline for agent actions |
| **Domain routing** | Reusable pattern for intent-to-tool mapping in enterprise assistant design |
| **APAC operations** | Safe entry point for WeChat Work automation before touching the full domain suite |

## Limitations / Verification

- Security audits: Gen Agent Trust Hub Warn, Snyk Warn (both named in the tier), Socket Pass
- Publisher-page total verified (4.4K, single skill); 59 GitHub stars as of the sweep
- Single-skill cluster — it is the router for wecom-cli, not a standalone capability set
- SKILL.md is maintained in Chinese by the WeCom team
- Install count below the 20K guide bar; drafted on official-vendor brand authority plus its role as the guardrail for the 153.4K wecom-cli suite

```bash
npx skills add wecomteam/wecom-unified   # verify install works
```

## Related

- [WeCom CLI Skills — Enterprise WeChat Agent Suite Setup](/hermes/skills/catalog/wecom-cli-skills-setup/)
- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
