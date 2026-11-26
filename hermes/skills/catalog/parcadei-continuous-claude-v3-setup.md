---
title: "Continuous Claude - Context Management for Claude Code Setup"
description: "parcadei/continuous-claude-v3 - 53.4K combined installs: context management for Claude Code with hooks, ledgers, handoffs, and multi-agent orchestration."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/parcadei-continuous-claude-v3-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "claude code", "context management", "multi-agent"]
---

# Continuous Claude - Setup Guide

**Source:** [parcadei/continuous-claude-v3](https://www.skills.sh/parcadei/continuous-claude-v3) via skills.sh - 53.4K combined installs across 96 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 evening sweep)
**GitHub:** [parcadei/Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3) - 3,953 stars, MIT license, last pushed Nov 16, 2026, main branch; skills in .claude/skills/<name>/SKILL.md alongside .claude/agents/ and .claude/hooks/.
**Category:** Developer Workflows (Claude Code / Multi-Agent)
**Quality Tier:** 🟡 Yellow - 15 sampled skills: four carry a Warning (three on Snyk, one on Gen Agent Trust Hub) and eleven pass all three checks; no Fails.

parcadei/continuous-claude-v3 is Continuous Claude, a persistent, learning, multi-agent development environment built on Claude Code. It attacks Claude Code's compaction problem by extracting learnings automatically and handing context across sessions through continuity ledgers and YAML handoffs, so each session starts fresh with full context. The 96 indexed listings surface the repository's skills; the full install bundles 109 skills, 32 specialized agents, and 30 lifecycle hooks together.

The suite runs on three layers: natural-language skills in .claude/skills/, specialized sub-agents in .claude/agents/, and hooks in .claude/hooks/ that maintain state at SessionStart, PreToolUse, PreCompact, and SessionEnd. A PostgreSQL plus pgvector memory daemon and a TLDR five-layer code-analysis stack (about 95 percent token savings) round out the system. The project's mantra is "compound, don't compact": extract learnings automatically, then start fresh with full context.

## Installation

The README documents a 12-step setup wizard. The pyproject.toml lives in the opc/ directory, so uv commands must run from there.

```bash
# Clone
git clone https://github.com/parcadei/Continuous-Claude-v3.git
cd Continuous-Claude-v3/opc

# Run setup wizard (12 steps)
uv run python -m scripts.setup.wizard
```

The wizard backs up any existing .claude/ config, checks prerequisites (Python 3.11+, uv, Docker), starts the PostgreSQL stack, and installs the agents, skills, and hooks into ~/.claude/. It offers a copy mode (default) and a symlink mode for contributors. Uninstall with `uv run python -m scripts.setup.wizard --uninstall`.

## What It Provides

skills.sh publishes per-skill install counts for all 96 indexed listings. The 8 most-installed skills are listed below; the remaining 88 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| discovery-interview | 4,199 | Deep interview process to turn vague ideas into detailed specs |
| premortem | 916 | Identify failure modes before they occur with structured risk analysis |
| math | 889 | Unified symbolic and numeric computation via SymPy, Z3, and Pint |
| github-search | 745 | Search GitHub code, repositories, issues, and PRs via MCP |
| dead-code | 745 | Find unused functions and dead code in the codebase |
| refactor | 625 | Code refactoring workflow from analysis through validation |
| recall-reasoning | 605 | Search past reasoning for relevant decisions and approaches |
| graceful-degradation | 603 | Graceful degradation with helpful messages |

The remaining 88 indexed listings range from 479 to 581 installs.

## Why This Matters for Hermes Agents

Continuous Claude encodes the exact problem a long-running agent hits: context fills up, compaction drops decisions, and the next session starts cold. Its ledgers and handoffs preserve state across clears and sessions, and the memory daemon extracts learnings from the reasoning that would otherwise be thrown away. For a builder running agent fleets, the meta-skills (/fix, /build, /explore, /tdd) give a known-good workflow instead of improvisation, and the TLDR code-analysis hooks cut token spend by replacing full-file reads with layered summaries. The premortem and security skills add pre-flight risk checks that catch failures before implementation. The main caveat is scope: this is a Claude Code harness, not a Hermes plugin, so you adopt its workflow conventions wholesale rather than cherry-picking a few skills.

## Usage

| You say | What happens |
|---|---|
| Fix the broken login | Uses /fix workflow, routing to debug-agent and scout |
| Build a user dashboard | Uses /build workflow, routing to plan-agent and kraken |
| What could go wrong with this plan | Uses premortem for structured risk analysis |
| Find all usages of this API | Uses scout agent with ast-grep structural search |
| Done for today | Uses create_handoff to save session state for next time |
| Resume where we left off | Uses resume_handoff to restore prior context |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/parcadei/Continuous-Claude-v3/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/parcadei/Continuous-Claude-v3/main/.claude/skills/discovery-interview/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skill before relying on it, and re-check the security pages on skills.sh for the Warnings noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| discovery-interview | Pass | Pass | Warn |
| premortem | Pass | Pass | Pass |
| math | Pass | Pass | Pass |
| github-search | Pass | Pass | Warn |
| dead-code | Pass | Pass | Pass |
| refactor | Pass | Pass | Pass |
| recall-reasoning | Pass | Pass | Pass |
| graceful-degradation | Pass | Pass | Pass |
| explore | Warn | Pass | Pass |
| agentic-workflow | Pass | Pass | Pass |
| modular-code | Pass | Pass | Pass |
| math-help | Pass | Pass | Pass |
| sub-agents | Pass | Pass | Pass |
| perplexity-search | Pass | Pass | Warn |
| security | Pass | Pass | Pass |

Of the 15 sampled listings, four carry a Warning (explore on Gen Agent Trust Hub; discovery-interview, github-search, and perplexity-search on Snyk) and eleven pass all three checks, with no Fails. The remaining 81 indexed listings were not sampled.

## Limitations

- Snapshot data, verified Nov 25, 2026: 53,409 combined installs across 96 indexed listings; 3,953 GitHub stars; MIT license; last pushed Nov 16, 2026. Counts drift over time.
- The security sample covers 15 of 96 listings; the other 81 listings have no skills.sh verdict published here.
- The 96 install-index listings do not map one-to-one onto the README's "109 skills": nested math subtopics are indexed separately while some top-level skills are not listed individually.
- Installation targets ~/.claude/ directly and requires Python 3.11+, uv, Docker for the PostgreSQL container, and the Claude Code CLI.
- The memory and continuity systems depend on a running PostgreSQL instance, which the wizard manages via Docker.
- The README notes the agent set is larger than it needs to be and lists agent consolidation as a v4 goal.

## Related

[AgentMemory Setup - Persistent Memory for Hermes Agents](/hermes/skills/catalog/agentmemory-setup) | [Proactive Agent - WAL Memory and Compaction Recovery Setup](/hermes/skills/catalog/proactive-agent-setup) | [Subagent-Driven Development - Skill Setup Guide](/hermes/skills/catalog/subagent-driven-development-setup) | [Basilic Skills - Slash Playbooks for Coding Agents](/hermes/skills/catalog/basilic-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run premortem before any significant implementation; it surfaces failure modes while they are still cheap to fix.
- End sessions with create_handoff ("Done for today") so the next session resumes with full context instead of a cold start.
- Keep uv commands in the opc/ directory; the pyproject.toml lives there and the wizard expects that working directory.
- Use copy mode for a stable daily setup and symlink mode only if you plan to contribute changes back.
- Run /onboard in an existing project to generate an initial continuity ledger before relying on the recall system.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
