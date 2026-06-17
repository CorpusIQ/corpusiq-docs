# Notion

## What it unlocks
Notion holds a surprising amount of business data that lives outside your SaaS tools — project plans, meeting notes, hiring trackers, product specs. Connecting it lets CorpusIQ search across your workspace, query databases, and read pages, so questions like "what's the status on the Q2 launch plan?" get real answers from your actual Notion docs.

## Before you connect
- A Notion workspace where you can create internal integrations
- A Notion Internal Integration Token with read access
- About 5 minutes (includes granting page access to the integration)

## How to connect
1. Go to [notion.so/my-integrations](https://www.notion.so/my-integrations) and click **New integration**.
2. Name it something recognizable (e.g. `CorpusIQ read-only`) and select the workspace you want to connect.
3. <!-- screenshot: Notion integration creation screen -->
4. Copy the Internal Integration Token — Notion shows it once.
5. For each database or page you want CorpusIQ to read, open it in Notion, click the ••• menu, go to Connections, and add your new integration.
6. <!-- screenshot: Notion connections menu -->
7. Open your CorpusIQ dashboard and click Connections.
8. Find Notion and click Connect.
9. Paste the Internal Integration Token and save.
<!-- screenshot: CorpusIQ Notion token form -->

You'll see Notion change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
- The bot user associated with your integration
- Workspace users visible to the integration
- Databases the integration has been granted access to, with full schemas
- Database rows (pages) with their properties
- Page content: block trees including paragraphs, headings, lists, and to-dos
- Full-text search across pages and databases the integration can access

CorpusIQ never creates pages, edits content, or modifies databases.

## Questions you can ask
- "Search my Notion workspace for 'Q2 launch plan'."
- "List all databases my Notion integration can access."
- "What's in the Engineering Projects database?"
- "Show me the content of the weekly standup notes page."
- "Who are the users in my Notion workspace?"

## Troubleshooting
- **"No databases found"** — Your integration token hasn't been granted access to any databases yet. Open each database, go to ••• → Connections, and add the integration.
- **"Page not found"** — Same issue: the integration needs explicit access to each page. You must invite it via the Connections menu on every page or database individually.
- **"Integration token invalid"** — The token may have been regenerated. Create a new integration at notion.so/my-integrations and update the token in CorpusIQ.
- **Block content looks incomplete** — Notion paginates block children. Large pages will return content in pages; CorpusIQ handles pagination automatically, but very large documents may need multiple calls.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
