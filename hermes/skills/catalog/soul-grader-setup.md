---
title: SOUL Grader — Full Setup Guide for Hermes Agents
description: Install, configure, and use the soul-grader skill from cobibean/soul-grader-skill. Grade, review, and approve Hermes Agent SOUL.md identity files with a research-backed rubric.
---

# SOUL Grader — Setup Guide

**Source:** [cobibean/soul-grader-skill](https://github.com/cobibean/soul-grader-skill) (25⭐, community skill)
**Category:** Agent Identity & Governance

Grade, review, rewrite, or approve a Hermes Agent `SOUL.md` identity file using a narrow, research-backed rubric. The bundled grading standard is the only normative source — no generic prompt-engineering advice or personal taste. Scores 11 categories out of 100 with automatic fail conditions for secrets, false claims, and missing safety gates.

---

## Installation

```bash
npx skills add cobibean/soul-grader-skill
```

Or clone directly for manual inspection:

```bash
git clone https://github.com/cobibean/soul-grader-skill.git
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Any version. SOUL.md loading behavior is consistent across releases. |
| **Target SOUL.md** | A SOUL.md file to grade (local path or inline text). |
| **Adjacent files (optional)** | `CLAUDE.md`, `AGENTS.md`, manifests, or operator guides — only needed for contradiction checks and artifact separation scoring. |

---

## Key Capabilities

### Core Features

| Capability | How to Trigger | Notes |
|---|---|---|
| **Full SOUL grade** | "Grade this SOUL.md" or "Review my agent SOUL" | Returns 11-category score table, automatic blockers, drift risks, suggested wording |
| **Quick grade** | "Quick grade this SOUL" | Returns score/verdict, deployability, biggest issue, top 3 fixes |
| **SOUL rewriting** | "Rewrite this weak SOUL" or "Make this SOUL stronger" | Patches from bundled research artifacts, not generic advice |
| **Fleet grading** | "Grade all my agent SOULs" | Uses fleet workflow reference — active/retired classification, contradiction checks |
| **Deployability check** | "Is this SOUL ready to deploy?" | Runs automatic fail scan first (secrets, false claims, missing gates) |
| **Deep research** | "Do a SOUL research project" | Swarm deliverable pattern — independent research lanes, static HTML review surface |

### Grading Rubric (11 Categories, 100 Points)

| Category | Points | What It Evaluates |
|---|---|---|
| Mission clarity | 15 | Names who/what the agent serves and what outcome matters |
| Identity + negations | 12 | What the agent is and what it must not become |
| Core thesis | 10 | Durable decision lens about the user/domain/problem |
| Optimization hierarchy | 10 | Ranks tradeoffs instead of listing virtues |
| Hard constraints | 10 | 3–5 true filters with approval/override semantics |
| Soft preferences | 8 | Separates scoring signals from bans |
| Authority + escalation | 10 | Allowed / ask-before / never boundaries |
| Voice + truthfulness | 10 | Tone, vocabulary, never-claims, evidence thresholds |
| Success / artifacts | 8 | Durable/verifiable completion definitions |
| Artifact separation | 5 | Keeps commands, workflows, secrets elsewhere |
| Runtime hygiene | 2 | Fits Hermes loading behavior, avoids hidden assumptions |

### Automatic Fail Conditions

- Secrets, tokens, passwords, API keys in SOUL
- False or unverified claims of access, deployment state, or authority
- Ungated spend, publishing, outreach, destructive edits
- Cross-client data/credential contamination
- Assuming YAML frontmatter is hidden from Hermes (it's visible prompt text)
- Contradictions with nearby operating files or approval policy

### Verdict Bands

| Score | Verdict | Meaning |
|---|---|---|
| 90–100 | Excellent | Production-grade; keep reviewed as scope changes |
| 75–89 | Operational | Usable; patch missing layers before high-risk autonomy |
| 60–74 | Scaffold | Serviceable draft; needs constraints, negations, or success artifacts |
| 0–59 | Needs rewrite | Rewrite from mission/constraints upward |
| Any auto-fail | Not deployable | Blocker must be resolved before deployment |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **New agent onboarding** | Grade every new agent's SOUL.md before deployment — catch missing gates, false claims, and secret leaks |
| **Agent identity drift detection** | Re-grade SOUL.md monthly; compare scores to catch mission drift, constraint erosion, or scope creep |
| **Client agent handoff** | Grade client-facing agent SOULs before delivery — ensures isolation, approval, and credential language is correct |
| **SOUL authoring** | Use the wording standards and rubric to author strong SOUL.md files from scratch — operational language, no vibes |
| **Fleet audit** | Run fleet-wide grading across all deployed Hermes agents — classify active/retired, catch contradictions, generate remediation reports |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| **Bundled references missing** | The grader stops and reports "source bundle missing" — re-clone the skill or check `references/` directory |
| **Frontmatter treated as hidden** | Hermes native SOUL loading injects SOUL as prompt text; YAML is visible. Move secrets to env vars or config |
| **Session cache ignores SOUL fix** | A corrected SOUL may not affect a running session — restart Hermes or start a new session |
| **Adjacent file contradictions** | If CLAUDE.md or AGENTS.md conflicts with SOUL, the grader flags it — decide which file owns the rule |

### Verification

```bash
# Verify skill installed
hermes skills list | grep soul-grader

# Quick functional test — load the grading standard reference
# (run inside a Hermes session)
skill_view(name="soul-grader", file_path="references/soul-md-grading-standard.md")
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Home](/hermes/) →*
*Powered by CorpusIQ*
