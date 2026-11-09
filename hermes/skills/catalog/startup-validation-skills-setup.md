---
title: "Startup Validation Skills - Design, Pitch and Positioning"
description: "ferdinandobons/startup-skill on skills.sh: 3.3K installs; four skills for startup validation, competitive battle cards, positioning and pitch scripts."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/startup-validation-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "startup validation", "competitive intelligence", "positioning", "fundraising"]
---

# Startup Validation Skills - Setup Guide

**Source:** [ferdinandobons/startup-skill](https://www.skills.sh/ferdinandobons/startup-skill) via skills.sh - 3.3K combined installs across 4 indexed listings (3,272 exact); first seen 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 1,269 stars, MIT via LICENSE, `main` branch, last pushed 2026-07-01, four skill directories at the repository root (`startup-design/`, `startup-competitors/`, `startup-positioning/`, `startup-pitch/`), each with a `SKILL.md` and its own `references/` tree, 57 files in total
**Category:** Business and fundraising: startup validation, market research, competitive intelligence, positioning, pitch construction and a 30-day plan
**Quality Tier:** 🟡 Experimental - MIT licensed and Pass on the Trust Hub and Socket scanners, but Snyk returns Warn on all four skills, and every research phase depends on live web search plus a large token budget.

This is the startup strategy suite from Ferdinand Obons, and it is unusually ambitious for a skill repository: the README describes it as what a $10K strategy consultant would deliver, and the file counts back that up. `startup-design/SKILL.md` alone is 476 lines and runs a pre-flight check, eight numbered phases, a customer discovery gate and a validation phase, writing markdown deliverables into a `{project-name}/` tree as it goes. The other three skills are narrower: `startup-pitch` is 424 lines and produces seven pitch formats plus a scoring rubric, `startup-competitors` is 268 lines across three research waves, and `startup-positioning` is 302 lines built on April Dunford's 5+1 framework.

The detail that separates it from a prompt library is the honesty scaffolding. Every phase output carries `[Data]`, `[Estimate]`, `[Assumption]` and `[Opinion]` labels, every document ends with Red Flags and Yellow Flags sections, and the run closes on a `kill-criteria.md` file with 5-7 measurable stop or pivot conditions. A design run also writes `PROGRESS.md` and resumes from it, which is the property that makes a multi-hour research job survivable in an agent session.

## Installation

The README leads with the Claude Code plugin route and calls it recommended:

```bash
claude plugin marketplace add ferdinandobons/startup-skill
claude plugin install startup@startup-skill
```

The CLI route installs all four skills into the agent's skills directory:

```bash
npx skills add ferdinandobons/startup-skill
```

For a manual install, the README clones once and copies the four directories into `.agents/skills/`. The copy step is not optional in this layout: there is no root `SKILL.md`, so each skill directory is its own skill and the directory name is the name the client indexes:

```bash
git clone https://github.com/ferdinandobons/startup-skill.git
cp -r startup-skill/startup-design .agents/skills/
cp -r startup-skill/startup-competitors .agents/skills/
cp -r startup-skill/startup-positioning .agents/skills/
cp -r startup-skill/startup-pitch .agents/skills/
```

The README also documents a git submodule route (`git submodule add https://github.com/ferdinandobons/startup-skill.git .agents/startup-skill`) and SkillKit (`npx skillkit install ferdinandobons/startup-skill`), which the README says works with Claude Code, Cursor and Copilot.

Updates depend on the route. The plugin updates with `claude plugin update startup@startup-skill`, and if that misses changes the README prescribes a full uninstall, marketplace remove and re-add cycle. CLI and SkillKit installs are updated by re-running the install command, which overwrites the previous version, and a submodule with `git submodule update --remote .agents/startup-skill`. The repository's latest release is v1.10.0, and Claude.ai users download `.skill` files from the releases page and upload them under Settings, Skills.

## What It Provides

The threshold for this guide is zero installs, so all four indexed listings appear:

| Skill | Installs | Use For |
|---|---|---|
| startup-design | 1,089 | Full startup build: pre-flight sanity check, eight phases from intake to validation, four research waves, brand, product definition, a two-stage financial model, and a 30-day action plan with kill criteria |
| startup-pitch | 788 | Pitch narratives at 10, 5, 2 and 1 minutes plus an investor email, appendix, deck outline, an eight-dimension scoring rubric with an overall score, and optional investor roleplay |
| startup-competitors | 723 | Competitor battle cards, feature matrix, pricing landscape, value metric analysis and churn signals from three waves of web research |
| startup-positioning | 672 | Dunford 5+1 positioning document, competitive alternatives map, market category choice, Onliness Test and messaging implications |

All four indexed listings clear the zero-install threshold and appear in the table above.

The install index and the repository tree agree here: four listings, four directories, no drift, and 43 of the 57 files in the repo sit inside those four directories. `startup-design` carries 15 reference files, from `output-guidelines.md` and `honesty-protocol.md` through four research wave briefs to `verification-agent.md` and `industry-benchmarks.md`, and the body instructs the agent to read only the file for the phase it is in.

## Why This Matters for Hermes Agents

A model asked to size a market will produce a number, and the number will look researched. `startup-design` is built to make that hard: research agents must run 5-8 searches each, cross-reference every key finding across 2-3 independent sources, rate source tiers, date every figure and flag anything older than 18 months, and the synthesis step has to output a confidence dashboard that names each claim, its source tier, its corroborating count and its data age. That is the difference between a deliverable a founder can act on and a plausible document.

The suite also solves a Hermes specific problem, which is context loss on long jobs. The design skill writes `PROGRESS.md` after every phase and starts each session with a resume check, so a research run that spans several sessions picks up where it stopped instead of restarting the market sizing. For an agent that compacts or is restarted mid-task, an on-disk checkpoint is worth more than a longer prompt.

The third fit is that the gates are explicit. `Phase 3.7` forces a written choice between running interviews now and deferring them, and the deferred branch is documented with its cost: projections stay Stage A, the dashboard records zero interviews, and interviews become the first experiment in the validation playbook. The interview gate itself is arithmetic (4 or more of 5 interviewees confirming the problem unprompted, at least 2 with behaviour signals), and the final scorecard maps a 1-10 score to a verdict band (8-10 proceed, 6-7 conditional, 4-5 concerns, 1-3 stop or pivot). An agent can follow a rule with a threshold; it cannot reliably follow "be honest".

Two things to know before relying on it. The research phases assume web search and, in Claude Code, an `Agent` tool to spawn parallel subagents. When web search is missing the skill falls back to a Knowledge-Based Research Mode that labels findings as not live data and drops confidence by one level, and when the Agent tool is missing the same waves run sequentially and take longer. Neither fallback is as good as the real thing, and both are recorded in `PROGRESS.md`.

## Usage

| You say | What happens |
|---|---|
| "I want to build a SaaS for real estate agents that automates follow-up emails. Is it worth building?" | Runs `startup-design` end to end: pre-flight check, intake interview, 8 phases, customer discovery gate, then a validation scorecard and a 30-day action plan |
| "Who are my competitors in project management for creative agencies? I need battle cards and a pricing comparison." | Runs `startup-competitors`: profiles 5-8+ competitors across three research waves and writes one battle card file per competitor plus `pricing-landscape.md` and `competitive-matrix.md` |
| "Quick validation, I do not have weeks." | Switches `startup-design` into Fast Track mode: lean canvas only, revenue model only, scorecard plus the top 3 experiments, with the mode recorded in `PROGRESS.md` so a later session can expand it |
| "How should we position this? We are in project management but different from Asana and Monday." | Runs `startup-positioning`: Dunford's 5+1 components in order, then the Neumeier Onliness Test and the Ries/Trout mental ladder, and it refuses to ship a position that fails either |
| "Prepare my pitch, I am raising 500K pre-seed with 45 active customers growing 20% MoM." | Runs `startup-pitch`: writes the full, 5 minute, 2 minute, 1 minute, email, appendix and deck outline files, then scores them on an eight-dimension rubric |
| "Practice my pitch, you play the investor." | Runs the optional roleplay step with a chosen persona: angel, seed VC, Series A VC or accelerator partner, each with its own question set |
| "The session died halfway through the research phase." | The Phase 0 resume check finds `PROGRESS.md`, reports which phases are complete, and continues from the first incomplete one |

## Verification

There is no root `SKILL.md` in this repository, so the root URL returns 404 by design. Each skill is checked at its own path. This returns 200 and opens with frontmatter naming the skill:

```bash
curl -fsSL https://raw.githubusercontent.com/ferdinandobons/startup-skill/main/startup-design/SKILL.md | head -6
```

The same check per skill, all four on the `main` branch:

```bash
for s in startup-design startup-pitch startup-competitors startup-positioning; do
  curl -fsSL -o /dev/null -w "%{http_code} $s\n" \
    "https://raw.githubusercontent.com/ferdinandobons/startup-skill/main/$s/SKILL.md"
done
```

The references matter as much as the body, because the bodies are routers. The design skill's first hard dependency is the output contract it tells the agent to read once per session:

```bash
curl -fsSL https://raw.githubusercontent.com/ferdinandobons/startup-skill/main/startup-design/references/output-guidelines.md | head -5
```

A 404 there means the phase instructions no longer resolve and the deliverables will be shaped by the model rather than by the spec. After a manual copy, confirm each skill landed as its own directory rather than nested one level too deep:

```bash
test -f .agents/skills/startup-design/SKILL.md && echo ok
test -f .agents/skills/startup-pitch/SKILL.md && echo ok
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| startup-design | Pass | Pass | Warn |
| startup-pitch | Pass | Pass | Warn |
| startup-competitors | Pass | Pass | Warn |
| startup-positioning | Pass | Pass | Warn |

The Warn on all four is a Snyk-only result, and the package contents explain the shape of the risk: 50 of the 57 files are Markdown, the remaining seven are one PNG banner, one plugin manifest under `.claude-plugin/`, three issue-template YAML files, `LICENSE` and `.gitignore`. There is no installer, no shell script and no network client in the repository. A Warn against that surface usually reflects the skill's instructions and their blast radius rather than malicious code, and the instructions here tell an agent to research the open web, spawn subagents and write a multi-file deliverable tree.

That is also the real security boundary. The skills write into `{project-name}/` in whatever directory the session runs from, using the agent's own filesystem permissions, so the practical control is where you start the agent and what it can write to. Run it in a repository scoped to the project, not in a home directory.

The data the skills collect is worse to leak than the code. Intake captures revenue, pricing, margins and customer names, `customer-interview.md` drives interview synthesis, and `startup-competitors` writes per-competitor churn signals and how-to-win talking points. All of it lands as plain markdown with no access control, so a `git add -A` publishes the whole run. Add the project directory to `.gitignore` before the first phase, and treat the output tree as confidential until you have read it.

One more consideration for autonomous use: the research waves read arbitrary web pages, and that content reaches the agent's context during a phase that also writes files and, in Fast Track, makes a go/no-go call. Prompt injection in a fetched page is a live path here, so keep a human review on the research gate output rather than letting the agent chain straight from research into strategy unattended.

## Limitations

- Snapshot data, verified 2026-11-09: 3,272 combined installs across 4 indexed listings; 1,269 GitHub stars; MIT license; last pushed 2026-07-01. Counts drift over time.
- The suite is expensive to run. The README warns that these skills run multiple research agents and can consume a large number of tokens, and recommends a Claude Max 5x plan for the intended experience. On a metered API budget, budget for a full `startup-design` run before starting one.
- Research quality degrades silently without tools. With no web search the skill switches to Knowledge-Based Research Mode, marks findings as not live data and lowers every confidence rating by one level; with no `Agent` tool the four waves run sequentially. Both paths still produce a complete deliverable tree, which is the risk: the output looks the same whether or not it was researched live.
- The install index covers four skills and the tree carries four directories, so there is no drift today, but `startup-design` alone routes into 15 reference files and the skill has no version field. A pin means pinning a commit, and reference paths can move between releases such as v1.10.0.
- The honesty rules are instructions to the model, not enforcement. Data labels, Red Flag sections and the kill-criteria file all depend on the agent following the phase spec, and the skill's own verification phase is itself an agent run. Read the confidence dashboard before you trust a verdict.
- Output language defaults to English and switches only if the user writes in another language or asks for one. Multicultural research depth is not addressed by the skills, and market sizing instructions lean on English-language sources and analyst tiers.

## Related

- [Startup OS Skills - Sales, Product and Video Pack](/hermes/skills/catalog/startup-os-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the pre-flight check, not the intake interview. It costs 2-3 searches and 5 minutes, and it surfaces a dominant incumbent, a public prior failure or a regulatory wall before you spend hours on research.
- Read the confidence dashboard before the market analysis. It lists each major claim with source tier, corroborating count and data age, which is the fastest way to see where the numbers are thin.
- Use Fast Track to kill an idea and Full mode to build one. Fast Track skips brand and product and reduces the financial phase to a revenue model, which is the right size for a go/no-go and the wrong size for a plan you intend to execute.
- Name the language of your market in the intake. All four skills default to English output, and the customer language map in `startup-design` is built from the sources the research waves actually read.
- Run `startup-design` before `startup-pitch` if you can. The pitch skill works standalone, but it checks for prior work and reuses the positioning, market sizing and competitive framing when those files exist, which is where most of the pitch's evidence comes from.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
