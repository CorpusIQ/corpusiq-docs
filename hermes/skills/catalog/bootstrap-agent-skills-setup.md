---
title: "Bootstrap Agent Skills - Framework Guidance"
description: "twbs/bootstrap: 6.5K combined installs across 12 listings, official Bootstrap 6 agent skills for colour, components, builds and migration."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/bootstrap-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "bootstrap", "css", "frontend"]
---

# Bootstrap Agent Skills - Setup Guide

**Source:** [twbs/bootstrap](https://www.skills.sh/twbs/bootstrap) via skills.sh - 6.5K combined installs across 12 indexed listings; first seen Nov 14, 2026 (this sweep)
**GitHub:** 175,057 stars, MIT license, `main` branch, last pushed 2026-11-12, 12 `SKILL.md` files (11 in `skills/<name>/` plus `.cursor/skills/bootstrap-release/`)
**Category:** Bootstrap 6 / CSS framework agent skills
**Quality Tier:** 🟢 Green - official repo, MIT license, all six sampled verdicts pass.

The Bootstrap source repo now ships official agent skills for Bootstrap 6. The suite covers the colour system, components and their JavaScript behaviour, the utility API, four build setups (Vite, npm, Parcel, Webpack) and both v5-to-v6 and v4-to-v6 migrations. Eleven of the twelve skills sit in `skills/<name>/`; the release skill lives in `.cursor/skills/bootstrap-release/`.

This is the framework's own repo, so the skills document the current Bootstrap 6 API the way its maintainers intend it, not a third-party interpretation. The `main` branch tracks Bootstrap 6 development, while Bootstrap 5 lives on the `v5-dev` branch, which is why the v5-to-v6 migration skill matters for anyone still on v5.

## Installation

The README quick start installs the framework itself:

```bash
npm install bootstrap@6.0.0-alpha.1
```

It also lists yarn, Bun, Composer and NuGet variants. The README does not document a `npx skills` command for the agent skills, so install them explicitly:

```bash
npx skills add twbs/bootstrap --skill 'bootstrap-v6-install' -g
```

Install the full set with `--skill '*'` instead of a single name.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| bootstrap-color-system | 632 | Work with Bootstrap 6's colour system in Sass and CSS, adding or overriding theme colours. |
| bootstrap-component | 625 | Build a Bootstrap 6 component's CSS and markup, including modifiers and variants. |
| bootstrap-component-js | 616 | Add JavaScript behaviour to a Bootstrap 6 component from its TypeScript source. |
| bootstrap-v6-install | 610 | Add Bootstrap 6 to a project and set it up for local development. |
| bootstrap-utility-api | 607 | Use, extend and customize Bootstrap 6's utility API. |
| bootstrap-v5-v6-migration | 600 | Migrate a project from Bootstrap 5 to Bootstrap 6. |
| bootstrap-vite | 574 | Bundle Bootstrap 6's CSS and JavaScript in a Vite project. |
| bootstrap-npm | 573 | Build a Bootstrap 6 starter project with npm and CLI tools, no bundler. |
| bootstrap-parcel | 547 | Bundle Bootstrap 6's CSS and JavaScript in a Parcel project. |
| bootstrap-webpack | 542 | Bundle Bootstrap 6's CSS and JavaScript in a Webpack project. |
| bootstrap-v4-v6-migration | 540 | Migrate a project from Bootstrap 4 to Bootstrap 6. |

The remaining 1 indexed listing is bootstrap-release (1 install), which cuts a Bootstrap release from version preparation through npm, GitHub, NuGet and documentation deployment.

## Why This Matters for Hermes Agents

Bootstrap 6 is a major release, and the API surface an agent must know changed with it: the colour system, the utility API, TypeScript-backed component JavaScript and new build setups. An agent drawing on Bootstrap 5 habits will emit code that no longer matches the current docs. These skills pin the agent to the v6 API, and the two migration skills (v5-to-v6 and v4-to-v6) give it a checklist instead of a guess when upgrading an existing project.

The build-coverage point matters too. The same bundling task is spelled out four ways (Vite, npm-only, Parcel, Webpack), so an agent can follow the setup that matches the project's actual toolchain rather than force-fitting a generic import block. The utility-API and colour-system skills cover the customization surface most agents get wrong, where the fix is Sass configuration rather than overriding compiled CSS.

Because these skills live in the official repo and are maintained by the Bootstrap team, they track the framework's own release cadence. That is a stronger grounding signal than a community pack that may lag a major version behind.

## Usage

| You say | What happens |
|---|---|
| "Add Bootstrap 6 to my project" | Runs bootstrap-v6-install for the install and local-development setup. |
| "Customize the theme colours" | Runs bootstrap-color-system to modify the Sass colour map. |
| "Build a new component" | Runs bootstrap-component for the CSS and markup. |
| "Add interactivity to a component" | Runs bootstrap-component-js for the TypeScript-backed behaviour. |
| "Bundle it with Vite" | Runs bootstrap-vite for the Vite-specific CSS and JS setup. |
| "Upgrade this project from v5" | Runs bootstrap-v5-v6-migration for the v5-to-v6 checklist. |

## Verification

Probe skills on the `main` branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/twbs/bootstrap/main/skills/bootstrap-v6-install/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/twbs/bootstrap/main/skills/bootstrap-color-system/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/twbs/bootstrap/main/skills/bootstrap-v5-v6-migration/SKILL.md
```

Skills live at `skills/<name>/SKILL.md` on `main`; the release skill is the one exception at `.cursor/skills/bootstrap-release/SKILL.md`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| bootstrap-color-system | Pass | Pass | Pass |
| bootstrap-component | Pass | Pass | Pass |
| bootstrap-component-js | Pass | Pass | Pass |
| bootstrap-v6-install | Pass | Pass | Pass |
| bootstrap-utility-api | Pass | Pass | Pass |
| bootstrap-v5-v6-migration | Pass | Pass | Pass |

All six sampled skills pass all three auditors. The sample covers 6 of the 12 indexed listings, so it says little about the remaining 6.

## Limitations

- Snapshot data, verified 2026-11-14: 6,467 combined installs across 12 indexed listings; 175,057 GitHub stars; MIT; last pushed 2026-11-12. Counts drift over time.
- The README documents framework installs (npm, yarn, Bun, Composer, NuGet) but no `npx skills` command for the agent skills; the install line above is a fallback.
- bootstrap-release sits at 1 install and is a maintainer-facing release skill, not general usage guidance.
- Code is MIT, but the README licenses the docs under Creative Commons BY 3.0; treat the two assets separately if you redistribute either.
- The security sample covers only 6 of 12 listings; the rest publish no verdict on skills.sh.

## Related

- [daisyUI Skills - Tailwind Component Tokens](/hermes/skills/catalog/daisyui-skills-setup)
- [Ant Design Skills - Official antd Agent Suite Setup](/hermes/skills/catalog/ant-design-skills-setup)
- [Designlang Skill - Extract Any Site's Design System](/hermes/skills/catalog/design-extract-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- On an existing project, run the matching migration skill (v5 or v4) before the build-setup skill; the migration output changes the install you need.
- Pick the build skill that matches your toolchain exactly rather than installing all four.
- The colour and utility skills edit Sass configuration, so keep the compiled CSS out of the diff when the agent works on them.
- Since `main` tracks Bootstrap 6, confirm the version you are targeting before trusting the v6 API the skills describe.
- Keep the release skill out of a general-purpose install; it assumes maintainer access to npm, GitHub and NuGet.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
