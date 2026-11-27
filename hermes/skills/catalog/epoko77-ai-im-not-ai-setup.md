---
title: "IM NOT AI - Korean AI Text Humanizer Setup"
description: "epoko77-ai/im-not-ai - 3.4K combined installs: a Korean AI-text humanizer that rewrites machine-written Hangul and flags translationese."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/epoko77-ai-im-not-ai-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "korean", "writing", "humanizer"]
---

# IM NOT AI - Setup Guide

**Source:** [epoko77-ai/im-not-ai](https://www.skills.sh/epoko77-ai/im-not-ai) via skills.sh - 3.4K combined installs across 5 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 evening sweep)
**GitHub:** [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) - 6,800 stars, MIT license, last pushed Nov 23, 2026, main branch; four skills at skills/<name>/SKILL.md plus commit-ko at extras/skills/commit-ko/SKILL.md.
**Category:** Korean Writing (AI Text Humanizer)
**Quality Tier:** 🟡 Yellow - five sampled verdicts are mostly Pass with Warn cells on humanize (Socket) and humanize-scan (Snyk); no Fails.

epoko77-ai/im-not-ai is a Korean AI-text humanizer: it detects the tells of machine-written Hangul and rewrites the style, rhythm, and wording so the result reads as natural human prose, while leaving facts, claims, numbers, proper nouns, and direct quotes untouched. The detection taxonomy covers ten categories and 85 sub-patterns, including translationese, mechanical parallelism, excessive English quotes, formulaic idioms, overuse of the passive voice, piled-up sentence-initial conjunctions, uniform sentence rhythm, and overuse of emoji and bullets.

The suite ships four main skills under skills/ plus one opt-in extra. humanize-korean is the orchestrator that runs the rewrite, humanize is the entry command that launches the pipeline, and humanize-redo and humanize-scan are the redo and scan stages of the same pipeline. commit-ko, a standalone commit-message naturalizer, lives under extras/skills/. The repository is MIT-licensed, holds 6,800 stars, and was last pushed Nov 23, 2026 at version v2.4.8.

## Installation

The repository supports Claude Code, GitHub Copilot CLI, Codex CLI, and Gemini CLI. The recommended path is each runtime's plugin marketplace, which installs without cloning.

Claude Code (plugin marketplace):

```
/plugin marketplace add epoko77-ai/im-not-ai
/plugin install humanize-korean@im-not-ai
```

GitHub Copilot CLI (plugin marketplace):

```bash
copilot plugin marketplace add epoko77-ai/im-not-ai
copilot plugin install humanize-korean@im-not-ai
copilot plugin list
```

Clone plus script (Claude Code, Codex CLI, and Gemini CLI):

```bash
git clone https://github.com/epoko77-ai/im-not-ai.git
cd im-not-ai
./install.sh
```

The script auto-detects the installed runtimes; restrict it with ./install.sh --claude-only, --codex-only, or --gemini-only. Update with ./update.sh and remove with ./uninstall.sh.

Gemini CLI (remote install, Gemini CLI 0.14.0 or newer):

```bash
gemini extensions install https://github.com/epoko77-ai/im-not-ai.git
```

The commit-ko extra sits outside the default plugin and install.sh scope; install it separately with ./install.sh --extras.

## What It Provides

skills.sh publishes a per-skill install count for the five indexed listings. Three of the four main skills are stages of one humanizing pipeline: humanize-korean rewrites, humanize-redo redoes, and humanize-scan scans.

| Skill | Installs | Use For |
|---|---|---|
| humanize-korean | 1,180 | Orchestrator stage that diagnoses and rewrites machine-written Korean across ten categories and 85 AI-tell sub-patterns, routing light, standard, or heavy paths |
| humanize | 876 | Entry command (/humanize) that launches the humanize-korean pipeline on the route_hint path; --strict forces the heavy path |
| humanize-redo | 839 | Redo stage that re-runs the most recent rewrite for a second pass, targeting a specific category, paragraph, or intensity |
| humanize-scan | 463 | Scan stage that scores how much AI-tell a Korean text carries and shows sample before/after fixes before committing to a full rewrite |

The remaining 1 indexed listing is commit-ko (6 installs), a standalone opt-in skill that rewrites AI-suggested Korean commit messages into natural developer phrasing.

## Why This Matters for Hermes Agents

Korean machine text has a distinct failure mode that general humanizers miss: most of its tells come from English translationese, so an English-oriented rewording tool leaves them in place. This suite is built specifically for Hangul, with a single source of truth taxonomy of ten categories and 85 sub-patterns, and it routes each text through a light, standard, or heavy path based on a deterministic pre-score rather than a blanket rewrite. That keeps well-written text cheap (one call) and reserves the multi-call diagnose-then-rewrite-then-finalize path for the worst cases, with a structural convergence gate checking character change rate, diagnosis-goal convergence, and parallel-structure survival on every path.

For a Hermes agent the redo and scan stages are the useful loop: scan answers whether a full rewrite is worth running at all, and redo lets the agent re-target a specific category or paragraph after the first pass. The MIT license covers the code, skill definitions, agent definitions, and taxonomy documents, so the pipeline can be integrated and forked. The trade-off is language: the instruction sets, references, and trigger prompts are Korean, so an agent that does not write Korean gains nothing here.

## Usage

| You say | What happens |
|---|---|
| Humanize this Korean draft | humanize-korean diagnoses the text and rewrites style, rhythm, and wording, leaving facts, numbers, proper nouns, and quotes intact |
| /humanize draft.md | Runs the entry command, which pre-scores the text and routes it to a light, standard, or heavy rewrite path |
| /humanize-scan this text | Scores how much AI-tell the text carries and returns sample before/after fixes for the top signals, without a full rewrite |
| /humanize-redo "translationese only" | Re-runs the most recent rewrite targeting just the translationese category |
| Make this commit message sound human | commit-ko strips office-style phrasing from the suggested Korean commit message in one pass |

## Verification

Confirm the skill bodies resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/epoko77-ai/im-not-ai/main/skills/humanize-korean/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/epoko77-ai/im-not-ai/main/skills/humanize/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/epoko77-ai/im-not-ai/main/skills/humanize-redo/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/epoko77-ai/im-not-ai/main/skills/humanize-scan/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/epoko77-ai/im-not-ai/main/extras/skills/commit-ko/SKILL.md | head -40
```

All five URLs return 200. After installing, read each SKILL.md and its references before relying on it.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| humanize-korean | Pass | Pass | Pass |
| humanize | Pass | Warn | Pass |
| humanize-redo | Pass | Pass | Pass |
| humanize-scan | Pass | Pass | Warn |
| commit-ko | Pass | Pass | Pass |

Across the 5 sampled skills there are 13 Pass, 2 Warn, and 0 Fail cells; the Warns are Socket on humanize and Snyk on humanize-scan.

## Limitations

- Snapshot data, verified Nov 26, 2026: 3,364 combined installs across 5 indexed listings; 6,800 GitHub stars; MIT license; last pushed Nov 23, 2026. Counts drift over time.
- The skill bodies, references, and trigger prompts are Korean; the English descriptions in this guide are summaries, and the suite gives no coverage for non-Korean text.
- The taxonomy is a classifier, not proof of authorship: the README documents a reproduced false positive where a pre-2020 human essay scored maximum risk from one author's comma habit, and states that a single metric is never evidence of AI writing.
- The Gemini CLI extension ships a separate 47-pattern rulebook (extension 1.5.0) that does not apply the main 85-pattern taxonomy, the three route_hint paths, or the deterministic gates.
- Two sampled skills carry a Warn (Socket on humanize, Snyk on humanize-scan), so re-check those security pages on skills.sh before production use.
- The commit-ko extra is outside the default plugin and install.sh scope and must be installed separately with ./install.sh --extras.

## Related

[Korean Skills - Hangul Writing and Style Checks](/hermes/skills/catalog/korean-skills-setup) | [K-Skill - Korean Agent Skills Setup](/hermes/skills/catalog/k-skill-setup) | [Humanizer Setup](/hermes/skills/catalog/humanizer-setup) | [Ultimate Humanizer Setup](/hermes/skills/catalog/ultimate-humanizer-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run /humanize-scan first to see whether a full rewrite is worth the calls; it finishes inside the current conversation with no workspace files or subagents.
- Trust the light path for well-written text: the route_hint pre-score keeps single-call rewrites cheap and reserves the heavy path for dense slop or very long inputs.
- Use /humanize-redo with a category name (such as translationese) to re-target one finding instead of re-running the whole pipeline.
- Install commit-ko separately with ./install.sh --extras; it is not part of the default plugin or script install.
- Keep the references folder together with each SKILL.md; the taxonomy, rewriting playbook, and quick-rules files load by relative path.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
