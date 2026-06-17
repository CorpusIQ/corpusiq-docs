# GoHighLevel (LeadConnector)

## What it unlocks
If you run an agency or service business on GoHighLevel, this is where contacts, pipelines, appointments, and payments all converge. Connecting it lets CorpusIQ pull that operational data into the same view as your finance and marketing sources, so you can answer questions about pipeline health, conversation volume, and revenue without leaving one tool.

## Before you connect
- A GoHighLevel sub-account (location) you have admin access to
- About 2 minutes

## How to connect
1. In CorpusIQ, open Settings → Connectors and find GoHighLevel.
2. Click Connect.
3. Follow the standard GoHighLevel OAuth flow when prompted and sign in.
4. <!-- screenshot: GoHighLevel location selection during OAuth -->
5. Pick the sub-account (location) you want CorpusIQ to read and approve access.
6. You'll be returned to CorpusIQ.

You'll see GoHighLevel change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- Location info — name, address, phone, timezone, plan
- Contacts with custom fields and tags, plus search
- Opportunities (pipeline deals)
- Calendars and appointments
- Conversations (SMS, email, calls) and their full message history
- Payment orders
- Forms

CorpusIQ never sends messages, books appointments, or charges customers.

## Questions you can ask
- "How many opportunities are in my pipeline?"
- "Show me appointments booked this week."
- "Find the conversation thread with Jane Doe."
- "List payments collected in the last 30 days."
- "What forms do I have set up?"

## Troubleshooting
- **"Location not authorized"** — During OAuth you may have picked the wrong sub-account. Disconnect and reconnect to choose the right one.
- **No conversations found** — The conversations API requires the `conversations.readonly` scope; reconnect to refresh scopes if you connected before that scope was added.
- **Empty pipeline** — Make sure your opportunities live in the location you authorized, not a sibling sub-account.

<!-- DOC-GAP: No internal SETUP doc exists. Setup steps inferred from registry + vendor public docs. Verify before publish. -->

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
