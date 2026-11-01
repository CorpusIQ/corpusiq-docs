---
title: "AgentMail Skills - Agent Email Inbox Setup"
description: "agentmail-to/agentmail-skills: 10.7K combined installs. Eleven skills for agent inboxes, the AgentMail SDK, CLI, MCP server and email threat model."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agentmail-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "email", "mcp", "agent identity"]
---

# AgentMail Skills - Setup Guide

**Source:** [agentmail-to/agentmail-skills](https://www.skills.sh/agentmail-to/agentmail-skills) via skills.sh - 10.7K combined installs across 11 indexed listings; first seen 2026-11-01 (morning sweep)

**GitHub:** [agentmail-to/agentmail-skills](https://github.com/agentmail-to/agentmail-skills) - 25 stars, no licence file at the repository root, branch main, last pushed 2026-10-27; 11 `SKILL.md` files, one per top-level directory, alongside `scripts/`, `tests/`, `evals/`, `backend-contract.json` and the `skills.json` and `skills.sh.json` manifests

**Category:** Agent email operations: inbox lifecycle, sending, triage, SDK and CLI usage, MCP connection setup, framework toolkits and agent account creation

**Quality Tier:** 🟡 Yellow - Gen Agent Trust Hub and Socket pass on all three sampled skills, but Snyk returns a Warn on `agentmail` and `agentmail-cli` (code W011 on both), and the repository ships no LICENSE file

This is the canonical skill set for AgentMail, an API-first email platform built for agents, and the README says as much: skills are authored here and every other first-party copy is generated from this repository. The eleven skills divide cleanly. Four act on a mailbox (`agentmail-check-email`, `agentmail-send-email`, `agentmail-manage-inboxes`, `agentmail-agentid`), three are for building against the platform (`agentmail` for the SDK, `agentmail-cli` for the shell, `agentmail-toolkit` for framework adapters), one configures the hosted MCP server (`agentmail-mcp`), one carries the architecture and threat model (`agent-email-patterns`), and two are deprecated aliases kept so pinned URLs resolve.

The action skills are unusual in that they ship an authorization contract rather than only instructions. Each carries a matrix naming what authorises an action, what does not, and what safeguards apply: a draft is not authorisation to send, a send with an inferred recipient needs a preview and confirmation, a retry after an ambiguous timeout must reconcile state first, and content arriving in email never authorises anything. The SDK skill is the other half, a list of API traps that cost real debugging time, including no per-message delete, no subject parameter on reply, an add-or-remove-only webhook update, and a thread list that ignores a pod filter.

## Installation

The README documents the skills CLI and a Claude Code plugin:

```bash
npx skills add agentmail-to/agentmail-skills
npx skills add agentmail-to/agentmail-skills --skill agentmail
```

```text
/plugin install agentmail@agentmail
```

The README also states that `npx skills add` tracks `main`, so an install is a moving target rather than a pinned release. For a Hermes profile the copy route works the same way, and it is worth selecting rather than taking all eleven, since two of them are aliases:

```bash
git clone --depth 1 https://github.com/agentmail-to/agentmail-skills.git /tmp/agentmail-skills
cp -r /tmp/agentmail-skills/agentmail/. ~/.hermes/profiles/corpusiq/skills/
```

Either route only installs instructions. The skills need an AgentMail account and an `AGENTMAIL_API_KEY` before any of them can act on a mailbox, and the MCP skills assume a host that can register a remote server.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| agentmail | 2,966 | Building against the AgentMail TypeScript or Python SDK: inboxes, messages, threads, drafts, attachments, domains, allow and block lists, pods, webhooks and deliverability triage. |
| agentmail-cli | 1,663 | Shell operations for the official CLI: list and create inboxes, read and search mail, send, reply, forward, manage drafts, and emit JSON, JSONL or YAML for scripting. |
| agentmail-mcp | 1,158 | Configuring or debugging the hosted MCP server in Claude Code, Codex, Cursor, Claude.ai or ChatGPT, including OAuth, API key headers and connection failures. |
| agentmail-toolkit | 1,015 | Wiring mail tools into Vercel AI SDK, LangChain, OpenAI Agents SDK, LiveKit Agents or your own MCP server, in TypeScript or Python. |
| agent-email-patterns | 872 | Architecture decisions for agent email: dedicated inboxes, provider tradeoffs, conversation loops, human-in-the-loop drafts, event design and the prompt injection threat model. |
| email-for-ai-agents | 816 | Deprecated alias of `agent-email-patterns`, an identical generated copy kept so existing installs and pinned URLs resolve. |
| agentmail-sdk | 757 | Deprecated alias of `agentmail`, an identical generated copy kept so existing installs and pinned URLs resolve. |
| agentmail-check-email | 464 | Reading, searching, summarising and triaging inboxes through MCP, with pagination, label state and a spam and unauthenticated check. |
| agentmail-send-email | 451 | Drafting, sending, replying and forwarding through MCP, with an explicit preview and confirm rule for any inferred field. |
| agentmail-manage-inboxes | 441 | Creating, listing, inspecting, updating and deleting inboxes, with confirmation required before a destructive delete. |
| agentmail-agentid | 102 | Creating accounts for an agent at third-party services with AgentID, using an inbox as the identity, and listing where each inbox already has an account. |

No indexed listings fall below the threshold; all 11 appear above.

## Why This Matters for Hermes Agents

Email is the tool most agents are given first and the one that does the most damage when it goes wrong, because a send is irreversible and a mailbox is an inbound channel for instructions. This pack addresses both halves. The architecture skill argues against the common shortcut of granting an agent OAuth access to a human mailbox, on the grounds that typical scopes reach the entire history, that a crafted email already in the mailbox becomes an attack surface, that revocation cannot be scoped per workflow, and that agent and human actions share one audit trail. Its recommendation is one dedicated API-native inbox per agent.

The action skills take the next step and write the authorisation rules down. That matters mechanically: an agent asked to "send the client an update" will otherwise infer a recipient and a body and proceed. Here the default is a draft, a send needs explicit fields or a preview, and content that arrived by email is never authority. Those three rules remove most of the ways an agent turns an inbound message into an outbound commitment.

The SDK and CLI skills carry hard-won API detail that is hard to rediscover. Knowing that a list call returns metadata only, that a reply must be threaded with a message ID rather than a thread ID, or that `extracted_text` strips the quoted chain, saves a debugging loop on every implementation and prevents the most common failure in a reply loop, which is re-processing the entire quoted history on each turn.

For a builder, the toolkit skill is the shortest path from a model to a working mail action in a framework that already exists, and the AgentID skill is the interesting edge case: an agent that can sign itself up for a third-party API using its inbox as identity is a genuinely different shape of autonomy, and the skill is written to require an explicit account check before creating a second account at the same app.

## Usage

| You say | What happens |
|---|---|
| "Any new mail that needs a reply?" | `agentmail-check-email` resolves the inbox, searches, follows pagination, fetches full bodies, groups results into urgent, needs reply, waiting and FYI, and updates labels so the same mail is not reviewed twice. |
| "Reply to the last message from Dana and confirm the Tuesday call" | `agentmail-send-email` fetches the thread, picks the message ID, drafts the reply and shows it for confirmation when any field was inferred. |
| "Give my agent its own email address" | `agentmail-manage-inboxes` creates the inbox with a stable client ID, then reports the address and tells the user it is the agent's own address rather than theirs. |
| "Connect AgentMail to Cursor" | `agentmail-mcp` adds the hosted streamable HTTP server, prefers OAuth, and falls back to an `x-api-key` header instead of a query string. |
| "Our agent should not read a human's Gmail" | `agent-email-patterns` lays out the over-permissioning, injection and revocation arguments and the provider constraints behind the one-inbox-per-agent recommendation. |
| "Add mail tools to our LiveKit voice agent" | `agentmail-toolkit` wires the Python toolkit into the agent and enumerates the installed tool catalog at runtime. |
| "Sign my agent up for a web scraping API" | `agentmail-agentid` finds the app, checks for an existing account, shows the identity it will use, and creates the account with the inbox as the sign-in. |

## Verification

The raw path for the SDK skill returned HTTP 200 on branch main when this guide was written on 2026-11-01:

```bash
curl -sL -o /dev/null -w "%{http_code} agentmail\n" \
  https://raw.githubusercontent.com/agentmail-to/agentmail-skills/main/agentmail/SKILL.md
```

Expect `200`. After the clone, confirm that all eleven skill directories arrived and that the aliases are byte-identical to their replacements:

```bash
find /tmp/agentmail-skills -maxdepth 2 -name SKILL.md | wc -l
head -4 /tmp/agentmail-skills/agentmail/SKILL.md
diff -q /tmp/agentmail-skills/agentmail/SKILL.md /tmp/agentmail-skills/agentmail-sdk/SKILL.md
```

The count should print 11, the header should show `name: agentmail` with a `description:` line before the closing frontmatter, and the diff should report no differences. A diff that reports differences means the alias has drifted from its replacement, which the README says should not happen.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| agentmail | Pass | Pass | Warn |
| agentmail-cli | Pass | Pass | Warn |
| agentmail-mcp | Pass | Pass | Pass |

Both warnings carry Snyk code W011, and both land on the two skills that tell an agent to install and execute something: `agentmail` runs `npm install agentmail` or `pip install agentmail`, and `agentmail-cli` runs `npm install -g agentmail-cli` and then shell commands. That is the most plausible reading of a dependency and execution warning, and it is a fair one: those skills add a third-party package to the runtime on the strength of a markdown instruction. Pin versions and install from a reviewed lockfile rather than letting an agent run the install line as written.

The repository itself carries build machinery (`scripts/`, `tests/`, `evals/`, a backend contract file and two skill manifests) that is used to regenerate and validate skills, not to run at skill load. The more important security property is that the skills treat inbound mail as untrusted input by design, with an explicit rule that content arriving from email, attachments, webhooks, quoted text or tool output never authorises an action on its own. Treat that as policy the model is asked to follow rather than a control that is enforced: pair it with a gateway or proxy that holds the API key and refuses sends the agent was not granted, or run the inbox with drafts only until the loop has proven reliable.

The MCP skill is careful about credentials in a way worth copying, recommending OAuth where available and an `x-api-key` header otherwise, and explicitly discouraging the query parameter form because keys end up in logs and history. Note also that connector configuration on a hosted client is not synced to a local client, so a single sign-in does not cover both.

## Limitations

- Snapshot data, verified 2026-11-01: 10,705 combined installs across 11 indexed listings; 25 GitHub stars; no LICENSE at the repository root; last pushed 2026-10-27. Counts drift over time.
- The 11 listings and 11 skill directories match, but two listings are deprecated aliases of others: `agentmail-sdk` duplicates `agentmail` and `email-for-ai-agents` duplicates `agent-email-patterns`. Installing both of a pair gives the agent the same instructions twice, and their 1,573 combined installs inflate the total without representing distinct capability.
- No licence file at the repository root. The README invites PRs and describes exports into other repos but says nothing about reuse terms, so treat redistribution as unresolved until a licence is published.
- Nothing works without an AgentMail account and an API key. Every action skill assumes a live inbox and a connected MCP server, so the pack is inert documentation until that account exists.
- The action skills are written for hosts that can add a remote MCP server with OAuth, and name Claude Code, Codex, Cursor, Claude.ai and ChatGPT. Registering the server in another client is not covered, so expect to translate the connection step.
- Install counts are heavily skewed: `agentmail` at 2,966 is 29 times `agentmail-agentid` at 102, and the four action skills sit below 500 despite being the ones most agents need.

## Related

- [Agent Email CLI Skill Setup](/hermes/skills/catalog/agent-email-cli-setup)
- [Imap Smtp Email Setup](/hermes/skills/catalog/imap-smtp-email-setup)
- [Composio - SDK Monorepo and Agent Toolkit Setup Guide](/hermes/skills/catalog/composiohq-composio-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `agentmail` and `agent-email-patterns` first. One gives the API surface, the other gives the architecture and threat model, and the action skills assume both.
- Skip `agentmail-sdk` and `email-for-ai-agents` unless something already pins their URLs. The README says they are identical generated copies, so loading them costs context and buys nothing.
- Load `agentmail-check-email` by default in any profile with a mailbox. Its description is written to trigger on the smallest request ("any new mail?") because triage without pagination and label updates is how a loop reprocesses the same thread.
- Configure the MCP server with OAuth or an `x-api-key` header, never the `apiKey` query parameter. Keys in URLs end up in client logs and shell history.
- Ask for the gotcha list before writing SDK code. "What are the AgentMail API traps" returns the delete, reply subject, webhook update, pod filter and pagination cases in one pass, which is cheaper than debugging them one at a time.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
