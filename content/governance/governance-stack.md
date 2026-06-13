# Agent Governance Stack — Production Architecture

## How we run autonomous AI agents that don't drift, repeat, or break in production.

After deploying autonomous agents across multiple workflows (email, social, video generation, growth), the pattern that emerged is a six-layer governance stack. Each layer builds on the previous. Skip one, and the system eventually drifts.

This is not a white paper. This is what we run.

---

## The Six Layers

```
CONSTITUTION → GOVERNANCE GATE → PREFLIGHT → EXECUTION LOOP → DRIFT PROTOCOL → ENFORCEMENT
```

### Layer 0: Constitution

**What it answers:** How does the agent reason?

Before any task, before any cron run, the constitution loads. It is not a ruleset. It is how the agent thinks.

Key principles baked into the constitution:
- Verify, never re-execute. If something was already done, read the evidence — don't run it again.
- Pre-flight gate before any external action. Email, social, video, GitHub — pause and verify format, dedup, delivery target.
- Done means done. If a task exists with status VERIFIED, present the result and stop. Do not re-execute without explicit instruction.
- Blocked means escalate once, log it, move on. Do not retest, re-escalate, or spawn subagents to retry.

The constitution is permanent. It is loaded before every session, every task, every cron run.

### Layer 1: Governance Gate

**What it answers:** Should this thing exist?

Before creating any new workflow, cron, integration, platform, API, agent, or automation:

1. **Classify** the thing (workflow, automation, platform, API, MCP, agent, memory, reporting).
2. **Check registries** — does it already exist? If not, draft a registry entry.
3. **Define memory policy** — what gets stored, where, retention, dedup.
4. **Assign ownership** — which agent owns this workflow?
5. **Risk review** — duplicate? Platform supported? API accessible?
6. **Audit registration** — log the creation.
7. **Approval** — new workflows require approval. Existing workflows proceed.

Rule: reuse before creating. Extend before replacing.

### Layer 2: Preflight

**What it answers:** Is it safe to execute right now?

Eight checks before every execution, every session start, every cron run:

1. Query shared memory for platform bans, token status, recent failures.
2. Check knowledge base handoff from previous session.
3. Read audit log for last 24 hours of failures.
4. Check memory capacity — compact if above 80%.
5. Check workflow state files for dedup.
6. Verify delivery target is reachable.
7. Detect duplicate content.
8. If any check reveals a blocked, banned, or failed condition: stop. Log. Do not retry.

### Layer 3: Execution Loop

**What it answers:** Did it work, and what did we learn?

No execution ends at delivery. Every execution ends at learning. A 15-step loop:

Trigger → Governance Gate → Preflight → Context Retrieval → Execution → Validation → Delivery → Feedback Capture → Feedback Classification → Learning Update → Improvement Recommendation → Apply Improvement → Audit Entry → State Update → Loop Complete.

Critical: the next run must start with knowledge from the previous run. No fresh starts. Every run inherits from every prior run.

### Layer 4: Drift Protocol

**What it answers:** Is the system still aligned?

Daily integrity check comparing:

- Registries against actual system state (any unknown crons? unregistered workflows?)
- Workflow integrity (every active workflow has owner, audit trail, state file)
- Governance integrity (all layers present and identical across worker nodes)
- Memory integrity (any conflicts between memory systems?)
- Worker integrity (all nodes running same governance version)

Scored 0-100. 0 = perfect alignment. Alert if above 20.

### Layer 5: Enforcement

**What it answers:** What happens when something goes wrong?

- Kill switches: automatic workflow pauses based on drift score, failure count, or governance violations.
- Registry enforcement: if a script, cron, workflow, agent, or tool is not in a registry, it does not exist and cannot execute.
- Content quality gate: every public-facing output scored on 8 dimensions. Reject if any dimension below 8 or total below 70.
- Golden dataset: approved examples stored as reference. Every output compared before delivery.

---

## Why This Matters

Most agent systems fail in production because they lack governance. They drift. They repeat. They accumulate unregistered crons and orphaned automations.

The six-layer stack prevents this by design:
- The constitution ensures consistent reasoning.
- The governance gate prevents unregistered sprawl.
- Preflight prevents executing into broken state.
- The execution loop ensures every run learns.
- Drift detection catches misalignment early.
- Enforcement provides automatic circuit breakers.

This is not theory. This is the operating system we run every day.

---

*Part of the CorpusIQ Agent Operating System documentation.*
