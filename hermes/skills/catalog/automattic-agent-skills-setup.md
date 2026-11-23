---
title: "Automattic Agent Skills - WordPress Development Setup"
description: "Agent Skills for WordPress by Automattic: plugin, block theme, block, REST API and WP-CLI guidance for AI assistants - 5.3K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/automattic-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "wordpress", "woocommerce", "gutenberg"]
---

# Automattic Agent Skills - WordPress Development Setup

**Source:** [automattic/agent-skills](https://www.skills.sh/automattic/agent-skills) via skills.sh - 5.3K combined installs across 13 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 morning sweep)
**GitHub:** [automattic/agent-skills](https://github.com/automattic/agent-skills) - 211 stars, no LICENSE file, trunk branch, archived, last pushed Feb 1, 2026; one SKILL.md per skill directory under skills/ with references/ and scripts/ alongside.
**Category:** WordPress and Web Development Knowledge
**Quality Tier:** 🟢 Green - all 13 sampled skills carry Pass across Gen Agent Trust Hub, Socket and Snyk, with zero Warn or Fail cells.

Agent Skills for WordPress teaches AI coding assistants how to build WordPress the right way. Each skill is a portable bundle of instructions, checklists and scripts that an assistant such as Claude, Copilot, Codex or Cursor reads as context, covering plugin development, block themes, Gutenberg blocks, WP-CLI operations, the REST API, performance, PHPStan, WordPress Playground and the WordPress Design System. The README states the premise plainly: stock models generate outdated pre-Gutenberg patterns, miss security considerations in plugin code, skip block deprecations that later produce "Invalid block" errors, and ignore tooling already present in the repository.

Two things stand out about the suite. First, the repository is archived and has moved to WordPress/agent-skills, so this snapshot captures the Automattic-era code that all future development has left behind. Second, every skill sits in a narrow install band of 307 to 551 installs with a wordpress-router umbrella at 468 that classifies a repository and routes the agent to the correct workflow skill. The README targets WordPress 6.9+ (PHP 7.2.24+) and states that any assistant that supports project-level instructions can use the skills.

## Installation

The README installs skills by cloning the repository, building a distribution, then running the install script, rather than through a plugin marketplace or package registry:

```bash
git clone https://github.com/WordPress/agent-skills.git
cd agent-skills
node shared/scripts/skillpack-build.mjs --clean
node shared/scripts/skillpack-install.mjs --global
```

The global install writes skills to ~/.claude/skills/. To install into a specific WordPress project instead:

```bash
git clone https://github.com/Automattic/agent-skills.git
cd agent-skills
node shared/scripts/skillpack-build.mjs --clean
node shared/scripts/skillpack-install.mjs --dest=../your-wp-project --targets=codex,vscode,claude
```

The project install copies skills into .codex/skills/, .github/skills/ and .claude/skills/ for OpenAI Codex, VS Code or GitHub Copilot, and Claude Code respectively. The installer also supports --list, --dry-run and --skills= for a selective install, and skills can be copied into an assistant's instructions directory manually.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| wp-plugin-development | 551 | plugin architecture, hooks, Settings API, data, cron and security |
| wp-block-themes | 542 | block themes: theme.json, templates, patterns and style variations |
| wp-wpcli-and-ops | 496 | WP-CLI operations: search-replace, multisite, cron, cache and automation |
| wp-block-development | 475 | Gutenberg blocks: block.json, attributes, rendering and deprecations |
| wordpress-router | 468 | classifying a WordPress repo and routing to the right workflow |
| wp-performance | 436 | profiling, caching, database and object-cache optimization |
| wp-phpstan | 382 | PHPStan configuration, baselines and WordPress-specific typing |
| wp-project-triage | 357 | deterministic repo inspection with a structured JSON report |
| wpds | 348 | WordPress Design System components, tokens and patterns |
| wp-interactivity-api | 335 | data-wp-* directives, stores and viewScriptModule integration |
| wp-playground | 325 | disposable in-browser or local WordPress instances |
| wp-rest-api | 322 | REST routes, controllers, schema and permission callbacks |
| wp-abilities-api | 307 | the WordPress Abilities API for capability-based permissions |

All 13 indexed listings clear the 50-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

An agent that writes WordPress code without these skills reliably emits the patterns this suite exists to correct: pre-Gutenberg plugin APIs, unsafe data handling, and block updates that break saved content because deprecations were skipped. The highest-value skills for a builder are wordpress-router, which prevents the agent from guessing what kind of repository it is looking at, and wp-plugin-development, which carries the hooks, activation lifecycle and security rules (nonces, capabilities, sanitization and escaping) that plugin code depends on. wp-block-development and wp-block-themes encode the current Gutenberg and block-theme APIs that stock models lag behind, and wp-wpcli-and-ops keeps destructive operations such as search-replace behind a safe procedure. For an operator the practical move is to install the whole suite once and let wordpress-router dispatch, since the skills are plain markdown that only loads when the agent reads them.

## Usage

| You say | What happens |
|---|---|
| Install Automattic agent skills | Clones, builds and installs the skills to the assistant's skills directory |
| What kind of WordPress repo is this? | Runs wordpress-router to classify the repo and pick the right workflow |
| Add a settings page to my plugin | Routes to wp-plugin-development for the Settings API and hooks pattern |
| My block breaks after an update | Uses wp-block-development to write a deprecation migration |
| Fix this WP-CLI search-replace | Applies the wp-wpcli-and-ops safe search-replace procedure |
| Why is this endpoint slow? | Uses wp-performance for profiling, caching and query optimization |
| Spin up a throwaway WordPress site | Uses wp-playground for a disposable in-browser instance |

## Verification

Confirm the archived repository README and the move notice resolve on the trunk branch:

```bash
curl -sL https://raw.githubusercontent.com/automattic/agent-skills/trunk/README.md | head -30
```

Confirm the routing skill body is present before relying on it for repository classification:

```bash
curl -sL https://raw.githubusercontent.com/automattic/agent-skills/trunk/skills/wordpress-router/SKILL.md | head -30
```

Confirm the plugin development skill body is present before using it as a plugin authoring reference:

```bash
curl -sL https://raw.githubusercontent.com/automattic/agent-skills/trunk/skills/wp-plugin-development/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| wp-plugin-development | Pass | Pass | Pass |
| wp-block-themes | Pass | Pass | Pass |
| wp-wpcli-and-ops | Pass | Pass | Pass |
| wp-block-development | Pass | Pass | Pass |
| wordpress-router | Pass | Pass | Pass |
| wp-performance | Pass | Pass | Pass |
| wp-phpstan | Pass | Pass | Pass |
| wp-project-triage | Pass | Pass | Pass |
| wpds | Pass | Pass | Pass |
| wp-interactivity-api | Pass | Pass | Pass |
| wp-playground | Pass | Pass | Pass |
| wp-rest-api | Pass | Pass | Pass |
| wp-abilities-api | Pass | Pass | Pass |

The sample is fully clean: all 13 indexed listings carry Pass in every cell, with no Warn or Fail and no unverified listings.

## Limitations

- Snapshot data, verified Nov 23, 2026: 5,344 combined installs across 13 indexed listings; 211 GitHub stars; no LICENSE file; last pushed Feb 1, 2026. Counts drift over time.
- The repository is archived and has moved to WordPress/agent-skills; this snapshot captures the Automattic-era code that no longer receives updates.
- GitHub reports no LICENSE file at the repository root, while the README's License section reads MIT, so there is no enforceable grant at the root path.
- The README's two install blocks clone inconsistent URLs: the global block clones WordPress/agent-skills and the project block clones Automattic/agent-skills.
- Install counts sit in a flat band from 307 to 551 across all 13 listings, so no single skill dominates the suite.

## Related

- [WordPress Agent Skills - Official WP Development Setup](/hermes/skills/catalog/wordpress-agent-skills-setup)
- [WooCommerce Agent Skills - Store Development](/hermes/skills/catalog/woocommerce-agent-skills-setup)
- [Addy Osmani - Production-Grade Agent Skills for Hermes](/hermes/skills/catalog/addyosmani-agent-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Treat this repository as a frozen reference: the active fork is WordPress/agent-skills, so pin any new work to that repository instead.
- Install the whole suite and let wordpress-router dispatch; the skills are plain markdown and cost nothing until the agent reads them.
- Run wp-project-triage first on an unfamiliar repository to get the JSON report of tooling, tests and versions before editing.
- Keep the safe search-replace and nonce/capability rules from wp-wpcli-and-ops and wp-plugin-development in front of any destructive or user-facing operation.
- Note the README targets WordPress 6.9+ and PHP 7.2.24+, so older sites may need the deprecated-pattern guidance rather than the current APIs.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
