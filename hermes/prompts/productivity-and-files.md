# Productivity, inbox, and files

The boring-but-vital one. **Email**, **Calendar**, **Drive/OneDrive/Dropbox**,
**Slack**.

---

### "What urgent emails do I have that I haven't responded to?"

**What this does:** Scans inbox for high-priority threads where you
haven't replied. Looks for payment terms, contract language, legal
notices, renewals, client escalations.
**Connectors used:** Email (Gmail and/or Outlook), Slack (optional).
**Behind the scenes:** `missed-critical-email` skill.
**Sample answer shape:** Thread list with sender, subject, date, and a
flag explaining why it matters.

---

### "Anything important buried in spam or promotions?"

**What this does:** Same as above but explicitly scans low-priority
folders. Catches misclassified critical messages.
**Connectors used:** Email.
**Behind the scenes:** `missed-critical-email`.
**Sample answer shape:** Flagged messages from spam/promotions with
reason.

---

### "What's on my calendar today?"

**What this does:** Today's meetings.
**Connectors used:** Calendar (Google or Outlook).
**Behind the scenes:** `list_my_calendar_events` /
`list_my_outlook_events`.
**Sample answer shape:** Time-ordered meeting list with attendees and
location.

---

### "Find emails from [person] about [topic]."

**What this does:** Inbox search with natural language.
**Connectors used:** Email.
**Behind the scenes:** `search_gmail` / `search_my_outlook_emails`.
**Sample answer shape:** Matching threads with snippets.

---

### "Find my Q3 contract with [vendor] in Drive."

**What this does:** Searches Google Drive (or OneDrive, or Dropbox) for
files matching the query.
**Connectors used:** Drive.
**Behind the scenes:** `search_drive`, `search_my_onedrive`, or
`search_my_dropbox`.
**Sample answer shape:** File list with name, type, last modified, and
the snippet that matched.

---

### "Read me the latest version of the pricing sheet."

**What this does:** Finds the file then reads its content into the
conversation so the assistant can answer follow-ups.
**Connectors used:** Drive.
**Behind the scenes:** `search_drive` → `get_file_content` (or the
OneDrive/Dropbox equivalents).
**Sample answer shape:** A summary of the document, with the assistant
ready to answer follow-up questions about it.

---

### "Read row 2-50 of my KPI tracker spreadsheet."

**What this does:** Reads a specific range from a Google Sheet.
**Connectors used:** Drive.
**Behind the scenes:** `read_sheet`.
**Sample answer shape:** Tabular data from the requested range.

---

### "How busy is my calendar this week?"

**What this does:** Calendar density  --  meeting hours, focus blocks,
overcommitted days.
**Connectors used:** Calendar.
**Behind the scenes:** `list_my_calendar_events` over the week.
**Sample answer shape:** Day-by-day meeting load with totals.

---

### "Summarize my Slack workspace activity."

**What this does:** Top active channels, member count, recent volume.
**Connectors used:** Slack.
**Behind the scenes:** `get_slack_workspace_analytics`.
**Sample answer shape:** Workspace topline plus top channels by
activity.

---

### "Search Slack for messages about [topic]."

**What this does:** Cross-channel message search.
**Connectors used:** Slack.
**Behind the scenes:** `search_slack_messages`.
**Sample answer shape:** Matching messages with channel, user, and
timestamp.

*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts)  --  production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts)  --  production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
