---
title: "Connect Google Search Console to Claude via MCP"
description: "Connect Google Search Console to Claude through CorpusIQ MCP. Ask about queries, pages, clicks and position, and get cited answers from live search data."
category: Claude Integrations
tags: ["connect Google Search Console to Claude", "Search Console Claude integration", "MCP Search Console connector", "GSC data to Claude", "SEO data in Claude", "CorpusIQ MCP"]
last_updated: "2026-11-01"
canonical: https://www.corpusiq.io/docs/connect-google-search-console-to-claude
robots: index,follow
---

# How to Connect Google Search Console to Claude with CorpusIQ MCP

Search Console holds the answer to one narrow question: which pages and queries earned visibility, and how that changed. Reading it means opening the property, choosing a date range, switching dimensions, exporting a table, then rebuilding the same view next month. Connecting Search Console to Claude through CorpusIQ MCP replaces that loop. You authorize read-only access once, ask in plain English, and get an answer with the numbers and the source attached.

Direct MCP retrieval is read-only and does not retain raw customer files or full connector response payloads. Operational query logs are retained for up to 30 days.

## What Questions Can You Ask?

- "Which pages lost the most clicks month over month?"
- "What queries have impressions but a position worse than 20?"
- "Show me the top 10 queries for /pricing over the last 90 days."
- "Compare mobile and desktop CTR for the same pages."
- "Which countries drove the most impressions last quarter?"

The point is not a prettier report. It is a question you could not answer before without exporting three tables and joining them by hand.

## Why Connect Search Console to Claude?

Search Console is the only place that records what people typed before they reached your site. Analytics tells you what happened after the click. Search Console tells you what earned the click.

The interface was built for inspection, one dimension at a time. Claude turns it into a conversation, so the follow-up question costs nothing:

- **Query decay, caught early.** "Which pages lost the most clicks versus last month?" surfaces a drop while it is still fixable.
- **Striking distance, ranked.** "What queries sit between position 8 and 20 with rising impressions?" turns a fuzzy content backlog into an ordered list.
- **Page-level diagnosis.** "For /pricing, show queries, average position, and CTR, and compare to the previous quarter."
- **Segment comparison.** Mobile against desktop, one country against another, branded against non-branded, all from one question.
- **Cross-source answers.** Query data from Search Console next to sessions and conversions in Google Analytics, or spend in Google Ads, in a single response.

## How the Integration Works

1. **Connect Google.** Search Console is part of the Google connector in CorpusIQ, alongside Gmail, Calendar, Drive, Sheets, Google Analytics, and Google Ads. One authorization covers them.
2. **Grant read access.** You approve the Search Console read scope for the properties you own.
3. **Add CorpusIQ to Claude.** Register the CorpusIQ MCP server as a custom connector. See the [Quick Start guide](quick-start.md).
4. **Ask.** Claude picks the Search Console tools when a question needs search data, and states the property, the date range, and the dimensions it used.

Read-only is enforced by scope, not by policy. Nothing in the retrieval path can submit a sitemap, request indexing, or change a property setting.

## Setup Steps

1. **Sign up** at [corpusiq.io](https://www.corpusiq.io). The 30-day trial needs no credit card.
2. **Open Connectors** in your CorpusIQ dashboard and select **Google**.
3. **Sign in** with the Google account that is a verified owner of the Search Console property. Approve read access.
4. **Copy the MCP config block** shown under **Settings, Integrations, Claude Desktop**.
5. **Open Claude Desktop**, then **Settings, Developer, Edit Config**. This opens `claude_desktop_config.json`.
6. **Add the CorpusIQ entry:**

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

7. **Save the file and fully quit Claude Desktop.** Not just the window: quit the application.
8. **Reopen Claude** and complete the device login when prompted. The tools indicator appears next to the message box.
9. **Verify the data.** Ask "How many clicks did the site get last month?" and check the answer against the Search Console interface.

If the tools indicator does not appear, work through [Claude can't see CorpusIQ](troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

**Next step:** [Connect Google Search Console to Claude](https://corpusiq.io/connect/google-search-console-with-claude).

## Example Claude Queries

**Performance review:**
- "What were total clicks and impressions for the last 28 days, and how does that compare to the 28 days before?"
- "Which five pages earned the most clicks last quarter?"
- "Show me the average position trend for our top 20 queries."

**Content and SEO work:**
- "Which queries sit between position 8 and 20 with more than 1,000 impressions?"
- "Which blog posts lost impressions week over week?"
- "Show me queries where CTR is below 1 percent but the average position is better than 10."

**Technical checks:**
- "How many URLs are indexed versus submitted in the sitemap?"
- "Which pages have a coverage problem right now?"
- "Compare mobile and desktop performance for the same pages."

**Combined with other sources:**
- "Which queries brought sessions that converted, using Analytics for the outcome?" (requires Google Analytics)
- "Which organic landing pages also carry paid spend?" (requires Google Ads)
- "Match these queries to the pages that rank, then show revenue for those pages." (requires an ecommerce or revenue connector)

## Comparison: MCP vs. Manual Export

| Aspect | CorpusIQ MCP | Search Console export |
|---|---|---|
| Time to answer a new question | Seconds | Export, then reshape by hand |
| Dimensions | Chosen from the question | Fixed before you knew the answer |
| Follow-up question | One sentence | Rebuild the export |
| Cross-source joins | Built in with other connected tools | Manual spreadsheet work |
| History | Roughly 16 months, paginated | Same window, capped by the export |
| Setup | Under 5 minutes, no code | No setup, but recurring manual work |

## Security

- **Read-only by scope.** The connector requests the read scope for search performance data. Write-capable management tools, where present, are separately named and annotated.
- **No stored payloads.** Direct MCP retrieval does not retain raw customer files or full connector response payloads. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **Access follows the Google account.** Revoking that account's access in Google ends the connector's reach immediately.
- **Disconnect behavior.** A CorpusIQ disconnect requires reauthorization before reuse. Provider authorization remains governed by Google.

## FAQ: Common Questions

<details>
<summary><strong>Which Search Console properties can I connect?</strong></summary>

Both property types work: URL-prefix properties and Domain properties. The property you can read is the one your Google account is a verified owner of. If you own several, connect the account that carries the traffic you care about, or use the same account to cover a portfolio.
</details>

<details>
<summary><strong>How much history is available?</strong></summary>

The Search Console API exposes roughly 16 months of performance data. Anything older has to come from your own archive. Recent data also arrives with a short delay, which is normal for Search Console and not something the connector can remove.
</details>

<details>
<summary><strong>Can Claude change my property settings or submit a sitemap?</strong></summary>

No. The integration is read-only. It can read search performance, sitemap status, and URL inspection results, and it cannot submit sitemaps, request indexing, or modify verification.
</details>

<details>
<summary><strong>How is this different from exporting a Search Console report?</strong></summary>

An export is a snapshot with the dimensions you chose before you knew what you were looking for. A live query picks dimensions from the question, so the follow-up costs one sentence instead of another export.
</details>

<details>
<summary><strong>Does this work for agency accounts with many properties?</strong></summary>

Each CorpusIQ user authorizes their own Google account, so an agency can read a client property under the client's permission set. Access follows the account you authorize.
</details>

<details>
<summary><strong>What about large result sets?</strong></summary>

Search Console returns paged responses. The connector follows the pages, so an answer is not quietly capped at the first screen of rows. For a very large range, narrow it with a date range or a page filter.
</details>

<details>
<summary><strong>Where is my data stored?</strong></summary>

It is not stored. Retrieval happens on demand against the live API. CorpusIQ does not retain raw customer files or full connector response payloads. Operational query logs may persist for up to 30 days. See the [security documentation](../security/) for the detail.
</details>

## Related Pages

- [Connect Google Analytics to Claude](connect-google-analytics-to-claude.md) - the outcome layer beside the query layer
- [Connect Google Ads to Claude](connectors/connect-google-ads-to-claude.md) - paid search beside organic
- [Connect Google Sheets to Claude](connect-google-sheets-to-claude.md) - where the fixed reports live today
- [MCP for Marketing](mcp-for-marketing.md) - the reporting pattern in full
- [Browse all CorpusIQ connectors](connectors.md) - the full list
- [MCP vs API Integrations](mcp-vs-api-integrations.md) - why the access model differs

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
