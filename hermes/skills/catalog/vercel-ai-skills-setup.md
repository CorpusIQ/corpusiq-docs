---
title: "Vercel AI SDK Skills — TypeScript AI Development Setup"
description: "vercel/ai — 3 skills, 51.1K installs: ai-sdk documentation, v6-to-v7 migration, and framework guidance from the Vercel team."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/vercel-ai-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-16"
tags: ["hermes skill", "agent skill", "skill setup", "ai sdk", "typescript", "vercel"]
---

# Vercel AI SDK Skills — Setup Guide

**Source:** [vercel/ai](https://skills.sh/vercel/ai)
**GitHub:** [vercel/ai](https://github.com/vercel/ai)
**Skills:** 3 skills · 51.1K total installs
**Category:** TypeScript AI Development
**First Seen:** ai-sdk on skills.sh January 23, 2026; catalogued August 16, 2026 sweep
**Quality Tier:** 🟡 Trusted — official Vercel org; ai-sdk carries a Snyk Warn (see Limitations)

Vercel's official skills make the AI SDK (`ai` package on npm) safe for agents to work with: version-matched documentation, migration playbooks, and a guardrail against the single biggest agent failure mode — writing AI SDK code from memory against obsolete APIs.

---

## Installation

```bash
npx skills add vercel/ai
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/vercel/ai --skill ai-sdk
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **TypeScript project** | The SDK is TypeScript-first |
| **Vercel AI SDK** | `npm install ai` in the target project |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| ai-sdk | 48.0K | Core SDK docs: `generateText`, `streamText`, `ToolLoopAgent`, `embed`, tool calling across providers |
| migrate-ai-sdk-v6-to-v7 | 3.1K | Breaking-change migration playbook |
| island-rescue | 9 | Early-access helper |

The core ai-sdk skill covers the unified API across OpenAI, Anthropic, Google, and other providers; React hooks (`useChat`, `useCompletion`); type-safe agent consumption via `InferAgentUIMessage`; and local DevTools debugging. Its central doctrine: **never write AI SDK code from memory** — always verify against the version-matched docs bundled inside `node_modules`.

## Quick Start

1. Install: `npx skills add vercel/ai`
2. Ask the agent to scaffold an agent loop: "build a TypeScript agent with `generateText` + tool calling per the bundled AI SDK docs"
3. For upgrades, invoke the migration skill: "migrate this project from AI SDK v6 to v7"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Agent infrastructure** | `ToolLoopAgent` and streaming patterns are reference architecture for CorpusIQ's own agent loops |
| **Multi-provider routing** | One unified API across providers maps directly onto our DeepSeek-primary, Claude-fallback model routing |
| **Client delivery** | Version-matched scaffolding for clients building LLM-powered products |
| **Migration discipline** | The v6→v7 playbook is a template for how we document breaking changes in our own stack |

## Limitations / Verification

- Security audits on ai-sdk: Gen Agent Trust Hub Pass, Socket Pass, **Snyk Warn** — trusted with the audit named
- Publisher-page install counts verified (48.0K ai-sdk); GitHub 26.2K stars
- island-rescue shows 9 installs — experimental content, ignore it
- Skills assume a Next.js/Vercel-adjacent stack; React hooks guidance is client-framework-specific

```bash
npx skills add vercel/ai   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
