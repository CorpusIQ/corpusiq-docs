---
title: "Purrfold Scaffold - Frontend App Generation Skills"
description: "c3sc0-v4113/scaffold - 21.7K combined installs across 5 indexed listings: purrfold CLI plus four governance skills for generated frontend apps."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/c3sc0-scaffold-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "frontend", "scaffolding", "shadcn"]
---

# Purrfold Scaffold - Setup Guide

**Source:** [c3sc0-v4113/scaffold](https://www.skills.sh/c3sc0-v4113/scaffold) via skills.sh - 21.7K combined installs across 5 indexed listings; first seen Nov 16, 2026 (Nov 16 evening sweep)
**GitHub:** 3 stars, MIT license, `main` branch, last pushed 2026-11-16, five skills under `skills/<name>/SKILL.md` plus a `.agents/skills/architecture-decision-records/SKILL.md` bridge
**Category:** Frontend scaffolding - purrfold generates Next.js, Astro, Vite and React Router apps with a shadcn and linting baseline
**Quality Tier:** 🟢 Green - all 5 sampled skills pass the Gen Agent Trust Hub, Socket, and Snyk.

The Scaffold repository ships a TypeScript CLI called purrfold plus five agent skills. Running `npx purrfold@latest my-app` produces a fresh Next.js, Astro, Vite or React Router framework app and layers on a quality baseline: shadcn setup, strict ESLint with `@shadcn/lint` design-system rules, Prettier, Husky, React Doctor, React Scan, agent docs and Claude compatibility, with optional unit, E2E and commit tooling.

The install data looks lopsided because of how the skills travel. The four governance skills each hold over five thousand installs because purrfold downloads them into every generated app via `npx skills add`, while the purrfold listing itself sits at 2 installs because the CLI is the distribution channel rather than a standalone skill people install.

## Installation

Install the purrfold CLI and scaffold a new app:

```sh
npx purrfold@latest my-app --yes
```

Install the Claude Code skill (the README's own path):

```sh
npx skills@latest add github:C3SC0-V4113/Scaffold --skill purrfold --copy --yes
```

By hand: copy `skills/<name>/SKILL.md` into your agent's skills directory, for example `.claude/skills/` or `~/.hermes/profiles/corpusiq/skills/`. purrfold also downloads these skills into each generated app's `.agents/skills/` directory automatically.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| shadcn-component-boundaries | 5,445 | Enforcing registry and product component boundaries so the shadcn `ui` path stays reserved for registry primitives. |
| decision-doc-sync | 5,444 | Keeping existing project docs in sync with architecture changes, new conventions and ADRs. |
| project-architecture | 5,387 | Keeping Next.js and Astro apps server-first across UI, layout, state flow and theming decisions. |
| project-min-evaluation | 5,381 | Running the project's own minimum quality scripts before work is called complete. |

The remaining 1 indexed listing ranges from 2 to 2 installs.

The fifth listing is purrfold at 2 installs, the CLI driver itself. It is the channel: purrfold downloads the four skills above into every generated app, which is why those four carry the install traffic while the CLI does not.

## Why This Matters for Hermes Agents

purrfold treats a coding agent as its primary user: the README maps user intent to the exact `npx purrfold` invocation and exposes the full option schema as `npx purrfold@latest info --json`, so an agent can scaffold the right stack without a human translating the flags. The four governance skills are the part worth copying, because they are the rails a generated app rides on after the scaffold.

shadcn-component-boundaries reserves the shadcn `ui` path for registry primitives, project-architecture keeps Next.js and Astro apps server-first, decision-doc-sync keeps docs in line with every structural decision, and project-min-evaluation forces the project's own quality scripts to pass before anything is declared done. project-min-evaluation is the lesson for agent reliability: a generated app carries its own minimum quality gate, and the agent is told to run it before claiming completion, which is exactly the verification discipline a long-running agent needs.

The generated baseline is also a strong default: strict ESLint with `@shadcn/lint` blocks restyled components, raw colors, arbitrary values and inline styles, with a generated DESIGN.md explaining each rule, so the design system is enforced mechanically rather than by memory.

## Usage

| You say | What happens |
|---|---|
| "Scaffold a new Next.js app" | `npx purrfold@latest my-app --yes` creates the app with the full quality baseline and downloads the governance skills. |
| "Scaffold an Astro app with SSR on Cloudflare" | `npx purrfold@latest my-app --framework astro --ssr --adapter cloudflare --yes` generates the Astro SSR setup with the adapter. |
| "Keep the shadcn ui directory clean" | shadcn-component-boundaries enforces registry and product boundaries so primitives stay where they belong. |
| "Log an architecture decision and update the docs" | decision-doc-sync keeps project docs in sync with the ADR and the new convention. |
| "Check the app before I say it is done" | project-min-evaluation runs the project's own minimum quality scripts and fails the claim if any fail. |
| "This UI change might break the server-first layout" | project-architecture keeps the Next.js or Astro app server-first across the change. |

## Verification

Check the tree before copying:

```sh
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/C3SC0-V4113/Scaffold/main/skills/shadcn-component-boundaries/SKILL.md
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/C3SC0-V4113/Scaffold/main/skills/decision-doc-sync/SKILL.md
```

Each URL prints 200. The skill root is `skills/` on branch `main`, and each of the five directories sits directly under it with its own SKILL.md, some with a references/ folder.

After copying, count what landed:

```sh
find ~/.hermes/profiles/corpusiq/skills -maxdepth 2 -name SKILL.md | wc -l
```

The count should be 5 if the profile started empty.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| shadcn-component-boundaries | Pass | Pass | Pass |
| decision-doc-sync | Pass | Pass | Pass |
| project-architecture | Pass | Pass | Pass |
| project-min-evaluation | Pass | Pass | Pass |
| purrfold | Pass | Pass | Pass |

All 5 sampled skills pass all three scanners.

## Limitations

- Snapshot data, verified Nov 16, 2026: 21,659 combined installs across 5 indexed listings; 3 GitHub stars; MIT; last pushed 2026-11-16. Counts drift over time.
- The install counts concentrate in four skills that purrfold downloads into generated apps; the purrfold listing itself holds 2 installs, so the table does not reflect which skill is the flagship.
- The CLI targets new projects created with create-next-app, create-astro, create-vite or create-react-router; it does not retrofit existing apps.
- The repository has 3 GitHub stars at snapshot, so it carries little community vetting compared with larger catalogs.
- `.agents/skills/architecture-decision-records/SKILL.md` appears as a bridge alongside the five `skills/` directories, and the README notes `.claude/skills` is only a compatibility bridge.

## Related

- [System Design Skills](/hermes/skills/catalog/system-design-skills-setup)
- [Context Engineering Kit](/hermes/skills/catalog/context-engineering-kit-setup)
- [Code Review Skill](/hermes/skills/catalog/code-review-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Always pass `--yes` when running purrfold non-interactively so it does not block on prompts.
- Run a `--dry-run` first to preview every file and package operation before the real scaffold.
- Keep the shadcn `ui` path reserved for registry primitives; violating that boundary breaks future shadcn updates.
- Run the generated app's own `check` script before declaring work complete; project-min-evaluation exists to make that a hard gate.
- Scaffold to the package manager the project will actually use (`--pm npm|pnpm|bun`) from the start, since changing it later rewrites the lockfile and scripts.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
