---
title: apple-calendar — Setup Guide
description: Apple Calendar integration for Hermes agents. Create, read, update, and delete calendar events via CalDAV. Manage schedules, set reminders, and coordinate meetings autonomously.
---

# apple-calendar — Setup Guide

## Prerequisites
- **macOS** with Calendar app configured (iCloud, Exchange, or Google)
- **Hermes Agent** installed
- **CalDAV access** enabled on your calendar account
- **Node.js 18+** with `npx` available

## Capabilities

| Capability | Description |
|-----------|-------------|
| **CRUD Events** | Create, read, update, delete calendar events |
| **Reminders & Alerts** | Set time-based and location-based alerts |
| **Availability Query** | Find open time slots across multiple calendars |
| **Multi-Calendar Support** | iCloud, Exchange, Google (via CalDAV), local |
| **Natural Language** | "Schedule a meeting tomorrow at 2pm for 1 hour" |
| **Recurring Events** | Daily, weekly, monthly, custom recurrence rules |

## Installation

```bash
npx skills add sundial-org/awesome-openclaw-skills/apple-calendar
```

## Configuration

Grant Calendar access in macOS:

```bash
# System Settings → Privacy & Security → Calendars → Terminal / Hermes
```

Or via command line (requires admin):

```bash
# Add Hermes to calendar access
sudo sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
  "INSERT OR REPLACE INTO access VALUES('kTCCServiceCalendar','com.hermes.agent',0,2,2,1,NULL,NULL,NULL,'UNUSED',NULL,0,0);"
```

Configure in `~/.hermes/config.yaml`:

```yaml
skills:
  apple-calendar:
    default_calendar: "Work"        # Default calendar name
    default_duration_minutes: 60    # Default meeting duration
    default_alert_minutes: 15       # Default reminder before event
    working_hours:
      start: "09:00"
      end: "17:00"
      timezone: "America/Phoenix"
      days: [1, 2, 3, 4, 5]        # Mon-Fri
    read_only_calendars:
      - "Holidays"
      - "Birthdays"
```

## Usage Examples

### Create Events

```
Create a calendar event "CorpusIQ Sprint Review" tomorrow at 3pm for 45 minutes
Schedule "Team Standup" every weekday at 9:30am starting next Monday
Add "Content Calendar Review" to my Work calendar Friday 2pm with a 10-minute reminder
```

### Query Availability

```
What's on my calendar tomorrow?
Find a 30-minute slot this week for a meeting with 3 attendees
Check my availability Thursday afternoon
```

### Manage Events

```
Reschedule tomorrow's "Sprint Review" to Friday at 11am
Cancel the "Coffee Chat" on Thursday
Add "Prep slides" as a reminder for my Monday presentation at 8am
```

## How It Works

```
┌──────────┐     ┌──────────────┐     ┌──────────────┐
│  Hermes   │────▶│  apple-      │────▶│  macOS        │
│  Agent    │     │  calendar    │     │  Calendar     │
└──────────┘     │  skill        │     │  (CalDAV)     │
                 └──────────────┘     └──────────────┘
                        │                      │
                        ▼                      ▼
                 ┌──────────────┐     ┌──────────────┐
                 │  Natural Lang │     │  iCloud /     │
                 │  → CalDAV API │     │  Exchange /   │
                 └──────────────┘     │  Google       │
                                      └──────────────┘
```

The skill uses CalDAV (the standard calendar protocol) to communicate with macOS Calendar. This provides a uniform interface regardless of which backend you use (iCloud, Exchange, Google).

## CorpusIQ Use Cases

1. **Content Calendar Management:** Schedule social posts, blog publications, and video releases directly from Hermes. "Schedule the UGC video #47 for Thursday at 6pm"

2. **Meeting Coordination:** Hermes can find mutually available slots for team meetings across multiple calendars.

3. **Deadline Tracking:** Set reminders for product milestones, launch dates, and customer deliverables. "Set a reminder for 'CorpusIQ v2 launch' on August 1st with 1-week and 1-day alerts"

4. **Daily Standup Automation:** Automatically schedule daily standups that respect working hours and existing commitments.

5. **Client Follow-up Calendar:** Create calendar events for follow-up tasks based on email conversations.

## Limitations

- **macOS Only:** This skill uses CalDAV via macOS — not available on Linux or Windows.
- **Calendar Permissions:** macOS privacy settings may require manual approval on first use.
- **Read-Only External:** Some shared calendars may be read-only depending on permissions.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| "Calendar access denied" | macOS privacy permissions | Grant access in System Settings → Privacy → Calendars |
| "Calendar not found" | Calendar name mismatch | List calendars: `hermes calendar list` |
| Events not syncing | CalDAV sync delay | Wait 30-60 seconds; check internet connection |
| "Invalid recurrence rule" | Complex custom rule syntax | Use simple recurrence patterns (daily/weekly/monthly) |
| Working hours not respected | Timezone mismatch in config | Verify `timezone` matches `systemsetup -gettimezone` |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
*↑ [Skills Home](/hermes/skills/)*

---

*Curated by CorpusIQ — one MCP endpoint, all your business tools.*
