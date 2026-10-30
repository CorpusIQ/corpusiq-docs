---
title: "Slack CLI Skill - Agent-Driven Workspace Automation Setup"
description: "paymog/slack-cli: 9.8K combined installs. A Go CLI that gives agents JSON reads and writes on Slack, with no resident MCP server per agent."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/paymog-slack-cli-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "slack", "team chat", "cli"]
---

# Slack CLI - Setup Guide

**Source:** [paymog/slack-cli](https://www.skills.sh/paymog/slack-cli) via skills.sh - 9.8K combined installs across 1 indexed listing; first seen 2026-10-29 (evening sweep)

**GitHub:** [paymog/slack-cli](https://github.com/paymog/slack-cli) - 0 stars, MIT License, branch master, last pushed 2026-10-20; one skill at `skills/slack-cli/SKILL.md` inside a real Go application tree (`cmd/slack-cli`, `cmd/slack-mcp-server`, `pkg/provider`, `pkg/handler`, `internal/toolcall`, `internal/credstore`, `docs/`, `npm/`), 80 Go files, tagged v0.4.0 at HEAD

**Category:** Team chat automation, developer tooling and CLI wrappers around MCP servers

**Quality Tier:** 🟡 Beta - one Snyk Warn (S123) on the single indexed listing; MIT, 0 stars, same publisher as the Groundcover and incident.io CLI guides

slack-cli is a command line interface for Slack workspaces built on the korotovsky/slack-mcp-server engine, and the repository's MIT license names Dmitrii Korotovskii, the author of that engine. It keeps the same auth modes, edge API access, rate limiter, smart history and on-disk caching, but exposes them as ordinary subcommands instead of a long-lived MCP server. Both entrypoints ship from the same tree: `cmd/slack-cli` is the new binary, and `cmd/slack-mcp-server` is the original server, kept working on purpose. The CLI is additive and reuses `pkg/provider` and `pkg/handler` unchanged, so upstream engine changes still merge cleanly.

What is in the box for an agent is small: a single 13,445 character skill file at `skills/slack-cli/SKILL.md` that lists the real command surface, the credential variables, the cache rule and the opt-in write gates. The skill assumes the binary is already installed and tells the agent to invoke it per task, so the file stays a routing and reference document rather than a runtime. This is the third CLI-shaped skill from the same publisher in this catalog, after the Groundcover and incident.io guides, and it is the one that removes a resident process from the picture entirely.

## Installation

The README's install path is Homebrew. The formula builds from source, so Homebrew pulls in a Go toolchain as a build dependency:

```bash
brew install paymog/tap/slack-cli
```

Go install works if the toolchain is already present:

```bash
go install github.com/paymog/slack-cli/cmd/slack-cli@latest
```

Or build the checkout directly. `make cli` writes `./slack-cli`:

```bash
make cli
# or
go build ./cmd/slack-cli
```

The skill is separate from the binary. Because this repository has a real skill directory rather than a root-level `SKILL.md`, the file can be fetched straight into the Hermes profile:

```bash
mkdir -p ~/.hermes/profiles/corpusiq/skills/slack-cli
curl -sL -o ~/.hermes/profiles/corpusiq/skills/slack-cli/SKILL.md \
  https://raw.githubusercontent.com/paymog/slack-cli/master/skills/slack-cli/SKILL.md
```

The skills.sh CLI is the other route. `npx skills add paymog/slack-cli --skill slack-cli` is the skills CLI convention and installs only the skill, so pair it with one of the binary installs above:

```bash
npx skills add paymog/slack-cli --skill slack-cli
```

Before the first useful call, credentials have to resolve. Either export a token or store a profile, which keeps the secret in the OS keyring and only non-secret metadata in `~/.config/slack-cli/profiles.yaml`:

```bash
export SLACK_MCP_XOXP_TOKEN=xoxp-...
slack-cli auth login work --xoxp xoxp-...
slack-cli auth status
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| slack-cli | 9,849 | Teaches the agent to shell out to the `slack-cli` binary: list channels, read history and whole threads with `--limit 1d`, triage unreads and mentions, run legacy or real-time search, resolve users to DM channel IDs, manage user groups, post through `--text-file` for multi-line replies, and react, mark read or save items, with JSON on stdout that pipes into `jq`. |

No indexed listings fall below the threshold; all 1 appear above.

## Why This Matters for Hermes Agents

An MCP server is one resident stdio process per agent, so ten agents means ten Slack servers, each warming and holding its own user and channel cache for the whole session. slack-cli inverts that: every command is a short-lived process that reads a shared on-disk cache, so process count and memory do not grow with the number of agents you run.

Each invocation follows the same short path. It resolves credentials (explicit `SLACK_MCP_*` variables or flags, then `--profile`, then the default profile), builds the provider from `pkg/provider`, loads the cached user and channel maps so `#channel` and `@username` resolve to IDs, then calls the MCP tool handler in-process and prints its JSON. No transport, no JSON-RPC, no daemon, no port, no bearer token to keep alive between turns.

Output is JSON by default, which the underlying MCP server does not do (it emits CSV), so `jq -r '.[].Text'` works directly and `--raw` gets you the old CSV back when you want it. Writes are disabled unless the matching environment variable is set in the same invocation, so an agent cannot post, react or mark read by accident, and the channel allowlist accepts both `C123,D456` and the all-except form `!C123`.

The other practical win is that both frontends share the cache and the packages. If a profile already runs the bundled MCP server, the CLI reads the same cache file and neither side needs a rewrite; `slack-cli cache refresh` warms it for both.

## Usage

| You say | What happens |
|---|---|
| "What are the unread messages in #incidents?" | The agent runs `slack-cli cache refresh` once so names resolve, then `slack-cli conversations unreads --types dm` or `--mentions-only`, and reports with DMs ranked above partner and internal channels. |
| "Find the deploy thread and read the replies" | `conversations search "deploy rollback" --in-channel #incidents --after 2024-06-01` returns matching messages, then `conversations replies C0123456789 1718000000.123456` pulls the thread. A Cursor on a default replies call means the thread was cut short. |
| "Who is @alice, and can you DM her?" | `users search alice` returns user objects including `DMChannelID`; a follow-up `SLACK_MCP_ADD_MESSAGE_TOOL=D0123 slack-cli conversations add D0123 -t "ping"` opens the conversation. |
| "Post the standup summary to #eng" | The agent writes the body to a UTF-8 file with real newlines, then runs `SLACK_MCP_ADD_MESSAGE_TOOL=C123 slack-cli conversations add C123 --text-file /tmp/reply.txt --content-type text/mrkdwn`, which avoids shell escaping and Block Kit collapse. |
| "React with :rocket: to that message" | `SLACK_MCP_REACTION_TOOL=true slack-cli reactions add <channel> <timestamp> --emoji rocket`, with the same env gate for `reactions remove`. |
| "Pull the last day of #general and extract the text" | `conversations history #general --limit 1d` returns a JSON array, and the agent pipes it through `jq -r '.[].Text'` instead of printing raw records into the transcript. |
| "Grab the screenshot someone posted" | `attachments get F0123ABCD -o avatar.png` writes the decoded bytes to disk and keeps stdout to a small metadata JSON; attachment reads need no opt-in variable. |

## Verification

The raw SKILL.md path in this guide returned 200 on branch master when the guide was written on 2026-10-29:

```bash
curl -sL -o /dev/null -w "%{http_code} SKILL.md\n" \
  https://raw.githubusercontent.com/paymog/slack-cli/master/skills/slack-cli/SKILL.md
```

Expect `200`. There is exactly one SKILL.md in the repository tree, at `skills/slack-cli/SKILL.md`, and the raw URL is the same path with a leading slash added, so what you review is what the install fetches.

Read the file before you install it. It is the only place the credential gates and write gates are documented together, and the review is cheap: check the `name` and `description` frontmatter, the auth block, and the list of write commands that need an environment variable in the same call.

```bash
head -6 ~/.hermes/profiles/corpusiq/skills/slack-cli/SKILL.md
```

After install, confirm the binary resolves and that credentials resolve to the source you expect:

```bash
slack-cli auth status
slack-cli auth list
slack-cli cache refresh
slack-cli channels list --query eng --limit 5
```

The last command returning a JSON array with `ID`, `Name`, `Topic`, `Purpose` and `MemberCount` fields means the binary, the credentials and the cache are all working. If it errors with `users cache is not ready`, rerun `slack-cli cache refresh`; if it errors with `no Slack credentials`, the token or profile did not resolve.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| slack-cli | Pass | Pass | Warn |

No listing fails. Gen Agent Trust Hub and Socket pass the single sampled listing, and Snyk records one Warn, S123, which is the same shape of finding this publisher's other CLI guides carry; the pack does not include the finding text, so read the S123 entry on the skills.sh security page before you point the binary at a real workspace.

What installs by default is a markdown file that executes nothing. The risk sits in what the skill tells the agent to run: a CLI holding workspace credentials, with write commands behind opt-in environment variables, profiles that keep secrets in the OS keyring rather than a plaintext dotfile, and no way to delete a message short of a direct `chat.delete` call. Treat the browser session token pair (`xoxc` plus `xoxd`) as the most sensitive option, because it authenticates as a logged-in person rather than as an app installed in the workspace.

## Limitations

- Snapshot data, verified 2026-10-29: 9,849 combined installs across 1 indexed listing; 0 GitHub stars; MIT License; last pushed 2026-10-20. Counts drift over time.
- The index and the tree agree here: skills.sh indexes one listing named `slack-cli` and the repository holds one skill directory, `skills/slack-cli/`. That is also the whole surface, so the install number is volume from a single package rather than a suite.
- Young and unstarred. The clone is tagged v0.4.0 at HEAD with 0 stars, so flag behaviour can move between point releases; pin a version if an agent workflow depends on exact command output.
- There is no delete subcommand. Removing a botched post means calling `https://slack.com/api/chat.delete` with the token from `slack-cli auth token`, and only works for messages your token is allowed to delete.
- Bot tokens lose capability. Legacy search and unreads work best with `xoxp` or browser tokens, bots need `conversations context-search` with an action token for public channels, and saved items require `xoxc` plus `xoxd`.
- Rate limits bite on unlisted Slack apps at 1 request per minute and 15 messages per page on history and replies, and the first `cache refresh` on a cold profile crawls the whole workspace.

## Related

- [incident.io CLI - Incident and On-Call API Setup](/hermes/skills/catalog/incidentio-cli-setup)
- [Groundcover CLI - Observability API Setup Guide](/hermes/skills/catalog/groundcover-cli-setup)
- [Agent Email CLI Skill Setup](/hermes/skills/catalog/agent-email-cli-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Refresh the cache once per profile, not once per command. `slack-cli cache refresh` is the slow call that crawls users and channels; after it, name lookups and `channels list` read the shared file. Skip it with `--no-cache` only when you are passing raw IDs.
- Write message bodies to a file. `--text-file` preserves newlines, backticks and dollar signs that `-t "first\nsecond"` will mangle, and it cannot be combined with `--text`. Re-read the thread afterwards to confirm bullets did not collapse.
- Default to `text/mrkdwn` for conversational replies. The default `text/markdown` converts GitHub Markdown into Block Kit, which is not native Slack text; reserve `--blocks` for deliberately structured UI.
- Scope the write gates narrowly. `SLACK_MCP_ADD_MESSAGE_TOOL=C123,D456` limits posting to two channels, and the `!C123` form excludes one from everything else, which is the safer setting on a workspace where an agent runs unattended.
- Keep the action token in a file. `SLACK_MCP_ACTION_TOKEN_FILE` is read fresh and trimmed on each call, while `--action-token` puts a secret in shell history and process listings.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
