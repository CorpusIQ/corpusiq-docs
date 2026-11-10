---
title: "Zapier Agent Skills - Automation and App Actions"
description: "zapier/agent-skills on skills.sh: 3.1K combined installs; 7 official Zapier skills to build, inspect and repair durable Workflows"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/zapier-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "zapier", "workflow automation", "zapier sdk"]
---

# Zapier Agent Skills - Setup Guide

**Source:** [zapier/agent-skills](https://www.skills.sh/zapier/agent-skills) via skills.sh - 3.1K combined installs across 7 indexed listings; first seen 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 24 stars, MIT via LICENSE, `main` branch, last pushed 2026-10-16, 7 SKILL.md files under `skills/workflows/`, `.claude-plugin/` and `.codex-plugin/` manifests at the root, README.md at the repository root
**Category:** Workflow automation: Zapier app actions, trigger design, workflow diagnostics and cross-app data flow
**Quality Tier:** 🟡 Solid with caveats - MIT licensed official Zapier skills, mostly Pass verdicts with one Socket and one Snyk Warning in the sample.

Zapier maintains this repository for its own automation product rather than for the connector catalog. The README is explicit about the split: this is the home for non-connector skills, and per-app connector skills are distributed through a separate connectors download API instead of skills.sh. What remains here is one category called `workflows`, seven skills deep, covering the full life cycle of a durable Zapier workflow: install the toolchain, create, list, inspect history, modify and repair, plus one skill for the AI by Zapier step that lives inside a workflow.

The important framing is that these skills do not talk to the Zapier web UI. They drive the Zapier SDK CLI, which exposes an experimental Code Workflows command group, and they assume the account has been allowlisted for Zapier Workflows Early Access. The `workflows-install` skill spells the sequence out: probe for Node 18 or newer, npm and git, install or update `@zapier/zapier-sdk-cli`, check that the Code Workflows commands and their flags are visible, authenticate through a browser login, then read a workflow list to confirm Early Access. A step that fails stops the chain instead of working around it.

The repository is a generated mirror of an internal source. The README states that pull requests are not merged and that a maintainer makes the change upstream, which matters when you are deciding whether to patch a skill locally or wait for the next export.

## Installation

The documented install takes every skill in the repository:

```bash
npx skills add zapier/agent-skills
```

A single skill installs by its `name`, which is the value in the frontmatter rather than the directory name:

```bash
npx skills add zapier/agent-skills --skill <skill-name>
```

The README notes that this drops the skill into your local agent configuration, naming `.claude/skills/` and `.cursor/skills/` as examples. For local testing that should not create a public marketplace listing, it documents the telemetry opt-out:

```bash
DISABLE_TELEMETRY=1 DO_NOT_TRACK=1 npx skills add zapier/agent-skills --skill <skill-name>
```

None of that is enough to build a workflow. The skills sit on top of the Zapier SDK CLI, and `workflows-install` is the skill that puts it there. Its own steps are the authoritative install, quoted in order:

```bash
npm install -g @zapier/zapier-sdk-cli@latest
zapier-sdk login
zapier-sdk get-profile --json
```

The skill checks for Node 18 or newer, npm and git before it runs the npm install, verifies that `zapier-sdk` resolves the Code Workflows command group and the flags each skill documents, and treats a missing flag as an install failure rather than a warning. Authentication goes through the browser login flow; the skill explicitly tells the agent not to ask for a Zapier password, API key, npm token or copied auth token. It also warns that a non-interactive shell cannot complete the browser step.

The last gate is account access. `workflows-install` performs a read-only workflow list to confirm Early Access, and stops with an access message when the account is not allowlisted. Node, npm and git reinstalls do not fix that check.

## What It Provides

The threshold for this guide is zero installs, so all 7 indexed listings appear below with the install integers exactly as skills.sh reports them:

| Skill | Installs | Use For |
|---|---|---|
| workflows-doctor | 575 | Diagnosing workflow skill and SDK CLI compatibility, spotting missing SDK commands or flags and refreshing stale workflow skills after a CLI change |
| workflows-create | 548 | Building a durable Zapier workflow from natural language with `@zapier/zapier-durable` and the Zapier SDK CLI |
| workflows-list | 498 | Listing deployed durable workflows in the authenticated account through the SDK Code Workflows commands |
| workflows-modify | 494 | Editing and republishing an existing durable workflow when a Zap needs a fix, an update or a repair |
| workflows-history | 485 | Pulling run and execution history for one durable workflow to see what happened and when it fired |
| workflows-install | 474 | Installing the Zapier SDK CLI for Workflows Early Access, checking auth and access, and bootstrapping the companion skills |
| workflows-ai-by-zapier | 13 | Configuring an AI by Zapier step with runtime context, outputs, typed integration tools, public web search and a failure exit |

Seven listings, seven rows, nothing summarised away. The distribution is the interesting part: six skills sit between 474 and 575 installs and the seventh, `workflows-ai-by-zapier`, sits at 13. That is not a quality signal, it is a scope signal. The six life-cycle skills are what an agent needs to do anything at all with a workflow, so they get installed together or not at all; the AI step is a narrower job that only applies once a workflow already exists.

Two boundaries define what the suite cannot do. There is no skill for building a Zap in the classic editor, because the entire set targets durable Workflows built in code through the SDK. And there is no per-app skill, because connectors ship through a different channel: the README says an agent looking for a connector-specific skill should not expect to find it under `skills/` here. What remains is the orchestration layer, which is also the part that is hardest to write from scratch.

## Why This Matters for Hermes Agents

Automation is the job where an agent most often produces confident nonsense: it describes a Zap in fluent prose, the user builds it, and the trigger turns out to be wrong. These skills invert that by making the agent operate the real toolchain. A workflow is created, listed, modified and republished through SDK commands, so the artifact exists in the account rather than in the conversation.

The design lesson is the doctor skill. `workflows-doctor` exists because a skill written against one SDK version drifts from the CLI installed on the machine, and the symptom is a command or flag that no longer exists. Rather than letting the agent improvise a substitute, the skill compares expectations with the installed CLI and tells you to update. Any agent tooling that wraps an external CLI needs an equivalent compatibility check, or it degrades quietly the first time the CLI ships a breaking change.

The install skill is the second lesson, and it is a good model for anything credentialed. It probes the environment, installs the dependency, verifies the capability that later steps depend on, authenticates through a browser rather than a pasted secret, checks entitlement, and only then bootstraps the companion skills. Each step gates the next, and a failure stops the chain. That ordering is why the suite can be handed to an agent without a human watching every command.

The third is restraint about scope. Six of the seven skills are read, create, modify and diagnose operations on one object type. There is no attempt to cover the whole Zapier surface, no generic HTTP skill, no kitchen-sink app skill. A narrow, correct toolset beats a broad one that half works, and the install counts suggest users reward that: a repository with 24 stars has 3,087 combined installs.

The limit is real, though. If your account is not in Workflows Early Access, most of this suite cannot run, and no amount of skill reading changes that.

## Usage

| You say | What happens |
|---|---|
| "Build me a Zap that posts new Stripe payments to Slack and logs each one in a sheet" | Writes a durable workflow with `@zapier/zapier-durable`, wires the Stripe trigger to the Slack and spreadsheet steps, then republishes it through the SDK CLI |
| "What workflows do I have deployed?" | Runs the Code Workflows list command against the authenticated account and returns the durable workflows it finds |
| "This Zap stopped firing two days ago, find out why and fix it" | Reads the run history for that workflow, identifies where execution stopped, then edits and republishes the workflow with the fix |
| "Set up Zapier Workflows on this machine" | Probes Node, npm and git, installs or updates the SDK CLI, verifies the Code Workflows commands, opens the browser login, checks Early Access and installs the companion skills |
| "The workflow skill wants a flag my CLI does not have" | Runs the compatibility check, compares the installed CLI version with what the skill expects, and updates the CLI before any other step retries |
| "Add an AI step that summarises the ticket and can search the web before replying" | Configures an AI by Zapier step with runtime context, typed integration tools, public web search and a failure exit path |
| "Rename this workflow and add a filter before the Slack step" | Modifies the deployed workflow through the SDK, republishes it and confirms the new version is the one the account is running |

## Verification

The layout is `skills/workflows/<dir>/SKILL.md`, where the directory is the short name and the skill name carries the `workflows-` prefix. This one returns 200 and is the file the table lists first:

```bash
curl -fsSL https://raw.githubusercontent.com/zapier/agent-skills/main/skills/workflows/doctor/SKILL.md | head -8
```

It opens with YAML frontmatter holding `name: workflows-doctor`, the compatibility description that begins "Diagnose Zapier Workflows skill and SDK CLI compatibility", then the heading for the doctor skill. A 404 here means the `skills/workflows/` layout moved and every path in this guide needs a new segment.

After an install, the skills CLI can list what it wrote. This is the check the `workflows-install` skill itself runs:

```bash
npx skills list --json
```

That returns JSON rather than a table, so it is safe to parse. For the directory check the README names, look in the two locations it documents, relative to the project or the user home depending on how the CLI was run:

```bash
ls .claude/skills | grep '^workflows-'
ls .cursor/skills | grep '^workflows-'
```

Seven lines means the full set landed; one line means you installed a single skill by name. The CLI check is separate from the skill check and worth running on its own, because a missing command group looks like a broken skill:

```bash
zapier-sdk --version
zapier-sdk get-profile --json
```

A profile with data and no errors confirms auth. An access error on the workflow list is the Early Access gate, not a credentials problem.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| workflows-doctor | Pass | Pass | Pass |
| workflows-create | Pass | Pass | Pass |
| workflows-list | Pass | Pass | Pass |
| workflows-modify | Pass | Pass | Pass |
| workflows-history | Pass | Pass | Pass |
| workflows-install | Pass | Warn | Pass |
| workflows-ai-by-zapier | Pass | Pass | Warn |

Five of the seven are clean on all three scanners. `workflows-install` carries a Socket Warn, which fits a skill whose job is to run a global npm install and a browser login, and `workflows-ai-by-zapier` carries a Snyk Warn, which fits a skill that enables public web search inside an automation. Neither is a Fail, and both are skills you would read before running anyway.

The permission surface is the account itself. These skills create, modify and republish live automations under an OAuth grant that can reach every app the Zap is wired to. `workflows-modify` and `workflows-create` are write operations against production state, and the SDK login is a browser session on a machine where an agent is running commands. Keep the login interactive and human-completed, do not store a Zapier password or API token in a skill file or an environment variable the agent can read, and prefer a dedicated Zapier account or folder for agent-built workflows so a bad publish cannot touch the automations the business depends on.

Two supply-chain notes are worth carrying. The npm package is installed globally at `@latest`, so the CLI version moves under you; the `workflows-doctor` skill exists precisely because that drift happens. Pin a version in your own environment if you need reproducibility. And the repository is a generated mirror, so a local patch to a skill file will be overwritten by the next export; open an issue instead of editing in place.

## Limitations

- Snapshot data, verified 2026-11-09: 3,087 combined installs across 7 indexed listings; 24 GitHub stars; MIT; last pushed 2026-10-16. Counts drift over time.
- Zapier Workflows is Early Access. The install skill checks entitlement with a read-only list call and stops when the account is not allowlisted, so a large part of this suite is unusable until Zapier grants access.
- The suite covers orchestration only. Per-app connector skills are distributed through the connectors download API rather than this repository, and the README says the public GitHub home for connectors is still being set up, so there is no link to follow yet.
- The repository is a generated mirror: pull requests are not merged, and changes have to go through an issue and an upstream export. Do not plan on a local fork as a long-lived fix.
- `workflows-ai-by-zapier` at 13 installs against 474 to 575 for the rest is a scope gap, not a quality one. Nothing in the set is independently verified beyond the skills.sh verdicts, and none of the skills can be exercised without an allowlisted account.
- The skills target durable Workflows built in code. Classic editor Zaps and their trigger and action semantics are outside this set, so do not install it expecting a general Zapier assistant.

## Related

- [n8n Skills - Workflow Automation for Business](/hermes/skills/catalog/n8n-skills-setup)
- [Twilio Agent Skills - SMS, Voice and Messaging APIs](/hermes/skills/catalog/twilio-agent-skills-setup)
- [Firecrawl Workflows - Growth & Research Automation Setup](/hermes/skills/catalog/firecrawl-workflows-setup)

## Pro Tips

- Install `workflows-install` first and let it do its job. Running `npx skills add` for the other six before the SDK CLI exists produces skills that read well and fail on their first command.
- Run `workflows-doctor` after any CLI update, and before debugging a workflow that suddenly misbehaves. The compatibility check is cheaper than reading a stack trace from a renamed flag.
- Use `workflows-list` and `workflows-history` before `workflows-modify`. Reading the deployed state and the last run first is what separates a targeted fix from a rewrite.
- Keep the browser login interactive. The install skill refuses to ask for a password or token, and that refusal is the security control, not an inconvenience to route around.
- Test on a throwaway workflow in a dedicated account folder. These skills publish to live state, and there is no dry-run flag documented anywhere in the set.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
