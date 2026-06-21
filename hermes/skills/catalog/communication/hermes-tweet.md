---
name: hermes-tweet
description: Native Hermes Agent plugin for X/Twitter search, account reads, trend checks, and approval-gated account actions through Xquik.
triggers:
  - "x twitter automation"
  - "tweet search"
  - "social listening"
source: Xquik-dev/hermes-tweet
category: communication
setup: hermes plugins install Xquik-dev/hermes-tweet --enable
---

# Hermes Tweet

Hermes Tweet is a native Hermes Agent plugin for X/Twitter automation. It
adds a dedicated `hermes-tweet` toolset with catalog discovery, read-only
calls, and gated account actions.

## Setup

```bash
hermes plugins install Xquik-dev/hermes-tweet --enable
```

For a PyPI install inside an existing Hermes Python environment:

```bash
uv pip install --python ~/.hermes/hermes-agent/venv/bin/python hermes-tweet
hermes plugins enable hermes-tweet
```

Hermes prompts for `XQUIK_API_KEY` during an interactive plugin install. For
non-interactive installs, set `XQUIK_API_KEY` in the Hermes runtime environment
or `~/.hermes/.env` before using read tools.

## Capabilities

- X/Twitter search and account lookup workflows
- Tweet, reply, follower, list, media, and trend reads
- Social listening, launch monitoring, support triage, and creator research
- Giveaway and community audit evidence gathering
- Optional posting, replies, follows, DMs, monitor changes, webhooks, media,
  extraction jobs, and draw actions

## Safety Model

Hermes Tweet separates discovery, reads, and actions:

| Tool | Purpose |
|------|---------|
| `tweet_explore` | Search the bundled endpoint catalog without an API call. |
| `tweet_read` | Call catalog-listed read-only endpoints. Requires `XQUIK_API_KEY`. |
| `tweet_action` | Call private or write-like endpoints. Requires `XQUIK_API_KEY` and `HERMES_TWEET_ENABLE_ACTIONS=true`. |

Keep `tweet_action` disabled for unattended cron or gateway sessions unless the
workflow has an explicit approval step.

## Hermes Integration

The plugin uses the Hermes plugin entry point `hermes-tweet = hermes_tweet` and
ships a bundled skill for agent-facing usage guidance. Install it on the Hermes
runtime host that executes plugin code, then connect Desktop or remote gateway
profiles to that runtime.

Start with `tweet_explore` to find a supported `/api/v1/...` route, then use
`tweet_read` for public or account reads. Use `tweet_action` only after stating
the exact endpoint and payload.

## Source

- Repository: [Xquik-dev/hermes-tweet](https://github.com/Xquik-dev/hermes-tweet)
- Package: [hermes-tweet on PyPI](https://pypi.org/project/hermes-tweet/)
- License: MIT

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) - 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*
