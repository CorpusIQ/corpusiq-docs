---
title: "Connect CallRail to Claude via MCP - Call Attribution"
description: "Connect CallRail to Claude through CorpusIQ MCP. Ask which campaigns produced calls, how long they lasted and where callers came from, read-only."
category: Claude Integrations
tags: ["connect CallRail to Claude", "CallRail Claude integration", "call attribution in Claude", "MCP CallRail connector", "phone lead analytics", "CorpusIQ MCP"]
last_updated: "2026-11-03"
canonical: https://www.corpusiq.io/docs/connect-callrail-to-claude
robots: index,follow
---

# How to Connect CallRail to Claude with CorpusIQ MCP

Calls are the part of marketing that spreadsheets miss. A form fill arrives with a campaign attached. A phone call arrives with a tracking number, a duration, and a source, and the story stops there unless somebody joins it back to the campaign by hand.

Connecting CallRail to Claude through CorpusIQ MCP makes the call record queryable. Authorize read-only access once, ask which campaigns produced calls and how those calls went, and the answer arrives with the account, the window, and the source attached.

### Why Connect CallRail to Claude?

- **Attribution that includes the phone.** "Which source sent the most calls this quarter, and did that change week over week?" Paid search usually looks different once calls are counted.
- **Call quality, not just call volume.** "How many calls came in last month, and how long did they last on average?" A cheap channel that produces sixty-second calls is not cheap.
- **Tracking numbers.** "Which tracking numbers received the most calls?" Useful for checking whether a number is deployed where you think it is.
- **Timing against spend.** "Do the calls arrive at the same time as the ad clicks, or later?" That answer tells you whether the phone is an impulse channel or a considered one, and it changes budgets.
- **Multi-company accounts.** "Which companies under this account are generating calls, and which are quiet?"
- **Read-only by scope.** The connector lists accounts, companies, trackers, and calls. It never creates, tags, edits, or deletes anything.

### How It Works

1. **Connect CallRail to CorpusIQ** by authorizing read-only access to the account you want to read.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ retrieves** the reachable accounts, the account summary and features, the companies and tracking numbers under it, and the calls themselves with duration, start time, source, and caller data.
4. **Claude answers** from that retrieved content, naming the account and the window it used.

Every read after the account list is scoped to one account, so the first call behind any question is always the account lookup. That is why an answer names the account it came from.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **CallRail**.
3. Authorize read-only access and pick the account you want to query.
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

**Volume and quality**

- "How many calls came in last month, and how long did they last on average?"
- "Which source sent the most calls this quarter?"
- "Show me calls shorter than one minute, by source."

**Tracking numbers and companies**

- "Which tracking numbers received the most calls this month?"
- "Which companies under this account are generating calls, and which are quiet?"
- "Which tracking number has had no calls in 30 days?"

**Timing and cross-source**

- "Do the calls arrive at the same time as the ad clicks, or later?" (requires the ads connector)
- "Which campaign I spent the most on produced the fewest calls?" (requires the ads connector)
- "Which calls came from sessions that never submitted a form?" (requires the analytics connector)
- "Which leads in the CRM came from a phone call rather than a form?" (requires the CRM connector)

### Security

- **Read-only by contract.** The connector exposes five read actions: accounts, one account summary, companies, tracking numbers, and calls. Write access is not exposed at all, not hidden behind a confirmation step.
- **Account-scoped.** Every read after the account list is bounded to the account you selected, so a question cannot silently reach another client's data.
- **Revocable at any time.** Removing the authorization in CallRail ends the connection.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between CallRail, CorpusIQ, and Claude.

### Comparison: CallRail Reporting vs CallRail Through Claude

| Aspect | CallRail reports | CorpusIQ MCP with Claude |
|---|---|---|
| Input | A report, a date range, an account | A question in plain language |
| Output | Tables and call lists | A synthesized answer with the source named |
| Campaign join | Export and match by hand | Calls beside ad and analytics data in one answer |
| Multi-company view | Company by company | Compared in one answer |
| Reading a call | Open the record | Summarized with duration and source |
| Write access | Yes, by you | None, read-only |

Reports are the right tool when you need the call log. Claude is the right tool when you need to know which channel is producing the phone calls worth answering.

### FAQ: Common Questions

<details>
<summary><strong>What does the connector expose?</strong></summary>

Five read actions: the accounts the connection can reach, a single account summary with its features, the companies under an account, the tracking numbers configured under an account, and the calls themselves with tracking number, duration, start time, source, and caller data.
</details>

<details>
<summary><strong>Is this read-only?</strong></summary>

Yes. The connector lists accounts, companies, trackers, and calls. It does not create, tag, edit, or delete anything in CallRail.
</details>

<details>
<summary><strong>Can I query more than one account?</strong></summary>

The account list comes back first, and each further read is scoped to one account. To compare two accounts, ask two questions or ask for a comparison that names both, and the answer keeps the accounts separate.
</details>

<details>
<summary><strong>Does it read call recordings or transcripts?</strong></summary>

The connector reads the call record: tracking number, duration, start time, source, and caller data. Recordings and transcripts are not part of the read set.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Every question is answered against CallRail at the moment you ask. There is no nightly copy of your call data behind the answers.
</details>

<details>
<summary><strong>Why does the answer always name the account?</strong></summary>

Because every read is account-scoped. Naming the account is how you can tell which business the call data belongs to when one login manages several.
</details>

---

**Next steps:** [Connect CallRail to Claude now](https://www.corpusiq.io/connectors)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
