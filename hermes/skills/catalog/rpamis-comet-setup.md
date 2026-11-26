---
title: "Comet Skills - Agent Workflow Harness Setup"
description: "rpamis/comet - 9.8K combined installs: Comet agent skill harness for turning ideas into evaluated workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/rpamis-comet-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "agent workflow", "skill harness", "evaluation"]
---

# Comet Skills - Setup Guide

**Source:** [rpamis/comet](https://www.skills.sh/rpamis/comet) via skills.sh - 9.8K combined installs across 24 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 evening sweep)
**GitHub:** [rpamis/comet](https://github.com/rpamis/comet) - 3,317 stars, MIT license, last pushed Nov 25, 2026, master branch; skills live under assets/skills/<name>/SKILL.md, with Chinese variants under assets/skills-zh/ and maintainer skills under assets/skills-maintainer/.
**Category:** Agent Workflow Harness (Comet)
**Quality Tier:** 🟠 Orange - 15 of 24 listings sampled: nine pass all three checks, three carry a Snyk Fail, and three carry at least one Warn.

rpamis/comet is Comet, a resumable long-running task workflow and Skill platform for agents. It provides two independent requirement workflows: Native for strong models, powered only by Comet's own runtime, and Classic, which preserves the full OpenSpec + Superpowers phase-governance model. On top of those sit the SDK, Comet Any, Eval, Personal Memory, and Project Knowledge, so agents can compose existing skills into workflows, evaluate them scientifically, and retain preferences and project knowledge over time.

The 24 indexed listings span the workflow entry skills (/comet, /comet-native, /comet-classic), the Classic phase skills (open, design, build, verify, archive, tweak, hotfix), and a set of maintainer and GitHub helper skills. The default branch is master, so every raw URL in this guide uses master.

## Installation

Requirements: Node.js 22.16+ (22.x) or 24+, npm/npx, and Git.

```bash
npm install -g @rpamis/comet
```

Initialize Comet in the project where you want to use it:

```bash
cd your-project
comet init
```

Interactive setup explains and offers Native, Classic, or both. Non-interactive setup picks a workflow directly:

```bash
comet init --workflow classic
comet init --workflow both
```

For platforms that use the generic skills CLI (including Hermes), install the Comet skill package with:

```bash
npx skills add rpamis/comet
```

## What It Provides

skills.sh publishes per-skill install counts for all 24 indexed listings. The 8 most-installed skills are listed below; the remaining 16 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| comet | 1,236 | workflow entry; routes to Native or Classic from project configuration |
| comet-build | 894 | plan, implement, and accept Classic tasks |
| comet-archive | 881 | archive and deliver a Classic change |
| comet-verify | 878 | verify a Classic change and record the results |
| comet-design | 874 | complete the Classic technical design and obtain user confirmation |
| comet-open | 870 | create a Classic change, clarify requirements, and obtain user confirmation |
| comet-tweak | 868 | lightweight adjustment within one change via the Classic preset |
| comet-hotfix | 868 | repair a localized defect via the Classic preset |

The remaining 16 indexed listings range from 19 to 373 installs.

## Why This Matters for Hermes Agents

Comet is a harness for the exact problem Hermes builders hit when an agent runs long multi-phase work: keeping a spec lifecycle resumable after interruptions, and making phase transitions depend on real checks rather than the model saying "done." The Classic flow bakes OpenSpec and Superpowers into a five-phase state machine with guard scripts, and Native hands a strong model the planning and implementation while Comet still owns state, acceptance, and archive. For a builder, that means an agent can be interrupted and resumed cleanly, with worktrees, verification evidence, and archive status tracked by the runtime. The SDK and Comet Any extend the same harness to your own skills, and Eval gives you scientific Rubric, Pass@k, and Pass^k scoring so skill changes are judged on evidence. The cost is complexity: this is a large platform with its own CLI, configuration, and a master-branch default that breaks scripts expecting main.

## Usage

| You say | What happens |
|---|---|
| Start a Comet workflow | Uses /comet to route to Native or Classic from the project config |
| Open a new Classic change | Uses /comet-open to create the change and confirm its requirements |
| Design the technical approach | Uses /comet-design to complete the design and get confirmation |
| Plan and implement this task | Uses /comet-build to plan, implement, and accept the task |
| Verify the change | Uses /comet-verify to verify and record the results |
| Fix this one bug quickly | Uses /comet-hotfix for a localized repair |
| Make a small adjustment | Uses /comet-tweak for a lightweight change |

## Verification

Confirm the README and a representative skill body resolve on the master branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/rpamis/comet/master/README.md | head -40
curl -sL https://raw.githubusercontent.com/rpamis/comet/master/assets/skills/comet/SKILL.md | head -40
```

Both URLs return 200. After installing, review each assets/skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Fail and Warn verdicts noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| comet | Warn | Pass | Warn |
| comet-build | Pass | Pass | Pass |
| comet-archive | Pass | Pass | Pass |
| comet-verify | Pass | Pass | Fail |
| comet-design | Warn | Pass | Pass |
| comet-open | Pass | Pass | Fail |
| comet-tweak | Pass | Pass | Pass |
| comet-hotfix | Pass | Pass | Warn |
| comet-any | Pass | Pass | Pass |
| comet-native | Pass | Pass | Fail |
| comet-classic | Pass | Pass | Pass |
| comet-review | Pass | Pass | Pass |
| comet-safe-delivery | Pass | Pass | Pass |
| comet-runtime-diagnose | Pass | Pass | Pass |
| comet-release | Pass | Pass | Pass |

15 of the 24 indexed listings were sampled; nine pass all three checks, three carry a Snyk Fail (comet-verify, comet-open, comet-native), and three carry at least one Warn (comet has a Warn in both Gen Agent Trust Hub and Snyk, comet-design and comet-hotfix one each).

## Limitations

- Snapshot data, verified Nov 25, 2026: 9,828 combined installs across 24 indexed listings; 3,317 GitHub stars; MIT license; last pushed Nov 25, 2026. Counts drift over time.
- The default branch is master, not main; every raw URL in this guide uses master, and scripts that assume main will 404.
- skills.sh sampled only 15 of the 24 indexed listings for verdicts; the nine un-sampled listings (the comet-github family, comet-bilingual-docs, comet-memory, and grill-test) carry no published verdict.
- Three sampled listings carry a Snyk Fail and three carry at least one Warn; review those security pages before production use.
- Comet is a large, fast-moving platform (over 4,000 tracked files) with its own CLI and configuration; installation commands and entry points can change between releases.

## Related

[Vigiles - Agent Harness Quality Suite Setup](/hermes/skills/catalog/vigiles-setup) | [AI Evals Skills - Product-Specific Evaluations](/hermes/skills/catalog/ai-evals-skills-setup) | [Walden - Spec-Driven Development with Executable Proofs](/hermes/skills/catalog/walden-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Remember the low-memory entry point: /comet to enter the project workflow, /comet-any to create workflow applications, and `comet eval` to evaluate any skill.
- `comet init --workflow classic` or `--workflow both` selects the OpenSpec + Superpowers flow; Native is the default for new projects.
- For Hermes or any host that uses the generic skills CLI, install with `npx skills add rpamis/comet`.
- Comet supports 39 AI coding platforms; check the Supported Platforms table in the README for your host's skills directory.
- Prefer Native for strong models that implement and verify autonomously; Classic is for work that needs full Spec/TDD phase constraints.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
