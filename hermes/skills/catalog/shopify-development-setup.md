---
title: "Shopify Development - Full Setup Guide for Hermes Agents"
description: "sickn33/agentic-awesome-skills - shopify-development, 1,812 installs from the 45,000-star AAS catalog. Platform-agnostic playbook for building Shopify apps, checkout/admin/POS UI extensions, and Liquid themes - GraphQL Admin API, Shopify CLI, Polaris UI, Shopify Functions, validated GraphQL templates, and Python scaffolding scripts."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/shopify-development-setup/"
robots: "index,follow"
last_updated: "2026-09-08"
tags: ["hermes skill", "agent skill", "skill setup", "shopify", "ecommerce", "development"]
---

# Shopify Development - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/sickn33/agentic-awesome-skills/shopify-development) (1,812 installs)
**GitHub:** [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) (45,000+⭐, MIT)
**Category:** Development / E-Commerce
**First Seen:** Sep 8, 2026 sweep (uncatalogued high-install skill from the partially-covered AAS cluster)
**Quality Tier:** 🟢 Production (Gen Agent Trust Hub Pass / Socket Pass / Snyk Pass)

A routing playbook for building on the Shopify platform: apps (OAuth, GraphQL Admin API, webhooks, billing), UI extensions (checkout, admin, POS with Polaris components), and themes (Liquid templating, sections, snippets). It ships GraphQL templates validated against the Shopify Admin API 2026-01 schema via the official Shopify MCP, Python scaffolding scripts, and per-path reference docs. It comes from Agentic Awesome Skills (AAS), one of the largest community skill catalogs on skills.sh, but sits outside the 37-skill roster in the AAS cluster setup guide, so it gets its own guide here.

**Compatibility note:** in the repo the skill lives under `plugins/agentic-awesome-skills-claude/` (a Claude Code packaging directory), but the SKILL.md itself is standard Agent Skills format with no platform binding - it loads natively in Hermes Agent like any other skill.

---

## Installation

Selective install via the skills.sh CLI:

```bash
npx skills add sickn33/agentic-awesome-skills --skill shopify-development
```

Manual install (proven path - keeps the bundle intact, mirrors the repo layout):

```bash
mkdir -p ~/.hermes/skills/shopify-development/references ~/.hermes/skills/shopify-development/scripts
BASE=https://raw.githubusercontent.com/sickn33/agentic-awesome-skills/main/plugins/agentic-awesome-skills-claude/skills/shopify-development
curl -sL "$BASE/SKILL.md" -o ~/.hermes/skills/shopify-development/SKILL.md
curl -sL "$BASE/references/app-development.md" -o ~/.hermes/skills/shopify-development/references/app-development.md
curl -sL "$BASE/references/extensions.md" -o ~/.hermes/skills/shopify-development/references/extensions.md
curl -sL "$BASE/references/themes.md" -o ~/.hermes/skills/shopify-development/references/themes.md
curl -sL "$BASE/scripts/shopify_init.py" -o ~/.hermes/skills/shopify-development/scripts/shopify_init.py
curl -sL "$BASE/scripts/shopify_graphql.py" -o ~/.hermes/skills/shopify-development/scripts/shopify_graphql.py
```

Full-catalog install (all 2,025 skills - heavy; see the AAS cluster guide):

```bash
npx skills add sickn33/agentic-awesome-skills
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Any version with skills directory support (`~/.hermes/skills/`) |
| **Shopify CLI** | `npm install -g @shopify/cli@latest` - required for app, extension, and theme workflows |
| **Shopify Partner account** | Required for app development (OAuth app creation, app distribution) |
| **Dev store** | Free development store for testing apps, extensions, and themes |
| **Node.js 18+** | For the Shopify CLI and the `npx skills` path |
| **Python 3** | For the bundled scripts (`shopify_init.py` scaffolding, `shopify_graphql.py` GraphQL utilities) |

## Key Capabilities

| Capability | How It Works |
|---|---|
| **App development** | OAuth, GraphQL Admin API, REST, webhooks, and billing integration, with routing guidance in `references/app-development.md` |
| **UI extensions** | Checkout UI, admin actions/blocks, and POS extensions built with Polaris components |
| **Theme development** | Liquid templating, sections, and snippets for storefront customization |
| **Shopify Functions** | Custom discount, payment, and delivery rules that execute server-side |
| **Validated GraphQL** | Every template query/mutation validated against the Shopify Admin API 2026-01 schema via the official Shopify MCP |
| **Scaffolding scripts** | `shopify_init.py` (interactive project scaffolding) and `shopify_graphql.py` (GraphQL utilities and templates) |

## Quick Start

1. Install the Shopify CLI and the skill (above)
2. Scaffold: `shopify app init` (or `shopify theme init` for theme-only work)
3. Describe the goal to the agent - the skill's routing section decides app vs extension vs theme, including combined App + Theme Extension builds
4. Pull specifics from the matching reference file (OAuth/webhooks/billing for apps, extension types for UI work, Liquid architecture for themes)
5. Develop with `shopify app dev` (tunneled dev server) and ship with `shopify app deploy`

```bash
# Generate extension scaffolding
shopify app generate extension --type checkout_ui_extension
shopify app generate extension --type admin_action
shopify app generate extension --type admin_block
shopify app generate extension --type pos_ui_extension

# GraphQL utilities from the skill dir
python3 scripts/shopify_graphql.py
```

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Shopify connector roadmap** | CorpusIQ's Shopify connector covers store data; this skill gives the agent working knowledge of the app/extension side of the platform for connector planning and debugging |
| **E-commerce operator support** | Answer merchant questions with working knowledge of custom app, checkout, and theme development paths - the core CorpusIQ ICP |
| **Feature prototyping** | Prototype checkout extensions or Shopify Functions to validate operator-facing product ideas before committing engineering time |
| **Demo content** | Build working Shopify app/theme demos for outreach and onboarding material |
| **Competitive intelligence** | Evaluate Shopify app ecosystem moves and merchant tooling to sharpen positioning |

## Limitations / Verification

- **Path quirk:** the repo stores this skill under `plugins/agentic-awesome-skills-claude/` (Claude Code packaging), but the SKILL.md is platform-agnostic Agent Skills format - use the raw-URL paths above, not the AAS cluster guide's `skills/<name>/` paths
- **Slow listing:** `npx skills add sickn33/agentic-awesome-skills --list` on the full 2,025-skill repo is slow; use the skills.sh product page as the fast reference
- **Schema pin:** GraphQL templates are validated against Admin API 2026-01; re-validate against newer API versions if a query errors
- **Full-catalog install pulls 2,025 skills** - prefer selective or manual install

```bash
# Verify skill installed
ls ~/.hermes/skills/shopify-development/SKILL.md

# Verify Shopify CLI
shopify version
```

## Security

All three skills.sh security audits pass (verified Sep 8, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Pass |
| Socket | Pass |
| Snyk | Pass |

## Related

- [Agentic Awesome Skills (AAS) - 2,000+ Skill Catalog Setup](/hermes/skills/catalog/agentic-awesome-skills-setup)
- [Shopify Skills (official Shopify AI Toolkit)](/hermes/skills/catalog/shopify)
- [Nexscope E-Commerce Skills - Shopify, Etsy, TikTok Shop Setup](/hermes/skills/catalog/nexscope-ecommerce-skills-setup)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
