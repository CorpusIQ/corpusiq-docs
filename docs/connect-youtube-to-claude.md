---
title: "Connect YouTube to Claude via MCP - Channel Analytics"
description: "Connect YouTube to Claude through CorpusIQ MCP. Ask which videos earned watch time, where viewers came from and what comments ask, read-only."
category: Claude Integrations
tags: ["connect YouTube to Claude", "YouTube MCP", "YouTube Claude integration", "YouTube analytics in Claude", "channel analytics questions", "CorpusIQ MCP"]
last_updated: "2026-11-07"
canonical: https://www.corpusiq.io/docs/connect-youtube-to-claude
robots: index,follow
---

# How to Connect YouTube to Claude with CorpusIQ MCP

YouTube Studio answers channel questions one tab at a time. Watch time lives in one view, traffic sources in another, the comment thread in a third, and the transcript in a fourth. None of them tell you whether the video that earned eight thousand views moved the store.

Connecting YouTube to Claude through CorpusIQ MCP puts channel analytics in the same conversation as your site, your ads, and your order data. You ask a question, Claude reads the channel, and the answer comes back with the video and the period it used named in the reply. Read-only.

### Why Connect YouTube to Claude?

- **Top performers by the metric that matters.** "What are my top videos this quarter by watch time?" is a different list from the one sorted by views.
- **Traffic sources.** "Where are most of my viewers coming from this month, and did that change after the last upload?"
- **Comments as research.** "What are people asking in the comments on the launch video?" Comments are the cheapest customer interview you have.
- **Transcripts on demand.** "Summarize the transcript of my latest upload." Useful for repurposing, for SEO, and for checking what was actually promised.
- **The commercial question.** "Which upload drove the most referred traffic to the store last month?" That one needs YouTube beside analytics and orders.
- **Read-only by scope.** The connector reads. It never uploads, edits, deletes, or replies.

### How It Works

1. **Connect YouTube to CorpusIQ** through Google. Personal channels and Brand Account channels both work, and when several are available you choose which one to read.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ retrieves** channel totals, videos, per-video analytics, geography, comments, and transcripts for the channel you selected.
4. **Claude answers** from that retrieved content, with the video and the date range named.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **YouTube**. If you already connected Google Workspace, YouTube may already be authorized under that connection.
3. Sign in with the Google account that owns or manages the channel and approve the read-only scopes.
4. If several channels are available, pick the one you want to read.
5. Copy the MCP config block shown under **Settings, Integrations, Claude Desktop**.

**In Claude Desktop**

6. Open **Settings, Developer, Edit Config**. This opens `claude_desktop_config.json`.
7. Add the CorpusIQ entry:

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

8. Save the file and fully quit Claude Desktop. Not just the window: quit the application.
9. Reopen Claude, complete the device login when prompted, and the tools indicator appears next to the message box.

If the tools indicator does not appear, work through [Claude can't see CorpusIQ](troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

### Example Claude Questions

**Channel performance**

- "What are my top videos this quarter by watch time?"
- "Which uploads earned the most watch time per view?"
- "Compare this month's channel totals with last month."

**Audience**

- "Where are most of my viewers coming from?"
- "Which countries grew the most in the last 90 days?"
- "Is my audience watching on mobile or desktop?"

**Content research**

- "Summarize the transcript of my latest upload."
- "List every tool or product mentioned in that video."
- "What are people asking in the comments on the launch video?"
- "Which comments mention a competitor?"

**Cross-source**

- "Which upload drove the most referred traffic to the store last month?" (requires the analytics or commerce connector)
- "Did the video that launched the same week as the ad campaign earn more watch time than the ones before it?" (requires the ads connector)
- "Show me store orders from customers who arrived from YouTube." (requires the commerce connector)

### Security

- **Read-only by scope.** The connector reads channel totals, videos, per-video analytics, geography, transcripts, comments on public videos, and search results. It cannot upload, edit, or delete a video, reply to a comment, or change a channel setting.
- **Google-enforced consent.** Google shows exactly which scopes are granted, and they are read scopes, not a bundle of write permissions.
- **Revocable at any time.** Google Account, Security, Third-party access. Revoking there ends the connection.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between YouTube, CorpusIQ, and Claude.

### Comparison: YouTube Studio vs YouTube Through Claude

| Aspect | YouTube Studio | CorpusIQ MCP with Claude |
|---|---|---|
| Input | Tabs, filters, date pickers | A question in plain language |
| Output | Charts and tables | A synthesized answer with the video named |
| Comments | You scroll the thread | Summarized into what viewers are asking |
| Transcripts | Copy from the caption view | Returned on request |
| Mixing sources | Export and join elsewhere | Channel plus site, ads, and orders in one answer |
| Write access | Yes, by you | None, read-only |

Studio is the right tool when you want to look at one video. Claude is the right tool when you want to know what the channel is doing.

### FAQ: Common Questions

<details>
<summary><strong>Does it work with a Brand Account channel?</strong></summary>

Yes. Personal channels and Brand Account channels both work. When several channels are available under one Google account, the connection asks which channel to read and you pick the one that matters.
</details>

<details>
<summary><strong>Do I need a separate connection for YouTube?</strong></summary>

Not always. If you already connected Google Workspace, YouTube may already be authorized under the same Google connection. Otherwise YouTube connects on its own with the same Google sign-in.
</details>

<details>
<summary><strong>Can Claude post a video or reply to comments?</strong></summary>

No. Every YouTube tool exposed to Claude is read-only. Publishing, editing metadata, deleting, and replying to comments are not available through this connection.
</details>

<details>
<summary><strong>Which comments can it read?</strong></summary>

Comments on public videos for the connected channel. Private messages and comments on videos the connection cannot see are not accessible.
</details>

<details>
<summary><strong>Are transcripts available for every video?</strong></summary>

Transcripts are available where YouTube publishes captions or auto-captions for the video. A video with no caption track returns no transcript, and the answer says so rather than guessing at the content.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Every question is answered against the channel at the moment you ask. There is no nightly copy of your analytics behind the answers.
</details>

---

**Next steps:** [Connect YouTube to Claude now](https://www.corpusiq.io/connectors/youtube)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
