---
title: "OpenClaw Agent Skills — Official OpenClaw Org Skill Suite Setup"
description: "openclaw/agent-skills — 8 skills, ~2.0K installs: the OpenClaw org's canonical agent workflow suite covering structured code review (autoreview), PR/issue transcript provenance, session inspection, prompt handoff, and black-box behavior validation."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/openclaw-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-19"
tags: ["hermes skill", "agent skill", "skill setup", "openclaw", "code review", "agent handoff", "session viewer"]
---

# OpenClaw Agent Skills — Setup Guide

**Source:** [openclaw/agent-skills](https://skills.sh/openclaw/agent-skills)
**GitHub:** [openclaw/agent-skills](https://github.com/openclaw/agent-skills)
**Skills:** 8 skills · ~2.0K total installs
**Category:** Agent Operations
**First Seen:** August 19, 2026 sweep
**Quality Tier:** 🟡 Beta — official OpenClaw org repository (1,057 GitHub stars, actively maintained — last commit August 18, 2026); install counts still growing

This is the public canonical source for shared agent workflows from the OpenClaw organization itself. The goal stated in the repo: write a workflow once, reuse it everywhere, and avoid hand-copying long SKILL.md files across repos. The 8 skills cluster into three families — review (autoreview, behavior-validator, crabbox), handoff/context (handoff, agent-transcript), and sessions/documentation (session-viewer, beam, readme-standard). autoreview is the flagship at 1,388 installs, a structured multi-engine code review workflow (Codex, Claude, Amp, Pi, Kimi) that reports blocking issues only when explicitly requested.

---

## Installation

Install everything via the bundled installer (lists, dry-runs, and selective installs supported):

```bash
git clone https://github.com/openclaw/agent-skills.git
cd agent-skills
scripts/install-skills --list          # see available skills
scripts/install-skills --dry-run       # preview without changes
scripts/install-skills                 # all skills, default agent skill dir
scripts/install-skills autoreview crabbox   # selective
scripts/install-skills --target ~/.codex/skills autoreview   # custom target
scripts/install-skills --mode copy --target ~/.agents/skills  # copies, not symlinks
```

Or via the skills.sh marketplace (skills are indexed there):

```bash
npx skills add openclaw/agent-skills
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skills.sh installer path |
| **An agent runtime** | Skills assume a Codex/Claude/OpenClaw/Pi-style SKILL.md runtime |
| **Codex (optional)** | autoreview's default review engine (`gpt-5.6-sol`, high reasoning) |
| **GitHub CLI or git** | agent-transcript writes PR/issue bodies; crabbox runs remote validation |

## What It Provides

| Skill Group | Skills | Purpose |
|---|---|---|
| Review | autoreview, behavior-validator, crabbox | Structured code review closeout, source-blind behavior validation against a contract, and Crabbox/Testbox remote proof (Linux/macOS/Windows/WSL2) |
| Handoff | handoff, agent-transcript | Clipboard-ready prompt handoff to another agent; redacted local-only PR/issue transcript provenance |
| Sessions | session-viewer, beam | Local searchable HTML viewer for agent session JSONL; authenticated redacted publication of sessions to an OpenClaw catalog |
| Documentation | readme-standard | House README structure, badge row, tone, and verification gates for steipete/openclaw repos |

Top skills by installs: autoreview (1,388), agent-transcript (355), session-viewer (66), handoff (62), behavior-validator (49), crabbox (42).

## Quick Start

1. Clone and list: `git clone https://github.com/openclaw/agent-skills.git && cd agent-skills && scripts/install-skills --list`
2. Install the flagship: `scripts/install-skills autoreview`
3. For review closeout, say "run autoreview on this change" — it reports P0 blocking issues by default
4. For handoffs, say "write a handoff for the next agent" — it builds a standalone prompt and copies it to the clipboard

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Agent code review closeout** | autoreview's P0-only default output maps to our verify-before-assertion discipline — blocking issues only, advisory output, no blind apply |
| **Multi-agent handoffs** | handoff builds path-free standalone prompts for fresh agents — matches our multi-agent orchestration and delegation patterns |
| **Session forensics** | session-viewer renders session JSONL as searchable single-file HTML — useful for auditing agent runs and sharing context |
| **PR/issue transparency** | agent-transcript attaches sanitized agent transcripts to PRs (redacted, fail-closed on secrets) — matches our public-content sanitization rules |
| **Behavior validation** | behavior-validator checks user-visible behavior against a contract without source inspection — useful for testing skills against their documented behavior |

## Limitations / Verification

- Below the 20K install guide bar — drafted on official-org authority (the OpenClaw org itself, 1,057 GitHub stars, last commit August 18, 2026)
- Skills are Codex/OpenClaw-first; Hermes usage works via SKILL.md conventions but the installer targets generic agent skill directories
- agent-transcript is explicitly best-effort and local-only; PR/issue creation continues without it
- beam requires an authenticated OpenClaw receiver endpoint

```bash
npx skills add openclaw/agent-skills   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)
- [OpenClaw Audit Watchdog Setup](/hermes/skills/catalog/openclaw-audit-watchdog-setup/)
- [OpenClaw Skill Vetter Setup](/hermes/skills/catalog/openclaw-skill-vetter-setup/)

*Powered by CorpusIQ*
