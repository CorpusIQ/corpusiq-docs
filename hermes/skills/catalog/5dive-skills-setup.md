---
title: "5dive Skills - Knowledge Compile and Dev Loop Setup"
description: "5dive-ai/skills on skills.sh: 7.3K combined installs across 17 listings; runtime CLI, knowledge compilation, deep research, review and loops."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/5dive-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "agent runtime", "knowledge base", "loops"]
---

# 5dive Skills - Setup Guide

**Source:** [5dive-ai/skills](https://www.skills.sh/5dive-ai/skills) via skills.sh - 7.3K combined installs across 17 indexed listings; first seen 2026-11-05 (Nov 5, 2026 morning sweep)
**GitHub:** 1 star, MIT licence, last pushed 2026-11-03, 16 skill directories at the repository root with one SKILL.md each
**Category:** Agent runtime operations, knowledge compilation, research, review and loop authoring
**Quality Tier:** 🟡 Beta - Gen Agent Trust Hub Warn on 5dive-cli; MIT; 1 star.

5dive publishes drop-in SKILL.md bundles aimed at Claude Code, openclaw, Hermes and any harness that loads skills.sh format prompts. The set splits into two layers. The first operates the 5dive runtime itself: `5dive-cli` spawns, messages and tears down sibling agents on the same host and works the shared task queue, `5dive-cli-extras` covers administration beyond that, and `diagnose` runs auth, service, disk, memory and skill-integrity checks on the VM and returns a root-cause report.

The second layer is portable and runs in any agent: `compile-knowledge` for interlinked markdown memory, `deep-research` for cited synthesis, `code-review`, `verify` and `playwright-e2e` for proof of work, `copywriting` and `ad-creative` for marketing copy, `no-ai-slop` for editing, and `loops` plus `find-loops` for scheduled agents. The README names `openagent` and `loops` as the best starting points because neither needs a 5dive account.

## Installation

The README installs single skills through the open `skills` CLI, which works across Claude Code, Codex, Cursor and any harness that loads SKILL.md:

```bash
npx skills add 5dive-ai/skills --skill openagent
npx skills add 5dive-ai/skills --skill loops
npx skills add 5dive-ai/skills --skill zero-human-dev-team
```

The whole set installs with a wildcard:

```bash
npx skills add 5dive-ai/skills --skill '*'
```

On a 5dive runtime host, the README documents the platform command and a fully specified upstream call:

```bash
sudo 5dive agent skill <agent-name> add \
  --source=5dive-ai/skills \
  --skill=5dive-cli
```

```bash
npx skills add https://github.com/5dive-ai/skills --skill 5dive-cli --agent claude-code --yes
```

The dashboard equivalent is Agents, then Connect skills, then 5dive-cli, then Install.

## What It Provides

Fourteen listings clear the 10-install threshold.

| Skill | Installs | Use For |
|---|---|---|
| 5dive-cli | 3,271 | Spawning, inspecting, messaging and tearing down sibling agents on the local 5dive runtime, plus the shared task queue |
| compile-knowledge | 2,418 | Compiling a decision record, cause or gap analysis into atomic markdown files with wiki-links and a maintained index |
| openagent | 1,261 | Writing and validating a persona yaml, checking its rarity tier, rendering the shareable holo card and opening a registry PR |
| deep-research | 193 | Multi-source research that judges source quality, adversarially verifies each key claim and states confidence |
| no-ai-slop | 19 | Editing a draft into sharper, more direct prose, or detecting AI-slop patterns without rewriting |
| diagnose | 18 | Root-cause diagnosis on a 5dive VM: auth state, service health, disk, memory, recent CLI errors, skill integrity |
| ad-creative | 17 | Ad headlines, descriptions, primary text and full variations, refined against real performance data |
| loops | 14 | Authoring or editing a LOOP.md that holds a trigger, its skills and a prompt in one portable file |
| verify | 13 | Grading a delivered claim against the artifact, with a pass, fail or not-reached verdict and unchecked items named |
| playwright-e2e | 13 | Playwright specs, authenticated page drives, screenshots and CI runs that prove a web change works |
| find-loops | 13 | Searching the agenticloops.dev directory for an existing recurring agent and installing it |
| copywriting | 13 | Homepage, landing, pricing and feature copy: headlines, CTAs, value propositions and hero sections |
| code-review | 13 | Reviewing a diff or PR for logic bugs, races, missing tests and API misuse, with an approve or request-changes verdict |
| 5dive-cli-extras | 11 | Runtime administration beyond delegation: auth recovery, fleets, live screens, governance, plugins, host remediation |

The remaining 3 indexed listings sit below the threshold at 2, 1 and 1 installs: zero-human-dev-team (2), ai-dev-team (1) and caveman-marketing (1). ai-dev-team has no matching directory in the repository, which holds 16 skill directories against 17 indexed listings.

## Why This Matters for Hermes Agents

A skill's name and description are loaded at selection time, in every session, whether or not the skill fires. This repository is built around that cost: the README caps every description at two discriminating sentences, holding the capability, the activation condition and at most one exclusion, and pushes command catalogs into the skill body or its references. For an agent carrying dozens of skills that is the difference between a selector that routes correctly and one that pays a token tax on every turn.

The activation conditions are written to be narrow on purpose. `diagnose` is for a suspect 5dive runtime, not for a failing build or a failing test. `compile-knowledge` fires when persistence is asked for explicitly or when the work produced a decision record, a cause or a gap analysis, not on every factual answer. `find-loops` handles discovery while `loops` handles authoring, so a request to schedule something does not load the wrong half.

The proof-of-work skills are the reusable part. `verify` grades a claim against the artifact rather than against the report of it and emits a three-state verdict with the unchecked parts stated, which is the failure mode behind most confident "it works" messages. `code-review` puts correctness ahead of quality with a severity model. `playwright-e2e` proves a web change in a real browser instead of a unit test.

The repository also ships `evals/routing.json`, behavioural routing cases that guard the boundaries the description cap exists to protect. That is a pattern worth copying: skills that can be mis-selected need regression tests, not just prose.

## Usage

| You say | What happens |
|---|---|
| "Save this decision and the reasons behind it" | compile-knowledge writes atomic files with wiki-links and updates the index |
| "Research the options and tell me how confident you are" | deep-research fans out across sources, verifies key claims and reports per-claim confidence |
| "Review this PR before I merge it" | code-review works the diff for correctness, then quality, and returns a verdict |
| "Prove the fix actually works in the browser" | playwright-e2e writes a spec, drives the page and captures screenshots |
| "Did this task really get done?" | verify grades the claim against the artifact and names what it could not check |
| "Message the other agent and get its status" | 5dive-cli sends to the sibling agent and reads the shared task queue |
| "Schedule a recurring agent that checks this weekly" | find-loops looks for an existing loop, then loops authors or edits the LOOP.md |

## Verification

Confirm the raw file the installer pulls before trusting the description:

```bash
curl -fsSL https://raw.githubusercontent.com/5dive-ai/skills/main/compile-knowledge/SKILL.md | head -6
```

It should open with `name: compile-knowledge` and a description naming interlinked markdown, atomic files and a maintained index. The same check on the runtime skill:

```bash
curl -fsSL https://raw.githubusercontent.com/5dive-ai/skills/main/verify/SKILL.md | head -8
```

It should name the three-state verdict. Then confirm the install landed as one directory per skill in the skills directory your installer targets:

```bash
ls ~/.claude/skills | grep -E '5dive|compile-knowledge|code-review'
```

From a clone, the repository enforces its own description budget:

```bash
./scripts/check-descriptions.sh
```

That script prints the total characters and fails when a description breaks the two-sentence cap.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| 5dive-cli | Warn | Pass | Pass |
| compile-knowledge | Pass | Pass | Pass |
| verify | Pass | Pass | Pass |
| caveman-marketing | Pass | Pass | Pass |

`5dive-cli` is the one flagged skill and it is also the one that spawns, messages and tears down other agents on the host. Read it before granting unattended use on a shared runtime.

## Limitations

- Snapshot data, verified 2026-11-05: 7,291 combined installs across 17 indexed listings; 1 GitHub star; MIT; last pushed 2026-11-03. Counts drift over time.
- The index outruns the tree by one: 17 indexed listings against 16 skill directories. `ai-dev-team` (1 install) has no matching directory in the current repository.
- `caveman-marketing` sits below the table threshold at 1 install but is documented in the README as the three-second ad and landing page cut, with a word-and-button checker.
- The runtime skills assume a 5dive VM. `5dive-cli` and `diagnose` call the local 5dive CLI and its host services, so on a plain Hermes host they load as prompts but their commands will not resolve.
- Descriptions are capped at two sentences by design, so a description never lists a skill's commands. Read the SKILL.md body before scripting a specific subcommand.
- With 1 star and a last push of 2026-11-03, this is an early-stage publication. Pin the version you audit rather than tracking the branch.

## Related

- [Superpowers - Agentic Skills Framework Setup](/hermes/skills/catalog/superpowers-setup)
- [Matt Pocock Agent Workflow Suite - 20-Skill Setup](/hermes/skills/catalog/mattpocock-agent-workflow-suite-setup)
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)

## Pro Tips

- Start with `openagent` or `loops`. Neither needs a 5dive account, and both exercise the description-cap design the rest of the suite follows.
- Install one skill at a time when you first evaluate the set. The wildcard install adds fourteen directories and every description competes for the selector's attention.
- Reach for `verify` before `code-review` when the question is whether a claim is true rather than whether code is good. They answer different questions and the first one is cheaper.
- Keep `diagnose` scoped to the runtime. Loading it for an ordinary failing build is exactly the mis-route its description and the routing evals are written to prevent.
- Treat `compile-knowledge` as a deliberate write, not a transcript dump. It fires on explicit persistence requests and on decision records, causes and gap analyses, which is what keeps the wiki readable a month later.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
