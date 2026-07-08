---
title: Incident Response Blueprint for Hermes Agent  --  Automated Detection & Remediation
description: SLA-driven Hermes Agent incident response blueprint. Automated detection, triage, severity scoring, remediation coordination, and postmortem generation. Connects monitoring, communication, and issue tracking with time-gated escalation.
category: blueprints
tags: [hermes-agent, blueprint, incident-response, monitoring, sla, triage, remediation, postmortem, devops]
last_updated: 2026-07-08
---

# Incident Response Blueprint  --  Automated Detection & Remediation

## Incident Lifecycle

```
DETECTION → TRIAGE → REMEDIATION → POSTMORTEM
  (T+0m)     (T+5m)    (T+15m→)     (T+24h→)
```

Each phase has SLAs, automated actions, escalation paths, and human decision gates. The system tracks time-in-phase and escalates when thresholds are breached.

## Architecture Overview

```
┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│Monitoring│  │   Logs   │  │   APM    │  │  Alerts  │
│(PagerDuty│  │(Cloud-   │  │(Datadog, │  │(Email,   │
│ DataDog) │  │ watch)   │  │ NewRelic)│  │ Webhooks)│
└────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘
     │             │             │             │
     └─────────────┴──────┬──────┴─────────────┘
                          │
                ┌─────────▼─────────┐
                │ Incident Engine   │
                │ - Correlation     │
                │ - Severity scoring│
                │ - Runbook matching│
                │ - SLA tracking    │
                └─────────┬─────────┘
                          │
     ┌────────────────────┼────────────────────┐
     │                    │                    │
┌────▼─────┐     ┌───────▼──────┐     ┌───────▼──────┐
│  Slack   │     │Issue Tracker │     │  Knowledge   │
│(War Room)│     │(GitHub, Jira)│     │  Base/Wiki   │
└──────────┘     └──────────────┘     └──────────────┘
```

## Phase 1: Detection (T+0 to T+5 minutes)

**SLA:** Incident detected and acknowledged within 5 minutes.
**Goal:** Reliably detect incidents and suppress noise.

### Step 1: Alert Ingestion

The agent monitors alert sources continuously using a combination of polling and webhook receivers:

| Source | Method | Frequency |
|---|---|---|
| Monitoring webhooks | HTTP endpoint | Real-time (push) |
| Error rate thresholds | Polled metrics | Every 60 seconds |
| Log-based alerts | Polled log queries | Every 120 seconds |
| Synthetic checks | Active probing | Every 60 seconds |
| User-reported issues | Slack bot listener | Real-time (events) |

**Cron:** Continuous  --  use webhook receivers where possible, with `*/1 * * * *` polling fallback.

### Step 2: Noise Suppression and Deduplication

Not every alert is an incident. The agent applies filters:

**Deduplication Rules:**
1. Same alert type + same service + within 5 minutes → group as one incident
2. Alerts from dependencies during their declared maintenance windows → suppress
3. Alerts matching known flaky patterns (fired and self-resolved in < 2 min, 3+ times this week) → flag as "flaky" but don't page

**Correlation Rules:**
When multiple alerts fire simultaneously, correlate them:
1. `ERROR_RATE_SPIKE` + `LATENCY_INCREASE` on the same service → likely related
2. `DATABASE_CONNECTION_ERRORS` across multiple services → upstream database issue
3. `CDN_ERRORS` + `ORIGIN_TIMEOUTS` → likely the origin, not the CDN

### Step 3: Severity Classification

The agent scores each potential incident:

**Severity Levels:**

| Level | Criteria | Response SLA | Notification |
|---|---|---|---|
| SEV1 | Customer-facing outage, data loss, security breach | Acknowledge: 5m, Resolve: 1h | Page on-call + war room |
| SEV2 | Degraded performance, partial feature outage | Acknowledge: 15m, Resolve: 4h | Page on-call |
| SEV3 | Non-critical issue, single user affected | Acknowledge: 1h, Resolve: 24h | Create ticket, notify during business hours |
| SEV4 | Cosmetic, minor, informational | Acknowledge: 4h, Resolve: best effort | Create backlog ticket |

**Severity Scoring Algorithm:**
```
severity_score = (user_impact × 40)     # % of users affected
               + (revenue_impact × 30)  # Estimated $/min impact
               + (data_risk × 20)       # Data loss/exposure potential
               + (time_of_day × 10)     # Peak vs off-peak
```

## Phase 2: Triage (T+5 to T+15 minutes)

**SLA:** Incident triaged and owner assigned within 15 minutes.
**Goal:** Understand what's broken, who needs to fix it, and start the right runbook.

### Step 1: Create Incident Record

The agent creates a structured incident in the issue tracker:

```markdown
# Incident #[AUTO-ID]: [Service]  --  [Brief Description]

**Status:** 🚨 OPEN
**Severity:** [SEV1/SEV2/SEV3/SEV4]
**Detected:** [TIMESTAMP]
**Declared:** [TIMESTAMP]

## Affected Services
- [Service A]  --  [Symptom]
- [Service B]  --  [Symptom]

## Current Impact
- Users affected: [ESTIMATE]
- Revenue impact: [ESTIMATE $/min]
- Geographic regions: [LIST]

## Initial Signals
- [Alert 1]: [Details]
- [Alert 2]: [Details]

## Assigned
- Incident Commander: [AUTO-ASSIGNED FROM ON-CALL SCHEDULE]
- Communications Lead: [AUTO-ASSIGNED]
- Engineering Lead: [AUTO-ASSIGNED FROM SERVICE OWNERSHIP]

## Timeline (auto-updated)
| Time | Event |
|---|---|
| [T+0] | Alert fired |
| [T+2] | Deduplicated and correlated |
| [T+4] | Severity classified as SEV[X] |
| [T+5] | Incident created |
```

### Step 2: On-Call Notification

**For SEV1 and SEV2:**
1. Page the on-call engineer via PagerDuty or equivalent
2. Post to the incidents Slack channel with `@channel`
3. Start a war room thread or Huddle
4. If no acknowledgment within 5 minutes, escalate to secondary on-call
5. If no acknowledgment within 10 minutes, escalate to engineering manager

**For SEV3 and SEV4:**
1. Create a ticket with priority flag
2. Notify the service owner during business hours
3. No paging unless it escalates

### Step 3: Runbook Matching

The agent searches the knowledge base for a runbook matching the incident pattern:

1. Match on: affected service name + alert type + error signature
2. Retrieve the most relevant runbook from the knowledge base (Notion, Confluence, or Git repository)
3. Post the runbook link in the incident channel with the specific steps most likely relevant
4. If no runbook found, post a template: "No runbook found for this pattern  --  here's the generic diagnostic checklist"

**Generic Diagnostic Checklist:**
```
1. Check recent deployments: [link to deploy history for affected service]
2. Check infrastructure changes: [link to Terraform/CF changelog]
3. Check upstream dependencies: [link to dependency status page]
4. Check database performance: [link to DB metrics dashboard]
5. Check error logs: [link to log explorer with relevant time window]
6. Attempt rollback if deployment was within last 30 minutes
```

### Step 4: Status Page Update

Automatically update the public status page:
1. Create an incident with the service name and "Investigating" status
2. Include a non-technical description of user impact
3. Subscribe affected users for updates

## Phase 3: Remediation (T+15 minutes to Resolution)

**SLA:** Varies by severity.
**Goal:** Fix the issue, verify the fix, and communicate throughout.

### During the Incident

The agent provides continuous support during remediation:

**Automated Diagnostics (refresh every 2 minutes):**
- Current error rate and trend (improving or worsening?)
- Recent deployments (any new deploys since the incident started?)
- Infrastructure metrics (CPU, memory, connections  --  any anomalies?)
- Dependency health (are upstream services healthy?)
- User impact trend (more or fewer users affected?)

**Communication Automation:**
- Every 15 minutes: post a status update to the incident channel if no human has
- Every 30 minutes: update the status page with new information
- Auto-detect when incident commander changes and update the incident record
- Log all commands run against production as part of the incident timeline

**Escalation Triggers:**
| Condition | Action |
|---|---|
| SEV1 not resolved in 30 min | Escalate to VP Engineering |
| SEV1 not resolved in 60 min | Escalate to CTO |
| SEV2 not resolved in 2 hours | Escalate to engineering manager |
| Incident commander unresponsive for 15 min | Transfer role to backup |

### Resolution Verification

When the team indicates the fix is deployed:

1. **Verify recovery signals:**
   - Error rate returned to baseline?
   - Latency returned to normal p95?
   - User-facing functionality confirmed working?
   - Synthetic checks passing?

2. **Monitor for 15 minutes post-fix:**
   - No recurrence of the original alert?
   - No new alerts triggered by the fix?
   - All dependent services healthy?

3. **Mark incident as RESOLVED when all checks pass.**

## Phase 4: Postmortem (T+24 hours to T+7 days)

**SLA:** Postmortem published within 5 business days for SEV1, 7 days for SEV2.
**Goal:** Learn from the incident and prevent recurrence.

### Step 1: Timeline Reconstruction

**Cron:** `0 8 * * *`  --  daily check for incidents needing postmortem.

The agent reconstructs the full incident timeline from:
- Alert history
- Chat messages in the war room
- Deployment logs
- Configuration changes
- Monitoring data (metrics, logs, traces)

**Automated Timeline:**
```
[HH:MM] Monitoring detected error rate spike on payment-service
[HH:MM] Alert deduplicated  --  3 related alerts grouped
[HH:MM] Classified as SEV1  --  payment processing affected
[HH:MM] On-call engineer paged (primary: jane-engineer)
[HH:MM] Jane acknowledged page
[HH:MM] War room opened in #incidents
[HH:MM] Runbook "payment-outage" matched and posted
[HH:MM] Rollback of deploy #abc123 initiated
[HH:MM] Error rate began decreasing
[HH:MM] Error rate returned to baseline
[HH:MM] Monitoring period complete  --  incident resolved
```

### Step 2: Postmortem Draft

Generate a postmortem draft following a standard template:

```markdown
# Postmortem: [Incident Title]

**Date:** [DATE]
**Duration:** [START] to [END] ([DURATION])
**Severity:** [SEV1/SEV2]
**Authors:** [INCIDENT COMMANDER], [ENGINEERING LEAD]

## Summary
[2-3 sentences describing what happened and the impact]

## Customer Impact
- [N] users affected for [DURATION]
- [Describe what users experienced]
- Revenue impact: [ESTIMATE]

## Timeline
[Auto-generated timeline from above]

## Root Cause
[What specifically caused the incident  --  the "why"]

## Contributing Factors
- [Factor 1  --  e.g., "no alert on this specific error pattern"]
- [Factor 2  --  e.g., "deploy didn't have automated canary analysis"]

## Detection
- **Time to detect:** [DURATION]  --  [how we found out]
- **Could we have detected it faster?** [Analysis]

## Resolution
- [What fixed it]
- **Time to resolve:** [DURATION]

## Action Items
| # | Action | Owner | Due Date | Priority |
|---|---|---|---|---|
| 1 | [Prevent recurrence] | [Owner] | [Date] | P0 |
| 2 | [Improve detection] | [Owner] | [Date] | P1 |
| 3 | [Process improvement] | [Owner] | [Date] | P2 |

## Lessons Learned
- [What went well]
- [What went poorly]
- [What surprised us]
```

### Step 3: Action Item Tracking

1. Create tickets for each action item in the issue tracker
2. Link them to the postmortem
3. Schedule automated check-ins: 7 days, 14 days, 30 days
4. Escalate overdue action items to the postmortem owner's manager

**Cron:** `0 9 * * 1`  --  weekly action item status sweep.

### Step 4: Postmortem Review

1. Schedule a postmortem review meeting (blameless, 45 minutes)
2. Add to calendar with the incident team
3. After the meeting, update the postmortem with discussion notes
4. Publish to the postmortem archive (searchable, indexed by service and root cause category)

## SLA Dashboard

The agent maintains an incident response dashboard:

| SLA | Target | Current Month | Previous Month |
|---|---|---|---|
| Mean Time to Detect (MTTD) | < 5 min | [X] min | [X] min |
| Mean Time to Acknowledge (MTTA) | < 5 min | [X] min | [X] min |
| Mean Time to Resolve (MTTR) | < 60 min (SEV1) | [X] min | [X] min |
| Postmortem Completion | < 5 days | [X] days avg | [X] days avg |
| Action Item Closure (30 days) | > 90% | [X]% | [X]% |

**Cron:** `0 8 * * 1`  --  weekly SLA dashboard update.

## Full Cron Schedule

| Timing | Phase | Task | Trigger/Frequency |
|---|---|---|---|
| Continuous | Detection | Alert ingestion and correlation | Webhook + `* * * * *` poll |
| T+0 | Detection | Noise suppression and deduplication | On alert |
| T+4min | Detection | Severity classification | Automated |
| T+5min | Triage | Incident record creation | Automated |
| T+5min | Triage | On-call paging (SEV1/2) | Automated |
| T+5min | Triage | Runbook matching and posting | Automated |
| T+15min→ | Remediation | Continuous diagnostics refresh | Every 2 minutes |
| Every 15min | Remediation | Status update posting | Cron |
| Every 30min | Remediation | Status page update | Cron |
| Post-resolution | Remediation | Fix verification and monitoring period | 15 minutes |
| Daily | Postmortem | Check for incidents needing postmortem | `0 8 * * *` |
| Weekly | Postmortem | Action item status sweep | `0 9 * * 1` |
| Weekly | All | SLA dashboard update | `0 8 * * 1` |

## Implementation Notes

### Never Fully Autonomous
The response pipeline automates detection, classification, notification, and information gathering  --  but remediation decisions remain human. The agent's job is to reduce the cognitive load on responders by answering "what's happening right now?" so they can focus on "what do we do about it?"

### Runbook Quality
This blueprint is only as effective as your runbooks. Invest in writing clear, current runbooks for your top failure modes. Review and update them quarterly. The automation can find the runbook  --  it can't fix the issue if the runbook is wrong.

### Testing
Schedule regular incident response drills:
1. Fire a test alert monthly
2. Measure: did the automation detect, classify, notify, and post the runbook correctly?
3. Time the human response separately from the automated response
4. Use drill results to tune thresholds and improve runbooks

### Extending
- Add **deployment rollback automation** for common failure patterns (error rate spike within 5 minutes of deploy → automated rollback)
- Integrate with **feature flags** to automatically disable problematic features
- Connect to **customer communication** tools (Intercom, Zendesk) to notify affected customers proactively
- Add **cost tracking** to incidents  --  compute the estimated cost of each incident for prioritization

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  406+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  406+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
