---
title: mattpocock/skills — Full Setup Guide for Hermes Agents
description: Install and configure Matt Pocock's engineering skills suite — grill-me, handoff, TDD, domain modeling, codebase architecture, and more. 45 skills, 5M+ installs.
---

# mattpocock/skills — Setup Guide

**Source:** [mattpocock/skills](https://skills.sh/mattpocock/skills) (5.0M total installs)
**Category:** Engineering / Development Workflow

A collection of 45 agent skills by Matt Pocock for real engineering — not "vibe coding." Designed to be small, adaptable, composable, and model-agnostic. Use them to reduce misalignment, verbosity, broken code, and architectural decay in AI-assisted development.

---

## Installation

```bash
npx skills add mattpocock/skills
```

After install, run setup:

```
/setup-matt-pocock-skills
```

This configures your issue tracker, triage labels, and documentation paths.

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | v0.16.0+ |
| **Node.js** | v18+ for `npx` install |
| **GitHub repo** | Issue tracker configured for triage skills |

---

## Key Skills

### User-Invoked Skills (Orchestrators)

| Skill | What It Does |
|---|---|
| **`/grill-with-docs`** | Grilling session + builds domain model (glossary, `CONTEXT.md`, ADRs) |
| **`/grill-me`** | Non-code grilling — agent asks detailed questions to clarify intent |
| **`/triage`** | Moves GitHub issues through a state machine of triage roles |
| **`/improve-codebase-architecture`** | Scans for deep module opportunities, produces HTML report, guides improvement |
| **`/to-prd`** | Synthesizes conversation into a PRD, publishes to issue tracker |
| **`/to-issues`** | Breaks plan/spec/PRD into independent vertical-slice issues |
| **`/prototype`** | Creates throwaway terminal prototypes or multiple UI variations |

### Model-Invoked Skills (Reusable Discipline)

| Skill | What It Does |
|---|---|
| **`tdd`** | Red-green-refactor loop with guidance on good/bad tests |
| **`diagnosing-bugs`** | Systematic loop: reproduce → minimize → hypothesize → instrument → fix |
| **`domain-modeling`** | Builds shared language document to reduce verbosity |
| **`codebase-design`** | Prioritizes deep modules, reduces architectural entropy |
| **`review`** | Code review — bugs, security, style, documentation |
| **`handoff`** | Session handoff: captures context, decisions, next steps |
| **`writing-great-skills`** | Authoring guide for creating new agent skills |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Hermes skill development** | Use `writing-great-skills` to author new CorpusIQ agent skills |
| **Code review pipeline** | Use `review` + `tdd` for quality gates on PRs |
| **Architecture maintenance** | Run `/improve-codebase-architecture` weekly to prevent entropy |
| **Session handoffs** | Use `handoff` to pass context between agent sessions |
| **Bug triage** | Use `triage` + `diagnosing-bugs` for systematic issue resolution |
| **PRD generation** | Use `/to-prd` + `/to-issues` to convert user conversations into actionable work |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| **Skills not found** | Verify install: `ls ~/.claude/skills/` or `ls .cursor/skills/` |
| **Setup fails** | Run `/setup-matt-pocock-skills` first — it configures required paths |
| **Triage labels missing** | Create GitHub labels: `triage`, `bug`, `enhancement`, `question` |

## Verification

```bash
# Check installed skills
npx skills list | grep mattpocock

# Run the ask-matt router to verify
# In your agent: /ask-matt "I need to improve my codebase architecture"
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
*Powered by CorpusIQ*
---

*
---
*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
