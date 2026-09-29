---
title: "Jezweb Skills - 96-Skill Web Dev & Design Suite Setup"
description: "Setup guide for jezweb/claude-skills - 96 agent skills across Cloudflare, Tailwind v4, shadcn/ui, TanStack, WordPress, Shopify, SEO and business English. 115K+ combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/jezweb-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-28"
tags: ["hermes skill", "agent skill", "skill setup", "tailwind", "cloudflare", "wordpress", "shopify", "seo"]
---

# Jezweb Skills - Setup Guide

**Source:** [jezweb/claude-skills](https://github.com/jezweb/claude-skills) (1,034⭐, pushed Sep 26, 2026)
**Skill:** `jezweb/claude-skills` (96 installable skills, 115,071 combined installs)
**Publisher:** Jeremy Dawes / [Jezweb](https://jezweb.com.au) (Australian web agency)
**Category:** Web Development / Design / SEO / Business Writing
**Quality Tier:** 🔵 Community (no skills.sh security verdicts published - verified Sep 28, 2026)

Jezweb ships 96 workflow skills organized as 10 Claude Code plugins, each "producing tangible output" - from scaffolding Cloudflare Workers and Hono APIs to generating favicon packages, Elementor builds, Shopify product content, and business English rewrites. Skills are Agent Skills-spec compatible and installable through any host that reads SKILL.md directories, including Hermes Agent via `npx skills add`.

---

## Installation

```bash
# Full suite
npx skills add jezweb/claude-skills

# Single skill
npx skills add jezweb/claude-skills --skill shadcn-ui
```

Alternatively install the Claude Code plugin set (each plugin bundles its skills):

```bash
# From the marketplace (in Claude Code):
/plugin marketplace add jezweb/claude-skills
/plugin install web-design@jezweb-skills
```

## Plugin / Category Layout

| Plugin | Skills | Focus |
|---|---|---|
| frontend | 15+ | Tailwind v4 theming, shadcn/ui, TanStack (Query/Start/Router/Table), React patterns, Zustand, motion, Next.js, landing pages |
| cloudflare | 12+ | Workers, Hono APIs, D1/Drizzle schemas + migrations, R2, Vite+Workers starters, TanStack Start SSR |
| web-design | 2 | Local business SEO setup (JSON-LD, meta, robots.txt, sitemap) |
| design-assets | 8+ | Colour palettes, favicon packages, SVG icon sets, image processing |
| wordpress | 6+ | Elementor, WP setup, content, plugin core |
| shopify | 4+ | Store setup, products, content |
| dev-tools | 12+ | Project health, team updates, GitHub releases, UX audits, git workflows, browser automation, brains trust |
| writing | 8+ | Business English (US/UK/AUS/NZ), proposals, resumes, strategy docs, deep research |
| integrations | 8+ | Google Chat, Apps Script, ElevenLabs agents, MCP server building, Stripe, parcel tracking |
| social-media | 2+ | Social media posts, walkthrough videos |

## Roster - Top Skills

| Skill | Installs | Does |
|---|---|---|
| shadcn-ui | 3,541 | shadcn/ui component scaffolding and theming |
| tailwind-theme-builder | 3,146 | Build complete Tailwind v4 theme systems |
| color-palette | 3,145 | Generate cohesive brand colour palettes |
| wordpress-elementor | 2,742 | Elementor page builds and layouts |
| tailwind-v4-shadcn | 2,716 | Tailwind v4 + shadcn/ui combined workflows |
| ux-audit | 2,668 | Structured UX audit of an interface |
| tanstack-query | 2,607 | TanStack Query data fetching patterns |
| tanstack-start | 2,523 | TanStack Start full-stack SSR apps |
| image-processing | 2,319 | Resize, convert, optimise images |
| favicon-gen | 2,161 | Complete favicon package generation |
| fastapi | 1,976 | FastAPI backend scaffolding |
| google-apps-script | 1,877 | Google Apps Script automation |
| seo-local-business | 1,754 | Local business SEO: JSON-LD, meta, sitemap |
| responsiveness-check | 1,719 | Responsive layout testing |
| d1-drizzle-schema | 1,710 | Cloudflare D1 + Drizzle schema design |
| wordpress-content | 1,609 | WordPress content production |
| project-health | 1,547 | Project health and permission management |
| mcp-builder | 1,370 | Build MCP servers |
| social-media-posts | 1,350 | Platform-specific social post drafting |
| deep-research | 1,134 | Structured deep research workflow |

(96 skills total - full roster on the [skills.sh listing](https://skills.sh/jezweb/claude-skills).)

**Roster reconciliation (Sep 28 evening sweep):** skills.sh still lists `web-design-patterns` (473 installs) under `jezweb/claude-skills` — a pre-rename index entry. The skill ships today as `seo-local-business` (1,755 installs) inside the `web-design` plugin; no `web-design-patterns` SKILL.md exists in `main`. Searches for the old name resolve to `seo-local-business`.


## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Landing pages & docs site** | `tailwind-theme-builder`, `landing-page`, and `design-system` for marketing pages and the docs theme |
| **SEO/AEO for corpusiq.io** | `seo-local-business` and `seo-meta` produce JSON-LD + meta; pairs with CorpusIQ's AEO/FAQ pipeline |
| **Client web work** | `wordpress-elementor`, `shopify-products`, and `cloudflare-worker-builder` cover common client stacks |
| **Visual assets** | `favicon-gen`, `color-palette`, `icon-set-generator`, and `image-processing` for on-brand asset production |
| **Business writing** | `us-business-english` and `proposal-writer` align with CorpusIQ email/response standards |

## Limitations / Verification

- Published for Claude Code plugins first; individual skills are Agent Skills-spec SKILL.md files, so Hermes installs work via `npx skills add`
- 96 skills is a lot to install wholesale - install per-category
- Verify: `npx skills add jezweb/claude-skills --list` shows 96 skills

## Security

No skills.sh security audits published (verified Sep 28, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [TanStack Skills Setup](/docs/hermes/skills/catalog/tanstack-skills-setup)
- [Frontend God Mode Setup](/docs/hermes/skills/catalog/frontend-god-mode-setup)
- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Skills Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
