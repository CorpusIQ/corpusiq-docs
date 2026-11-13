---
title: "Awesome AI Agent Skills - 103-Skill Agent Library"
description: "seb1n/awesome-ai-agent-skills: 13.1K combined installs across 96 listings, 103 self-contained skills for agent engineering, security and data work"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/awesome-ai-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-12"
tags: ["hermes skill", "agent skill", "skill setup", "agent engineering", "agent security", "evaluation"]
---

# Awesome AI Agent Skills - Setup Guide

**Source:** [seb1n/awesome-ai-agent-skills](https://www.skills.sh/seb1n/awesome-ai-agent-skills) via skills.sh - 13.1K combined installs across 96 indexed listings; first seen Nov 12, 2026 (this sweep)
**GitHub:** 252 stars, MIT license, `main` branch, last pushed 2026-08-09, 103 `SKILL.md` files across 21 category directories, with a validation workflow and an offline demo fixture
**Category:** Agent engineering, agent security, and the general operator surface around them
**Quality Tier:** 🟢 Production - 103 self-contained skills, MIT, a CI skill validator, and Pass verdicts across every sampled skill; the one dent is a repository that has not been pushed since August 2026.

This is a library rather than a pack. Each of the 103 skills is a folder with its own `SKILL.md`, grouped under 21 category directories: `agent-engineering`, `agent-security`, `code-and-development`, `data-and-analytics`, `legal-and-compliance`, `finance-and-accounting`, `devops-and-infrastructure`, `marketing-and-seo`, `sales`, `customer-success`, `design-and-ui-ux`, `documents-and-files`, and the rest of the operator map. Nothing is a link out to another repository, which is unusual for a collection advertised as awesome.

The strongest ground is agent work itself. `agent-engineering` carries six skills: `agent-evaluation`, `agent-observability`, `human-in-the-loop`, `mcp-server-building`, `multi-agent-orchestration`, and `tool-schema-design`. `agent-security` adds three: `prompt-injection-defense`, `agent-red-teaming`, and `skill-supply-chain-audit`. Those nine are the parts most agent stacks improvise badly, and they are written as procedures rather than as opinions.

The repository also ships a fixture that can be run offline. `demos/production-agent-stack/run_demo.py --check` starts at 1 of 5 checks against a fragile agent boundary and reaches 5 of 5 against a stack built from six of the skills, with local mock effects only: no API keys, no network calls, no model calls. A vendor that ships a test you can run before installing anything is doing something different from a vendor that ships a manifest.

Install counts are flat. The top listing sits at 222 installs and the ninetieth at 110, which is the shape of a library people install in pieces rather than a handful of viral skills.

## Installation

The README documents the Skills CLI as the primary route:

```bash
npx skills add seb1n/awesome-ai-agent-skills
```

List what is available without installing:

```bash
npx skills add seb1n/awesome-ai-agent-skills --list
```

Install a single skill:

```bash
npx skills add seb1n/awesome-ai-agent-skills --skill agent-evaluation
```

Install a working set by repeating the flag:

```bash
npx skills add seb1n/awesome-ai-agent-skills \
  --skill agent-evaluation \
  --skill agent-observability \
  --skill human-in-the-loop
```

The README's starter packs are the sensible entry points: Production Agent Stack, Multi-Agent Systems, Agent Security, and Document Work. Each names six or fewer skills, which keeps the first install reviewable.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| note-taking | 222 | Capture, tag and retrieve notes in structured files, with naming and retrieval conventions. |
| proofreading | 187 | Grammar, spelling, punctuation and style correction, with consistency checks across a document. |
| fact-checking | 177 | Breaking a claim into assertions and checking each against authoritative sources. |
| data-visualization | 175 | Charts and dashboards from structured data with matplotlib, seaborn and plotly. |
| summarization | 173 | Extractive, abstractive and multi-document summaries at a target length. |
| chatbot-conversation-design | 170 | Intent handling, slot filling, disambiguation and fallback flows for a conversational interface. |
| context-compression | 169 | Compressing working context to a token budget while keeping decisions, constraints and evidence. |
| data-analysis | 159 | Statistical analysis, trend detection and hypothesis testing over a dataset. |
| technical-writing | 157 | API references, user guides and tutorials with consistent terminology. |
| data-labeling | 157 | Annotation workflows, active learning and quality checks for labeled datasets. |
| knowledge-graph-creation | 154 | Entity and relation extraction from unstructured text into a queryable graph. |
| database-schema-design | 154 | Normalized schemas with keys, relationships, indexes and constraints. |
| version-control | 152 | Branching strategy, commit hygiene and conflict resolution in Git. |
| refactoring | 152 | Code smell identification and systematic restructuring without behavior change. |
| data-cleaning | 152 | Missing values, duplicates, type correction and outlier handling before analysis. |
| code-documentation | 151 | API references, inline documentation and docstring generation for a codebase. |
| social-media-posting | 150 | Platform-specific formatting and scheduling across social channels. |
| deep-research | 150 | Multi-step research that decomposes a question, gathers sources and cross-checks claims. |

The remaining 78 indexed listings range from 110 to 147 installs.

## Why This Matters for Hermes Agents

An agent stack is usually assembled from whatever the last project needed. That produces a system that can write code and cannot say whether the code it wrote works. The four disciplines that fix this are evaluation, observability, human approval and tool schema design, and they are exactly the disciplines nobody writes from scratch on a deadline.

The security half matters for a different reason. An agent that reads a GitHub issue, a web page or a support ticket is reading untrusted input into its own instruction stream. `prompt-injection-defense` and `skill-supply-chain-audit` treat that as a design problem with checks, not as a warning in a README. For anyone running an agent against external data, those two files are worth the install on their own.

The rest of the library is ordinary leverage. Proofreading, fact-checking, data cleaning, schema design, refactoring and documentation are tasks that recur in every project and are never the interesting part. A written procedure for each of them is cheaper than re-deriving the procedure every session.

The offline demo is the part worth copying. A skill that can be tested before installation, with deterministic fixtures, gives an agent stack something it usually lacks: a way to prove a change made the boundary stronger.

## Usage

| You say | What happens |
|---|---|
| "Set up an evaluation for this agent before we ship" | Loads `agent-evaluation` and produces a test set, scoring method and pass criteria. |
| "This deployment agent reads GitHub issues. What can go wrong?" | Loads `prompt-injection-defense` and maps the trust boundaries around untrusted input. |
| "Write the tool schema for these four functions" | Loads `tool-schema-design` and returns typed schemas with required fields and error shapes. |
| "Where should a human approve in this workflow?" | Loads `human-in-the-loop` and places approval gates at the irreversible steps. |
| "Check this report against the source documents" | Loads `fact-checking` and `summarization`, asserting each claim and flagging the unsupported ones. |
| "Clean this CSV and tell me what is wrong with it" | Loads `data-cleaning` then `data-analysis` and returns both the defect list and the analysis. |
| "Add a knowledge graph over these documents" | Loads `knowledge-graph-creation` and extracts entities and relations into a queryable structure. |

## Verification

Probe two SKILL.md files on the branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/seb1n/awesome-ai-agent-skills/main/agent-engineering/agent-evaluation/SKILL.md | head -6
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/seb1n/awesome-ai-agent-skills/main/productivity-and-workflow/note-taking/SKILL.md
```

Run the offline demo from a clone before trusting the security claims:

```bash
git clone https://github.com/seb1n/awesome-ai-agent-skills.git
cd awesome-ai-agent-skills && python3 demos/production-agent-stack/run_demo.py --check
```

After installation, list the agent skills directory and confirm one folder per installed skill, each with a `SKILL.md`. The category path is not preserved in the install target, so two skills with the same name in different categories would collide.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-12) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| note-taking | Pass | Pass | Pass |
| proofreading | Pass | Pass | Pass |
| fact-checking | Pass | Pass | Pass |
| data-visualization | Pass | Pass | Pass |
| summarization | Pass | Pass | Pass |

The sample is clean and the skills are instruction files, which is what the scanners can actually judge. The two that reach the network are `data-visualization` (plotly can fetch) and `deep-research` (web retrieval), so review those bodies past the scanner result. The repository also carries a validation workflow that checks `SKILL.md` structure on every push, which is a stronger signal than a one-off audit.

## Limitations

- Snapshot data, verified 2026-11-12: 13,145 combined installs across 96 indexed listings; 252 GitHub stars; MIT license; last pushed 2026-08-09. Counts drift over time.
- 96 is the cap of the skills.sh search API and the repository carries 103 `SKILL.md` files, so the listing count and the combined total are both floors.
- The repository has not been pushed since August 2026 and there is no release tag, so the installed tree is whatever `main` holds at install time.
- Install counts are flat and low across the whole library, topping out at 222. These are not field-tested workflows at scale, and a broken skill would not show up in the numbers.
- 21 categories mean 21 different authors' habits. Several skills overlap, and reading each `SKILL.md` before installing is the only way to know which of the two database skills you want.
- The demo proves the fixture's own claims against mock effects. It is not evidence that the skills work against a live system.

## Related

- [Awesome Codex Skills - Curated Codex Index](/hermes/skills/catalog/composio-awesome-codex-skills-setup)
- [Skill Vetter - Security Audit for Hermes Skills Setup](/hermes/skills/catalog/skill-vetter-setup)
- [Claude Skills Generator - Coding Setup](/hermes/skills/catalog/claude-skills-generator-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the nine agent skills. Evaluation, observability, human-in-the-loop, tool schema design, multi-agent orchestration, MCP server building, prompt-injection defense, red teaming and supply-chain audit are the ones that change how a stack behaves.
- Run the demo fixture before installing anything. It takes a minute and it tells you whether the authors' boundary model matches yours.
- Install by category, not by listing. `agent-security` is three folders and one decision; the marketing category is five folders and a different decision.
- Keep the category directory names when you vendor a folder into a project. The names are how the README's index and starter packs refer to the skills.
- Ask the agent to cite the skill it used. With 103 procedures available, the wrong one is invisible in the answer and obvious in the trace.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
