---
title: Hermes Agent Self-Evolution — Auto-Learning Skill Framework
description: Aradotso community skill for Hermes agent self-evolution. Agents learn from past tasks, auto-create reusable skills, and improve over time. 280+ installs.
---

# Hermes Agent Self-Evolution — Setup Guide

**Source:** [aradotso/hermes-skills](https://github.com/aradotso/hermes-skills)
**Skill:** `hermes-agent-self-evolution` · **Installs:** 280+ · **Category:** Agent Learning / Meta
**Platform:** Linux, macOS, Windows

A self-improvement framework for Hermes agents that learns from completed tasks, automatically creates reusable skills, and continuously improves performance. Agents observe their own execution patterns, identify reusable workflows, and codify them as new skills — reducing manual curation and accelerating capability growth.

---

## Installation

```bash
# Install via skills.sh
npx skills add aradotso/hermes-skills --skill hermes-agent-self-evolution -g -y
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | v0.16.0+ |
| **Skill Directory** | `~/.hermes/profiles/<profile>/skills/` must be writable |
| **Session DB** | Active session database with at least 5 past sessions |

---

## How Self-Evolution Works

The framework operates on a 5-stage learning loop:

### Stage 1: Observe

After every complex task (5+ tool calls), the agent captures:
- What was the goal?
- What tools were used?
- What errors were encountered?
- What was the resolution?
- How many turns did it take?

### Stage 2: Pattern Match

The framework compares the captured execution against:
- Past tasks with similar goals
- Existing skills (to avoid duplicates)
- Known pitfalls from previous sessions

### Stage 3: Synthesize

When a pattern repeats 3+ times, the framework proposes a new skill:
- Generates `SKILL.md` with proper frontmatter
- Extracts the workflow steps from observed executions
- Documents pitfalls that recurred
- Adds verification steps that confirmed success

### Stage 4: Validate

Before the skill is activated:
- Dry-run against the task that triggered creation
- Verify all commands are copy-paste runnable
- Check for hardcoded secrets or paths
- Validate YAML frontmatter syntax

### Stage 5: Activate

The skill is written to the skills directory and loaded on next session:
- Appears in `hermes skills list`
- Loaded automatically when trigger conditions match
- Tracked for usage and success rate

---

## Configuration

The self-evolution framework respects these thresholds:

| Parameter | Default | Description |
|-----------|:-------:|-------------|
| `min_complexity` | 5 | Minimum tool calls to trigger observation |
| `pattern_threshold` | 3 | Times a pattern must repeat before skill creation |
| `max_auto_skills_per_day` | 3 | Cap on auto-created skills to prevent noise |
| `review_required` | false | If true, skills are proposed but not activated until human review |

---

## What Gets Learned

The framework detects these patterns:

| Pattern Type | Example |
|-------------|---------|
| **Workflow** | "Fetch data → analyze → generate chart → send report" |
| **Error Recovery** | "API rate limit → wait 60s → retry with backoff" |
| **Tool Combination** | "Always pair `web_search` with `web_extract` for research tasks" |
| **Verification** | "After sending email, check sent folder for message ID" |
| **Platform-Specific** | "On macOS, use `brew`; on Linux, use `apt`" |

---

## Managing Auto-Created Skills

```bash
# List skills, including auto-created (marked with 🤖)
hermes skills list

# Review a proposed skill before activation
hermes skills review <skill-name>

# Disable an auto-created skill
hermes skills disable <skill-name>

# Manually trigger pattern analysis
hermes skills evolve --analyze-last 10
```

---

## Limitations

This is a **community skill** (not official Nous Research). It auto-generates skills by pattern matching — quality varies. Some generated skills may be:
- Too specific (only works for one exact scenario)
- Missing edge cases the agent hasn't encountered yet
- Redundant with existing skills (check before activating)

**Best practice:** Use as a "first draft" generator. Review, edit, and refine auto-created skills before relying on them in production workflows.

---

## Example: Auto-Created Skill

After observing 7 sessions where the agent:
1. Searched Reddit for CorpusIQ mentions
2. Extracted relevant threads
3. Drafted helpful responses
4. Posted via Reddit API

The framework generated:

```yaml
---
name: reddit-mention-response
description: "Monitor Reddit for CorpusIQ mentions and respond helpfully."
version: 0.1.0-auto
metadata:
  hermes:
    tags: [reddit, social, monitoring, corpusiq]
    auto_generated: true
    source_sessions: 7
---
```

---

## Related Skills

- [Hermes Agent Core](/hermes/skills/catalog/hermes-agent-setup/) — Official core skill
- [Hermes Agent Skill Authoring](/hermes/skills/catalog/hermes-agent-skill-authoring-setup/) — Writing SKILL.md files
- [Aradotso Hermes Skills Collection](https://skills.sh/aradotso/hermes-skills)
