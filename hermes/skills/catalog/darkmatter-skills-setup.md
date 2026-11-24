---
title: "Darkmatter Skills - Team Skill Catalog Setup"
description: "darkmatter/skills - 4.9K combined installs: team-wide TypeScript, Effect, Nix and UI skills for the darkmatter umbrella."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/darkmatter-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "typescript", "effect", "nix"]
---

# Darkmatter Skills - Setup Guide

**Source:** [darkmatter/skills](https://www.skills.sh/darkmatter/skills) via skills.sh - 4.9K combined installs across 31 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 morning sweep)
**GitHub:** [darkmatter/skills](https://github.com/darkmatter/skills) - 0 stars, no LICENSE file, main branch, last pushed Nov 23, 2026; one SKILL.md per directory under skills/ (with reference/ and assets/ subdirectories for several skills), distributed via Nix Home Manager or a Claude Code plugin marketplace.
**Category:** TypeScript, Effect and Nix Engineering Skills
**Quality Tier:** 🟡 Yellow - seven of the 15 sampled skills carry a Warn cell (alchemy, darkmatter-ts-toolchain, effect-typescript, darkmatter-repo-setup, ui-ux-pro-max, shadcn-registry-first, run-ui-registry-variations); no Fail cells, and the repo carries no LICENSE file.

darkmatter/skills is the team-wide skill and preset infrastructure for the darkmatter umbrella, shipped as a source-oriented repository that stays provider-agnostic. Shared skills live under skills/ with one SKILL.md per directory, and the repo also bundles OpenCode presets, shared instruction topics under docs/agents/, skill reference material, and installer and sync tooling. The catalog is distributed through Nix Home Manager on darkmatter machines, or as a Claude Code plugin marketplace for users outside that setup.

The indexed skills concentrate on darkmatter's own TypeScript stack: Effect 4 patterns, the Bun-based darkmatter TypeScript toolchain, Alchemy deploy infrastructure, a Tailwind CSS v4 and React 19 design system, the shadcn registry workflow, and Nix flake organization. The top listings also include maintainability and testing guidance such as codebase-cleanup, when-to-write-tests and ui-component-architecture. The repository carries no LICENSE file, so treat the skills and presets as reference material rather than a clearly licensed dependency until you confirm terms with darkmatter.

## Installation

The README does not document a skills.sh installer command; the command below is the standard installer form for the skills.sh catalog.

```bash
npx skills add darkmatter/skills
```

The README's own distribution paths are the Claude Code plugin marketplace and Nix Home Manager. In Claude Code:

```
/plugin marketplace add darkmatter/skills
/plugin install darkmatter-skills@darkmatter
```

The flake exports a Home Manager module (darkmatter-skills.homeManagerModules.default) that installs every skill into Claude Code, Codex and the generic $HOME/.agents/skills target. On machines without Nix, the README offers `scripts/install-base.sh --target <client config dir>` to install the shared instructions manually.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| nix-flake-organization | 313 | reorganizing Nix flakes and modules into the blueprint-style folder convention |
| alchemy | 311 | configuring and deploying Alchemy v2 infrastructure for darkmatter apps |
| codebase-cleanup | 307 | safely simplifying a codebase without adding features |
| darkmatter-ts-toolchain | 299 | the darkmatter TypeScript stack, persistence and check contract |
| darkmatter-design-system | 298 | the dark-first Tailwind CSS v4 and React 19 design system |
| darkmatter-gitops-conventions | 297 | GitOps conventions (no counterpart in the current skills/ tree) |
| effect-typescript | 296 | Effect 4 patterns for services, Layers, Schema and typed errors |
| keep-codebase-maintainable | 292 | keeping a codebase maintainable (no counterpart in the current skills/ tree) |
| darkmatter-repo-setup | 283 | onboarding a repo to darkmatter standards via the owner skills |
| ui-ux-pro-max | 266 | UI and UX guidance (no counterpart in the current skills/ tree) |
| shadcn-registry-first | 265 | installing existing components from shadcn registries before hand-rolling |
| run-ui-registry-variations | 265 | composing three user-reviewable UI variations from registries |
| when-to-write-tests | 264 | deciding whether a new test is needed |
| ui-component-architecture | 264 | keeping React screens thin and reusable UI in its own package |
| test-driven-development | 264 | test-driven development (no counterpart in the current skills/ tree) |
| sops-secret-access | 264 | accessing secrets via SOPS |
| domain-organization | 252 | domain organization (no counterpart in the current skills/ tree) |

The remaining 14 indexed listings range from 1 to 40 installs.

## Why This Matters for Hermes Agents

darkmatter/skills is a complete worked example of a team-standard agent skill catalog: every skill is a concise SKILL.md that points to a reference/ directory for detail, so the always-on context stays small while deep guidance stays one hop away. For a builder assembling agent skills, the repo demonstrates the cross-vendor AGENTS.md convention plus per-vendor shims, and it shows how to ship the same catalog to Claude Code, Codex, OpenCode and Cursor without forking it. The TypeScript skills are the most immediately reusable: effect-typescript documents Effect 4 services, Layers and typed errors, while darkmatter-ts-toolchain pins the Bun, Effect 4, tsgo, Vitest and oxlint/oxfmt stack. The UI skills encode a clear default: darkmatter-design-system for the dark-first Tailwind v4 and React 19 design system, and shadcn-registry-first for installing existing components before hand-rolling. Testing and maintainability skills such as when-to-write-tests and codebase-cleanup turn judgment calls into checklists. Because there is no LICENSE file, treat the whole catalog as reference material rather than a dependency you can freely vendor.

## Usage

| You say | What happens |
|---|---|
| Set up a new TypeScript repo to darkmatter standards | Uses darkmatter-repo-setup to audit and apply the template via the owner skills |
| Clean up dead code without adding features | Uses codebase-cleanup with its pass-ordered cleanup workflow |
| Write typed Effect code with services and errors | Uses effect-typescript for services, Layers, Schema and typed errors |
| Build a dark-first dashboard with Tailwind | Uses darkmatter-design-system for the Tailwind v4 and React 19 component set |
| Add a shadcn component instead of hand-rolling it | Uses shadcn-registry-first to search and add from the configured registries |
| Reorganize my Nix flakes into folders | Uses nix-flake-organization for the blueprint-style convention |
| Decide whether a change needs a test | Uses when-to-write-tests for the coverage decision |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/darkmatter/skills/main/README.md | head -40
```

Confirm the alchemy skill body is present before deploy work:

```bash
curl -sL https://raw.githubusercontent.com/darkmatter/skills/main/skills/alchemy/SKILL.md | head -30
```

Confirm the codebase-cleanup skill body is present before cleanup work:

```bash
curl -sL https://raw.githubusercontent.com/darkmatter/skills/main/skills/codebase-cleanup/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| nix-flake-organization | Pass | Pass | Pass |
| alchemy | Pass | Pass | Warn |
| codebase-cleanup | Pass | Pass | Pass |
| darkmatter-ts-toolchain | Warn | Pass | Pass |
| darkmatter-design-system | Pass | Pass | Pass |
| darkmatter-gitops-conventions | Pass | Pass | Pass |
| effect-typescript | Pass | Pass | Warn |
| keep-codebase-maintainable | Pass | Pass | Pass |
| darkmatter-repo-setup | Pass | Warn | Warn |
| ui-ux-pro-max | Pass | Warn | Pass |
| shadcn-registry-first | Pass | Pass | Warn |
| run-ui-registry-variations | Pass | Pass | Warn |
| when-to-write-tests | Pass | Pass | Pass |
| ui-component-architecture | Pass | Pass | Pass |
| test-driven-development | Pass | Pass | Pass |

Seven of the fifteen sampled skills carry a Warn cell: darkmatter-ts-toolchain on Gen Agent Trust Hub; ui-ux-pro-max on Socket; alchemy, effect-typescript, shadcn-registry-first and run-ui-registry-variations on Snyk; and darkmatter-repo-setup on both Socket and Snyk. The remaining eight sampled skills pass all three checks. The repository ships no LICENSE file, so confirm terms with darkmatter before treating the skills as a reusable dependency.

## Limitations

- Snapshot data, verified Nov 24, 2026: 4,885 combined installs across 31 indexed listings; 0 GitHub stars; no LICENSE file; last pushed Nov 23, 2026. Counts drift over time.
- The repository carries no LICENSE file, so the skills and presets are not clearly licensed for reuse until you confirm terms with darkmatter; treat them as reference material.
- Index-vs-tree drift: darkmatter-gitops-conventions, keep-codebase-maintainable, ui-ux-pro-max, test-driven-development and domain-organization carry install counts but have no counterpart directory in the current skills/ tree.
- The README documents Claude Code plugin and Nix Home Manager install paths but no skills.sh installer, so the npx form above is the standard installer rather than a documented one.
- Fourteen indexed listings sit at 1 to 40 installs; the long tail is exploratory.
- sops-secret-access has a skills/ tree counterpart but no description in the indexed listing, so its Use For cell is name-level.

## Related

- [codebase-design - Deep Module Design Vocabulary](/hermes/skills/catalog/codebase-design-setup)
- [Next.js Agent Skills - Official Vercel Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Tailwind 4 Docs Skill - Local Docs Snapshot Setup](/hermes/skills/catalog/tailwind-4-docs-skill-setup)
- [System Design Skills - Reasoning-Driven Architecture](/hermes/skills/catalog/system-design-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install via the Claude Code plugin marketplace or Nix Home Manager rather than copying individual SKILL.md files, since the repo expects the catalog to stay in sync.
- Use darkmatter-repo-setup as the entry point; it orchestrates the other skills, so invoke it before reaching for the individual stack skills.
- Prefer shadcn-registry-first over hand-rolling components, and run run-ui-registry-variations to get three reviewable variations before settling.
- Keep an eye on the license situation: with no LICENSE file, do not vendor the skills into a shipped product until darkmatter confirms terms.
- Treat the skills below roughly 300 installs, and the five listings with no tree counterpart, as exploratory.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
