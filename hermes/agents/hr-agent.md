# HR Agent Configuration

## Role Description

The HR Agent automates recruiting and people operations workflows — resume screening, interview scheduling, onboarding coordination, policy Q&A, and employee data management. It connects to your ATS (Applicant Tracking System), calendar, HRIS, communication tools, and document storage to reduce the administrative burden on your people team. The agent handles the high-volume, repetitive tasks that consume HR bandwidth so your team can focus on culture, employee experience, and strategic workforce planning.

The agent screens inbound resumes against job requirements, drafts candidate summaries, coordinates interview panels across calendars, sends onboarding checklists to new hires, and fields common policy questions from employees. It maintains strict confidentiality — all employee data handling follows access controls defined in your Hermes profile.

## Recommended Model

**Claude Sonnet 4** or **GPT-4o** — resume evaluation requires nuanced understanding of experience, skills, and role fit. Both models handle structured candidate comparison well and can draft professional, warm communications. For policy Q&A and simple scheduling, **Claude Haiku** or **GPT-4o Mini** are cost-effective and fast.

## Key Skills to Load

- `resume-screening` — Parse resumes, score against job requirements, flag top candidates, identify skill gaps
- `interview-scheduling` — Coordinate panel availability across calendars, send invites with context briefs
- `onboarding-coordinator` — New hire checklist tracking, document collection, equipment provisioning status
- `policy-qa` — Answer employee questions by searching your handbook, policies, and past precedent
- `compliance-tracking` — Certification expiry monitoring, training completion tracking, document renewal alerts
- `employee-lifecycle` — Track anniversaries, probation periods, contract renewals; generate reminders

## MCP Connectors Needed

| Connector | Purpose |
|-----------|---------|
| **Calendly / Google Calendar / Outlook** | Interview scheduling, onboarding session booking |
| **Email (Gmail/Outlook)** | Candidate communications, offer letters, policy responses |
| **Slack** | HR channel alerts, onboarding notifications, approval requests |
| **Notion / Airtable** | Employee handbooks, policy docs, onboarding checklists, job descriptions |
| **Google Drive / OneDrive / Dropbox** | Resume storage, offer letter templates, signed documents |
| **HubSpot / Close CRM** | If recruiting pipeline is managed in CRM |

> **Note:** HRIS platforms (BambooHR, Workday, Rippling, Gusto) and ATS systems (Greenhouse, Lever, Ashby) are accessed via API integrations. Configure API keys in your Hermes profile `tools` configuration. Build a connector skill for your specific HR stack.

## Sample Cron Schedule

```cron
# Resume screening every hour during business hours
0 9-17 * * 1-5 hermes skill resume-screening --new-applications --since 1h

# Onboarding progress check every weekday at 10:00 AM
0 10 * * 1-5 hermes skill onboarding-coordinator --active-onboardings --check-progress

# Compliance tracking every Monday at 8:00 AM
0 8 * * 1 hermes skill compliance-tracking --expiring-in 30d

# Employee lifecycle events every Monday at 9:00 AM
0 9 * * 1 hermes skill employee-lifecycle --upcoming 14d

# Policy Q&A response time check every Friday at 4:00 PM
0 16 * * 5 hermes skill policy-qa --unanswered --older-than 24h
```

## Quick-Start Command

```bash
hermes agent create hr \
  --model claude-sonnet-4 \
  --skills resume-screening,interview-scheduling,onboarding-coordinator,policy-qa,compliance-tracking,employee-lifecycle \
  --connectors calendly,gmail,slack,notion,drive \
  --profile hr \
  --description "Recruiting and people operations automation agent"
```

## Daily Workflow

Throughout the day, the agent screens new applications against active job descriptions, ranking candidates and surfacing top matches to the recruiting team with summaries. For candidates advancing to interview stage, it coordinates panel availability and sends calendar invites with interviewer briefs. Every morning it checks onboarding progress for new hires — which documents are outstanding, which setup tasks are incomplete — and nudges responsible parties. On Mondays it scans for expiring certifications, visas, and contract end dates and alerts the appropriate stakeholders.

## Configuration Notes

Store job descriptions, evaluation rubrics, and scoring criteria in canonical facts or a designated Notion database. Define your interview panel configurations (who must attend for each role type). Configure your policy document locations so the Q&A skill can search them. Set data retention policies — the agent should not retain candidate PII beyond your legal retention window. All resume data handling must respect GDPR/CCPA requirements configured in your profile.

## Extending

Add `offer-letter-generation` that drafts offer letters with compensation bands from your canonical facts. Integrate with DocuSign or HelloSign for document execution tracking. Add `culture-survey-analysis` for periodic engagement survey processing. Build a `headcount-planner` that tracks open roles, time-to-fill, and hiring velocity against budget.
