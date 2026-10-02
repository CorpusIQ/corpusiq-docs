---
title: Agent Skill Creator - Skill Generation and Templating Setup
description: "Skills from coreyhaines31/marketingskills at skills.sh - agent-skill-creator for generating custom Hermes skills from descriptions and templates. 689 github skills related."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agent-skill-creator-setup/"
robots: "index,follow"
last_updated: "2026-09-17"
tags: ["hermes skill", "skill creation", "templating", "automation", "agent-skill-creator"]
---

# Agent Skill Creator - Setup Guide

**Source:** [coreyhaines31/marketingskills](https://skills.sh/coreyhaines31/marketingskills)  
**Skills:** agent-skill-creator and related skill generation tools  
**Category:** Agent Infrastructure & Skill Development  
**First Seen:** September 17, 2026 sweep  
**Quality Tier:** 🟡 Trusted (community suite; verify per-skill before production use)

## Installation

```bash
npx skills add coreyhaines31/marketingskills --skill agent-skill-creator
```

Individual skill creation tools can be installed separately:

```bash
npx skills add coreyhaines31/marketingskills --skill agent-skill-creator
npx skills add coreyhaines31/marketingskills --skill apprun-skills
npx skills add coreyhaines31/marketingskills --skill autonomous-skill-orchestrator
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Profile: corpusiq |
| **Node.js + npx** | For the skills.sh installer |
| **Python 3.8+** | Required for skill generation scripts |
| **Template Engine** | Jinja2 or similar for skill templates |

## What It Provides

| Skill | Purpose | Notes |
|---|---|---|
| **agent-skill-creator** | Generates custom Hermes skills from descriptions | Takes natural language descriptions and produces complete SKILL.md files with triggers, tools, steps, and verification gates |
| **apprun-skills** | Skill execution runner | Runs generated skills in Hermes context |
| **autonomous-skill-orchestrator** | Skill orchestration engine | Coordinates multiple skills in sequence |
| **autoschei-skill** | Skill checkpoint and state management | Checkpoint-based skill execution with state persistence |

## Quick Start

1. `npx skills add coreyhaines31/marketingskills --skill agent-skill-creator`
2. `"Create a skill for email automation audit with trigger 'email audit'"`
3. Review generated SKILL.md in ~/.hermes/profiles/corpusiq/skills/
4. `hermes skills install ./generated-skill.md`

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
npx skills add coreyhaines31/marketingskills --skill agent-skill-creator   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog)
- [Advanced Skill Creator](/hermes/skills/catalog/advanced-skill-creator-setup)
- [Agent Treasury](/hermes/skills/catalog/agent-treasury-setup) - resource management

*← [Skills Catalog](/hermes/skills/catalog) | [Marketplace](/hermes/skills/marketplace) →*

*Powered by CorpusIQ*