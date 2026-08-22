---
title: "Agentic Awesome Skills (AAS) — 2,000+ Skill Catalog Setup"
description: "sickn33/agentic-awesome-skills — 45,000-star community skill catalog (2,025 skills) with 37 newly catalogued engineering playbooks at 100 to 13,215 installs each: Node.js, TypeScript, Next.js, security, testing, architecture, and more. Platform-agnostic SKILL.md playbooks load natively in Hermes Agent."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agentic-awesome-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-21"
tags: ["hermes skill", "agent skill", "skill setup", "engineering", "development"]
---

# Agentic Awesome Skills (AAS) — Setup Guide

**Source:** [sickn33/agentic-awesome-skills](https://skills.sh/sickn33/agentic-awesome-skills)
**GitHub:** [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) (45,000+⭐, MIT)
**Catalog size:** 2,025 skills (registry v15.16.0)
**Newly catalogued:** 37 engineering playbooks, ~130,000 combined installs
**Category:** Development & Engineering
**First Seen:** August 21, 2026 sweep
**Quality Tier:** 🟢 Production

Agentic Awesome Skills (AAS) is one of the largest community skill catalogs on skills.sh. It distributes plain SKILL.md playbooks plus a local MCP control plane called AAS Core. This guide covers the 37 generic engineering playbooks that were verified as uncatalogued in the August 21 sweep: each is a standalone SKILL.md file with standard frontmatter (name, description, metadata) and no platform binding, so they load natively in Hermes Agent like any other skill.

**Compatibility note:** AAS Core (the MCP stack-composition tool) and the repo's direct `npx agentic-awesome-skills` installer target Codex and Claude first. Neither is required for the playbooks documented here. Hermes users install the playbooks through the skills.sh CLI or by copying individual SKILL.md files.

---

## Overview

| Skill | Installs | Domain |
|---|---|---|
| `nodejs-best-practices` | 13,215 | JavaScript/TypeScript |
| `typescript-expert` | 11,576 | JavaScript/TypeScript |
| `clean-code` | 10,483 | JavaScript/TypeScript |
| `api-security-best-practices` | 8,377 | Security |
| `nextjs-best-practices` | 6,929 | Web/Frontend |
| `nextjs-supabase-auth` | 6,219 | Web/Frontend |
| `3d-web-experience` | 4,315 | Web/Frontend |
| `prisma-expert` | 4,027 | Backend/Architecture |
| `playwright-skill` | 3,729 | Testing |
| `game-development` | 3,589 | AI/Product/Ops |
| `software-architecture` | 3,459 | Backend/Architecture |
| `mobile-design` | 3,358 | Web/Frontend |
| `product-manager-toolkit` | 3,327 | AI/Product/Ops |
| `ui-ux-designer` | 2,754 | Web/Frontend |
| `i18n-localization` | 2,712 | Web/Frontend |
| `web-performance-optimization` | 2,692 | Web/Frontend |
| `bun-development` | 2,665 | JavaScript/TypeScript |
| `powershell-windows` | 2,452 | AI/Product/Ops |
| `nestjs-expert` | 2,391 | Backend/Architecture |
| `senior-architect` | 2,093 | Backend/Architecture |
| `api-documentation-generator` | 2,069 | Backend/Architecture |
| `database-design` | 1,955 | Backend/Architecture |
| `senior-fullstack` | 1,895 | Backend/Architecture |
| `agent-memory-systems` | 1,856 | AI/Product/Ops |
| `cc-skill-security-review` | 1,856 | Security |
| `youtube-summarizer` | 1,826 | AI/Product/Ops |
| `scroll-experience` | 1,805 | Web/Frontend |
| `bash-scripting` | 1,773 | JavaScript/TypeScript |
| `bullmq-specialist` | 1,767 | Backend/Architecture |
| `bash-linux` | 1,701 | JavaScript/TypeScript |
| `vercel-deployment` | 1,684 | Backend/Architecture |
| `react-nextjs-development` | 1,680 | Web/Frontend |
| `backend-dev-guidelines` | 1,657 | Backend/Architecture |
| `browser-extension-builder` | 1,654 | Web/Frontend |
| `discord-bot-architect` | 1,506 | AI/Product/Ops |
| `documentation-templates` | 1,502 | AI/Product/Ops |
| `backend-architect` | 1,499 | Backend/Architecture |

**Not included:** `antigravity-workflows` (876 installs) is Antigravity-IDE specific and excluded under the existing house rule for `antigravity-*` skills. `agent-self-scheduling` (18) and `mercury-mcp` (8) sit below the 100-install cataloguing bar and remain watchlisted.

---

## Installation

Install the full catalog via the skills.sh CLI:

```bash
npx skills add sickn33/agentic-awesome-skills
```

Install individual skills by copying the playbook into your Hermes skills directory (same layout as the repo):

```bash
mkdir -p ~/.hermes/skills/aas
curl -sL https://raw.githubusercontent.com/sickn33/agentic-awesome-skills/main/skills/nodejs-best-practices/SKILL.md \
  -o ~/.hermes/skills/aas/nodejs-best-practices/SKILL.md
```

The repo's own direct installer (`npx agentic-awesome-skills`) targets Codex, Claude, Gemini CLI, and other IDEs. Hermes users should use the two paths above. AAS Core (the local stdio MCP for catalog search and stack composition) is optional, read-only, and Codex/Claude-first.

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Any version with skills directory support (`~/.hermes/skills/`) |
| **Node.js 18+** | Only for the `npx skills` CLI path |
| **No API keys** | The playbooks are knowledge and decision guides; they use tools you already have configured |
| **Network (optional)** | Only needed for `npx skills` fetch or raw.githubusercontent.com downloads |

## Key Capabilities

### JavaScript & TypeScript Engineering

`nodejs-best-practices` and `typescript-expert` teach framework selection, async patterns, and type-system decision making rather than fixed code snippets. `clean-code` applies the same discipline across languages. `bun-development`, `bash-scripting`, and `bash-linux` cover the adjacent runtime and shell tooling.

### Web & Frontend

`nextjs-best-practices` and `react-nextjs-development` cover framework decisions; `nextjs-supabase-auth` handles the full auth stack; `web-performance-optimization`, `scroll-experience`, and `3d-web-experience` target UX quality; `ui-ux-designer` and `mobile-design` carry design-system constraints; `i18n-localization` and `browser-extension-builder` round out the surface.

### Backend & Architecture

`software-architecture`, `senior-architect`, and `backend-architect` provide decision frameworks for system design. `prisma-expert`, `nestjs-expert`, and `bullmq-specialist` go deep on specific stacks. `database-design`, `api-documentation-generator`, and `vercel-deployment` cover data modeling, API surfaces, and shipping.

### Security & Testing

`api-security-best-practices` is a checklist-driven security review for API surfaces. `cc-skill-security-review` audits skills before install, a useful gate for the catalog itself. `playwright-skill` covers browser test automation.

### AI, Product & Ops

`agent-memory-systems` covers memory architecture choices for agents, `product-manager-toolkit` brings PM discipline to spec work, and `discord-bot-architect`, `documentation-templates`, `youtube-summarizer`, `game-development`, and `powershell-windows` fill specialized operational gaps.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Docs quality** | Use `clean-code` and `typescript-expert` as review lenses when auditing Hermes ecosystem repos and MCP server code |
| **Security reviews** | Use `api-security-best-practices` when vetting third-party MCP servers before cataloguing |
| **Skill vetting** | Use `cc-skill-security-review` as an additional gate for new skills.sh publisher content |
| **Agent architecture** | Use `agent-memory-systems` to inform GBrain/Honcho memory design discussions |
| **Product specs** | Use `product-manager-toolkit` and `software-architecture` when drafting feature specs for CorpusIQ product work |

## Limitations / Verification

- AAS Core MCP and the `npx agentic-awesome-skills` installer are Codex/Claude-first; they are not part of the Hermes install path
- `antigravity-*` skills are Antigravity-IDE specific and excluded
- Install counts are from skills.sh as of the August 21, 2026 sweep

```bash
# Verify skills installed
ls ~/.hermes/skills/aas/

# Verify the skills.sh listing
npx skills find "nodejs-best-practices" --json 2>&1 | grep skills.sh
```

## Security

- [sickn33/agentic-awesome-skills repo](https://github.com/sickn33/agentic-awesome-skills) — review SKILL.md files before install (standard practice)
- [Hermes skills security](/hermes/best-practices/security/) — skill trust guidance
- `cc-skill-security-review` in this catalog audits skills before activation

## Related

- [M. Collina Node Skills — Fastify & Node.js Agent Suite Setup](/hermes/skills/catalog/mcollina-node-skills-setup/) — Node.js-focused suite from the Fastify author
- [design-review — Visual UI Audit & Fix Setup](/hermes/skills/catalog/design-review-setup/) — complementary UI review skill
- [Skills Catalog](/hermes/skills/catalog/) — full catalog index

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
