---
title: "Microsoft VS Code Skills - Editor Workflow Suite"
description: "microsoft/vscode on skills.sh: 28.0K combined installs across 13 listings; editor contributor skills for accessibility, pipelines and memory audits."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/microsoft-vscode-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "vscode", "editor", "code review"]
---

# VS Code Skills - Setup Guide

**Source:** [microsoft/vscode](https://www.skills.sh/microsoft/vscode) via skills.sh - 28.0K combined installs across 13 indexed listings; first seen 2026-11-04 (Nov 4, 2026 evening sweep)
**GitHub:** 194,645 stars, MIT licence, last pushed 2026-11-05, 79 SKILL.md directories split between .github/skills and .agents/skills
**Category:** Editor contribution workflows: accessibility requirements, build and pipeline validation, memory leak audits and agent session layout for the VS Code source tree
**Quality Tier:** 🟡 Beta - Snyk Warn on azure-pipelines; MIT; Microsoft's own editor repo.

This is the Code - OSS repository, the source tree Microsoft develops Visual Studio Code in. Alongside the editor code of a 194,645 star repository it carries 79 SKILL.md directories, with paths such as `.github/skills/accessibility`, `.github/skills/azure-pipelines` and `.agents/skills/launch`. Each one encodes a piece of the workflow the team uses to change the editor: how to satisfy the accessibility contract, how to validate an Azure DevOps pipeline change without a full CI run, how to audit a listener for a leak, how to trace what one author contributed to a branch.

The distinguishing feature is that these are not generic coding skills. They are written against a specific tree and name real subsystems: `src/vs/sessions` for the Agents Window, blocks-ci screenshot hashes for component tests, addDisposableListener and DisposableStore for disposal audits. An agent that reads one inherits a maintainer's checklist rather than a general essay about best practice.

## Installation

The skills ship inside the editor repository, and the README documents the editor build and contribution flow rather than a plugin marketplace line for the skills. The working route is to clone the tree and read the skill directories from it:

```bash
git clone https://github.com/microsoft/vscode.git
cd vscode
```

Confirm the set is present before pointing an agent at it:

```bash
find .agents .github -name SKILL.md | wc -l
```

An agent that discovers skills from a directory can be pointed at `.github/skills` directly, or at individual files through `.github/skills/<name>/SKILL.md`. The README routes contributors to its How to Contribute wiki page for the build, debug and test workflow, which these skills assume is already working.

## What It Provides

Ten listings clear the 500 install threshold. Integers are the exact index figures from the November 4, 2026 snapshot.

| Skill | Installs | Use For |
|---|---|---|
| memory-leak-audit | 3,226 | Auditing listeners, DOM handlers, lifecycle callbacks and leak reports, covering addDisposableListener, Event.once, MutableDisposable, DisposableStore and onWillDispose |
| azure-pipelines | 3,224 | Validating Azure DevOps pipeline changes for the VS Code build: queueing builds, checking status, viewing logs and iterating on YAML without waiting for full CI |
| accessibility | 3,187 | Required for new feature and contribution work: accessibility help dialogs, accessible views, verbosity settings, signals, ARIA announcements, keyboard navigation, labels and roles |
| sessions | 3,073 | Core principles and workflow router for changes to the Agents Window under src/vs/sessions |
| author-contributions | 3,030 | Tracing every file an author touched on a branch versus its upstream, following renames, for authorship audits before a merge |
| update-screenshots | 3,005 | Refreshing committed blocks-ci screenshot hashes after a Screenshots and Tests failure, or investigating a screenshot diff on a PR |
| fix-errors | 2,818 | No description captured in the snapshot; the name points at error repair, so open its SKILL.md before relying on it |
| tool-rename-deprecation | 2,561 | No description captured in the snapshot; the name points at tool rename and deprecation handling, so read the file before use |
| hygiene | 2,160 | No description captured in the snapshot; read SKILL.md for the specific hygiene checks it enforces |
| agent-sessions-layout | 911 | No description captured in the snapshot; read SKILL.md for the agent sessions layout rules |

Three indexed listings fall below the threshold, ranging from 239 to 302 installs.

## Why This Matters for Hermes Agents

An agent working in a large, opinionated repository fails in predictable ways: it adds an interactive widget without the accessibility wiring the project requires, it guesses at a CI failure instead of reading the log, it leaks a disposable that a reviewer then has to catch. Each skill here is a corrective for one of those failure modes, written by the people who maintain the code.

Accessibility is the clearest case. The skill is not advisory: it states that a new interactive surface must ship an accessibility help dialog, an accessible view and a verbosity setting, and it lists which existing features already carry all three. An agent that loads it before writing UI code produces a contribution that can survive review instead of one that has to be rewritten.

The leak audit skill carries the same value in a different shape. It names the disposal primitives the codebase actually uses, so a review question about an event handler resolves against a known list rather than a vague remark about cleanup.

The pipeline skill removes a slow loop. Rather than pushing a change and waiting for full CI to answer, an agent can queue a build, read the status and iterate on the YAML while the feedback is still cheap.

For agents outside this repository, the transferable pattern is the shape of the skills themselves: narrow, path-specific, and written as a checklist over named APIs. That is what makes a skill usable by a model that has never seen the codebase.

## Usage

| You say | What happens |
|---|---|
| "Add a settings panel to the Agents Window" | sessions routes to the Agents Window workflow and accessibility supplies the required dialog, view and verbosity setting |
| "Why did this PR fail the screenshot check?" | update-screenshots reads the diff and refreshes the committed blocks-ci hashes |
| "Review this listener for a leak" | memory-leak-audit checks the handler against the disposal primitives the codebase uses |
| "Who touched this file on this branch?" | author-contributions traces the files, following renames, and reports what the author contributed |
| "Will this pipeline YAML work?" | azure-pipelines queues a build, reads the status and shows the log |
| "Run the hygiene checks before I push" | hygiene runs the repository hygiene pass, with the specific checks listed in its SKILL.md |
| "Rename this tool without breaking callers" | tool-rename-deprecation walks the rename and deprecation path described in its SKILL.md |

## Verification

Fetch one skill file and confirm the frontmatter is intact (probed 2026-11-04, HTTP 200):

```bash
curl -fsSL https://raw.githubusercontent.com/microsoft/vscode/main/.github/skills/accessibility/SKILL.md | head -6
```

Then confirm the local tree carries the full set:

```bash
find .agents .github -name SKILL.md | wc -l
```

The count should match the 79 directories reported in the layout line above. To check that an agent has actually picked the skills up, ask it to list what it can see and confirm that `accessibility` and `memory-leak-audit` appear by name.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-04) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| memory-leak-audit | Pass | Pass | Pass |
| azure-pipelines | Pass | Pass | Warn |
| accessibility | Pass | Pass | Pass |
| fix-errors | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified 2026-11-04: 28,011 combined installs across 13 indexed listings; 194,645 GitHub stars; MIT licence; last pushed 2026-11-05. Counts drift over time.
- These skills are written against this repository's own paths and subsystems (src/vs/sessions, blocks-ci screenshot hashes, the accessibility dialog contract), so they transfer as patterns more than as drop-in procedures.
- No marketplace install line for the skills appears in the README section captured for this guide, so the tree has to be cloned before they can be read.
- Four of the ten skills in the table carry no SKILL.md description in the snapshot (fix-errors, tool-rename-deprecation, hygiene, agent-sessions-layout), so their entries stay at name level.
- azure-pipelines draws a Snyk Warn while the other three sampled skills pass all three scanners.
- Install counts are a skills.sh index figure and do not measure use inside Microsoft.

## Related

- [CC DevOps Skills - Kubernetes and IaC Suite](/hermes/skills/catalog/cc-devops-skills-setup)
- [Cypress AI Toolkit - E2E Testing Skills](/hermes/skills/catalog/cypress-ai-toolkit-setup)
- [Fallow Skills - Codebase Intelligence for TS and JS Setup](/hermes/skills/catalog/fallow-rs-fallow-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load accessibility before writing UI code, not after a reviewer asks for the dialog. The skill is explicit that it applies to any new interactive surface, named or not.
- Read hygiene, fix-errors and the other description-less skills directly. The table deliberately stops at the name rather than guessing at their contents.
- Treat the tree as the source of truth. These files change with the codebase, so re-read the SKILL.md instead of trusting a cached copy from an older checkout.
- Point the agent at a single skill file when context is tight. Ten files describing ten different subsystems is more than most turns need.
- Use the pipeline skill while iterating on YAML. Reading a build log is cheaper than a full CI cycle and gives the same answer.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
