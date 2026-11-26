---
title: "Drupal AI - Drupal 11 Toolkit Setup"
description: "edutrul/drupal-ai - 2.1K combined installs: a Drupal 11 AI toolkit with skills, agents, rules, hooks, and commands for Claude Code and Codex."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/drupal-ai-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "drupal", "claude code", "codex"]
---

# Drupal AI - Setup Guide

**Source:** [edutrul/drupal-ai](https://www.skills.sh/edutrul/drupal-ai) via skills.sh - 2.1K combined installs across 35 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [edutrul/drupal-ai](https://github.com/edutrul/drupal-ai) - 75 stars, MIT license, last pushed Jun 5, 2026, main branch; 35 skills under .claude/skills/<name>/SKILL.md plus 10 subagents, 8 slash commands, and 8 rules.
**Category:** Drupal 11 Development (Claude Code / Codex)
**Quality Tier:** 🟡 Yellow - 12 of 35 listings sampled: eleven pass all three checks, and drupal-contrib-mgmt carries Socket and Snyk Warns.

edutrul/drupal-ai is a production-tested AI toolkit for Drupal 11 development, compatible with Claude Code, Codex, Cursor, and GitHub Copilot. Beyond 35 skills it ships 10 subagents, 8 slash commands, 8 always-loaded rules, 2 session hooks, and a settings file with Drupal-safe permissions. It is used on a real Drupal 11 / DDEV / Acquia Cloud project, and the .claude/ folder is project-agnostic so it drops into any Drupal project.

Unlike a pure skills collection, the skills live under .claude/skills/ rather than skills/, and the repo is shaped as a full project configuration. Install counts sit in a flat band from 56 to 72 across all 35 listings.

## Installation

The README documents a copy-based setup rather than a skills-CLI command. Copy the .claude/ folder into your project:

```bash
cp -r /path/to/this-repo/.claude /path/to/your-project/.claude
```

Then generate CLAUDE.md (Claude Code) or AGENTS.md (Codex) from the CLAUDE.example.md and AGENTS.example.md references, for example by pasting the README's interview prompt into your AI tool. Copy .claude/data/mappings.example.json to mappings.json for GitHub-to-Jira team mappings, review .claude/settings.json permissions, and edit .claude/rules/workflow.md for branch and commit conventions. Codex users can symlink .claude/skills into .codex/skills (see .codex/README.md).

## What It Provides

skills.sh publishes per-skill install counts for all 35 indexed listings. The 9 most-installed skills are listed below; the remaining 26 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| drupal-htmx | 72 | HTMX in Drupal 11.3+ core: fluent builder, swapOob, partial routes, and Drupal.behaviors |
| drupal-caching | 67 | Cache API: cache tags, contexts, max-age, bins, and invalidation |
| drupal-taxonomy | 64 | taxonomy terms, vocabularies, hierarchy, and reference fields |
| drupal-entity-api | 64 | load, create, update, and delete entities via entity_type.manager |
| drupal-services | 63 | services and dependency injection for controllers, forms, and plugins |
| drupal-queries | 63 | database queries via the abstraction layer; never concatenate SQL |
| drupal-plugins | 63 | Block, Field, Condition, and Filter plugins with PHP attributes |
| drupal-drush | 63 | Drush commands for cache, config, modules, generators, and scaffolding |
| drupal-contrib-mgmt | 63 | contrib module upgrade triage: patches, Drupal 11 compatibility, upgrade_status |

The remaining 26 indexed listings range from 56 to 62 installs.

## Why This Matters for Hermes Agents

This is a complete, opinionated Drupal 11 operating environment rather than a loose skill bag, which is its real value for an agent: the rules and settings encode the conventions (Drupal-style docblocks, DI-first, phpcs.xml as source of truth, DTT ExistingSite-only testing) so an agent produces project-consistent code without being re-briefed. The 35 skills are a reference layer for the Drupal API surface, and the 10 subagents (drupal-backend-dev, drupal-reviewer, drupal-test-writer, and the rest) plus slash commands give a multi-agent host ready delegation targets and a review loop. The hooks re-establish context on session start and resume, and the settings file prompts before destructive operations like drush cim and drush sql-drop. The trade-off is setup: this is a project scaffold, not a one-line install, and the install band is flat because one project install pulls the whole toolkit.

## Usage

| You say | What happens |
|---|---|
| Add interactive UI without reloads | Uses drupal-htmx for the HTMX fluent builder and partial routes |
| Cache this render array | Uses drupal-caching for cache tags, contexts, and max-age |
| Wire a service into this plugin | Uses drupal-services for dependency injection via ContainerFactoryPluginInterface |
| Query the database safely | Uses drupal-queries for the database abstraction layer with no SQL concatenation |
| Build a Drush command | Uses drupal-drush for generators and non-interactive scaffolding |
| Upgrade a contrib module | Uses drupal-contrib-mgmt for issue queue research, patches, and D11 checks |
| Review this branch before merge | Uses the /code-review or /security-audit slash commands |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/edutrul/drupal-ai/main/README.md | head -60
curl -sL https://raw.githubusercontent.com/edutrul/drupal-ai/main/.claude/skills/drupal-htmx/SKILL.md | head -40
```

Both URLs return 200. After installing, review each .claude/skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warn verdicts noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| drupal-htmx | Pass | Pass | Pass |
| drupal-caching | Pass | Pass | Pass |
| drupal-taxonomy | Pass | Pass | Pass |
| drupal-entity-api | Pass | Pass | Pass |
| drupal-services | Pass | Pass | Pass |
| drupal-queries | Pass | Pass | Pass |
| drupal-plugins | Pass | Pass | Pass |
| drupal-drush | Pass | Pass | Pass |
| drupal-contrib-mgmt | Pass | Warn | Warn |
| drupal-javascript | Pass | Pass | Pass |
| drupal-hooks | Pass | Pass | Pass |
| drupal-access | Pass | Pass | Pass |

Across the 12 sampled skills there are 34 Pass, 2 Warn, and 0 Fail cells. Eleven skills pass all three checks; drupal-contrib-mgmt carries the two Warns (Socket and Snyk).

## Limitations

- Snapshot data, verified Nov 26, 2026: 2,129 combined installs across 35 indexed listings; 75 GitHub stars; MIT license; last pushed Jun 5, 2026. Counts drift over time.
- Installs sit in a flat band from 56 to 72 across all 35 listings, so the most-installed table reflects only a few installs of difference, not a long tail of popularity.
- skills.sh sampled only 12 of the 35 indexed listings; the other 23 carry no published verdict.
- Skills live under .claude/skills/ rather than skills/, so paths differ from the agentskills.io convention most repos use.
- This is a project scaffold, not a one-line install: it needs the CLAUDE.example.md/AGENTS.example.md and mappings setup steps before it is useful on a new project.
- The repo last pushed Jun 5, 2026, several months before this sweep; its Drupal 11 focus may lag newer core releases.

## Related

[WordPress Agent Skills - Audit and Optimize Setup](/hermes/skills/catalog/agent-skills-wordpress-setup) | [Drupal Canvas Skills - Code Components Setup](/hermes/skills/catalog/drupal-canvas-skills-setup) | [Drupal Claude Skills - Drupal Development Setup](/hermes/skills/catalog/drupal-claude-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Generate your CLAUDE.md/AGENTS.md from the example files via the README's interview prompt instead of editing them by hand.
- Run everything inside DDEV (the tooling rule enforces this) and keep the settings permissions block matched to your toolchain.
- Symlink .claude/skills into .codex/skills for Codex use instead of copying.
- Check the hooks' develop-branch assumption if your default branch is main.
- Read drupal-contrib-mgmt's security page first; it carries the sample's only Warns.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
