# The 15-Step Execution Loop

## Why most agent workflows fail, and how we prevent it.

The default pattern for autonomous AI agents is execute-and-forget. A cron fires. The agent runs. Output is delivered. Next run starts fresh.

This produces three failure modes:
1. **Duplicates** — no memory of what was already done.
2. **Repeated failures** — same error, same retry, no learning.
3. **Silent degradation** — outputs drift without detection.

Our fix: the execution loop. No execution ends at delivery. Every execution ends at learning. The next run inherits from every prior run.

---

## The 15 Steps

### Step 1: Trigger
Record what started the workflow (cron, user request, event). Log workflow ID, timestamp, source.

### Step 2: Governance Gate
Pass the 7-step gate: classification, registry check, memory policy, ownership, risk review, audit registration, approval.

### Step 3: Preflight
Eight checks: shared memory for bans, knowledge base handoff, audit log for recent failures, memory capacity, state files for dedup, delivery target, duplicate detection.

### Step 4: Context Retrieval
Pull from four memory stores before execution: user preferences, platform restrictions, prior outcomes, workflow state (last success, last failure, learned patterns).

### Step 5: Execution
Execute the workflow using approved tools, APIs, and skills.

### Step 6: Validation
Verify output before delivery. Workflow-specific checks. Examples: video branding visible, post published on platform, email sent successfully. If validation fails: stop. Do not deliver.

### Step 7: Delivery
Deliver validated output to target (email, social, GitHub, file). Verify delivery completed.

### Step 8: Feedback Capture
Capture every outcome. No silent deliveries. Track: approved/rejected, engagement metrics, replies, corrections.

### Step 9: Feedback Classification
Classify: SUCCESS, PARTIAL SUCCESS, or FAILURE. Store reason.

### Step 10: Learning Update
Update knowledge stores with feedback. If same failure occurs 3 times, it becomes a hard rule. If success occurs 3 times, it becomes a preferred method.

### Step 11: Improvement Recommendation
Generate from feedback: what worked, what failed, what should change, what should be tested next.

### Step 12: Apply Improvement
Auto-approved changes apply immediately. User-approval-required changes queue.

### Step 13: Audit Entry
Write structured audit record: timestamp, workflow, trigger, validation, delivery, feedback, classification, learning, improvement.

### Step 14: State Update
Update workflow state: last execution, last success, last failure, learned patterns, preferred methods, improvement queue.

### Step 15: Loop Complete
Return workflow status. The next execution loads this state as context. No fresh starts. Every run inherits from every prior run.

---

## Failure Severity Classification

Not all failures are equal. We classify severity before action:

| Level | Type | Examples | Action |
|:---:|------|----------|--------|
| 1 | Content failure | Weak hook, typo, duplicate theme | Auto-regenerate. No human needed. |
| 2 | Validation failure | URL missing, duration out of range | Auto-regenerate. Max 2 retries. |
| 3 | Pipeline failure | Tool output mismatch, API returns wrong format | Stop. Repair. Validate fix. Return to production. |
| 4 | Governance failure | Unregistered workflow, skipped gate | Escalate immediately. Block all execution. |

---

## Why This Works

The loop transforms agents from fire-and-forget workers into learning systems. After three iterations of any workflow, the system knows what fails, what succeeds, and what to avoid. It stops repeating mistakes because the next run starts with the previous run's knowledge.

This is not prompt engineering. This is operating system design.

---

*Part of the CorpusIQ Agent Operating System documentation.*
