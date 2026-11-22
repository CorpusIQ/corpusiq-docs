---
title: "Agents Inc Skills - Atomic Skills Marketplace Setup"
description: "agents-inc/skills: official marketplace of 230+ atomic skills that compile Claude Code subagents - 6.7K combined installs across 96 indexed listings."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agents-inc-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-22"
tags: ["hermes skill", "agent skill", "skill setup", "skills marketplace", "claude code", "atomic skills"]
---

# Agents Inc Skills - Atomic Skills Marketplace Setup

**Source:** [agents-inc/skills](https://www.skills.sh/agents-inc/skills) via skills.sh - 6.7K combined installs across 96 indexed listings; first seen Nov 22, 2026 (Nov 22, 2026 morning sweep)
**GitHub:** [agents-inc/skills](https://github.com/agents-inc/skills) - 27 stars, MIT license, main branch, last pushed Oct 27, 2026; 238 skill directories under `src/skills/<domain>-<subcategory>-<name>/SKILL.md`, each with a metadata.yaml, reference.md and examples/, mirrored to a dist/plugins/ build output with .claude-plugin catalog.json and marketplace.json manifests.
**Category:** Agent Skills Marketplace and Claude Code Plugin
**Quality Tier:** 🟢 Green - MIT license, 27 stars and last pushed Oct 27, 2026; the 20 sampled skills carry no Fail cells, with a single Socket Warn on web-animation-view-transitions and Gen Agent Trust Hub clean across all 20.

Agents Inc is the publisher behind this repository, the official skills marketplace for its agent composition framework, which builds stacks and compiles specialized subagents for Claude Code. The repository ships 238 atomic skills under a domain-subcategory-name directory convention, and the README advertises 230+ skills spanning web, API, AI, infrastructure, desktop, mobile, CLI and meta domains. Each skill covers patterns, conventions, anti-patterns, edge cases and real code examples for a single technology, packaged as a SKILL.md plus a metadata.yaml, reference.md and examples directory.

The install index is far narrower than the tree: skills.sh carries 96 indexed listings combining to 6.7K installs, while the repository ships 238 skill directories, so over half the catalog has no install count yet. Install happens two ways, both documented in the README: as a Claude Code plugin marketplace, or through the agents-inc CLI.

## Installation

The README documents two install routes. Via Claude Code, add the marketplace and install a skill by name:

```
/plugin marketplace add agents-inc/skills
/plugin install <skill-name>@agents-inc
```

Or via the Agents Inc CLI, which chooses between plugin or eject mode scoped to a single project or the entire machine:

```bash
npx agents-inc init
```

The CLI route links out to the separate Agents Inc CLI repository. The README advises picking the skills that match your stack rather than installing the whole set, since the full marketplace spans 230+ technologies.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| web-forms-zod-validation | 171 | Zod schema validation patterns for TypeScript: schema definitions, type inference, refinements, transforms, discriminated unions |
| web-pwa-offline-first | 155 | Local-first architecture with sync queues for offline-capable PWAs |
| web-styling-cva | 148 | Type-safe component variant styling with cva(), compound variants and VariantProps |
| web-animation-framer-motion | 140 | Motion components, variants, AnimatePresence, gestures, layout and scroll-linked animations |
| web-tooling-vite | 125 | Vite config, path aliases, vendor chunk splitting and environment-specific builds |
| web-styling-tailwind | 124 | Tailwind CSS v4 utility-first styling with CSS-first configuration |
| web-pwa-service-workers | 118 | Service Worker lifecycle, caching strategies, offline patterns and update handling |
| web-routing-react-router | 112 | Client-side routing with data APIs: loaders, actions, error boundaries and nested layouts |
| web-animation-view-transitions | 108 | View Transitions API patterns for same-document and cross-document navigation |
| web-animation-css-animations | 106 | CSS transitions, keyframes, scroll-driven timelines and compositor-friendly properties |
| web-accessibility-web-accessibility | 106 | WCAG, ARIA and keyboard navigation patterns for accessible UI |
| web-testing-playwright-e2e | 105 | Playwright E2E patterns: Page Object Model, locator strategies, network mocking and visual regression |
| web-i18n-next-intl | 104 | Type-safe i18n for the App Router: locale routing, message rendering and static generation |
| web-framework-react | 104 | Component architecture, hooks and React 19 patterns |

The remaining 82 indexed listings range from 38 to 96 installs.

## Why This Matters for Hermes Agents

The suite's value is its atomicity: each skill isolates one technology with its patterns, conventions, anti-patterns, edge cases and code examples, so an agent loads only the skills that match the stack it is working on instead of one giant general-purpose prompt. The domain-subcategory-name naming convention makes skills discoverable and composable, and the same content ships in two layouts, source under src/skills/ and a built dist/plugins/ output with a .claude-plugin manifest, so it works both as a Claude Code plugin marketplace and as plain SKILL.md directories any agent can read. The repository also ships a skill-summoner agent that researches current best practices and writes new skills following the repo's own conventions, which is a useful pattern for keeping a catalog self-consistent. The realistic caveat for operators is adoption data: only 96 of the 238 shipped skills have install counts, and the counts concentrate in web skills while the API, AI, infrastructure, desktop, mobile and CLI domains sit in a long niche tail.

## Usage

| You say | What happens |
|---|---|
| Validate this form schema with Zod | Applies Zod schema definitions, type inference, refinements, transforms and discriminated unions |
| Make this app work offline | Applies local-first architecture with sync queues and Service Worker caching strategies |
| Style this component with variants | Applies cva() compound variants and VariantProps for type-safe variant styling |
| Animate this component | Chooses Motion components, variants, AnimatePresence and gestures for the interaction |
| Set up Vite for this project | Configures path aliases, vendor chunk splitting and environment-specific builds |
| Make this UI accessible | Applies WCAG, ARIA and keyboard navigation patterns |
| Write E2E tests with Playwright | Applies Page Object Model, locator strategies, network mocking and visual regression |

## Verification

Fetch the highest-count skill and read its routing before relying on it:

```bash
curl -sL https://raw.githubusercontent.com/agents-inc/skills/main/src/skills/web-forms-zod-validation/SKILL.md | head -40
```

Check the animation skill:

```bash
curl -sL https://raw.githubusercontent.com/agents-inc/skills/main/src/skills/web-animation-framer-motion/SKILL.md | head -40
```

Review the styling and E2E skills:

```bash
curl -sL https://raw.githubusercontent.com/agents-inc/skills/main/src/skills/web-styling-tailwind/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/agents-inc/skills/main/src/skills/web-testing-playwright-e2e/SKILL.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Nov 22, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| web-forms-zod-validation | Pass | Pass | Pass |
| web-pwa-offline-first | Pass | Pass | Pass |
| web-styling-cva | Pass | Pass | Pass |
| web-animation-framer-motion | Pass | Pass | Pass |
| web-tooling-vite | Pass | Pass | Pass |
| web-styling-tailwind | Pass | Pass | Pass |
| web-pwa-service-workers | Pass | Pass | Pass |
| web-routing-react-router | Pass | Pass | Pass |
| web-animation-view-transitions | Pass | Warn | Pass |
| web-animation-css-animations | Pass | Pass | Pass |
| web-accessibility-web-accessibility | Pass | Pass | Pass |
| web-testing-playwright-e2e | Pass | Pass | Pass |
| web-i18n-next-intl | Pass | Pass | Pass |
| web-framework-react | Pass | Pass | Pass |
| web-performance-web-performance | Pass | Pass | Pass |
| web-state-zustand | Pass | Pass | Pass |
| web-testing-vitest | Pass | Pass | Pass |
| web-ui-shadcn-ui | Pass | Pass | Pass |
| web-meta-framework-nextjs | Pass | Pass | Pass |
| api-performance-api-performance | Pass | Pass | Pass |

The 20 sampled skills carry no Fail cells: the only non-Pass is a Socket Warn on web-animation-view-transitions, and Gen Agent Trust Hub is clean across the whole sample. Only 20 of the 96 indexed listings have verdicts in this snapshot; the remaining 76 are unverified.

## Limitations

- Snapshot data, verified Nov 22, 2026: 6.7K combined installs across 96 indexed listings; 27 GitHub stars; MIT license; last pushed Oct 27, 2026. Counts drift over time.
- The install index is far narrower than the tree: 96 indexed listings against 238 skill directories, so over half the catalog has no install count yet.
- Only 20 of the 96 indexed listings carry skills.sh security verdicts in this snapshot; the remaining 76 are unverified.
- Install counts concentrate in web skills; the API, AI, infrastructure, desktop, mobile, CLI and meta skills sit in a long niche tail.
- The README advises picking the skills that match your stack; installing the whole marketplace spans 230+ technologies and adds real context overhead.

## Related

- [Tons of Skills - Agent Skills Marketplace Platform](/hermes/skills/catalog/tons-of-skills-marketplace-setup)
- [Claude Skills Marketplace - Engineering Workflow Setup](/hermes/skills/catalog/claude-skills-marketplace-setup)
- [Claude Plugin Marketplace - Azure and DevOps Packs](/hermes/skills/catalog/claude-plugin-marketplace-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by name with `/plugin install <skill-name>@agents-inc` rather than the whole marketplace; the README says to pick the skills that match your stack.
- Read the SKILL.md before relying on a skill; the Use For cells here condense each skill's full description.
- Use the src/skills/ path when reviewing; dist/plugins/ is the built output and mirrors the same content.
- The agents-inc CLI offers plugin or eject mode scoped to a project or the whole machine; pick eject mode to edit skill content directly.
- Re-check the security pages on skills.sh before production use, since only 20 of 96 listings have verdicts in this snapshot.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
