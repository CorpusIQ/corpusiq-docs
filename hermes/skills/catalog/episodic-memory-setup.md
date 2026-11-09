---
title: "Episodic Memory - Semantic Search for Coding Agents"
description: "obra/episodic-memory on skills.sh: 9.2K combined installs; one skill that indexes past Claude Code, Codex and Cursor sessions for semantic search."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/episodic-memory-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "agent memory", "semantic search", "episodic memory"]
---

# Episodic Memory - Setup Guide

**Source:** [obra/episodic-memory](https://www.skills.sh/obra/episodic-memory) via skills.sh - 9.2K combined installs across 1 indexed listing; first seen 2026-11-08 (Nov 8, 2026 evening sweep)
**GitHub:** 499 stars, MIT via `LICENSE`, `main` branch, last pushed 2026-09-10, 1 SKILL.md directory at `skills/remembering-conversations/` with `MCP-TOOLS.md` beside it
**Category:** Memory
**Quality Tier:** 🟡 Beta - one skill, 9,225 installs, MIT license, Pass on Socket and Snyk, but Gen Agent Trust Hub returns Warn, so review before production use.

Episodic Memory indexes the coding conversations you already had and makes them searchable by meaning rather than by keyword. It reads session transcripts from Claude Code, Codex, Cursor, opencode and Oh My Pi, embeds each exchange with a local sentence-transformer model, and stores the vectors in SQLite so a query like "provider catalog" can surface a discussion about API design patterns that never used those words.

The repository is more than the skill file. There is a TypeScript core library, a unified `episodic-memory` CLI, an MCP server that exposes `search` and `read`, and harness integrations for each of the five tools it reads. The single skill, `remembering-conversations`, is the instruction layer: it tells an agent to search memory before saying "I don't know", guessing, or treating a topic as new, and it tells the agent how to dispatch a search agent or call the MCP tools directly when dispatch is not available.

## Installation

The README documents four install paths and does not publish a `skills add` line, so the commands below come from the repository rather than from the skills.sh listing.

The recommended path is the Claude Code plugin, which brings the MCP server, the session-end indexing hook and the skill in one step:

```bash
# In Claude Code
/plugin install episodic-memory@superpowers-marketplace
```

The plugin indexes conversations at the end of each session, exposes the MCP search and read tools, and makes the work searchable in natural language without further setup.

For Codex, the repository ships a plugin manifest at `.codex-plugin/plugin.json` and needs `codex-cli 0.130.0` or newer. For local testing the README builds the plugin, enables plugin hooks, and registers the checkout as a marketplace:

```bash
npm run build
codex features enable plugin_hooks
codex plugin marketplace add /path/to/episodic-memory
```

Then open `/plugins` in Codex, install and enable `episodic-memory` from `Episodic Memory Dev`, open `/hooks`, review the Episodic Memory hook, and press `t` to trust it. New hooks are listed but do not run until trusted, so the sync is silent until that step is done.

For opencode, install the package globally and add the plugin to the config file:

```bash
npm install -g github:obra/episodic-memory
```

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["episodic-memory"]
}
```

The bare npm path is the same global install, which gives you the `episodic-memory` commands without any harness plugin:

```bash
npm install -g github:obra/episodic-memory
```

All four paths write to the same archive and index, in `~/.config/superpowers` by default, so a machine can mix a Claude Code plugin with a CLI install and see one history.

## What It Provides

The threshold for this guide is zero installs, so the single indexed listing appears below:

| Skill | Installs | Use For |
|---|---|---|
| remembering-conversations | 9,225 | Making an agent search past coding conversations before answering from uncertainty, then reading the top matches and citing them |

One row clears the threshold, and since the threshold is zero no rows fall below it.

The install count is the only adoption signal here: 9,225 installs against 499 GitHub stars is an unusually wide gap, which suggests the skills.sh listing is doing most of the distribution rather than the repository. Treat the number as reach, not as evidence that anyone has run a search against a real index.

The pipeline behind the skill is five steps, and understanding it explains most of the behaviour. Sync copies new or modified transcripts from `~/.claude/projects`, `~/.claude/transcripts`, `~/.codex/sessions`, `~/.omp/agent/sessions` and `~/.cursor/projects`, and exports opencode sessions out of `~/.local/share/opencode/opencode.db` into generated JSONL. Parse extracts user and agent exchanges. Embed runs each exchange through BAAI `bge-small-en-v1.5`, quantized to q8, loaded through `@huggingface/transformers` and onnxruntime on the CPU at 384 dimensions. Index stores the vectors in SQLite with `sqlite-vec`. Search does vector similarity, exact text matching, or both.

Three details are easy to miss and change how you use it. Summaries are display-only: each sync may make up to 10 summarization calls to decorate results, and those summaries are never embedded or searched, so `EPISODIC_MEMORY_SKIP_SUMMARIES=1` removes the cost and loses only that line of context. Text search matches the whole query as one case-insensitive substring with no word splitting or stemming, which makes it right for git SHAs and error strings and wrong for descriptive phrases. And the MCP `search` tool accepts an array of 2 to 5 concepts for an AND search, so `["React Router", "authentication", "JWT"]` is one call rather than three.

There is also a per-conversation opt-out. A conversation containing the marker `<INSTRUCTIONS-TO-EPISODIC-MEMORY>DO NOT INDEX THIS CHAT</INSTRUCTIONS-TO-EPISODIC-MEMORY>` in any message is archived but never indexed. Subagent and workflow work is recorded as sidechain exchanges, searched by default and ranked just below equally relevant main-thread matches.

## Why This Matters for Hermes Agents

Most of what makes a decision good is not in the code. Code comments record what, documentation records how, and the reasoning that rejected two alternatives before picking a third usually lives in a conversation that nothing indexes. That is the gap this tool targets, and it is the same gap a Hermes agent hits every time a session starts cold and re-derives an architecture that was already settled.

The second fit is discipline, not retrieval. The skill is written as a mandate rather than a suggestion: search before saying "I don't know", before guessing, and before treating a topic as new. That phrasing travels. Even without the index, an agent that has read the skill will announce a search, check what exists, and cite a source instead of asserting from nothing, and the failure mode it removes (confident re-litigation of a settled question) is one of the more expensive ways an agent wastes a session.

The third fit is the interface. Because the retrieval surface is MCP, a Hermes agent can consume it the same way it consumes any other MCP server, with two tools and no bespoke client. The `search` tool returns ranked exchanges and the `read` tool returns one conversation as markdown, which is enough to build a citations step on top rather than trusting a summary.

The honest counterweight: Hermes is not one of the harnesses this project indexes. There is no Hermes session reader in the tree, so the archive will contain Claude Code, Codex, Cursor, opencode and Oh My Pi history, not Hermes history. The value for a Hermes agent is reading that shared history and the search-first habit, not remembering its own runs.

## Usage

| You say | What happens |
|---|---|
| "How did we handle auth in the last router migration?" | Searches past conversations semantically, reads the top matches, and answers with the decisions and the source conversations |
| "Why did we reject the queue-based approach?" | Finds the rejected alternative and returns the reasoning rather than a fresh opinion |
| "Where did we leave the indexing work?" | Recovers the last state of the task, the open questions, and the next step from the most recent matching session |
| "Find the sqlite-vec initialization error we hit" | Switches to text mode, which matches the exact string, then reads the conversation around it |
| "What did Codex decide about the plugin hooks?" | Searches across harnesses, so a decision made in one tool is visible while working in another |
| "Show me that conversation in full" | Calls the read tool, or `episodic-memory show --format html conversation.jsonl` for a browser view |
| "How much history is indexed?" | Runs `episodic-memory stats` for conversation counts, date ranges and project breakdown |

## Verification

The skill lives on `main`, so the raw path resolves directly. This one should return the file:

```bash
curl -fsSL https://raw.githubusercontent.com/obra/episodic-memory/main/skills/remembering-conversations/SKILL.md | head -20
```

It should open with YAML frontmatter naming `remembering-conversations` and a description that begins "You MUST invoke this skill before saying", followed by the core principle "Search before reinventing". If you get a 404, the skill directory moved and the path in this guide is stale.

Confirm the reference file ships beside it, because the skill points at it for the full tool API:

```bash
curl -fsSL https://raw.githubusercontent.com/obra/episodic-memory/main/skills/remembering-conversations/MCP-TOOLS.md | head -20
```

After install, the cheapest end-to-end check is a real index rather than a version string:

```bash
episodic-memory sync
episodic-memory stats
episodic-memory index --verify
```

`stats` should report a non-zero conversation count with a date range that matches your actual work, and `index --verify` should report a healthy index. If the count is zero, the transcripts are not where the sync expects them, and `episodic-memory doctor codex` or `episodic-memory doctor opencode` will say which path failed.

The final check is retrieval quality on something you know the answer to: search for a decision you remember making, and confirm the right conversation comes back in the top few results. A search that returns nothing useful with a non-zero index usually means the query was too short to embed well, so try a full phrase instead of one word.

## Security

skills.sh verdicts for the sampled skill (verified 2026-11-08) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| remembering-conversations | Warn | Pass | Pass |

The Warn verdict from Gen Agent Trust Hub means the skill should be reviewed before production use, and it reads local conversation history, which is sensitive data.

That is the right framing, because the skill file itself is markdown and the payload is your transcript archive. The archive is plaintext JSONL under `~/.config/superpowers`, which means every past conversation, including anything pasted into one, sits on disk in readable form with whatever permissions your user account has. Backups of that directory inherit the same content, and so does any sync tool pointed at the home directory. Decide that deliberately before indexing a machine that handles production credentials.

The second surface is summarization, which is the only part that sends data off the machine. By default it uses your existing Claude Code authentication, Codex sessions are summarized through `codex app-server`, and the README documents an Anthropic-compatible endpoint plus AWS Bedrock as alternatives. If `ANTHROPIC_API_KEY` is set without an endpoint override, summaries bill the metered API instead of the subscription, and the tool prints a one-time warning unless `EPISODIC_MEMORY_ALLOW_METERED_API=1`. Embeddings and search stay local. If the conversation content must not leave the host, `EPISODIC_MEMORY_SKIP_SUMMARIES=1` disables that pass and leaves search working.

The dependency chain is the usual one for a Node tool of this shape: `better-sqlite3`, `sqlite-vec`, `onnxruntime-node` and `@huggingface/transformers`, several of which need native builds. The repository whitelists install scripts for `better-sqlite3` and `onnxruntime-node` and blocks `sharp`, so an install that runs arbitrary postinstall scripts is a wider surface than the two scanners are measuring.

## Limitations

- Snapshot data, verified 2026-11-08: 9,225 combined installs across 1 indexed listing; 499 GitHub stars; MIT license; last pushed 2026-09-10. Counts drift over time.
- The index is a local SQLite database plus a JSONL archive under `~/.config/superpowers` by default, and it grows with your history. Nothing prunes it for you, and a sync run embeds new exchanges one at a time on the CPU, so a large first import takes real time.
- Embedding runs against `bge-small-en-v1.5` at q8, 384 dimensions, through `@huggingface/transformers`. The weights are fetched and cached on first use, so the first sync needs network access and later runs do not, and a fully offline machine needs that cache warm before indexing.
- It searches local history only. There is no shared or remote index, two machines do not see each other, and the only sources it reads are Claude Code, Codex, Cursor, opencode and Oh My Pi. Hermes session history is not a supported source.
- Summaries depend on Claude Code authentication, `codex-cli 0.130.0` or newer, or an Anthropic-compatible endpoint. Without one of those, summaries fail and the README says sync falls back to transcript-text summarization.
- 1 indexed listing and 1 SKILL.md directory match, so there is no directory drift, but there is also no second listing to cross-check the install count against.

## Related

- [Basic Memory Skills Setup Guide for Hermes Agents](/hermes/skills/catalog/basic-memory-skills-setup)
- [Hermes Advanced Memory - Setup Guide](/hermes/skills/catalog/hermes-advanced-memory-setup)
- [AgentMemory Setup - Persistent Memory for Hermes Agents](/hermes/skills/catalog/agentmemory-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `episodic-memory sync` once by hand before trusting the hook. The plugin path makes indexing automatic, which also makes it invisible, and a manual run tells you whether the transcripts were found.
- Use a full phrase for semantic queries and an exact string for text queries. `"why did we move off sqlite-vec"` belongs in vector mode; a commit SHA belongs in text mode, where the whole query has to appear contiguously.
- Put the exclusion marker in a conversation before you do sensitive work in it. The exclusion is decided at index time on any message, so adding it later means reindexing rather than editing a record.
- Set `EPISODIC_MEMORY_SKIP_SUMMARIES=1` on a machine that should not call an external model. Search is unaffected because summaries are never embedded, and it removes both the latency and the billing question in one flag.
- Search with an array when you need all concepts present. A single string blends them; a 2 to 5 element array turns the query into an AND and is the correct shape for "this library, this problem".
- Check `episodic-memory index --verify` after an upgrade. The encoder was migrated from `all-MiniLM-L6-v2` to `bge-small-en-v1.5` with the same 384 dimensions, and a half-migrated index is the one failure that looks like bad ranking rather than an error.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
