---
title: Stably Orca — Agent Orchestration CLI Setup Guide for Hermes Agents
description: "Install stablyai/orca (317.5K combined installs) — 15 skills for the Orca agent orchestration CLI: orca-cli (125K), orchestration (104.2K), computer-use (77.3K), Linear integration, emulators, and auto PR workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/stablyai-orca-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Stably Orca — Setup Guide

**Source:** [stablyai/orca](https://www.skills.sh/stablyai/orca) (317.5K combined installs)
**GitHub:** [github.com/stablyai/orca](https://github.com/stablyai/orca)
**Category:** Agent Orchestration / CLI
**First Seen:** August 12, 2026
**Quality Tier:** 🟡 Beta (strong core skills, long tail still forming)

Orca is Stably AI's agent orchestration layer. `orca-cli` (125K installs) is the command-line driver; `orchestration` (104.2K) defines multi-agent workflow patterns; `computer-use` (77.3K) adds desktop control. A growing tail covers Linear ticket automation, Android/iOS emulator control, and autonomous PR loops (auto-review-fix, auto-pr-merge).

---

## Installation

```bash
# Install the full repo
npx skills add stablyai/orca

# Or install the core individually
npx skills add stablyai/orca --skill orca-cli
npx skills add stablyai/orca --skill orchestration
npx skills add stablyai/orca --skill computer-use
```

---

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| `orca-cli` | 125.0K | The Orca command-line driver |
| `orchestration` | 104.2K | Multi-agent orchestration patterns |
| `computer-use` | 77.3K | Desktop/UI control |
| `orca-linear` | 6.2K | Linear.app integration |
| `orca-per-workspace-env` | 2.7K | Per-workspace environment isolation |
| `orca-emulator` | 815 | Emulator control |
| `orca-emulator-android` | 686 | Android emulator control |
| `linear-tickets` | 609 | Linear ticket workflows |

Emerging (single-digit installs): `auto-pr-merge`, `auto-review-fix`, `auto-submit`, `review-and-submit`, `electron`, `react-useeffect`, `typescript`.

---

## Prerequisites

| Requirement | Details |
|---|---|
| Node.js + npx | For the skills.sh CLI install path |
| Orca runtime | Check the repo README for the CLI install (`orca-cli` drives it) |
| Linear API key | For `orca-linear` / `linear-tickets` |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Orchestration reference** | `orchestration` patterns to cross-check the multi-agent workflows in the growth stack |
| **Linear-based ops** | `orca-linear` + `linear-tickets` when Linear becomes the ops tracking layer |
| **Autonomous PR loops** | `auto-review-fix` pattern for docs repo automation (once the tail matures) |

---

## Limitations / Verification

- Long tail (7 of 15 skills) is single-digit installs — production-ready core, experimental periphery
- Verify install: `npx skills list | grep orca`

---

## Related

- [Ruflo — Multi-Agent Orchestration Setup](/hermes/skills/catalog/ruflo-setup/)
- [Linear Integration Setup](/hermes/skills/catalog/linear-setup/)
- [Skills Catalog](/hermes/skills/catalog/)

*Powered by CorpusIQ*
