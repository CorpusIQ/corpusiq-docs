---
title: Hermes Executive Agent — AI Chief of Staff for Calendar & Inbox
description: Deploy an autonomous executive assistant agent for daily briefings, calendar management, inbox triage, meeting preparation, and task follow-up. Complete Hermes blueprint.
category: Agents
tags:
  - executive-agent
  - calendar-management
  - inbox-triage
  - ai-chief-of-staff
  - daily-briefing
last_updated: 2026-06-16
---

# Hermes Executive Agent — Autonomous Calendar, Inbox & Daily Briefings

The **Hermes Executive Agent** is your **AI chief of staff** — it manages your calendar, prepares meeting briefs, triages your inbox, and delivers a structured **daily briefing** so you start every day with clarity instead of chaos. Designed for founders, executives, and anyone juggling too many priorities.

This agent integrates deeply with your calendar, email, task management, and communication tools through [CorpusIQ MCP connectors](/hermes/mcp/connectors/). It learns your priorities, communication patterns, and working style to provide **proactive, context-rich support**.

## Overview

**The Executive Agent replaces the morning scramble.** Instead of scanning your calendar, digging through email, and reconstructing action items from memory, you receive a 6:30 AM briefing: today's meetings with context, the 3-5 emails that need attention (with suggested responses), pending decisions, and a key metrics snapshot.

| Capability | What It Does |
|-----------|-------------|
| **Daily briefing** | Morning summary: meetings, priority emails, pending decisions, metrics |
| **Calendar management** | Schedule optimization, conflict resolution, meeting prep, travel blocking |
| **Priority inbox** | Email triage into "needs action," "needs awareness," and "can wait" |
| **Meeting preparation** | Per-meeting briefs: attendee bios, recent interactions, open action items |
| **Task follow-up** | Track action items from meetings and emails, flag overdue items |

> **See also:** [Agent Library Overview](/hermes/agents/) · [Sales Agent](/hermes/agents/sales-agent.md) · [HR Agent](/hermes/agents/hr-agent.md)

## How It Works

1. **Connect your personal stack** — Google/Outlook Calendar, Calendly, Gmail/Outlook, Slack, Notion, Drive
2. **Define your priorities** — Store communication preferences and delegation patterns in canonical facts
3. **Load the skills** — Daily briefing, calendar manager, priority inbox, meeting prep, task follow-up
4. **Schedule the crons** — 5 AM calendar optimization, 6:30 AM briefing, 15-min inbox triage
5. **Receive via email and Slack** — Morning briefings, meeting prep docs, task reminders

## Key Features

- **6:30 AM daily briefing** delivered to your inbox — meetings, priority emails, decisions, metrics
- **Calendar optimization** at 5 AM — resolves conflicts, blocks focus time, ensures travel buffers
- **Every-15-minute inbox triage** during business hours with response drafts
- **Pre-meeting briefs** with attendee bios, recent interactions, and open action items
- **4:00 PM task follow-up** checking delegated items and flagging overdue tasks
- **Friday weekly review** — wins, blockers, decisions made, next week's priorities

## Recommended Model

**Claude Sonnet 4** or **GPT-4o** — sophisticated prioritization, contextual understanding, and professional communication drafting. Use **Claude Haiku** for daily briefings and scheduling.

## MCP Connectors Needed

| Connector | Purpose |
|-----------|---------|
| **Google Calendar / Outlook Calendar** | Schedule management, meetings |
| **Calendly** | External scheduling links, booking management |
| **Gmail / Outlook** | Inbox triage, response drafting, thread tracking |
| **Slack** | Message triage, priority notifications, team coordination |
| **Notion / Airtable** | Task tracking, project dashboards, decision logs |
| **Google Drive / OneDrive / Dropbox** | Document access for meeting prep, brief storage |
| **Monday.com** | Project status tracking for stakeholder updates |

## Sample Cron Schedule

```cron
# Daily briefing at 6:30 AM
30 6 * * 1-5 hermes skill daily-briefing --format email --deliver-to user@example.com

# Meeting prep for the day at 6:45 AM
45 6 * * 1-5 hermes skill meeting-prep --today --format brief

# Calendar optimization at 5:00 AM
0 5 * * 1-5 hermes skill calendar-manager --optimize --next 7d

# Priority inbox triage every 15 minutes during business hours
*/15 7-19 * * 1-5 hermes skill priority-inbox --since-last

# Task follow-up every weekday at 4:00 PM
0 16 * * 1-5 hermes skill task-followup --due-today --overdue

# Weekly review every Friday at 4:30 PM
30 16 * * 5 hermes skill weekly-review --format email
```

## Quick-Start Command

```bash
hermes agent create executive \
  --model claude-sonnet-4 \
  --skills daily-briefing,calendar-manager,priority-inbox,meeting-prep,task-followup,weekly-review \
  --connectors google_calendar,calendly,gmail,slack,notion,drive \
  --profile executive \
  --description "Executive assistant for calendar, inbox, and daily briefings"
```

## Configuration Notes

- Define **priorities, communication preferences, and delegation patterns** in canonical facts
- Configure **high-priority senders and topics** vs. noise
- Set **working hours, focus time preferences, and meeting duration defaults**
- Define **action item keywords and formats** for automatic tracking
- The agent respects **calendar and email privacy** — only accesses what you've granted

## Extending

- Add `travel-planner` booking flights and hotels within policy
- Integrate with **CRM for pre-meeting deal context**
- Add `stakeholder-update` drafting board updates, investor communications, and team all-hands
- Build a `decision-log` capturing decisions from meetings with implementation tracking
- Add `relationship-manager` reminding you to reconnect with key contacts on cadence

## FAQ

### What does the Hermes Executive Agent do?

The **Hermes Executive Agent** serves as an AI chief of staff — delivering daily briefings at 6:30 AM, optimizing your calendar, triaging your inbox every 15 minutes, preparing meeting briefs with attendee context, and tracking action items and delegated tasks.

### How does the daily briefing work?

Every weekday at 6:30 AM, the agent compiles and emails: **today's schedule with one-line context per meeting, the 3-5 emails that need your attention (with suggested responses), pending decisions requiring action, and a key metrics snapshot** if business data sources are connected.

### Does the agent prepare me for meetings?

Yes. Before each meeting, the agent prepares a **brief covering who's attending, what's been discussed recently, open action items, and relevant documents** — so you walk in fully prepared without pre-meeting research.

### How does inbox triage work?

Every 15 minutes during business hours, the agent classifies new emails into three buckets: **"needs action"** (drafts suggested responses), **"needs awareness"** (surfaces for reading), and **"can wait"** (files away). Only high-priority items interrupt you.

### Can the executive agent help with weekly reviews?

Yes. Every Friday at 4:30 PM, the agent delivers a **weekly review** covering wins, blockers, decisions made, delegated task status, and priorities for next week — so you close the week clean and start Monday with a clear plan.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What does the Hermes Executive Agent do?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Hermes Executive Agent serves as an AI chief of staff — delivering daily briefings, optimizing your calendar, triaging your inbox, preparing meeting briefs, and tracking action items."
      }
    },
    {
      "@type": "Question",
      "name": "How does the daily briefing work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Every weekday at 6:30 AM, the agent emails today's schedule with context per meeting, the 3-5 priority emails with suggested responses, pending decisions, and a key metrics snapshot."
      }
    },
    {
      "@type": "Question",
      "name": "Does the agent prepare me for meetings?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Before each meeting, the agent prepares a brief with attendee bios, recent discussion history, open action items, and relevant documents."
      }
    },
    {
      "@type": "Question",
      "name": "How does inbox triage work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Every 15 minutes, the agent classifies emails into needs action (with drafts), needs awareness, and can wait — only high-priority items interrupt you."
      }
    },
    {
      "@type": "Question",
      "name": "Can the executive agent help with weekly reviews?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Every Friday at 4:30 PM, the agent delivers a weekly review covering wins, blockers, decisions, delegated task status, and next week's priorities."
      }
    }
  ]
}
</script>

## Related Pages

- [Agent Library — All 9 Role Configurations](/hermes/agents/)
- [HR Agent — Recruiting & People Operations](/hermes/agents/hr-agent.md)
- [Sales Agent — Pipeline & CRM Automation](/hermes/agents/sales-agent.md)
- [CorpusIQ MCP Connectors — 37+ Business Tools](/hermes/mcp/connectors/)
- [Cron Scheduling Guide](/hermes/governance/scheduling/)
- [Model Selection Best Practices](/hermes/best-practices/model-selection.md)


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*
