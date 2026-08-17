---
title: "Planning With Files — Agent Planning Methodology Setup"
description: "othmanadi/planning-with-files — 7 skills, 90.5K combined installs. File-based planning methodology: task plan, findings, and decisions files that keep agents on track across long sessions."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/planning-with-files-setup/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["hermes skill", "agent skill", "skill setup", "methodology"]
---

# Planning With Files — Setup Guide

**Source:** [skills.sh](https://www.skills.sh/othmanadi/planning-with-files) (90.5K combined installs)
**GitHub:** [othmanadi/planning-with-files](https://github.com/othmanadi/planning-with-files)
**Category:** Agent Methodology
**First Seen:** August 13, 2026 sweep
**Quality Tier:** 🟢 Production (framework-agnostic)

A planning methodology skill for agents working on long, multi-step tasks: persist a task plan, findings, and decisions to files on disk instead of holding everything in context. This is the skills.sh-ecosystem answer to context loss on long sessions — the agent re-reads its plan files each turn, so interrupted or context-compacted runs resume cleanly. Multilingual: Arabic, German, Spanish, Simplified and Traditional Chinese, plus a personal-intelligence variant (`pi-planning-with-files`).

---

## Installation

```bash
npx skills add othmanadi/planning-with-files
```

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| planning-with-files | 40.2K | Core file-based planning methodology (English) |
| planning-with-files-zh | 16.8K | Simplified Chinese edition |
| pi-planning-with-files | 9.8K | Personal-intelligence variant — reflection-aware planning |
| planning-with-files-zht | 6.8K | Traditional Chinese edition |
| planning-with-files-es | 5.7K | Spanish edition |
| planning-with-files-de | 5.6K | German edition |
| planning-with-files-ar | 5.6K | Arabic edition |

## Prerequisites

- No dependencies — pure procedural knowledge; works with any agent that can read/write files
- Best paired with a workspace directory the agent owns

## CorpusIQ Use Cases

- **Cron resilience** — file-plan persistence is the exact pattern CorpusIQ crons use (handoff pages, state files); this skill formalizes it for any long-running agent task
- **Session handoff** — complements the Honcho/GBrain session-handoff ritual with a lightweight on-disk plan for task continuity
- **Localized support** — the zh/es/de/ar editions support multilingual operator teams

## Limitations / Verification

- Methodology only — no enforcement; the agent must actually follow its own plan files
- Verify: start a task, confirm the plan file is written, interrupt, and confirm the next run resumes from the plan

## Related

- [Momentic Skills — AI QA Testing Suite Setup](/hermes/skills/catalog/momentic-skills-setup/)
- [Warp Common Skills — Spec-Driven Development Workflow Setup](/hermes/skills/catalog/warpdotdev-common-skills-setup/)
