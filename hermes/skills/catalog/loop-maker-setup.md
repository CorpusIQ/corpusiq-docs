---
title: Loop Maker — Agent Loop Scaffolding Setup Guide
description: Install and configure EricTechPro/loop-maker — cross-harness agent skill that interviews you and scaffolds a self-running autonomous loop with verifier, state file, and human gate
---

# Loop Maker — Skill Setup

**Source:** [EricTechPro/loop-maker](https://github.com/EricTechPro/loop-maker)
**Stars:** 0 ⭐ | **License:** MIT
**Created:** June 24, 2026
**Category:** Agent Infrastructure / Loop Engineering / Automation
**Cross-Harness:** Claude Code · Codex · Hermes · OpenClaw

---

## 1. What It Is

A portable agent skill that interviews you through a 7-question wizard and scaffolds a self-running autonomous loop — complete with separate verifier, state file, stop conditions, and human gate. Works across all major agent harnesses.

**Why most loops fail (and how this catches it):**
1. ❌ Agent judges its own work → ✅ Separate verifier built into scaffold
2. ❌ State leaks into the skill file → ✅ Dedicated STATE.md outside the skill
3. ❌ No stop condition → ✅ Stop condition wired in before you run

---

## 2. Prerequisites

- Any supported agent harness (Hermes Agent, Claude Code, Codex CLI, or OpenClaw)
- No additional packages required

---

## 3. Installation

```bash
git clone https://github.com/EricTechPro/loop-maker.git
cp -r loop-maker ~/.hermes/skills/loop-maker
```

### Verify

```bash
ls ~/.hermes/skills/loop-maker/
# Should show: SKILL.md
```

---

## 4. The 7-Question Wizard

When invoked, `loop-maker` asks these questions one at a time:

| # | Question | What It Catches |
|---|----------|-----------------|
| 1 | **Goal** — What checkable condition means "done for now"? | Vague/unfalsifiable goals |
| 2 | **Trigger** — What starts each run? Schedule, event, or run-until-done? | Undefined activation |
| 3 | **Discovery** — How does it find the work to do each round? | Blind loops with nothing to do |
| 4 | **Action** — What's it allowed to do, and through which tools? | Unbounded capabilities |
| 5 | **Verification** — Who checks the result, and against what? | Agent self-grading |
| 6 | **State** — Where does "what's done / what's left" live? | Amnesia between runs |
| 7 | **Human gate** — Which actions are irreversible and must ask first? | Catastrophic automation |

### Output

```
loop-output/
├── SKILL.md          # The loop skill definition
├── STATE.md          # Persistent state file (outside the skill)
├── verifier.py       # Separate verification script
└── README.md         # Runbook for the loop
```

---

## 5. Usage

```bash
# Start the loop wizard
hermes -s loop-maker "I need a loop that..."

# The skill interviews you through the 7 questions
# Then emits a ready-to-run loop folder
```

---

## 6. Comparison: Loop Maker vs Perfectloop

| Feature | Loop Maker | Perfectloop |
|---------|------------|-------------|
| Questions | 7 (goal through human gate) | 8 (adds verifier-verification + scheduler cleanup) |
| Cross-harness | ✅ Claude Code, Codex, Hermes, OpenClaw | Hermes-specific |
| Output | Folder: SKILL.md + STATE.md + verifier.py | YAML loop spec |
| Interview style | Conversational wizard | Formal 8-question contract |
| Rejection | Scaffolds anyway (warns) | Flatly rejects bad candidates |
| Best for | Quick loop prototyping, cross-platform | Production-critical loops, safety-first |

---

## 7. CorpusIQ Use Cases

| Automation | Loop Maker Application |
|------------|----------------------|
| **Daily skills sweep** | Trigger: cron; Verify: GitHub API returns valid; State: last_discovered_id |
| **Email watchdog** | Trigger: poll interval; Verify: SMTP delivery confirmed; Human gate: auto-reply content |
| **Lead qualification pipeline** | Trigger: new email; Verify: human reviews first 5; State: qualified_leads.json |
| **Competitive monitoring** | Trigger: daily; Verify: diff against previous run; State: last_snapshot.json |

---

## 8. Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Loop output missing verifier | Interview skipped question 5 | Re-run; question 5 is mandatory |
| STATE.md grows without bound | No cleanup defined | Add `max_entries` or `ttl_days` to state management |
| Loop runs forever | Stop condition too vague | Use a concrete, checkable condition (count, timestamp, boolean) |
| Cross-harness compatibility | Tool names differ | Loop Maker uses abstract tool references — bind to your harness |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 24 Evening Discovery](/hermes/skills/marketplace/new-june24-2026-evening/) →*
