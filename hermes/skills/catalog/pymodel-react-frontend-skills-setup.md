---
title: "React Frontend Skills - PyModel Suite Setup"
description: "pymodel/react-frontend-skills: 10.5K combined installs across 18 listings; production-grade React, Next.js, TypeScript and testing skills for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pymodel-react-frontend-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "react", "nextjs", "frontend"]
---

# React Frontend Skills - Setup Guide

**Source:** [pymodel/react-frontend-skills](https://www.skills.sh/pymodel/react-frontend-skills) via skills.sh - 10.5K combined installs across 18 indexed listings; first seen Nov 18, 2026 (Nov 18, 2026 evening sweep)
**GitHub:** 43 stars, MIT licence, `main` branch, last pushed 2026-11-09. Each skill is a `SKILL.md` folder under `skills/` that indexes `references/` or `rules/` files.
**Category:** React and frontend engineering
**Quality Tier:** 🟠 Orange - 4 Snyk Fails among 12 sampled verdicts (typescript, nextjs, vitest, shadcn); MIT licence.

React Frontend Skills is a collection of 18 production-grade skills for the React ecosystem, by PyModel. Dropped into a coding assistant, they apply current patterns for React 19, Next.js 16, TypeScript 7, Tailwind CSS v4, Vitest, Playwright, MSW, TanStack Query, Zod, React Hook Form, and nuqs.

Each skill is a portable SKILL.md folder that indexes detailed references/ or rules/ files loaded only when a task needs them, so they work across Claude Code, Codex, Cursor, and other agents. A zero-dependency companion CLI handles the deterministic step: checking that the project is on the versions the skills target.

## Installation

One command installs everything and auto-detects the agents on your machine:

```bash
npx skills add PyModel/react-frontend-skills --all
```

Pick specific skills, or install at the user level:

```bash
npx skills add PyModel/react-frontend-skills -s react,nextjs,tailwind
npx skills add PyModel/react-frontend-skills --all -g
```

The set is also published to npm with a sync step:

```bash
npm install @pymodel/react-frontend-skills
npx skills experimental_sync
```

Target one agent with `-a`, and check your project's versions with the companion CLI:

```bash
npx skills add PyModel/react-frontend-skills -a claude-code -s '*' -y
npx -y @pymodel/react-frontend-skills detect
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| react | 669 | React 19 components and hooks. |
| tailwind | 653 | Tailwind CSS v4 styling and configuration. |
| typescript | 637 | TypeScript 7 types and tsconfig. |
| ui-design | 636 | Accessible, responsive frontend UI and UX design. |
| playwright | 606 | Playwright end-to-end tests and flaky-test fixes. |
| nextjs | 606 | Next.js 16 App Router caching and routing. |
| vitest | 595 | Vitest 5 unit tests and mocking. |
| feature-arch | 594 | Feature-based React folder structure and module boundaries. |
| zod | 582 | Zod 4 schema validation and type inference. |
| shadcn | 582 | shadcn/ui components on Radix or Base UI. |
| react-hook-form | 578 | React Hook Form 7 forms and validation. |
| tanstack-query | 570 | TanStack Query v5 data fetching and caching. |
| vercel-react-best-practices | 560 | React and Next.js performance optimization. |
| web-design-guidelines | 552 | Review UI code against Web Interface Guidelines. |
| tdd | 533 | Test-driven development with red-green-refactor. |
| msw | 526 | MSW 3 API mocking for tests. |
| vercel-composition-patterns | 523 | React component API design with compound components. |
| nuqs | 504 | nuqs type-safe URL search-param state. |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

For a frontend agent, the default failure mode is code that compiles but does not follow current library semantics: stale React patterns, wrong caching in Next.js, hand-rolled state where TanStack Query fits. These skills pin the current major of each library and index reference files that load only when a task needs them, so the agent applies the 2026 pattern instead of what it remembered.

For Hermes agents, the most transferable pieces are the review and architecture skills: feature-arch's module boundaries, web-design-guidelines' review pass, and the test disciplines of vitest, playwright, msw, and tdd. The version check CLI gives a deterministic guard before relying on any of the skills, which is rare among skill collections.

## Usage

| You say | What happens |
|---|---|
| "Build this form with validation" | react-hook-form applies the current React Hook Form 7 patterns and Zod-based validation. |
| "Set up API mocking for these tests" | msw configures MSW 3 handlers and lifecycle. |
| "Make my Next.js app cache correctly" | nextjs applies Next.js 16 App Router caching and routing rules. |
| "Write this feature test-first" | tdd drives red-green-refactor with Vitest 5. |
| "Type-safe URL state" | nuqs maps search params to typed React state. |
| "Review this UI code" | web-design-guidelines checks it against the Web Interface Guidelines. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/PyModel/react-frontend-skills/main/skills/react/SKILL.md
```

Then install the set:

```bash
npx skills add PyModel/react-frontend-skills --all
```

Check your project's majors against the skills' targets before relying on them:

```bash
npx -y @pymodel/react-frontend-skills detect
```

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| react | Pass | Pass | Warn |
| tailwind | Pass | Pass | Warn |
| typescript | Pass | Pass | Fail |
| ui-design | Pass | Pass | Pass |
| playwright | Pass | Pass | Pass |
| nextjs | Pass | Pass | Fail |
| vitest | Pass | Pass | Fail |
| feature-arch | Pass | Pass | Pass |
| zod | Pass | Pass | Warn |
| shadcn | Pass | Pass | Fail |
| react-hook-form | Pass | Pass | Pass |
| tanstack-query | Pass | Pass | Pass |

The sample covers 12 of the 18 indexed listings; typescript, nextjs, vitest, and shadcn carry Snyk Fails, and react, tailwind, and zod carry Snyk Warns.

## Limitations

- Snapshot data, verified Nov 18, 2026: 10,506 combined installs across 18 indexed listings; 43 GitHub stars; MIT licence; last pushed 2026-11-09. Counts drift over time.
- The security sample carries four Snyk Fails (typescript, nextjs, vitest, shadcn) plus three Warns (react, tailwind, zod), so review those skills before production use.
- The skills target current majors only (React 19, Next.js 16, TypeScript 7, Tailwind 4, Vitest 5); older majors were removed in 4.0.0, so projects on older versions need those versions' docs.
- The companion detect CLI reports a range-mismatch when the installed major differs from what package.json declares.

## Related

- [React Doctor - React Codebase Diagnostics Setup](/hermes/skills/catalog/react-doctor-setup)
- [Syncfusion React UI Skills - Component Suite Setup](/hermes/skills/catalog/syncfusion-react-ui-skills-setup)
- [Frontend God Mode - Design Skills Bundle Setup](/hermes/skills/catalog/frontend-god-mode-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the detect CLI first to confirm the project is on the majors the skills target.
- Install per-agent with -a and -s '*' -y to pin the full set to one agent.
- Prefer the npm package plus npx skills experimental_sync for a reproducible, pinned install.
- Run web-design-guidelines and ui-design as a review pass after generating UI.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
