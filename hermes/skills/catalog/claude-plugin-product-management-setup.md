---
title: "PM Prompt Skills - Product Management Suite Setup"
description: "pmprompt/claude-plugin-product-management: 10.4K combined installs across 30 listings; PM skills for PRDs, prioritisation and strategy."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-plugin-product-management-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "product management", "prd", "strategy"]
---

# PM Prompt Skills - Setup Guide

**Source:** [pmprompt/claude-plugin-product-management](https://www.skills.sh/pmprompt/claude-plugin-product-management) via skills.sh - 10.4K combined installs across 30 indexed listings; first seen 2026-11-07 (Nov 7, 2026 evening sweep)
**GitHub:** 57 stars, MIT, last pushed 2026-10-22, 30 `SKILL.md` directories under `skills/` with a one to one match against the indexed listings, nine command files in `commands/`, and plugin manifests for both Claude and Codex at `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`
**Category:** Product management craft for agents: PRDs, prioritisation, discovery, positioning, growth models, pricing, experiments and stakeholder communication
**Quality Tier:** 🟡 Yellow - Snyk returns Warn on `user-feedback-synthesizer`, and the rest of the set is markdown only, so the risk is what you paste into it rather than what it runs.

This is a product management plugin that ships as a folder of skills rather than a tool. Thirty skills, one per framework or workflow, each written as guidance an agent can follow and each naming the practitioner behind the model it encodes: Jobs to be Done from Clayton Christensen, the Hooked model from Nir Eyal, the Hierarchy of Engagement and Hierarchy of Marketplaces from Sarah Tavel, Growth Loops from Brian Balfour and Elena Verna, Seven Powers from Hamilton Helmer, Thinking in Bets from Annie Duke, the Design Sprint from Jake Knapp, and Shape Up's appetite and betting table.

The set is not only recycled frameworks. Two skills are aimed squarely at AI products and have no counterpart in a classic PM toolkit: `agent-spec-generator`, which writes a production spec for an agent covering scope, tools and permissions, autonomy levels, stop rules, escalation, failure modes and evals, and `ai-ship-bar`, which defines a measurable quality bar for an AI feature with task completion, precision and recall, p95 latency, cost per successful request and regression gates.

## Installation

The README gives three routes. The skills CLI is the shortest:

```bash
npx skills add pmprompt/claude-plugin-product-management
```

Claude Code, from a local checkout, loads the repository as a plugin directory:

```bash
git clone https://github.com/pmprompt/claude-plugin-product-management.git
cd claude-plugin-product-management
claude --plugin-dir .
```

Codex uses the marketplace metadata the repository ships:

```bash
codex plugin marketplace add pmprompt/claude-plugin-product-management
codex plugin add pmprompt@pmprompt-skills
```

Installed as a plugin, the skills appear under a namespace, so the invocation is `/pmprompt:prd-writer` rather than a bare skill name. The README lists `/pmprompt:prd-writer`, `/pmprompt:jobs-to-be-done` and `/pmprompt:working-backwards` as the entry points, and the plugin manifest is version 0.5.0 in all three manifests.

For Hermes, copy the directories you want from `skills/` into the profile skills directory. Each skill is a single `SKILL.md` with no scripts or references, which makes partial adoption easy. The nine files in `commands/` are Claude Code slash commands, and the README notes that Codex turns them into skills automatically.

## What It Provides

Five listings clear the reporting threshold, and they are the practical core:

| Skill | Installs | Use For |
|---|---|---|
| prd-writer | 1,242 | A product requirements document with problem, goals, scope and non-goals, risks, edge cases and a done-when section |
| feature-prioritization-assistant | 546 | RICE scoring across a roadmap so prioritisation decisions carry arithmetic instead of opinion |
| user-feedback-synthesizer | 434 | Synthesising feedback collected from several sources into patterns and themes |
| thinking-in-bets | 426 | Making decisions under uncertainty, separating decision quality from outcome, and avoiding resulting |
| product-led-growth | 400 | Designing self-serve growth motions where the product drives acquisition, activation and monetisation |

The remaining 25 indexed listings range from 6 to 397 installs.

Do not read the tail as the leftovers. It holds most of the framework skills, including `jobs-to-be-done` at 397, `ab-test-designer` and `shape-up` at 391 each, `okrs` at 390 and `strategic-narrative` at 383. The bottom five sit at 6 or 7 installs: `shaping`, `competitive-analysis-framework`, `breadboarding`, `ai-ship-bar` and `agent-spec-generator`. The two AI-specific skills are among the newest and least installed, which is the usual lag rather than a verdict.

## Why This Matters for Hermes Agents

Product work is where an agent is most likely to produce fluent nonsense. Ask for a roadmap and you get a plausible list with invented confidence intervals, because nothing in the request forces evidence. These skills counter that by making the artefact specific. RICE scoring forces four numbers per item. A PRD template forces a non-goals section and a done-when line. Working backwards forces a press release before any engineering estimate.

The second value is vocabulary matching. A user who says "set an appetite" or "run a betting table" is speaking Shape Up, and a user who says "find the real competitor" is speaking Jobs to be Done. The skill descriptions in this set are unusually trigger-heavy, listing the exact phrases that should fire them, which is the part most skill authors skip and the part that decides whether a skill loads at all.

Third, the two AI product skills fill a real gap. Most PM frameworks were written before agents existed, so the questions they ask stop at the interface. `ai-ship-bar` asks for a p95 latency budget and a cost per successful request, and `agent-spec-generator` asks for stop rules and escalation paths. Those are the questions that decide whether an AI feature ships in a usable state.

Finally, this is a low-risk install. Thirty markdown files, no scripts, no network calls of their own, MIT licensed. The review effort goes into judging the frameworks rather than auditing code.

## Usage

| You say | What happens |
|---|---|
| "Turn this messy feature idea into a PRD" | `prd-writer` produces problem, goals, scope and non-goals, risks, edge cases and done-when criteria |
| "Prioritise these twelve features for next quarter" | `feature-prioritization-assistant` scores each on reach, impact, confidence and effort, then ranks with the arithmetic shown |
| "Here are 40 support tickets, what are users actually asking for" | `user-feedback-synthesizer` clusters the feedback into themes with counts rather than a summary |
| "Should we build this or is it a coin flip" | `thinking-in-bets` separates the decision from the outcome and names what would change the answer |
| "Write the PR/FAQ for this product" | `working-backwards` drafts the launch press release and the FAQ before any solution design |
| "Set a quality bar for shipping our AI assistant" | `ai-ship-bar` defines task completion, precision and recall, latency, cost and regression gates |
| "Spec out the agent we want to build" | `agent-spec-generator` writes scope, tools, permissions, autonomy levels, stop rules, evals and rollout |

## Verification

Read the entry skill before installing. This path returned HTTP 200 on `main` when this guide was written:

```bash
curl -fsSL https://raw.githubusercontent.com/pmprompt/claude-plugin-product-management/main/skills/prd-writer/SKILL.md | head -10
```

It should open with `name: prd-writer` and a description about generating product requirements documents for a new feature or initiative. The second one to check is a framework skill rather than a template:

```bash
curl -fsSL https://raw.githubusercontent.com/pmprompt/claude-plugin-product-management/main/skills/jobs-to-be-done/SKILL.md | head -10
```

After install, confirm thirty directories landed in the skills directory your agent uses, or that the plugin route exposes the `pmprompt` namespace. Then ask for a PRD on a feature you already understand, and check that the output contains a non-goals section. A model with the skill loaded will produce one; without it, the same request usually does not.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| prd-writer | Pass | Pass | Pass |
| feature-prioritization-assistant | Pass | Pass | Pass |
| user-feedback-synthesizer | Pass | Pass | Warn |

The tree is thirty `SKILL.md` files and a `.gitkeep`, so there is no executable surface at all. The one Warn sits on `user-feedback-synthesizer`, which is also the skill most likely to be handed raw customer material, so read it before you paste support tickets into a session.

That is the real security consideration here: the data, not the code. Feedback synthesis means putting customer verbatim into a model context, and those collections routinely carry names, account identifiers, email addresses and pricing conversations. Decide what may enter the loop, and strip identifiers before the skill sees them.

The install-time manifests are worth a glance if you use the plugin routes, because `.agents/plugins/marketplace.json` and `.codex-plugin/plugin.json` tell Codex where to fetch the plugin from. They point at this repository, which is what you would expect, and they are versioned at 0.5.0.

## Limitations

- Snapshot data, verified 2026-11-07: 10,352 combined installs across 30 indexed listings; 57 GitHub stars; MIT; last pushed 2026-10-22. Counts drift over time.
- The README's skills table documents 28 of the 30 directories. `shaping` and `breadboarding` ship without a table row, and both sit at 6 to 7 installs, so the documentation and the install index disagree slightly at the bottom of the list.
- Install counts fall away sharply after the first five. 25 of 30 listings sit between 6 and 397, and the two AI-specific skills are among the lowest, so the popular skills here are the templates rather than the newer thinking.
- These are interpretations of published frameworks, not the books. Each skill names its source, and where the framework matters to a decision, read the original rather than the compressed version.
- Nothing is enforced. A template cannot tell whether your non-goals are honest or your RICE confidence scores are real, so the output is only as good as the inputs you supply.
- The publisher runs a companion site at pmprompt.com alongside the repository. The skills themselves are MIT and free, but expect the in-skill links to point at that site.
- Skills are markdown with no version negotiation. When 0.5.0 becomes 0.6.0, refresh the copy in your skills directory rather than assuming the old text still matches the README.

## Related

- [PM Skills - Product Management Lifecycle Suite Setup](/hermes/skills/catalog/pm-skills-setup)
- [Phuryn PM Skills - Competitive Strategy for Hermes Agents](/hermes/skills/catalog/phuryn-pm-skills-setup)
- [Dean Peters PM Skills - Product Management Workflows](/hermes/skills/catalog/deanpeters-pm-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the whole set even if you only want PRDs. The skill descriptions are trigger-keyed, so an adjacent skill fires on the vocabulary your team already uses and saves you restating the framework.
- Run `prd-writer` and `working-backwards` on the same idea. The PRD tells you what to build and the PR/FAQ tells you whether anyone would care, and disagreements between them are the useful signal.
- Feed `user-feedback-synthesizer` counts, not adjectives. Forty tickets with themes beat a paragraph saying customers are frustrated.
- Use `agent-spec-generator` before the build, not after. Stop rules and escalation paths are cheap to write and expensive to retrofit once an agent has shipped with unlimited autonomy.
- Keep the plugin namespace if you use Claude Code. `/pmprompt:prd-writer` is unambiguous in a session that also has other PM skill sets installed, which is the normal case after a few months of collecting them.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
