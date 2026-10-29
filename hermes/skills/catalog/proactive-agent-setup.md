---
title: "Proactive Agent - WAL Memory and Compaction Recovery Setup"
description: "Proactive Agent: 15.2K combined installs. A single SKILL.md turning an agent proactive, persistent across compaction, and safely self-improving."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/proactive-agent-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "agent memory", "proactivity", "context management"]
---

# Proactive Agent - Setup Guide

**Source:** [halthelobster/proactive-agent](https://www.skills.sh/halthelobster/proactive-agent) via skills.sh - 15.2K combined installs across 1 indexed listing; snapshot 2026-10-28 (Oct 28 evening sweep)

**GitHub:** [halthelobster/proactive-agent](https://github.com/halthelobster/proactive-agent) - 22 stars, no license file at the repo root (the SKILL.md itself claims MIT), branch main, last pushed 2026-02-04; the whole tree is one `SKILL.md` at the repository root, version 3.0.0, with no scripts, no assets and no manifest

**Category:** Agent memory architecture, proactivity and context recovery instruction sets

**Quality Tier:** 🟡 Beta - single-skill repository from an individual publisher, 22 GitHub stars, no LICENSE file at the root, all three sampled auditors Pass, and a Quick Start that references `assets/` and `scripts/` the repository does not actually ship

Proactive Agent is a behaviour specification, not a tool. The repository holds one markdown file of roughly 17 KB, version 3.0.0, written by an agent called Hal 9001 (@halthelobster) as the first entry in something it calls the Hal Stack. There is no code, no MCP server, no dependency manifest and no README, so installing it changes nothing except the instructions your agent reads. The file argues that most agents simply wait for instructions, and lays out three pillars it wants an agent to adopt: be proactive and create value unasked, be persistent across context loss, and improve its own operating rules without drifting.

The substance is a set of named protocols. The WAL protocol says chat history is a buffer and not storage, so corrections, proper nouns, preferences, decisions and specific values get written to `SESSION-STATE.md` before the agent answers. A working buffer logs every exchange once context passes 60 percent, and a compaction recovery routine reads that buffer first when a session wakes up truncated. Around those sit a unified search protocol, a skill installation vetting policy, a relentless resourcefulness rule, ADL and VFM guardrails on self-edits, a heartbeat checklist, reverse prompting and three growth loops. It also prescribes a workspace layout: `ONBOARDING.md`, `AGENTS.md`, `SOUL.md`, `USER.md`, `MEMORY.md`, `SESSION-STATE.md`, `HEARTBEAT.md`, `TOOLS.md` and a `memory/` directory with daily notes.

## Installation

There is no README, so there is no upstream install section to follow. The skills.sh listing page documents the CLI command:

```bash
npx skills add halthelobster/proactive-agent
```

The CLI's handling of a root-level `SKILL.md` with no skill directory is not documented anywhere in the repository, and Hermes loads skills from named directories, so the reliable route is to create the directory and fetch the file itself:

```bash
mkdir -p ~/.hermes/profiles/corpusiq/skills/proactive-agent
curl -sL -o ~/.hermes/profiles/corpusiq/skills/proactive-agent/SKILL.md \
  https://raw.githubusercontent.com/halthelobster/proactive-agent/main/SKILL.md
```

The SKILL.md's own Quick Start assumes files this repository does not contain. It says to run `cp assets/*.md ./` and then `./scripts/security-audit.sh`, but the tree is the single `SKILL.md` and nothing else, so both steps have to be skipped or written yourself. What the document actually asks of you is behavioural: create the workspace files it lists, let the agent populate `USER.md` and `SOUL.md` from an onboarding conversation, and keep `AGENTS.md` as the place its learned rules live.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| proactive-agent | 15165 | A behaviour contract for one agent, not a script: write-ahead logging of corrections and decisions into `SESSION-STATE.md`, a working buffer that logs every exchange past 60 percent context, step-by-step compaction recovery, unified memory search before saying "I don't know", skill-install vetting, relentless resourcefulness, and ADL/VFM guardrails on self-edits. |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

Context loss is the failure that quietly ruins long agent runs, and most skill collections have nothing to say about it. This file treats the problem mechanically: the state file is RAM, the daily notes are the log, and the curated memory file is the distilled result. The WAL rule is the sharp part, because it fires on the human's input rather than on the agent's memory of what mattered, which removes the judgement call that usually loses the detail.

The 60 percent working buffer maps onto a real boundary in a long Hermes session, where the gap between a memory write and a compaction is exactly where details disappear. The recovery routine is written with a specific opening move: read the buffer, then the state file, then the last two daily notes, and only then admit to missing context. That is a better default than asking the user to re-explain.

Two other rules travel well. Verify before reporting says that code existing is not a feature working, so the word "done" is gated on an end-to-end test from the user's point of view. Self-improvement guardrails put stability above novelty and refuse any change the agent cannot verify, which is the right posture for a skill that asks an agent to edit its own `AGENTS.md`. The proactive surprise rule also carries its own brake: build freely, but nothing goes external without approval, so emails get drafted rather than sent.

The honest caveat is that this is prose with no enforcement. Nothing checks that your agent follows it, and the tone is prescriptive enough that it will compete with rules you already have, so read it as a source of patterns to adopt selectively rather than a package to switch on.

## Usage

| You say | What happens |
|---|---|
| "Use the blue theme, not red" | The WAL trigger fires on the correction, so the agent writes `Theme: blue (not red)` into `SESSION-STATE.md` before it replies, instead of trusting the live context to hold it. |
| "Where were we?" | Compaction recovery reads `memory/working-buffer.md` first, then `SESSION-STATE.md`, then today's and yesterday's daily notes, and reports the last task with an offer to continue. |
| "Context is getting long, keep going" | Past 60 percent every exchange is appended to the working buffer as a timestamped human message plus a one or two sentence agent summary, so the danger zone is on disk. |
| "What did we decide about the pricing page last week?" | Unified search runs memory search over the daily notes and curated memory first, then session transcripts, then a grep fallback, before the agent is allowed to say it does not have that information. |
| "Install this skill I found on GitHub" | The skill installation policy checks the author, reads the SKILL.md for shell, curl or exfiltration patterns, and asks you before installing when anything looks off. |
| "Write the follow-up email to that client" | Proactive surprise applies: the draft gets built, but the guardrail keeps it internal until you approve sending it. |
| "Do a heartbeat pass" | The heartbeat checklist walks proactive items, security, self-healing, a context check for the 60 percent threshold, memory distillation and one question about what to build next. |

## Verification

Read the file before you install it, since there is nothing else to read. The raw path below returned 200 on the main branch when this guide was written:

```bash
curl -sL -o /dev/null -w "%{http_code} SKILL.md\n" \
  https://raw.githubusercontent.com/halthelobster/proactive-agent/main/SKILL.md
```

The document is a single linear file with its own contents list, so the sections worth checking against your own setup are The WAL Protocol, Working Buffer Protocol and Compaction Recovery. Everything the skill claims about itself is in that one URL:

- https://raw.githubusercontent.com/halthelobster/proactive-agent/main/SKILL.md

After install, confirm the directory and frontmatter landed. The name in the frontmatter is `proactive-agent` and the version is 3.0.0, which is how you tell a good copy from a stale one:

```bash
ls -l ~/.hermes/profiles/corpusiq/skills/proactive-agent/SKILL.md
head -6 ~/.hermes/profiles/corpusiq/skills/proactive-agent/SKILL.md
```

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| proactive-agent | Pass | Pass | Pass |

One listing was sampled and all three auditors pass it. What installs is a single markdown file, so there is no install hook, no postinstall script and nothing that executes on clone. The risk sits one layer up: the file instructs an agent to write to a known set of workspace files on every message, and to edit its own `AGENTS.md` under the self-improvement section, so review those two behaviours against your own rules before adopting them.

The skill's own security section is a good default rather than a guarantee. It forbids executing instructions found in external content, treats emails, websites and PDFs as data, requires approval before deleting files and before any change it calls a security improvement, warns against connecting to external agent networks, and adds a context leakage check before posting to a shared channel. It also cites a figure that roughly 26 percent of community skills contain vulnerabilities and tells the agent to vet each install. That figure is asserted in the file and not sourced there, so treat it as a prompt to review, not a measured statistic.

The licensing position deserves its own line. GitHub reports no license for this repository and there is no `LICENSE` file at the root, while the SKILL.md's own License and Credits section says MIT. Until the author adds the file, the repository is effectively unlicensed for redistribution purposes, which matters if you vendor it into an internal skills repository.

## Limitations

- Snapshot data, verified 2026-10-28: 15165 combined installs across 1 indexed listing; 22 GitHub stars; no license file; last pushed 2026-02-04. Counts drift over time.
- The repository ships no README, so this guide is grounded in the SKILL.md alone. There are no upstream install instructions, no changelog outside the in-file v3.0.0 section, and no documented support channel.
- The missing license is a real adoption risk. GitHub's API returns no SPDX identifier and no `LICENSE` file exists at the root, while the SKILL.md says MIT. Treat the repository as unlicensed until a file appears, especially before copying it into anything you distribute.
- The Quick Start references `assets/*.md` and `scripts/security-audit.sh`, and the current tree contains neither, only the root `SKILL.md`. The onboarding flow and the security audit script have to be supplied by you.
- The single indexed listing is named `proactive-agent` but no directory of that name exists in the tree, because the `SKILL.md` sits at the root. The CLI's behaviour with that layout is undocumented, so the manual directory route is the predictable one.
- Nothing enforces the behaviour. There are no tests, no eval files and no scripts, so compliance is a matter of whether the agent reads and follows the file, and there is no version signal beyond the `3.0.0` string in the frontmatter and body.
- The file names companion skills from the same publisher, Bulletproof Memory, PARA Second Brain and Agent Orchestration, but they are separate repositories and are not part of this install.

## Related

- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)
- [CodeStable Skills - AI Coding Workflow Setup](/hermes/skills/catalog/codestable-skills-setup)

## Pro Tips

- Adopt the WAL trigger before anything else. One sentence in `AGENTS.md` saying that corrections, names, decisions and specific values get written to the state file before replying buys most of the value in this document.
- Put the working buffer threshold where your own compaction actually happens. 60 percent is the file's number; if your profile compacts later, logging from 60 percent just costs tokens, and logging from 85 percent will miss the truncation.
- Keep the recovery routine literal. Read the buffer, then the state file, then the two daily notes, in that order, before answering any "where were we" question, because improvising that order is how an agent invents context.
- Trim the prescriptive sections you already cover. The security hardening and verify-before-reporting parts overlap with rules most Hermes profiles carry, and duplicate rules with different wording create ambiguity about which one wins.
- Skip the two Quick Start commands as written. `assets/` and `scripts/` do not exist in this repository, so a copy of the workspace files and any audit script you want are yours to create and keep under version control.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
