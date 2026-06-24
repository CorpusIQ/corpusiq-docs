---
title: Perfectloop — Agent Loop Design Framework Setup Guide
description: Install and configure sebmarion/hermes-agent-skill-perfectloop — a design-layer framework for building safe, testable, gated agent loops with objective verification
---

# Perfectloop — Loop Design Framework Setup

**Source:** [sebmarion/hermes-agent-skill-perfectloop](https://github.com/sebmarion/hermes-agent-skill-perfectloop)
**Stars:** 0 ⭐ | **License:** MIT
**Created:** June 24, 2026
**Category:** Agent Infrastructure / Loop Engineering
**SKILL.md size:** 21KB (largest single skill file this week)

---

## 1. What It Is

A design-layer framework for turning vague automation ideas into safe, testable agent loops. Uses an 8-question core interview before any loop is designed — and will flatly reject bad loop candidates.

**Core philosophy:** The job is not to "make an agent" by writing a big prompt. The job is to design the system that repeatedly prompts, observes, verifies, records state, learns, and safely decides the next action.

```text
Act → Observe → Learn → Repeat
         ↑
    External gate (not the agent)
```

### When It Says "No"

The skill's first job is a **loop fit test**. It kills:
- Vague or unfalsifiable goals ("monitor sentiment")
- Tasks that happen once (use a script, not a loop)
- Judgment-call work that can't be externally verified
- Tasks where the agent would grade its own homework

## 2. Prerequisites

- Hermes Agent (works with cron jobs, watchdogs, background agents)
- No special tools — pure skill definition

## 3. Installation

```bash
git clone https://github.com/sebmarion/hermes-agent-skill-perfectloop.git
cp -r hermes-agent-skill-perfectloop ~/.hermes/skills/perfectloop
```

### Verify

```bash
ls ~/.hermes/skills/perfectloop/
# Should show: SKILL.md  references/
```

## 4. The 8-Question Interview

Before any loop is designed, Perfectloop answers these in order:

1. **Should this be a loop at all?** — If the task happens once, say no.
2. **What exactly is the falsifiable goal?** — Must be provably done or not done ("100 emails sent by 5 PM", not "improve engagement").
3. **What outside signal can reject bad output?** — Must exist. The agent cannot verify its own work.
4. **What persistent state survives between runs?** — A JSON file, DB row, or checkpoint that outlives the agent process.
5. **What can the agent do, and what is forbidden?** — Explicit permission boundaries.
6. **When does the loop stop, escalate, or clean itself up?** — Terminal conditions, budget limits, max retries.
7. **Who/what verifies the verifier?** — Prevent the gate itself from going rogue.
8. **If scheduled, what cleanup proves the controller is removed?** — Proof the cron job can be cleanly disabled.

If any answer is missing and materially changes the design, the skill asks the user. If low-stakes, it states a default and continues.

## 5. Loop Design Output

After the interview, Perfectloop emits a portable loop spec:

```yaml
# Example loop spec output
loop:
  goal: "Send daily newsletter to 1,000 subscribers by 8 AM SGT"
  falsifiable: ">= 995 deliveries with < 5% bounce rate"
  gate:
    type: "log-based"  # Mailgun logs prove delivery
    hosted_by: "external script (not this agent)"
  state:
    file: "/tmp/newsletter-loop.json"
    fields: [last_run, sent_count, bounce_count, next_issue_id]
  budget:
    max_tokens: 500000
    max_api_calls: 100
    max_wall_clock: "30 minutes"
  stop_conditions:
    - "sent_count >= 1000"
    - "bounce_rate > 0.15"
    - "any consecutive 5 failures"
  schedule:
    cron: "0 8 * * *"
    timezone: "Asia/Singapore"
```

## 6. Key Failure Modes (Documented)

The skill explicitly warns against these 7 failure modes:

| # | Failure Mode | Prevention |
|---|-------------|------------|
| 1 | **No objective gate** | Agent verifies its own work → always needs external signal |
| 2 | **Maker grades own work** | Same agent writes and reviews → split roles |
| 3 | **No persistent state** | Every run starts from scratch → define state file |
| 4 | **Vague stop conditions** | Loop runs forever or stalls → explicit terminal conditions |
| 5 | **No budget cap** | Tokens or API calls burn indefinitely → set budgets |
| 6 | **Judgment work loops** | Subjective tasks can't be objectively gated → reject loop |
| 7 | **Orphaned scheduler** | Cron keeps running after terminal state → cleanup proof |

## 7. CorpusIQ Use Cases

| Cron/Automation | Perfectloop Interview Application |
|-----------------|-----------------------------------|
| **Daily HTML report (6 PM AZ)** | Verify falsifiable: "file exists at path, size > 0, delivered to Telegram" |
| **Skills sweep cron** | Gate: GitHub API returns valid responses; State: last_discovered_id; Budget: max 100 API calls |
| **Video generation pipeline** | Gate: HeyGen returns status="completed"; Stop: max 3 retries per video |
| **Email watchdog** | State: last_polled_email_uid; Gate: SMTP delivery confirmed; Budget: max 10 replies/hour |
| **Community engagement** | Reject outright — "engagement" is not falsifiable. Use observation-only instead. |

## 8. Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Interview rejects the loop | Task is temporal, judgmental, or one-shot | Accept rejection; use a manual prompt or one-shot script instead |
| Loop spec is too conservative | Interview identified too many edge cases | Start with MVP loop (one action, one gate, one state file) |
| State file grows without bound | No cleanup or rotation defined | Add `max_entries` or `ttl_days` to the state spec |
| Gate fails but loop continues | Gate is advisory, not blocking | Make gate blocking: "if gate rejects, stop and escalate" |
| Loop redesign needed | First implementation revealed new constraints | Re-run the interview with new information |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 24 Discovery](/hermes/skills/marketplace/new-june24-2026/) →*
