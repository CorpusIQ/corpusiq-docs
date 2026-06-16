# Executive Assistant Agent Configuration

## Role Description

The Executive Assistant Agent is your AI chief of staff — it manages your calendar, prepares you for meetings, triages your inbox, and delivers a structured daily briefing so you start every day with clarity instead of chaos. Designed for founders, executives, and anyone juggling too many priorities, this agent acts as the operational layer between you and the flood of information competing for your attention.

The agent integrates deeply with your calendar, email, task management, and communication tools to provide proactive support. It doesn't just list your meetings — it prepares briefing documents with attendee context, recent history, and open action items. It doesn't just show your inbox — it identifies the 3-5 messages that actually need your attention and drafts responses for the rest. It learns your priorities, your communication patterns, and your working style over time.

## Recommended Model

**Claude Sonnet 4** or **GPT-4o** — executive support requires sophisticated prioritization, contextual understanding, and professional communication drafting. Both models handle the multi-source synthesis this agent performs (calendar + email + tasks + documents). For daily briefings and scheduling, **Claude Haiku** provides fast, cost-effective results.

## Key Skills to Load

- `daily-briefing` — Morning summary: today's meetings, priority emails, pending decisions, key metrics snapshot
- `calendar-manager` — Schedule optimization, conflict resolution, meeting prep doc generation, travel time blocking
- `priority-inbox` — Email triage into "needs action," "needs awareness," and "can wait"; response drafting
- `meeting-prep` — Per-meeting briefs: attendee bios, recent interactions, open items, relevant documents
- `task-followup` — Track action items from meetings and emails, follow up on delegated tasks, flag overdue items
- `weekly-review` — Friday summary: wins, blockers, decisions made, priorities for next week

## MCP Connectors Needed

| Connector | Purpose |
|-----------|---------|
| **Google Calendar / Outlook Calendar** | Schedule management, meeting details, availability |
| **Calendly** | External scheduling links and booking management |
| **Email (Gmail/Outlook)** | Inbox triage, response drafting, thread tracking |
| **Slack** | Message triage, priority notifications, team coordination |
| **Notion / Airtable** | Task tracking, project dashboards, decision logs |
| **Google Drive / OneDrive / Dropbox** | Document access for meeting prep, brief storage |
| **Monday.com** | Project status tracking for stakeholder updates |

## Sample Cron Schedule

```cron
# Daily briefing generation at 6:30 AM
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

## Daily Workflow

At 5:00 AM, the agent optimizes your calendar for the next week — resolving conflicts, blocking focus time, and ensuring travel buffers between off-site meetings. At 6:30 AM, your daily briefing lands in your inbox: today's schedule with one-line context per meeting, the 3-5 emails that need your attention (with suggested responses), pending decisions, and a key metrics snapshot if you've connected business data sources. Before each meeting, the agent prepares a brief covering who's attending, what's been discussed recently, and what open action items exist. Throughout the day it triages your inbox and Slack, surfacing only what needs your direct input. At 4:00 PM it checks on delegated tasks and flags overdue items. Friday at 4:30 PM, you get a weekly review to close the week clean.

## Configuration Notes

Define your priorities, communication preferences, and delegation patterns in canonical facts so the agent learns your style. Configure which senders and topics are high-priority vs. noise. Set your working hours, focus time preferences, and meeting duration defaults. Define what constitutes an "action item" (keywords, formats) for tracking. The agent respects calendar privacy — it only accesses events and emails you've granted permission to.

## Extending

Add `travel-planner` that books flights and hotels within policy. Integrate with your CRM for pre-meeting deal context. Add `stakeholder-update` that drafts board updates, investor communications, and team all-hands summaries. Build a `decision-log` that captures decisions from meetings and tracks their implementation status. Add `relationship-manager` that reminds you to reconnect with key contacts on a cadence.
