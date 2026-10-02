---
title: Tech Logos - Brand Logo Installer for shadcn/ui
description: "Install official, theme-aware tech brand logos (154 available) from the Elements shadcn registry. Covers AI providers, auth stacks, social platforms, and payment logos for Next.js + shadcn/ui projects. 100+ installs, 521-star registry."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tech-logos-setup/"
robots: "index,follow"
last_updated: "2026-08-25"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Tech Logos - Setup Guide

**Source:** [crafter-station/elements](https://github.com/crafter-station/elements) (521 ⭐)
**Skill:** `crafter-station/elements@tech-logos`
**Installs:** 100
**Category:** UI Development / shadcn Registry
**Quality Tier:** 🟢 Production (registry is a trusted shadcn directory entry)
**First Seen:** August 25, 2026

`tech-logos` is an agent playbook for installing official, theme-aware brand logos from the Elements registry - a full-stack shadcn/ui block library (auth, payments, AI components, and 154 tech brand logos). It triggers on logo/brand requests ("add a Clerk logo", "GitHub icon"), placeholder-logo detection, or when an agent builds landing pages, auth UIs, or integration showcases in a Next.js + shadcn/ui project. The skill files live in the repo's `.claude/skills/` directory (authored with Claude Code in mind), but the playbook is agent-agnostic: every action is a plain `npx shadcn` CLI command that any Hermes agent with terminal access can execute.

---

## Installation

```bash
# Install the skill playbook via skills.sh
npx skills add crafter-station/elements --skill tech-logos
```

The skill itself wraps the Elements shadcn registry - no plugin or API key is required. The underlying install primitive is the standard shadcn CLI:

```bash
# Add individual logos to a shadcn-initialized Next.js project
npx shadcn@latest add @elements/clerk-logo
npx shadcn@latest add @elements/github-logo
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js 18+** | Required by the shadcn CLI |
| **Next.js project with shadcn/ui** | Run `npx shadcn@latest init` first if `components.json` is missing |
| **Hermes Agent** | Terminal access; no version restriction |
| **Elements registry** | Trusted shadcn registry - listed in the [shadcn directory](https://ui.shadcn.com/docs/directory?q=elements); no manual config |

---

## Key Capabilities

### Core Features

| Capability | How to Trigger | Notes |
|---|---|---|
| Install single brand logo | "add a Stripe logo" → `npx shadcn@latest add @elements/stripe-logo` | Installs to `components/logos/{name}.tsx` |
| Install logo bundles | `@elements/logos`, `@elements/ai-services`, `@elements/social-media`, `@elements/package-managers` | All-logo and themed bundles |
| Theme-aware rendering | `mode="light"` / `mode="dark"`, `variant="icon"` / `variant="wordmark"` | Auto-detects theme when mode is omitted |
| Discover available logos | `ls registry/default/blocks/logos/` (in-repo) or browse [tryelements.dev/docs/logos](https://tryelements.dev/docs/logos) | 154 logos as of Aug 2026 |
| Request missing logo | Pre-filled GitHub issue URL: `https://github.com/crafter-station/elements/issues/new?title=[Logo%20Request]%20Add%20{Name}%20logo&labels=enhancement,logo-request` | Skill generates the full issue body |

### CLI Command Reference

```bash
# Auth stack
npx shadcn@latest add @elements/clerk-logo @elements/better-auth-logo

# AI provider logos
npx shadcn@latest add @elements/openai-logo @elements/anthropic-logo @elements/claude-logo

# Social footer
npx shadcn@latest add @elements/twitter-logo @elements/github-logo @elements/discord-logo

# Tech stack showcase
npx shadcn@latest add @elements/vercel-logo @elements/supabase-logo @elements/stripe-logo

# Usage in JSX (after install)
# <ClerkLogo className="h-8 w-auto" />
# <ClerkLogo variant="wordmark" mode="dark" />
```

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Brand walls on landing pages** | "Add a logo wall of our integrations to the hero section" → agent installs the relevant `@elements/*-logo` set and composes a themed wall |
| **AI provider showcases** | For demo apps or comparison pages (e.g., "OpenAI vs Anthropic"), install `@elements/ai-services` to render correct, current provider marks |
| **Partner integration pages** | For each partner connector (Stripe, Clerk, Supabase, Vercel), install that partner's logo with `variant="wordmark" mode="dark"` for dark-themed docs pages |
| **Tech-stack footers** | Standardize project/dashboard footers with package-manager and infra logos from one registry instead of hand-sourced SVGs |
| **UI prototypes in shadcn** | Any `pick-ui-library` → shadcn/ui selection: the agent can immediately add authentic brand assets rather than placeholder boxes |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| `Component X not found` on install | Verify the name against the registry: `ls registry/default/blocks/logos/ \| sed 's/-logo$//'` (in the repo) or browse tryelements.dev/docs/logos |
| `components.json` missing error | Run `npx shadcn@latest init` in the project root first |
| Logo doesn't respect dark mode | Pass `mode="dark"` (or `"light"`) explicitly, or omit `mode` to auto-detect theme |
| Need a logo that doesn't exist | Generate the pre-filled GitHub issue URL with the skill and file a `logo-request` - the skill formats title, body, and labels |
| Wrong variant rendered | Check the `variant` prop: `"icon"` (mark only) vs `"wordmark"` (mark + wordmark) |

## Verification

```bash
# After install, confirm the component file exists
ls components/logos/

# Functional import check (in a project component)
# import { StripeLogo } from "@/components/logos/stripe"
# <StripeLogo className="h-6 w-auto" mode="dark" />
```

---

*← [Skills Catalog](/hermes/skills/catalog) | [Elements Registry](https://tryelements.dev/docs/logos) →*
*Powered by CorpusIQ*
