---
title: "ARIS Skills - Autonomous ML Research Setup"
description: "wanshuiyin/auto-claude-code-research-in-sleep: 44.0K combined installs across 88 listings, markdown skills for autonomous ML research and papers."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/auto-claude-code-research-in-sleep-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "ml research", "paper writing", "arxiv"]
---

# ARIS Skills - Setup Guide

**Source:** [wanshuiyin/auto-claude-code-research-in-sleep](https://www.skills.sh/wanshuiyin/auto-claude-code-research-in-sleep) via skills.sh - 44.0K combined installs across 88 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 19,359 stars, MIT license, `main` branch, last pushed 2026-11-17, one `SKILL.md` per skill under `skills/<name>/` plus `skills-codex/` and `skills-codex-*-review/` mirrors
**Category:** Autonomous ML research / paper-writing agent skills
**Quality Tier:** 🟡 Yellow - mixed Warn verdicts across the 20-skill sample (6 of 20 Trust Hub Warn, 9 of 20 Snyk Warn).

ARIS (Auto-Research-In-Sleep) is a markdown-only skill suite for autonomous machine-learning research. Its 88 indexed listings span the whole paper lifecycle: literature search over arXiv, Semantic Scholar and OpenAlex, idea discovery and novelty checks, multi-round review loops, and paper writing through to submission-ready PDFs with figures and LaTeX templates.

The skills are plain `SKILL.md` files with no framework and no lock-in, so the same files work in Claude Code, Codex, Cursor, Copilot CLI and OpenClaw. A second model (Codex by default, with Gemini, Grok and Claude Code options) critiques the executor's output, which is the cross-model loop the suite is known for.

## Installation

The README installs skills as project-local symlinks rather than through a package registry:

```bash
git clone https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep.git
bash Auto-claude-code-research-in-sleep/tools/install_aris.sh ~/your-project
```

The installer symlinks each skill into `.claude/skills/` and writes a manifest at `.aris/installed-skills.txt`. A global install copies the skills instead:

```bash
cp -r Auto-claude-code-research-in-sleep/skills/* ~/.claude/skills/
```

Install a subset with group or single-skill selectors:

```bash
bash Auto-claude-code-research-in-sleep/tools/install_aris.sh --list-groups
bash Auto-claude-code-research-in-sleep/tools/install_aris.sh --groups paper-core,lit-search
bash Auto-claude-code-research-in-sleep/tools/install_aris.sh --skills paper-writing
```

A Claude Code plugin route installs the whole set at once with a typed prefix:

```bash
claude plugin marketplace add wanshuiyin/Auto-claude-code-research-in-sleep
claude plugin install aris@aris
```

Then run `/aris:setup` once and restart Claude Code. The review skills need an independent model: install Codex and log in (`npm install -g @openai/codex && codex login`), then register the bridge as a `codex` MCP server with `claude mcp add`, pointing at `mcp-servers/codex-exec/server.py`, and restart Claude Code. Update later with `git pull` plus `bash tools/smart_update.sh --apply`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| semantic-scholar | 701 | Search published venue papers via the Semantic Scholar API with citation counts and venue metadata. |
| paper-figure | 683 | Generate publication-quality figures and tables from experiment results. |
| research-lit | 675 | Search and analyze papers, find related work and summarize key ideas. |
| idea-discovery | 635 | Run the full idea-discovery pipeline from a broad direction to pilot-tested ideas. |
| idea-creator | 631 | Generate and rank research ideas given a broad direction. |
| auto-review-loop | 625 | Run a multi-round research review loop until a positive verdict or max rounds. |
| arxiv | 623 | Search, download and summarize papers from arXiv into a local library. |
| research-pipeline | 618 | Run the end-to-end pipeline from research direction to polished paper PDF. |
| research-review | 617 | Get a deep critical review from a chosen model backend. |
| paper-writing | 615 | Run the full paper-writing pipeline from narrative report to submission-ready PDF. |
| pixel-art | 610 | Generate pixel-art SVG illustrations for READMEs, docs or slides. |
| grant-proposal | 610 | Draft a structured grant proposal from ideas and literature in nine funding formats. |
| novelty-check | 609 | Verify a research idea is novel against recent literature. |
| analyze-results | 605 | Analyze ML experiment results into statistics, tables and insights. |

The remaining 74 indexed listings range from 52 to 598 installs.

## Why This Matters for Hermes Agents

The suite encodes a complete, opinionated research workflow that a general agent would otherwise improvise stage by stage. Each skill is a small markdown file with explicit triggers and hand-offs, so an agent can load exactly the stage it needs instead of pulling a whole pipeline into context.

The cross-model loop is the part worth studying for agent builders: one model executes while a second model critiques, then the executor fixes and the loop re-runs until the work passes or hits a round cap. Applied to papers, ideas and experiments, that is a concrete template for any self-checking agent workflow.

The literature and idea skills lean on real APIs (arXiv, Semantic Scholar, OpenAlex, Exa, DeepXiv) and ship their own helper scripts for fetching and verifying, so an agent gets a working search-to-paper path rather than just prompt text.

## Usage

| You say | What happens |
|---|---|
| "/idea-discovery \"factorized gap in discrete diffusion LMs\"" | Runs the idea-discovery pipeline from a specific direction to pilot-tested ideas. |
| "/auto-review-loop \"my paper topic\"" | Runs review, fix, re-review rounds overnight until a positive verdict or the round cap. |
| "/paper-writing NARRATIVE_REPORT.md" | Turns a narrative report into a polished, submission-ready PDF. |
| "/research-lit on attention is all you need" | Searches and summarizes papers, finds related work and key ideas. |
| "/arxiv search transformers" | Searches, downloads and summarizes papers from arXiv into the local library. |
| "/rebuttal \"paper/ + reviews\"" | Parses reviews and drafts a rebuttal and follow-up plan. |
| "/research-wiki init" | Enables persistent research memory across sessions. |

## Verification

Probe skills on the `main` branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/wanshuiyin/auto-claude-code-research-in-sleep/main/skills/semantic-scholar/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/wanshuiyin/auto-claude-code-research-in-sleep/main/skills/paper-figure/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/wanshuiyin/auto-claude-code-research-in-sleep/main/skills/research-lit/SKILL.md
```

Skills live at `skills/<name>/SKILL.md` on the `main` branch; the repo mirrors the set under `skills-codex/` for the Codex route.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| semantic-scholar | Pass | Pass | Warn |
| paper-figure | Warn | Pass | Pass |
| research-lit | Pass | Pass | Warn |
| idea-discovery | Pass | Pass | Warn |
| idea-creator | Warn | Pass | Pass |
| auto-review-loop | Pass | Warn | Pass |
| arxiv | Warn | Warn | Warn |
| research-pipeline | Warn | Warn | Pass |
| research-review | Pass | Pass | Pass |
| paper-writing | Pass | Pass | Warn |
| pixel-art | Pass | Pass | Pass |
| grant-proposal | Warn | Pass | Warn |
| novelty-check | Pass | Pass | Warn |
| analyze-results | Pass | Pass | Pass |
| experiment-plan | Pass | Pass | Pass |
| auto-paper-improvement-loop | Pass | Pass | Pass |
| paper-write | Pass | Pass | Warn |
| paper-illustration | Warn | Pass | Pass |
| formula-derivation | Pass | Pass | Pass |
| research-refine | Pass | Pass | Warn |

The sample covers 20 of the 88 indexed listings. Six carry a Gen Agent Trust Hub Warn, three a Socket Warn and nine a Snyk Warn; arxiv is Warn on all three.

## Limitations

- Snapshot data, verified 2026-11-17: 44,004 combined installs across 88 indexed listings; 19,359 GitHub stars; MIT; last pushed 2026-11-17. Counts drift over time.
- The README's own skill counts are inconsistent (87 in the quick start, 82 in one changelog entry), so treat the per-skill numbers rather than the prose total as authoritative.
- The repository is a large monorepo of 768 files that also ships a Rust CLI, MCP bridges and Codex/Gemini review mirrors; the skill-level verdicts do not cover that wider codebase.
- One indexed listing (comm-lit-review-claude-single, 200 installs) has no matching directory in the current skills/ tree.
- The review loop needs an external model registered as the codex MCP bridge; without it, the review skills fall back or fail.
- Several skills bundle Python helpers that fetch papers or render figures and run as local scripts; read those before running them in a shared environment.

## Related

- [RigorPilot Skills - AI Research & Paper Reproduction Setup](/hermes/skills/catalog/rigorpilot-skills-setup)
- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)
- [Research Paper Writing Pipeline - Academic ML/AI Paper Production Setup](/hermes/skills/catalog/research-paper-writing-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the project-local symlink install rather than the global copy, so the manifest tracks what ARIS installed and uninstall only touches managed entries.
- Run `/research-wiki init` early so papers, ideas and failed experiments persist across sessions.
- Give `/idea-discovery` a specific direction rather than a broad topic; the skill is explicit that a one-word topic is too vague.
- Register the codex MCP bridge before running review skills, and confirm `claude mcp list` shows it connected.
- Update with `git pull` plus `smart_update.sh --apply`, then rerun the installer to pick up newly added skills, since symlinks do not propagate new entries on their own.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
