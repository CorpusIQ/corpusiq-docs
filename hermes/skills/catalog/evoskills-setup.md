---
title: "EvoSkills - Scientific Research Skill Packs Setup"
description: "Setup guide for evoscientist/evoskills - 5.6K combined installs. Research skill packs: paper planning, review, rebuttal, experiment pipelines."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/evoskills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "research", "academic writing"]
---

# EvoSkills - Setup Guide

**Source:** [evoscientist/evoskills](https://www.skills.sh/evoscientist/evoskills) via skills.sh - 5.6K combined installs across 18 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [evoscientist/evoskills](https://github.com/evoscientist/evoskills) (478 stars, Apache-2.0; pushed Sep 30, 2026; `skills/<name>/SKILL.md` layout)
**Category:** Scientific Research / Academic Writing
**Quality Tier:** 🟡 Beta - official EvoScientist repo; Apache-2.0; all sampled verdicts Pass; all listings below 500 installs

EvoSkills is the official skill repository for EvoScientist. Each skill is an installable knowledge pack that extends the agent with domain expertise, and together they cover a full research lifecycle: ideation grounded in literature, paper planning, staged experiment execution, debugging and iterative coding, writing, self-review, rebuttal, slides, figures, and paper discovery. The headline mechanism is persistence: under EvoScientist, the skills evolve across research cycles through `evo-memory`, which tracks feasible and failed directions and distills reusable experiment strategy.

The README is explicit that the skills are purpose-built for EvoScientist, where they amplify each other, but it also states compatibility with any coding agent through a single `npx skills add` command. Packaging is plain `skills/<name>/SKILL.md`, and the repo also ships a curated `mcp/` directory of supporting MCP servers for web search, paper retrieval, and documentation lookup.

---

## Installation

Inside EvoScientist (in-session commands):

```bash
# Install all skills at once
/install-skill EvoScientist/EvoSkills@skills

# Or a single skill
/install-skill EvoScientist/EvoSkills@skills/paper-planning
```

Or just ask in conversation: "Install all skills from EvoScientist/EvoSkills@skills."

Not using EvoScientist? The skills are compatible with any coding agent; on Claude Code, OpenCode, Cursor, Codex, Gemini CLI, DeepAgents, and more:

```bash
npx skills add EvoScientist/EvoSkills
```

The repo's `mcp/` directory adds supporting MCP servers (for example arXiv) installable via `/install-mcp` or `EvoSci mcp install arxiv`.

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| paper-review | 498 | Adversarial self-review before submission: 5-aspect checklist, reverse-outlining, rejection simulation |
| paper-writing | 497 | Section-by-section drafting: 11-step workflow, abstract and introduction templates, LaTeX skeleton |
| research-ideation | 476 | Literature grounding, three-track persona refinement, Elo tournament ranking, proposal generation |
| academic-slides | 467 | Research talks: narrative arc, slide design rules, .pptx generation, rehearsal and Q&A prep |
| paper-rebuttal | 435 | Post-review rebuttals: score diagnosis, champion strategy, and 18 tactical writing rules |
| paper-planning | 411 | Story design, experiment and figure planning, and a 4-week submission countdown |
| evo-memory | 381 | Persistent research memory: ideation and experimentation stores with IDE, IVE, and ESE evolution |
| experiment-pipeline | 379 | 4-stage experiment execution with attempt budgets: baseline, tuning, method, ablation |
| experiment-craft | 368 | Experiment debugging: 5-step diagnostic flow, structured logs, handoff to paper writing |
| paper-navigator | 347 | Paper discovery and reading: rubric-first triage, probe plus up to 3 search rounds, full-text reads |
| research-survey | 293 | Structured literature surveys: adaptive outline, draft-and-expand pipeline, survey-grade output |
| experiment-iterative-coder | 290 | Plan, code, evaluate, and refine cycles for research code with lint and test scoring |
| nano-banana | 275 | AI-generated slides and illustrations via Gemini image models, with a browser review loop |

The remaining 5 indexed listings range from 3 to 146 installs (evomath-tao, idea-tournament, paper-figures, paper-graph, and iterative-coder).

## Why This Matters for Hermes Agents

Research is a long-horizon task class where agents usually lose the thread: a strong assistant writes one section, forgets last week's failed direction, and re-suggests it. EvoSkills attacks that with structure - attempt budgets per experiment stage, diagnostic gates that force a working version before fixes, and templates that make each paper section checkable. The memory layer is the differentiator: IDE, IVE, and ESE mechanisms feed learned knowledge back into ideation and experimentation stores so the next cycle starts smarter. Coverage is unusually complete for a repo this size: from discovery and reading, through execution and debugging, to writing, review, rebuttal, and slides. Everything is plain `SKILL.md` content, so it is auditable, vendorable, and trimmable. Even outside EvoScientist, the standalone packs hand a Hermes-style agent a serious research methodology instead of generic "write a paper" prompting. The honest-status discipline in evomath-tao - five labels from PROVED down to HANDED_OFF, never a hand-waved result - is a good signal for how the whole set treats claims.

## Usage

| You say | What happens |
|---|---|
| "Find the key papers on test-time adaptation and propose three directions" | research-ideation grounds in literature via paper-navigator, runs the persona tracks, and ranks the ideas |
| "Plan a paper from these results" | paper-planning reverse-engineers the narrative, plans experiments and figures, and sets a 4-week timeline |
| "Run the baseline experiments" | experiment-pipeline executes stage 1 with attempt budgets and logs the trajectory into evo-memory |
| "Why is this experiment failing?" | experiment-craft runs the 5-step diagnostic and proposes the next single-variable change |
| "Draft the method section" | paper-writing applies its 11-step workflow and LaTeX assets section by section |
| "Review this paper before submission" | paper-review runs the checklist, reverse-outlines, and simulates a rejection |
| "Write the rebuttal" | paper-rebuttal scores every reviewer comment and drafts responses with its 18 rules |

## Verification

```bash
# Confirm the skill pack is installed for your agent
npx skills list | grep -E 'paper-review|evo-memory'

# Review the layout-verified skill straight from GitHub before installing
curl -sL https://raw.githubusercontent.com/evoscientist/evoskills/main/skills/paper-review/SKILL.md | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| paper-review | Pass | Pass | Pass |
| scientific-writing | - | - | - |
| research | - | - | - |

Only one sampled skill carries verdicts (paper-review, Pass across all three engines); the other sampled entries are unrated, so widen your own review for anything you run unattended.

## Limitations

- Purpose-built for EvoScientist: the README notes the skills amplify each other there, and cross-cycle evolution runs through evo-memory; elsewhere they work as standalone packs.
- All listings sit below 500 installs and the pack is young (first seen Oct 9, 2026), so maturity signals are limited.
- Sampled verdicts cover one skill; the rest are unrated.
- Some skills depend on external services: paper-navigator uses Semantic Scholar, arXiv, HuggingFace, GitHub, and Jina Reader, and nano-banana uses Gemini image models.
- The MCP marketplace servers in the repo carry their own setup and dependencies.
- Snapshot data, verified Oct 10, 2026: 5,593 combined installs across 18 indexed listings; 478 GitHub stars; Apache-2.0; last pushed Sep 30, 2026. Counts drift over time.

## Related

- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup) - a general academic paper pipeline to compare coverage
- [Research Paper Writing Pipeline - Academic ML/AI Paper Production Setup](/hermes/skills/catalog/research-paper-writing-setup) - focused on ML/AI paper production
- [Hermes ArXiv Agent - ArXiv Paper Fetcher Setup](/hermes/skills/catalog/hermes-arxiv-agent-setup) - pairs with paper-navigator's discovery workflow
- [Nature Skills - Academic Writing Setup](/hermes/skills/catalog/nature-skills-setup) - journal-style writing support
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- In EvoScientist, install the whole suite: the skills are designed to amplify each other, and evo-memory only pays off across cycles.
- On other agents, cherry-pick by name (for example, paper-planning alone) to keep context lean.
- Trust the attempt budgets (20/12/12/18): they exist to stop rabbit holes, not to slow you down.
- Read evo-memory at the start of a research cycle and let research-ideation reuse feasible directions instead of re-deriving them.
- For contest-style math work, evomath-tao returns honest status labels (PROVED, CONJECTURED, or HANDED_OFF) rather than a hand-waved result.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
