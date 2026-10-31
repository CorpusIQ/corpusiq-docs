---
title: "Jaganpro SF Skills - Salesforce Agent Suite"
description: "jaganpro/sf-skills: 43.9K combined installs. Thirty-seven Salesforce skills for Apex, LWC, Flow, SOQL, metadata, deploy and Agentforce work."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/jaganpro-sf-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "salesforce", "apex", "agentforce"]
---

# Jaganpro SF Skills - Setup Guide

**Source:** [jaganpro/sf-skills](https://www.skills.sh/jaganpro/sf-skills) via skills.sh - 43.9K combined installs across 46 indexed listings; first seen 2026-10-31 (morning sweep)

**GitHub:** [jaganpro/sf-skills](https://github.com/jaganpro/sf-skills) - 424 stars, MIT, branch main, last pushed 2026-04-27; 37 `SKILL.md` directories, one per folder under `skills/`, each carrying its own `references/` and `scripts/` material beside it

**Category:** Salesforce platform development for coding agents: Apex, LWC, metadata, deploy and test workflows

**Quality Tier:** 🟡 Yellow - the sample returns a Gen Agent Trust Hub Warn on sf-apex and a Socket Warn on sf-diagram-mermaid, and the repository is archived with a redirect to another project

This is a Salesforce skill library written by a Certified Technical Architect, and it is unusually opinionated for a skill pack: almost every development skill scores work against a fixed point budget (Apex 150 points, LWC 165, metadata 120, SOQL 100) and refuses to be triggered outside its own file patterns, so the skills hand off to each other by design rather than guessing. The set covers the platform surface a consultant actually touches: Apex, LWC, Flow, SOQL, metadata, permissions, data, integration, Connected Apps, deploys, test execution, debug log analysis, and the newer Agentforce tiers split across Builder metadata, Agent Script, agent testing and session-tracing observability.

The first thing to read before installing is the repository's own banner: it is archived, and the Salesforce AI skills have moved to `forcedotcom/afv-library`. That banner is consistent with the metadata, since the last push was 2026-04-27 and the skills.sh install counts have kept accruing against a repository that no longer changes. Treat this as a stable snapshot with a documented successor rather than an actively maintained library, and check the new home before you depend on any Agentforce skill in production.

## Installation

The README's primary route is the skills CLI, which works with Claude Code, Codex, Gemini CLI, OpenCode, Amp and the rest of the Agent Skills clients:

```bash
npx skills add Jaganpro/sf-skills
```

A single skill can be pulled on its own, and the picker can list what exists before anything is written:

```bash
npx skills add Jaganpro/sf-skills --skill sf-apex
npx skills add Jaganpro/sf-skills --list
```

The README's recommended path for Claude Code is a shell installer that goes well past the skills themselves, adding seven specialist agents, a shared hook system, LSP-backed feedback for Apex, LWC and Agent Script, a SOQL schema validator and Prettier plus Code Analyzer validators:

```bash
curl -sSL https://raw.githubusercontent.com/Jaganpro/sf-skills/main/tools/install.sh | bash
```

There is also a Python installer for Windows, CI and managed environments, with an optional flag for the Data Cloud runtime:

```bash
curl -sSL https://raw.githubusercontent.com/Jaganpro/sf-skills/main/tools/install.py | python3
curl -sSL https://raw.githubusercontent.com/Jaganpro/sf-skills/main/tools/install.py | python3 - --with-datacloud-runtime
```

Both installers write to `~/.claude/`, so neither is the right route for this profile. A directory copy keeps the 37 skills in Hermes where the router will find them, and each folder is a complete unit of `SKILL.md` plus whatever sits beside it:

```bash
git clone --depth 1 https://github.com/Jaganpro/sf-skills.git /tmp/sf-skills
cp -r /tmp/sf-skills/skills/. ~/.hermes/profiles/corpusiq/skills/
```

To take a subset, name the folders explicitly. The core development loop is `sf-apex`, `sf-lwc`, `sf-flow`, `sf-soql` and `sf-metadata`, with `sf-deploy` and `sf-testing` closing it out; skip the nine `sf-ai-agentforce-*` folders and the `sf-datacloud-*` family unless you work on those products, since the Data Cloud skills additionally expect a separate `sf data360` CLI runtime that the installer can fetch.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| sf-apex | 1,597 | Generating and reviewing Apex against a 150-point scorecard: classes, triggers, batch, queueable and schedulable jobs, and their test classes. |
| sf-lwc | 1,544 | Lightning Web Components built to the PICKLES method with a 165-point scorecard: wire service, SLDS styling and Jest tests for `lwc` bundles. |
| sf-flow | 1,506 | Record-triggered, screen, autolaunched and scheduled Flow work with a 110-point scorecard over `.flow-meta.xml` files. |
| sf-metadata | 1,490 | Custom objects, fields, validation rules and profile metadata XML, generated and queried against a 120-point scorecard. |
| sf-soql | 1,475 | SOQL and SOSL authoring, optimization and debugging: relationship queries, aggregates and query performance on a 100-point scorecard. |
| sf-debug | 1,463 | Debug log analysis and governor-limit troubleshooting: stack traces, limit exceptions and `.log` files pulled from an org. |
| sf-deploy | 1,454 | Metadata deploys through sf CLI v2: scratch orgs, sandboxes, CI/CD wiring and `sf project deploy` error triage. |
| sf-permissions | 1,442 | Answering who has access to what, by walking permission sets, permission set groups and `.permissionset-meta.xml` files. |
| sf-testing | 1,439 | Apex test execution, coverage analysis and the fix loop for failing tests, scored across six categories. |
| sf-data | 1,436 | Test data creation, bulk import and export through `sf data` commands, with data factory patterns for Apex tests. |
| sf-integration | 1,406 | Named Credentials, External Services, REST and SOAP callouts, Platform Events and change data capture. |
| sf-diagram-mermaid | 1,388 | Mermaid ERDs, sequence diagrams, flowcharts and class diagrams for Salesforce architecture, with an ASCII fallback. |
| sf-connected-apps | 1,383 | OAuth flows, JWT bearer authentication, and Connected App or External Client App metadata. |
| sf-ai-agentscript | 1,375 | The Agent Script DSL: `.agent` files, finite-state agents, slot filling and the `sf agent` authoring-bundle commands. |
| sf-diagram-nanobananapro | 1,334 | Image generation for Salesforce visuals: PNG or SVG output, UI mockups, wireframes and visual ERDs. |
| sf-ai-agentforce | 1,311 | Agentforce Builder metadata: topics and actions, Prompt Builder templates, GenAiFunction and GenAiPlugin XML. |
| sf-ai-agentforce-testing | 1,299 | Agentforce agent testing: `sf agent test` runs, test specs, topic routing checks and coverage analysis. |
| sf-ai-agentforce-observability | 1,267 | Session tracing extraction from Data Cloud and analysis of Agentforce conversation telemetry. |
| sf-docs | 1,210 | Retrieving authoritative Salesforce documentation from developer.salesforce.com and help.salesforce.com when pages resist naive fetching. |
| sf-ai-agentforce-persona | 1,175 | Persona design for agents: identity, tone and voice encoded into Agentforce Builder fields or Agent Script. |

The remaining 26 indexed listings range from 8 to 1,004 installs.

Those 26 include the whole Data Cloud family (`sf-datacloud` at 1,004 down to `sf-datacloud-act` at 973), the OmniStudio and Vlocity cluster, and a tail of retired or generic names such as `sf-ai-agentforce-legacy`, `skill-builder` and `util-youtube-analyzer`. Nine of the 46 indexed names have no directory in the clone at all, which is expected of an archived repository whose index kept accumulating entries.

## Why This Matters for Hermes Agents

Salesforce work punishes improvisation in a specific way. Governor limits, sharing behaviour and metadata ordering are not stylistic choices, and an agent that writes plausible Apex from general knowledge produces code that deploys and then fails review, or worse, fails in production with a limit exception nobody predicted. This suite replaces that guesswork with an explicit point budget per skill, so the agent's own output can be scored before a human reads it, and the 414 markdown files spread across the skill folders are the source material for the score, with `sf-flow` alone carrying 29 and `sf-apex` 22.

The other useful property is the trigger discipline. Each skill names the files and intents it owns and the ones it must hand off, so `sf-apex` declines LWC JavaScript and points at `sf-lwc`, and `sf-metadata` declines deploys and points at `sf-deploy`. On a platform where the same change touches Apex, metadata and permissions at once, that routing is what keeps an agent from writing a class when the real fix is a permission set.

The cost is small and the material is local. Every skill is markdown with YAML frontmatter, so nothing is spent until a skill is routed to, and the deep material is loaded on demand. The Agentforce split is worth understanding before you rely on it: Builder metadata, Agent Script DSL, agent testing and session tracing are four separate skills with four different prerequisites, and their `compatibility` fields say so. Builder metadata, Agent Script and agent testing all require API v66.0+ (Spring '26), and observability needs a Data 360 org with Agentforce Session Tracing switched on.

## Usage

| You say | What happens |
|---|---|
| "Write a batch job that recalculates renewal dates" | `sf-apex` takes it, produces the class and its test class against the 150-point scorecard, and leaves deploys to `sf-deploy`. |
| "Why is this trigger blowing the CPU limit in production" | `sf-debug` reads the debug log for limit exceptions and hotspots, then hands any code fix back to `sf-apex`. |
| "Who can see the Contract object's Discount field" | `sf-permissions` walks permission sets and groups for the field and reports the effective access path. |
| "Turn this object model into an ERD for the design review" | `sf-diagram-mermaid` emits Mermaid source with an ASCII fallback, and offers `sf-diagram-nanobananapro` if the review needs a PNG. |
| "Deploy just the changed metadata to the UAT sandbox" | `sf-deploy` builds the `sf project deploy` invocation, validates first, and reads the deploy error output if it fails. |
| "This LWC will not render the wired record" | `sf-lwc` handles the component: wire service configuration, SLDS and Jest coverage, with `sf-apex` only if the controller is at fault. |
| "Add a topic and action to our service agent" | `sf-ai-agentforce` covers the Builder metadata path, and `sf-ai-agentscript` takes over if the agent should be deterministic instead. |

## Verification

The raw path for the top skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} sf-apex\n" \
  https://raw.githubusercontent.com/Jaganpro/sf-skills/main/skills/sf-apex/SKILL.md
```

Expect `200`. After the copy lands, confirm the count and read one header:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/sf-* | wc -l
head -6 ~/.hermes/profiles/corpusiq/skills/sf-apex/SKILL.md
```

The count should print 37, and the header should show `name: sf-apex`, a multi-line `description:` carrying both a TRIGGER and a DO NOT TRIGGER clause, and `license: MIT`. Check that the supporting folders came along as well, since the scorecards lose most of their value without them:

```bash
find ~/.hermes/profiles/corpusiq/skills/sf-apex -type f -name "*.md" | wc -l
```

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| sf-apex | Warn | Pass | Pass |
| sf-diagram-mermaid | Pass | Warn | Pass |
| sf-industry-commoncore-omnistudio-analyze | Pass | Pass | Pass |
| sf-industry-cme-epc-model | Pass | Pass | Pass |
| sf-ai-agentforce-legacy | Pass | ? | Pass |

No sampled skill fails, but the sample is not clean either: `sf-apex`, the most-installed skill in the library, draws a Gen Agent Trust Hub Warn, and `sf-diagram-mermaid` draws a Socket Warn, which is the pair of reasons this guide is tiered Yellow rather than Green.

The real review surface here is not the markdown but the installer. The Claude Code route pipes a remote shell script into `bash` and rewrites the local agent configuration: it installs a hook registry, a PreToolUse prompt hook that runs a Haiku model for advisory guardrails, a PostToolUse dispatcher that runs Prettier, the LSP engine and Code Analyzer on every write, and a Bash PostToolUse hook that sends debug output to a Haiku agent. The Python installer can restore `settings.json` from a backup and uninstall what it wrote, which is the safer of the two, but both assume they own `~/.claude/`. Neither belongs in a shared profile.

The Data Cloud family widens the dependency surface. The `sf-datacloud-*` skills shell out to an external community plugin, `gthoppae/sf-cli-plugin-data360`, which the README treats as a separate prerequisite rather than part of the install. Read `skills/sf-datacloud/references/plugin-setup.md` before enabling it, and keep the org credentials the CLI stores out of the prompt entirely.

## Limitations

- Snapshot data, verified 2026-10-31: 43,852 combined installs across 46 indexed listings; 424 GitHub stars; MIT; last pushed 2026-04-27. Counts drift over time.
- The repository is archived. Its own README banner states it is no longer actively maintained and redirects users and contributors to `forcedotcom/afv-library`, so fixes to these skills will not arrive here, and the 2026-04-27 push date is the last one to expect.
- The index has drifted past the tree. 46 listings are indexed while the clone holds 37 skill directories, and nine indexed names have no folder: `sf-ai-agentforce-conversationdesign`, `sf-integration-procedure`, `sf-flexcard`, `sf-datamapper`, `sf-omnistudio-analyze`, `sf-omniscript`, `sf-ai-agentforce-legacy`, `skill-builder` and `util-youtube-analyzer`. Several look like retired short names for skills that still ship under the `sf-industry-commoncore-*` prefix.
- The README's own counts disagree with the tree. The badge reads 36 skills and the installer description repeats 36, while the checkout holds 37 directories. Trust the tree.
- Install counts are not a ranking. The spread from 1,597 down to 8 tracks how long a name has been indexed, not how useful it is, and the two most-installed skills are also the two the auditors warn about.
- Success depends on the agent honoring the trigger clauses. The DO NOT TRIGGER sections are prose instructions rather than enforcement, and the Apex, metadata and permissions skills overlap closely enough that a mis-route produces confident guidance for the wrong layer.

## Related

- [Salesforce Skills Library (sf-skills) - 330+ Agent Skills Setup](/hermes/skills/catalog/salesforce-sf-skills-setup)
- [Celigo AI Skills - Celigo Integrations Setup](/hermes/skills/catalog/celigo-ai-skills-setup)
- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the five development skills first and add the rest only when a project needs them. `sf-apex`, `sf-lwc`, `sf-flow`, `sf-soql` and `sf-metadata` cover most day to day work, and the Agentforce and Data Cloud families are four and six folders that stay dark unless you deploy those products.
- Score before you ship. The point budgets are the useful part of this library: ask the agent to run the scorecard on generated Apex or LWC and fix everything it flags before a human reviews the diff.
- Skip the shell installer on this host. It rewires `~/.claude/` hooks and the settings file, which is the wrong blast radius for a Hermes profile; the directory copy gives you the skills with none of the hook system.
- Read `sf-datacloud/references/plugin-setup.md` before installing the Data Cloud family, and decide deliberately whether you want a third-party community CLI between the agent and your org.
- Check `forcedotcom/afv-library` before starting new Agentforce work, since the archived skills stop at the April 2026 state of the platform and the newer library is where those fixes landed.
- Keep org authentication out of prompts. The skills assume a working `sf` CLI login; let it hold the credentials in its own auth store rather than pasting a session id into a conversation.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
