---
title: New Skills — August 11, 2026
description: 5 newly discovered Hermes Agent skills from skills.sh marketplace sweep — songwriting & AI music, TUI debugging, attestation guardian, research paper writing pipeline, and plan mode.
---

# New Skills — August 11, 2026

**Source:** [skills.sh](https://skills.sh) via `npx skills search`
**Date:** August 11, 2026
**Total new this batch:** 5 skills (3 genuinely new + 2 from Aug 10 sweep without guides)

Routine daily sweep of the skills.sh marketplace. After cross-referencing against the existing 366+ documented skills in `hermes/skills/catalog/`, 5 skills were identified as needing setup guides — 3 are genuinely new discoveries not covered by previous sweeps, and 2 were identified in the Aug 10 sweep but hadn't received setup guides yet.

---

## 🆕 Genuinely New Skills (3) — First Documentation

| # | Skill | Installs | Source | Setup Guide |
|---|-------|----------|--------|-------------|
| 1 | `songwriting-and-ai-music` | 324 | nousresearch/hermes-agent | [songwriting-and-ai-music-setup.md](/hermes/skills/catalog/songwriting-and-ai-music-setup.html) ✍️ |
| 2 | `debugging-hermes-tui-commands` | 76 | nousresearch/hermes-agent | [debugging-hermes-tui-commands-setup.md](/hermes/skills/catalog/debugging-hermes-tui-commands-setup.html) ✍️ |
| 3 | `hermes-attestation-guardian` | 94 | prompt-security/clawsec | [hermes-attestation-guardian-setup.md](/hermes/skills/catalog/hermes-attestation-guardian-setup.html) ✍️ |

---

## 📝 Previously Identified — Now With Setup Guides (2)

| # | Skill | Installs | Source | Setup Guide |
|---|-------|----------|--------|-------------|
| 4 | `research-paper-writing` | 396 | nousresearch/hermes-agent | [research-paper-writing-setup.md](/hermes/skills/catalog/research-paper-writing-setup.html) ✍️ |
| 5 | `plan` | 309 | nousresearch/hermes-agent | [plan-mode-setup.md](/hermes/skills/catalog/plan-mode-setup.html) ✍️ |

---

## Skill Details

### 1. songwriting-and-ai-music (324 installs)
Official Hermes Agent creative skill for AI-assisted songwriting. Provides song structure templates (ABABCB, AABA, ABAB, AAA), lyrical composition guidelines, and integration hooks for AI music generation tools like Suno and Udio. Art-forward philosophy: guidelines, not rules.

### 2. debugging-hermes-tui-commands (76 installs)
Essential developer tool for diagnosing TUI slash command issues across Hermes' three-layer architecture (Python registry → JSON-RPC gateway → Ink/TypeScript frontend). Covers autocomplete debugging, layer desync detection, and new command registration walkthrough.

### 3. hermes-attestation-guardian (94 installs)
Security verification skill from prompt-security/clawsec. Performs release artifact verification, checksum validation against ClawSec release keys, SBOM inspection, runtime attestation, and trust chain verification for Hermes infrastructure components.

### 4. research-paper-writing (396 installs)
End-to-end ML/AI research paper pipeline targeting NeurIPS, ICML, ICLR, ACL, AAAI, and COLM. Covers experiment design, execution, monitoring, analysis, paper writing, review response, and camera-ready submission. Originally from master-cai/research-paper-writing-skills.

### 5. plan (309 installs)
Plan Mode switches Hermes into planning-only execution. Generates structured markdown plans saved to `.hermes/plans/` but does NOT implement code, run mutating commands, or perform external actions. Ideal for architecture reviews and stakeholder alignment.

---

## Installation

```bash
# Songwriting & AI Music
npx skills add nousresearch/hermes-agent --skill songwriting-and-ai-music

# Debugging TUI Commands
npx skills add nousresearch/hermes-agent --skill debugging-hermes-tui-commands

# Attestation Guardian
npx skills add prompt-security/clawsec --skill hermes-attestation-guardian -a hermes-agent -y

# Research Paper Writing
npx skills add nousresearch/hermes-agent --skill research-paper-writing

# Plan Mode
npx skills add nousresearch/hermes-agent --skill plan
```

---

## Notable

- **songwriting-and-ai-music** is the first creative/music skill documented in the catalog — expanding Hermes beyond development and productivity into artistic workflows.
- **debugging-hermes-tui-commands** fills a critical developer experience gap — the three-layer TUI architecture has been a common source of confusion.
- **hermes-attestation-guardian** brings production-grade security verification to the ecosystem — essential for enterprise Hermes deployments.
- **research-paper-writing** at 396 installs is the highest-install academic skill documented, reflecting Hermes' growing adoption in ML research.
- **plan mode** introduces a formal planning-only execution mode — useful for architecture reviews, stakeholder sign-offs, and safe exploration.

---

## Existing Skills Verified (not new)

All top-20 skills from `npx skills search hermes` were verified as already cataloged (dogfood 5.4K, hermes-imports 4.5K, hermes-history-ingest 2.1K, hermes-tweet 682, hermes-agent 561, popular-web-designs 561, yuanbao 561, powerpoint 472, google-workspace 427, arxiv 422, claude-design 387, llm-wiki 370, jupyter-live-kernel 356, excalidraw 343, ascii-art 341, youtube-content 336, imessage 331, design-md 330, architecture-diagram 320, hermes-agent-skill-authoring 276).

---

*← [Skills Home](/hermes/skills/) | [Skills Catalog](/hermes/skills/catalog/) | [Previous Sweep →](/hermes/skills/marketplace/new-aug10-2026/)*

*Powered by CorpusIQ*
