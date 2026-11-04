---
title: "Stark AI Agent Skills - Engineering Workflow Kit"
description: "stark-ai-de/agent-skills: 29.2K combined installs. Engineering workflow skills for PRDs, ADRs, repo maps, plan slicing and review swarms."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/stark-ai-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "engineering workflow", "code review", "documentation"]
---

# Stark AI Agent Skills - Setup Guide

**Source:** [stark-ai-de/agent-skills](https://www.skills.sh/stark-ai-de/agent-skills) via skills.sh - 29.2K combined installs across 15 indexed listings; first documented November 3, 2026 (evening sweep)
**GitHub:** 8 stars, Apache-2.0, last pushed 2026-11-03, 54 SKILL.md directories
**Category:** Engineering workflow for agents: PRDs, ADRs, repo maps, plan slicing, debugging and review-fix swarms
**Quality Tier:** 🟢 Green - Apache-2.0 licence and a clean Snyk and Socket record across the sample, with no Gen Agent Trust Hub verdict on visual-reports

This is a one maintainer repository of reviewed agent workflows, organised by the editor they were written for. The 54 SKILL.md directories split across four trees: the portable plugin under plugins/stark-ai-developer/, per editor skills under skills/codex-operations/, skills/cursor-operations/ and skills/claude-operations/, an incubator of engineering and repo maintenance workflows, and one behavioural baseline copy under skill-evals/.

The 15 indexed listings are not the whole repository, and they are not the half the category line describes. Six of them are the curator and spec interviewer pair repeated for Codex, Cursor and Claude Code, and the other nine are plugin skills. The engineering workflows the README promotes (prd-writer, adr-writer, issue-plan-slicer, review-fix-swarm, repo-map-zoom-out, change-impact, debugging-diagnosis) sit in the incubator with no indexed install figure at all. The README is explicit that incubator work stays there until it has evaluation proof and a maintenance path.

## Installation

List the catalog without installing anything, then install one skill into the agent detected for the current project:

```bash
npx skills@latest add stark-ai-de/agent-skills --list
npx skills@latest add stark-ai-de/agent-skills --skill architecture-compass
npx skills@latest update
```

The README also ships editor bundles. The Codex bundle installs eleven skills in one command, and the Cursor bundle eight:

```bash
npx skills@latest add stark-ai-de/agent-skills --skill codex-memory-curator codex-spec-interviewer animated-readme-logo architecture-compass architecture-zoom codegraph-ast-grep drawio-diagrams telegram-serverless karakeep-knowledge jev-capability-advisor visual-reports -g -a codex -y
```

For the portable plugin instead of loose skills, Codex CLI 0.147.0 or later can add the marketplace and install the plugin:

```bash
codex plugin marketplace add stark-ai-de/agent-skills
codex plugin add stark-ai-developer@stark-ai-developer-local
```

Nothing in the repository mentions Hermes. The skills are Markdown, so a profile directory takes the tree directly, but note the extra folder level: per editor skills nest as skills/<editor>-operations/<skill>/SKILL.md.

```bash
git clone --depth 1 https://github.com/stark-ai-de/agent-skills.git /tmp/stark-skills
cp -R /tmp/stark-skills/skills/* ~/.hermes/profiles/corpusiq/skills/
cp -R /tmp/stark-skills/plugins/stark-ai-developer/skills/* ~/.hermes/profiles/corpusiq/skills/
```

The second copy is the one that matters for the plugin skills in the table; the first covers the three editor bundles. Install one editor's bundle rather than all three unless the team genuinely uses several agents, because the curators and interviewers overlap heavily across editors.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| codex-memory-curator | 2,714 | Curating the memory a Codex session carries: what to keep, what to compress and what to drop. Ships as skills/codex-operations/codex-memory-curator and again inside the plugin. |
| codegraph-ast-grep | 2,707 | Code graph search over a repository using ast-grep patterns, packaged at plugins/stark-ai-developer/skills/codegraph-ast-grep. |
| cursor-memory-curator | 2,686 | The Cursor edition of the memory curator, at skills/cursor-operations/cursor-memory-curator. |
| drawio-diagrams | 2,666 | Producing diagrams as draw.io files, at plugins/stark-ai-developer/skills/drawio-diagrams. |
| animated-readme-logo | 2,661 | Building an animated logo for a README, the same static SVG plus animated GIF pair this repository uses for its own header. |
| architecture-compass | 2,658 | Architecture orientation for a repository. The incubator carries architecture-compass-adr-authoring beside it for the ADR half of the job. |
| jev-capability-advisor | 2,647 | Advising on which capability or skill fits a task before the work starts, at plugins/stark-ai-developer/skills/jev-capability-advisor. |
| cursor-spec-interviewer | 2,640 | Interviewing the user until a rough request becomes a spec, for Cursor sessions. |
| codex-spec-interviewer | 2,632 | The Codex edition of the spec interviewer, shipped both at skills/codex-operations/codex-spec-interviewer and in the plugin. |
| claude-memory-curator | 2,593 | The Claude Code edition of the memory curator, at skills/claude-operations/claude-memory-curator. |
| claude-spec-interviewer | 2,566 | The Claude Code edition of the spec interviewer, at skills/claude-operations/claude-spec-interviewer. |
| telegram-serverless | 14 | A serverless Telegram bot workflow, at plugins/stark-ai-developer/skills/telegram-serverless. |
| architecture-zoom | 9 | Zooming from a repository overview into the specific parts that matter, at plugins/stark-ai-developer/skills/architecture-zoom. |
| karakeep-knowledge | 7 | Wiring Karakeep knowledge into an agent workflow, at plugins/stark-ai-developer/skills/karakeep-knowledge. |
| visual-reports | 4 | Rendering visual reports, at plugins/stark-ai-developer/skills/visual-reports. |

No indexed listings fall below the threshold; all 15 appear above.

Every one of the 15 listings has a SKILL.md directory in the tree. Six of them live under skills/<editor>-operations/, eleven are packaged in plugins/stark-ai-developer/skills/, and codex-memory-curator plus codex-spec-interviewer appear in both places, which is why fifteen listings cover seventeen directories. The install spread is the odd part: the top eleven sit between 2,566 and 2,714, a band narrow enough to look like the same audience installing the same bundle, and the bottom four sit between 4 and 14.

The tree holds far more than the table. The incubator carries engineering workflow skills (prd-writer, adr-writer, issue-plan-slicer, review-fix-swarm, repo-map-zoom-out, change-impact, debugging-diagnosis, test-first-implementation, prototype-spike), repo maintenance skills (pr-review, ci-debugger, release-manager, dependency-update-review, docs-audit, security-baseline-review, issue-triage, repo-health-audit, script-simplification, agent-context-bootstrap), skill maintenance skills and two productivity skills. None of those has an indexed listing in this snapshot.

## Why This Matters for Hermes Agents

The gap between a coding agent that can write a function and one that can be trusted with a repository is mostly process, and this repository treats process as installable text. A spec interviewer turns a vague request into something with edges. A plan slicer cuts that spec into issues. A repo map gives the agent the lay of the land before it edits. Those are the steps that an agent skips when nobody hands it a workflow, and they are exactly the steps that make the difference between a diff you accept and a diff you rewrite.

The editor specific copies are a real design choice rather than duplication for its own sake. A memory curator for Codex has to know where Codex keeps its context; the Cursor and Claude editions know their own hosts. If your agents run in one harness, the matching bundle is the smaller install and the better fit, and the three bundles are otherwise the same idea wearing three jackets.

The incubator is where the engineering value is, which makes the install data a poor map. The eleven skills that carry thousands of installs are the ones distributed through the bundles, and the workflows that would change how a team works (ADR writing, review-fix swarms, debugging diagnosis, prototype spikes) are the ones nobody has indexed yet. Reading these skills by install count inverts the repository's own priority order.

There is also a maintenance signal worth weighing. Fifty four directories maintained by a repository with eight stars means the bus factor is one, and it was pushed the same day as this sweep. That is fine for Markdown you can read and fork, and less fine if you build a process on top of it without pinning a commit.

## Usage

| You say | What happens |
|---|---|
| "Interview me about this feature until we have a spec" | codex-spec-interviewer, cursor-spec-interviewer or claude-spec-interviewer runs the questioning loop for your editor and produces a written spec instead of starting to code. |
| "Write an ADR for moving to Postgres" | The incubator's adr-writer produces the decision record, and architecture-compass-adr-authoring supplies the architecture context around it. |
| "Cut this spec into issues I can work one at a time" | issue-plan-slicer splits the spec into ordered, independently shippable slices. |
| "Give me a map of this repo before I touch it" | repo-map-zoom-out produces the overview, and architecture-zoom drills into the part you name. |
| "What does this codebase actually do around billing" | codegraph-ast-grep searches the code graph with ast-grep patterns rather than by string matching. |
| "Review my branch and fix what you find" | review-fix-swarm runs the review and fix loop, and pr-review covers the pull request form of the same pass. |
| "This test fails and I have no idea why" | debugging-diagnosis works the failure back to a cause, with ci-debugger for failures that only reproduce in CI. |
| "Clean up this session's context before we continue" | The memory curator for your editor decides what to keep, compress or drop. |

## Verification

Check a path from the LAYOUT on branch main before copying:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/stark-ai-de/agent-skills/main/skills/codex-operations/codex-memory-curator/SKILL.md
```

That URL should print 200. The plugin copies live at plugins/stark-ai-developer/skills/<name>/SKILL.md on the same branch, and the incubator at incubator/skills/<group>/<name>/SKILL.md.

After cloning, count what you actually got rather than trusting the listing count:

```bash
find /tmp/stark-skills -name SKILL.md | wc -l
find /tmp/stark-skills/incubator/skills -name SKILL.md | wc -l
```

The first count should be 54 for this snapshot, and the second is the incubator's share, which is the part with no install data. Then confirm the installed copies in the profile:

```bash
find ~/.hermes/profiles/corpusiq/skills -maxdepth 3 -name SKILL.md | wc -l
```

## Security

skills.sh verdicts for sampled skills (verified November 3, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| codex-memory-curator | Pass | Pass | Pass |
| drawio-diagrams | Pass | Pass | Pass |
| cursor-spec-interviewer | Pass | Pass | Pass |
| telegram-serverless | Pass | Pass | Pass |
| visual-reports | ? | Pass | Pass |

Four of the five sampled listings pass all three auditors, and the fifth, visual-reports, passes Socket and Snyk with no Gen Agent Trust Hub result. That is the cleanest sample of the three packs in this batch, and it covers both the highest install skill and the lowest.

The risk here is not a network call, it is the blast radius of the instructions. These skills change how an agent plans, reviews and edits a repository, and a workflow skill that is subtly wrong produces a wrong process repeated consistently. Read the SKILL.md you install and keep the reviewed public tree separate from the incubator, which the README itself describes as draft and experimental until it has evaluation proof.

The repository runs a validate workflow and a Pages workflow on every push, and its README states that public skills are reviewed before promotion. That is a process claim rather than an audit, so weight it as a signal about care, not as a guarantee about code. There is no executable surface in the skills themselves, which is why the auditors have little to flag.

## Limitations

- Snapshot data, verified November 3, 2026: 29,204 combined installs across 15 indexed listings; 8 GitHub stars; Apache-2.0; last pushed 2026-11-03. Counts drift over time.
- The engineering workflows the category line names (PRDs, ADRs, plan slicing, review-fix swarms) are incubator skills with no indexed listing. The 15 listings are the editor operations and plugin skills.
- Install counts do not rank the skills. Eleven listings sit between 2,566 and 2,714 as bundle installs, and the bottom four sit between 4 and 14.
- Eight stars and a single maintainer make this a young repository. Read the incubator skills before you rely on them, and pin a commit if a process depends on one.
- Gen Agent Trust Hub has no verdict for visual-reports in the sample, and four of the 15 listings are too small to have much community evidence behind their counts.
- The install layout is one folder deeper than a flat skills directory, so a copy that flattens skills/<editor>-operations/<skill>/ into <skill>/ changes the paths the skills describe.

## Related

- [Sanity Agent Toolkit - Headless CMS Setup](/hermes/skills/catalog/agent-toolkit-setup)
- [Agentic Awesome Skills - 2,000+ Skill Catalog Setup](/hermes/skills/catalog/agentic-awesome-skills-setup)
- [Qodex AI Agent Skills - 81 Skill Starter Library](/hermes/skills/catalog/qodex-ai-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the bundle for the editor you actually use. The three curator and interviewer pairs are near copies of each other, and installing all three adds context for skills your agent will never trigger.
- Go to the incubator for the engineering workflows. prd-writer, adr-writer, issue-plan-slicer and review-fix-swarm have no install figures but they are the reason to clone this repository.
- Keep the nesting intact. skills/codex-operations/codex-memory-curator/SKILL.md expects its parent folder name, and flattening the copy breaks the paths the skill describes.
- Run --list before installing. The catalog is larger than the 15 indexed listings, so the listing page is not the inventory.
- Pin a commit for anything you build a process on. Eight stars and one maintainer means the tree can move, and npx skills@latest update will happily follow it.
- Use the spec interviewer before the plan slicer. Slicing a vague request produces vague issues, and the interview is the cheap place to find that out.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
