---
title: "Ane Work Package - Research and Ops Skills Setup"
description: "gasserane/personal-skills: 22.2K combined installs across 52 listings, a MEL and SRHR specialist's own working set: evidence synthesis, memos, briefs"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gasserane-personal-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "monitoring and evaluation", "research", "evidence synthesis"]
---

# Ane Work Package - Setup Guide

**Source:** [gasserane/personal-skills](https://www.skills.sh/gasserane/personal-skills) via skills.sh - 22.2K combined installs across 52 indexed listings; first seen Nov 11, 2026
**GitHub:** 3 stars, no license file, `main` branch, last pushed 2026-11-11, 56 `SKILL.md` files in the tree against 52 indexed listings, 270 files in total
**Category:** Monitoring, evaluation and research operations for a single senior specialist
**Quality Tier:** 🟡 Yellow - a personal working set with real domain depth, but an empty README and no licence.

This is not a product. It is one specialist's skill directory published as a repository: 52 indexed listings that all appeared on Nov 11, 2026, and a README whose entire content is the heading `# anework-package`. The publisher works in monitoring, evaluation and research for sexual and reproductive health and rights programmes, and every skill in the tree is written for that job rather than for a general audience.

What makes it worth reading is the shape rather than the marketing. There are domain skills (evidence synthesis, instrument design, indicator design, theory of change, Power BI builds), document skills (decision memos, daily briefs, meeting notes, proposal and contract review), and then a meta layer that most packs never build: three personas, a session wrap-up, a system audit and a grading system that scores the system's own output.

The install index runs from 3 to 742, and the twenty largest listings sit between 647 and 742, a spread of 95. That flatness is the signature of a directory installed as a unit, so the numbers describe the package rather than the individual skills.

## Installation

The publisher README documents nothing. Its whole body is the single heading `# anework-package`, with no install command, no skill list and no description of what any directory does. The only published install path is the one on the pack's own skills.sh source page:

```bash
npx skills add gasserane/personal-skills
```

A single skill can be pulled with the CLI's `--skill` flag, which is documented by the CLI itself rather than by this repository:

```bash
npx skills add gasserane/personal-skills --skill evidence-synthesis
```

Check the tree before installing. It carries 56 `SKILL.md` files against 52 indexed listings, so four skills ship without an install count, and a few paths live under `org/` instead of `skills/`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| journal-reflection | 742 | Structured end-of-day, end-of-week and post-decision reflection instead of a freeform notebook. |
| evidence-synthesis | 714 | Rapid evidence assessments and systematic-lite literature reviews for MEL and SRHR questions. |
| daily-brief | 705 | A scannable morning briefing for a senior MEL and SRHR specialist. |
| video-content-analysis | 689 | Turning FGD, webinar and SBCC video into an artefact pack: transcript, frames, manifest, Tier 1 notes. |
| decision-memo | 687 | A structured decision memo or decision doc on request. |
| power-bi-build | 686 | IPPF-branded Power BI artefacts built, scaffolded or updated from analytical input. |
| mel-framework-citation | 680 | Enforces the IPPF, UNFPA and UNAIDS citation standard on MEL and SRHR output. |
| researcher | 677 | An evidence synthesis specialist persona for complex MEL and SRHR tasks. |
| ane-voice | 677 | Audits and rewrites AI-drafted prose into the owner's own MEL and SRHR voice without losing rigour. |
| ann | 676 | A convener persona that takes any analytical, evaluation or structured-output request and routes it. |
| vi | 675 | An execution orchestrator that receives an approved plan and runs the roster of work. |
| li | 675 | Knowledge manager for the personal library and MEL wiki: cataloguing, retrieval, reorganisation. |
| instrument-designer | 668 | Data-collection instruments to IPPF and UNFPA publication standard: questionnaires and survey tools. |
| wrap-up | 662 | Session close-out: gathers git state, errors and pending actions, then records them. |
| system-audit | 660 | Quality, sanity and efficiency audit of the whole setup: personas, wiki and skills. |
| indicator-designer | 657 | MEL and SRHR indicators written to IPPF, UNFPA and UNAIDS publication standard. |
| grade-system | 656 | Substantive quality and reliability grading applied to the system's own output. |
| learning-agenda | 651 | A learning agenda in one of three formats, from the canonical federation agenda to a quarterly RAG summary. |
| learning-product | 650 | Converts a Researcher evidence brief into one of four learning products. |
| toc-builder | 647 | Theory of Change built against Vogel (2012) DFID criteria and a second published framework. |

The remaining 32 indexed listings range from 3 to 644 installs.

## Why This Matters for Hermes Agents

Most published skill packs are organised by tool or by platform. This one is organised by the working week of a single analyst, which is a much better map of where an agent actually fails in research work: not at the retrieval step, but at the point where evidence has to become a defensible sentence.

The citation skill is the clearest example. `mel-framework-citation` does not summarise sources, it enforces a house standard across three agencies on anything the agent writes, which is the difference between output that can leave the building and output that has to be rewritten.

The instrument and indicator skills carry the same idea into data collection, where a badly worded question is expensive to discover after fieldwork. The theory of change builder pins a published evaluation framework to the output rather than letting the model improvise causal logic.

The meta layer is the transferable part. `wrap-up`, `system-audit`, `grade-system` and `improve-system` treat the agent setup as something to be audited and graded on a schedule, and `ann`, `vi`, `li` and `researcher` split convening, execution, knowledge management and deep research into separate roles.

Anyone building a multi-skill agent stack can copy that shape without copying the domain content: one router, one executor, one librarian, one specialist, plus a close-out and an audit.

The cost is coupling. These skills assume a file system, a wiki and a house style, so the useful reading is the pattern, not the prompts.

## Usage

| You say | What happens |
|---|---|
| "What did I decide about the indicator set, and why?" | Runs `decision-memo` and returns the memo structure with the options and the recorded rationale. |
| "Pull together what we know about condom use among adolescents" | Runs `evidence-synthesis` and returns a rapid assessment with sources graded. |
| "Draft the questionnaire for the clinic exit survey" | Runs `instrument-designer` and returns the instrument to IPPF and UNFPA publication standard. |
| "Build the ToC for the new programme" | Runs `toc-builder` and returns a theory of change on the named DFID criteria. |
| "Turn this webinar recording into something I can use" | Runs `video-content-analysis` and returns a transcript, frames and a manifest. |
| "Does this draft sound like me, or like a model?" | Runs `ane-voice` and rewrites the passage into the owner's register. |
| "Grade the last deliverable before it goes out" | Runs `grade-system` and returns a quality and reliability grading. |
| "Close the session and tell me what is outstanding" | Runs `wrap-up` and returns git state, errors and pending actions. |

## Verification

Read two skills on the branch before installing. Both paths return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/gasserane/personal-skills/main/skills/evidence-synthesis/SKILL.md | head -10
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/gasserane/personal-skills/main/org/toc-builder/SKILL.md
```

After installation, count the directories that landed: `ls ~/.claude/skills | wc -l` for a single-agent install, or check the equivalent skills directory for the agent you use. Expect more than 52 folders, because the tree carries 56 files, and confirm that the four `org/` skills (indicator-designer, toc-builder, mel-discipline, session-wrap-up) arrived with their folder names intact.

This is not a text-only pack. The 270 files include 76 Python scripts, three PowerShell files and a small WAV fixture, mostly helpers under `skills/srhr-map`, `skills/literature`, `skills/localise` and the `tools/` publishing utilities. Read a script before you let a skill run it.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| journal-reflection | Pass | Pass | Pass |
| evidence-synthesis | Pass | Pass | Warn |
| daily-brief | Pass | Pass | Warn |
| video-content-analysis | Pass | Pass | Warn |

Only four of the 52 listings carry published verdicts, so the table is a sample rather than a clearance. All four are instruction files, and the three Snyk Warns sit on skills that pull in outside material: literature, daily reading and recorded media. Read those three before pointing them at anything confidential, because the ingestion is described in the prompt rather than in code you can audit.

## Limitations

- Snapshot data, verified 2026-11-13: 22,154 combined installs across 52 indexed listings; 3 GitHub stars; no license file; last pushed 2026-11-11. Counts drift over time.
- The README is a single heading. There is no install documentation, no skill inventory and no statement of what the package is for, so everything in this guide comes from the tree and from the skills.sh listing rather than from the publisher.
- No licence file anywhere in the repository. Without one, the default all-rights-reserved position applies, so treat the content as readable reference material and check with the publisher before redistributing it or shipping it inside a product.
- Several skills encode one person's working style and one organisation's context: a named house citation standard, a named wiki, an owner's voice and a fixed persona roster. They need adaptation, not just installation.
- The tree carries 56 `SKILL.md` files against 52 indexed listings, so four skills have no install count. Four skills sit under `org/` rather than `skills/` (indicator-designer, toc-builder, mel-discipline, session-wrap-up), and the pack ships 76 Python scripts in skill-level `scripts/` folders, which is worth knowing before you script a copy.
- Three stars against 22.2K installs means this is being installed quietly, with very little public review to lean on.

## Related

- [Education Agent Skills - 165 Teaching Skills](/hermes/skills/catalog/education-agent-skills-setup)
- [PM Skills - Product Management Lifecycle Suite Setup](/hermes/skills/catalog/pm-skills-setup)
- [Metabase Skills - BI and Dashboard Agent Suite](/hermes/skills/catalog/metabase-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `ann`. It is the router, and the rest of the roster assumes a request has been framed before it runs.
- Read `mel-framework-citation` first if you work in a regulated or donor-funded field. It is the skill that decides whether output is publishable, and it constrains the others.
- Treat `system-audit` and `grade-system` as the template to copy. A pack that can grade its own output is worth more than one more domain skill.
- Keep `ane-voice` as the last step before delivery. Applied early it fights the citation skill, applied last it fixes register without touching substance.
- Strip the organisation-specific names before reuse. Replace the house standard, the wiki and the voice profile with your own, then re-read the skill for leftover assumptions.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
