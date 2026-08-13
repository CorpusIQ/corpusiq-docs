---
title: Momentic Skills — AI QA Testing Suite Setup Guide for Hermes Agents
description: "momentic-ai/skills — 5 skills, 118.9K combined installs. Agent-driven end-to-end testing: test authoring, result classification, mobile testing, and spec-driven QA with Momentic."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/momentic-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["hermes skill", "agent skill", "skill setup", "qa"]
---

# Momentic Skills — Setup Guide

**Source:** [skills.sh](https://www.skills.sh/momentic-ai/skills) (118.9K combined installs)
**GitHub:** [momentic-ai/skills](https://github.com/momentic-ai/skills)
**Category:** QA & Testing
**First Seen:** August 13, 2026 sweep
**Quality Tier:** 🟡 Beta (platform-dependent)

Momentic is an AI-native QA platform, and this is its official skill pack. Agents write and run end-to-end tests, classify failures, test mobile flows, and turn specs into test plans. The strongest agent-first QA cluster on skills.sh — relevant for any team shipping agent-built software without a dedicated QA function.

---

## Installation

```bash
npx skills add momentic-ai/skills
```

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| momentic-test | 41.0K | Authoring and running E2E tests |
| momentic-result-classification | 41.0K | Classifying test failures (bug vs flake vs env) |
| momentic-mobile-test | 26.8K | Mobile app test flows |
| momentic-explore-prompt | 9.3K | Exploratory testing prompts |
| momentic-spec | 786 | Spec-to-test plan generation |

## Prerequisites

- Momentic account (free tier for small teams)
- A deployed app or live site under test

## CorpusIQ Use Cases

- **QA gate for agent-built features** — run `momentic-test` against internal tools and docs site changes before shipping
- **Flake triage** — `momentic-result-classification` cuts noise from CI pipelines (the flake-vs-real-bug split is the expensive part of agent-driven QA)
- **Spec-driven acceptance** — `momentic-spec` converts product specs into acceptance tests for customer deliverables

## Limitations / Verification

- Tests execute on Momentic's platform — no fully local mode
- Verify: author one smoke test against docs.corpusiq.io and confirm it passes on the Momentic dashboard

## Related

- [Playwright Best Practices — E2E Testing Setup](/hermes/skills/catalog/infrastructure/playwright-best-practices/)
- [Convex Agent Skills — Backend Platform Setup](/hermes/skills/catalog/convex-agent-skills-setup/)
