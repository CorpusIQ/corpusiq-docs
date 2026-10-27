---
title: "CommentKeyword MCP - Instagram Comment-to-DM Automations"
description: "Create, retarget and pause Instagram keyword automations from Claude or Cursor through Meta's official Instagram API, with a token scoped per permission."
category: Social / Instagram Automation
stars: n/a (included on every plan, free tier)
added: 2026-10-27
source: "vendor page commentkeyword.com/instagram-mcp-server, official MCP registry entry com.commentkeyword/mcp 0.2.0 with an mcpb package, and the submission issue describing the local stdio server, its six tools and its permission scopes"
relevance: ★★★
tags: [instagram, comment-to-dm, dm-automation, social, marketing, meta-api, scoped-tokens, mit]
last_updated: "2026-10-27"
---

# CommentKeyword MCP

**A comment-to-DM automation is the highest-converting mechanic on Instagram and the most brittle thing to run by hand: the Reel publishes, the comments arrive, and the DM that was supposed to go out never does.**

```
Server type: Local stdio (npx, MIT, Node 18+)
Command:     npx -y github:commentkeyword/agent-toolkit#v0.2.0
Transport:   stdio
Auth:        CommentKeyword API token in COMMENTKEYWORD_API_TOKEN
Perms:       keywords:read, keywords:write, keywords:delete, agents:read
Tools:       6, from the vendor documentation and the submission
Registry:    com.commentkeyword/mcp version 0.2.0
```

## Why This Matters for Operators

The mechanic is simple and unforgiving: a viewer comments a word, and the automation sends them the link. Get the keyword wrong and it misfires on ordinary conversation. Get the timing wrong and the DM goes out before the post exists. Forget it entirely and the CTA in the video points at nothing.

This server puts the setup in the same conversation that writes the video. The agent reads the CTA from the script, picks a keyword that will not misfire, writes the DM, and arms it against the **next** post, so the automation exists before the Reel publishes rather than after somebody notices.

## What It Actually Does

| Tool | What it does | Permission |
|---|---|---|
| `create_keyword` | Creates an automation. `target` is `next_post`, `all_posts` or `specific_posts`, with DM variants, optional public replies, link tracking and an optional AI agent | `keywords:write` |
| `update_keyword` | Changes an existing automation: keyword, DM, target, public reply | `keywords:write` |
| `list_keywords`, `get_keyword` | Reads what is armed, and on which posts | `keywords:read` |
| `delete_keyword` | Removes an automation | `keywords:delete` |
| `list_agents` | Lists the Live AI agents available to attach to a conversation | `agents:read` |

The `next_post` target is the detail that makes it usable in an editing workflow: no media ID is needed, and the automation attaches itself to the next post or reel the account publishes. Automated DMs count against the plan's monthly allowance, and the toolkit is included on every plan including Free.

## How It Is Contained

- **Scoped token, not account access.** The operator mints a token with exactly the permissions they mean to grant. Read-only means the agent can look and cannot arm anything; adding `keywords:delete` is a separate decision.
- **Official Instagram API.** The DMs go out through Meta's official Instagram API on a Business or Creator account connected to CommentKeyword. The agent never logs in to Instagram and never sees a password.
- **Only commenters get the DM.** After creation the automation behaves exactly like one built in the dashboard, which means the audience is people who commented the keyword, not a list.
- **MIT and local.** The server runs on the operator's machine through `npx`, and the token sits in the system keychain when installed as a Claude Code plugin.

## Limitations Recorded

- **No remote endpoint.** claude.ai and ChatGPT can only attach remote servers by URL, so today this works in Claude Code, Claude Desktop, Cursor, Windsurf, Codex and the ChatGPT-backed Codex path - not in the claude.ai web connector dialog.
- The server itself was not executed here: the tokens and an Instagram professional account are required, so the tool and permission names come from the vendor's documentation and registry record.
- **There is no official Meta MCP server for organic Instagram.** Meta publishes an official MCP server for ads, not for organic posts, comments or DMs, so every Instagram MCP server is third-party. This one is documented as using Meta's official Instagram API behind a third-party platform, which is a materially different arrangement from a scraper.
- Keyword choice is the failure mode. The vendor's own guidance is to avoid words people write anyway, such as YES or WOW, because the automation cannot tell a CTA from a reaction.
- AI-agent handoff for the conversation after the DM needs a paid plan.

## FAQ

### Does the agent post to Instagram for me?
No. It creates, changes and pauses comment automations. Publishing the Reel is a separate step, and arming against `next_post` exists so the automation is ready before that step happens.

### Is this scraping Instagram?
No. DMs are sent through Meta's official Instagram API on a connected Business or Creator account, and the agent holds a CommentKeyword token with named permissions rather than an Instagram login.

### What is the safe first configuration?
A token with `keywords:read` only, so the agent can read what is armed while you set up the first automation by hand, then add `keywords:write` once you have seen how it phrases the keyword and the DM.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [gbply MCP - multi-location local presence the same way](/hermes/mcp/servers/external/gbply-mcp/)
- [CorpusIQ connectors for social and marketing platforms](/hermes/mcp/)
