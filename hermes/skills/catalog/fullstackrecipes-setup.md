---
title: "Full Stack Recipes - Full-Stack Web & AI App Setup Guide"
description: "andrelandgraf/fullstackrecipes: a Shadcn registry of production-ready full-stack web and AI app recipes - 13.2K combined installs across 77 listings."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/fullstackrecipes-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "fullstack development", "nextjs", "shadcn", "ai apps"]
---

# Full Stack Recipes - Setup Guide

**Source:** [andrelandgraf/fullstackrecipes](https://www.skills.sh/andrelandgraf/fullstackrecipes) via skills.sh - 13.2K combined installs across 77 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 morning sweep)
**GitHub:** [andrelandgraf/fullstackrecipes](https://github.com/andrelandgraf/fullstackrecipes) - 23 stars, no LICENSE file, main branch, last pushed Jun 8, 2026. Skills live under `skills/` and `.agents/skills/`, recipes as Markdown under `docs/recipes/`, and a Shadcn registry in `registry.json`.
**Category:** Full-Stack AI App Development
**Quality Tier:** 🔵 Community - 3 Gen Agent Trust Hub Fails (ralph-loop, skill-creator, nextjs-on-vercel) and 13 Snyk Warns among 20 sampled verdicts; Socket clean (20 Pass); no LICENSE file.

fullstackrecipes is a Shadcn registry and collection of complete step-by-step guides (recipes) for building full-stack web apps and agentic applications. It encodes one canonical assembled stack - Next.js, Shadcn and AI Elements for UI, the Workflow Development Kit and AI SDK v6 for agents, Drizzle for data, Bun for tooling, and Vercel Fluid Compute plus Neon Serverless Postgres for hosting - as atomic recipes an agent can follow instead of inventing configuration. Every page on fullstackrecipes.com has a Markdown twin, so a recipe can be fetched with plain curl and no special tooling.

The 77 indexed listings span three kinds of content: setup recipes (one-time configuration guides for auth, databases and payments), skills (day-to-day patterns installed through the skills CLI), and cookbooks (ordered two-phase setups that run their recipes then install the matching skills). The top listing ralph-loop and the ralph-loop-workflow skill are two listings for the one workflow, an autonomous coding loop driven by a /ralph command, and ralph-setup (104 installs) is a third alias for the same loop.

## Installation

The README ships no install commands; the install mechanics live in the recipes and the use-fullstackrecipes meta-skill. Recipes are fetched as Markdown, and skills are installed through the skills CLI.

```bash
# list every recipe and cookbook with its slug
curl https://fullstackrecipes.com/llms.txt

# fetch one recipe as Markdown (append .md to any page URL)
curl https://fullstackrecipes.com/recipes/neon-drizzle-setup.md

# install a skill so the agent retains the patterns for ongoing work
bunx skills add andrelandgraf/fullstackrecipes/skills -s ralph-loop-workflow
```

Setup recipes are one-time configuration guides; skills assume the canonical stack is already configured and are installed rather than pasted as content.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ralph-loop | 3,475 | Autonomous coding loop via a /ralph command; the recipe counterpart to ralph-loop-workflow below |
| ralph-loop-workflow | 684 | Run a coding agent in an autonomous loop, gated by a preflight check that every CLI is installed, linked and authenticated |
| observability-monitoring | 315 | Observability and monitoring: structured logging, error tracking and web analytics |
| stripe-subscriptions | 269 | Stripe subscription billing: checkout, feature-flag plan gating, webhooks and billing portal |
| og-image-generation | 250 | Dynamic social preview images with Next.js file conventions and next/og, cached at build time |
| shiki-code-blocks | 247 | Syntax-highlight code blocks with Shiki; server-side rendering in RSC and light/dark theme switching |
| use-fullstackrecipes | 240 | Meta-skill: discover and follow recipes by fetching their Markdown; use when planning a build or choosing a recipe |
| agent-browser | 237 | Browser automation for navigation, form filling, screenshots and data extraction |
| better-auth-setup | 200 | Base email/password auth with Better Auth, Drizzle ORM and Neon Postgres |
| better-auth-protected-routes | 196 | Server-side route protection to enforce auth on specific pages while keeping others public |
| better-auth-components | 195 | Auth UI components and pages: sign in, sign up, forgot/reset password and email verification |
| better-auth-profile | 192 | Account settings page: profile editing, password change, email update, session management and account deletion |
| better-auth-emails | 192 | Email verification, password reset and account-management emails via Resend |
| vercel-react-best-practices | 186 | React and Next.js performance optimization guidelines from Vercel Engineering |
| skill-creator | 181 | Guide for creating and updating skills with specialized knowledge and workflows |
| better-auth-best-practices | 179 | Better Auth integration guidance for the TypeScript authentication framework |
| nextjs-on-vercel | 164 | Create a Next.js app and add Next.js and Vercel MCP servers for deploy and debugging |
| ai-chat | 156 | Complete AI chat app: database persistence, chat-list management and automatic title generation |
| pino-logging-setup | 153 | Structured JSON logging with Pino and pino-pretty, configurable via LOG_LEVEL |

The remaining 58 indexed listings range from 1 to 135 installs: using-drizzle-queries (135), authentication (132), neon-drizzle-setup and ai-agent-workflow (128 each), then a long tail down to user-stories and recipes (5), fallow (4) and code-health-setup (1).

## Why This Matters for Hermes Agents

Full-stack builders stall when they have to assemble a modern stack from memory: the exact Next.js flags, the Drizzle schema, the Better Auth callbacks, the Stripe webhook signature. This suite encodes that whole stack as tested, re-fetchable recipes, so an agent applies a vetted sequence of steps instead of hallucinating configuration. The meta-skill use-fullstackrecipes makes the corpus machine-readable: an agent can list every recipe with one curl and then pull the exact one it needs, with no MCP server required. The Ralph loop shows the intended end state, an agent that plans, builds, tests and ships autonomously, gated by a preflight check that every CLI is installed, linked and authenticated before it runs. The better-auth family covers a complete authentication surface from base setup through routes, components, profile and emails, which is the part of most apps where half-baked agent output is most dangerous. Recipes are versioned with their libraries and meant to be re-fetched, so the guidance ages with the ecosystem rather than freezing at a snapshot. The only paid services are the ones the app itself uses (Stripe, Resend, Sentry, Vercel, Neon); the recipes themselves are free to fetch.

## Usage

| You say | What happens |
|---|---|
| Add email/password auth to my Next.js app | The better-auth-setup recipe wires Better Auth with Drizzle and Neon, then the components, emails and profile skills fill in the UI |
| Set up Stripe subscriptions with plan gating | The stripe-subscriptions recipe adds checkout, webhooks, feature flags and the billing portal |
| Add syntax-highlighted code blocks | The shiki-code-blocks skill adds Shiki with server-side rendering and theme switching |
| Generate social share images for my blog | The og-image-generation skill builds dynamic preview images with next/og |
| Run a coding agent autonomously on this repo | The ralph-loop-workflow skill drives the /ralph loop after a preflight check of every CLI |
| Where do I even start? | The use-fullstackrecipes meta-skill fetches the index and the relevant recipe Markdown |

## Verification

```bash
# confirm the fetched index lists the recipes you need
curl https://fullstackrecipes.com/llms.txt
# review a skill before installing it
curl -sL https://raw.githubusercontent.com/andrelandgraf/fullstackrecipes/main/skills/use-fullstackrecipes/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ralph-loop | Fail | Pass | Warn |
| ralph-loop-workflow | Pass | Pass | Pass |
| observability-monitoring | Warn | Pass | Pass |
| stripe-subscriptions | Warn | Pass | Warn |
| og-image-generation | Pass | Pass | Warn |
| shiki-code-blocks | Pass | Pass | Warn |
| use-fullstackrecipes | Pass | Pass | Warn |
| agent-browser | Pass | Pass | Warn |
| better-auth-setup | Pass | Pass | Warn |
| better-auth-protected-routes | Pass | Pass | Warn |
| better-auth-components | Pass | Pass | Warn |
| better-auth-profile | Pass | Pass | Warn |
| better-auth-emails | Pass | Pass | Warn |
| vercel-react-best-practices | Pass | Pass | Pass |
| skill-creator | Fail | Pass | Pass |
| better-auth-best-practices | Pass | Pass | Pass |
| nextjs-on-vercel | Fail | Pass | Warn |
| ai-chat | Warn | Pass | Warn |
| pino-logging-setup | Warn | Pass | Pass |
| using-drizzle-queries | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 20, 2026: 13,242 combined installs across 77 indexed listings; 23 GitHub stars; no LICENSE file; last pushed Jun 8, 2026. Counts drift over time.
- The top listing ralph-loop and the ralph-loop-workflow skill are two listings for the one Ralph-loop workflow, and ralph-setup (104 installs) is a third alias for it; ralph-loop has no SKILL.md in the current tree, its recipe is served from fullstackrecipes.com.
- Several listings map to recipe Markdown in `docs/recipes/` (nextjs-on-vercel, pino-logging-setup) while others are served only from the live site (stripe-subscriptions, ai-chat, observability-monitoring); the index and the tree do not line up one-to-one.
- Only 20 of 77 listings carry skills.sh security verdicts; the other 57 are unverified on that platform.
- The README is a stack summary only, so install commands must be read from the recipes and the use-fullstackrecipes meta-skill rather than the README.

## Related

- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Vercel Agent Skills - Official Vercel Collection Setup](/hermes/skills/catalog/vercel-agent-skills-setup)
- [Vercel AI SDK Skills - TypeScript AI Development Setup](/hermes/skills/catalog/vercel-ai-skills-setup)
- [Better Auth Skills - Authentication Infrastructure Setup](/hermes/skills/catalog/better-auth-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the meta-skill: curl the llms.txt index before a build so you know every recipe and cookbook that exists.
- Follow recipes exactly and complete the Prerequisites in order, finishing a setup recipe before its matching skill.
- Install skills with `bunx skills add andrelandgraf/fullstackrecipes/skills -s <skill>` rather than just reading the Markdown.
- Re-fetch the .md when troubleshooting or starting a feature; recipes evolve with their libraries.
- Before an autonomous run, run the Ralph preflight once and stop until every CLI is installed, linked and authenticated.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
