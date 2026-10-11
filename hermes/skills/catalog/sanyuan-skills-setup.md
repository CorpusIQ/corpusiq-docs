---
title: "Sanyuan Skills - Production Agent Skills Suite Setup"
description: "Setup guide for sanyuan0704/sanyuan-skills - 30.0K combined installs. Six production-grade skills: code review, tutoring, and skill authoring."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sanyuan-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "skill authoring", "tutoring"]
---

# Sanyuan Skills - Setup Guide

**Source:** [sanyuan0704/sanyuan-skills](https://www.skills.sh/sanyuan0704/sanyuan-skills) via skills.sh - 30.0K combined installs across 6 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [sanyuan0704/sanyuan-skills](https://github.com/sanyuan0704/sanyuan-skills) (3,939 stars, MIT license; pushed May 11, 2026; `skills/<name>/SKILL.md` layout)
**Category:** Agent Workflow / Code Review
**Quality Tier:** 🟡 Beta - 3,939-star MIT collection (Sanyuan); production-grade skill set; all sampled verdicts Pass

Sanyuan (sanyuan0704), known for in-depth writing on React internals, publishes this collection of production-grade agent skills for Claude Code and other agent terminals. Six skills cover two loops a working engineer repeats constantly. The first is code review: `code-review-expert` at 13,310 installs runs a senior-engineer pass over a diff covering SOLID, security, performance, error handling, and boundary conditions. The second is learning and library upkeep: `sigma` and `book-study` run Socratic tutoring with mastery checks, `wiki-ingest` compiles sources into a cross-referenced knowledge base, and `skill-forge` plus `skill-review` create and audit skills.

The collection is deliberately small and composable. Every skill lives at `skills/<name>/SKILL.md` and installs independently, so you can adopt the code-review pass without taking the tutoring stack. All six listings are above 2,100 installs, and the README ships a per-skill install command for each one.

---

## Installation

Prerequisites: Node.js, since every skill installs through the `npx` skills CLI.

```bash
# Install the full collection
npx skills add sanyuan0704/sanyuan-skills
```

The README ships a per-skill install command for each skill, useful when you only need one:

```bash
npx skills add sanyuan0704/sanyuan-skills --path skills/code-review-expert
npx skills add sanyuan0704/sanyuan-skills --path skills/sigma
npx skills add sanyuan0704/sanyuan-skills --path skills/skill-forge
npx skills add sanyuan0704/sanyuan-skills --path skills/book-study
npx skills add sanyuan0704/sanyuan-skills --path skills/wiki-ingest
npx skills add sanyuan0704/sanyuan-skills --path skills/skill-review
```

Once installed, invoke each skill from your agent terminal:

```bash
/code-review-expert    # Review current git changes
/sigma <topic>         # Start a tutoring session
/skill-review          # Audit an existing skill's quality
/skill-forge           # Create a new skill
/wiki-ingest           # Compile content into a wiki knowledge base
/book-study <book>     # Start a guided reading session
```

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| code-review-expert | 13,310 | Senior-engineer code review covering SOLID, security, performance, error handling, and boundary conditions |
| sigma | 4,661 | 1-on-1 AI tutor built on Bloom's 2-Sigma mastery learning with Socratic questioning |
| skill-forge | 4,000 | Meta-skill for creating high-quality skills with 12 battle-tested techniques |
| book-study | 3,276 | Reading coach with knowledge compilation, Socratic mastery testing, spaced repetition, and cross-book querying |
| wiki-ingest | 2,587 | Compile articles, documents, or notes into a structured, cross-referenced wiki knowledge base |
| skill-review | 2,135 | Quality audit for skills: structure, description, workflow, token efficiency, and anti-patterns |

All 6 indexed listings clear the 500-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Code review is one of the highest-leverage places to put an agent, and `code-review-expert` encodes the checklist a senior engineer applies on every diff instead of offering generic commentary. The skill-library half matters just as much for teams now maintaining dozens of their own skills: `skill-forge` packages 12 techniques for writing new ones well, and `skill-review` audits existing skills for structure, token efficiency, and anti-patterns before they get shared. The learning skills (`sigma`, `book-study`, `wiki-ingest`) turn the same agent into a patient tutor and a knowledge compiler, which fits long research sprints where context has to be rebuilt fast. Everything installs per-skill through the standard `npx skills add` flow, so a Hermes agent can pull in just `code-review-expert` and grow from there. The repo is small, MIT, and readable end to end, which makes it a useful study model for teams writing their own production skills.

## Usage

| You say | What happens |
|---|---|
| "Review my staged changes before I commit" | code-review-expert runs a senior review pass over the diff: SOLID, security, performance, error handling, boundary conditions |
| "Teach me React Server Components from scratch" | sigma starts a Socratic tutoring session and tests mastery as you go |
| "Audit the skill we just wrote" | skill-review checks structure, description, workflow, token efficiency, and anti-patterns |
| "Draft a skill for our deploy runbook" | skill-forge applies its 12 techniques to produce a well-structured new skill |
| "Turn these API docs and notes into a wiki" | wiki-ingest compiles the mixed sources into a cross-referenced knowledge base |
| "Coach me through this book in two weeks" | book-study schedules the reading, tests mastery, and links ideas across books |

## Verification

```bash
# Confirm the install through the skills CLI
npx skills list | grep -i sanyuan

# Or check the skills directory your agent scans
ls ~/.claude/skills/ | grep -E 'code-review-expert|skill-forge'

# Review the flagship skill straight from GitHub before installing
curl -sL https://raw.githubusercontent.com/sanyuan0704/sanyuan-skills/main/skills/code-review-expert/SKILL.md | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| code-review-expert | Pass | Pass | Pass |
| code-review | - | - | - |
| codex-review | - | - | - |

The scored sample passes on all three engines, but coverage is partial: only `code-review-expert` has verdict rows; the tutoring and skill-authoring skills were not sampled.

## Limitations

- The collection comes from a single independent author; it is six focused skills rather than a broad framework.
- Maintenance cadence: the repo was last pushed May 11, 2026, so it predates the newest agent-platform conventions.
- Verdict coverage is partial; extend the security review to the unsampled skills before production use.
- No MCP servers, hooks, or automation layer ship with the collection; these are plain SKILL.md skills.
- Snapshot data, verified Oct 10, 2026: 29,969 combined installs across 6 indexed listings; 3,939 GitHub stars; MIT; last pushed May 11, 2026. Counts drift over time.

## Related

- [Skill Vetter - Security Audit for Hermes Skills Setup](/hermes/skills/catalog/skill-vetter-setup) - audit any skill's security before you install it
- [Agent Skill Creator - Skill Generation and Templating Setup](/hermes/skills/catalog/agent-skill-creator-setup) - another take on generating new skills from templates
- [Book-to-Skill - Book to Agent Skill Converter Setup](/hermes/skills/catalog/book-to-skill-setup) - turn book notes into a reusable skill, complementing book-study
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `code-review-expert` alone; run it on staged diffs before commits and calibrate expectations from its feedback.
- Pair the authoring loop: draft with `skill-forge`, then press `skill-review` on the result before sharing it.
- For `sigma`, state your current level and target depth in the prompt; the mastery checks adapt better with that context.
- `wiki-ingest` takes mixed sources (articles, docs, raw notes); feed it captures and let it build the cross-references.
- Install per-skill with `--path` when you only need one; the collection is small, but there is no reason to carry skills the agent will not use.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
