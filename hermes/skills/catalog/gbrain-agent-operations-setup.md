---
title: GBrain Agent Operations — Full Setup Guide for Hermes Agents
description: Install, configure, and use GBrain operational skills for Hermes Agents — cross-modal review, soul audit, cron scheduling, minion orchestration, and daily task preparation.
---

# GBrain Agent Operations — Setup Guide

**Source:** [garrytan/gbrain](https://skills.sh/garrytan/gbrain) (24,066 ⭐)
**Category:** Agent Operations & Knowledge Management

GBrain is Garry Tan's opinionated agent brain layer for OpenClaw and Hermes Agent. This guide covers the operational skills that power agent identity, quality gates, scheduling, orchestration, and daily workflows.

---

## Installation

Install the complete operational skillset in one shot:

```bash
# Core operational skills
npx skills add garrytan/gbrain/cross-modal-review
npx skills add garrytan/gbrain/soul-audit
npx skills add garrytan/gbrain/cron-scheduler
npx skills add garrytan/gbrain/daily-task-prep
npx skills add garrytan/gbrain/minion-orchestrator
npx skills add garrytan/gbrain/skillify
npx skills add garrytan/gbrain/skill-creator
npx skills add garrytan/gbrain/skillpack-check
npx skills add garrytan/gbrain/smoke-test
npx skills add garrytan/gbrain/frontmatter-guard
npx skills add garrytan/gbrain/repo-architecture
npx skills add garrytan/gbrain/signal-detector
npx skills add garrytan/gbrain/webhook-transforms

# Knowledge management
npx skills add garrytan/gbrain/perplexity-research
npx skills add garrytan/gbrain/article-enrichment
npx skills add garrytan/gbrain/concept-synthesis
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **GBrain installed** | `git clone https://github.com/garrytan/gbrain.git ~/corpusiq-brain && cd ~/corpusiq-brain && bun install` |
| **Bun runtime** | GBrain requires Bun. Install: `curl -fsSL https://bun.sh/install | bash` |
| **OpenAI-compatible endpoint** | For cross-modal-review: any OpenAI-compatible API (local Ollama, DeepSeek, Anthropic via proxy) |
| **Hermes Agent** | v0.16.0+ recommended for full skill compatibility |
| **Perplexity API key** | Required for perplexity-research skill only. Set `PERPLEXITY_API_KEY` in env. |

---

## Key Capabilities

### Core Operational Skills

| Capability | How to Trigger | Notes |
|---|---|---|
| **Cross-Modal Review** | "second opinion", "cross-modal review", "double check this", "adversarial review" | Spawns second model to review work before committing. Routes refusals silently. |
| **Soul Audit** | "soul audit", "customize agent", "who am I", "set up identity" | 6-phase interactive interview generating SOUL.md, USER.md, ACCESS_POLICY.md, HEARTBEAT.md |
| **Cron Scheduler** | "schedule this", "set up a cron", "run daily at 6 PM" | Manages staggered schedules, quiet hours, wake-up overrides |
| **Daily Task Prep** | "morning prep", "what's on my calendar", "prepare for today" | Calendar lookahead, meeting context loading, open threads synthesis |
| **Minion Orchestrator** | "submit a gbrain job", "spawn agent", "check on agent", "what's running" | Unified queue for shell jobs and LLM subagents. Durable, observable, steerable. |
| **Skillify** | "turn this into a skill", "make a skill from this workflow" | Meta skill: converts raw features into conformant SKILL.md files |
| **Skill Creator** | "create a skill for X", "make a new skill" | Template-driven SKILL.md generator with trigger mapping and tool declarations |
| **Skillpack Check** | `gbrain skillpack-check` | Generates agent-readable JSON health report on all installed skills |
| **Smoke Test** | "run smoke tests", "verify environment" | Post-restart validation with auto-fix for gbrain and OpenClaw |
| **Frontmatter Guard** | Automatic on every brain write | Validates and auto-repairs YAML frontmatter on brain pages |

### Knowledge Management Skills

| Capability | How to Trigger | Notes |
|---|---|---|
| **Repo Architecture** | "where should I file this", "which category" | Decision protocol for filing brain pages by domain and lifecycle |
| **Signal Detector** | Always-on, fires on every inbound message | Detects actionable signals from messages, emails, notifications |
| **Webhook Transforms** | "set up webhook for X", "ingest from webhook" | Converts external events (SMS, meetings, social) into structured brain pages |
| **Perplexity Research** | "research X with brain context", "what's new about Y" | Brain-augmented web research — returns what's NEW vs what the brain already knows |
| **Article Enrichment** | "enrich this article", "structure this dump" | Transforms raw text dumps into structured pages with executive summaries |
| **Concept Synthesis** | "synthesize concepts", "map my ideas" | Deduplicates and organizes concepts into tiered intellectual maps |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Agent identity governance** | Run soul-audit to generate/update agent SOUL.md after any behavior change. Frontmatter-guard prevents metadata corruption across 400+ brain pages. |
| **Pre-deployment quality gates** | Cross-modal review on all public content and code before pushing. Smoke-test after every Hermes restart to verify toolchain health. |
| **Scheduled content operations** | Cron-scheduler manages 6 PM daily reports, morning video generation, and weekly performance audits with quiet-hour awareness. |
| **Multi-agent fan-out** | Minion-orchestrator spawns parallel research subagents for competitive analysis, prospect research, and content mining — all from a single queue. |
| **Skill development pipeline** | Skillify converts proven workflows into reusable skills. Skill-creator generates conformant SKILL.md. Skillpack-check audits the installed skillset. |
| **Daily intelligence brief** | Daily-task-prep loads calendar + open threads + brain context. Signal-detector surfaces high-priority inbound signals. Combined, this replaces manual morning triage. |
| **Knowledge synthesis** | Concept-synthesis maps ideas across brain sections. Article-enrichment structures raw research. Together, they turn information firehose into actionable intelligence. |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| **cross-modal-review: "no second model configured"** | Set `OPENAI_BASE_URL` and `OPENAI_API_KEY` in your environment. The skill spawns any OpenAI-compatible model. |
| **soul-audit: generates empty files** | Ensure the `templates/` directory exists at `SKILL_DIR/skills/soul-audit/templates/`. The skill reads template scaffolds, not ships pre-filled content. |
| **minion-orchestrator: jobs stuck in queue** | Run `gbrain jobs list` to see active jobs. Use `gbrain jobs cancel <id>` for stuck jobs. Restart the gbrain daemon if queue is unresponsive. |
| **skillpack-check: returns empty report** | Run `gbrain skillpack-check --rebuild-cache` to regenerate the skill index. First run after install may need cache priming. |
| **"gbrain: command not found" after install** | Add `export PATH="$HOME/.bun/bin:$HOME/corpusiq-brain/bin:$PATH"` to your shell profile. The CLI lives in the repo's `bin/` directory. |
| **frontmatter-guard: false positive on valid YAML** | The validator enforces strict GBrain schema. Custom frontmatter fields outside the schema trigger warnings. Run `gbrain schema-author --add-field <name>` to register new fields. |

## Verification

```bash
# Verify GBrain is installed and reachable
cd ~/corpusiq-brain && gbrain --version

# List all installed gbrain skills
gbrain skillpack-check 2>&1 | head -20

# Test cross-modal review (will use current model if no second configured)
echo "test" | gbrain cross-modal-review --dry-run

# Run smoke tests
gbrain smoke-test
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Discovery Page](/hermes/skills/marketplace/new-june25-2026/) →*
*Curated by CorpusIQ — one MCP endpoint, all your business tools. Content remains attributed to original authors and repositories.*
