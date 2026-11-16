---
title: "Koru Works Skills - Document-Driven Coding Workflow"
description: "koruworks/skills - 4.5K combined installs across 26 indexed listings: document-driven workflow that takes features from idea to retired docs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/koruworks-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "document-driven workflow", "planning"]
---

# Koru Works Skills - Setup Guide

**Source:** [koruworks/skills](https://www.skills.sh/koruworks/skills) via skills.sh - 4.5K combined installs across 26 indexed listings; first seen Nov 16, 2026 (Nov 16 morning sweep)
**GitHub:** 0 stars, MIT license, `main` branch, last pushed 2026-10-30, one `SKILL.md` per skill under `skills/<name>/`
**Category:** Coding workflow - document-driven feature delivery
**Quality Tier:** 🟢 Green - all 12 sampled skills pass the Gen Agent Trust Hub, Socket, and Snyk.

Koru Works ships a document-driven workflow for coding agents as 26 skills, one `SKILL.md` each, used in the koruworks/mono repo. Together they take a feature from idea to retired docs: shape, design, plan or roadmap, review loop, finalize, execute, accept, hand off or close, plus a few git helpers (commit, merge, fix).

The skills share a few convictions. The user decides; agents recommend and put product decisions to the user as one plain question each. Never block: when the user is away, record the question and keep going. The shape comes before the mechanism, so every plan opens with one sentence and a ladder of use cases. The tree is the truth: documents are claims, and the code plus `git log` are checked before anything is called done. Persisted schema or format changes are announced and approved first, and acceptance teaches the next feature.

## Installation

With the skills CLI:

```sh
npx skills add koruworks/skills
```

Or by hand: copy `skills/<name>/` into your agent's skills directory, for example `.claude/skills/` for Claude Code or `.agents/skills/` for agents that read that path. Copy the whole set if you use the workflow; the skills link to each other by relative path.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| execute-roadmap | 192 | Execute an approved roadmap by orchestrating sub-agents in parallel, in isolated checkouts where the runtime allows. |
| finalize-doc | 191 | Turn a signed-off revision into the final doc with the collapsed history of decisions, then delete the revs and notes. |
| draft-technical | 191 | Design how a feature is built as an engineering conversation, writing TECHNICAL.rev1.md only when the user says the design is ready. |
| draft-experience | 191 | Shape a feature as a product before planning: the sentence, the ladder of use cases, and open questions. |
| fix-bug | 190 | Fix bugs and small improvements while leaving the codebase better than it was found. |
| execute-plan | 190 | Execute a signed-off PLAN.final.md for one feature, phase by phase, one verified commit per phase. |
| draft-roadmap | 190 | Plan a large feature as a roadmap: milestones that follow the ladder, plans small enough to delegate. |
| review-doc-loop | 188 | Run the reviewer's half of the review loop without the user relaying each round. |
| merge-branch | 188 | Merge as a review gate: survey, check against principles, and ask before settling product decisions. |
| review-doc | 187 | Review any planning doc with fresh eyes into <STEM>.revN.notes.md. |
| write-acceptance | 186 | Write the ACCEPTANCE.md checklist of what only a person can verify, each step with its observable. |
| resume-handoff | 186 | Pick up unfinished work from a handoff, verify it against the tree, and propose scope. |
| commit-changes | 183 | Write a commit message sized to the change, show it, and commit on approval. |
| answer-notes-loop | 183 | Run the author's half of the review loop: answer each notes file with the next rev. |
| close-roadmap | 182 | Retire a finished roadmap: triage, fold landed work into docs, and carry the rest to V2. |
| close-plan | 182 | Retire a finished plan: fold what landed into existing docs, and carry the rest to V2. |
| build-feature | 182 | Shape, plan, review, and code a single feature end to end. |
| write-handoff | 181 | Write the HANDOFF.md briefing so a fresh session can pick up unfinished work. |

The remaining 8 indexed listings range from 121 to 144 installs.

## Why This Matters for Hermes Agents

The suite encodes a lifecycle an agent can run end to end without a human relaying each step. The review loop is split into two halves, review-doc-loop and answer-notes-loop, so a reviewer agent and an author agent can pass a document back and forth without the user in the middle. finalize-doc collapses the decision history into one executable doc and deletes the revs, so the reasoning stays in git without cluttering the tree. execute-roadmap gives a lead agent a pattern for fanning a roadmap out to sub-agents in isolated checkouts, then merging verified results. The convictions matter for long-running agents: record questions instead of blocking, and check the tree before declaring anything done. Acceptances feed forward, so what a person finds in testing becomes lessons the next feature reads first.

## Usage

| You say | What happens |
|---|---|
| "/draft-experience payments" | Shapes the feature as a product first: the sentence, the ladder, and the open questions. |
| "/draft-technical payments" | Designs how it is built and writes TECHNICAL.rev1.md only on sign-off. |
| "/review-doc payments" | Reviews the current rev into <STEM>.revN.notes.md with fresh eyes. |
| "/execute-plan spell-check" | Executes the signed-off plan phase by phase with one verified commit per phase. |
| "/execute-roadmap implement m2" | Fans the roadmap out to one sub-agent per plan and merges verified results. |
| "/write-handoff payments" | Writes the HANDOFF.md briefing for the next session. |
| "/resume-handoff payments" | Verifies the handoff against the tree and proposes scope before changing anything. |

## Verification

Check the skill files before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/koruworks/skills/main/skills/execute-roadmap/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/koruworks/skills/main/skills/draft-technical/SKILL.md | head -20
npx skills add koruworks/skills
```

Each skill is one `SKILL.md` under `skills/<name>/`; confirm the path exists in the current tree before copying a specific skill.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| execute-roadmap | Pass | Pass | Pass |
| finalize-doc | Pass | Pass | Pass |
| draft-technical | Pass | Pass | Pass |
| draft-experience | Pass | Pass | Pass |
| fix-bug | Pass | Pass | Pass |
| execute-plan | Pass | Pass | Pass |
| draft-roadmap | Pass | Pass | Pass |
| review-doc-loop | Pass | Pass | Pass |
| merge-branch | Pass | Pass | Pass |
| review-doc | Pass | Pass | Pass |
| write-acceptance | Pass | Pass | Pass |
| resume-handoff | Pass | Pass | Pass |

All 12 sampled skills pass all three scanners.

## Limitations

- Snapshot data, verified Nov 16, 2026: 4,451 combined installs across 26 indexed listings; 0 GitHub stars; MIT; last pushed 2026-10-30. Counts drift over time.
- The repository has 0 GitHub stars at snapshot, so the suite carries less community vetting than larger catalogs.
- 8 of the 26 indexed listings fall below 150 installs (end-pr-review, end-acceptance, merge-branch-mac, start-pr-review, start-acceptance, write-release-notes, release-nightly, release-stable).
- The skills link to each other by relative path, so a partial install can break the workflow; copy the whole set if you use it.
- merge-branch-mac targets the koruworks/mono mac branch layout and is only relevant to that repo's platform split.

## Related

- [Sentimony Agentic Workflow](/hermes/skills/catalog/sentimony-agentic-workflow-setup)
- [Spec Kit Skills](/hermes/skills/catalog/speckit-agent-skills-setup)
- [Pandoscope Skills](/hermes/skills/catalog/pandoscope-skills-setup)
- [Meticulous Agent Skills](/hermes/skills/catalog/meticulous-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy the whole set: the skills link to each other by relative path, so a partial install can break the chain.
- Follow the verb-object naming (<verb>-<object>[-<qualifier>]); size is said only by plan versus roadmap, never by adjectives.
- Use finalize-doc to collapse revs and notes into one executable doc, then delete the superseded files.
- Record open questions with a recommendation and keep going; never block a run on the user being away.
- Read docs/acceptances/ATTENTION.md before shaping, planning, building, or reviewing; it carries the lessons from prior acceptances.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
