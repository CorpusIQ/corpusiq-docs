---
title: "Inertia Rails Skills - Inertia.js for Rails Setup"
description: "inertia-rails/skills: 4.5K combined installs across 11 listings, the Inertia.js workflow for Rails: setup, pages, controllers, forms, typing and shadcn."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/inertia-rails-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "inertia.js", "rails", "react"]
---

# Inertia Rails Skills - Setup Guide

**Source:** [inertia-rails/skills](https://www.skills.sh/inertia-rails/skills) via skills.sh - 4.5K combined installs across 11 indexed listings; first seen Nov 14, 2026 (Nov 14 evening sweep)
**GitHub:** 71 stars, MIT license, `main` branch, last pushed 2026-09-01, 11 `SKILL.md` files under `skills/`
**Category:** Rails with Inertia.js, React, Vue 3 and Svelte
**Quality Tier:** 🟢 Green - both sampled skills pass all three auditors.

This is an anti-pattern collection rather than a tutorial. The README opens with the problem in plain terms: training data contains outdated or wrong patterns for the Rails and Inertia.js stack, so the skills exist to correct specific mistakes. Each skill maps to one of them.

The table of corrections is worth reading on its own because it names exactly what an agent gets wrong here: `redirect_to` for an external URL where `inertia_location(url)` belongs, third-party form libraries where Inertia's `<Form>` component or `useForm` hook is the idiomatic path, legacy `PageProps extends SharedProps` typing instead of `InertiaConfig` module augmentation, and Next.js patterns such as `use client` leaking into a Vite-based Inertia app.

## Installation

Install the skills with the skills CLI:

```bash
npx skills add inertia-rails/skills
```

The documented stack is Rails 8 or later with inertia-rails 3.17 or later, React 19 with `@inertiajs/react` 2.3 or later, Vue 3.5 or later with `@inertiajs/vue3`, or Svelte 5 with `@inertiajs/svelte`, all in TypeScript. The setup skill detects which of those you have and generates a `CLAUDE.md` describing the configuration it found.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| inertia-rails-architecture | 548 | The mental model, decision matrices and anti-pattern detection for the whole stack. |
| inertia-rails-pages | 512 | Page components, layouts, navigation and client-side APIs, with React inline and Vue and Svelte references. |
| inertia-rails-controllers | 499 | Rails controller patterns for Inertia responses. |
| inertia-rails-forms | 494 | Form handling with the `<Form>` component and the `useForm` hook. |
| inertia-rails-typescript | 476 | `InertiaConfig` module augmentation for shared props, flash and error typing. |
| inertia-rails-testing | 473 | RSpec and Minitest matchers for Inertia responses. |
| shadcn-inertia | 436 | shadcn/ui patterns adapted for Inertia and React rather than Next.js. |
| inertia-rails-setup | 426 | Detecting the stack, offering the recommended dependencies and generating `CLAUDE.md`. |
| alba-inertia | 383 | Alba serializer patterns with Typelizer-generated types. |
| shadcn-vue-inertia | 118 | shadcn-vue patterns adapted for Inertia with Vue 3. |
| shadcn-svelte-inertia | 96 | shadcn-svelte patterns adapted for Inertia with Svelte 5. |

All 11 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

Inertia sits between a server framework and a client framework, and most of the mistakes happen at that seam. An agent that has seen thousands of Next.js applications will reach for client-side data fetching or a form library, and both are wrong in an Inertia app where the server sends props and the adapter owns navigation.

The corrections are stated as replacements, which is the easiest form for an agent to apply: the wrong pattern, the right one, and the reason. That is more reliable than a principle, because it can be matched against the code in front of it.

The testing skill is the underrated one. Inertia responses have their own assertion surface, and a Rails test that checks the wrong thing passes while the page does not render. Giving an agent the right matchers means its tests actually verify the response.

## Usage

| You say | What happens |
|---|---|
| "Set up Inertia for this Rails app" | Detects the stack, proposes the dependency set and writes the `CLAUDE.md` configuration. |
| "This controller redirects to Stripe but the page breaks" | Replaces `redirect_to` with `inertia_location(url)` for the external URL. |
| "Add a form for creating invoices" | Uses the `<Form>` component or `useForm` instead of a third-party form library. |
| "Type the shared props properly" | Applies `InertiaConfig` module augmentation instead of extending `SharedProps`. |
| "Write a request spec for this page" | Uses the RSpec or Minitest matchers for Inertia responses. |
| "Add a shadcn component to this page" | Uses the Inertia-adapted shadcn skill rather than the Next.js default. |

## Verification

Read the architecture skill and the setup skill before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/inertia-rails/skills/main/skills/inertia-rails-architecture/SKILL.md | head -20
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/inertia-rails/skills/main/skills/inertia-rails-setup/SKILL.md
```

Skills sit at `skills/<name>/SKILL.md`, and the setup skill is the one that inspects your project rather than asserting conventions.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| inertia-rails-architecture | Pass | Pass | Pass |
| inertia-rails-pages | Pass | Pass | Pass |

The repository is Markdown skills under an MIT licence, with no install scripts or binaries.

## Limitations

- Snapshot data, verified 2026-11-14: 4,461 combined installs across 11 indexed listings; 71 GitHub stars; MIT; last pushed 2026-09-01. Counts drift over time.
- The stack floor is high: Rails 8 or later, inertia-rails 3.17 or later, and React 19, Vue 3.5 or Svelte 5. Older applications are outside its assumptions.
- Content is React-inline with Vue and Svelte kept in reference files, so Vue and Svelte users get less detail per skill.
- The plugin targets Claude Code and its `CLAUDE.md` output; other hosts read the skills but do not get the generated configuration file automatically.
- The repository is a month and a half past its last push, so inertia-rails releases after September 2026 may not be reflected.

## Related

- [WordPress Agent Skills - Official WP Development Setup](/hermes/skills/catalog/wordpress-agent-skills-setup)
- [Qodo Skills - Code Review and Standards Suite](/hermes/skills/catalog/qodo-skills-setup)
- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the setup skill first; the generated `CLAUDE.md` tells later sessions which stack they are in.
- Ask the agent to name the adapter version before changing forms or navigation: the patterns differ between 2.x releases.
- Keep third-party form libraries out of Inertia pages, even when the agent suggests them confidently.
- Use the shadcn skill that matches your client framework; the React skill will not produce Vue or Svelte components.
- Treat `inertia_location` as the only way out of an Inertia request to an external URL.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
