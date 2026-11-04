---
title: "Connect Google Calendar to Perplexity via MCP"
description: "Connect Google Calendar to Perplexity through CorpusIQ MCP. Ask what is booked, what was agreed and where the week went, read-only, from live calendars."
category: Perplexity Integrations
tags: ["connect Google Calendar to Perplexity", "Google Calendar Perplexity integration", "MCP Calendar connector", "calendar data to Perplexity", "meeting load analysis", "CorpusIQ MCP"]
last_updated: "2026-11-04"
canonical: "https://www.corpusiq.io/docs/connect-google-calendar-to-perplexity"
robots: "index,follow"
---

# How to Connect Google Calendar to Perplexity with CorpusIQ MCP

A calendar is the most honest record of where a week went. Not the plan, not the time sheet, the actual blocks and the people in them.

That record is invisible to an AI tool unless you paste it in. Connecting Google Calendar through CorpusIQ MCP makes it answerable inside a Perplexity thread, read-only.

### Why Connect Google Calendar to Perplexity?

- **Meeting load.** "How many hours of external calls did I have last month, by customer?"
- **Account coverage.** "Which of my top ten accounts have I not spoken to in 45 days?"
- **Thread recall.** "What did we agree in the Acme kickoff, and who was in the room?"
- **Capacity planning.** "Where is the first two-hour block free next week for deep work?"
- **Cost of meetings.** "Total hours in recurring internal meetings this quarter, and who attends them."
- **Read-only by scope.** The connector reads events. It cannot create, move, or delete anything, and it cannot invite anyone.

### How It Works

1. **Connect Google Calendar to CorpusIQ** through Google OAuth and approve the read scopes, Calendar included.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ reads** the events that answer the question, within what the connected account can see.
4. **Perplexity answers** from the retrieved events, naming the meetings it counted.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational query logs are retained for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **Google Calendar** (or the Google Workspace connector, which covers Calendar, Drive, Sheets and Gmail in one authorization).
3. Sign in to Google and approve the read scopes.
4. Copy the MCP endpoint shown under **Settings, Integrations**.

**In Perplexity**

5. Open **Settings** and find the **MCP servers** section.
6. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

7. Connect and approve the CorpusIQ authorization page once.
8. Start a new thread and ask a question about your week or your accounts.

One approval covers future threads. There is no per-question reconnect step.

### Example Perplexity Questions

**Where the time went**

- "How many hours did I spend in meetings last week, split internal and external?"
- "Which recurring meetings take the most total attendee hours this month?"
- "What is my average number of meetings per day this quarter?"

**Customer coverage**

- "Which of my accounts have no meeting in the last 30 days?"
- "When did I last speak to the Acme team, and who joined?"
- "List every meeting with the renewal customer this year."

**Planning**

- "Where is my first free two-hour block on Thursday?"
- "What is on my calendar before the board meeting?"
- "Which days next week have more than four hours of calls?"

**Cross-source**

- "Do the accounts with the most meetings also carry the most open pipeline?" (requires the CRM connector)

### Security

- **Read scope only.** The connection requests Google's read-only calendar scopes. There is no tool that writes an event.
- **Account-scoped.** Access follows the Google account you approve. A calendar that account cannot see stays out of reach.
- **Revocable at any time.** Google Account, Security, Third-party access. Revoking there ends the connection.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Google, CorpusIQ, and Perplexity.

### Comparison: Reading a Calendar Manually vs Calendar in Perplexity

| Aspect | Scrolling the calendar | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | Visual scan, week by week | A question about a period or a person |
| Output | Blocks you count yourself | A computed total with the events named |
| Across people | Ask each person | Asked across the account's visible calendars |
| History | Scroll back and guess | Queried over a range |
| Combining sources | Manual cross-reference | Asked across connectors |
| Write access | Yes, by you | None, read-only scope |

The calendar view answers "what is next". The connector answers "what happened, with whom, and how much".

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity book or move a meeting through this connection?</strong></summary>

No. The connection is read-only. It cannot create, edit, delete, or invite anyone to an event.
</details>

<details>
<summary><strong>Whose calendars can it see?</strong></summary>

The calendars the authorized Google account can already open, including ones shared with it. It does not gain access to anything the account could not see in Google.
</details>

<details>
<summary><strong>Can it answer "what did we agree" from a meeting?</strong></summary>

When the notes or agenda were written into the event, the event record carries them, so a question about what was agreed can be answered from that text. A meeting with no written record has nothing to read.
</details>

<details>
<summary><strong>How far back can I ask?</strong></summary>

Questions are answered over the range you specify, as far back as the calendar still holds. Naming a date range gives the tightest answer.
</details>

<details>
<summary><strong>Is attendee data included?</strong></summary>

Attendee lists are part of the event record and fall under the same read scope as the rest of it. Anything the authorized account can see on the event is in scope.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. Calendar is exposed to ChatGPT, Claude, and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Where is the calendar data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect Google Calendar to Perplexity now](https://corpusiq.io/connect/google-calendar-with-perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
