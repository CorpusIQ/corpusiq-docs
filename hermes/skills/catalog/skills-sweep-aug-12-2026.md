---
title: Skills.sh Sweep — August 12, 2026
description: Automated marketplace sweep discovering 7 new/undocumented Hermes Agent skills from the 215-skill nousresearch/hermes-agent catalog. 7 setup guides drafted and pushed.
date: 2026-08-12
sweep_id: aug-12-2026-cron
total_discovered: 215
new_skills: 7
guides_drafted: 7
---

# Skills.sh Sweep — August 12, 2026 (Cron Update)

Automated discovery sweep across the [skills.sh](https://skills.sh) marketplace. Cross-referenced the full 215-skill `nousresearch/hermes-agent` catalog plus external marketplace listings against the existing 380+ entry catalog at `corpusiq-docs/hermes/skills/catalog/`.

**Result:** 7 skills not yet cataloged. All 7 setup guides drafted.

---

## 🆕 New Skills Discovered (7)

| Skill | Installs | Source | Setup Guide |
|-------|----------|--------|-------------|
| `heartmula` | 224 | nousresearch/hermes-agent | [heartmula-setup.md](heartmula-setup.md) ✍️ |
| `simplify-code` | 187 | nousresearch/hermes-agent | [simplify-code-setup.md](simplify-code-setup.md) ✍️ |
| `ideation` | 111 | nousresearch/hermes-agent | [ideation-setup.md](ideation-setup.md) ✍️ |
| `subagent-driven-development` | 88 | nousresearch/hermes-agent | [subagent-driven-development-setup.md](subagent-driven-development-setup.md) ✍️ |
| `linear` | 80 | nousresearch/hermes-agent | [linear-setup.md](linear-setup.md) ✍️ |
| `webhook-subscriptions` | 80 | nousresearch/hermes-agent | [webhook-subscriptions-setup.md](webhook-subscriptions-setup.md) ✍️ |
| `grounded-citations` | 22 | nousresearch/hermes-agent | [grounded-citations-setup.md](grounded-citations-setup.md) ✍️ |

---

## Skill Details

### 1. heartmula (224 installs)
Open-source AI music generation with HeartMuLa models (Apache 2.0). Four-model pipeline: HeartMuLa (3B/7B music LM), HeartCodec (12.5Hz audio codec), HeartTranscriptor (Whisper-based lyrics), HeartCLAP (audio-text alignment). Suno/Udio alternative — local, offline, no API keys.

### 2. simplify-code (187 installs)
Parallel code review with four focused reviewers running concurrently: Reuse (DRY), Quality (maintainability), Efficiency (performance), Altitude (architecture). Cleanup pass, not bug hunt — removes duplication, flattens complexity, cuts waste. Each reviewer runs in parallel.

### 3. ideation (111 installs)
Constraint-driven creative ideation. Generates 3 concrete project ideas from a creative constraint library, then builds the chosen one. Philosophy: constraint + direction = creativity. Works for code, art, hardware, tools.

### 4. subagent-driven-development (88 installs)
Multi-agent development workflow. Dispatches fresh subagents per task with systematic two-stage review (spec compliance then quality). Clean context per task, automated gating between steps. Consumes `plan` skill output.

### 5. linear (80 installs)
Linear.app integration via GraphQL API using curl. No MCP server, no OAuth — just an API key. Manage issues, projects, sprints, and team workloads from Hermes. Both UUID and short IDs (ENG-123) work.

### 6. webhook-subscriptions (80 installs)
External service webhook triggers for Hermes. GitHub pushes, Stripe events, CI/CD completions become agent triggers. HMAC signature verification, per-subscription routing, dynamic subscription management.

### 7. grounded-citations (22 installs)
Perplexity-style inline citations with verifiable source chains. Ledger-owned `url → [n]` mapping, verbatim quote verification, `[unverified]` flagging for model knowledge. `verify --evidence` command for fact-checking. Integrates with `research-paper-writing`.

---

## 📊 Existing Skills Verified (200+)

Full cross-reference against the 215-skill nousresearch/hermes-agent catalog confirmed the remaining 200+ skills are already cataloged, including all top-20 by installs: dogfood (5.4K), humanizer (740), hermes-tweet (695), popular-web-designs (563), yuanbao (561), hermes-agent (533), powerpoint (475), google-workspace (428), arxiv (424), research-paper-writing (397), claude-design (392), llm-wiki (371), jupyter-live-kernel (356), excalidraw (345), ascii-art (343), youtube-content (337), imessage (332), design-md (332), songwriting-and-ai-music (325), architecture-diagram (322).

---

## 🔍 Methodology

- **4 search queries** across skills.sh CLI:
  - `hermes` (20 results)
  - `hermes agent` (20 results)
  - `hermes skill` (20 results)
  - Full `nousresearch/hermes-agent` page scrape (215 skills)
- **Cross-referenced** against 380+ existing catalog entries
- **7 setup guides** drafted for all uncataloged skills
- **Sweep report** published to `marketplace/new-aug12-2026/`

---

## 📈 Ecosystem Growth

| Metric | Aug 10 (Pass 2) | Aug 11 | Aug 12 | Delta |
|--------|-----------------|--------|--------|-------|
| Catalog entries | 358+ | 363+ | 370+ | +7 |
| Official skills tracked | 34 | 36 | 43 | +7 |
| Guides drafted this sweep | — | 5 | 7 | +7 |
| nousresearch/hermes-agent coverage | ~170/215 | ~175/215 | ~182/215 | +7 |

---

**Next sweep:** Automated cron — next run.

*Powered by CorpusIQ*
