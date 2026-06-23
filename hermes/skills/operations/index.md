---
title: Operations Skills
description: Autonomous operations workflows  --  email automation, cron management, system audits, lead capture, monitoring, governance, and communication discipline. 20+ production skills for running Hermes agents reliably.
---

# Operations Skills

Operations skills handle the infrastructure layer that keeps autonomous agents running reliably. These aren't development or marketing skills  --  they're the operational backbone: email monitoring, cron management, system audits, lead capture, communication protocols, and governance. If marketing skills drive growth and development skills ship code, operations skills ensure nothing silently breaks at 2 AM.

## Email Operations

Email is the primary external interface for most Hermes agents. These skills manage inbound and outbound email at production scale.

**Dual-Account Monitoring**  --  Monitors multiple Gmail inboxes simultaneously (e.g., `team@example.com` and `info@example.com`). Classifies incoming mail by type: lead inquiry, support request, partnership opportunity, newsletter, spam. Routes each to the appropriate response skill. The classification logic runs before any response is composed, so leads don't get auto-replies meant for support tickets.

**OAuth Token Lifecycle**  --  Persistent OAuth token management for Gmail API access. Handles token refresh before expiry, detects revoked tokens, and triggers re-authentication flows. The most common failure mode in email automation is an expired token silently failing  --  this skill checks token validity before every email operation.

**Email Send Checklist**  --  Hard pre-send gate for every outbound email. Before any email leaves the system, it passes through: (1) recipient email validation (no typos in the To field), (2) company name verification (the agent's company name must be correct in every message), (3) phone number policy enforcement (never include phone numbers unless explicitly authorized), and (4) template conformity (matches approved HTML email template). Any check failure blocks the send until resolved.

**Inbound Response Personalization**  --  Before responding to an inbound lead, this skill performs prospect research: checks the sender's domain, identifies their business, scans for recent news or product launches, and incorporates relevant context into the response. The goal is to make every reply feel like it was written by someone who did their homework.

**Professional Email Templates**  --  Maintains and enforces HTML email templates for all outbound communication. Each template category (lead response, partnership outreach, follow-up, introduction) has an approved format. The agent selects the right template, populates it with personalized content, and sends through the verification gate.

## Cron Management

Cron jobs are the heartbeat of autonomous operations. These skills ensure crons actually deliver  --  not just report "ran successfully."

**Cron Delivery Audit**  --  The principle: "scheduled" and "delivered" are different things. This skill audits every cron job by actually executing it once and verifying the output reached its destination. For email crons: check the sent folder. For content crons: check the published URL. For data crons: check the database. The audit produces a report: cron name, last scheduled run, last verified delivery, delivery status, and any failures.

**Cron Operating Manual**  --  Production cron patterns: server-local time management (crons respect the machine's timezone, not UTC), profile-aware scheduling (skills run in the correct Hermes profile), watchdog patterns (a separate cron verifies the primary crons are running), and the deliver-script pattern (crons call scripts that verify output, not fire-and-forget).

**Scheduled Jobs Architecture**  --  When to use Unix cron vs. Hermes built-in scheduling vs. external job queues. Covers the tradeoffs: cron is simple but has no retry logic, Hermes scheduling has context but can't survive server restarts, and job queues (Redis, BullMQ) are resilient but add infrastructure complexity.

## System Audits

Regular system audits catch degradation before it causes visible failures. Automated agents accumulate state  --  stale tokens, full disks, orphaned processes  --  that audits detect and surface.

**System Discovery Audit**  --  Comprehensive environment audit. Scans for: installed tools and their versions, active processes and their resource consumption, disk usage and growth trends, network listeners and their ownership, and cron configurations. The output is a system state snapshot that can be compared across audits to detect drift.

**Six-Category System Audit**  --  Structured audit covering: (1) Connectivity  --  can the agent reach all configured API endpoints? (2) Auth  --  are all tokens valid and not near expiry? (3) Storage  --  disk usage, database size trends. (4) Processes  --  any zombie or runaway processes? (5) Logs  --  any ERROR patterns in the last 24 hours? (6) Deliverables  --  have all scheduled outputs actually appeared? Each category gets a pass/fail and remediation steps for failures.

**Session Database Optimization**  --  Hermes sessions accumulate context. This skill analyzes session size, identifies stale sessions that can be archived, compresses conversation summaries, and reduces context window bloat that slows down agent responses.

## Lead Capture and Management

Autonomous lead capture turns inbound communication into structured pipeline data without human intervention.

**Inbound Lead Capture**  --  Monitors email and messaging channels, identifies leads using domain analysis (checks the sender's business domain to classify by industry and size), enriches with publicly available company data, and routes to the appropriate nurture sequence. Captured leads are logged to CRM or Airtable for pipeline tracking.

**Lead Classification Router**  --  Classifies inbound inquiries by: urgency (time-sensitive vs. informational), business domain (matching against target industries), and intent (purchase signal vs. research vs. partnership). Routes high-urgency purchase signals to immediate response, informational queries to nurture sequences, and partnership inquiries to a separate qualification workflow.

**Autonomous Lead Response**  --  End-to-end pipeline: capture → classify → research → personalize → respond → track. Each stage verifies success before proceeding to the next. If research fails (company data unavailable), the system falls back to a generic-but-professional template rather than stalling.

## Monitoring and Health

**Communication Priority Hierarchy**  --  Establishes monitoring SLAs per channel: business-critical channels (WhatsApp, Telegram) checked every 5 minutes, email checked every 15 minutes, social DMs checked hourly. The agent respects this hierarchy when deciding what to check next.

**Health Monitoring**  --  Checks agent health indicators: API rate limit status, error rate trends, response latency, and task queue depth. Surfaces anomalies before they become outages.

**Done-Only Reporting**  --  The agent's reporting discipline: never report "scheduled," "queued," or "planned"  --  only report work that is actually complete with verifiable output. This eliminates the "I'll do it tomorrow" illusion from agent reports.

## Governance

**System Registry**  --  Tracks every component in the agent ecosystem: skills installed, connectors configured, cron jobs scheduled, and their dependencies. Prevents duplication and surfaces orphaned components.

**Improvement Recommendation Engine**  --  Analyzes operational patterns (failed crons, slow responses, authentication errors) and recommends specific improvements. Each recommendation includes: the pattern observed, the proposed fix, the effort estimate, and the expected reliability improvement.

**Tool Exclusivity Doctrine**  --  Enforces "use X only" policies for critical operations. Some tasks require specific tools (e.g., "send email only through the approved email connector, never through terminal mail commands"). This prevents agents from improvising dangerous shortcuts.

## Installation

Most operations skills are native CorpusIQ skills that load automatically. For marketplace additions:

```bash
npx skills add googleworkspace/cli@gws-workflow-email-to-task
npx skills add googleworkspace/cli@recipe-save-email-attachments
npx skills add wshobson/agents@changelog-automation
npx skills add claude-office-skills/skills@crm-automation
```

## Operating Principles

All operations skills follow three hard rules:

1. **Verify, don't trust.** Cron output is verified by actual execution, not status flags. Email delivery is confirmed in the sent folder, not assumed from API response codes. System health is measured, not estimated.

2. **Fail loudly.** Silent failures compound. If an email cron can't connect, the agent reports the failure with the exact error, not "completed with issues."

3. **Self-heal where possible.** For known failure patterns (expired tokens, full disks, stale processes), the skill includes recovery steps. Don't just detect  --  fix.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
