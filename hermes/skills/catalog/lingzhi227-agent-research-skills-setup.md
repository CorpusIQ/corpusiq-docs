---
title: "Agent Research Skills - Academic Paper Suite Setup"
description: "lingzhi227/agent-research-skills: 57.8K combined installs. 31 skills for literature review, paper writing, LaTeX, citations and rebuttals."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/lingzhi227-agent-research-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "academic research", "latex"]
---

# Agent Research Skills - Setup Guide

**Source:** [lingzhi227/agent-research-skills](https://www.skills.sh/lingzhi227/agent-research-skills) via skills.sh - 57.8K combined installs across 31 indexed listings; first seen Feb 20, 2026
**GitHub:** [lingzhi227/agent-research-skills](https://github.com/lingzhi227/agent-research-skills) (433 stars; no LICENSE file, GitHub reports no license; pushed 2026-02-27; layout `skills/<name>/SKILL.md` for 31 skills, with `scripts/*.py` in 16 of them and `references/*.md` in 28, plus `install.sh`, `commands/research.md`, `CHANGELOG.md` and two design notes)
**Category:** Research / Academic Writing
**Quality Tier:** 🔵 Community (broad, script-backed and coherent, but the published skills.sh audits are mixed: Snyk Fail on citation-management with a HIGH risk finding, Warn from Snyk and Socket on the flagship research skills, and no LICENSE file in the repo)

Agent Research Skills is a 31-skill pipeline for the academic paper lifecycle, from literature search to conference slides. The author describes it as extracted from 17 GitHub repos studying LLM-agent-driven research automation, and the structure shows it: skills are grouped into phases (discovery and planning, method design, experiments, writing, figures and citations, LaTeX and compilation, review and polish) and cross-link through `## Related Skills` sections as upstream or downstream.

This is not a prompt pack. Sixteen skills ship Python scripts with argparse CLIs - literature search against Semantic Scholar, arXiv, OpenAlex and CrossRef, PDF extraction, a paper database, BibTeX harvesting and validation, LaTeX compilation with error-fix loops, statistical summaries, figure templates - and the README states the scripts are stdlib-only where possible. `paper-assembly` is the orchestrator that runs the phases with checkpointing.

## Installation

```bash
npx skills add lingzhi227/agent-research-skills -g -a claude-code
```

The `-g` flag is not optional in practice: the README states the scripts use `~/.claude/skills/` paths and require a global install.

```bash
# Post-install: slash commands, dependency check, script syntax verification
git clone https://github.com/lingzhi227/agent-research-skills.git /tmp/agent-research-skills
/tmp/agent-research-skills/install.sh
rm -rf /tmp/agent-research-skills
```

```bash
# Dependencies the README lists, installed only if you use the skills that need them
pip install PyMuPDF        # self-review, deep-research: PDF parsing
pip install numpy scipy    # data-analysis: statistical tests
```

Semantic Scholar key, if you want the higher rate limits the README mentions: create `~/keys.md` with the line `S2_API_Key: your-key-here`. Python 3 is required for every script.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| literature-review | 3,987 | Multi-perspective literature review: generate expert personas, run grounded Q&A dialogues and synthesise the findings into structured knowledge |
| literature-search | 2,608 | Multi-source academic search across Semantic Scholar, arXiv, OpenAlex and CrossRef, returning JSONL with title, authors, venue, citations and BibTeX |
| figure-generation | 2,242 | Publication-quality matplotlib figures through a three-phase pipeline: query expansion, code generation with execution, then VLM visual feedback |
| latex-formatting | 2,206 | Conference templates for ICML, ICLR, NeurIPS, AAAI and ACL, package and formatting fixes, pre-submission checks |
| math-reasoning | 2,146 | Derivations, proofs, problem formalisation, statistical test selection and LaTeX notation tables |
| backward-traceability | 2,123 | Ties every number in the finished PDF to the code line that produced it, using hypertarget and hyperlink pairs plus num checks |
| citation-management | 2,098 | BibTeX harvesting from a draft, cite key validation against the .bib file, deduplication and bibliography formatting |

The remaining 24 indexed listings range from 1,519 to 1,965 installs and carry the substance of the pipeline: data-analysis 1,965, deep-research 1,874, idea-generation 1,801, novelty-assessment 1,785, paper-writing-section 1,778, paper-revision 1,771, github-research 1,763, experiment-design 1,762, research-planning 1,744, survey-generation 1,687, algorithm-design 1,680, code-debugging 1,661, rebuttal-writing 1,655, related-work-writing 1,638, table-generation 1,625, self-review 1,616, paper-compilation 1,592, slide-generation 1,591, atomic-decomposition 1,589, paper-to-code 1,572, experiment-code 1,570, paper-assembly 1,568, symbolic-equation 1,546 and excalidraw-skill 1,519. The tight 1,519 to 1,965 band suggests the suite is usually installed as a unit rather than skill by skill.

## Why This Matters for Hermes Agents

Research agents fail on provenance. A model asked to summarise a field will produce plausible citations, and a model asked to report numbers will produce numbers with no path back to the run that made them. This suite attacks both: `literature-search` queries real APIs and returns structured records with BibTeX, `citation-management` validates cite keys against the actual .bib file, and `backward-traceability` makes every number in the PDF a hyperlink to the code line that produced it.

The second gain is the review loop. `self-review` runs the NeurIPS review form with three reviewer personas and ensemble scoring, `paper-revision` maps reviewer concerns onto sections, and `rebuttal-writing` produces point-by-point responses. That is the part of paper work agents are usually worst at, because it needs a hostile reader rather than a helpful one, and the personas supply the hostility on demand.

The third is that the scripts make the skills executable rather than advisory. `paper-compilation` runs pdflatex and bibtex with an auto-fix loop, `latex-formatting` checks venue compliance before submission, `table-generation` converts JSON or CSV into booktabs tables with bold-best and significance stars. An agent can run these and read the output, which turns "looks done" into "compiles clean".

The tradeoff is real and it belongs in the same breath: this is the most script-heavy suite in the academic category, and it carries the only Snyk Fail found in this batch. Read the Security section before installing it near a credential store.

## Usage

| You say | What happens |
|---|---|
| "Do a literature review on protein folding with LLMs" | literature-review runs the multi-persona dialogue workflow and literature-search pulls the underlying papers from the four indexes |
| "Search arXiv, OpenAlex and Semantic Scholar for long-context attention" | literature-search queries all configured sources and returns ranked JSONL with citations and BibTeX |
| "Make publication figures from results.csv" | figure-generation writes matplotlib code, executes it and reviews the rendered output through a VLM feedback loop |
| "Format this draft for NeurIPS submission" | latex-formatting applies the venue template and runs the pre-submission checks |
| "Check whether my idea is actually novel" | novelty-assessment runs multi-round search and critique with a harsh critic persona and returns a binary decision with justification |
| "Write the rebuttal for these reviewer comments" | rebuttal-writing maps each concern to an evidence-based response, and paper-revision applies the accepted edits |
| "Every number in my PDF needs to trace to code" | backward-traceability instruments the LaTeX so each reported value hyperlinks to the code line behind it |

## Verification

Read the flagships before installing anything. All four URLs below returned HTTP 200 when checked with curl on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/lingzhi227/agent-research-skills/main/README.md
curl -sL https://raw.githubusercontent.com/lingzhi227/agent-research-skills/main/skills/literature-review/SKILL.md
curl -sL https://raw.githubusercontent.com/lingzhi227/agent-research-skills/main/skills/deep-research/SKILL.md
curl -sL https://raw.githubusercontent.com/lingzhi227/agent-research-skills/main/skills/citation-management/SKILL.md
```

Then run the repo's own dependency check, and confirm the scripts actually execute:

```bash
./install.sh --check
python3 ~/.claude/skills/literature-search/scripts/search_arxiv.py --help
```

`install.sh` verifies dependencies and script syntax, and it tracks a list of 30 skills - `github-research` (added in 1.1.0) is not in that list, so a clean report does not cover it.

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| literature-review | Pass | Pass | Warn |
| deep-research | Pass | Warn | Warn |
| citation-management | Warn | Warn | Fail |

These are the only non-Pass verdicts in this batch, and they point at one shared cause. Snyk rates citation-management HIGH with W007 (insecure credential handling): the SKILL.md shows a command that extracts the Semantic Scholar key with `grep S2_API_Key /Users/lingzhi/Code/keys.md | cut -d: -f2` and passes it straight in as `--api-key`, which puts the secret in the model's context and the shell history. Gen Agent Trust Hub files the same pattern under CREDENTIALS_UNSAFE and DATA_EXFILTRATION, with INDIRECT_PROMPT_INJECTION and EXTERNAL_DOWNLOADS alongside; Socket raises a low-severity anomaly for "forwarding a plaintext API key from a personal file into unseen local cross-skill scripts". The second finding, W011, applies to the literature skills generally: they fetch third-party papers chosen by generated queries, so untrusted text enters the context by design.

Beyond the verdicts, the permissions the files ask for are substantial. Sixteen skills ship Python scripts; several of them make outbound calls to Semantic Scholar, arXiv, OpenAlex, CrossRef, GitHub and Papers with Code, and write downloaded PDFs and JSONL databases to disk. `paper-compilation` shells out to pdflatex and bibtex. `excalidraw-skill` needs a running canvas server (`EXPRESS_SERVER_URL`, default `http://localhost:3000`) and drives it over MCP with element-level writes and deletes. No skill declares an `allowed-tools` block, so the host's tool policy is the only brake. If you install this suite, create the key file yourself, keep the key out of the prompt (export it as an environment variable and edit the SKILL.md examples), and run the writing and compilation skills in a directory you are willing to have overwritten.

## Limitations

- No LICENSE file, and GitHub reports no license, so the default all-rights-reserved position applies. Ask the author before using the skills or scripts in anything redistributed.
- Hardcoded personal paths. `citation-management` and `literature-search` read `/Users/lingzhi/Code/keys.md`, and `deep-research` writes to `/Users/lingzhi/Code/deep-research-output/{slug}/`. The README documents `~/keys.md` and `~/deep-research-output/` instead, so the docs and the skill files disagree; edit both before the first run.
- The README's design-notes link points at `/Users/lingzhi/Code/research-engine/SKILLS_DESIGN.md`, which is the author's local filesystem and does not resolve for anyone else.
- `install.sh` checks 30 skills while the tree holds 31: `github-research`, added in 1.1.0, is missing from its list, and its output says "30 skills" either way.
- Runtime dependencies are uneven. PDF parsing needs PyMuPDF, statistics need numpy and scipy, compilation needs a working TeX distribution, and the diagramming skill needs a separate canvas server. A bare install gets you prompts and no tooling.
- Audit verdicts are mixed and one is a Snyk Fail with a HIGH risk rating (see Security). The suite is best treated as a research assistant that runs in a sandbox, not as a trusted dependency.
- Snapshot data, verified Oct 26, 2026: 57,762 combined installs across 31 indexed listings; 433 GitHub stars; no license; last pushed 2026-02-27. Counts drift over time.

## Related

- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup) - the closest catalogue neighbour: imbad0202/academic-research-skills ships 4 prompt-level skills at 26.4K installs (academic-paper, academic-paper-reviewer, deep-research, academic-pipeline), where this suite ships 31 skills at 57.8K with 16 script-bearing skills, LaTeX compilation, figure and table generation and a citation validator. Start with that one for a light drafting and review loop; choose this one when you need the compile-and-verify toolchain, and accept the credential-handling findings that come with it.
- [Research Paper Writing Pipeline - Academic ML/AI Paper Production Setup](/hermes/skills/catalog/research-paper-writing-setup) - a single skill for end-to-end ML paper production, useful when 31 skills is more machinery than the job needs.
- [Deep Research Skill - Citation-Tracked Research Setup](/hermes/skills/catalog/claude-deep-research-skill-setup) - claim-level verification and evidence persistence for the research phase, without the paper-production phases.
- [Tavily Research - AI-Powered Deep Research Setup](/hermes/skills/catalog/tavily-research-setup) - hosted deep research with citations, for when you would rather call an API than run local scripts.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Set up the key file before anything else, and patch the two SKILL.md examples that grep `/Users/lingzhi/Code/keys.md`. Exporting `S2_API_KEY` in the environment and referencing that variable keeps the secret out of the prompt, which is what the auditors flagged.
- Install with `-g`. Half the suite's value is the scripts at `~/.claude/skills/<skill>/scripts/`, and a project-local install leaves those paths empty.
- Point the output directory at your own project. `deep-research` defaults to an absolute path on the author's machine, so set the output root explicitly on the first run or the files land nowhere you can find.
- Run literature-search first and check the JSONL before you run literature-review. The review skill reasons over whatever the search returned, and a bad query propagates into a confident review of the wrong literature.
- Use `paper-compilation` as the done-check. It runs pdflatex and bibtex with an auto-fix loop, so "it compiles" becomes evidence rather than an opinion.
- Leave excalidraw-skill out unless you actually need canvas diagrams: it is the only piece that requires a long-running local server.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
