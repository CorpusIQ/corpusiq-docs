---
title: "CCFA Skills - Academic Paper and Research Suite"
description: "mikubaka88/ccfa-skills: 33.9K combined installs. Eighteen linked skills that carry a paper from idea to review, rebuttal and submission."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ccfa-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "academic writing", "research", "latex"]
---

# CCFA Skills - Setup Guide

**Source:** [mikubaka88/ccfa-skills](https://www.skills.sh/mikubaka88/ccfa-skills) via skills.sh - 33.9K combined installs across 24 indexed listings; first seen 2026-10-31 (morning sweep)

**GitHub:** [mikubaka88/ccfa-skills](https://github.com/mikubaka88/ccfa-skills) - 3,358 stars, MIT, branch main, last pushed 2026-10-31; 18 `SKILL.md` directories at the repository root, one per skill, with the LaTeX venue templates kept beside them in `ccf-latex-templates/` rather than inside any skill

**Category:** Academic research and paper writing for agents: literature work, LaTeX, review and submission prep

**Quality Tier:** 🟢 Green - the three sampled skills Pass all three auditors and the repository is MIT-licensed markdown plus Python helper scripts, with no package install

CCFA-Skills is a family rather than a toolbox. Eighteen skills are arranged along the life of a CCF-A paper, and the design assumption is that a single long prompt cannot both retrieve faithfully and write well, so the work is split by the kind of judgement it needs: `ccf-idea-reviewer` judges an idea while `ccf-idea-optimizer` develops one, `ccf-paper-reviewer` reviews while `ccf-paper-writer` revises, and `ccf-integrity-auditor` checks that claims, numbers, terminology and citations still match their evidence. Two preflight skills run in front of everything: `ccf-humanization` first, which strips defensive and process language from the prose, then `ccf-common`, which applies scope, evidence and file rules. Every one of the eighteen descriptions states what the skill owns and what belongs to a neighbour, which is the most disciplined handoff design in this catalog.

The practical consequence is that a partial install is a bad install. The README says plainly that partial installs must include `ccf-humanization` and `ccf-common` and must not copy only a `SKILL.md`, and the docs warn that the LaTeX templates and other sibling resources are not installed by the skills CLI at all. Take the whole 18 or take a documented subset with both preflights, and add the templates by hand if you intend to build PDFs.

## Installation

The README's one-line route installs all 18 skills for a named agent. The command is shown in a PowerShell fence, but it is a plain `npx` invocation:

```bash
npx skills add mikubaka88/CCFA-Skills --global --agent codex --skill '*' --yes --copy
```

Swap the agent identifier for the client you actually use, and use `--all` to hit every detected agent:

```bash
npx skills add mikubaka88/CCFA-Skills --global --agent <agent-id> --skill '*' --yes --copy
npx skills list --global --agent <agent-id>
npx skills add mikubaka88/CCFA-Skills --all
```

Updates are a separate command, and with `--copy` a source refresh also needs the installed copies refreshed:

```bash
npx skills update --global --yes
```

The README's own preference is the lean 0.12.1 release package rather than the full repository, because the repository also ships complete paper PDFs as research material. The release is extracted and installed with the local installer described in `docs/INSTALLATION_MATRIX.md`, which previews the change and leaves personal preferences untouched.

For this profile, copy the 18 skill folders directly. Keep `ccf-latex-templates/` out of the skills directory and place it only if you need venue templates:

```bash
git clone --depth 1 https://github.com/mikubaka88/CCFA-Skills.git /tmp/ccfa-skills
cp -r /tmp/ccfa-skills/ccf-common /tmp/ccfa-skills/ccf-humanization \
      /tmp/ccfa-skills/ccf-idea-reviewer /tmp/ccfa-skills/ccf-idea-optimizer \
      /tmp/ccfa-skills/ccf-literature-searcher /tmp/ccfa-skills/ccf-literature-monitor \
      /tmp/ccfa-skills/ccf-experiment-designer /tmp/ccfa-skills/ccf-research-engineer \
      /tmp/ccfa-skills/ccf-paper-writer /tmp/ccfa-skills/ccf-paper-reviewer \
      /tmp/ccfa-skills/ccf-integrity-auditor /tmp/ccfa-skills/ccf-visual-composer \
      /tmp/ccfa-skills/ccf-rebuttal-writer /tmp/ccfa-skills/ccf-submission-checker \
      /tmp/ccfa-skills/ccf-paper-to-exemplar /tmp/ccfa-skills/ccf-pipeline-orchestrator \
      /tmp/ccfa-skills/ccf-project-scaffolder /tmp/ccfa-skills/ccf-skill-forger \
      ~/.hermes/profiles/corpusiq/skills/
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ccf-common | 2,070 | The shared preflight that runs after humanization: routing, scope, prerequisites, evidence rules, handoffs and artifact contracts. |
| ccf-paper-writer | 2,027 | Drafting, revising, polishing and compressing manuscript prose, including abstracts, sections and slides, with evidence preserved. |
| ccf-humanization | 2,012 | The first preflight for every other skill: removing empty defensive framing while keeping uncertainty and evidence intact. |
| ccf-paper-reviewer | 2,009 | Structured scientific or writing review without rewriting, including version comparison and a readiness judgement. |
| ccf-idea-optimizer | 2,009 | Developing a rough idea into a problem, insight, mechanism and evidence plan. |
| ccf-literature-searcher | 2,003 | Finding and verifying prior art, datasets, benchmarks and citation candidates. |
| ccf-experiment-designer | 2,002 | Experiment design and interpretation: datasets, baselines, metrics, ablations and result-table contents. |
| ccf-integrity-auditor | 1,997 | Auditing existing claims, numbers, terminology and citations against supplied or verified evidence. |
| ccf-idea-reviewer | 1,993 | Judging an idea for value, novelty, insight and mechanism, defaulting to concept-only review without experiments. |
| ccf-literature-monitor | 1,990 | Scanning arXiv, OpenReview, venue feeds and competitor labs for overlap, with dated evidence since the prior scan. |
| ccf-visual-composer | 1,983 | Rendering and redesigning scientific figures, visual tables and method diagrams as GPT Image 2, pure SVG or editable SVG, PDF or PPTX. |
| ccf-paper-to-exemplar | 1,980 | Distilling supplied paper PDFs into writing exemplar cards that transfer argument structure without copying claims. |
| ccf-pipeline-orchestrator | 1,974 | Planning and coordinating research stages, goals, gates and `ccfa.yaml` state, including explicitly requested autonomous iterations. |
| ccf-submission-checker | 1,972 | Checking venue rules and the submission package: template, page limits, anonymity, PDF build and metadata. |
| ccf-rebuttal-writer | 1,969 | Writing rebuttals, author responses, revision ledgers and resubmission plans grounded in feasible changes. |
| ccf-skill-forger | 1,968 | Maintaining the family itself: triggers, references, scripts, diagrams, install dependencies and release validation. |
| ccf-project-scaffolder | 1,968 | Initialising the project folder structure, LaTeX templates, artifact directories and `ccfa.yaml`. |
| ccf-research-engineer | 3 | Implementing research code: codebase selection, baseline reproduction, mechanism implementation and training diagnostics. |
| forge-skills | 1 | Name-only listing with no directory in the clone; the shipped maintenance skill is `ccf-skill-forger`. |
| ccf-writing-skills | 1 | Name-only listing with no directory in the clone; the writing skills that ship are `ccf-paper-writer` and `ccf-humanization`. |
| ccf-paper-compressor | 1 | Name-only listing with no directory in the clone; compression is part of `ccf-paper-writer`. |
| ccf-literature-search | 1 | Name-only listing with no directory in the clone; the shipped equivalent is `ccf-literature-searcher`. |
| ccf-conference-paper-reviewer | 1 | Name-only listing with no directory in the clone; the shipped equivalent is `ccf-paper-reviewer`. |
| ccf-conference-paper-rebuttal | 1 | Name-only listing with no directory in the clone; the shipped equivalent is `ccf-rebuttal-writer`. |

All 24 indexed listings clear the threshold and appear in the table.

The threshold for this guide is zero, so the table is the whole index rather than a head. That exposes the shape of the repository honestly: seventeen skills carry between 1,968 and 2,070 installs each, `ccf-research-engineer` carries 3 despite shipping a full skill directory, and six listings carry a single install each and have no folder at all.

## Why This Matters for Hermes Agents

Research writing fails an agent in ways that look like success. The prose is fluent, the sections are present, and the citations are invented. CCFA-Skills attacks that with role separation and an evidence rule in `ccf-common`: claims, numbers, terminology and citations must resolve to supplied or verified material, and a missing fact stays missing rather than being filled in plausibly. That is the single most valuable property of this pack for an agent that writes unattended, and it is why the integrity auditor and the humanization preflight are worth having even if you never touch the rest.

The second property is that the skills know the difference between diagnosing and repairing. `ccf-paper-reviewer` returns a review and refuses to rewrite; `ccf-paper-writer` writes and does not judge. When an agent is asked to "improve this paper" it tends to do both at once and produces a document that argues with its own review. Splitting the two is what makes the review usable as an input rather than as a tone.

The third is the figure path. `ccf-visual-composer` generates an aesthetic draft first and then asks whether to rebuild it as editable SVG, PDF or PPTX, which is the opposite of the usual behaviour of producing a flat image nobody can revise. Values and topology are meant to be preserved, so a quantitative plot stays reproducible while a method diagram becomes editable.

Cost is moderate for a suite this disciplined: 18 markdown bundles plus Python helper scripts, with the heavy material in references. The Chinese-first documentation is the real entry cost for an English reader, since quite a few of the docs pages and skill instructions are written in Chinese with English mirrors only for the top-level README.

## Usage

| You say | What happens |
|---|---|
| "Rank these three thesis directions and say why each would be rejected" | `ccf-idea-reviewer` scores value, novelty and mechanism without asking for experiments, and names the likeliest rejection reason for each. |
| "Find recent work and published baselines on this task" | `ccf-literature-searcher` retrieves and verifies sources, leaving recurring tracking to `ccf-literature-monitor`. |
| "Design the ablations for this method without inventing results" | `ccf-experiment-designer` produces datasets, baselines, metrics and the result-table structure, and refuses to fill in numbers. |
| "Rewrite the method section in CVPR style, keeping equations and citations" | `ccf-paper-writer` rewrites with evidence preserved, and `ccf-humanization` keeps the result out of defensive register. |
| "Check whether every number in the abstract matches the tables" | `ccf-integrity-auditor` audits claims, values and citations against the supplied evidence rather than re-reviewing the paper. |
| "Draw the method architecture, then let me decide about PPTX" | `ccf-visual-composer` drafts the figure and offers the editable reconstruction path instead of a flat image. |
| "The reviews are in and we have one week" | `ccf-rebuttal-writer` builds the response letter and revision ledger, grounding every promise in a feasible change. |

## Verification

The raw path for the shared preflight returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} ccf-common\n" \
  https://raw.githubusercontent.com/mikubaka88/CCFA-Skills/main/ccf-common/SKILL.md
```

Expect `200`. After the copy lands, confirm the count and read one header:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/ccf-* | wc -l
head -6 ~/.hermes/profiles/corpusiq/skills/ccf-common/SKILL.md
```

The count should print 18, and the header should show `name: ccf-common`, a single-line quoted `description:` and a `metadata:` block carrying `ccf_skill_controls`. Check that both preflights are present before you trust any output, since the family assumes they run first:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/ccf-humanization \
      ~/.hermes/profiles/corpusiq/skills/ccf-common
```

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ccf-common | Pass | Pass | Pass |
| ccf-experiment-designer | Pass | Pass | Pass |
| ccf-pipeline-orchestrator | Pass | Pass | Pass |
| forge-skills | ? | ? | ? |
| ccf-conference-paper-rebuttal | ? | ? | ? |

Three sampled skills Pass all three auditors with no Warn and no Fail anywhere in the sample, which is why this guide is tiered Green. The two listings that return nothing are the same two that have no directory in the clone, so the missing verdicts follow the missing code rather than hiding a finding.

The install surface is small and legible. Each skill is a `SKILL.md` plus a references folder, with Python helpers under `ccf-common/scripts/` for the preference configurator, and a `tools/` directory at the repository root. There is no package to install, no build step and no postinstall hook, so the risk is what the instructions tell an agent to run. The one script worth reading before use is the local configurator, which is started with `python ccf-common/scripts/preferences.py serve` and writes preferences outside the installed skill folders so they survive updates; give it a project path and it writes per-paper settings instead.

The judgement call is the content side. `ccf-research-engineer` selects codebases, reproduces baselines and debugs training runs, which means executing third-party research code on your machines, and `ccf-visual-composer` can call an image generation model. Neither installs anything by itself, but both widen what an unattended agent may do. The licence is MIT, so redistribution is uncomplicated, though the attribution rule for exemplar cards should be respected: `ccf-paper-to-exemplar` transfers argument structure, not claims, and it says so.

## Limitations

- Snapshot data, verified 2026-10-31: 33,935 combined installs across 24 indexed listings; 3,358 GitHub stars; MIT; last pushed 2026-10-31. Counts drift over time.
- The index has drifted past the tree. 24 listings are indexed against 18 skill directories, and six listings have no folder: `forge-skills`, `ccf-writing-skills`, `ccf-paper-compressor`, `ccf-literature-search`, `ccf-conference-paper-reviewer` and `ccf-conference-paper-rebuttal`. Every one holds a single install, so they look like early names that were superseded by the `ccf-*` scheme rather than live skills.
- Install counts are not a ranking. Seventeen skills sit in a 102-install band between 1,968 and 2,070, which is what a family installed as a unit looks like, while `ccf-research-engineer` holds 3 installs despite being one of the eighteen shipped skills and one of the most demanding.
- A partial install breaks the design. Every skill assumes `ccf-humanization` and then `ccf-common` run before it, and the README states that partial installs must include both and must not copy only a `SKILL.md`.
- The skills CLI does not install the LaTeX templates. Venue templates for AAAI, ACL, ACM, CVPR and the rest live in `ccf-latex-templates/`, outside every skill folder, and have to be added from the same version by hand or through the installation matrix.
- The documentation is Chinese-first. `README.md` is the primary file, English is a mirror, and several docs pages and in-skill instructions are Chinese only, so an English-only reader will hit untranslated guidance.
- The suite is opinionated about venue. It is built around CCF-A conference submissions and their review cycle, including the day and night preference modes, so a journal workflow, a workshop paper or a non-academic technical report is a poor fit for the review and submission skills.
- Success depends on the agent honoring the handoffs. Reviewer-versus-writer separation is prose in each `SKILL.md`, not enforcement, and an agent asked to "fix this paper" will happily do both jobs at once unless the request is split.

## Related

- [Nature Skills - Academic Writing Setup](/hermes/skills/catalog/nature-skills-setup)
- [Jwynia Agent Skills - Presentation and Writing Suite](/hermes/skills/catalog/jwynia-agent-skills-setup)
- [Hermes ArXiv Agent - ArXiv Paper Fetcher Setup](/hermes/skills/catalog/hermes-arxiv-agent-setup)
- [HuggingFace Agent Skills - Datasets, Papers, ML Tools Setup](/hermes/skills/catalog/huggingface-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install all 18 even if you only write papers occasionally. The family is designed as a chain, and dropping `ccf-humanization` or `ccf-common` removes the evidence rules that make the rest trustworthy.
- Ask for review and revision in separate turns. `ccf-paper-reviewer` will not rewrite and `ccf-paper-writer` will not judge, so a single "make this better" request gets the weakest version of both.
- Use `ccf-integrity-auditor` before every submission, not just when something feels wrong. It checks numbers, terminology and citations against evidence, which is the failure mode that survives fluent prose.
- Set the preference mode per project rather than globally. `python ccf-common/scripts/preferences.py serve --project "path/to/paper"` keeps a submission-ready paper in review mode while everyday work stays light.
- Reach for `ccf-experiment-designer` before `ccf-research-engineer`. The designer fixes protocols, baselines and metrics; the engineer then has something to implement against, and the split is what stops invented results.
- Read the Chinese pages when the English mirror is thin. The family's most specific guidance, including the day and night control semantics, is written for the primary audience first.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
