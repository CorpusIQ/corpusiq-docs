# Close

## What it unlocks
Close is where your outbound sales motion lives — leads, opportunities, and the calls and emails that move them forward. Connecting it lets CorpusIQ pull pipeline health, rep activity, and lead details into the conversation, and tie them to email sequences and revenue data from your other connectors.

## Before you connect
- A Close CRM account with admin access to generate API keys
- About 3 minutes

## How to connect
1. In Close, navigate to Settings → API Keys and generate a new API key (or copy an existing one).
2. <!-- screenshot: Close API key generation page -->
3. Open your CorpusIQ dashboard and click Connections.
4. Find Close and click Connect.
5. Paste the API key and save.
<!-- screenshot: CorpusIQ Close API key form -->

You'll see Close change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- Leads with statuses, contacts, and addresses
- Full lead details including custom fields
- Opportunities (pipeline deals) with values, statuses, and expected close dates
- Activities: calls, emails, notes, and meetings with timestamps
- Full-text search across leads, contacts, and opportunities
- Organization users (sales reps) for activity attribution

CorpusIQ never creates leads, moves opportunities, or logs activities.

## Questions you can ask
- "How many leads are in active sequence right now?"
- "Show me opportunities closing this month with value over $10k."
- "What did my team do last week — calls, emails, and meetings?"
- "Search Close for any lead or contact mentioning 'Acme Corp'."
- "Which rep has the most open opportunities?"

## Troubleshooting
- **"API key invalid"** — Confirm the key was generated in Close under Settings → API Keys and hasn't been revoked.
- **"No leads returned"** — Your API key may be scoped to a specific user. Try generating a key with organization-wide access.
- **Search returns unexpected results** — Close search uses its own query language. Try exact phrases or use the full-text search for broader matching.
- **Auth fails after key rotation** — Update the key in your CorpusIQ Connections dashboard.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
