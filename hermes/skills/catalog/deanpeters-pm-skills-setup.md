---
title: Dean Peters PM Skills — Product Management Workflows for Hermes Agents
description: Structured product management skills with 8.8K+ combined installs. PRD development, user story creation, and roadmap planning for agent-driven product development.
---

# Dean Peters PM Skills — Setup Guide

**Source:** [deanpeters/product-manager-skills](https://skills.sh/deanpeters/product-manager-skills) (8.8K+ combined installs)
**Category:** Product & Strategy
**Quality Tier:** 🟢 Production

Structured product management workflows for agents. Create comprehensive PRDs with standard templates, generate well-formed user stories with acceptance criteria, and build strategic roadmaps. Designed for agents to drive product development from problem definition through delivery planning.

---

## Installation

```bash
npx skills add deanpeters/product-manager-skills --skill prd-development
npx skills add deanpeters/product-manager-skills --skill user-story
npx skills add deanpeters/product-manager-skills --skill roadmap-planning
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **prd-development** | 3.2K | Complete PRD creation — problem statement, personas, solution, metrics, user stories, scope |
| **user-story** | 2.9K | User story generation with acceptance criteria, Given-When-Then format |
| **roadmap-planning** | 2.7K | Strategic roadmap creation — timeline, milestones, dependencies, resource planning |

---

## Key Capabilities

### PRD Development
- **Standard Template**: Executive summary → problem statement → personas → strategic context → solution → metrics → user stories → out of scope
- **Input Flexibility**: Works with full discovery notes OR starts from problem definition alone
- **Evidence-Driven**: Customer quotes, data, research, competitive landscape
- **OKR Alignment**: Ladders features to business goals
- **Scope Discipline**: Explicit "what are we NOT building" section

### User Story Creation
- **Standard Format**: "As a [persona], I want [action] so that [outcome]"
- **Acceptance Criteria**: Given-When-Then format for testable requirements
- **Story Mapping**: Organize stories into epics, themes, and releases
- **Priority Framework**: MoSCoW or RICE scoring integration

### Roadmap Planning
- **Timeline Visualization**: Now / Next / Later structure
- **Milestone Tracking**: Key deliverables with dates and dependencies
- **Resource Planning**: Team allocation, skill requirements, capacity
- **Risk Management**: Dependencies, blockers, mitigation strategies

---

## Quick Start

```bash
# Generate a PRD from problem statement
npx skills use deanpeters/product-manager-skills@prd-development
# Then: "Build a PRD for self-serve workspace provisioning — here are my discovery notes"

# Generate user stories from PRD
npx skills use deanpeters/product-manager-skills@user-story
# Then: "Create user stories for the workspace provisioning feature"
```

---

## Verification

```bash
npx skills list | grep deanpeters/product-manager-skills
```

---

## Notes

- Structured, template-driven approach — consistent output format every time
- Works with or without upfront discovery data; handles "empty-handed" invocations gracefully
- Complements `phuryn/pm-skills` (competitive analysis) and `refoundai/lenny-skills` (PM methodology)
- PRD template follows industry-standard sections used at major tech companies
- Useful for CorpusIQ product development workflow and feature specification
