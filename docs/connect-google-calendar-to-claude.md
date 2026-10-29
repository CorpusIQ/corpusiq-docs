---
title: "Connect Google Calendar to Claude via MCP - Read Your Week"
description: "Connect Google Calendar to Claude through CorpusIQ MCP. Ask what is booked, where the hours go, and what was agreed, read-only from your live calendars."
category: Claude Integrations
tags: ["connect Google Calendar to Claude", "Google Calendar Claude integration", "MCP Calendar connector", "calendar data to Claude", "meeting load analysis", "CorpusIQ MCP"]
last_updated: "2026-10-29"
canonical: "https://www.corpusiq.io/docs/connect-google-calendar-to-claude"
robots: "index,follow"
---

# How to Connect Google Calendar to Claude with CorpusIQ MCP

A calendar is a record of where the company spent its most expensive resource, and almost nobody reads it that way. It answers questions the calendar app never asks: how much of the week went to internal meetings, which customer keeps coming back, what got booked after the last contract call.

Connecting Google Calendar through CorpusIQ MCP turns that record into something you can question in plain language.

### Why Connect Google Calendar to Claude?

- **Time allocation.** "How many hours went to internal meetings versus customer meetings last month?"
- **Meeting load.** "Who on the team has more than 20 hours of meetings a week?"
- **Customer history.** "When did we last meet this account, and who attended?"
- **Booking sprawl.** "Which recurring meetings have no agenda and have not changed in a quarter?"
- **Cross-source timing.** "For meetings with accounts that have open deals, what was discussed?" (with notes or CRM connected)
- **Read-only by scope.** The connection reads calendar events. It cannot create, move, or cancel anything.

### How It Works

1. **Connect Google Calendar to CorpusIQ** through Google OAuth and approve the read-only calendar scopes.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ translates** the question into calendar queries, retrieves the matching events, and returns titles, times, attendees, and descriptions.
4. **Claude answers** from that retrieved content, with the events it used.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **Google Calendar** (or the Google Workspace connector to include Drive, Sheets, and Gmail).
3. Sign in to Google and approve the read-only scopes.
4. Copy the MCP config block shown under **Settings, Integrations, Claude Desktop**.

**In Claude Desktop**

5. Open **Settings, Developer, Edit Config**. This opens `claude_desktop_config.json`.
6. Add the CorpusIQ entry:

```json
{
  "mcpServers": {
    "corpusiq": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote",
        "https://www.corpusiq.io/mcp/direct-connection"
      ]
    }
  }
}
```

7. Save the file and fully quit Claude Desktop. Not just the window: quit the application.
8. Reopen Claude, complete the device login when prompted, and the tools indicator appears next to the message box.

If the tools indicator does not appear, work through [Claude can't see CorpusIQ](troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

### Example Claude Questions

**Where the time went**

- "How many hours went to internal meetings versus customer meetings last month?"
- "Which meetings took more than 90 minutes, and who organised them?"
- "Show the weekly meeting load for each person on the revenue team."

**Customer contact**

- "When did we last meet this account, and who was in the room?"
- "How many times have we met a customer in the last 30 days?"
- "Which accounts have had no meeting since the deal closed?"

**Meeting hygiene**

- "Which recurring meetings have no agenda attached?"
- "List meetings this week with no description and more than six attendees."
- "Which series has run unchanged for more than a quarter?"

**Cross-source**

- "For meetings with accounts that have open invoices, what was discussed?" (requires billing and notes sources)
- "Did the quarterly review for this customer happen before or after the renewal date in the CRM?" (requires the CRM connector)

### Security

- **Read scope only.** The connection requests Google's read-only calendar scopes. Claude cannot create, move, or cancel an event.
- **Account-scoped.** Access follows the Google account you approve. Calendars that account cannot see stay out of reach.
- **Revocable at any time.** Google Account, Security, Third-party access. Revoking there ends the connection.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Google, CorpusIQ, and Claude.

### Comparison: Calendar App vs Calendar Through Claude

| Aspect | The calendar app | CorpusIQ MCP with Claude |
|---|---|---|
| Input | Scrolling days and weeks | A question about a period |
| Output | Events in a grid | An answer with totals and the events used |
| History | You page back | Asked across a quarter or a year |
| Attendees | You open each event | Aggregated per person or account |
| Cross-source | Manual cross-check | Asked across connectors |
| Write access | Yes, by you | None, read-only scope |

The calendar app is the right tool when you need to book something. Claude is the right tool when you need to know what the bookings cost you.

### FAQ: Common Questions

<details>
<summary><strong>Can Claude create or cancel meetings through this connection?</strong></summary>

No. The connection is read-only. Claude lists and reads events. Creating, moving, inviting, and cancelling are not available, and no write scope is requested.
</details>

<details>
<summary><strong>Whose calendars can it read?</strong></summary>

The calendars the connected Google account can already see, including calendars shared with it. Each account is authorized independently, so a work and a personal calendar can be connected without sharing a login, and you can connect only the account a question needs.
</details>

<details>
<summary><strong>Can it see meeting notes or recordings?</strong></summary>

It reads what the event carries: title, time, attendees, description, and location. Notes stored in another system come from that system's connector, and recordings are not part of this connector.
</details>

<details>
<summary><strong>Does it work with Microsoft 365 calendars?</strong></summary>

This page covers Google Calendar. Microsoft 365 and Outlook calendars are a separate connector with their own authorization.
</details>

<details>
<summary><strong>How far back can it go?</strong></summary>

As far back as the connected calendars hold events. Ask for the period explicitly: "last quarter", "the last 90 days", or a date range, so the query stays tight and the answer stays fast.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. Events are read at the moment you ask, so a meeting booked an hour ago is visible to the next question.
</details>

<details>
<summary><strong>Where is my calendar data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Retrieval happens on demand. Operational logs may persist for up to 30 days. See the [security documentation](../security/) for detail.
</details>

---

**Next steps:** [Connect Google Calendar to Claude now](https://corpusiq.io/connect/google-calendar-with-claude)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
