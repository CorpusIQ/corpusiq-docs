---
title: Obra Superpowers — Engineering Workflow Skills for Hermes Agents
description: Brainstorming, systematic debugging, planning, code review, and test-driven development — 1.2M+ combined installs across 6 skills. Production-grade engineering workflows trusted by 295K+ developers.
---

# Obra Superpowers — Setup Guide

**Source:** [obra/superpowers](https://skills.sh/obra/superpowers) (1.2M+ combined installs)
**Category:** Engineering / Workflow
**Quality Tier:** 🟢 Production

Obra Superpowers is one of the most-installed skill suites on skills.sh, providing structured engineering workflows that turn any agent into a disciplined software engineer. The suite covers the full development lifecycle: brainstorming → planning → implementation → code review → testing → debugging.

---

## Installation

```bash
npx skills add obra/superpowers --skill brainstorming
npx skills add obra/superpowers --skill systematic-debugging
npx skills add obra/superpowers --skill writing-plans
npx skills add obra/superpowers --skill using-superpowers
npx skills add obra/superpowers --skill requesting-code-review
npx skills add obra/superpowers --skill test-driven-development
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **brainstorming** | 295.4K | Structured ideation with divergent/convergent thinking phases |
| **systematic-debugging** | 200.3K | Root-cause analysis with hypothesis testing and evidence collection |
| **writing-plans** | 197.5K | Create detailed implementation plans with milestones and acceptance criteria |
| **using-superpowers** | 195.5K | Meta-skill: teaches agents when and how to invoke other superpowers |
| **requesting-code-review** | 179.3K | Structured code review with diff analysis, feedback categorization, and approval gates |
| **test-driven-development** | 177.7K | Red-green-refactor cycle: write tests first, implement, then refactor |

---

## Key Capabilities

### Brainstorming — Structured Ideation
- Divergent phase: generate many ideas without judgment
- Convergent phase: evaluate, prioritize, and select
- Useful for architecture decisions, feature design, and problem-solving

### Systematic Debugging — Root-Cause Analysis
- Hypothesis-driven: form a theory, test it, gather evidence
- Systematic elimination of variables
- Evidence collection and documentation at each step

### Writing Plans — Implementation Planning
- Breaks work into milestones and tasks
- Includes acceptance criteria and dependencies
- Template-driven for consistency across projects

### Requesting Code Review — Quality Gates
- Structured diff analysis with categorized feedback
- Approval workflow with explicit gates
- Focus on architecture, correctness, and maintainability

### Test-Driven Development — Quality Assurance
- Write failing tests first (red)
- Implement minimal code to pass (green)
- Refactor for clean design (refactor)
- Maintains the discipline across the full cycle

---

## Quick Start

```bash
# Start any engineering task with brainstorming
npx skills use obra/superpowers@brainstorming

# Debug a complex issue systematically
npx skills use obra/superpowers@systematic-debugging

# Write a plan before implementing
npx skills use obra/superpowers@writing-plans
```

---

## Verification

```bash
npx skills list | grep "obra/superpowers"
# Expected: 6 skills listed with install counts
```

---

## Notes

- 1.2M+ combined installs makes this the most-installed engineering workflow suite on skills.sh
- All skills follow a structured, phase-based approach — no ad-hoc workflows
- The `using-superpowers` meta-skill teaches agents WHEN to use each workflow (not just how)
- Best used as a pipeline: brainstorm → plan → TDD implementation → code review → debug any issues
- These skills are Claude Code native but compatible with any Hermes agent doing engineering work
- The disciplined approach reduces rework and improves code quality across sessions
