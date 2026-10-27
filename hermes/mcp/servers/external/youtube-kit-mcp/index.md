---
title: "YouTube Kit MCP - Channel Analytics, Uploads, Comments"
description: "MIT Python MCP server and ytk CLI for YouTube: per-video analytics, resumable uploads, metadata, playlists and comment moderation across channels."
category: Social Media Management
stars: 0
added: 2026-10-19
source: "mcpservers.org /all page 1 (eukosh/youtube-kit)"
relevance: ★★★
tags: [youtube, video, analytics, content-operations, comment-moderation, uploads, multi-channel, cli, self-hosted]
last_updated: "2026-10-24"
---

# YouTube Kit MCP

**The YouTube channel as a set of tools an agent can run: analytics broken down by video, day or traffic source, resumable uploads, metadata and thumbnails, playlists, and comment moderation - across several channels, from one local server, with the quota cost printed next to every command.**

```
Server type: Local (stdio) - `uvx youtube-kit mcp`
Also a CLI: `ytk` (same code, same operations)
Package: `youtube-kit` 0.6.0 on PyPI, Python 3.12+, MIT
Auth: Your own Google Cloud OAuth client (Desktop app), one login per channel.
      Public data only: `YOUTUBE_API_KEY`
Channels: Several at once - default channel plus `--my-channel` / `my_channel` per call
Not covered: captions, localizations, live streaming, channel memberships
Quota: 10,000 units a day per Cloud project, resets midnight Pacific
Publisher: eukosh (github.com/eukosh/youtube-kit, created August 21, 2026)
```

## Why This Matters for Operators

The channel is a business asset, but its numbers live in Studio, its comments live in a queue nobody opens, and its upload path lives in a browser. That means the questions an operator actually asks - which video earned the views this quarter, which traffic source is growing, are there comments held for review, did last week's upload get its thumbnail - get answered by a person clicking through screens, or not at all.

This server answers them as tool calls. The difference from a generic "YouTube API wrapper" is the packaging: a daily quota budget stated per operation, a JSON output contract with named exit codes, and deletes that refuse to run without an explicit second call naming the exact target. Those three things are what make it safe to leave connected.

## What You Can Do Today

| Area | Operations |
|---|---|
| Analytics | Totals, or breakdowns by day, month, video, country, device, OS, traffic source, playback location, age, gender, subscriber status |
| Videos | Get, categories, resumable upload with progress, update metadata, set thumbnail, wait for processing, like or dislike, check your rating, delete |
| Comments | List published, held for review or likely spam; list replies; post, reply, edit, delete; approve, hold, reject; ban the author |
| Playlists | List, get, items, create, update, set image, add, remove, move, delete |
| Channel | Get, recent activity, your logged-in channels, about info (description, keywords, country, language, trailer), banner, watermark, home-page sections |
| Search | Videos, channels and playlists, filtered by channel or date |
| Subscriptions | List, subscribe, unsubscribe |

Typical prompts this supports: "which of my videos got the most views in the last 90 days", "are any comments waiting for review", "upload this clip to the gaming channel with this title", "move these three videos into the Q4 playlist", "what share of views came from browse versus search last month".

## The Contract That Makes It Safe to Connect

- **One JSON document per command on stdout.** On failure stdout stays empty, the last line of stderr is a JSON error object, and the exit code names the type: 2 bad input, 3 not found, 4 not authorized, 5 quota exceeded, 6 forbidden, 7 network, 8 confirmation required, 9 protected, 10 timeout.
- **Quota cost is stated up front.** Every command's `--help` and every MCP tool description says what it spends, so a planner can budget a day rather than discover exhaustion at 3pm.
- **Deletes are two-step.** The first call deletes nothing: a human gets a `[y/N]` prompt, an agent gets exit 8 with a description of the target and must call again with `--confirm <id>`, so the approval always names the thing being deleted.
- **Damage limits.** A video with more than 100 views, or a public video older than 7 days, cannot be deleted through this tool at all; the thresholds are in `config.toml` under `[delete_protection]`. Deleting something already gone succeeds with `"already_gone": true`.

## Setup

1. `uv tool install youtube-kit` (or `brew install uv` first).
2. Create a Google Cloud project and enable **YouTube Data API v3** and **YouTube Analytics API**.
3. In Google Auth Platform, set the audience to External, fill the branding fields (home page, privacy policy, authorized domain) and publish the app. While it stays in Testing, only listed test users can sign in and Google expires them after 7 days.
4. Create a **Desktop app** OAuth client and download its JSON.
5. `ytk auth login --client-secrets path/to/client_secret.json`, then repeat per channel, including brand channels.

`ytk auth guide` (or the `setup_guide` MCP tool) walks an agent through what is left and can create the project itself when the gcloud CLI is signed in; the browser step stays manual. With an API key only, `export YOUTUBE_API_KEY=...` covers public search, videos, channels, playlists and comments.

Register the server with a client:

```bash
claude mcp add youtube -- uvx youtube-kit mcp
```

```json
{
  "mcpServers": {
    "youtube": { "command": "uvx", "args": ["youtube-kit", "mcp"] }
  }
}
```

ChatGPT desktop app: Settings → MCP servers → Add server → STDIO, command `uvx youtube-kit mcp`.

Credentials and `config.toml` live in `~/.config/youtube-kit/` on Linux (`ytk auth status` prints the exact paths). Environment overrides: `YOUTUBE_API_KEY`, `YOUTUBE_CLIENT_SECRETS`, `YOUTUBE_TOKEN_DIR`, `YOUTUBE_CHANNEL`, `YOUTUBE_CONFIG_FILE`.

## Quota Arithmetic

Each Cloud project gets 10,000 units a day. Reads cost 1 unit per request, `search` costs 100 per page of 50 results, most writes cost 50, guarded deletes cost 52, and an upload costs 1,600 - roughly six uploads a day before the project is done. Analytics uses the separate YouTube Analytics API quota.

That arithmetic is the reason the tool ships its own OAuth client instead of bundling one: a shared client would put every user on the same 10,000 units.

## Integration with CorpusIQ

YouTube numbers are one input in a business answer, not the answer. CorpusIQ joins the channel side to the rest of the operator's stack - commerce, payments, ads, CRM, analytics - over read-only scoped connectors with source citations, so "views are up but revenue is flat" becomes a comparison across two systems instead of two browser tabs. This server supplies the channel side: what was published, what it earned, what people said, and what still needs a reply.

## Limitations

- **Bring your own Google Cloud project.** There is no hosted option and no shared quota; the ~5 minute setup is real work, and an unpublished OAuth consent screen logs testers out every 7 days.
- **Four gaps:** captions, localizations, live streaming and channel memberships are not covered.
- **Guardrails, not a guarantee.** The delete protections stop mistakes, not a determined agent; anything holding the OAuth token can call the API directly. Pair it with client-side approval prompts for `ytk video delete`, `ytk playlist delete` and `ytk comment delete`.
- **Young project.** First release August 2026, version 0.6.0 on October 18, 2026, no stars yet and two open issues; the tool surface is current as of this catalog entry, and the CLI/MCP parity test is in CI.
- **Uploads are synchronous from the agent's point of view.** Resumable upload with progress works, but large files still consume the turn; use `wait for processing` deliberately.

## FAQ

### Does it need my Google password?

No. It uses an OAuth desktop client you create, and tokens are stored per channel on your own machine. Nothing passes through a third-party server.

### Can it post and moderate, or only read?

Both. It can post comments and replies, approve, hold or reject comments, ban an author, upload and update videos, and edit playlists. The write surface is the reason the delete path is guarded and quota-priced.

### Is it affiliated with YouTube?

No. MIT licensed, not affiliated with or endorsed by Google; YouTube is a trademark of Google LLC.

## Sources

- mcpservers.org listing `eukosh/youtube-kit` (page 1 of `/all`, October 19, 2026)
- README and skill documentation at `github.com/eukosh/youtube-kit` (created August 21, 2026, last push October 19, 2026, MIT, Python, topics include `youtube-analytics`, `youtube-mcp`)
- PyPI metadata for `youtube-kit` 0.6.0, uploaded October 18, 2026 (Python >= 3.12)
