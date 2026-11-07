---
title: "Claude Scholar - Research Pipeline for Agents"
description: "galaxy-dawn/claude-scholar on skills.sh: 19.9K combined installs; a research pipeline from ideation and citation checks to papers and rebuttals."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-scholar-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "academic research", "citation verification", "obsidian"]
---

# Claude Scholar - Setup Guide

**Source:** [galaxy-dawn/claude-scholar](https://www.skills.sh/galaxy-dawn/claude-scholar) via skills.sh - 19.9K combined installs across 57 indexed listings; first seen 2026-11-06 (Nov 6, 2026 evening sweep)
**GitHub:** 6,006 stars, MIT licence, last pushed 2026-10-19, 45 SKILL.md directories under skills/, plus 36 slash commands, 6 subagents and 5 rule files
**Category:** Academic research for agents: ideation, literature review, citation verification, experiments, paper writing and rebuttals
**Quality Tier:** 🟡 Review - clean scanner verdicts on three of four sampled skills, a large star count and an MIT licence, held back by a Snyk warning on the citation checker and one listing with no verdicts at all.

Claude Scholar is a semi-automated research assistant built for computer science and AI researchers: literature review, coding, experiments, reporting, writing and project knowledge management, wired into one agent workflow. The repository describes itself as the Claude Code edition, with separate `codex`, `kimi` and `opencode` branches for other runtimes, and the `main` branch is the one this guide covers.

The shape of the thing is a full research loop rather than a writing helper. Ideation turns a vague topic into questions and gaps. Literature runs through Zotero collections. Paper notes become structured claims. Durable knowledge is routed into an Obsidian vault across `Sources`, `Knowledge`, `Experiments`, `Results`, `Writing`, `Daily` and `Maps`. Experiments track hypotheses and run history. Analysis produces statistics and figures. Reporting writes the post-experiment report back into the vault, and writing carries stable findings into papers, rebuttals, slides and posters.

Two recent additions make the loop auditable. A shared `research-contract.md` defines Evidence Records, claim strength and Claim Promotion Gates, and the ideation, ingestion, synthesis, reporting, writing and rebuttal workflows all read it. `expression-skill` was made the explicit conclusion-first discipline for reports, plans and multi-step technical work, and `planning-with-files` was restored as the default on-disk planning layer for complex tasks.

That combination is why the citation checker is the most installed skill in the set. A pipeline that promotes claims on evidence is only as good as its references.

## Installation

The recommended route is the repository's own installer. It is backup-aware and handles incremental updates, which matters if you already have a `~/.claude` directory worth keeping:

```bash
git clone https://github.com/Galaxy-Dawn/claude-scholar.git /tmp/claude-scholar
bash /tmp/claude-scholar/scripts/setup.sh
```

On Windows the README says to use Git Bash or WSL. The installer updates repo-managed `skills/commands/agents/rules/hooks/scripts/CLAUDE*.md`, backs overwritten files up to `~/.claude/.claude-scholar-backups/<timestamp>/`, backs `settings.json` up to `settings.json.bak`, and adds missing hook entries instead of replacing your hook set.

It also refuses to overwrite your own instruction file. An existing `~/.claude/CLAUDE.md` is preserved and the repository's version lands beside it as `CLAUDE.scholar.md`, which you then merge by hand. The README is emphatic that the sidecar file is not applied automatically.

To update later, or to remove it cleanly:

```bash
cd /tmp/claude-scholar
git pull --ff-only
bash scripts/setup.sh
bash scripts/uninstall.sh
```

The installer writes `~/.claude/.claude-scholar-manifest.txt` and `~/.claude/.claude-scholar-install-state`, and the uninstaller only removes what that state records, rather than guessing from the current checkout.

There is a minimal route for people who want the research core without the rest. It copies hooks plus eight named skills:

```bash
cp -r /tmp/claude-scholar/skills/ml-paper-writing ~/.claude/skills/
cp -r /tmp/claude-scholar/skills/research-ideation ~/.claude/skills/
```

The README's minimal list is `ml-paper-writing`, `research-ideation`, `results-analysis`, `results-report`, `review-response`, `writing-anti-ai`, `git-workflow` and `bug-detective`, plus `hooks/*.js`. A plugin marketplace route also exists for Claude Code, but it cannot distribute rules, cannot auto-load `CLAUDE.md`, and does not configure `settings.json`, so the README tells you to install `rules/*.md` separately afterwards.

Optional pieces are Zotero with the author's `zotero-mcp` server for literature work, Obsidian for the knowledge base, and `uv` for Python projects.

## What It Provides

Fifty-seven indexed listings, of which twenty clear the 386-install threshold and appear here:

| Skill | Installs | Use For |
|---|---|---|
| citation-verification | 1,506 | Reference checks against arXiv, DOI/CrossRef, Semantic Scholar, publisher pages and Zotero, plus the common fake-citation patterns |
| writing-anti-ai | 778 | Strip AI writing patterns: inflated symbolism, promotional language, vague attributions, negative parallelisms, AI vocabulary |
| paper-self-review | 697 | Review a draft against the standards a reviewer will apply before it is submitted |
| review-response | 567 | Draft point-by-point rebuttals and response letters to reviewers |
| results-analysis | 552 | Strict statistics and real scientific figures from experiment output |
| research-ideation | 543 | Turn a topic into research questions, gaps and an initial plan |
| ui-ux-pro-max | 513 | Interface review and design guidance for research demos and tools |
| results-report | 501 | Write the complete post-experiment report and route it back into the vault |
| zotero-obsidian-bridge | 485 | Move literature between Zotero collections and the Obsidian knowledge base |
| ml-paper-writing | 467 | Draft machine learning papers section by section |
| skill-quality-reviewer | 466 | Audit a skill definition for trigger quality and structural problems |
| kaggle-learner | 444 | Work a Kaggle competition end to end as a learning loop |
| publication-chart-skill | 423 | Publication-grade charts and tables, including the pubfig and pubtab stack |
| daily-paper-generator | 420 | Daily paper discovery with arXiv and bioRxiv, narrowed from a top ten to a top three to a top one |
| obsidian-literature-workflow | 417 | Literature synthesis inside the Obsidian vault |
| bug-detective | 411 | Structured debugging when something in the research code fails |
| skill-improver | 405 | Rewrite an existing skill from its failures |
| latex-conference-template-organizer | 400 | Organize LaTeX conference templates and submission structure |
| post-acceptance | 391 | Camera-ready, artifact and promotion work after acceptance |
| architecture-design | 386 | Factory and registry patterns for new registrable ML components |

The remaining 37 indexed listings range from 19 to 382 installs.

The tail is dominated by the Obsidian project-memory family (`obsidian-experiment-log`, `obsidian-synthesis-map`, `obsidian-research-log`, `obsidian-project-memory`, `obsidian-project-lifecycle`, `obsidian-project-bootstrap`, `obsidian-link-graph`, `obsidian-markdown`, `obsidian-cli`, `obsidian-bases`) plus `json-canvas` and a listing called `Agent Development`, all between 19 and 49 installs. The rest of the tail between 271 and 382 is the tooling layer: `nature-writing`, `nature-response`, `nature-data`, `expression-skill`, `mcp-integration`, `hook-development`, `plugin-structure`, `command-development`, `agent-identifier`, `defuddle` and `git-workflow`. They are useful, they are simply not what people install first.

## Why This Matters for Hermes Agents

Fake references are the failure mode that ends careers rather than embarrassing them, and a model asked to produce a bibliography will produce plausible ones. The citation pass is specific about authority: verify against arXiv, DOI/CrossRef, Semantic Scholar, publisher landing pages and Zotero metadata, and treat Google Scholar as a discovery tool rather than the canonical record. That ordering is the useful part, because it tells the agent where to stop.

The evidence contract is the structural answer to the same problem one level up. Claims carry strength, an evidence record, and a promotion gate before they move from a paper note into the knowledge base or into prose. For an agent that writes across sessions, this is the difference between a vault that accumulates verified claims and one that accumulates confident summaries of summaries.

The writing stack is unusually concrete for a research repository. `writing-anti-ai` is built on Wikipedia's "Signs of AI writing" guide and names the patterns it removes, down to superficial `-ing` analyses and negative parallelisms. `expression-skill` enforces conclusion-first reporting with visible risk and next steps. `paper-self-review` and `review-response` cover the two moments when a draft is judged by someone hostile.

The analysis and reporting pair is where the loop closes. `results-analysis` is instructed to produce strict statistics and real figures, `results-report` writes the report, and both feed the vault rather than a chat window, so the next session starts from artifacts instead of recollection.

The cost is surface area. Forty-five skills, 36 commands and a hook set is a lot of instruction to load, and it is designed for someone whose working life is research. For a general engineering session most of this is dead weight, which is why the minimal install list exists.

## Usage

| You say | What happens |
|---|---|
| "Is this reference real? Check the DOI and the authors" | Citation verification resolves the DOI and publisher record, then reports mismatched authors, titles or years |
| "Read this paper and file it in my Zotero library under the right collection" | The literature workflow imports the paper, creates a structured note and routes durable claims into the vault |
| "What is still open in this area, and what would I test first?" | Ideation produces questions, gaps and an initial plan, written to disk rather than kept in context |
| "Turn these results into a report with figures" | Results analysis produces the statistics and figures, then the report pass writes the artifact and files it |
| "Draft the methods section from the experiment log" | ml-paper-writing drafts the section from the recorded experiment line, with claims tied to evidence |
| "Reviewer 2 says the baselines are weak, write the rebuttal" | The rebuttal pass drafts point-by-point responses and flags where the paper needs new evidence rather than new wording |
| "This abstract sounds like a model wrote it" | writing-anti-ai rewrites the prose and names the patterns it removed |

## Verification

Read the most-installed skill before installing the set. This path returned 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/Galaxy-Dawn/claude-scholar/main/skills/citation-verification/SKILL.md | head -25
```

It should open with the core principle: verify every citation against programmatic or canonical scholarly sources first, with Google Scholar explicitly not the canonical authority.

After the full install, confirm the count and the install record:

```bash
ls ~/.claude/skills | wc -l
head -5 ~/.claude/.claude-scholar-manifest.txt
ls ~/.claude/CLAUDE.scholar.md
```

The skills directory should hold the 45 skill directories, plus any upstream licence notes the installer copies. The manifest should list the managed files, and the sidecar instruction file should exist if you already had a `CLAUDE.md`. If the sidecar is there, its contents are not active until you merge them, so grep your own `CLAUDE.md` for a Claude Scholar section before assuming the workflow is loaded.

For the optional literature path, the Zotero integration is a separate check, and `MCP_SETUP.md` in the repository is the documented route.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| citation-verification | Pass | Pass | Warn |
| obsidian-literature-workflow | Pass | Pass | Pass |
| code-review-excellence | Pass | Pass | Pass |
| expression-skill | Pass | Pass | Pass |
| Agent Development | ? | ? | ? |

The scanner picture is mostly clean, with a single Snyk warning on the citation checker, which is a skill that reaches out to scholarly APIs and parses the responses. One listing, `Agent Development`, has no verdicts recorded, so treat it as unassessed rather than safe.

The install surface deserves more attention than the verdicts. `scripts/setup.sh` writes into `~/.claude`, copies hooks, modifies `settings.json` and merges permission and MCP entries. The design mitigates this well: backups before overwrite, an install-state file, and an uninstaller that removes only recorded paths. Read the script before running it anyway, because a shell installer that edits your agent configuration is the highest-authority thing in this repository.

The hook layer is the part that runs on every session. Hooks are JavaScript in `hooks/`, registered in `settings.json`, and the changelog notes write-guard behaviour and quieter temp-file summaries, which tells you they inspect file activity. That is a real capability increase for the agent and a real surface for bugs, so keep the hook list small if you only wanted the research skills.

The README carries three sponsor placements (OfoxAI, APIMart and Kimi) with affiliate-style links. They do not affect the skills, and they are worth knowing about before you treat a recommendation in the docs as neutral.

The licence is MIT, which is the permissive case, and the skills are markdown plus scripts, so there is nothing here you cannot read.

## Limitations

- Snapshot data, verified 2026-11-06: 19,910 combined installs across 57 indexed listings; 6,006 GitHub stars; MIT licence; last pushed 2026-10-19. Counts drift over time.
- Thirty-seven of the 57 listings sit below the threshold, between 19 and 382 installs, mostly the Obsidian project-memory family. Install counts there describe adoption, not quality.
- The `main` branch is the Claude Code edition. Codex CLI, Kimi Code CLI and OpenCode users are pointed at separate branches, so the file layout in this guide does not describe those branches.
- The installer edits your agent configuration. It is backup-aware and reversible, but it does assume it may write to `~/.claude`, and the sidecar `CLAUDE.scholar.md` still needs a manual merge.
- The plugin route is incomplete on its own: rules are not distributed by plugins, `CLAUDE.md` is not auto-loaded, and `settings.json` is not configured, so it is not a one-step install despite looking like one.
- It is one researcher's opinionated workflow. Forty-five skills, a vault taxonomy and an evidence contract are a package deal; adopting half of it produces a knowledge base with no routing rules.

## Related

- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)
- [Research Paper Writing Pipeline - Hermes Skill Setup Guide](/hermes/skills/catalog/research-paper-writing-setup)
- [Academic Writing Skills - Paper Workflow](/hermes/skills/catalog/academic-writing-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install minimal first. Eight skills cover ideation through writing, and the full set can wait until you know which parts of the vault taxonomy you will actually use.
- Make the citation pass mandatory before any bibliography leaves your machine. It is the cheapest possible defence against the failure that is hardest to walk back.
- Keep the vault out of the repository and out of the agent's write path until you have read the routing rules. `Sources` and `Knowledge` are separate for a reason, and a misfiled claim is worse than an unfiled one.
- If you already maintain `CLAUDE.md`, diff `CLAUDE.scholar.md` against it rather than merging wholesale. The installer deliberately keeps them apart so you can decide what to take.
- Point `results-analysis` at raw output files, not at summaries. It is instructed to produce real statistics, and a summary has already thrown away the data it needs.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
