---
title: Agent Treasury - Agent Resource Management Setup
description: "Skills from coreyhaines31/marketingskills at skills.sh - agent-treasury for managing agent resources, capabilities, and metadata. 689 github skills related."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agent-treasury-setup/"
robots: "index,follow"
last_updated: "2026-09-17"
tags: ["hermes skill", "agent skill", "resource-management", "metadata"]
---

# Agent Treasury - Setup Guide

**Source:** [coreyhaines31/marketingskills](https://skills.sh/coreyhaines31/marketingskills)  
**Skills:** agent-treasury and related agent resource management tools  
**Category:** Agent Infrastructure & Resource Management  
**First Seen:** September 17, 2026 sweep  
**Quality Tier:** 🟡 Trusted (community suite; verify per-skill before production use)

## Installation

```bash
npx skills add coreyhaines31/marketingskills --skill agent-treasury
```

Individual resource management skills can be installed separately:

```bash
npx skills add coreyhaines31/marketingskills --skill agent-treasury
npx skills add coreyhaines31/marketingskills --skill agent-registry
npx skills add coreyhaines31/marketingskills --skill agent-self-governance
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Profile: corpusiq |
| **Node.js + npx** | For the skills.sh installer |
| **Agent Registry** | Optional: centralized agent capability registry |
| **Configuration Storage** | Persistent storage for agent metadata |

## What It Provides

| Skill | Purpose | Notes |
|---|---|---|
| **agent-treasury** | Manages agent resources and capabilities | Central registry of agent skills, states, and configurations |
| **agent-registry** | Agent capability registry | Searchable registry of all agent capabilities |
| **agent-self-governance** | Self-governance patterns | Agent self-assessment and constraint enforcement |
| **agent-skills-toolkit** | Utility tools for agent management | Helper functions for treasury operations |

## Quick Start

1. `npx skills add coreyhaines31/marketingskills --skill agent-treasury`
2. `"Register my agent's capabilities in the treasury"`
3. `"Check if agent has skill X"`
4. `"List all registered agent capabilities"`

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Agent Fleet Management** | Track capabilities across distributed agent fleets |
| **Skill Discovery** | Find agents with specific capabilities for tasks |
| **Resource Allocation** | Allocate tasks based on agent availability and skills |
| **Compliance Monitoring** | Monitor agent adherence to governance policies |

## Limitations / Verification

- Registry consistency depends on all agents reporting accurately
- Verify treasury state periodically for drift
- Cross-reference with actual agent capability outputs

```bash
npx skills add coreyhaines31/marketingskills --skill agent-treasury   # verify install works
```

## Related

- [Skills Catalog](/docs/hermes/skills/catalog)
- [Agent Orchestrator](/docs/hermes/skills/catalog/agent-orchestrator-setup)
- [Advanced Skill Creator](/docs/hermes/skills/catalog/advanced-skill-creator-setup) - skill generation

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Marketplace](/docs/hermes/skills/marketplace) →*

*Powered by CorpusIQ*