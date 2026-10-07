---
title: Matt Pocock Skills (简体中文) - Localized Engineering Suite
description: "vinvcn/mattpocock-skills-zh-cn - 54 skills, 138.8K combined installs. The Simplified-Chinese localization of mattpocock/skills: TDD, domain modeling, code review, and spec-to-ticket workflows for Chinese-speaking agents, plus a translate-skill workflow for localizing other skill packs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mattpocock-skills-zh-cn-setup/"
robots: "index,follow"
last_updated: "2026-08-31"
tags: ["hermes skill", "agent skill", "skill setup", "localization"]
---

# Matt Pocock Skills (简体中文) - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/vinvcn/mattpocock-skills-zh-cn) (138.8K combined installs)
**GitHub:** [vinvcn/mattpocock-skills-zh-cn](https://github.com/vinvcn/mattpocock-skills-zh-cn) (3,856⭐, MIT)
**Category:** Engineering Workflow (Localized)
**First Seen:** May 6, 2026 (skills.sh)
**Quality Tier:** 🟢 Production (Gen Agent Trust Hub Pass / Socket Pass / Snyk Pass)

This is the Simplified-Chinese localization of `mattpocock/skills` - Matt Pocock's well-known engineering skill suite (TDD, domain modeling, code review, spec-to-ticket workflows) already documented in the catalog under its English source. The zh-CN fork matters on its own: 138.8K installs make it one of the largest non-English suites on skills.sh, and it adds unique localization tooling - `translate-skill` (localize any skill pack), `setup-matt-pocock-skills`, and Chinese-language grilling/domain-modeling workflows. Skills keep their English names for cross-compatibility; SKILL.md bodies are Chinese.

---

## Installation

```bash
npx skills add vinvcn/mattpocock-skills-zh-cn --skill grill-me
npx skills add vinvcn/mattpocock-skills-zh-cn --skill tdd
npx skills add vinvcn/mattpocock-skills-zh-cn --skill domain-modeling
npx skills add vinvcn/mattpocock-skills-zh-cn --skill translate-skill
```

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| grill-me / grill-with-docs / grilling / batch-grill-me | 5.3K / 5.0K / 3.1K / 626 | Socratic grilling sessions against docs and decisions |
| setup-matt-pocock-skills | 4.8K | Full-suite installation bootstrap |
| handoff / claude-handoff | 4.7K / 1.8K | Session handoff documentation |
| tdd / improve-codebase-architecture / prototype | 4.7K / 4.6K / 4.6K | Test-driven development and architecture |
| triage / diagnosing-bugs / code-review / diagnose | 4.5K / 2.9K / 2.9K / 1.7K | Bug triage and review workflows |
| domain-modeling / ubiquitous-language / domain-model | 2.9K / 2.1K / 1 | Domain-driven design |
| to-spec / to-tickets / to-prd / to-issues / to-questionnaire | 2.2-2.4K | Spec-to-work-item conversion chain |
| research / implement / design-an-interface / qa | 2.2-2.9K | Build-loop workflow skills |
| writing-shape / writing-fragments / writing-beats / writing-great-skills / writing-for-agents | 719-2.7K | Writing craft for agents and articles |
| translate-skill | 19 | Localize any skill pack into another language |
| wayfinder / wizard / loop-me / zoom-out / wait-what / caveman | 1.7-2.6K | Agent operating reflexes |
| (≈18 more) | <1.7K each | git guardrails, pre-commit, obsidian vault, shoehorn migration, teaching |

## Prerequisites

- None - pure prompt-skill suite; works with any runtime that loads skills.sh skills
- Chinese-language SKILL.md content: the agent must be able to follow Chinese instructions

## CorpusIQ Use Cases

- **Chinese-market operator support** - the localized suite lets CorpusIQ-connected agents serve Chinese-speaking operators with native-language engineering workflows
- **Localization pipeline** - `translate-skill` is a reusable workflow for localizing CorpusIQ's own skill packs and docs into zh-CN
- **Spec discipline parity** - the to-spec → to-tickets → to-prd chain matches CorpusIQ's spec-first governance pattern

## Limitations / Verification

- Fork of the already-documented mattpocock/skills (English); upstream changes lag behind the source repo - cross-check against the English catalog entry for the canonical workflow set
- Skills keep English names but Chinese bodies - mixed-language tooling friction in English-first runtimes
- Verify install: `npx skills list | grep grill-me`

## Security

[Gen Agent Trust Hub: Pass](https://www.skills.sh/vinvcn/mattpocock-skills-zh-cn/grill-with-docs/security/agent-trust-hub) · [Socket: Pass](https://www.skills.sh/vinvcn/mattpocock-skills-zh-cn/grill-with-docs/security/socket) · [Snyk: Pass](https://www.skills.sh/vinvcn/mattpocock-skills-zh-cn/grill-with-docs/security/snyk)

## Related

- [Matt Pocock Skills Setup](/hermes/skills/catalog/mattpocock-skills-setup)
- [Matt Pocock Engineering Setup](/hermes/skills/catalog/matt-pocock-engineering-setup)
