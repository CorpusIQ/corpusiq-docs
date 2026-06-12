---
title: June 13, 2026 — Hermes Agent Ecosystem Expansion (10 new skills)
description: Skills.sh sweep: 10 additional Hermes agent ecosystem skills from aradotso/hermes-skills and nousresearch/hermes-agent — skill authoring, UI dashboards, IDE integration, education, and more.
---

# June 13, 2026 — Hermes Agent Ecosystem Expansion

Sweep of skills.sh discovered **10 new Hermes-specific skills** from `aradotso/hermes-skills` and `nousresearch/hermes-agent` that were not in the existing catalog. These extend the Hermes Agent Ecosystem with skill authoring tooling, additional UI dashboards, IDE integration, Kanban/Obsidian bridge, education skills, and more.

*Previously cataloged: 350 total (89 native + 261 marketplace). This update adds 10 → 360 total.*

---

## nousresearch/hermes-agent — 1 new skill

### hermes-agent-skill-authoring (124 installs) ✍️

Create, test, and publish skills for Hermes Agent from within an agent session. Guides through SKILL.md structure, YAML frontmatter, trigger conditions, and verification steps. The official skill-authoring workflow from Nous Research.

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill hermes-agent-skill-authoring
```

---

## aradotso/hermes-skills — 9 new skills

All install with: `npx skills add aradotso/hermes-skills@<skill-name>`

### hermes-control-interface-dashboard (121 installs) 🎛️

Operator control interface for Hermes agents. Dashboard for monitoring agent status, task queues, resource usage, and manual intervention controls.

**Install:**
```bash
npx skills add aradotso/hermes-skills@hermes-control-interface-dashboard
```

---

### hermes-war-room-ui (104 installs) ⚔️

War room / operations center UI for coordinating multiple Hermes agents during critical incidents or complex multi-agent operations. Real-time status, agent communication channels, and decision tracking.

**Install:**
```bash
npx skills add aradotso/hermes-skills@hermes-war-room-ui
```

---

### hermes-agent-architecture (103 installs) 🏗️

Architecture reference for designing Hermes agent systems. Covers agent topology patterns, communication models, state management strategies, and deployment architectures.

**Install:**
```bash
npx skills add aradotso/hermes-skills@hermes-agent-architecture
```

---

### hermes-lcm-context-management (102 installs) 🧠

Lifecycle context management (LCM) for Hermes agents. Strategies for managing context windows across long-running agent sessions, context compaction, and memory prioritization.

**Install:**
```bash
npx skills add aradotso/hermes-skills@hermes-lcm-context-management
```

---

### hermes-agent-guide (100 installs) 📖

Comprehensive getting-started guide for Hermes Agent. Covers installation, configuration, profile setup, skill management, and first-agent patterns. Ideal onboarding resource.

**Install:**
```bash
npx skills add aradotso/hermes-skills@hermes-agent-guide
```

---

### hermes-kanban-obsidian-integration (93 installs) 📋

Bridge Hermes agent task management with Obsidian kanban boards. Sync agent task lists to Obsidian vaults, track progress visually, and maintain persistent task state.

**Install:**
```bash
npx skills add aradotso/hermes-skills@hermes-kanban-obsidian-integration
```

**Requires:** Obsidian with Kanban plugin

---

### hermes-skins-customization (89 installs) 🎨

Theme and skin customization for Hermes agent interfaces. CSS customization, dark/light themes, brand colors, and layout presets for Hermes dashboards and UIs.

**Install:**
```bash
npx skills add aradotso/hermes-skills@hermes-skins-customization
```

---

### hermes-edu-skills (88 installs) 🎓

Educational skill pack for learning Hermes Agent. Tutorials, exercises, and example projects for mastering Hermes agent development, skill creation, and deployment patterns.

**Install:**
```bash
npx skills add aradotso/hermes-skills@hermes-edu-skills
```

---

### hermes-ide-terminal (86 installs) 💻

IDE and terminal integration for Hermes Agent. Launch Hermes from VS Code, Cursor, Zed, or terminal. Hotkeys, panel integration, and terminal multiplexing support.

**Install:**
```bash
npx skills add aradotso/hermes-skills@hermes-ide-terminal
```

**Requires:** VS Code, Cursor, Zed, or terminal emulator

---

## Summary

| # | Skill | Installs | Source | Category |
|---|-------|----------|--------|----------|
| 1 | `hermes-agent-skill-authoring` | 124 | nousresearch/hermes-agent | Skill Authoring |
| 2 | `hermes-control-interface-dashboard` | 121 | aradotso/hermes-skills | UI/Dashboard |
| 3 | `hermes-war-room-ui` | 104 | aradotso/hermes-skills | UI/Operations |
| 4 | `hermes-agent-architecture` | 103 | aradotso/hermes-skills | Architecture |
| 5 | `hermes-lcm-context-management` | 102 | aradotso/hermes-skills | Context/Memory |
| 6 | `hermes-agent-guide` | 100 | aradotso/hermes-skills | Documentation |
| 7 | `hermes-kanban-obsidian-integration` | 93 | aradotso/hermes-skills | Integration |
| 8 | `hermes-skins-customization` | 89 | aradotso/hermes-skills | UI/Theming |
| 9 | `hermes-edu-skills` | 88 | aradotso/hermes-skills | Education |
| 10 | `hermes-ide-terminal` | 86 | aradotso/hermes-skills | IDE/DevTools |

**New this update:** 10 skills
**Marketplace subtotal before:** 261 → **After:** 271
**Total skills:** 350 → **360**

---

*← [June 12 Afternoon Update](/hermes/skills/marketplace/new-june12-2026-update/) | [Skills Catalog](/hermes/skills/catalog/) →*
*↑ [Marketplace Home](/hermes/skills/marketplace/)*
