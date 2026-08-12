---
title: New Skills — August 12, 2026
description: 7 newly discovered Hermes Agent skills from skills.sh marketplace sweep — HeartMuLa music generation, simplify-code parallel review, ideation brainstorming, subagent-driven development, Linear integration, webhook subscriptions, and grounded citations.
---

# New Skills — August 12, 2026

**Source:** [skills.sh](https://skills.sh) via `npx skills search`
**Date:** August 12, 2026
**Total new this batch:** 7 skills

Routine daily sweep of the skills.sh marketplace. After cross-referencing the full 215-skill `nousresearch/hermes-agent` catalog against 380+ documented skills in `hermes/skills/catalog/`, 7 skills were identified as uncataloged and received setup guides.

---

## New Skills (7)

| # | Skill | Installs | Source | Setup Guide |
|---|-------|----------|--------|-------------|
| 1 | `heartmula` | 224 | nousresearch/hermes-agent | [heartmula-setup.md](/hermes/skills/catalog/heartmula-setup) ✍️ |
| 2 | `simplify-code` | 187 | nousresearch/hermes-agent | [simplify-code-setup.md](/hermes/skills/catalog/simplify-code-setup) ✍️ |
| 3 | `ideation` | 111 | nousresearch/hermes-agent | [ideation-setup.md](/hermes/skills/catalog/ideation-setup) ✍️ |
| 4 | `subagent-driven-development` | 88 | nousresearch/hermes-agent | [subagent-driven-development-setup.md](/hermes/skills/catalog/subagent-driven-development-setup) ✍️ |
| 5 | `linear` | 80 | nousresearch/hermes-agent | [linear-setup.md](/hermes/skills/catalog/linear-setup) ✍️ |
| 6 | `webhook-subscriptions` | 80 | nousresearch/hermes-agent | [webhook-subscriptions-setup.md](/hermes/skills/catalog/webhook-subscriptions-setup) ✍️ |
| 7 | `grounded-citations` | 22 | nousresearch/hermes-agent | [grounded-citations-setup.md](/hermes/skills/catalog/grounded-citations-setup) ✍️ |

---

## Skill Highlights

### heartmula — Open-Source Suno Alternative (224 installs)
Apache 2.0 licensed music generation. Four-model pipeline: HeartMuLa generates from lyrics + tags, HeartCodec decodes to audio, HeartTranscriptor transcribes vocals, HeartCLAP verifies style alignment. Runs locally, no API keys, full ownership of output.

### simplify-code — Four Parallel Code Reviewers (187 installs)
Cleanup pass with four concurrent reviewers: Reuse, Quality, Efficiency, Altitude. Each hunts its own problem class. Four reviewers, one review's latency. Complements `requesting-code-review` (bug hunt) with waste reduction.

### subagent-driven-development — Multi-Agent Task Dispatch (88 installs)
Fresh subagent per task with automated two-stage review. Consumes `plan` skill output. Clean context isolation prevents cross-task errors. Automated gating between steps.

### grounded-citations — Verifiable Source Chains (22 installs)
Low install count but high research integrity value. Perplexity-style inline citations with ledger-owned URL mapping. Verbatim quote verification. `verify --evidence` command. Integrates with `research-paper-writing` for academic pipelines.

---

## Installation

```bash
# HeartMuLa — AI Music Generation
npx skills add nousresearch/hermes-agent --skill heartmula

# Simplify Code — Parallel Review
npx skills add nousresearch/hermes-agent --skill simplify-code

# Creative Ideation
npx skills add nousresearch/hermes-agent --skill ideation

# Subagent-Driven Development
npx skills add nousresearch/hermes-agent --skill subagent-driven-development

# Linear Integration
npx skills add nousresearch/hermes-agent --skill linear

# Webhook Subscriptions
npx skills add nousresearch/hermes-agent --skill webhook-subscriptions

# Grounded Citations
npx skills add nousresearch/hermes-agent --skill grounded-citations
```

---

## Coverage Progress

| Metric | Aug 11 | Aug 12 | Progress |
|--------|--------|--------|----------|
| Catalog entries | ~363 | ~370 | +7 |
| nousresearch/hermes-agent coverage | ~175/215 | ~182/215 | 84.7% documented |
| Remaining uncataloged | ~40 | ~33 | Closing in on full coverage |

---

*← [Skills Home](/hermes/skills/) | [Skills Catalog](/hermes/skills/catalog/) | [Previous Sweep →](/hermes/skills/marketplace/new-aug11-2026/)*

*Powered by CorpusIQ*
