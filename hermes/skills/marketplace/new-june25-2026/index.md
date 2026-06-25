---
title: New June 25, 2026 — 33 GBrain Skills Discovered
description: 33 newly catalogued GBrain skills from garrytan/gbrain — agent identity, orchestration, quality gates, scheduling, research, and brain management tools for Hermes Agents.
---

# New Skills Discovered — June 25, 2026

**Source:** [garrytan/gbrain](https://skills.sh/garrytan/gbrain) via [skills.sh](https://skills.sh)
**Total new:** 33 skills | **Combined installs:** 2,802+
**Date:** June 25, 2026

A major expansion of the GBrain ecosystem — 33 previously uncatalogued skills from Garry Tan's agent brain layer. These span agent identity generation, subagent orchestration, quality gates, scheduling, research augmentation, and brain knowledge management. All compatible with Hermes Agent via the OpenClaw/Hermes runtime.

---

## High-Value Tier (100+ installs)

| Skill | Installs | Description |
|---|---|---|
| **cross-modal-review** | 135 | Quality gate via second model. Spawn a different AI model to review work before committing. Includes refusal routing and Codex code-review handoff. |
| **soul-audit** | 134 | 6-phase interactive interview generating agent identity (SOUL.md), user profile, access control, and operational cadence. Re-runnable anytime. |
| **cron-scheduler** | 134 | Schedule management with staggering, quiet hours, and wake-up override for agent automation. |
| **daily-task-prep** | 134 | Morning preparation: calendar lookahead, meeting context loading, open threads synthesis. |
| **skillify** | 133 | The meta skill — turn any raw feature into a properly-skilled, tested, documented skill following GBrain conformance standards. |
| **repo-architecture** | 132 | Decision protocol for filing brain pages by primary domain, functional area, and lifecycle stage. |
| **signal-detector** | 132 | Always-on ambient signal capture. Fires on every inbound message to detect actionable signals. |
| **skill-creator** | 130 | Create new skills following the GBrain conformance standard. Generates SKILL.md with triggers, tools, and mutating flags. |
| **webhook-transforms** | 125 | Generic framework for converting external events (SMS, meetings, social mentions) into structured brain pages. |
| **minion-orchestrator** | 124 | Unified Minions skill for deterministic shell jobs and LLM subagent orchestration. Durable, observable, steerable queue interface. |
| **skillpack-check** | 120 | Run `gbrain skillpack-check` to produce an agent-readable JSON health report covering all installed skills. |
| **smoke-test** | 110 | Post-restart smoke tests + auto-fix for gbrain and OpenClaw environments. |
| **frontmatter-guard** | 109 | Validate and auto-repair YAML frontmatter on brain pages. Catches malformed metadata before it corrupts the knowledge base. |

## Mid-Value Tier (50–99 installs)

| Skill | Installs | Description |
|---|---|---|
| **book-mirror** | 96 | Take any book (EPUB/PDF), produce personalized chapter-by-chapter analysis with two-column tables mapping ideas to the reader's life using brain context. |
| **strategic-reading** | 92 | Read content through a specific strategic problem lens, producing an applied playbook mapping insights to decisions. |
| **academic-verify** | 92 | Verify research claims by tracing publication → methodology → raw data → independent replication. Routes through multiple verification layers. |
| **perplexity-research** | 90 | Brain-augmented web research. Sends brain context to Perplexity, returns what is NEW vs what the brain already knows. |
| **article-enrichment** | 89 | Transform raw article dumps into structured pages with executive summary, key insights, and why-it-matters analysis. |
| **brain-pdf** | 89 | Generate publication-quality PDF from any brain page via gstack make-pdf binary. Strips YAML frontmatter, applies headers and formatting. |
| **concept-synthesis** | 89 | Deduplicate and synthesize raw concept stubs into a tiered intellectual map (T1 Canon to T4 Riff), tracing idea evolution across sources. |
| **archive-crawler** | 89 | Universal archivist for personal file archives (Dropbox, B2, Gmail takeout, local mounts). Filters for high-value user-authored content. |
| **voice-note-ingest** | 88 | Ingest voice notes with exact-phrasing preservation. Routes content to proper brain categories (concepts, people, companies, ideas). |
| **ask-user** | 81 | Reusable pattern for presenting the user with explicit choices and gating decisions that require human judgment. |
| **functional-area-resolver** | 72 | Compress an agent's routing file (RESOLVER.md) by converting functional area mappings into compact decision trees. |
| **skillpack-harvest** | 61 | Lift a proven skill from a host repo (e.g., OpenClaw fork) back into the canonical gbrain skillpack for reuse. |

## Lower-Value Tier (<50 installs)

| Skill | Installs | Description |
|---|---|---|
| **schema-author** | 55 | Evolve the brain's schema pack: add page types, propose new ones from corpus scans, backfill page.type, audit pack health. |
| **eiirp** | 55 | "Everything In Its Right Place" — universal post-work organizer that files output into proper brain locations after any task. |
| **brain-taxonomist** | 55 | Filing gate for ALL brain writes. Consulted before creating any new page to ensure proper taxonomy placement. |
| **schema-unify** | 47 | Migrate a brain from gbrain-base to gbrain-base-v2's 14-canonical-type taxonomy via the unify-types Minion handler. |
| **skill-optimizer** | 40 | Self-evolving skill optimization via SkillOpt-paper-grounded text-space optimizer. Improves skills based on usage patterns. |
| **gbrain-upgrade** | 31 | Keep gbrain current. Automatically detects version drift and runs upgrade sequences with rollback protection. |
| **idea-lineage** | 26 | Trace one idea's evolution through the brain: first mention, best articulation, current state, and derivative concepts. |
| **gbrain-advisor** | 9 | Proactive "make the most of gbrain" coaching. Analyzes usage patterns and suggests underutilized capabilities. |

---

## Installation

All skills install via `npx skills add`:

```bash
# High-value tier (recommended for all Hermes agents)
npx skills add garrytan/gbrain/cross-modal-review
npx skills add garrytan/gbrain/soul-audit
npx skills add garrytan/gbrain/cron-scheduler
npx skills add garrytan/gbrain/daily-task-prep
npx skills add garrytan/gbrain/skillify
npx skills add garrytan/gbrain/repo-architecture
npx skills add garrytan/gbrain/signal-detector
npx skills add garrytan/gbrain/skill-creator
npx skills add garrytan/gbrain/webhook-transforms
npx skills add garrytan/gbrain/minion-orchestrator
npx skills add garrytan/gbrain/skillpack-check
npx skills add garrytan/gbrain/smoke-test
npx skills add garrytan/gbrain/frontmatter-guard

# Mid-value tier (domain-specific)
npx skills add garrytan/gbrain/book-mirror
npx skills add garrytan/gbrain/strategic-reading
npx skills add garrytan/gbrain/academic-verify
npx skills add garrytan/gbrain/perplexity-research
npx skills add garrytan/gbrain/article-enrichment
npx skills add garrytan/gbrain/brain-pdf
npx skills add garrytan/gbrain/concept-synthesis
npx skills add garrytan/gbrain/archive-crawler
npx skills add garrytan/gbrain/voice-note-ingest
npx skills add garrytan/gbrain/ask-user
npx skills add garrytan/gbrain/functional-area-resolver
npx skills add garrytan/gbrain/skillpack-harvest
```

## Key Use Cases for CorpusIQ Agents

| Use Case | Skills |
|---|---|
| **Agent identity & governance** | soul-audit, frontmatter-guard, conventions |
| **Quality assurance** | cross-modal-review, smoke-test, skillpack-check |
| **Daily operations** | daily-task-prep, cron-scheduler, eiirp |
| **Knowledge management** | repo-architecture, brain-taxonomist, concept-synthesis, article-enrichment |
| **Research & intelligence** | perplexity-research, academic-verify, strategic-reading, signal-detector |
| **Skill development** | skillify, skill-creator, skill-optimizer, skillpack-harvest |
| **Orchestration** | minion-orchestrator, webhook-transforms, ask-user |
| **Content ingestion** | book-mirror, voice-note-ingest, archive-crawler, brain-pdf |
| **System maintenance** | gbrain-upgrade, schema-author, schema-unify, functional-area-resolver |

## Previous GBrain Skills (Already Catalogued)

These 20 skills were catalogued in [new-june18-2026-ecosystem](../new-june18-2026-ecosystem/index.md):
brain-ops, idea-ingest, query, maintain, meeting-ingestion, enrich, data-research, citation-fixer, media-ingest, daily-task-manager, briefing, ingest, testing, reports, migrate, publish, capture, setup, conventions, install

---

*← [Marketplace Overview](/hermes/skills/marketplace/) | [Skills Catalog](/hermes/skills/catalog/) →*
*Curated by CorpusIQ — one MCP endpoint, all your business tools. Content remains attributed to original authors and repositories.*
