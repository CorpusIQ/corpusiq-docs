---
title: "Connect Airtable to Claude via MCP - Query Bases"
description: "Connect Airtable to Claude through CorpusIQ MCP. Ask about bases, tables and records in plain English, read-only, with the token scopes that matter."
last_updated: "2026-11-07"
---

# How to Connect Airtable to Claude with CorpusIQ MCP

Airtable holds the work that never reaches a reporting tool: the content calendar, the hiring pipeline, the partnership tracker, the product roadmap. The records stay current because people update them by hand. The answers do not, because nobody exports a base to settle one question.

Connecting Airtable through CorpusIQ MCP puts bases, tables, records, and keyword search in the same conversation as everything else you run the business on. You ask, Claude reads the base as it stands, and the answer names the table and the record it came from.

### Why Connect Airtable to Claude?

- **Pipeline questions.** "Which hiring candidates are sitting at Onsite with no feedback logged?"
- **Calendar questions.** "Which content items are still in Draft two weeks before publish?"
- **Tracker questions.** "How many partnership conversations are waiting on legal?"
- **Record lookup.** "Which roadmap rows belong to the platform team, and what status are they in?"
- **Search by keyword.** "Which records mention this customer by name?"
- **Read-only by token.** The personal access token reads. It cannot create, edit, or delete a record, and it cannot change a base schema.

### How It Works

1. **Create an Airtable personal access token** with the two read scopes and grant it the bases you want visible.
2. **Connect Airtable to CorpusIQ** with that token. Anything the token cannot reach is invisible to the connector.
3. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your account settings.
4. **CorpusIQ reads the base**: base and table listings, records from a table, single records, and keyword searches.
5. **Claude answers** from those records, naming the base and table it read.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In Airtable**

1. Open the **Developer hub**, then **Personal access tokens**, and create a token for this purpose.
2. Add the two read scopes: `data.records:read` and `schema.bases:read`.
3. Under **Access**, add the bases you want answerable. Leave out the bases nobody will ask about.

**In CorpusIQ**

4. Log in and open **Connections**.
5. Select **Airtable** and paste the token.
6. Copy the MCP config block shown under **Settings, Integrations, Claude Desktop**.

**In Claude Desktop**

7. Open **Settings, Developer, Edit Config**. This opens `claude_desktop_config.json`.
8. Add the CorpusIQ entry:

```json
{
  "mcpServers": {
    "corpusiq": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote",
        "https://mcp2.corpusiq.io/mcp"
      ]
    }
  }
}
```

9. Save the file and fully quit Claude Desktop. Not just the window: quit the application.
10. Reopen Claude, complete the device login when prompted, and the tools indicator appears next to the message box.
11. Verify with "list my bases". If the base list is right, the token scope is right.

If the tools indicator does not appear, work through [Claude can't see CorpusIQ](../troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

### Example Claude Questions

**Calendar and content**

- "Which items in the content calendar are still in Draft two weeks before publish?"
- "List every record scheduled for next month, with its owner."
- "Which drafts have no assignee?"

**Hiring and pipeline**

- "Show me every record in the hiring pipeline where stage is Onsite."
- "How many candidates have been waiting more than a week for feedback?"
- "Which open roles have no candidates at all?"

**Partnerships and delivery**

- "How many partnership conversations are waiting on legal?"
- "Pull the roadmap rows owned by the platform team and list their status."
- "Which records mention this customer by name?"

**Cross-source**

- "Which blocked roadmap items belong to accounts with an open support ticket?" (requires the CRM and helpdesk connectors)
- "Do the deals in the tracker match what the CRM shows for the same period?" (requires the CRM connector)

### Security

- **Read-only token.** The connector lists bases, tables, records, and single records, and searches by keyword. It cannot create, edit, or delete a record, and it cannot change a schema.
- **Scoped by base.** The token is granted per base. A base you never granted is a base the connector cannot see, so the token access list is the whole permission model.
- **Revocable immediately.** Delete or edit the token in the Airtable developer hub and access ends at once.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Airtable, CorpusIQ, and Claude.

### Comparison: The Airtable UI vs Airtable Through Claude

| Aspect | Airtable interface | CorpusIQ MCP with Claude |
|---|---|---|
| Input | A view, a filter, a sorted grid | A question, in your own words |
| Output | Rows to scan | A count or a list, with the table named |
| Across bases | Open each base in turn | Asked across the bases you granted |
| Across systems | Export, then reconcile by hand | Asked across connectors |
| New question | Build another view | Ask again |
| Write access | Yes, by you | None, read-only token |

Airtable is the right place to keep the record. Claude is the right place for the question that spans the record and three other systems.

### FAQ: Common Questions

<details>
<summary><strong>Is this read-only?</strong></summary>

Yes. The connector reads bases, tables, records, and keyword search results. It never creates, edits, or deletes a record, and it cannot change a base schema.
</details>

<details>
<summary><strong>How does the connection authenticate?</strong></summary>

With an Airtable personal access token you create, carrying `data.records:read` and `schema.bases:read`, granted to specific bases. Anything the token cannot reach, the connector cannot answer from.
</details>

<details>
<summary><strong>Do I need to share every base?</strong></summary>

No, and you probably should not. Grant the bases a question would actually use. A base you never ask about is one more thing to review later, and removing it is an edit to the token rather than a support request.
</details>

<details>
<summary><strong>Can it answer across Airtable and my other systems?</strong></summary>

Yes, and that is the reason to put a base behind an MCP connector instead of opening a second browser tab. "Which blocked roadmap items belong to accounts with an open ticket" spans Airtable, the CRM, and the helpdesk in one answer.
</details>

<details>
<summary><strong>What about views and filters?</strong></summary>

The connector reads records from a table. Where a base relies on a view to hide archived or test rows, say so in the question, for example "active rows only, not the archive view". A hidden filter becomes a sentence you can see rather than a default you have to remember.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. When you ask, the connector reads Airtable as it stands, so a record edited a minute ago is visible to the next question.
</details>

<details>
<summary><strong>Which bases can Claude see?</strong></summary>

Only the ones you granted to the token. If a base is missing from an answer, check the token's access list before anything else.
</details>

<details>
<summary><strong>Why connect Airtable to Claude at all?</strong></summary>

Because the useful questions are joins. Airtable holds the commitment; the invoice, the ticket, and the campaign hold the consequence. A base answers its own half well, and the join is where the answer usually stops.
</details>

---

**Next steps:** [Connect Airtable to Claude now](https://corpusiq.io/connect/airtable-with-claude)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
