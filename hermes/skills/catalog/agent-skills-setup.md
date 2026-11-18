---
title: "Gohypergiant Agent Skills - Engineering Collection"
description: "gohypergiant/agent-skills: 6.7K combined installs across 46 listings; TypeScript, React, Next.js, testing, security, and skill authoring for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "typescript", "react", "coding standards"]
---

# Gohypergiant Agent Skills - Setup Guide

**Source:** [gohypergiant/agent-skills](https://www.skills.sh/gohypergiant/agent-skills) via skills.sh - 6.7K combined installs across 46 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 25 stars, Apache-2.0 license, `main` branch, last pushed 2026-11-13, skills live under a `skills/` subdirectory, symlinked into `.agents/skills/` and published as a Fumadocs site in `docs/`
**Category:** Coding standards / agent skill authoring
**Quality Tier:** 🟡 Yellow - 57 Pass and 3 Warn across the 20 sampled listings; no Fail.

gohypergiant/agent-skills is a repository of reusable agent skills and the docs site that publishes them. The source of truth lives in `skills/`, and local agent harnesses read the same directories through symlinks in `.agents/skills/`. Most skills carry an `accelint-` prefix; the family covers TypeScript, React, Next.js, testing, security, and README writing.

The repository also names four third-party skills it uses internally (humanizer, ask-questions-if-underspecified, skill-judge, bash-defensive-patterns), which the README recommends installing globally from skills.sh rather than from this repo.

## Installation

Skills follow the Agent Skills format and install through the skills CLI:

```bash
npx skills add gohypergiant/agent-skills
```

With pnpm:

```bash
pnpm dlx skills add gohypergiant/agent-skills
```

The README recommends selecting only the skills relevant to your project, the "Project" installation scope, and the "Symlink" installation method. For contributors, `bash scripts/symlink-agent-skills.sh` rebuilds the `.agents/skills/` symlinks after adding a skill directory.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| accelint-readme-writer | 390 | Write or edit a README.md, analyzing the codebase and generating copy-pasteable examples. |
| accelint-nextjs-best-practices | 386 | Optimize Next.js code: Server Components, data fetching, Server Actions auth, and Suspense. |
| accelint-ts-testing | 350 | Write and review vitest tests with AAA pattern, parameterized tests, and fast-check. |
| accelint-ts-performance | 348 | Audit TypeScript/JavaScript performance with V8 profiling and allocation patterns. |
| accelint-ts-best-practices | 339 | Apply TypeScript coding standards: type safety, defensive programming, and correctness. |
| accelint-react-best-practices | 335 | Optimize React components, re-renders, memoization, state, and hydration. |
| accelint-security-best-practices | 323 | Audit JS/TS applications for OWASP Top 10 vulnerabilities and hardcoded secrets. |
| accelint-react-testing | 282 | Write React component tests with Testing Library and user-centric queries. |
| accelint-tanstack-query-best-practices | 279 | Configure QueryClient, mutations, caching, and optimistic updates with TanStack Query. |
| accelint-ts-documentation | 263 | Audit and improve JSDoc comments and code comment quality. |
| accelint-skill-manager | 230 | Create, refactor, and audit domain expertise into agent skills. |
| accelint-prompt-manager | 219 | Turn draft prompts into clearer, executable prompts without running the task. |
| accelint-ts-audit-all | 204 | Run a full TypeScript file audit across testing, best-practices, performance, and docs. |

The remaining 33 indexed listings range from 1 to 198 installs.

## Why This Matters for Hermes Agents

The accelint- family is organized by concern rather than by product. An agent that needs TypeScript correctness loads the best-practices skill, one that needs speed loads the performance skill, and one that needs coverage loads the testing skill. Each is a focused reference instead of a single oversized style guide.

The suite also covers the process around the code. accelint-onboard-agents writes AGENTS.md or CLAUDE.md so a repository tells its agents how to behave, accelint-onboard-openspec generates an OpenSpec config through a structured interview, and the QRSPI skills drive spec-first planning with review stops before implementation.

Two skills close the loop on the skills themselves. accelint-skill-manager scaffolds and audits new skills, and accelint-ts-audit-all chains the four TypeScript skills into a single audit that tracks progress and approves changes interactively. For a team standardizing how coding agents work, this is the entry point.

## Usage

| You say | What happens |
|---|---|
| "Add these skills to my project" | `npx skills add gohypergiant/agent-skills` installs the skills, prompting for scope and method. |
| "Audit this TypeScript file" | accelint-ts-audit-all runs the testing, best-practices, performance, and docs audits in one pass. |
| "Review my React components for re-renders" | accelint-react-best-practices applies memoization, state, and hydration patterns. |
| "Write a README for this repo" | accelint-readme-writer analyzes the codebase and generates README content with examples. |
| "Set up OpenSpec for this project" | accelint-onboard-openspec runs a structured interview and writes a QRSPI config. |
| "Create a new agent skill" | accelint-skill-manager scaffolds a skill directory and runs a quality audit. |

## Verification

Probe a skill on the `main` branch before installing. The path reflects the `skills/` subdirectory layout:

```bash
curl -fsSL https://raw.githubusercontent.com/gohypergiant/agent-skills/main/skills/accelint-readme-writer/SKILL.md | head -12
```

The installer is `npx skills add gohypergiant/agent-skills` (or `pnpm dlx skills add gohypergiant/agent-skills`).

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| accelint-readme-writer | Pass | Pass | Pass |
| accelint-nextjs-best-practices | Pass | Pass | Pass |
| accelint-ts-testing | Pass | Pass | Pass |
| accelint-ts-performance | Pass | Pass | Pass |
| accelint-ts-best-practices | Pass | Pass | Pass |
| accelint-react-best-practices | Pass | Pass | Pass |
| accelint-security-best-practices | Pass | Warn | Pass |
| accelint-react-testing | Pass | Pass | Pass |
| accelint-tanstack-query-best-practices | Pass | Pass | Pass |
| accelint-ts-documentation | Pass | Pass | Pass |
| accelint-skill-manager | Pass | Pass | Pass |
| accelint-prompt-manager | Pass | Pass | Pass |
| accelint-ts-audit-all | Pass | Pass | Pass |
| accelint-onboard-agents | Pass | Pass | Pass |
| accelint-onboard-openspec | Pass | Pass | Pass |
| accelint-qrspi-propose | Pass | Pass | Pass |
| accelint-architecture-doc | Pass | Pass | Pass |
| accelint-persona-review | Pass | Pass | Warn |
| accelint-qrspi-apply | Pass | Pass | Pass |
| humanizer | Pass | Pass | Warn |

The three Warns are Socket on accelint-security-best-practices and Snyk on accelint-persona-review and humanizer; no skill in the sample Fails any auditor.

## Limitations

- Snapshot data, verified 2026-11-17: 6,683 combined installs across 46 indexed listings; 25 GitHub stars; Apache-2.0; last pushed 2026-11-13. Counts drift over time.
- The skills.sh index (46 listings) outruns the repo tree, which holds 32 skill directories under `skills/`. Four indexed skills are third-party skills the repo uses internally (humanizer, ask-questions-if-underspecified, skill-judge, bash-defensive-patterns); the other unmatched index entries have no directory in the current tree.
- The README does not define what the `accelint-` prefix stands for; treat it as a naming convention, not a documented product family.
- Install counts concentrate in the accelint- TypeScript, React, and Next.js skills; the authoring and process skills trail far behind.
- The repo is content-first rather than library-first; the API surface is the directory structure and the scripts you work with, not a published library.

## Related

- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Cursor Plugins Skills - Engineering Discipline Suite Setup](/hermes/skills/catalog/cursor-plugins-skills-setup)
- [AI Dev Standards Skills - Design Setup](/hermes/skills/catalog/ai-dev-standards-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install with "Project" scope and "Symlink" method so the skill reads stay in sync with upstream.
- Let accelint-ts-audit-all drive broad cleanups; it chains the four TypeScript skills and tracks progress across sessions.
- Reach for accelint-onboard-agents first on a new repo, before the coding skills, so agent behavior rules exist before the work starts.
- The four internal skills are third-party; install them globally from skills.sh, not from this repo.
- After adding a skill locally, run `bash scripts/symlink-agent-skills.sh` so `.agents/skills/` picks it up.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
