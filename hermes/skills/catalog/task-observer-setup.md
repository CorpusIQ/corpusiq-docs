---
title: Task Observer - Meta-Skill for Continuous Skill Improvement
description: "rebelytics/one-skill-to-rule-them-all - task-observer, 5.4K installs, 2.2K GitHub stars. The meta-skill that watches work sessions and converts friction, corrections, and workflow insights into reusable skill improvements, with an observation log and skill-authoring feedback loop."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/task-observer-setup/"
robots: "index,follow"
last_updated: "2026-09-01"
tags: ["hermes skill", "agent skill", "skill setup", "meta-skill", "skill improvement", "skill governance"]
---

# Task Observer - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/rebelytics/one-skill-to-rule-them-all) (5.4K installs)
**GitHub:** [rebelytics/one-skill-to-rule-them-all](https://github.com/rebelytics/one-skill-to-rule-them-all) (2,220⭐, CC BY 4.0)
**Category:** Skill Lifecycle & Governance
**First Seen:** Feb 18, 2026 (skills.sh)
**Quality Tier:** 🟡 Trusted (Gen Agent Trust Hub Warn / Socket Pass / Snyk Pass)

Task Observer ("One Skill to Rule Them All") is a meta-skill by Eoghan Henn ([rebelytics.com](https://rebelytics.com)) that watches work sessions - autonomous or human - and converts friction into reusable skills. Instead of sitting down to "improve a skill," it formalizes the noticing: patterns, user corrections, workflow insights, and methodology get captured as one observation-log entry per insight, and proposed skill updates land in a review directory. The author's own log: 1,200+ observations across 70 skills in seven months, with most turned into skill improvements. The current version incorporates suggestions from 36 users across 60 issues and 12 pull requests. On the skills.sh hot board as of Sep 1, 2026, with steady 400-650 weekly installs.

---

## Installation

```bash
npx skills add rebelytics/one-skill-to-rule-them-all --skill task-observer
```

Live-verified Sep 1, 2026: `npx skills add rebelytics/one-skill-to-rule-them-all --list` reports "Found 1 skill."

**Hermes manual install** (per the publisher's "other systems" guidance - keep the bundle intact wherever your platform expects skills):

```bash
git clone https://github.com/rebelytics/one-skill-to-rule-them-all.git /tmp/task-observer
mkdir -p ~/.hermes/profiles/corpusiq/skills/task-observer
cp -r /tmp/task-observer/SKILL.md /tmp/task-observer/references /tmp/task-observer/scripts \
  ~/.hermes/profiles/corpusiq/skills/task-observer/
```

The skill runs degraded without `references/` and `scripts/` - it will tell you which files are missing.

## Prerequisites

| Requirement | Details |
|---|---|
| **No API keys** | Fully local - observation logs live on your filesystem |
| **Stable workspace path** | One absolute path that outlives sessions, pinned in the activation config (see Quick Start) |
| **Session-start hook** | The SKILL.md states description matching alone is not enforceable - pair it with an AGENTS.md instruction or a harness session-start hook |
| **Hermes Agent** | Uses the `<available_skills>` convention, which Hermes shares natively |

## What It Provides

| Capability | How It Works |
|---|---|
| **Session observation** | Invoked before the first tool call of any multi-step session; watches for friction, corrections, and workflow patterns |
| **Observation log** | One Markdown file with YAML frontmatter per insight at `[workspace]/skill-observations/observation-log/`; resolved entries archive under `observation-log/archive/` |
| **Skill update proposals** | Proposed skill edits land in `[workspace]/skill-updates/` for review |
| **Skill authoring rules** | `references/skill-authoring.md` - includes a feedback pre-flight with duplicate checks across issues/PRs before submitting upstream |
| **Signals & weekly review** | `references/signals.md` defines what counts as an observation; `references/weekly-review.md` drives the periodic consolidation pass |
| **Bundle validation** | `scripts/validate-skill-bundle.py` checks the skill bundle's own integrity |

## Quick Start

1. Install the skill (above)
2. Pick a stable workspace path, e.g. `~/.hermes/profiles/corpusiq/vault/` - never a cwd inside an ephemeral checkout
3. Add an activation instruction to the profile's AGENTS.md (or a session-start hook): invoke task-observer before the first tool call of any session
4. Run real work. The observer writes observations as friction happens
5. Review `skill-updates/` periodically (or on the weekly-review cadence) and patch skills accordingly

## CorpusIQ Use Cases

- **Quarterly skill audits** - the observation log is the evidence layer: which skills hit friction in production ops, backed by dated entries instead of vibes
- **Skill sweep operations** - sweeps like this one (skills.sh monitoring, docs maintenance) generate friction patterns the observer captures, feeding the improvement loop
- **Session post-mortems** - corrections made during inbox, cron, and monitoring sessions become durable skill patches instead of being lost between sessions
- **Skill authoring feedback loop** - the skill-authoring pre-flight (duplicate check across issues/PRs, upstream-HEAD verification) matches the patch-first discipline used for this catalog
- **Cross-agent consistency** - the same observation discipline applies to dev@, support@, and growth agents, giving a unified improvement stream

## Limitations / Verification

- **Gen Agent Trust Hub Warn** caps the tier at 🟡 Trusted (Socket and Snyk both Pass) - the warning is named in this guide's Security section
- **Claude-architected content** - the publisher's own words: the SKILL.md format is cross-platform but "the content assumes Claude's architecture" (Claude path conventions like `~/.claude/projects/`, Cowork shared folders). Hermes shares the `<available_skills>` convention, but re-pin all workspace paths to a stable Hermes profile path; users have reported successful Hermes and OpenClaw integrations
- **Activation is the weak point** - without the AGENTS.md/hook instruction, description matching alone will not reliably trigger the skill
- **CC BY 4.0** - share and adapt freely with attribution to Eoghan Henn / rebelytics.com
- Verify install: `npx skills list | grep task-observer` (CLI) or `ls ~/.hermes/profiles/corpusiq/skills/task-observer/` (manual)

## Security

[Gen Agent Trust Hub: Warn](https://www.skills.sh/rebelytics/one-skill-to-rule-them-all/task-observer/security/agent-trust-hub) · [Socket: Pass](https://www.skills.sh/rebelytics/one-skill-to-rule-them-all/task-observer/security/socket) · [Snyk: Pass](https://www.skills.sh/rebelytics/one-skill-to-rule-them-all/task-observer/security/snyk)

## Related

- [Skill Creator - Anthropic's Skill Creation Framework Setup](/hermes/skills/catalog/skill-creator-setup)
- [Wyatt Walsh Agents - Skill Governance and Orchestration Suite Setup](/hermes/skills/catalog/wyattowalsh-agents-setup)
- [Distribute Skill To All Agents Setup](/hermes/skills/catalog/distribute-skill-to-all-agents-setup)

---

*← [Skills Catalog](/hermes/skills/catalog) →*
*Powered by CorpusIQ*
