---
title: Vercel Agent Skills — Full Setup Guide for Hermes Agents
description: Install and use Vercel's official agent skills collection — 4 skills for optimization, React best practices, web design, and writing guidelines. 29K+ GitHub stars.
---

# Vercel Agent Skills — Setup Guide

**Source:** [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) (29,139⭐)
**Category:** Development / Quality
**Language:** JavaScript

Vercel's official collection of skills for AI coding agents. Four skills covering Vercel project optimization, React/Next.js best practices (40+ rules), web design guidelines (100+ rules), and writing guidelines (80+ rules). Follows the Agent Skills format.

---

## Installation

```bash
# Install all skills
npx skills add vercel-labs/agent-skills

# Or install individual skills
npx skills add vercel-labs/agent-skills --skill vercel-optimize
npx skills add vercel-labs/agent-skills --skill react-best-practices
npx skills add vercel-labs/agent-skills --skill web-design-guidelines
npx skills add vercel-labs/agent-skills --skill writing-guidelines
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Vercel account** | Required for `vercel-optimize` skill only |
| **Vercel API token** | Set as `VERCEL_TOKEN` env var for optimization skill |
| **Hermes Agent** | Any version — skills load as markdown instructions |

---

## Key Capabilities

### Available Skills

| Skill | What It Does | Use When |
|---|---|---|
| **vercel-optimize** | Audits Vercel project for cost, performance, caching, function usage | Reducing Vercel bills, investigating slow routes, optimizing deployments |
| **react-best-practices** | 40+ React/Next.js rules across 8 categories | Writing new components, code review, bundle optimization |
| **web-design-guidelines** | 100+ UI rules covering accessibility, performance, UX | "Review my UI", accessibility audits, design reviews |
| **writing-guidelines** | 80+ writing rules covering voice, structure, typography | "Review my docs", content audits, style checks |

### react-best-practices Categories

| Category | Priority | Focus |
|---|---|---|
| Eliminating waterfalls | Critical | Data fetching patterns |
| Bundle size optimization | Critical | Tree shaking, dynamic imports |
| Server-side performance | High | Caching, streaming |
| Client-side data fetching | Medium-High | SWR, React Query patterns |
| Re-render optimization | Medium | Memoization, state placement |
| Rendering performance | Medium | Virtualization, CSS containment |
| JavaScript micro-optimizations | Low-Medium | Loop patterns, object reuse |

### web-design-guidelines Categories

Accessibility (aria-labels, semantic HTML, keyboard handlers), Focus States, Forms, Animation (prefers-reduced-motion), Typography, Images, Performance (virtualization, layout thrashing), Navigation & State, Dark Mode & Theming, Touch & Interaction, Locale & i18n.

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Vercel cost optimization** | Run `vercel-optimize` on corpusiq-docs deployment to find billing savings |
| **Code review automation** | Use `react-best-practices` when reviewing PRs for corpusiq-docs frontend |
| **UI accessibility audits** | Run `web-design-guidelines` on landing pages to catch a11y issues before launch |
| **Content quality checks** | Use `writing-guidelines` on blog posts, docs pages, and marketing copy |
| **Onboarding new agents** | Install all skills to give new Hermes agents production-grade development instincts |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| **vercel-optimize fails** | Ensure `VERCEL_TOKEN` env var is set with team scope |
| **Skill not found** | Verify install: `npx skills list` — should show `vercel-labs/agent-skills` |
| **Rules conflict with project conventions** | Skills are advisory — override specific rules in project config |

## Verification

```bash
# Verify skill installed
npx skills list | grep vercel-labs

# Verify Vercel token (for optimize skill)
npx vercel whoami

# Quick test — check web design guidelines load
ls $(npx skills list --json 2>/dev/null | python3 -c "import json,sys; d=json.load(sys.stdin); print([s['path'] for s in d if 'web-design' in s.get('name','')][0])" 2>/dev/null)
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Discovery Page](/hermes/skills/marketplace/new-july16-2026/) →*
*Powered by CorpusIQ*
