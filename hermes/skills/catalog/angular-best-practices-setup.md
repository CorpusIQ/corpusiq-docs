---
title: "Angular Best Practices - Agent Rules and Library Skills"
description: "alfredoperez/angular-best-practices - 5.9K combined installs: curated Angular rules and library skills for AI agents (archived; use angular/skills)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/angular-best-practices-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "angular", "frontend", "rules"]
---

# Angular Best Practices - Setup Guide

**Source:** [alfredoperez/angular-best-practices](https://www.skills.sh/alfredoperez/angular-best-practices) via skills.sh - 5.9K combined installs across 12 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [alfredoperez/angular-best-practices](https://github.com/alfredoperez/angular-best-practices) - 36 stars, no LICENSE file (the README says MIT), last pushed Mar 28, 2026, main branch; archived on GitHub. Skills live under skills/<name>/SKILL.md, with two contributor skills under .claude/skills/.
**Category:** Frontend Development Rules (Angular)
**Quality Tier:** 🟡 Yellow - 9 of 12 listings sampled: no Fail verdicts, but one Snyk Warn on angular-best-practices-rules-reviewer.

alfredoperez/angular-best-practices is a curated rule set for building performant, maintainable Angular 17+ applications, packaged for AI agents. The core skill covers Signals, RxJS, components, templates, performance, SSR, testing, forms, routing, and accessibility, and eight library skills add rules for Angular Material, PrimeNG, NgRx, SignalStore, Spartan UI, TanStack Query, and Transloco. The repository is archived on GitHub: the README points contributors to the official angular/skills resource and states the project is no longer maintained, so treat this as a snapshot rather than an actively maintained suite.

All rules are compiled into a single AGENTS.md by a TypeScript build script (packages/angular-best-practices-build), and the README documents a manual install path for Claude Code, Cursor, and VS Code Copilot.

## Installation

The README documents the skills CLI for the core skill and optional library skills:

```bash
npx skills add alfredoperez/angular-best-practices
npx skills add alfredoperez/angular-best-practices-ngrx
npx skills add alfredoperez/angular-best-practices-signalstore
npx skills add alfredoperez/angular-best-practices-tanstack
```

Or copy AGENTS.md directly into your project: .claude/AGENTS.md for Claude Code, .cursor/rules/angular.md for Cursor, and .github/copilot-instructions.md for VS Code Copilot. Because the repository is archived, prefer the official angular/skills resource for new projects.

## What It Provides

skills.sh publishes per-skill install counts for all 12 indexed listings. The 8 most-installed skills are listed below; the remaining 4 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| angular-best-practices | 1,541 | core modern Angular rules: Signals, RxJS, components, templates, performance, SSR, testing, forms, routing, accessibility |
| angular-best-practices-primeng | 979 | PrimeNG rules: tree-shaking imports, lazy-loaded tables, and Aura/Lara theming with design tokens |
| angular-best-practices-ngrx | 617 | NgRx rules: pure reducers, action groups, entity adapter, selectors, and signal-based selection |
| angular-best-practices-signalstore | 595 | SignalStore rules: shared state, computed state, entity management, and rxMethod integration |
| angular-best-practices-material | 540 | Angular Material and CDK rules: selective imports, M3 theming, CDK utilities, and test harnesses |
| angular-best-practices-rules-reviewer | 359 | review and audit rule files for accuracy, validity, and formatting (contributor skill) |
| angular-best-practices-transloco | 354 | Transloco i18n rules: runtime translation, lazy-loaded files per route, and test mocking |
| angular-best-practices-rule-creator | 340 | create new rule files and library skills following project conventions (contributor skill) |

The remaining 4 indexed listings range from 12 to 283 installs.

## Why This Matters for Hermes Agents

This suite gives an agent a single, token-efficient checklist for Angular instead of scattered documentation. Every rule is a concise file (under 50 lines, one to three line code examples) with an impact rating and an incorrect vs correct pattern, so an agent can apply the CRITICAL and HIGH rules first and skip what the project does not use. The Signals and SSR rules matter most now that Angular 17+ is signals-first, and the library skills keep an agent from mixing component-library guidance (Material vs PrimeNG vs Spartan). The build script compiles every rule into one AGENTS.md, which is a cheap way to give an agent the whole reference in a single context load. The two contributor skills (rules-reviewer and rule-creator) are explicitly not for Angular application development, so they are for maintainers of this repository only.

## Usage

| You say | What happens |
|---|---|
| Review my Angular component | Applies the core rules for components, templates, and change detection |
| Use NgRx here | Uses angular-best-practices-ngrx for reducers, selectors, and signal selection |
| Set up SignalStore state | Uses angular-best-practices-signalstore for shared, computed, and entity state |
| Add Angular Material | Uses angular-best-practices-material for selective imports and M3 theming |
| Migrate this to signals | Applies the signal rules for computed, model, resource, and view queries |
| Audit the bundle | Uses the optimization rules for bundle size and async waterfalls |

## Verification

Confirm the README and two skill bodies resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/alfredoperez/angular-best-practices/main/skills/angular-best-practices/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/alfredoperez/angular-best-practices/main/skills/angular-best-practices-ngrx/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warn verdict noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| angular-best-practices | Pass | Pass | Pass |
| angular-best-practices-primeng | Pass | Pass | Pass |
| angular-best-practices-ngrx | Pass | Pass | Pass |
| angular-best-practices-signalstore | Pass | Pass | Pass |
| angular-best-practices-material | Pass | Pass | Pass |
| angular-best-practices-rules-reviewer | Pass | Pass | Warn |
| angular-best-practices-transloco | Pass | Pass | Pass |
| angular-best-practices-rule-creator | Pass | Pass | Pass |
| angular-best-practices-spartan | Pass | Pass | Pass |

Across the 9 sampled skills there are 26 Pass, 1 Warn, and 0 Fail cells. Eight skills pass all three checks; angular-best-practices-rules-reviewer carries the single Snyk Warn.

## Limitations

- Snapshot data, verified Nov 26, 2026: 5,873 combined installs across 12 indexed listings; 36 GitHub stars; no LICENSE file (the README says MIT); last pushed Mar 28, 2026. Counts drift over time.
- The repository is archived on GitHub and no longer maintained; the README points to the official angular/skills resource instead.
- skills.sh sampled only 9 of the 12 indexed listings; angular-best-practices-tanstack, rules-reviewer, and rule-creator carry no published verdict.
- rules-reviewer and rule-creator have no matching directory in the current tree; they mirror the angular-best-practices-rules-reviewer and angular-best-practices-rule-creator contributor skills under .claude/skills/.
- The repo advertises "MIT" in its README License section, but no LICENSE file is present and GitHub reports no license detected.

## Related

[Angular Framework Skills - Official Repo Agent Guides](/hermes/skills/catalog/angular-framework-agent-skills-setup) | [Angular Skills - Framework Development Setup](/hermes/skills/catalog/angular-skills-setup) | [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- The core angular-best-practices skill is the entry point; install the library skills only for the libraries your project actually uses.
- Read the impact ratings (CRITICAL, HIGH, MEDIUM, LOW) first and apply the CRITICAL and HIGH rules before the rest.
- Run `npm run build` in the repo to regenerate AGENTS.md, and use `--exclude ngrx,signalstore,tanstack` to strip unused library rules.
- The repository is archived, so fork it before customizing rules you intend to keep long-term.
- Skip rules-reviewer and rule-creator unless you are contributing rule files to the repository itself.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
