---
title: "AtlasOmnia Hermes Custom Pack — 60+ Skill Independent Pack Setup"
description: "atlasomnia/hermes-custom-pack — 60+ installable skills, plugins, and utilities for Hermes Agent: a Hermes-ops core (config editing, context optimization, self-evaluation, session maintenance, Mnemosyne, plugin development) plus verification, macOS automation, and productivity families."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/atlasomnia-hermes-custom-pack-setup/"
robots: "index,follow"
last_updated: "2026-08-19"
tags: ["hermes skill", "agent skill", "skill setup", "hermes configuration", "hermes plugins", "mnemosyne", "skill audit", "pre-push gates"]
---

# AtlasOmnia Hermes Custom Pack — Setup Guide

**Source:** [atlasomnia/hermes-custom-pack](https://skills.sh/atlasomnia/hermes-custom-pack)
**GitHub:** [AtlasOmnia/hermes-agent-custom-pack](https://github.com/AtlasOmnia/hermes-agent-custom-pack)
**Skills:** 60+ skills (9 indexed on skills.sh at 2-3 installs each) · independent per-package installs
**Category:** Hermes Operations + Productivity
**First Seen:** August 19, 2026 evening sweep
**Quality Tier:** 🟡 Beta — 48 GitHub stars, unofficial pack, every package documented with explicit verification steps and safe to inspect before use

An independent pack of practical skills, plugins, integrations, scripts, and utilities built by AtlasOmnia from real Hermes installations. Unlike monolithic skill dumps, every package installs on its own and carries its own verification steps. The strongest value is the Hermes-ops core: configuration editing patterns that work around security guards, context payload optimization, self-evaluation through external models, session history maintenance, and Mnemosyne memory operations. The verification family (pre-push gates, publication link audits, source verification, evidence-based replies) overlaps directly with CorpusIQ's public-content discipline.

---

## Installation

Inspect a skill before installing it:

```bash
hermes skills inspect https://raw.githubusercontent.com/AtlasOmnia/hermes-agent-custom-pack/main/skills/browser-harness-authoring/SKILL.md
```

Install it directly:

```bash
hermes skills install https://raw.githubusercontent.com/AtlasOmnia/hermes-agent-custom-pack/main/skills/browser-harness-authoring/SKILL.md
```

Start a new Hermes session after installation so the skill registry is refreshed. Note the GitHub repo name is `hermes-agent-custom-pack` while the skills.sh source listing shows `atlasomnia/hermes-custom-pack` — use the GitHub raw URLs for direct installs.

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | All skills are Hermes-native SKILL.md packages |
| **macOS (for some families)** | apple-reminders, imessage, macos-app-automation, macos-storage-management are macOS-only |
| **CLI companions (per skill)** | imsg (iMessage), pygount (codebase-inspection), gws CLI (google-workspace), ntn (notion), OpenCode (opencode) |

## What It Provides

| Family | Representative Skills | Purpose |
|---|---|---|
| Hermes ops core | hermes-config-editing, hermes-context-optimization, hermes-self-evaluation, hermes-diagnostic-review, hermes-session-maintenance, hermes-overnight-autonomy, hermes-nightly-self-check-decisions | Edit config safely, shrink context payloads, review Hermes itself, maintain session history, run unattended continuity |
| Memory | hermes-mnemosyne, mnemosyne-maintenance, obsidian-memory-architecture | Configure, troubleshoot, and maintain the Mnemosyne memory provider; use Obsidian as a durable knowledge layer |
| Plugins | hermes-plugin-development, hermes-plugin-evaluation, hermes-desktop-plugins, inspecting-hermes-desktop-dom | Design, register, debug, and evaluate Hermes plugins before install; read desktop DOM over CDP |
| Verification | github-pre-push-gates, publication-link-audit, source-verification, evidence-based-replies, external-model-review, specification-compliance-review, skill-auditor | Immutable pre-push gates, outbound link verification, claim-source separation, A-F skill grading |
| Community | content-style, reddit-browse-and-post, meta-business-posting, xurl | Content for r/hermesagent, read-only Reddit browsing with opt-in posting, X via xurl CLI |
| macOS + productivity | apple-reminders, imessage, macos-app-automation, daily-news-digests, session-artifact-indexing, obsidian, notion | Native macOS automation, digest scripts, durable artifact indexing, note vaults |

Hermes-ops skills indexed on skills.sh: hermes-diagnostic-review (3), hermes-agent (2), hermes-mnemosyne (2), hermes-themes (2), hermes-desktop-plugins (2), hermes-plugin-evaluation (2), hermes-self-evaluation (2), hermes-config-editing (2), hermes-nightly-self-check-decisions (2).

## Quick Start

1. Inspect the ops core: `hermes skills inspect https://raw.githubusercontent.com/AtlasOmnia/hermes-agent-custom-pack/main/skills/hermes-context-optimization/SKILL.md`
2. Install it and hermes-config-editing for safe configuration work
3. For publishing discipline, add github-pre-push-gates and publication-link-audit
4. Start a new session; say "optimize my Hermes context payload" or "run the pre-push gates"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Session DB and context optimization** | hermes-context-optimization and hermes-session-maintenance map to our three-phase session DB optimization and token-health work |
| **Pre-push sanitization** | github-pre-push-gates (immutable verification, privacy scanning, clean publication) matches our pre-push sanitization checklist for public content |
| **Outbound link integrity** | publication-link-audit verifies every outbound URL — the same class of check as our broken-link audits |
| **Skill quality grading** | skill-auditor's A-F grading with fix suggestions aligns with our quarterly skill audits and skill-consolidate passes |
| **Overnight autonomy** | hermes-overnight-autonomy and nightly-self-check-decision recording match our nocturnal cron maintenance cycle |
| **Evidence-disciplined replies** | evidence-based-replies and source-verification encode verify-before-assertion for public responses |

## Limitations / Verification

- Below the 20K install guide bar — drafted on cluster authority: a cohesive 60+ skill Hermes-native pack with a strong ops core, 48 GitHub stars
- Unofficial and not affiliated with Nous Research; every package should still be inspected before install (the pack's own stated policy)
- Some families are macOS-only or require CLI companions not present on Linux workers
- Related project `AtlasOmnia/hermes-loops` (autoresearch propose→test→keep/revert harness) is a separate monorepo, not part of this pack

```bash
hermes skills inspect https://raw.githubusercontent.com/AtlasOmnia/hermes-agent-custom-pack/main/skills/hermes-context-optimization/SKILL.md   # verify fetch works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)
- [Hermes Field Kit Setup](/hermes/skills/catalog/hermes-field-kit-setup/)
- [Avoid AI Writing — AI-Pattern Audit & Rewrite Setup](/hermes/skills/catalog/avoid-ai-writing-setup/)

*Powered by CorpusIQ*
