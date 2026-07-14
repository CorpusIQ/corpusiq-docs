---
title: Hermes HR Agent  --  Recruiting & People Operations Automation
description: Deploy an AI HR agent for resume screening, interview scheduling, onboarding coordination, policy Q&A, and compliance tracking. Complete Hermes configuration blueprint.
category: Agents
tags:
  - hr-agent
  - recruiting-automation
  - people-operations
  - resume-screening
  - ai-hr-assistant
last_updated: 2026-07-08
---

# Hermes HR Agent  --  Autonomous Recruiting & People Operations

The **Hermes HR Agent** automates **recruiting and people operations workflows**  --  resume screening, interview scheduling, onboarding coordination, policy Q&A, and employee data management. It connects to your ATS, calendar, HRIS, and document storage through [CorpusIQ MCP connectors](/hermes/mcp/connectors/) to reduce administrative burden on your people team.

The agent handles high-volume, repetitive HR tasks so your team can focus on culture, employee experience, and strategic workforce planning. All employee data handling follows access controls configured in your Hermes profile.

## Overview

**The HR Agent eliminates manual recruiting busywork.** Instead of reading every resume, coordinating interview panels across calendars, and tracking onboarding checklists manually, your HR team receives ranked candidate summaries, auto-scheduled interviews, and automated onboarding progress checks.

| Capability | What It Does |
|-----------|-------------|
| **Resume screening** | Parses resumes, scores against job requirements, flags top candidates |
| **Interview scheduling** | Coordinates panel availability, sends invites with context briefs |
| **Onboarding coordination** | New hire checklist tracking, document collection, provisioning status |
| **Policy Q&A** | Answers employee questions by searching handbooks, policies, and precedent |
| **Compliance tracking** | Certification expiry, training completion, document renewal alerts |

> **See also:** [Agent Library Overview](/hermes/agents/) · [Executive Agent](/docs/hermes/agents/executive-agent.html) · [Calendar Connector](/hermes/mcp/connectors/)

## How It Works

1. **Connect your HR stack**  --  Calendly, Google/Outlook Calendar, Gmail, Notion, Drive
2. **Store job descriptions and rubrics**  --  In canonical facts or a Notion database
3. **Load the skills**  --  Resume screening, interview scheduling, onboarding, policy QA, compliance
4. **Schedule the crons**  --  Hourly resume screening, daily onboarding checks, weekly compliance
5. **Receive in Slack/Email**  --  Candidate summaries, onboarding status, compliance alerts

## Key Features

- **Hourly resume screening**  --  ranks new applicants against job requirements with scored summaries
- **Panel coordination**  --  checks availability across interviewer calendars and sends invites
- **Onboarding progress tracking**  --  flags outstanding documents, incomplete setup tasks
- **Compliance monitoring**  --  weekly scans for expiring certifications, visas, and contract end dates
- **Employee lifecycle tracking**  --  anniversaries, probation periods, contract renewals
- **Policy Q&A**  --  semantic search across handbooks and policies for employee self-service

## Recommended Model

**Claude Sonnet 4** or **GPT-4o**  --  nuanced resume evaluation and professional communication drafting. Use **Claude Haiku** or **GPT-4o Mini** for policy Q&A and simple scheduling.

## MCP Connectors Needed

| Connector | Purpose |
|-----------|---------|
| **Calendly / Google Calendar / Outlook** | Interview scheduling, onboarding sessions |
| **Gmail / Outlook** | Candidate communications, offer letters, policy responses |
| **Slack** | HR channel alerts, onboarding notifications |
| **Notion / Airtable** | Handbooks, policies, checklists, job descriptions |
| **Google Drive / OneDrive / Dropbox** | Resume storage, templates, signed documents |
| **HubSpot / Close CRM** | If recruiting pipeline managed in CRM |

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

## Configuration Notes

- Store **job descriptions, evaluation rubrics, and scoring criteria** in canonical facts
- Define **interview panel configurations**  --  who must attend per role type
- Configure **policy document locations** for Q&A skill searching
- Set **data retention policies**  --  agent respects GDPR/CCPA requirements
- All resume data handling follows **access controls** configured in your profile

## Extending

- Add `offer-letter-generation` drafting offers with compensation bands
- Integrate with **DocuSign or HelloSign** for document execution tracking
- Add `culture-survey-analysis` for engagement survey processing
- Build a `headcount-planner` tracking open roles, time-to-fill, and hiring velocity

## FAQ

### What does the Hermes HR Agent do?

The **Hermes HR Agent** automates recruiting and people operations: it screens resumes against job requirements, coordinates interview scheduling across panels, tracks onboarding progress, answers policy questions from employees, and monitors compliance deadlines  --  all on scheduled crons.

### How does resume screening work?

The agent **parses incoming resumes**, scores candidates against your job requirements using configurable rubrics, and ranks applicants. **Top matches are surfaced to the recruiting team** with scored summaries highlighting relevant experience, skills, and any identified gaps.

### Can the agent schedule interviews automatically?

Yes. For candidates advancing to interview stage, the agent **checks panel availability across connected calendars** (Google Calendar, Outlook, Calendly), finds open slots, and sends calendar invites with interviewer briefs and candidate context.

### How does the HR agent handle employee data privacy?

The agent **respects all access controls** configured in your Hermes profile. Resume data handling follows GDPR/CCPA requirements. Policy Q&A responses are scoped to the requesting employee's access level. Data retention policies are configurable.

### Can the HR agent track compliance and certifications?

Yes. Weekly scans check for **expiring certifications, visas, contract end dates, and training completions**. Alerts are sent to appropriate stakeholders with 30, 14, and 7-day advance warnings.

## Related Pages

- [Agent Library  --  All 9 Role Configurations](/hermes/agents/)
- [Executive Agent  --  Calendar & Inbox Management](/docs/hermes/agents/executive-agent.html)
- [Legal Agent  --  Compliance & Contract Review](/docs/hermes/agents/legal-agent.html)
- [CorpusIQ MCP Connectors  --  37+ Business Tools](/hermes/mcp/connectors/)
- [Cron Scheduling Guide](/hermes/governance/scheduling/)

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  406+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  406+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
