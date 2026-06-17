# Google Workspace (Gmail, Calendar, Drive, Docs, Sheets)

## What it unlocks
Google Workspace is where most founders actually run their day — email, meetings, contracts, KPIs in a spreadsheet. Connecting it gives CorpusIQ read access to all of it in one go, so questions like "what did the agency promise me last month?" or "what's on my calendar before the board meeting?" can pull straight from the original source.

## Before you connect
- A Google account (Workspace or personal Gmail both work)
- About 1 minute

## How to connect
1. In CorpusIQ, open Settings → Connectors and find Google Workspace.
2. Click Connect.
3. Sign in with the Google account you use for work.
4. <!-- screenshot: Google Workspace OAuth consent screen — scope list -->
5. Approve read access for Gmail, Calendar, and Drive when prompted.
6. You'll be redirected back to CorpusIQ.

You'll see Google Workspace change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- **Gmail** — list and search messages, read individual messages
- **Calendar** — list your calendars, list upcoming events, get a specific event, search events by text
- **Drive** — list and search files, read file contents (Docs, PDFs, text), get Drive storage stats
- **Sheets** — read ranges from any spreadsheet you have access to

CorpusIQ never sends mail, creates events, edits files, or shares anything.

## Questions you can ask
- "Find the email thread from the agency about September spend."
- "What's on my calendar for next Tuesday?"
- "Pull the KPI numbers from cell B2:B12 of my Q3 metrics sheet."
- "Find the latest contract draft in my Drive."
- "Summarize today's meetings."

## Troubleshooting
- **"Insufficient permissions"** — Google asks you to approve each scope on a separate checkbox. Reconnect and make sure you tick all of them.
- **Workspace admin blocks the app** — Some Workspace admins restrict third-party apps. Ask your admin to allow CorpusIQ, or sign in with a personal Google account.
- **Sheet read returns empty** — Confirm the spreadsheet ID and the range string (e.g. `Sheet1!A1:C10`). The ID is the long token in the sheet URL.

<!-- DOC-GAP: No internal SETUP doc exists. Setup steps inferred from registry + vendor public docs. Verify before publish. -->

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
