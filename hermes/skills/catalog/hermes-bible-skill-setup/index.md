---
title: Hermes Bible Skill Setup
description: Install and configure the Hermes Bible community knowledge base  --  169 pages of unofficial docs, 25+ real-world flows, SOUL.md patterns, and intent-based routing
---

# Hermes Bible Skill Setup

**Skill:** hermes-bible
**Source:** [DeployFaith/hermes-bible-skill](https://github.com/DeployFaith/hermes-bible-skill)
**Author:** iamlukethedev ([hermesbible.com](https://www.hermesbible.com))
**Stars:** 4 ⭐ | **License:** MIT | **Created:** June 21, 2026

## 1. What It Is

The largest community-built Hermes Agent knowledge base outside the official docs. 169 pages distilled into a single loadable skill with embedded routing tables, 26 real-world flow catalogs, 8 hidden features, SOUL.md templates, and delegation/cron/kanban patterns.

**What it covers:**
- 25+ real-world Hermes workflows with intent-based routing
- SOUL.md templates and operating contracts
- Delegation patterns (subagent spawning, task routing)
- Kanban board concepts for agent task management
- Cron job patterns for autonomous overnight operation
- 8 community-sourced hidden Hermes features
- Full documentation index at hermesbible.com

**What it does NOT replace:**
- Official Hermes CLI docs (`hermes --help`, `hermes-agent` skill)
- Nous Research documentation (hermes-agent.nousresearch.com/docs)
- Live `hermes` CLI output (always authoritative over cached skill content)

## 2. Prerequisites

- Hermes Agent installed (any version supporting skills)
- Git (for recommended install) or `hermes skills install` (for light install)
- Disk space: ~30KB for skill + references

## 3. Installation

### Recommended: Full Install (SKILL.md + References)

This preserves linked `references/` files so agents can access patterns, flows, and hidden features:

```bash
git clone https://github.com/DeployFaith/hermes-bible-skill.git
cd hermes-bible-skill
mkdir -p ~/.hermes/skills/hermes-bible
cp -r SKILL.md references ~/.hermes/skills/hermes-bible/
```

**For a named Hermes profile (e.g., corpusiq):**

```bash
PROFILE=corpusiq
mkdir -p ~/.hermes/profiles/$PROFILE/skills/hermes-bible
cp -r SKILL.md references ~/.hermes/profiles/$PROFILE/skills/hermes-bible/
```

Restart Hermes or run `/reload-skills` in an interactive surface.

### Light Install: SKILL.md Only

```bash
hermes skills install https://raw.githubusercontent.com/DeployFaith/hermes-bible-skill/main/SKILL.md
```

**⚠️ Light mode caveat:** Reference files (`references/patterns.md`, `references/flows-catalog.md`, `references/hidden-features.md`) are NOT included. The agent can still answer from embedded routing tables and fetch live content from `llms.txt` when tools permit. For offline/air-gapped use, prefer the full install.

### Optional: Install the Complete Bundle

Adds a `/hermes-complete` slash command that loads both `hermes-agent` and `hermes-bible`:

```bash
mkdir -p ~/.hermes/skill-bundles
cp bundles/hermes-complete.yaml ~/.hermes/skill-bundles/
hermes bundles reload
```

## 4. Capabilities

| Capability | Trigger Keywords | What Agent Gets |
|-----------|-----------------|-----------------|
| Hidden Features | "hidden features", "hermes tricks" | 8 community-sourced features not in official docs |
| Real-World Flows | "how do other people", "hermes workflows", "hermes flows" | 26 flows with intent-based routing |
| SOUL.md Patterns | "SOUL.md template", "operating contract" | Templates and pattern catalog |
| Delegation Patterns | "delegation patterns", "subagent" | Best practices for spawning subagents |
| Kanban Concepts | "hermes kanban", "task board" | Kanban board patterns for Hermes |
| Cron Patterns | "hermes overnight", "autonomous" | Cron job patterns for autonomous ops |
| Documentation Index | "hermes bible", "community knowledge" | Full 169-page index with URLs |

## 5. CLI Reference

After installation, Hermes loads the skill automatically when triggers match. No CLI commands.

For the bundle:
```bash
hermes bundles list                    # Confirm hermes-complete is loaded
/hermes-complete                       # In interactive surface: load both skills
```

## 6. CorpusIQ Use Cases

**Profile-specific install for the CorpusIQ agent:**

```bash
cd /tmp
git clone https://github.com/DeployFaith/hermes-bible-skill.git
mkdir -p ~/.hermes/profiles/corpusiq/skills/hermes-bible
cp -r hermes-bible-skill/SKILL.md hermes-bible-skill/references ~/.hermes/profiles/corpusiq/skills/hermes-bible/
```

**When the CorpusIQ agent should use this skill:**
- Researching community patterns for autonomous agent design
- Auditing SOUL.md patterns against the CorpusIQ profile structure
- Discovering hidden features that could improve CorpusIQ's agent infrastructure
- Cross-referencing workflows against CorpusIQ's own cron/canon patterns

**When NOT to use:**
- For official Hermes CLI commands  --  use `hermes --help` or `hermes-agent` skill
- For CorpusIQ-specific product decisions  --  use `corpusiq-fundamentals` skill

## 7. Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Skill not loading | Hermes didn't scan the new directory | Restart Hermes or `/reload-skills` |
| References 404 | Light install  --  references/ not copied | Reinstall with clone+copy method |
| Conflicting with hermes-agent | Both skills loaded, Bible is secondary | Bible defers to official docs by design |
| Outdated content | Community KB ages | Bible links to live `llms.txt` for freshness |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
