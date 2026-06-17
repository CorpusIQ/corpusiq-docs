---
title: Daily Operations Blueprint for Hermes Agent — Automate Your Business Day
description: End-to-end Hermes Agent daily operations blueprint. Morning briefing, task triage, midday pulse check, execution monitoring, and evening wrap-up. 12 cron jobs orchestrate a complete business day with human decision gates.
category: blueprints
tags: [hermes-agent, blueprint, daily-operations, morning-briefing, task-triage, cron, workflow-automation]
last_updated: 2026-06-16
---

# Daily Operations Blueprint — Automate Your Business Day with Hermes Agent

## Overview

The Daily Operations blueprint automates the rhythm of a business day. It pulls data from multiple sources (calendar, email, CRM, project management, analytics), synthesizes it into actionable briefings, and tracks execution throughout the day.

```
MORNING                  MIDDAY                EVENING
───────                  ──────                ──────
06:30 Data Collection    12:00 Pulse Check     17:00 Wrap-Up
07:00 Morning Brief      12:30 Midday Update   17:30 EOD Report
08:00 Task Triage        13:00 Reprioritize    18:00 Tomorrow Prep
```

## Full Cron Schedule

| Time | Task | Cron | Description |
|---|---|---|---|
| 06:30 | Data Collection | `30 6 * * 1-5` | Pull fresh data from all connected sources |
| 07:00 | Morning Briefing | `0 7 * * 1-5` | Synthesize data into a daily briefing |
| 08:00 | Task Triage | `0 8 * * 1-5` | Prioritize today's work based on the briefing |
| 08:15 | Calendar Review | `15 8 * * 1-5` | Check today's meetings; flag conflicts or missing prep |
| 09:00 | Standup Summary | `0 9 * * 1-5` | Generate standup update from yesterday's activity |
| 10:00 | Blockers Scan | `0 10 * * 1-5` | Check project management for blocked tasks |
| 12:00 | Midday Pulse | `0 12 * * 1-5` | Check key metrics for anomalies since morning |
| 14:00 | Afternoon Reminder | `0 14 * * 1-5` | Surface tasks still not started |
| 16:00 | Pre-Wrap Collection | `0 16 * * 1-5` | Gather data for end-of-day report |
| 17:00 | Evening Wrap-Up | `0 17 * * 1-5` | Generate end-of-day summary |
| 17:30 | Tomorrow Prep | `30 17 * * 1-5` | Draft tomorrow's priorities and meeting prep |

## Phase 1: Morning Briefing (06:30–08:15)

### Data Collection (06:30)
The agent pulls a snapshot from all connected systems:

**Calendar:** Today's events — title, attendees, time, location, virtual meeting links. Highlight external meetings and any flagged as "needs prep."

**Email:** Unread count, priority senders (configurable VIP list), emails marked urgent. Extract action items from emails received overnight.

**Project Management:** Open tasks assigned to you, sorted by due date. Flag anything due today or overdue. Pull blocked tasks and their blocker descriptions.

**CRM:** Deals closing this week, deals stuck in stage, contacts needing follow-up. If using pipeline management, pull your personal pipeline health metrics.

**Analytics:** Key business metrics compared to yesterday and same-day-last-week. Flag any metric outside normal range.

### Morning Briefing Format (07:00)
The agent compiles the collected data into a structured briefing:

```markdown
# Morning Briefing — [DATE]

## Today's Calendar ([N] events)
| Time | Event | Attendees | Location | Prep Needed? |
|---|---|---|---|---|
| 09:00 | Sprint Planning | Team (6) | Zoom | Review backlog |
| 11:00 | Client Call — Acme | Acme team (3) | Google Meet | YES — see prep section |
| 14:00 | 1:1 with [Manager] | 2 | In-person | Bring project status |

## Priority Inbox ([N] unread, [N] flagged)
- 🔴 [Sender]: [Subject] — [one-line summary]
- 🟡 [Sender]: [Subject] — [one-line summary]

## Tasks at Risk
- ⚠️ [Task] — Due today, not started
- ⚠️ [Task] — Due yesterday, in progress

## Key Metrics
| Metric | Today | Yesterday | Change | Status |
|---|---|---|---|---|
| Revenue | $XX,XXX | $XX,XXX | +2.1% | 🟢 |
| New Signups | XXX | XXX | -5.3% | 🟡 |
| Support Tickets | XX | XX | +40% | 🔴 |

## Recommended Focus Today
1. [Highest priority item with rationale]
2. [Second priority]
3. [Third priority]
```

### Task Triage (08:00)
Based on the briefing, the agent:
1. Suggests a priority order for today's tasks
2. Identifies what can be deferred or delegated
3. Flags meetings that could be declined or shortened
4. Generates time blocks on the calendar for focused work periods
5. Creates prep notes for meetings flagged as needing preparation

## Phase 2: Execution Monitoring (09:00–16:00)

### Standup Summary (09:00)
If the team does standups, generate a structured update:
```
Yesterday: [1-2 accomplished items]
Today: [1-2 planned items]  
Blockers: [0-1 items]
```

### Blockers Scan (10:00)
Query project management for tasks blocked by you or for you. If you're the blocker, surface it immediately. If you're blocked, check if the blocker has been resolved overnight.

### Midday Pulse (12:00)
Lightweight re-check of the morning's key metrics. Answer: has anything materially changed since 7 AM? If yes, flag it. This prevents end-of-day surprises.

### Afternoon Reminder (14:00)
Surface the most important task from the morning briefing that still hasn't been started or completed. Gentle nudge format — the tone should help, not nag.

## Phase 3: Evening Wrap-Up (16:00–17:30)

### Pre-Wrap Collection (16:00)
Gather data for the end-of-day report:
- What was completed today (from project management)
- What was deferred (tasks moved to tomorrow or later)
- What new tasks emerged during the day
- Meeting outcomes and action items from calendar events
- End-of-day metric values for the morning metrics

### Evening Wrap-Up Report (17:00)
```markdown
# End of Day — [DATE]

## Completed Today
- ✅ [Item 1]
- ✅ [Item 2]
- ✅ [Item 3]

## Deferred to Tomorrow
- 🔄 [Item 1] — reason: [blocked / reprioritized / capacity]
- 🔄 [Item 2] — reason: [needs more info]

## New Items Added Today
- 🆕 [Item 1] — source: [meeting / email / Slack]

## Meeting Outcomes
| Meeting | Key Decision | Action Items |
|---|---|---|

## Metric Close
| Metric | Open | Close | Day Change |
|---|---|---|---|

## Tomorrow's Draft Plan
1. [Top priority for tomorrow]
2. [Second priority]
3. [Third priority]
```

### Tomorrow Prep (17:30)
- Draft tomorrow's priority list based on today's deferred items and calendar
- Identify meetings that need preparation
- Flag any early-morning deadlines
- Save the draft — the morning briefing will refine it with overnight data

## Configuration

### Working Hours
```yaml
working_hours:
  days: [1, 2, 3, 4, 5]  # Monday-Friday
  start: "09:00"
  end: "17:00"
  timezone: "America/Chicago"
```

### Priority Senders
```yaml
priority_senders:
  - "ceo@example.com"
  - "key_client@example.com"
  - "investor@example.com"
```

### Key Daily Metrics
Define which metrics to track morning and evening. These can come from database queries, analytics platforms, or CRM:
```yaml
daily_metrics:
  - name: "Revenue"
    source: "database"
    query: "select sum(amount) from orders where created_at::date = current_date"
  - name: "New Signups"
    source: "analytics"
    metric: "signups"
  - name: "Support Tickets"
    source: "crm"
    query: "support_tickets_created_today"
```

## Implementation Notes

### Resilience
- If a data source is unavailable (API down, credential expired), the briefing should still generate with "N/A" for that source and a clear warning
- Never let one failed data pull block the entire briefing

### Personalization
- Tune the morning briefing format over the first two weeks — remove sections you never read, add data you find yourself looking up manually
- Adjust the priority-senders list based on whose emails actually require same-day response
- The task triage suggestions will improve as the agent learns which types of tasks you typically defer vs tackle

### Extending
- Add a **weekly review** on Friday afternoons that aggregates the week's daily reports
- Connect to Slack for a "good morning" DM with the briefing instead of email
- Integrate a **commute briefing** — a voice-readable summary for the drive/walk to work

## FAQ

### How does the Daily Operations blueprint handle data source failures?
If a data source is unavailable (API down, credential expired), the briefing still generates with "N/A" for that source and a clear warning. One failed data pull never blocks the entire briefing — resilience is built into every stage.

### Can I customize the Daily Operations blueprint schedule?
Yes. Adjust all cron times to match your working hours and timezone. The blueprint is designed to be customized — change the morning briefing time from 7:00 AM to whenever your day starts, add or remove check-ins, and tune notification channels.

### How do I extend the Daily Operations blueprint?
Add a weekly review on Friday afternoons that aggregates the week's reports, connect to Slack for DM briefings instead of email, or integrate a commute briefing for voice-readable summaries. The pattern of data-collection → computation → action extends naturally.

## Related Pages

- [Automation Blueprints Overview](/hermes/blueprints/) — All workflow templates
- [Customer Lifecycle Blueprint](customer-lifecycle.md) — Feeds customer health into morning briefings
- [Cron Design Best Practices](/hermes/best-practices/cron-design.md) — Reliable scheduling patterns
- [Integration Examples](/hermes/integrations/) — Connect the tools this blueprint needs

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How does the Daily Operations blueprint handle data source failures?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "If a data source is unavailable, the briefing still generates with N/A for that source and a clear warning. One failed data pull never blocks the entire briefing — resilience is built into every Hermes Agent blueprint stage."
      }
    },
    {
      "@type": "Question",
      "name": "Can I customize the Daily Operations blueprint schedule?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Adjust all cron times to match your working hours and timezone. Change the morning briefing from 7:00 AM to whenever your day starts, add or remove check-ins, and tune notification channels to your preferred platforms."
      }
    }
  ]
}
</script>


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
