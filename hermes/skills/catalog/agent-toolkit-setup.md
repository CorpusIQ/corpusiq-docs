---
title: "Agent Toolkit - 44 Skills for Coding Agents Setup"
description: "Softaworks Agent Toolkit: 136.7K combined installs. 44 skills for diagrams, writing, QA plans, React, commit hygiene and agent handoffs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agent-toolkit-setup/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skill setup", "agent toolkit", "developer tooling", "coding agents"]
---

# Agent Toolkit - Setup Guide

**Source:** [softaworks/agent-toolkit](https://www.skills.sh/softaworks/agent-toolkit) via skills.sh - 136.7K combined installs across 44 indexed listings; new to this catalog in the Oct 22, 2026 sweep

**GitHub:** [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit) - 2,587 stars, MIT license, last pushed 2026-03-05 (branch main)

**Category:** Developer Tooling / Agent Workflow

**Quality Tier:** 🟢 Production - MIT, 2,587 stars, CI workflows in the repo, and 43 of the 44 indexed listings backed by a SKILL.md in the tree; one sampled skill (qa-test-planner) carries MEDIUM warnings from Socket and Gen Agent Trust Hub for an eval pattern in its helper scripts

Agent Toolkit is a curated collection of skills for AI coding agents. Skills are packaged instructions and scripts that extend agent capabilities across development, documentation, planning, and professional workflows. In practice that means one repo you can point an agent at when you want Mermaid diagrams, cleaner prose, QA plans, typed React components, tidier commits, or a handoff document that survives a context reset.

The collection is broad rather than deep: 44 indexed listings drawing 136.7K combined installs, backed by 2,587 GitHub stars and an MIT license. Most listings are a single SKILL.md with optional helper scripts, so the cost of trying one is close to zero and the cost of installing all of them is prompt budget you may not want to spend.

## Installation

Install the whole collection through the skills CLI:

```bash
npx skills add softaworks/agent-toolkit
```

Or register the repo as a plugin marketplace inside Claude Code and pull only the skills you want:

```bash
# Register as a plugin marketplace inside Claude Code
/plugin marketplace add softaworks/agent-toolkit
/plugin install humanizer@agent-toolkit
/plugin install codex@agent-toolkit
```

There is no separate build step documented, and each skill ships as instructions plus, in some cases, helper scripts that carry their own dependencies. After install the skills live as directories under the agent's skills path, each with a SKILL.md that the agent loads when a request matches its trigger description.

## What It Provides

43 listings at or above the 500-install threshold, with install counts as indexed on October 22, 2026.

| Skill | Installs | Use For |
|---|---|---|
| mermaid-diagrams | 5,109 | Guides creation of software diagrams in Mermaid syntax: class, sequence, flowchart, and entity relationship visuals. |
| humanizer | 4,408 | Detects and fixes AI writing tells, including inflated symbolism, promotional language, and em dash overuse. |
| qa-test-planner | 4,327 | Generates test plans, manual test cases, regression suites, and bug reports, with Figma MCP integration for design validation. |
| database-schema-designer | 4,325 | Designs SQL and NoSQL schemas with normalization, indexing, migration, and constraint guidance. |
| writing-clearly-and-concisely | 4,305 | Applies Strunk's rules to documentation, commit messages, error messages, reports, and UI text. |
| skill-judge | 4,231 | Scores SKILL.md files and skill packages against official specifications, with improvement suggestions. |
| c4-architecture | 4,219 | Produces C4 architecture documentation as context, container, component, and deployment diagrams. |
| agent-md-refactor | 4,213 | Splits bloated AGENTS.md or CLAUDE.md files into linked docs using progressive disclosure. |
| session-handoff | 4,188 | Writes handoff documents for session transfers when context fills or work pauses. |
| crafting-effective-readmes | 4,182 | Templates and guidance for README files matched to audience and project type. |
| commit-work | 4,147 | Reviews and stages changes, splits logical commits, and writes Conventional Commits messages. |
| marp-slide | 4,106 | Builds Marp decks across seven themes, from default and minimal to dark, gradient, and business. |
| react-dev | 4,066 | Type-safe React 18 and 19 patterns: generic components, hook typing, event typing, and routing integration. |
| professional-communication | 4,056 | Email structure, team messaging etiquette, meeting agendas, and audience-adapted technical messages. |
| codex | 4,055 | Runs Codex CLI (codex exec, codex resume) for analysis, refactoring, and automated edits, GPT-5.2 by default. |
| dependency-updater | 4,032 | Auto-detects project type, applies safe updates, prompts on major versions, and diagnoses dependency issues. |
| command-creator | 4,023 | Builds Claude Code slash commands with proper structure and best-practice conventions. |
| react-useeffect | 4,017 | Official-docs useEffect guidance, including when not to use Effect and what to use instead. |
| meme-factory | 4,011 | Generates memes through the memegen.link API across 100+ templates with custom text and styling. |
| reducing-entropy | 3,997 | Manual-only skill that shrinks codebase size, biased toward deletion and measured by final code amount. |
| ship-learn-next | 3,983 | Turns transcripts, articles, and tutorials into implementation plans via the Ship-Learn-Next framework. |
| openapi-to-typescript | 3,976 | Converts OpenAPI 3.0 JSON or YAML into TypeScript interfaces and type guards. |
| gemini | 3,967 | Runs Gemini CLI for code review, plan review, and large-context analysis, Gemini 3 Pro by default. |
| feedback-mastery | 3,957 | Preparation-Delivery-Follow-up and Situation-Behavior-Impact frameworks for difficult conversations. |
| domain-name-brainstormer | 3,943 | Generates domain name ideas and checks availability across multiple TLDs, including .com, .io, .dev, and .ai. |
| daily-meeting-update | 3,940 | Four-question standup interview that pulls GitHub, Jira, and session history into a Markdown update. |
| difficult-workplace-conversations | 3,938 | Preparation-delivery-followup approach to conflicts, performance discussions, and critical feedback. |
| plugin-forge | 3,937 | Creates Claude Code plugins with manifests, components, version bumps, and marketplace wiring. |
| game-changing-features | 3,924 | Finds 10x product opportunities and high-leverage improvements through strategic product thinking. |
| naming-analyzer | 3,898 | Suggests better variable, function, and class names from context and conventions. |
| lesson-learned | 2,983 | Mines git history for engineering lessons and principles from recent code changes. |
| gepetto | 1,540 | Builds sectionized implementation plans through research, stakeholder interviews, and multi-LLM review. |
| requirements-clarity | 946 | Clarifies ambiguous requirements with a YAGNI check and a KISS check before coding. |
| jira | 820 | Issue lookup, creation, updates, and sprint or backlog workflow for Jira tickets. |
| draw-io | 807 | draw.io diagram creation and review: .drawio XML editing, PNG conversion, layout, and AWS icons. |
| backend-to-frontend-handoff-docs | 791 | Writes API handoff documentation for frontend integration work. |
| frontend-to-backend-requirements | 788 | Documents frontend data needs as API requirements for backend developers. |
| mui | 787 | Material-UI v7 patterns: sx prop styling, theme integration, responsive design, and MUI hooks. |
| design-system-starter | 786 | Design tokens, component architecture, accessibility guidelines, and documentation templates. |
| excalidraw | 782 | Delegates Excalidraw file work to subagents so verbose diagram JSON does not exhaust context. |
| perplexity | 763 | Web search and research for generic queries through Perplexity, not library docs or workspace questions. |
| web-to-markdown | 751 | Converts JS-rendered pages to Markdown through the local web2md CLI built on Puppeteer and Readability. |
| datadog-cli | 709 | Log search, metric queries, request tracing, and dashboard management from the Datadog CLI. |

The remaining 1 indexed listing is lessons-learned (1 install), indexed on skills.sh but with no SKILL.md in the current repository tree.

## Why This Matters for Hermes Agents

Hermes loads skills from a directory of SKILL.md files, which is the same shape this repo ships. You can drop selected directories into the profile's skills path and get the same trigger-based loading Hermes already uses, without a wrapper or a translation layer.

The collection fills gaps that come up constantly in agent work. `commit-work` and `agent-md-refactor` deal with the two artifacts that rot fastest in a long-lived repo: git history and the instruction file. `session-handoff` is the direct counterpart to context compression, and `skill-judge` gives you a scoring rubric for the skills you write yourself.

It is also a useful reference set. `reducing-entropy` is deliberately manual-only, so it will not fire unless asked, which makes it safe to keep installed. `writing-clearly-and-concisely` and `humanizer` cover different problems, one structural and one stylistic, and they compose well when you are publishing prose.

Two caveats worth internalizing. First, install counts measure attention, not maintenance. Second, the repo's own quality signal is uneven across 43 listings, and the sampled verdicts in the Security section show at least one that needs a read before you trust it with a shell.

## Usage

After installation, invoke a skill by describing the task the way its trigger expects. The agent matches on the skill description, so the practical skill is naming the artifact you want:

- "Diagram this service's request flow" routes to `mermaid-diagrams` or `c4-architecture` depending on whether you want a flowchart or a C4 view.
- "Clean up the AI phrasing in this announcement" routes to `humanizer`.
- "Write a test plan and regression suite for the checkout flow" routes to `qa-test-planner`.
- "Split these staged changes into logical commits" routes to `commit-work`.
- "Save a handoff before I close this session" routes to `session-handoff`.

Chaining works the way it does for any skill: produce the artifact with one skill, then hand it to another. A common sequence on documentation work is `mermaid-diagrams` for the diagram, `writing-clearly-and-concisely` for the surrounding prose, then `humanizer` for a final pass on anything customer-facing.

If you only want part of the collection, use the plugin marketplace path and install named skills rather than the whole repo. Keeping the installed set small matters: every installed skill adds a line to the agent's skill index, and a 43-skill install competes for attention with your own internal skills.

## Verification

Confirm the repo layout before you rely on it. Each skill should resolve to a SKILL.md under `dist/plugins/<skill>/skills/<skill>/SKILL.md`. Three paths verified on October 22, 2026, all returning HTTP 200:

```bash
for s in mermaid-diagrams humanizer qa-test-planner; do
  curl -sL -o /dev/null -w "%{http_code} $s\n" \
    "https://raw.githubusercontent.com/softaworks/agent-toolkit/main/dist/plugins/$s/skills/$s/SKILL.md"
done
```

- https://raw.githubusercontent.com/softaworks/agent-toolkit/main/dist/plugins/mermaid-diagrams/skills/mermaid-diagrams/SKILL.md
- https://raw.githubusercontent.com/softaworks/agent-toolkit/main/dist/plugins/humanizer/skills/humanizer/SKILL.md
- https://raw.githubusercontent.com/softaworks/agent-toolkit/main/dist/plugins/qa-test-planner/skills/qa-test-planner/SKILL.md

A 200 on all three means the tree still matches the documented layout and the install command has something to resolve. A 404 on a specific skill means that listing was renamed or removed since this snapshot, so trust the tree over the install counts rather than the other way around.

## Security

Sampled verdicts from skills.sh, verified October 22, 2026:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| mermaid-diagrams | Pass | Pass | Pass |
| humanizer | Pass | Pass | Pass |
| qa-test-planner | Warn | Warn | Pass |
| database-schema-designer | Pass | Pass | Pass |
| writing-clearly-and-concisely | Pass | Pass | Pass |

The one warning is specific: `qa-test-planner` carries MEDIUM warnings from Socket and Gen Agent Trust Hub for an eval pattern in its helper scripts. That is not a verdict on the prose instructions, it is a flag on executable code, and it is the kind of thing that matters because a skill's scripts run with whatever permissions your agent already has.

Practical rules. Read the helper scripts of anything that shells out before you install it, especially eval patterns, network calls, and file writers. Install from the plugin marketplace a few skills at a time rather than pulling all 43 blind. Use `skill-judge` on any skill you plan to keep, including third-party ones, since it scores against the same specification the repo cites. And treat a Pass from a scanner as a floor, not a guarantee: five sampled verdicts out of 43 listings is a sample, not a full audit.

## Limitations

Snapshot data, verified October 22, 2026: 136734 combined installs across 44 indexed listings; 2,587 GitHub stars; license MIT; last pushed 2026-03-05. Counts drift over time.

- 44 indexed listings, but only 43 have a SKILL.md in the current tree. `lessons-learned` is indexed without a tree counterpart and sits below the install threshold at 1 install.
- The repo has not been pushed since 2026-03-05, more than seven months before this snapshot. Skills that wrap fast-moving CLIs, notably `codex`, `gemini`, and `datadog-cli`, can drift from the current tool surface.
- One sampled skill, `qa-test-planner`, carries MEDIUM warnings from Socket and Gen Agent Trust Hub for an eval pattern in its helper scripts. The other four sampled skills passed both scanners and Snyk.
- Two pairs overlap heavily: `feedback-mastery` and `difficult-workplace-conversations` both cover a preparation-delivery-followup approach to hard conversations, and `writing-clearly-and-concisely` and `humanizer` both touch prose quality. Install counts alone will not tell you which one to pick.
- `reducing-entropy` and `web-to-markdown` are manual-only by their own instructions. They will not trigger from ambient context, which is a feature but also a surprise if you expect automatic behavior.
- Install counts are a point-in-time index, not a quality signal, and they cluster between 709 and 5,109, so rank order among mid-pack skills says very little.

## Related

- [Humanizer Setup](/hermes/skills/catalog/humanizer-setup)
- [Design Doc Mermaid Skill - Diagram & Documentation Setup](/hermes/skills/catalog/design-doc-mermaid-setup)
- [TestDino Playwright Skills - 79-Guide Testing Suite Setup](/hermes/skills/catalog/testdino-playwright-skill-setup)
- [Vercel AI SDK Skills - TypeScript AI Development Setup](/hermes/skills/catalog/vercel-ai-skills-setup)

## Pro Tips

- Install `humanizer` and `writing-clearly-and-concisely` together, then run the structural edit before the stylistic one. Doing it in the other order means you humanize prose you are about to rewrite.
- Use `agent-md-refactor` when your AGENTS.md passes a few hundred lines. Progressive disclosure beats a longer instruction file every time, and the skill is opinionated about the split.
- Run `skill-judge` on your own skills before you publish them. It scores against the same specification this repo follows, so its critique transfers.
- Point `session-handoff` at a specific next action rather than a general summary. Handoffs that end in "continue the work" cost more context than they save.
- For architecture work, start with `c4-architecture` for the container and component views, then use `mermaid-diagrams` only for the flows that need a sequence or flowchart. Two diagram skills on one document produce inconsistent notation.
- Check the tree, not the install count, when a skill misbehaves. The three verified raw paths above are the fastest way to confirm a listing still exists.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
