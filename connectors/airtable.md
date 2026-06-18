# Airtable

## What it unlocks
Airtable is where a lot of operating data lives that never made it into a "real" SaaS tool — content calendars, hiring pipelines, partnership trackers, product roadmaps. Connecting it means CorpusIQ can pull those records into answers alongside your finance, sales, and marketing data, so a question like "what's blocking shipping this month?" can actually see your Airtable backlog.

## Before you connect
- An Airtable account with access to the bases you want CorpusIQ to read
- A personal access token from airtable.com/create/tokens
- About 2 minutes

## How to connect
1. In CorpusIQ, open Settings → Connectors and find Airtable.
2. Click Connect.
3. In a second tab, go to airtable.com/create/tokens and create a personal access token.
4. Give it the scopes `data.records:read` and `schema.bases:read`, and grant access to the specific bases you want CorpusIQ to see.
5. <!-- screenshot: Airtable token scope selection screen -->
6. Copy the token and paste it into the CorpusIQ form, then click Save.

You'll see Airtable change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- The list of bases the token can reach
- Tables inside each base
- Records inside each table
- Search across records by keyword
- A single record by ID

CorpusIQ never writes, edits, or deletes Airtable data.

## Questions you can ask
- "List my bases."
- "Show me every record in the Roadmap base where status is Blocked."
- "Find Airtable records mentioning 'Acme Corp'."
- "What tables are in my Content Calendar base?"
- "Pull record recXYZ from the Hiring base."

## Troubleshooting
- **"Base not found"** — Your token wasn't granted access to that base. Edit the token at airtable.com/create/tokens and add the base.
- **"Insufficient scope"** — Token is missing `data.records:read` or `schema.bases:read`. Recreate with both.
- **Records look stale** — Airtable API returns live data; check whether you're looking at the right view or whether a filter has hidden recent rows.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
