---
title: "Lyndonkl Skills - Knowledge Work Library Setup"
description: "lyndonkl/claude: 12.8K combined installs across 96 indexed listings, a broad knowledge-work skill library for evaluation, memory and strategy."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/lyndonkl-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "thinking frameworks", "research", "academic writing"]
---

# Lyndonkl Skills - Setup Guide

**Source:** [lyndonkl/claude](https://www.skills.sh/lyndonkl/claude) via skills.sh - 12.8K combined installs across 96 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 199 stars, no LICENSE file, `main` branch, last pushed 2026-09-01, 271 skills plus 85 orchestrating agents under `skills/<name>/SKILL.md`
**Category:** Knowledge work / thinking, research and writing agent skills
**Quality Tier:** 🟡 Yellow - the repository ships no LICENSE file, so treat it as source-available rather than MIT-style open source.

This is a broad, production-ready library of thinking, research, writing and domain skills built for Claude Code: 271 skills and 85 orchestrating agents covering decision frameworks, forecasting, scientific writing, data visualization, GraphRAG, corporate finance and household finance. The indexed listings span evaluation rubrics, memory retrieval, strategy analysis, manuscript review, teaching scaffolds and grant proposals, so an agent can reach for a proven methodology instead of improvising.

Skills activate on trigger phrases and most work out of the box; only two need external tools (pandoc plus a LaTeX engine for markdown-to-pdf, and the textstat Python package for readability-check). Because the repository carries no LICENSE file, the catalog marks it Yellow even though every sampled skill passed its security scan.

## Installation

The README recommends the Claude Code plugin route:

```
/plugin marketplace add lyndonkl/claude
/plugin install thinking-frameworks-skills
```

Or install manually:

```bash
git clone https://github.com/lyndonkl/claude.git
cd claude
cp -r skills/* ~/.claude/skills/
```

Every skill becomes available immediately and activates on matching trigger phrases. Two skills are optional because of native dependencies; if their tools are missing they print the exact install commands and exit rather than failing silently.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| evaluation-rubrics | 792 | Design scoring rubrics with explicit criteria, scales and descriptors for consistent quality assessment. |
| memory-retrieval-learning | 500 | Build spaced-repetition and retrieval-practice learning plans for durable retention. |
| strategy-and-competitive-analysis | 499 | Develop business strategy with Porter's Five Forces, SWOT, Blue Ocean and the Good Strategy kernel. |
| scientific-manuscript-review | 484 | Review and edit IMRaD manuscripts for clarity, structure and scientific rigor. |
| socratic-teaching-scaffolds | 461 | Teach complex concepts through Socratic questioning and progressive scaffold removal. |
| grant-proposal-assistant | 353 | Write NIH and NSF grant proposals with fundable hypotheses, significance and approach. |
| chef-assistant | 289 | Cook by technique, food science and flavor architecture rather than rote recipes. |
| communication-storytelling | 246 | Turn analysis and data into persuasive narratives for a specific audience. |
| visual-storytelling-design | 235 | Turn data into visual narratives with annotation and honest framing. |
| financial-unit-economics | 200 | Analyze CAC, LTV, contribution margin and payback for business-model viability. |

The remaining 86 indexed listings range from 50 to 179 installs.

## Why This Matters for Hermes Agents

The library packages proven methodologies rather than generic advice, so a Hermes agent gets a specific, repeatable procedure for each task. Evaluation rubrics turn quality review into scored criteria with inter-rater reliability, memory retrieval builds spaced-repetition plans, and strategy analysis grounds a recommendation in Porter's Five Forces or the Good Strategy kernel rather than intuition. The scientific-writing cluster (manuscript review, grant proposals, teaching scaffolds) covers the academic workflow end to end, from drafting a fundable hypothesis to editing a submission for clarity and rigor. Every skill ships a SKILL.md plus templates, a methodology reference and a quality rubric, so an agent can self-check its own output against the same standard it was asked to meet. The trigger-phrase design means agents pay no context cost for skills they are not using, which matters for long multi-step runs. Only two skills need external tools, so the rest of the library drops into a Hermes agent environment without native dependencies.

## Usage

| You say | What happens |
|---|---|
| "Score these ten draft summaries" | Runs evaluation-rubrics to define criteria and grade each one consistently. |
| "I need to study for an exam" | Runs memory-retrieval-learning to schedule spaced repetition and retrieval practice. |
| "Should we enter this market?" | Runs strategy-and-competitive-analysis over Porter and SWOT frameworks. |
| "Review my paper before submission" | Runs scientific-manuscript-review for clarity, structure and rigor. |
| "Help me write my R01 specific aims" | Runs grant-proposal-assistant for significance, innovation and approach. |
| "Why is my chicken dry?" | Runs chef-assistant for technique and food-science fixes. |

## Verification

Probe skills on the `main` branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/lyndonkl/claude/main/skills/evaluation-rubrics/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/lyndonkl/claude/main/skills/memory-retrieval-learning/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/lyndonkl/claude/main/skills/strategy-and-competitive-analysis/SKILL.md
```

Skills live at `skills/<name>/SKILL.md` on `main`. The 96 indexed listings are a subset of the 271 skills in the tree, so confirm a specific skill exists before referencing it.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| evaluation-rubrics | Pass | Pass | Pass |
| memory-retrieval-learning | Pass | Pass | Pass |
| strategy-and-competitive-analysis | Pass | Pass | Pass |
| scientific-manuscript-review | Pass | Pass | Pass |
| socratic-teaching-scaffolds | Pass | Pass | Warn |
| grant-proposal-assistant | Pass | Pass | Pass |
| chef-assistant | Pass | Pass | Pass |
| communication-storytelling | Pass | Pass | Pass |
| visual-storytelling-design | Pass | Pass | Pass |
| financial-unit-economics | Pass | Pass | Pass |
| market-mechanics-betting | Pass | Pass | Pass |
| decision-matrix | Pass | Pass | Pass |
| bayesian-reasoning-calibration | Pass | Pass | Pass |
| chain-roleplay-debate-synthesis | Pass | Pass | Pass |
| data-schema-knowledge-modeling | Pass | Pass | Pass |
| brainstorm-diverge-converge | Pass | Pass | Pass |
| visualization-choice-reporting | Pass | Pass | Pass |
| expected-value | Pass | Pass | Pass |
| design-of-experiments | Pass | Pass | Pass |
| deliberation-debate-red-teaming | Pass | Pass | Pass |

The sample covers 20 of the 96 indexed listings; all 20 pass Gen Agent Trust Hub and Socket, and 19 pass Snyk (socratic-teaching-scaffolds carries a Snyk Warn).

## Limitations

- Snapshot data, verified 2026-11-17: 12,850 combined installs across 96 indexed listings; 199 GitHub stars; no LICENSE file; last pushed 2026-09-01. Counts drift over time.
- The repository ships no LICENSE file, so there is no stated permission to redistribute or reuse the skills; treat it as source-available until the author adds one.
- The repo is a large monorepo (1,371 files in the current tree) with 271 skills, 85 agents and a large `knowledge/` corpus; the skill-level verdicts cover the skills only.
- The index lists 96 listings while the README describes 271 skills, so indexed installs cover a subset of what the repository actually ships.
- Two skills need external tools (pandoc plus a LaTeX engine, and textstat) and exit with install instructions when those tools are missing.

## Related

- [Lenny Skills - PM Methodology from Lenny Rachitsky Setup](/hermes/skills/catalog/lenny-skills-setup)
- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)
- [Research Paper Writing Pipeline - Academic ML/AI Paper Production Setup](/hermes/skills/catalog/research-paper-writing-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load evaluation-rubrics before grading any batch of outputs; it turns subjective review into a scored, repeatable rubric.
- Pair strategy-and-competitive-analysis with decision-matrix when choosing between options so the recommendation is grounded and defensible.
- Use memory-retrieval-learning to design study plans for exams, certifications or onboarding new material.
- Reach for scientific-manuscript-review and grant-proposal-assistant together when preparing a paper or an NIH or NSF application.
- Install the native dependencies for markdown-to-pdf only if you need PDF reports; every other skill works out of the box.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
