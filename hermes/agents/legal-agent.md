# Legal & Compliance Agent Configuration

## Role Description

The Legal Agent assists with contract review, regulatory monitoring, policy enforcement, and audit preparation. It works as a first-pass legal operations assistant — flagging contract risks, tracking regulatory changes, monitoring policy compliance, and organizing documentation for audits and due diligence. This agent does not provide legal advice or replace qualified counsel; it accelerates legal workflows by handling the structured, repeatable parts of legal operations so your legal team (or external counsel) can focus on judgment-intensive work.

The agent can review contracts for standard clauses, flag deviations from your playbook, track obligations and renewal dates, monitor regulatory feeds for relevant changes, and answer internal policy questions by searching your compliance documentation. All findings are framed as "flags for attorney review" with source references, never as definitive legal conclusions.

## Recommended Model

**Claude Sonnet 4** or **GPT-4o** — contract review requires careful reading, pattern matching against clause libraries, and the ability to identify deviations from standard language. Both models handle document-length context well. For ongoing monitoring and simple policy Q&A, **Claude Haiku** is sufficient. Always pair with human legal review for any contract or compliance action.

## Key Skills to Load

- `contract-review` — First-pass contract analysis: clause identification, playbook deviation flagging, obligation extraction, renewal tracking
- `regulatory-monitor` — Track regulatory agency updates, proposed rules, enforcement actions by jurisdiction and topic
- `policy-enforcement` — Monitor internal systems for policy violations, flag non-compliant configurations, track remediation
- `audit-prep` — Organize evidence collection, track control testing schedules, generate audit readiness reports
- `document-management` — Contract repository organization, version tracking, expiry and renewal calendar
- `legal-qa` — Search contracts, policies, and regulatory guidance to answer internal legal questions

## MCP Connectors Needed

| Connector | Purpose |
|-----------|---------|
| **Google Drive / OneDrive / Dropbox** | Contract repositories, policy documents, evidence collection |
| **Notion / Airtable** | Contract databases, compliance trackers, audit checklists |
| **Slack** | Compliance alerts, approval notifications, legal team coordination |
| **Email** | Contract review requests, regulatory digest distribution |
| **Monday.com** | Legal project tracking, matter management |

> **Note:** E-signature platforms (DocuSign, HelloSign), CLM systems (Ironclad, LinkSquares), regulatory monitoring APIs, and GRC platforms are accessed via custom skills and API integrations. Configure your legal tech stack in your Hermes profile's `tools` section.

## Sample Cron Schedule

```cron
# Contract renewal check every Monday at 8:00 AM
0 8 * * 1 hermes skill contract-review --renewals --expiring-in 90d

# Regulatory monitoring digest every weekday at 7:00 AM
0 7 * * 1-5 hermes skill regulatory-monitor --jurisdictions config --since 24h

# Policy compliance scan every Wednesday at 2:00 AM
0 2 * * 3 hermes skill policy-enforcement --scan-all

# Monthly audit readiness report on the 1st at 8:00 AM
0 8 1 * * hermes skill audit-prep --framework soc2

# Document expiry check every Friday at 4:00 PM
0 16 * * 5 hermes skill document-management --expiring-in 30d
```

## Quick-Start Command

```bash
hermes agent create legal \
  --model claude-sonnet-4 \
  --skills contract-review,regulatory-monitor,policy-enforcement,audit-prep,document-management,legal-qa \
  --connectors drive,onedrive,notion,slack,gmail,monday \
  --profile legal \
  --description "Legal operations and compliance monitoring agent"
```

## Daily Workflow

Each morning the agent scans regulatory feeds for changes relevant to your jurisdictions and industries, delivering a filtered digest of only what matters — no noise. On Mondays it checks all contracts for upcoming renewals and obligations, flagging anything expiring within 90 days and extracting key terms for review. Weekly it runs compliance scans against your internal policies (data access, security configurations, vendor compliance) and flags deviations. On the 1st of each month, it prepares an audit readiness report organized by control framework (SOC 2, ISO 27001, HIPAA, GDPR as applicable).

## Configuration Notes

Store your contract playbook (acceptable vs. flagged clauses, fallback positions, approval thresholds) in canonical facts. Define your regulatory jurisdictions and topics of interest. Configure your compliance frameworks and control mappings. Set document retention policies. All contract data should be access-controlled — the agent respects the permissions on your connected drives and databases. **Important:** The agent's contract review output must always include a disclaimer that it is not legal advice and requires attorney review.

## Extending

Add `nda-triage` for automated NDA review against standard mutual/one-way templates. Integrate with your CLM for end-to-end contract lifecycle management. Add `litigation-hold` for automated legal hold notifications when relevant triggers fire. Build a `vendor-due-diligence` skill that reviews vendor security documentation against your requirements. Add `ip-portfolio` for patent and trademark deadline tracking.
