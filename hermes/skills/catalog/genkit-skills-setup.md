---
title: "Genkit Skills — Firebase Genkit AI Framework Setup"
description: "genkit-ai/skills — 4 skills, 57.3K combined installs. Official Firebase Genkit development skills for building AI features in JavaScript, Dart, Go, and Python."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/genkit-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["hermes skill", "agent skill", "skill setup", "ai-framework"]
---

# Genkit Skills — Setup Guide

**Source:** [skills.sh](https://www.skills.sh/genkit-ai/skills) (57.3K combined installs)
**GitHub:** [genkit-ai/skills](https://github.com/genkit-ai/skills)
**Category:** AI Application Framework
**First Seen:** August 13, 2026 sweep
**Quality Tier:** 🟢 Production (official Google/Firebase)

Firebase Genkit is Google's open-source framework for building AI features (RAG, agents, flows, evals) with production tooling. This is the official companion skill pack — one development skill per language SDK. Complements the existing firebase/agent-skills cluster in the catalog.

---

## Installation

```bash
npx skills add genkit-ai/skills
```

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| developing-genkit-js | 55.1K | Genkit development in JavaScript/TypeScript |
| developing-genkit-dart | 787 | Genkit in Dart (Flutter apps) |
| developing-genkit-go | 700 | Genkit in Go |
| developing-genkit-python | 651 | Genkit in Python |

## Prerequisites

- Node.js 20+ (JS), Dart SDK, Go 1.22+, or Python 3.10+ depending on SDK
- A model provider key (Gemini, OpenAI, Anthropic, or local Ollama)

## CorpusIQ Use Cases

- **Eval-driven agent tooling** — Genkit's eval harness is a reference for CorpusIQ's own agent-eval framework
- **Customer-facing AI features** — the RAG and flows patterns for embedded assistant features in operator dashboards

## Limitations / Verification

- Firebase/Google ecosystem centric; multi-provider but tooling defaults to Google Cloud
- Verify: scaffold a Genkit JS project and run `genkit start` to confirm the dev UI boots

## Related

- [Firebase Agent Skills — Google Backend Setup](/hermes/skills/catalog/google-skills-setup/)
- [Convex Agent Skills — Backend Platform Setup](/hermes/skills/catalog/convex-agent-skills-setup/)
