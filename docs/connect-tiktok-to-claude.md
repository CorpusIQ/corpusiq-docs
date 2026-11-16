---
title: "Connect TikTok to Claude via MCP - Video Analytics in Chat"
description: "Connect TikTok to Claude through CorpusIQ MCP. Ask which videos drive views, likes and shares, and how each one performs per view."
category: Claude Integrations
tags: ["connect TikTok to Claude", "TikTok Claude integration", "MCP TikTok connector", "TikTok analytics to Claude", "AI for social analytics", "CorpusIQ MCP"]
last_updated: "2026-11-16"
canonical: https://www.corpusiq.io/docs/connect-tiktok-to-claude
robots: index,follow
---

# How to Connect TikTok to Claude with CorpusIQ MCP

TikTok analytics tells you what a video did. It is much worse at telling you why one video outperformed another, or how the channel compares with the rest of your content spend when the numbers live in different dashboards.

Connecting TikTok to Claude through CorpusIQ MCP puts your video data beside everything else you measure. Ask which videos earn engagement per view, and the answer arrives with the video list it came from.

### Why Connect TikTok to Claude?

- **Ranked video performance.** Top videos by views, likes, comments or shares, without scrolling the analytics tab.
- **Engagement per view.** A fairer comparison than raw totals when one video has ten times the reach of another.
- **Follower and posting context.** Profile level counts read in the same answer as per-video detail.
- **Cross-channel comparison.** Put TikTok results beside YouTube, Instagram or paid social in one conversation, once those connectors are added.
- **Period questions.** "This month" and "last 90 days" are answered from the same underlying video records.
- **Read path only.** The connection reads profile, videos and analytics. It never posts, comments or follows.

### How It Works

1. **Connect TikTok to CorpusIQ** through the TikTok authorization screen, approving the profile, video list and analytics scopes.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ translates** your question into TikTok API calls for profile, video list and per-video analytics, then assembles the records.
4. **Claude answers** from that data and names the videos behind the numbers.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in to CorpusIQ and open **Connectors**.
2. Select **TikTok** and click Connect.
3. Sign in to TikTok if you are not already signed in.
4. Review the requested scopes, which cover profile, video list and video analytics, and click Authorize. TikTok requires accepting all of them.
5. TikTok turns from gray to green in the CorpusIQ dashboard.
6. Copy the MCP config block under **Settings, Integrations, Claude Desktop**.

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

If the tools indicator does not appear, work through [Claude can't see CorpusIQ](troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

### Example Claude Questions

**Video performance**

- "What are my top 10 TikTok videos by views?"
- "Which videos drove the most engagement per view?"
- "How many likes did I get on TikTok this month?"
- "List my videos posted in the last 30 days with views and shares."

**Account questions**

- "Show my TikTok follower count and total video count."
- "What is my average view count per video?"
- "Which video has the best comment to view ratio?"
- "How many videos have I posted this quarter?"

**Cross-channel questions**

- "Compare TikTok views with YouTube views for the same period."
- "Which platform gave us the most engagement per view last month?"
- "Did the video that worked on TikTok get similar reach on Instagram?"

### Security

- **Scope-bound access.** TikTok shows the requested scopes on its authorization screen: profile, video list and video analytics. Access is limited to those.
- **No write path.** CorpusIQ reads videos and analytics. There is no publish, comment, follow or delete path exposed to the assistant.
- **Revocable at any time.** TikTok, Settings, Security, Manage app permissions. Removing CorpusIQ there ends the connection.
- **Scoped direct-MCP retention.** CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Comparison: TikTok analytics vs TikTok Through Claude

| Question | TikTok analytics tab | CorpusIQ MCP with Claude |
|---|---|---|
| Input | Date range and video picker | A question in plain language |
| Output | Charts and per-video tables | A ranked answer with the videos named |
| Comparison | One video at a time | Videos ranked by any measure you ask for |
| Cross-channel | TikTok only | TikTok beside your other channels |
| Write access | Yes, by you in the app | None exposed to the assistant |

TikTok analytics answers what happened on TikTok. Claude answers what it means next to everything else.

### FAQ: Common Questions

<details>
<summary><strong>Can Claude post to TikTok?</strong></summary>

No. The connection reads profile, video and analytics data only. Publishing stays in the TikTok app.
</details>

<details>
<summary><strong>Does this work for multiple TikTok accounts?</strong></summary>

Each account is authorized separately, so a personal and a brand account can both be connected without sharing a login.
</details>

<details>
<summary><strong>Which metrics are available?</strong></summary>

Views, likes, comments, shares, and profile level follower and video counts, read from the account at the moment you ask.
</details>

<details>
<summary><strong>Why did authorization fail?</strong></summary>

TikTok requires every requested scope to be approved. Reconnect and accept the full set; a partial approval is rejected at the TikTok layer.
</details>

<details>
<summary><strong>Can I see competitor accounts?</strong></summary>

No. The connection covers accounts you authorize. Public competitor data is a research question for a different source.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Each question runs against the account when you ask, so a video posted this morning is included.
</details>

---

**Next steps:** [Connect TikTok to Claude now](https://www.corpusiq.io/docs/connectors/tiktok)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
## See also

- [Connect TikTok to Perplexity](connect-tiktok-to-perplexity.md) - video performance and channel comparisons inside a Perplexity thread.
- [Connect TikTok to ChatGPT](connect-tiktok-to-chatgpt.md) - ranked video analytics inside a ChatGPT thread.
- [TikTok connector reference](connectors/tiktok.md) - connection requirements, visible objects and troubleshooting.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
