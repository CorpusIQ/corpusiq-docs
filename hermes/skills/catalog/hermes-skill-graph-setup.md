---
title: Hermes Skill Graph Setup Guide
description: Install and configure the knowledge-graph skill discovery plugin for Hermes Agent — FTS5 search, typed relationships, and dependency-aware skill management
---

# Hermes Skill Graph — Setup Guide

**Repo:** [nuffin/hermes-skill-graph](https://github.com/nuffin/hermes-skill-graph)
**Created:** June 21, 2026 | **License:** MIT (assumed)

A knowledge-graph layer for Hermes skill discovery. Instead of flat `skills/` directories, skills are nodes in a graph with typed edges representing dependencies, conflicts, synergies, and composition relationships. FTS5 full-text search across all installed skills.

---

## Installation

```bash
git clone https://github.com/nuffin/hermes-skill-graph.git /tmp/hermes-skill-graph
cd /tmp/hermes-skill-graph
./install.sh
```

The installer:
1. Copies the plugin to `~/.hermes/plugins/skill-graph/`
2. Indexes existing skills from `~/.hermes/skills/`
3. Registers as a Hermes plugin

**Manual install:**
```bash
cp -r skill/ ~/.hermes/skills/hermes-skill-graph/
cp -r plugin/ ~/.hermes/plugins/skill-graph/
```

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.16.0+ |
| Python | 3.10+ (for FTS5 indexing) |
| Disk | ~10MB for skill graph database |
| Existing skills | At least 5 installed skills for meaningful graph |

---

## Capabilities

### Search & Discovery

| Capability | Trigger | Output |
|-----------|---------|--------|
| Full-text search | `hermes-skill-graph search "<query>"` | Ranked skills matching query |
| Related skills | `hermes-skill-graph related <skill-name>` | Skills with typed relationships |
| Dependency graph | `hermes-skill-graph deps <skill-name>` | What this skill depends on / what depends on it |
| Conflict detection | `hermes-skill-graph conflicts` | Skill pairs with known conflicts |

### Graph Operations

| Capability | Command |
|-----------|---------|
| Add skill edge | `hermes-skill-graph edge add <skill-a> depends_on <skill-b>` |
| List all edges | `hermes-skill-graph edges` |
| Export graph | `hermes-skill-graph export --format dot > graph.dot` |
| Re-index | `hermes-skill-graph reindex` |

---

## CLI Reference

```bash
# Search for skills by keyword
hermes-skill-graph search "browser automation"

# Find all skills related to a specific skill
hermes-skill-graph related youtube-content

# Show the dependency tree for a skill
hermes-skill-graph deps corpusiq-autonomous-growth-agent

# Check for known skill conflicts
hermes-skill-graph conflicts

# Add a dependency edge
hermes-skill-graph edge add hermes-skill-graph depends_on native-mcp

# Re-index after installing new skills
hermes-skill-graph reindex

# Export the full graph for visualization
hermes-skill-graph export --format dot | dot -Tpng -o skill-graph.png

# Show skill metadata
hermes-skill-graph info hermes-bible-skill
```

---

## CorpusIQ Use Cases

### 1. Skill Audit Before Agent Spawn
Before spawning a new autonomous agent, check the skill graph for conflicts and dependencies:
```bash
hermes-skill-graph conflicts --agent corpusiq
hermes-skill-graph deps corpusiq-autonomous-growth-agent
```
Ensures the agent's skill bundle is internally consistent.

### 2. Discover Complementary Skills
When building a new workflow, find skills that compose well:
```bash
hermes-skill-graph related honcho-integration
# Returns: gbrain-operations, corpusiq-session-handoff, corpusiq-governance-system
```
Surfaces the ecosystem infrastructure skills that work together.

### 3. Skill Gap Analysis
Identify capability gaps in the CorpusIQ skill portfolio:
```bash
hermes-skill-graph search "deployment" --missing
# Returns skills that exist in the community but aren't installed
```

### 4. Dependency Health Monitoring
Track which CorpusIQ skills depend on external skills that may change:
```bash
hermes-skill-graph deps corpusiq-docs-management --direction=out
```
Flags upstream dependencies that need monitoring for breaking changes.

### 5. Onboarding New Agents
Quickly identify the minimal skill set for a new agent role:
```bash
hermes-skill-graph recommend --role "content-ops" --minimal
```

---

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| `install.sh` fails with "plugin directory not found" | Hermes plugin directory doesn't exist | `mkdir -p ~/.hermes/plugins/` |
| Search returns no results | Index not built | Run `hermes-skill-graph reindex` |
| Graph edges missing | Skills installed after initial indexing | Re-index after every skill install |
| FTS5 errors | Python sqlite3 module missing FTS5 | `python3 -c "import sqlite3; print(sqlite3.sqlite_version)"` must be 3.9+ |

### Verification

```bash
# Confirm installation
ls ~/.hermes/skills/hermes-skill-graph/SKILL.md && echo "✓ Skill installed"
ls ~/.hermes/plugins/skill-graph/ && echo "✓ Plugin installed"

# Test search
hermes-skill-graph search "skill" | head -5

# Check graph health
hermes-skill-graph reindex && echo "✓ Index healthy"
```

---

*← [Hermes Skills Catalog](/hermes/skills/catalog/) | [Next: Hermes Bible Skill →](/hermes/skills/catalog/hermes-bible-skill-setup/)*
*↑ [Skills Home](/hermes/skills/)*
