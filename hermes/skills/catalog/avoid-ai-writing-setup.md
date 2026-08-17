---
title: "Avoid AI Writing — AI-Pattern Audit & Rewrite Setup"
description: "conorbronsdon/avoid-ai-writing — 1 skill, 1.6K installs, 3.0K GitHub stars: audit and rewrite content to remove AI writing patterns, with rewrite, flag, and review modes. Installed in the CorpusIQ production profile."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/avoid-ai-writing-setup/"
robots: "index,follow"
last_updated: "2026-08-17"
tags: ["hermes skill", "agent skill", "skill setup", "writing", "content quality", "ai-detection"]
---

# Avoid AI Writing — Setup Guide

**Source:** [conorbronsdon/avoid-ai-writing](https://skills.sh/conorbronsdon/avoid-ai-writing)
**GitHub:** [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing)
**Skills:** 1 skill · 1.6K installs
**Category:** Content Quality
**First Seen:** catalogued August 17, 2026 sweep (avoid-ai-writing on skills.sh since March 7, 2026)
**Quality Tier:** 🟡 Trusted — Snyk Warn named (see Limitations)

Avoid AI Writing audits content for AI writing patterns ("AI-isms") and rewrites them out. Its distinguishing trait is epistemic honesty: the skill opens by stating it is a writing-quality tool, not a verdict — citing the Stanford false-positive study on non-native English writers and the 2025 open-source detector misclassification research. Patterns are signals to pair with context, not proof.

---

## Installation

```bash
npx skills add conorbronsdon/avoid-ai-writing
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/conorbronsdon/avoid-ai-writing --skill avoid-ai-writing
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Prose to audit** | Any draft — post, email, doc, or page copy |

## What It Provides

Three operating modes:

| Mode | Purpose |
|---|---|
| `rewrite` (default) | Flag AI-isms and rewrite the text to fix them, including a built-in corrective second pass |
| `detect` | Flag AI-isms only — no rewriting ("scan," "flag only," "audit only") |
| `edit` | Edit a file in place with minimal, targeted changes; preserves already-human passages |

Optional voice profiles (casual / professional / technical / warm / blunt), context hints (linkedin, blog, investor-email, docs), and an iterate-to-convergence pass capped at 2 rounds round out the CLI surface.

The skill's built-in guardrails warn against using its signals as the sole basis for consequential decisions (academic integrity, hiring, publication) and note that the same patterns fire on second-language writing, deadline-pressed humans, and compressed technical genres.

## Quick Start

1. Install: `npx skills add conorbronsdon/avoid-ai-writing`
2. Ask: "audit this draft with avoid-ai-writing and rewrite it"
3. Review the flagged patterns; accept or reject each rewrite

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Already installed in production** | This skill runs in the CorpusIQ Hermes profile — this guide closes the docs-catalog gap |
| **Public content gate** | Pairs with content-voice rules and slop scoring before anything ships publicly |
| **Outreach email quality** | AI-ism audit on cold outreach and partner emails keeps the human voice |

## Limitations / Verification

- Security audits on avoid-ai-writing: Gen Agent Trust Hub Pass, Socket Pass, **Snyk Warn** — named per catalog policy
- Publisher-page install counts verified (1.6K); GitHub 3.0K stars on the repo
- Install count is below the usual drafting bar — catalogued because the skill is installed in the CorpusIQ production profile and was flagged as a docs gap by the August 17 ecosystem scan
- Signals are statistical, not proof — the skill itself says so and cites the research

```bash
npx skills add conorbronsdon/avoid-ai-writing   # verify install works
```

## Related

- [Stop Slop Setup](/hermes/skills/catalog/stop-slop-setup/)
- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
