---
title: "TypeSafe AI Skills - Typed AI Judgments Setup"
description: "Setup guide for the official TypeSafe skill: build with System One models that turn natural language into typed judgments and probabilities for code."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/typesafe-ai-setup/"
robots: "index,follow"
last_updated: "2026-10-08"
tags: ["hermes skill", "agent skill", "skill setup", "typesafe", "structured decisions", "ai infrastructure"]
---

# TypeSafe AI Skills - Setup Guide

**Source:** [typesafe-ai/skills](https://www.skills.sh/typesafe-ai/skills/typesafe-ai) via skills.sh - 88,323 installs (single skill); first seen Oct 8, 2026 (trending pass)
**GitHub:** [typesafe-ai/skills](https://github.com/typesafe-ai/skills) (2,632 stars, MIT license; skill at `skills/typesafe-ai/SKILL.md`, ~10 KB; last push Sep 12, 2026)
**Category:** AI Infrastructure / Application Development
**Quality Tier:** 🟡 Beta (official TypeSafe publisher; MIT; all sampled verdicts Pass; the product itself is in early access - flagged, verified Oct 8, 2026)

TypeSafe makes small units of AI intelligence usable like programming primitives. Its System One models - including the flagship Jev - turn natural language and application state into typed judgments and probabilities that code can compose. The official skill teaches an agent to design within that model: read the live docs, map a feature to the judgments it needs, choose primitives, and write the API or SDK code that consumes the results.

The skill's own framing: code owns the workflow, and the model supplies programmable common sense where ordinary code needs semantic understanding.

---

## Installation

```bash
# Claude Code plugin
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai

# Other agents via skills.sh
npx skills add typesafe-ai/skills --skill typesafe-ai
```

Installation is project-local by default; add `-g` to install globally. In Claude Code the plugin skill can be invoked explicitly with `/typesafe:typesafe-ai`.

## What It Provides

| Capability | How |
|---|---|
| The programming model | System One concepts and the "how to build" guide, read from the live documentation site |
| Use-case discovery | A use-case map plus cookbooks - function calling, speculative fan-out, value extraction, reranking, hierarchical classification, composite scoring, citation checks, extraction cascades |
| Judgment primitives | Choice (pick one of a defined set; the distribution compares competing options), Noul (probability that a condition holds), Score (probability-weighted position on ordered levels) |
| State and inputs | Guidance on preparing state (source text, identities, relationships, policies), named JSON fields, question instructions, and criteria |
| Confidence handling | How to decide uncertainty behavior and where to escalate to a person or a reasoning model |
| SDKs and API | HTTP API plus Python and JavaScript SDKs, with a migration guide for older integrations |
| Live-docs discipline | The skill reads the current docs as part of the task (Markdown-served documentation) instead of relying on baked-in knowledge |

## Why This Matters for Hermes Agents

Most agent pipelines eventually hit a step shaped like "understand this blob and pick what to do" - routing a ticket, grading a match, extracting a field, verifying a claim - and prompt-and-parse is the usual fragile answer. This skill offers a structured alternative: define the judgment, get a typed answer with a probability, and let code branch on it. Its design patterns (route and fill arguments, select instead of generate, verify and escalate) map directly onto agent workflow construction, and the skill is written to be driven by an agent rather than a human.

## Usage

| You say | What happens |
|---|---|
| "Use TypeSafe to route incoming support tickets by department, with human review for uncertain decisions" | The skill maps the task to Choice/Noul judgments, defines state and criteria, and writes the integration |
| "Turn this prompt-and-parse step into a structured decision" | It identifies the judgment the step really needs and replaces free-text output with a typed answer |
| "What could AI make possible in this app?" | It works from the use-case map and cookbooks to propose concrete, buildable directions |
| "Check whether this integration is current" | It reads the migration guide and current SDK reference before touching code |

## Verification

```bash
# Confirm the Claude Code plugin skill
claude plugin list | grep typesafe

# Confirm the skills.sh install
npx skills list | grep typesafe-ai

# The docs index the skill reads (source of truth)
# https://docs.typesafe.ai/llms.txt
```

## Security

skills.sh verdicts for the typesafe-ai skill (verified Oct 8, 2026):

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| typesafe-ai | Pass | Pass | Pass |

**Note:** capabilities depend on a live external service (TypeSafe's API, currently in early access, with pricing and limits set by TypeSafe). The skill itself is documentation-driven - it guides code and doc reading rather than executing opaque commands - but integrations call TypeSafe's hosted models and should be reviewed under your own data-handling rules.

## Related

- [OpenSpec Skills - Spec-Driven Development Suite Setup](/hermes/skills/catalog/fission-openspec-skills-setup) - another structured-planning-before-code discipline for agent workflows
- [ECC - Agent Harness Performance Optimization](/hermes/skills/catalog/ecc-agent-harness-setup) - agent harness patterns that pair with structured decision steps
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

1. **Start from behavior, not the model.** The skill's method: decide what the application should show, select, or hand off, then work backward to the judgments required.
2. **Ask independent questions together.** Parallel questions over the same state cannot see one another's answers; state speculative premises explicitly and let code consume whichever answers apply.
3. **Keep known rules in code.** Exact lookups, calculations, and deterministic logic stay ordinary code; reserve the model for semantic understanding.
4. **Read a cookbook before designing a classifier.** The closest cookbook often shows a better decomposition than a generic design.
5. **Measure request budgets.** Extra questions cost tokens; the skill calls for measuring cost and end-to-end latency against real workflows.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
