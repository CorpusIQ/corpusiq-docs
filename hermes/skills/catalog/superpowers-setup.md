---
title: Superpowers — Agentic Skills Framework & Development Methodology for Hermes Agents
description: Obra's Superpowers framework — the most-installed agent skills system with 1.2M+ combined installs. Brainstorming, systematic debugging, TDD, code review, and planning workflows for AI coding agents.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/superpowers-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Superpowers — Setup Guide

**Source:** [obra/superpowers](https://skills.sh/obra/superpowers) (1.2M+ combined installs)
**GitHub:** [obra/superpowers](https://github.com/obra/superpowers) (261K+ ⭐)
**Category:** Agent Infrastructure / Development Methodology
**Quality Tier:** 🟢 Production

Superpowers is the most widely adopted agentic skills framework — a battle-tested development methodology that turns AI coding agents into systematic, reliable engineering partners. With 1.2M+ combined installs across 15+ skills, it covers the full software development lifecycle: brainstorming, planning, test-driven development, systematic debugging, code review, and more. For Hermes agents, Superpowers provides proven workflows that eliminate guesswork and enforce engineering rigor.

---

## Installation

```bash
# Core workflow skills
npx skills add obra/superpowers --skill brainstorming
npx skills add obra/superpowers --skill writing-plans
npx skills add obra/superpowers --skill using-superpowers

# Development methodology
npx skills add obra/superpowers --skill test-driven-development
npx skills add obra/superpowers --skill systematic-debugging

# Collaboration + quality
npx skills add obra/superpowers --skill requesting-code-review
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **brainstorming** | 294.5K | Structured ideation — explore solutions, evaluate trade-offs, converge on architecture |
| **systematic-debugging** | 199.6K | Root-cause analysis methodology — reproduce, isolate, fix, verify |
| **writing-plans** | 196.8K | Implementation planning — break down features into testable, sequential steps |
| **using-superpowers** | 194.9K | Framework orientation — how to combine and sequence Superpowers skills |
| **requesting-code-review** | 178.7K | Structured review requests — what to include, how to surface design decisions |
| **test-driven-development** | 177.1K | Red-green-refactor workflow — write tests first, implement, verify |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **skills.sh CLI** | `npx skills` (auto-installed) |
| **AI coding agent** | Claude Code, Codex CLI, or any skills.sh-compatible agent |
| **Git** | Required for code review and TDD workflows |

---

## Key Capabilities

### Brainstorming (294.5K installs)
The most-installed agent skill on skills.sh. Guides agents through structured exploration: define the problem, generate candidate solutions, evaluate trade-offs (performance, complexity, maintainability), and converge on an architecture decision. Replaces vague "what should I do?" agent loops with a decision framework.

### Systematic Debugging (199.6K installs)
Eliminates debugging guesswork. Five-phase methodology: (1) reproduce the bug with minimal input, (2) isolate the failure to specific code paths, (3) root-cause analysis using git bisect or log tracing, (4) implement the fix, (5) verify with regression tests. Reduces debugging time by forcing methodological rigor instead of random print statements.

### Test-Driven Development (177.1K installs)
True TDD workflow for AI agents: write failing test → implement minimum code to pass → refactor. Prevents over-engineering by enforcing "simplest thing that works" at each step. Includes patterns for mocking, fixtures, and test organization.

### Writing Plans (196.8K installs)
Implementation planning that produces actionable steps — not vague descriptions. Each plan step includes: what to change, which files, what tests verify it, expected diff size. Allows agents to execute complex features without losing context mid-implementation.

---

## Quick Start

```bash
# 1. Install the framework
npx skills add obra/superpowers --skill using-superpowers
npx skills add obra/superpowers --skill brainstorming

# 2. Start with a brainstorming session
claude "Using the brainstorming skill, explore architectures for a real-time collaboration feature"

# 3. Convert the decision into an implementation plan
npx skills add obra/superpowers --skill writing-plans
claude "Using the writing-plans skill, create an implementation plan from the brainstorming output"

# 4. Execute with TDD
npx skills add obra/superpowers --skill test-driven-development
claude "Using the TDD skill, implement step 1 of the plan"
```

---

## Verification

```bash
# Check installed Superpowers
npx skills list | grep obra/superpowers

# Verify the framework loads
npx skills use obra/superpowers@using-superpowers
```

---

## Notes

- Superpowers is framework-agnostic — works with Claude Code, Codex, and any skills.sh-compatible agent
- The `brainstorming` skill alone has more installs than many entire skill catalogs — it's the de facto standard for agent ideation
- Combine with `anthropics/claude-code` skills for the full agent development toolkit: Superpowers for methodology + Claude Code skills for extensibility
- For Hermes agents: use `systematic-debugging` and `writing-plans` before any implementation work — they enforce the rigor that prevents context-window sprawl
- The `using-superpowers` skill teaches the agent how to chain skills together (brainstorm → plan → TDD → review) for end-to-end feature delivery
