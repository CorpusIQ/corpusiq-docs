---
title: "WordPress Agent Skills - Official WP Development Setup"
description: "Setup guide for wordpress/agent-skills - 17.7K combined installs. Official WordPress skills for Playground, blueprints, and plugin development."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/wordpress-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "wordpress", "gutenberg", "plugin development"]
---

# WordPress Agent Skills - Setup Guide

**Source:** [wordpress/agent-skills](https://www.skills.sh/wordpress/agent-skills) via skills.sh - 17.7K combined installs across 7 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [wordpress/agent-skills](https://github.com/wordpress/agent-skills) (2,217 stars, NOASSERTION - README states GPL-2.0-or-later; pushed 2026-10-05; default branch `trunk`; skills under `skills/`, e.g. `skills/wp-playground/SKILL.md`)
**Category:** WordPress / Web Development
**Quality Tier:** 🟢 Production - official WordPress publisher; GPL-family license (NOASSERTION); active Oct 2026; Snyk Warn on one sampled skill

Agent Skills for WordPress is the official WordPress publisher suite that teaches AI coding assistants how to build WordPress the right way. The README lists 18 skills spanning blocks, block themes, plugins, the REST API, the Abilities API, Playground, WP-CLI, performance, and PHPStan, and 7 of them carry indexed install counts on skills.sh.

The skills are portable bundles of instructions, checklists, and scripts. They were generated using GPT-5.2 Codex (High Reasoning) from official Gutenberg and WordPress documentation, then reviewed and edited by WordPress contributors; the project labels this v1 and expects community contributions to improve it. A typical starting point for plugin work is `wp-plugin-development` plus `wp-plugin-directory-guidelines`; for environment work, `wp-playground` and `blueprint`.

---

## Installation

### skills.sh

```bash
# Install a skill (quick start)
npx skills add WordPress/agent-skills --skill wp-plugin-development

# See all available skills
npx skills add WordPress/agent-skills --list

# Install several skills at once
npx skills add WordPress/agent-skills --skill wp-plugin-development wp-abilities-api wp-playground
```

Add `--global` to install for all your projects instead of a single project scope:

```bash
npx skills add WordPress/agent-skills --skill wp-plugin-development --global
```

### Repo-local install

Clone the repo and use its skillpack scripts to build and install for a specific toolchain:

```bash
git clone https://github.com/WordPress/agent-skills.git
cd agent-skills
node shared/scripts/skillpack-build.mjs --clean
node shared/scripts/skillpack-install.mjs --dest=../your-wp-project --targets=codex,vscode,claude,cursor
```

### Prerequisites

WordPress 7.0+ (PHP 7.4.0+) is the compatibility floor, and any AI assistant that supports project-level instructions can use the skills.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| wp-playground | 4,251 | WordPress Playground routing, CLI runs, browser previews, and snapshots |
| blueprint | 3,434 | WordPress Playground Blueprints for declarative environment setup |
| wp-plugin-directory-guidelines | 3,202 | WordPress Plugin Directory Guidelines |
| wp-abilities-audit | 2,384 | Audit a plugin's REST surface and propose Abilities API registrations |
| wp-abilities-verify | 2,313 | Verify a plugin's Abilities API registrations against their declared annotations |
| wp-patterns | 1,786 | Create and update block patterns: starter pages, templates, template parts, and Query Loop layouts |

The remaining 1 indexed listing is wp-env (334 installs), local WordPress development with @wordpress/env.

## Why This Matters for Hermes Agents

AI coding assistants have a well-documented WordPress failure mode: they generate pre-Gutenberg patterns, skip block deprecations that later throw "Invalid block" errors, and miss the security considerations that plugin review catches. This suite gives Hermes agents expert-level WordPress knowledge in the format they actually consume, loaded as instructions, checklists, and scripts from the repo. The coverage matches the surfaces where agent-generated WordPress code causes the most rework: blocks, block themes, plugins, REST routes, and the newer Abilities API. Because it is published by the WordPress project itself and reviewed by contributors, the patterns track official documentation instead of model folklore. The skills are plain folders with SKILL.md plus references and scripts, so they travel across Claude, Copilot, Codex, Cursor, and other SKILL.md-aware tools.

## Usage

| You say | What happens |
|---|---|
| Set up a scratch WordPress in seconds to test a patch | wp-playground routes Playground CLI runs, browser previews, and snapshots |
| Give me a reproducible dev environment for the team | blueprint declares it as a WordPress Playground Blueprint that builds on demand |
| Review my plugin before Directory submission | wp-plugin-directory-guidelines checks the code against Plugin Directory rules |
| Audit my plugin's REST surface for the Abilities API | wp-abilities-audit inventories endpoints and proposes Abilities API registrations |
| Verify our Abilities API registrations match their annotations | wp-abilities-verify checks each registration against what it declares |
| Build a starter page from block patterns | wp-patterns creates or updates starter pages, templates, template parts, and Query Loop layouts |
| Run local WordPress with Xdebug for step debugging | wp-env sets up @wordpress/env with configuration, WP-CLI, and Xdebug troubleshooting |

## Verification

Confirm the install from the CLI or the skills directory:

```bash
npx skills list | grep wp-
```

In Claude Code, the repo-local installer copies skills to `~/.claude/skills/` for automatic discovery. Project installs land in `.claude/skills/`, `.cursor/skills/`, `.codex/skills/`, or `.github/skills/` depending on the target. Before installing, review the exact instructions the agent will read: fetch the Playground skill file at `https://raw.githubusercontent.com/wordpress/agent-skills/trunk/skills/wp-playground/SKILL.md` (verified reachable Oct 10, 2026).

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| wp-playground | Pass | Pass | Warn |
| blueprint | Pass | Pass | Pass |
| wp-plugin-directory-guidelines | Pass | Pass | Pass |

## Limitations

- Snyk marks wp-playground with a Warn; read that security page before wiring Playground automation into a pipeline.
- Verdicts cover the three sampled skills only; wp-abilities-audit, wp-abilities-verify, and wp-patterns are unaudited here.
- AI authorship: the skills were generated with GPT-5.2 Codex (High Reasoning) from official documentation and reviewed by WordPress contributors; the project labels the set v1 and expects iteration.
- GitHub reports NOASSERTION for the license while the README states GPL-2.0-or-later; confirm terms before redistribution.
- Compatibility floor is WordPress 7.0+ (PHP 7.4.0+); older targets are out of scope.
- Default branch is `trunk`, not `main` - point raw-file links and vendoring at `trunk`.

- Snapshot data, verified Oct 10, 2026: 17,704 combined installs across 7 indexed listings; 2,217 GitHub stars; NOASSERTION (README states GPL-2.0-or-later); last pushed 2026-10-05. Counts drift over time.

## Related

- [Netlify Agent Skills - Serverless Deployment for Hermes Setup](/hermes/skills/catalog/netlify-agent-skills-setup) - deploy the headless front end that consumes your WordPress APIs
- [Medusa Agent Skills - Official Ecommerce Platform Setup](/hermes/skills/catalog/medusa-agent-skills-setup) - another official publisher suite worth pairing
- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup) - official Vercel skills for headless front ends
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `npx skills add WordPress/agent-skills --list` first; the suite is large and most projects only need a subset.
- Choose scope deliberately: global puts WordPress knowledge in every repo, while project scope can be committed so the whole team shares it.
- Start routing with wordpress-router and wp-project-triage in mixed repos, then jump to the task skill.
- Pair wp-plugin-development with wp-plugin-directory-guidelines before you open a Directory submission.
- Keep the `trunk` branch in mind when pinning revisions or linking raw files.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
