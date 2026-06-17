---
title: June 11, 2026 — Update (19 New Skills)
description: 19 additional Hermes-relevant skills discovered in afternoon sweep. Agent architecture, UI dashboards, Nous variants, and OpenClaw ecosystem.
---

# June 11, 2026 — Update: 19 New Skills

Afternoon sweep of [skills.sh](https://skills.sh) found **19 additional skills** not in the morning discovery. Covers new Hermes agent architecture patterns, UI dashboards, Nous Research official variants, and OpenClaw ecosystem tools.

*Previously cataloged in morning sweep: aradotso/hermes-skills (20), membranedev/application-skills (10), nousresearch/hermes-agent (2), community standalone (5), aradotso/trending-skills (1).*

---

## aradotso/hermes-skills — 11 new skills

The community collection grew to **31 skills** (up from 20). New entries focus on agent architecture, context management, IDE integration, and the OpenClaw ecosystem.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `aradotso/hermes-skills@awesome-openclaw-skills` | 152 | Curated OpenClaw skill ecosystem map |
| `aradotso/hermes-skills@awesome-openclaw-usecases-discovery` | 146 | OpenClaw use-case discovery patterns |
| `aradotso/hermes-skills@hermes-control-interface-dashboard` | 120 | Agent control interface with visual dashboard |
| `aradotso/hermes-skills@hermes-war-room-ui` | 103 | Multi-agent war room for coordination |
| `aradotso/hermes-skills@hermes-agent-architecture` | 102 | Agent system architecture patterns |
| `aradotso/hermes-skills@hermes-lcm-context-management` | 101 | Lifecycle context management for long-running agents |
| `aradotso/hermes-skills@hermes-agent-guide` | 98 | Getting-started guide for new Hermes users |
| `aradotso/hermes-skills@hermes-kanban-obsidian-integration` | 92 | Kanban board sync with Obsidian vaults |
| `aradotso/hermes-skills@hermes-skins-customization` | 88 | UI theming and skin customization |
| `aradotso/hermes-skills@hermes-edu-skills` | 87 | Educational content and tutorial generation |
| `aradotso/hermes-skills@hermes-ide-terminal` | 85 | IDE-embedded terminal integration for Hermes |

**Setup:**

```bash
# Core architecture + context management
npx skills add aradotso/hermes-skills@hermes-agent-architecture
npx skills add aradotso/hermes-skills@hermes-lcm-context-management

# UI & dashboards
npx skills add aradotso/hermes-skills@hermes-control-interface-dashboard
npx skills add aradotso/hermes-skills@hermes-war-room-ui

# OpenClaw ecosystem
npx skills add aradotso/hermes-skills@awesome-openclaw-skills
npx skills add aradotso/hermes-skills@awesome-openclaw-usecases-discovery

# Productivity & education
npx skills add aradotso/hermes-skills@hermes-kanban-obsidian-integration
npx skills add aradotso/hermes-skills@hermes-edu-skills

# IDE & customization
npx skills add aradotso/hermes-skills@hermes-ide-terminal
npx skills add aradotso/hermes-skills@hermes-skins-customization

# Getting started
npx skills add aradotso/hermes-skills@hermes-agent-guide
```

---

## nousresearch/hermes-agent — 6 new official variants

Official Nous Research variants grew from 9 → 15. New skills cover Jupyter integration, design tools, container supervision, and skill authoring.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `nousresearch/hermes-agent@jupyter-live-kernel` | 152 | Jupyter notebook live kernel for Hermes |
| `nousresearch/hermes-agent@claude-design` | 150 | Design generation via Claude integration |
| `nousresearch/hermes-agent@excalidraw` | 144 | Excalidraw diagram generation from Hermes |
| `nousresearch/hermes-agent@architecture-diagram` | 141 | Architecture diagram generation (C4, UML) |
| `nousresearch/hermes-agent@hermes-agent-skill-authoring` | 123 | Create and publish custom Hermes skills |
| `nousresearch/hermes-agent@hermes-s6-container-supervision` | 74 | S6 overlay container supervision for Hermes |

**Setup:**

```bash
# Development & data science
npx skills add nousresearch/hermes-agent@jupyter-live-kernel

# Design & diagrams
npx skills add nousresearch/hermes-agent@claude-design
npx skills add nousresearch/hermes-agent@excalidraw
npx skills add nousresearch/hermes-agent@architecture-diagram

# Skill development
npx skills add nousresearch/hermes-agent@hermes-agent-skill-authoring
# Requires: Hermes Agent CLI + GitHub token for publishing

# Container ops
npx skills add nousresearch/hermes-agent@hermes-s6-container-supervision
# Requires: Docker + s6-overlay installed on host
```

---

## aradotso/ai-agent-skills — 2 skills (cross-listed)

Mirror repository with alternative Hermes agent framework and self-evolution skills.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `aradotso/ai-agent-skills@hermes-agent-framework` | 142 | Base framework for Hermes agents (mirror) |
| `aradotso/ai-agent-skills@hermes-agent-self-evolution` | 126 | Self-improvement loops (mirror) |

**Setup:**

```bash
npx skills add aradotso/ai-agent-skills@hermes-agent-framework
npx skills add aradotso/ai-agent-skills@hermes-agent-self-evolution
# Note: These are mirrors of the primary aradotso/hermes-skills versions.
# Use the primary versions unless you need specific patches from this fork.
```

---

## Summary

| Repository | New Skills | Total Cataloged | Category |
|-----------|:---------:|:---------------:|----------|
| aradotso/hermes-skills | 11 | 31 | Hermes Ecosystem |
| nousresearch/hermes-agent | 6 | 15 | Official Variants |
| aradotso/ai-agent-skills | 2 | 2 | Mirror/Fork |
| **Total New** | **19** | — | — |

**Combined June 11 total:** 38 (morning) + 19 (update) = **57 new skills discovered today.**

All skills installable via `npx skills add <owner/repo>@<skill>`. No additional configuration required beyond Hermes agent's existing tool access.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
