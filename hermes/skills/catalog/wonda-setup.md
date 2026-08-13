---
title: Wonda CLI — AI Content Creation from the Terminal Setup Guide for Hermes Agents
description: "degausai/wonda — 74.6K installs. Terminal-first AI content creation CLI: images, video, and media workflows agents can drive without a browser."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/wonda-setup/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["hermes skill", "agent skill", "skill setup", "media"]
---

# Wonda CLI — Setup Guide

**Source:** [skills.sh](https://www.skills.sh/degausai/wonda) (74.6K installs)
**GitHub:** [degausai/wonda](https://github.com/degausai/wonda) (143⭐, TypeScript)
**Category:** AI Content Creation
**First Seen:** August 13, 2026 sweep
**Quality Tier:** 🔵 Community

Wonda CLI is an AI-powered content creation tool for the terminal — image and video generation driven from the command line instead of a web UI. The skill teaches agents to orchestrate Wonda for media production inside automated pipelines, where browser-based generation tools don't fit. A single-skill publisher with outsized installs (74.6K).

---

## Installation

```bash
npx skills add degausai/wonda
npm install -g wonda-cli   # the underlying CLI
```

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| wonda-cli | 74.6K | Terminal-driven AI content creation workflows |

## Prerequisites

- Node.js 20+
- Wonda account/API access for generation
- Headless-friendly environment (Wonda runs without a browser)

## CorpusIQ Use Cases

- **Automated creative generation** — CLI-driven media fits the Mac Mini/Spark worker model where browser UIs are avoided
- **Pipeline diversification** — an alternative generation backend alongside HyperFrames and Postiz media for batch ad creative

## Limitations / Verification

- Community-maintained; API surface may change faster than the skill documentation
- Verify: `wonda --version` after install, then generate one test asset and confirm the output file lands

## Related

- [Higgsfield Skills — AI Video & Image Generation Cluster Setup](/hermes/skills/catalog/higgsfield-skills-setup/)
- [GenMedia Skills — AI Media Generation Cluster Setup](/hermes/skills/catalog/genmedia-skills-setup/)
