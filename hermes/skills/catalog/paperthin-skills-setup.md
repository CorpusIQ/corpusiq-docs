---
title: "Paperthin - Agentic Design Patterns Toolkit Setup"
description: "lilmgenius/paperthin - 36 skills, 22.1K combined installs. Low-level agentic design patterns: SSOT consolidation, context debloating, fact-checking, Feynman explanations, and a ground-zero reset (re0) workflow family for keeping agents sharp mid-task."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/paperthin-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-31"
tags: ["hermes skill", "agent skill", "skill setup", "context discipline"]
---

# Paperthin - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/lilmgenius/paperthin) (22.1K combined installs)
**GitHub:** [lilmgenius/paperthin](https://github.com/lilmgenius/paperthin) (945⭐, MIT)
**Category:** Agent Operating Patterns & Context Discipline
**First Seen:** June 21, 2026 (skills.sh)
**Quality Tier:** 🟢 Production (Gen Agent Trust Hub Pass / Socket Pass / Snyk Pass)

"Low-level agentic design patterns. Turning old engineering wisdom into reflexes your agent reaches for on its own." Paperthin is a discipline toolkit for long-running agent work: `ssotize` enforces single-source-of-truth with a read-only audit → approval → consolidation gate; `debloat` trims context bloat; `factchk` and `readchk` verify claims and reading comprehension; the `re0` family ("ground zero") resets, re-plans, and re-targets work when a session drifts. Every skill is small, approval-gated where it mutates artifacts, and designed to become reflex.

---

## Installation

```bash
npx skills add lilmgenius/paperthin --skill ssotize    # SSOT consolidation
npx skills add lilmgenius/paperthin --skill debloat    # context/artifact bloat removal
npx skills add lilmgenius/paperthin --skill factchk    # claim verification
npx skills add lilmgenius/paperthin --skill feynman    # plain-language explanation
npx skills add lilmgenius/paperthin --skill re0        # ground-zero reset workflow
```

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| ssotize | 858 | Single-source-of-truth consolidation (audit → approve → consolidate) |
| shower / hate / sip | 855 / 844 / 829 | Unblocking and judgment resets for stuck sessions |
| re0 + re0-git/work/release/memo/plan/loop/upgrade/merge | 708-851 | Ground-zero family: reset, re-plan, re-target work mid-task |
| factchk | 842 | Fact-checking claims before they enter output |
| mandela | 841 | Detecting false-memory / assumed-fact drift |
| readchk | 740 | Reading-comprehension verification of source material |
| modelchk | 725 | Model capability/limitation self-check |
| feynman | 724 | Feynman-technique plain-language explanations |
| prism | 722 | Multi-perspective analysis |
| debloat | 719 | Context and artifact diet |
| catchup / macrothink / aim | 740 / 728 / 712 | Session recovery and goal alignment |
| dedash / detool / reorder | 821 / 717 / 713 | Refactoring agent habits and workflows |
| ssotchk / retro / flywheel | 122 / 111 / 110 | SSOT health, retrospectives, compounding improvement |
| redteam / scratch / tasting | 5 / 3 / 10 | Adversarial and experimental edge workflows |

## Prerequisites

- None - pure prompt-skill toolkit, no API keys or services
- Works with any agent runtime that loads skills.sh skills

## CorpusIQ Use Cases

- **SSOT discipline** - `ssotize`'s audit-then-mutate gate is the exact pattern CorpusIQ uses for brand facts and product claims across content surfaces
- **Context token economics** - `debloat` and `readchk` reinforce the field-filtering and memory-compaction doctrine already in CorpusIQ agent operating rules
- **Research rigor** - `factchk`/`mandela`/`prism` harden competitive-intelligence sweeps against hallucinated or assumed facts
- **Long-session recovery** - the `re0` family is a reusable playbook for resetting stalled multi-hour agent sessions

## Limitations / Verification

- Pattern skills encode discipline, not tooling - value depends on the agent actually invoking them mid-task
- Some skill names are opaque until read; the SKILL.md files are short and worth a one-time skim
- Verify install: `npx skills list | grep -E "ssotize|debloat|factchk"`

## Security

[Gen Agent Trust Hub: Pass](https://www.skills.sh/lilmgenius/paperthin/ssotize/security/agent-trust-hub) · [Socket: Pass](https://www.skills.sh/lilmgenius/paperthin/ssotize/security/socket) · [Snyk: Pass](https://www.skills.sh/lilmgenius/paperthin/ssotize/security/snyk)

## Related

- [Stop Slop Setup](/docs/hermes/skills/catalog/stop-slop-setup)
- [Avoid AI Writing Setup](/docs/hermes/skills/catalog/avoid-ai-writing-setup)
- [LJG Skills - Personal Knowledge Work Suite](/docs/hermes/skills/catalog/ljg-skills-setup)
