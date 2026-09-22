---
title: Advanced Skill Creator - Custom Skill Generation Setup
description: "Skills from coreyhaines31/marketingskills at skills.sh - advanced-skill-creator for generating custom Hermes skills from descriptions. 689 github skills related."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/advanced-skill-creator-setup/"
robots: "index,follow"
last_updated: "2026-09-17"
tags: ["hermes skill", "skill creation", "automation", "skill-development"]
---

# Advanced Skill Creator - Setup Guide

**Source:** [coreyhaines31/marketingskills](https://skills.sh/coreyhaines31/marketingskills)  
**Skills:** advanced-skill-creator and related skill generation tools  
**Category:** Agent Infrastructure & Skill Development  
**First Seen:** September 17, 2026 sweep  
**Quality Tier:** 🟡 Trusted (community suite; verify per-skill before production use)

## Installation

```bash
npx skills add coreyhaines31/marketingskills --skill advanced-skill-creator
```

Individual skill creation tools can be installed separately:

```bash
npx skills add coreyhaines31/marketingskills --skill advanced-skill-creator
npx skills add coreyhaines31/marketingskills --skill better-skill-builder
npx skills add coreyhaines31/marketingskills --skill bocha-skill
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Profile: corpusiq |
| **Node.js + npx** | For the skills.sh installer |
| **Python 3.8+** | Required for skill generation scripts |
| **Text Editor** | VS Code or preferred editor for reviewing generated files |

## What It Provides

| Skill | Purpose | Notes |
|---|---|---|
| **advanced-skill-creator** | Generates custom SKILL.md files | Takes a description and produces a complete skill file |
| **better-skill-builder** | Enhanced skill builder with validation | Includes schema validation and error checking |
| **bocha-skill** | Bocha search integration skill | Search and extraction skill for Bocha API |
| **autonomous-skill-orchestrator** | Skill orchestration | Coordinates multiple skills in sequence |

## Quick Start

1. `npx skills add coreyhaines31/marketingskills --skill advanced-skill-creator`
2. `"Create a skill for email automation audit with trigger 'email audit'"` 
3. Review generated SKILL.md in ~/.hermes/profiles/corpusiq/skills/
4. `hermes skills install ./my-new-skill.md`

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Rapid Skill Prototyping** | Quickly generate skill skeletons for new workflows |
| **Skill Pattern Library** | Build reusable skill templates for common patterns |
| **Team Skill Onboarding** | Generate standardized skills for team agents |
| **Custom Connector Skills** | Create skills for niche APIs and services |

## Limitations / Verification

- Generated skills need review before production use
- Verify generated SKILL.md metadata and trigger patterns
- Test generated skills with dry-run before deploying

```bash
npx skills add coreyhaines31/marketingskills --skill advanced-skill-creator   # verify install works
```

## Related

- [Skills Catalog](/docs/hermes/skills/catalog)
- [Agent Orchestrator](/docs/hermes/skills/catalog/agent-orchestrator-setup)
- [Agent Treasury](/docs/hermes/skills/catalog/agent-treasury-setup) - agent resource management

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Marketplace](/docs/hermes/skills/marketplace) →*

*Powered by CorpusIQ*