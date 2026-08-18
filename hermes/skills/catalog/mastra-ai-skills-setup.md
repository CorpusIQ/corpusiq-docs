---
title: "Mastra AI Skills — TypeScript Agent Framework Setup"
description: "mastra-ai/skills — 5 skills, 32.6K installs: official Mastra reference guide for building agents, workflows, tools, memory, and RAG against current framework APIs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mastra-ai-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-18"
tags: ["hermes skill", "agent skill", "skill setup", "mastra", "typescript", "ai agents", "workflows"]
---

# Mastra AI Skills — Setup Guide

**Source:** [mastra-ai/skills](https://skills.sh/mastra-ai/skills)
**GitHub:** [mastra-ai/skills](https://github.com/mastra-ai/skills)
**Skills:** 5 skills · 32.6K total installs
**Category:** AI Agent Framework
**First Seen:** catalogued August 18, 2026 sweep (mastra on skills.sh since January 28, 2026)
**Quality Tier:** 🟡 Trusted — official Mastra org; flagship mastra passes Gen Agent Trust Hub and Socket, Snyk Warn (named)

The official Mastra skill suite is the canonical reference for building AI applications with the Mastra TypeScript framework. Its core doctrine is version discipline: never trust training-data knowledge of Mastra APIs, always verify against the embedded docs in `node_modules/@mastra/*/dist/docs/` or the remote `https://mastra.ai/llms.txt` before writing code. The flagship mastra skill carries 32.3K of the suite's 32.6K installs.

---

## Installation

```bash
npx skills add mastra-ai/skills
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/mastra-ai/skills --skill mastra
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Mastra project** | An existing TypeScript project with `@mastra/*` packages in `node_modules` |
| **ES2022 modules** | Required in TypeScript config for the framework |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| mastra | 32.3K | Reference guide for building agents and workflows with current Mastra APIs |
| create-mastra | 90 | Scaffolding new Mastra projects |
| mastra-best-practices | 89 | Framework conventions and patterns |
| mastra-embedded-docs-look-up | 67 | Lookup strategy against the installed version's embedded docs |
| mastra-embeded-docs-look-up | 41 | Earlier-named variant of the embedded docs lookup |

The flagship covers the core building blocks: Agents (autonomous decision-making), Workflows (structured sequences), Tools (capability extension), Memory (context maintenance), and RAG (external knowledge). It also documents the model format `"provider/model-name"` (for example `"openai/gpt-5.4"`), setup guidance, common errors, and migration notes matched to the installed version.

## Quick Start

1. Install: `npx skills add mastra-ai/skills`
2. Check the installed packages: `ls node_modules/@mastra/`
3. Ask the agent to build an agent or workflow — the skill routes every API question through the embedded docs of the exact installed version

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Version-accurate agent builds** | Kills the stale-training-data failure mode when generating Mastra agents and workflows |
| **RAG and memory patterns** | First-party reference for the Memory and RAG blocks we use in agent architecture |
| **Workflow orchestration** | Structured-sequence patterns translate to our multi-step automation design |

## Limitations / Verification

- Security audits on the mastra flagship: Gen Agent Trust Hub Pass, Socket Pass, Snyk Warn (named in the tier)
- Publisher-page total verified (32.6K across 5 skills); 72 GitHub stars on the skills repo as of the sweep
- create-mastra, mastra-best-practices, and the two embedded-docs variants are 41-90 installs each — early content
- The two embedded-docs skills overlap (one is a typo-named earlier variant)

```bash
npx skills add mastra-ai/skills   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
