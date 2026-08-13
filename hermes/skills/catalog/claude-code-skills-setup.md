---
title: Claude Code Skills — Agentic Coding & Skill Development for Hermes Agents
description: Anthropic's official Claude Code skills — build, extend, and customize coding agents. 73K+ combined installs across 6+ skills for agent development, skill creation, and plugin authoring.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-code-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Claude Code Skills — Setup Guide

**Source:** [anthropics/claude-code](https://skills.sh/anthropics/claude-code) (73K+ combined installs)
**GitHub:** [anthropics/claude-code](https://github.com/anthropics/claude-code) (139K+ ⭐)
**Category:** Agent Infrastructure / Coding Agents
**Quality Tier:** 🟢 Production

Claude Code is Anthropic's agentic coding tool that lives in your terminal. It understands your codebase, executes multi-step development tasks, and can be extended with custom skills, plugins, and hooks. These skills help Hermes agents build, develop, and customize their own Claude Code extensions — from creating new skills to writing hook rules and managing plugin structures.

---

## Installation

```bash
# Core skill development
npx skills add anthropics/claude-code --skill agent-development
npx skills add anthropics/claude-code --skill skill-development

# Plugin + hook authoring
npx skills add anthropics/claude-code --skill plugin-structure
npx skills add anthropics/claude-code --skill plugin-settings
npx skills add anthropics/claude-code --skill writing-hookify-rules

# Model migration
npx skills add anthropics/claude-code --skill claude-opus-4-5-migration
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **agent-development** | 16.3K | Build and customize Claude Code agents — system prompts, tool configuration, agent loops |
| **skill-development** | 15.9K | Create custom skills for Claude Code with YAML frontmatter, inline instructions, and testing |
| **plugin-structure** | 11.0K | Author Claude Code plugins — directory layout, manifest files, hook registration |
| **plugin-settings** | 10.9K | Configure plugin settings schema, user preferences, and environment overrides |
| **writing-hookify-rules** | 10.5K | Write hook rules for code transformation, linting, and automated refactoring |
| **claude-opus-4-5-migration** | 9.2K | Migration guide for Opus 4→4.5 model updates in agent configurations |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Claude Code CLI** | `npm install -g @anthropic-ai/claude-code` (or `npx @anthropic-ai/claude-code`) |
| **Anthropic API key** | Required for Claude Code agent usage |
| **Node.js 18+** | Required for Claude Code runtime |

---

## Key Capabilities

### Agent Development
Build production coding agents that understand your codebase, execute multi-file changes, run tests, and integrate with git workflows. Includes system prompt engineering, tool authorization patterns, and agent lifecycle management.

### Skill Development
Create reusable skills with YAML frontmatter (`name`, `description`, `trigger`) and markdown instructions. Skills are Claude Code's extension mechanism — they teach the agent domain-specific workflows, conventions, and tool patterns.

### Plugin Authoring
Structure plugins with manifests, hook registrations, and settings schemas. Plugins extend Claude Code with custom commands, MCP server integrations, and project-specific automation.

### Hookify Rules
Define code transformation rules that Claude Code applies during code generation and refactoring sessions. Supports pattern matching, AST-aware transformations, and project-specific linting.

---

## Quick Start

```bash
# 1. Install Claude Code (if not already)
npm install -g @anthropic-ai/claude-code

# 2. Add the agent-development skill
npx skills add anthropics/claude-code --skill agent-development

# 3. Use the skill in Claude Code
claude "Using the agent-development skill, help me build a code review agent"

# 4. Create your first custom skill
npx skills add anthropics/claude-code --skill skill-development
claude "Using the skill-development skill, create a new skill for running pytest suites"
```

---

## Verification

```bash
# Check installed Claude Code skills
npx skills list | grep anthropics/claude-code

# Verify Claude Code can see the skills
claude --version
claude "list available skills" | grep -i claude-code
```

---

## Notes

- Claude Code is distinct from the `anthropics/skills` catalog (700K+ installs for frontend-design, skill-creator, etc.) — that repo focuses on general-purpose agent skills rather than Claude Code extensibility
- These skills are most valuable when building custom Hermes sub-agents that use Claude Code for implementation
- Plugin skills work with Claude Code's hooks system (Starter, PostToolUse, Stop, etc.)
- For Hermes agents: use `agent-development` and `skill-development` to extend your coding capabilities without leaving the terminal
