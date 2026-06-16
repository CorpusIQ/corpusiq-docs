# Healthcare: HIPAA-Compliant Agent Workflows

Healthcare operations involve a dense web of scheduling, verification, record management, and privacy compliance. Hermes Agent can automate large portions of this workflow while maintaining the security boundaries HIPAA demands.

## The Healthcare Automation Landscape

A typical medical practice or healthcare provider juggles: patient intake and registration, appointment scheduling and reminders, insurance eligibility verification, prior authorization tracking, lab result notification, and referral management. Each involves checking multiple systems — EHR, practice management software, insurance portals, lab interfaces — and each failure mode means delayed care or denied claims.

Hermes Agent sits between these systems, coordinating data flows that currently require human staff to copy-paste between screens.

## Patient Record Management

The most sensitive domain. Hermes can query EHR systems through database connectors (PostgreSQL, MSSQL) or API-based MCP connectors to:

- Verify patient demographics are complete before appointments
- Flag duplicate patient records for merge review
- Monitor for missing required fields (insurance ID, emergency contact)
- Generate pre-visit summaries for providers

**Pre-Visit Chart Review Cron**

```yaml
- name: pre-visit-chart-review
  schedule: "0 5 * * *"  # Daily at 5 AM
  skill: patient-chart-review
  description: Reviews tomorrow's appointments for chart completeness
```

This skill queries the schedule for the next business day, pulls each patient's chart, and checks: insurance active, recent labs received, referrals attached, demographics current. It produces a per-provider checklist of gaps, delivered to a privacy-compliant Slack channel or secure email.

## Appointment Scheduling Automation

Hermes integrates with calendar systems (Google Calendar, Outlook, Calendly) and can:

- Monitor for cancellations and backfill from waitlists
- Send multi-channel reminders (email, SMS, voice) at configured intervals
- Detect no-shows and trigger follow-up sequences
- Coordinate multi-provider appointments (specialist + lab + imaging)

```yaml
- name: appointment-backfill
  schedule: "*/15 * * * *"  # Every 15 minutes
  skill: schedule-backfill
  description: Fills canceled appointment slots from waitlist
```

The backfill skill queries recent cancellations, matches available slots against a waitlist sorted by urgency and wait time, and proposes fills. With appropriate authorization, it can automatically book standard follow-ups and flag complex cases for staff review.

## Insurance Verification

Insurance eligibility verification is the highest-volume repetitive task in most practices. Hermes can:

1. Query the schedule for upcoming appointments
2. For each patient, check insurance eligibility through available payer portals or clearinghouse APIs
3. Flag patients with inactive coverage, changed plans, or outstanding deductibles
4. Generate pre-visit financial clearance reports

```yaml
- name: insurance-eligibility-check
  schedule: "0 6,14 * * *"  # Twice daily at 6 AM and 2 PM
  skill: insurance-verification
  description: Verifies insurance eligibility for upcoming appointments
```

The skill produces an exception report: patients who need updated insurance information, whose coverage is terminated, or whose plan requires prior authorization for the scheduled procedure. This report routes to the billing team through their existing workflow tool.

## HIPAA Compliance Patterns

Every automation touching PHI must respect HIPAA's Security Rule and Privacy Rule. Key patterns:

**Minimum Necessary Access**
Configure database connector queries with column-level restrictions. Never `SELECT *` — specify only fields the automation genuinely needs. For example, a scheduling skill needs `patient_id, appointment_time, provider_id` but not `diagnosis_codes, notes, medications`.

**Audit Trail**
Every Hermes action that accesses or processes PHI should log to an immutable audit trail:

```yaml
- name: hipaa-audit-log
  schedule: "0 */6 * * *"
  skill: phi-access-audit
  description: Aggregates all PHI access logs and checks for anomalies
```

**Encryption and Access Control**
- Run Hermes on encrypted storage
- Store credentials in a secrets manager, never in skill files
- Use Hermes profiles to isolate healthcare automations from other workloads
- Rotate database credentials on schedule

**Breach Detection**
Monitor for patterns that indicate compromise: unusual query volumes, off-hours PHI access, bulk data exports. Hermes can compare current access patterns against historical baselines and alert on statistical deviations.

## Lab Results Notification

```yarn
- name: lab-result-notifier
  schedule: "0 8,12,16,20 * * *"  # Four times daily
  skill: lab-result-routing
  description: Routes new lab results to appropriate providers with urgency flags
```

This skill queries the lab interface for new results, parses abnormal flags, and either delivers routine results to the patient portal or escalates critical results through on-call notification channels.

## Getting Started in Healthcare

1. **Begin with non-PHI workflows.** Start with appointment reminders or waitlist management before touching clinical data.
2. **Document your data flows.** Every PHI-touching automation needs a documented purpose, data minimization justification, and access control specification.
3. **Use Hermes profiles for segmentation.** Create a dedicated `healthcare` profile with its own credentials and skills, separate from marketing or operations profiles.
4. **Stage automation levels.** Level 1: report-only (Hermes identifies issues, humans act). Level 2: suggest-and-confirm (Hermes proposes actions, humans approve). Level 3: automated with audit (Hermes acts and logs).
5. **Test with synthetic data first.** Before connecting to production EHR databases, validate all skills against synthetic patient records.

The outcome: staff spend less time on administrative verification and more time on patient care, while compliance documentation becomes continuous rather than reactive.
