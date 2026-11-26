---
title: "Drupal Claude Skills - Drupal Development Setup"
description: "grasmash/drupal-claude-skills - 3.1K combined installs: Claude Code skills and agents for Drupal config, modules, security, and testing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/drupal-claude-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "drupal", "claude code", "config management"]
---

# Drupal Claude Skills - Setup Guide

**Source:** [grasmash/drupal-claude-skills](https://www.skills.sh/grasmash/drupal-claude-skills) via skills.sh - 3.1K combined installs across 24 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [grasmash/drupal-claude-skills](https://github.com/grasmash/drupal-claude-skills) - 85 stars, MIT license, last pushed Oct 1, 2026, main branch; 24 skill folders under skills/<name>/SKILL.md plus 8 subagents under .claude/agents/.
**Category:** Drupal Development (Claude Code)
**Quality Tier:** 🟡 Yellow - 12 of 24 listings sampled: eleven pass all three checks, and drupal-contrib-mgmt carries Socket and Snyk Warns.

grasmash/drupal-claude-skills is a comprehensive collection of Claude Code skills and subagents for Drupal development, covering configuration management, contrib module updates, security, local DDEV development, OAuth, Search API, and testing. skills.sh carries an empty repository description for this source; the README describes it as "A comprehensive collection of Claude Code skills and agents for Drupal development."

The repo ships 24 skills under skills/<name>/SKILL.md, 8 subagents under .claude/agents/, a sample .claude/settings.json, and two upstream sync scripts. The Drupal Canvas Code Component skills (React/JSX) are maintained upstream in drupal-canvas/skills; this repo only adds the complements that suite does not cover, drupal-canvas-sdc (Twig SDCs) and canvas-contribution (contributing upstream).

## Installation

The README documents four install paths. The quickest for skills only:

```bash
npx skills add grasmash/drupal-claude-skills
```

The one-line shell installer copies skills, agents, and settings together:

```bash
bash <(curl -s https://raw.githubusercontent.com/grasmash/drupal-claude-skills/main/install.sh)
```

The skills-CLI path copies skills into .claude/skills/ but does not install the agents, settings, or the AGENTS.md workflow guide. Manual cloning copies skills/ into .claude/skills/, .claude/agents/ into .claude/agents/, and the settings file, then appends the AGENTS.md workflow guide to CLAUDE.md.

## What It Provides

skills.sh publishes per-skill install counts for all 24 indexed listings. The 9 most-installed skills are listed below; the remaining 15 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| drupal-at-your-fingertips | 392 | Drupal 9-11 core API patterns across services, hooks, events, plugins, entities, forms, routes, Twig, caching, queries, and config |
| drupal-ddev | 384 | DDEV local development: ddev commands, .ddev/config.yaml, database import/export, Drush, Xdebug, Solr, and Mutagen |
| drupal-contrib-mgmt | 279 | manage contrib modules with Composer, composer-patches v2, Drupal 11 compatibility, and drupal.org contributions |
| drupal-search-api | 256 | configure Search API indexes, boost strategies, and custom search processors |
| drupal-config-mgmt | 232 | safe config export/import, Config Split, and syncing config across environments |
| drupal-canvas | 171 | entry point for Drupal Canvas Code Components; routes to the official suite and the Twig SDC complements |
| ivangrynenko-cursorrules-drupal | 171 | OWASP Top 10 security and coding rules from Ivan Grynenko's cursorrules |
| drupal-simple-oauth | 159 | OAuth2 with simple_oauth: scopes, consumers, Bearer tokens, and permission debugging |
| skill-developer | 158 | meta-skill for creating Claude Code skills per the agentskills.io specification |

The remaining 15 indexed listings range from 42 to 132 installs.

## Why This Matters for Hermes Agents

This is a dense, battle-tested reference layer for Drupal module work, so an agent stops guessing at subsystem APIs and reaches for a worked pattern instead. drupal-at-your-fingertips condenses Drupal 9-11 core API patterns across 14 subsystems, and drupal-config-mgmt plus drupal-config-reconcile make config import/export and drift resolution explicit and safe. drupal-contrib-mgmt encodes the Composer patches workflow with relock semantics, and ivangrynenko-cursorrules-drupal turns OWASP Top 10 categories into concrete Drupal code rules. The 8 subagents (quality-gate, done-gate, drupal-specialist, test-writer, and the rest) give a multi-agent host a ready review and completion gate. Two skills sync from upstream sources via scripts, so their content tracks Selwyn Polit's book and Ivan Grynenko's rulesets rather than being frozen in this repo.

## Usage

| You say | What happens |
|---|---|
| Set up partial config splits | Uses drupal-config-mgmt for Config Split setup and activation |
| Update a contrib module | Uses drupal-contrib-mgmt for Composer updates, patches, and Drupal 11 compatibility checks |
| Do a security review | Uses ivangrynenko-cursorrules-drupal for OWASP Top 10 Drupal patterns |
| Debug an OAuth token denial | Uses drupal-simple-oauth for scope/role matching and Bearer token CSRF issues |
| Fix my local DDEV setup | Uses drupal-ddev for ddev commands, database snapshots, and recovery |
| Reconcile config drift before deploy | Uses drupal-config-reconcile to decide import vs export vs skip per item |
| Tune Search API relevance | Uses drupal-search-api for boost strategies and processor patterns |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/grasmash/drupal-claude-skills/main/README.md | head -60
curl -sL https://raw.githubusercontent.com/grasmash/drupal-claude-skills/main/skills/drupal-config-mgmt/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warn verdicts noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| drupal-at-your-fingertips | Pass | Pass | Pass |
| drupal-ddev | Pass | Pass | Pass |
| drupal-contrib-mgmt | Pass | Warn | Warn |
| drupal-search-api | Pass | Pass | Pass |
| drupal-config-mgmt | Pass | Pass | Pass |
| drupal-canvas | Pass | Pass | Pass |
| ivangrynenko-cursorrules-drupal | Pass | Pass | Pass |
| drupal-simple-oauth | Pass | Pass | Pass |
| skill-developer | Pass | Pass | Pass |
| drupal-testing | Pass | Pass | Pass |
| drupal-config-reconcile | Pass | Pass | Pass |
| acquia-source | Pass | Pass | Pass |

Across the 12 sampled skills there are 34 Pass, 2 Warn, and 0 Fail cells. Eleven skills pass all three checks; drupal-contrib-mgmt carries the two Warns (Socket and Snyk).

## Limitations

- Snapshot data, verified Nov 26, 2026: 3,102 combined installs across 24 indexed listings; 85 GitHub stars; MIT license; last pushed Oct 1, 2026. Counts drift over time.
- skills.sh carries an empty repository description for this source; the README supplies its own description instead.
- skills.sh sampled only 12 of the 24 indexed listings; the other 12 carry no published verdict.
- Two skills sync from upstream sources via .claude/scripts/sync-d9book.sh and sync-ivan-rules.sh, so their content tracks external books and rulesets.
- The Drupal Canvas Code Component skills live upstream in drupal-canvas/skills; this repo ships only the Twig SDC and contribution complements, so Canvas Code Component work needs both installed.

## Related

[WordPress Agent Skills - Audit and Optimize Setup](/hermes/skills/catalog/agent-skills-wordpress-setup) | [Drupal Canvas Skills - Code Components Setup](/hermes/skills/catalog/drupal-canvas-skills-setup) | [Drupal AI - Drupal 11 Toolkit Setup](/hermes/skills/catalog/drupal-ai-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the agents and settings too, not just the skills, or the quality-gate and done-gate review workflow will not be available.
- Preview config imports before applying them, following drupal-config-mgmt's import pattern.
- For Canvas Code Component work, install drupal-canvas/skills alongside this repo and use drupal-canvas-sdc only for Twig Single Directory Components.
- Re-run the two sync scripts (.claude/scripts/sync-d9book.sh and sync-ivan-rules.sh) to refresh upstream-derived content.
- The skills-CLI install omits agents and settings; use install.sh for the full setup.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
