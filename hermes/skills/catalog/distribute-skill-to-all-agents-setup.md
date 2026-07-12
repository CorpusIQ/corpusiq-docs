---
title: distribute-skill-to-all-agents — Full Setup Guide for Hermes Agents
description: Install, configure, and use the distribute-skill-to-all-agents skill from davidondrej/skills. Sync a skill across Codex, Claude Code, Pi, and Hermes agent folders so all agents see it.
---

# distribute-skill-to-all-agents — Setup Guide

**Source:** [davidondrej/skills](https://skills.sh/davidondrej/skills) (59 installs)
**Category:** Agent Infrastructure / Skill Management

Sync a skill across the 4 agent skill folders (Codex, Claude Code, Pi, Hermes) so all agents discover it. Handles the symlink layout for `.claude` and `.pi` and copies only to the independent `.hermes` directory.

---

## Installation

```bash
npx skills add davidondrej/skills --skill distribute-skill-to-all-agents
```

The skill lives inside the `skill-authoring` category of davidondrej/skills alongside `effective-agent-skills`, `folder-specific-claude-and-agents-md`, and `push-skill-to-github`.

---

## Prerequisites

| Requirement | Details |
|---|---|
| **4 agent skill folders** | `~/.agents/skills/`, `~/.claude/skills/`, `~/.pi/agent/skills/`, `~/.hermes/skills/` must exist |
| **Symlink for Claude** | `~/.claude/skills` should be a symlink to `~/.agents/skills` (auto-covers Claude) |
| **Symlink for Pi** | `~/.pi/agent/skills` should be a symlink to `~/.agents/skills` (auto-covers Pi) |
| **Hermes standalone** | `~/.hermes/skills/` is independent — manual copy required |

---

## Key Capabilities

### Core Features

| Capability | How to Trigger | Notes |
|---|---|---|
| **Distribute a skill** | "Distribute this skill across all agents" | Copies from `~/.agents/skills/` to `~/.hermes/skills/` only; Claude and Pi are symlink-covered |
| **Verify distribution** | "Verify all agents have the skill" | Byte-count check across all 4 locations |
| **Check symlink integrity** | "Check agent symlinks" | Verifies `.claude` and `.pi` are symlinks, not diverged copies |

### CLI Command Reference

```bash
# Verify symlinks are intact (one-time check)
ls -la ~/.claude/skills
# Expect: ~/.claude/skills -> ~/.agents/skills

# Copy a skill to Hermes only
SKILL=<skill-name>
cp -r ~/.agents/skills/$SKILL ~/.hermes/skills/

# Verify all 4 locations show identical byte counts
for p in ~/.agents/skills/$SKILL ~/.claude/skills/$SKILL ~/.pi/agent/skills/$SKILL ~/.hermes/skills/$SKILL; do
  echo "$p: $(wc -c < $p/SKILL.md) bytes"
done
```

---

## The 4 Canonical Locations

| Agent | Skills Folder | Notes |
|---|---|---|
| Codex / OpenAI Agents | `~/.agents/skills/` | **Canonical** — author skills here first |
| Claude Code | `~/.claude/skills/` | **Symlink → `~/.agents/skills/`** — writing to `.agents/skills` automatically covers Claude |
| Pi Agent | `~/.pi/agent/skills/` | **Symlink → `~/.agents/skills/`** — auto-covered. (Path is `/agent/` nested — NOT `~/.pi/skills/`) |
| Hermes Agent | `~/.hermes/skills/` | **Independent copy** — the only one needing a manual copy |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Multi-agent skill sync** | After creating a new Hermes skill, run distribution to ensure Codex, Claude Code, Pi, and Hermes all have it |
| **Skill consistency audit** | Verify byte counts match across all 4 agent locations before deployment |
| **Symlink health check** | Detect broken or diverged symlinks that would cause skill drift between agents |
| **Onboarding new agents** | When adding a 5th agent to the stack, adapt the distribution pattern for the new skill folder |
| **Skill version rollback** | Copy a known-good SKILL.md to canonical location, then redistribute to all agents |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| `.claude/skills` is a real directory, not a symlink | The user has diverged copies — ask before touching. Compare contents to decide which is canonical |
| Byte counts don't match after copy | Check for trailing whitespace, different line endings, or file permissions. Re-copy with `cp -a` |
| `.pi/agent/skills` symlink broken | Recreate: `ln -sf ~/.agents/skills ~/.pi/agent/skills` (ensure `~/.pi/agent/` exists) |
| Skill not showing in Hermes | Verify the SKILL.md file is directly in `~/.hermes/skills/<skill-name>/SKILL.md`, not nested deeper |

## Verification

```bash
# Verify the 4 agent skill locations exist
for p in ~/.agents/skills ~/.claude/skills ~/.pi/agent/skills ~/.hermes/skills; do
  [ -d "$p" ] && echo "OK: $p" || echo "MISSING: $p"
done

# Verify symlinks (Claude and Pi should be symlinks to .agents)
ls -la ~/.claude/skills ~/.pi/agent/skills | grep "^l"
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Discovery Page](/hermes/skills/marketplace/new-july12-2026/) →*
*Powered by CorpusIQ*
