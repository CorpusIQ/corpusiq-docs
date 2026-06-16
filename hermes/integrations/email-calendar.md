# Email + Calendar Integration

Automate meeting scheduling, follow-up workflows, and availability management by connecting email and calendar systems. This blueprint covers Gmail/Outlook with Google Calendar/Outlook Calendar using MCP servers and cron-driven automation.

## Architecture Overview

```
┌──────────┐     ┌──────────────┐     ┌───────────┐
│  Email   │────▶│  Automation  │────▶│ Calendar  │
│  Server  │     │    Layer     │     │  Server   │
└──────────┘     └──────┬───────┘     └───────────┘
                        │
                  ┌─────▼──────┐
                  │  Hermes    │
                  │  Agent     │
                  └────────────┘
```

The automation layer reads incoming emails, extracts scheduling intent or follow-up triggers, and creates or updates calendar events accordingly.

## MCP Server Setup

### Email Servers

**Gmail MCP Server** — provides `list_gmail_messages`, `search_gmail`, and `get_gmail_message` tools. Configure with OAuth credentials from Google Cloud Console with the Gmail readonly scope. This lets the agent scan inboxes for meeting requests, scheduling emails, and follow-up triggers.

**Outlook MCP Server** — provides equivalent tools for Microsoft 365 mailboxes. Requires Azure AD app registration with Mail.Read scope. Supports shared mailboxes, useful for team inboxes like `scheduling@example.com`.

### Calendar Servers

**Google Calendar MCP Server** — provides `list_my_calendar_events`, `search_my_calendar`, and event detail retrieval. Configure with Google Calendar API scope. Supports multiple calendars — separate personal and team calendars.

**Outlook Calendar MCP Server** — provides the same capabilities for Microsoft 365 calendars. Handles delegated calendars and room resource lookups.

## Core Automation Scenarios

### 1. Meeting Scheduling from Email

**Trigger:** New email arrives containing scheduling language ("let's meet", "find time", "schedule a call", Calendly/Doodle link).

**Workflow:**
1. Scan inbox for scheduling-related emails (cron: every 10 minutes)
2. Extract proposed times, duration, and attendees from email body
3. Check availability on target calendar(s) using `list_my_calendar_events`
4. If times are proposed: validate against availability, flag conflicts
5. If no times proposed: find the next 3 open slots based on working hours
6. Draft reply with availability OR confirm the proposed time
7. Mark email with "scheduling-pending" label until confirmed

**Cron expression:** `*/10 * * * *` — checks inbox for new scheduling emails every 10 minutes during business hours.

### 2. Follow-Up Automation

**Trigger:** Email sent to a prospect or client with no reply after N days.

**Workflow:**
1. Monitor sent folder for emails tagged "needs-follow-up"
2. After [N] business days without reply, create a calendar reminder for the sender
3. Draft a gentle follow-up email template personalized with the original thread context
4. If still no reply after [2N] days: escalate to a calendar task with higher priority
5. If [3N] days: move to "cold" status and log for CRM update

**Configuration:** Define follow-up windows per contact category (hot lead: 3 days, warm lead: 5 days, client: 7 days).

**Cron expression:** `0 8 * * 1-5` — runs once each weekday morning to check for follow-up needs.

### 3. Availability Checking

**Trigger:** Someone asks "when are you free?" or a scheduling link is shared.

**Workflow:**
1. Agent reads the email requesting availability
2. Calls `list_my_calendar_events` for the requested date range
3. Identifies open slots based on working hours (configurable: default 9 AM–5 PM, timezone-aware)
4. Respects buffer rules (no back-to-back meetings, minimum 15-minute gaps)
5. Formats availability as a clean bulleted list with timezone notation
6. Optionally generates booking link text for insertion in the reply

**Working hours config:**
```yaml
working_hours:
  monday: "09:00-17:00"
  tuesday: "09:00-17:00"
  wednesday: "09:00-17:00"
  thursday: "09:00-17:00"
  friday: "09:00-15:00"
  timezone: "America/Chicago"
  buffer_minutes: 15
  max_meetings_per_day: 6
```

### 4. Meeting Preparation Briefs

**Trigger:** 30 minutes before a scheduled meeting.

**Workflow:**
1. Agent detects upcoming meeting on calendar (cron: checks every 15 minutes)
2. Searches email for the meeting thread — pulls recent correspondence with attendees
3. Extracts action items, open questions, and decisions from previous meeting notes
4. Compiles a one-page prep brief: agenda, previous context, open items, preparation notes
5. Sends the brief via email or posts to the meeting's Slack channel
6. Includes links to relevant documents and previous meeting summaries

**Cron expression:** `*/15 * * * *` — checks for upcoming meetings every 15 minutes.

## Cron Schedule Summary

| Task | Cron | Description |
|---|---|---|
| Scan for scheduling emails | `*/10 * * * *` | Detect meeting requests in inbox |
| Follow-up check | `0 8 * * 1-5` | Weekday morning follow-up sweep |
| Availability responder | On-demand | Triggered by specific email detection |
| Meeting prep brief | `*/15 * * * *` | Generate prep materials before meetings |
| Daily calendar digest | `0 7 * * *` | Morning email with today's schedule |

## Implementation Notes

### Rate Limiting
Both Gmail and Outlook APIs have rate limits. Implement exponential backoff in your automation scripts. For high-volume inboxes, batch email scanning into a single operation rather than per-message calls.

### Security Considerations
- Use read-only API scopes where possible — the agent should suggest, not autonomously send emails or create calendar events without human review.
- Store OAuth tokens securely; rotate refresh tokens on a schedule.
- Never log email bodies or calendar event details to plaintext files.

### Testing
Start with a "dry run" mode that logs proposed actions without executing them. After a week of dry runs that produce sensible output, enable execution one automation at a time. Monitor the first month closely — edge cases in scheduling language and timezone handling are the most common failure modes.

### Extending
Add CRM integration to log meetings against contacts. Connect Slack to post daily schedule summaries to your direct-message channel. Wire up task management (Notion, Monday, Linear) to create prep tasks for meetings automatically.
