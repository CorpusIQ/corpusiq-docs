---
title: Hermes Advanced Memory  --  Setup Guide
description: Workspace rules and memory management for Hermes AI agents  --  structured AGENTS.md index, project folders, SOUL.md principles.
author: salt-vrn (Leonid Zolotarev, NeiroHost.ru)
repo: https://github.com/salt-vrn/hermes-advanced-memory
license: MIT
---

# Hermes Advanced Memory Setup

**A Hermes Agent skill that enforces structured workspace memory.** Replaces scattered files and chaotic `MEMORY.md` entries with an organized workspace  --  `AGENTS.md` index, project folders with `README.md`, and `SOUL.md` for persistent principles.

## Quick Install

```bash
# Via Hermes CLI
hermes skill install salt-vrn/hermes-advanced-memory

# Manual
cd ~/.hermes/skills/
git clone https://github.com/salt-vrn/hermes-advanced-memory.git
```

## What It Creates

```
~/.hermes/
├── SOUL.md              ← identity + rules (including workspace rules)
├── workspace/
│   ├── AGENTS.md        ← index  --  loaded every session, TOC for all memory
│   ├── project-alpha/
│   │   └── README.md
│   ├── project-beta/
│   │   └── README.md
│   └── ...
└── ...
```

## Key Rules Enforced

1. **Workspace is the only working folder.** All agent files go into `workspace/`.
2. **AGENTS.md is the index.** Loaded at every session start. Without an index entry, a file is invisible to the agent.
3. **Small topics → AGENTS.md entry.** Major projects → separate folder + `README.md`.
4. **SOUL.md is the source of truth.** Workspace rules, key principles, and identity live there  --  not just in the skill file.

## Usage

### For a New Agent
1. Agent reads the skill
2. Asks user to confirm profile (never guesses)
3. Creates `workspace/` in profile root
4. Creates `AGENTS.md`  --  empty index
5. Moves working files into `workspace/`
6. Opens existing `SOUL.md` and adds key principles
7. Describes the new structure to the user

### For an Existing Agent
If memory is not organized, apply the skill, move scattered files into `workspace/`, and update the index.

## Why This Matters

Without a memory system, Hermes agents store data chaotically  --  files scattered across `~/.hermes/`, `MEMORY.md` filled with garbage, crucial facts forgotten across sessions. This skill solves that by enforcing a structure that:

- **Prevents context loss**  --  `AGENTS.md` is the single source of truth, loaded every session
- **Scales with projects**  --  new project = new folder + README, never a cluttered flat directory
- **Survives restarts**  --  `SOUL.md` preserves key principles across sessions and model changes
- **Self-documents**  --  the structure itself tells the agent where everything lives

## Production Notes

- **NeiroHost** uses this in production AI-agent hosting alongside `hermes-session-maintenance` and `openclaw-to-hermes-migration`
- The skill is bilingual (English + Russian README)
- MIT licensed, 8 commits as of June 2026

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Session Maintenance Setup →](/hermes/skills/catalog/hermes-session-maintenance-setup/)*
*Powered by CorpusIQ*
