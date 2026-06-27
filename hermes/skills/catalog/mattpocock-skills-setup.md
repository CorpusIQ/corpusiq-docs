---
title: Matt Pocock TypeScript Developer Toolkit — Setup Guide
description: Install and configure 19 Matt Pocock skills for Hermes Agent — complete TypeScript/React development lifecycle automation with 1.7M+ combined installs. Writing, refactoring, code review, implementation workflows, and decision mapping.
---

# Matt Pocock TypeScript Developer Toolkit

Matt Pocock is the world's leading TypeScript educator (146K GitHub stars). These **19 skills** from [mattpocock/skills](https://skills.sh/mattpocock/skills) bring his proven TypeScript/React development methodology to AI agents. Combined installs: **1,700,000+** across the skills.sh marketplace.

> **June 2026 Update:** Four new skills added — `implement` (implementation workflow), `decision-mapping` (decision frameworks), `writing-great-skills` (skill authoring guide), and `ask-matt` (Q&A helper).

---

## Prerequisites

- Hermes Agent installed and running
- Node.js 18+ with `npx` available
- A TypeScript or React project to work with (optional — skills work on any codebase)

---

## Capabilities

| Area | Skills | What They Do |
|---|---|---|
| **Writing & Authoring** | `write-a-skill`, `edit-article`, `writing-shape`, `writing-fragments`, `writing-beats`, `writing-great-skills` | Technical writing methodology, article editing, narrative structure, skill authoring guide |
| **Code Quality** | `caveman`, `ubiquitous-language`, `setup-pre-commit`, `git-guardrails-claude-code` | Debugging, domain language, pre-commit hooks, git safety |
| **Implementation** | `implement`, `decision-mapping`, `ask-matt` | Implementation workflow, decision frameworks, Q&A helper |
| **Design & Architecture** | `zoom-out`, `design-an-interface`, `request-refactor-plan` | System-level thinking, TypeScript interface design, refactoring |
| **Project Operations** | `scaffold-exercises`, `migrate-to-shoehorn` | Exercise generation, framework migration |

---

## Installation

Install all 19 skills at once:

```bash
# Core writing skills
npx skills add mattpocock/skills --skill write-a-skill
npx skills add mattpocock/skills --skill edit-article
npx skills add mattpocock/skills --skill writing-shape
npx skills add mattpocock/skills --skill writing-fragments
npx skills add mattpocock/skills --skill writing-beats
npx skills add mattpocock/skills --skill writing-great-skills

# Code quality & safety
npx skills add mattpocock/skills --skill caveman
npx skills add mattpocock/skills --skill ubiquitous-language
npx skills add mattpocock/skills --skill setup-pre-commit
npx skills add mattpocock/skills --skill git-guardrails-claude-code

# Implementation & decision support (NEW — June 2026)
npx skills add mattpocock/skills --skill implement
npx skills add mattpocock/skills --skill decision-mapping
npx skills add mattpocock/skills --skill ask-matt

# Design & architecture
npx skills add mattpocock/skills --skill zoom-out
npx skills add mattpocock/skills --skill design-an-interface
npx skills add mattpocock/skills --skill request-refactor-plan

# Project operations
npx skills add mattpocock/skills --skill scaffold-exercises
npx skills add mattpocock/skills --skill migrate-to-shoehorn
```

---

## CLI Reference

All skills are invoked through Hermes Agent's skill system:

```bash
# Write a new skill for Hermes
hermes skill mattpocock/skills/write-a-skill

# Get the big picture before making changes
hermes skill mattpocock/skills/zoom-out

# Debug with caveman approach
hermes skill mattpocock/skills/caveman

# Design a TypeScript interface
hermes skill mattpocock/skills/design-an-interface

# Request a refactoring plan
hermes skill mattpocock/skills/request-refactor-plan

# Edit technical writing
hermes skill mattpocock/skills/edit-article

# Work through implementation (NEW)
hermes skill mattpocock/skills/implement

# Map complex decisions (NEW)
hermes skill mattpocock/skills/decision-mapping

# Get real-time Q&A help (NEW)
hermes skill mattpocock/skills/ask-matt
```

---

## CorpusIQ Use Cases

| Use Case | Skill | Value |
|---|---|---|
| Writing docs pages | `write-a-skill`, `edit-article`, `writing-shape`, `writing-great-skills` | Consistent, high-quality documentation at scale |
| Code review automation | `git-guardrails-claude-code`, `caveman` | Safe AI-assisted code reviews |
| Product architecture | `zoom-out`, `design-an-interface`, `decision-mapping` | System-level thinking before implementation |
| Feature implementation | `implement`, `ask-matt` | Guided implementation workflows with real-time Q&A |
| Onboarding & training | `scaffold-exercises`, `ubiquitous-language` | Generate exercises from existing codebase |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| `npx skills add` not found | Run `npm install -g skills` first |
| Skill not loading in Hermes | Check `hermes skill list` — the skill name must match the install name exactly |
| TypeScript errors after using `design-an-interface` | The skill generates TypeScript interfaces — review before committing |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
