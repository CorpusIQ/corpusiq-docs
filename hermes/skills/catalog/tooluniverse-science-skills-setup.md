---
title: "ToolUniverse Science Skills - 242 Tools for Agents"
description: "mims-harvard/tooluniverse on skills.sh: 10.5K combined installs; 242 scientific agent skills for sequence, literature, clinical and chemistry work"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tooluniverse-science-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "tooluniverse", "bioinformatics", "life sciences", "drug discovery"]
---

# ToolUniverse - Setup Guide

**Source:** [mims-harvard/tooluniverse](https://www.skills.sh/mims-harvard/tooluniverse) via skills.sh - 10.5K combined installs across 20 indexed listings (10,545 exact); first seen 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 1,780 stars, Apache-2.0 license, `main` branch, last pushed 2026-11-09, 557 `SKILL.md` files among 9,992 blobs, with skill directories at `skills/<name>/` and a second copy under `plugin/skills/<name>/` for the Claude Code plugin
**Category:** Scientific research: biomedical and chemistry tooling, literature review, sequence retrieval and clinical guideline lookup
**Quality Tier:** 🟡 Solid with caveats - Apache-2.0 with a large install base, but 13 of the 20 sampled listings carry a warning and the two configuration skills draw Gen Agent Trust Hub Fails.

ToolUniverse is the Zitnik lab's ecosystem for building AI scientist systems, and this repository holds the agent skills that sit on top of it. The skills.sh page claims 242 skills from the repository, then renders 20 of them because its list is capped at 20 rows; those 20 carry 10,545 installs between them, led by sequence retrieval at 1,726. The repository itself is much larger than either number suggests: 557 `SKILL.md` files across 9,992 blobs, with the skills published under `skills/` and a parallel copy under `plugin/skills/` for the Claude Code plugin.

What the indexed twenty have in common is that they are procedures over the ToolUniverse tool layer rather than standalone scripts. That layer exposes more than 2,700 machine learning models, datasets, APIs and scientific packages through an MCP server, a `tu` CLI with 14 subcommands, and a Python SDK, so a skill like literature review is really a sequence of calls with rules about query disambiguation, source precedence and evidence grading. The repository ships `setup-tooluniverse` to configure that layer for a given client, and a router skill named `tooluniverse` that decides how an analysis should start. The rest of the list splits into four clusters: genomics and structure work, drug and target intelligence, clinical evidence, and general research reporting.

## Installation

The README's skills route installs the whole suite, and the skills.sh listing pages name one skill at a time:

```bash
npx skills add mims-harvard/ToolUniverse
```

```bash
npx skills add https://github.com/mims-harvard/tooluniverse --skill setup-tooluniverse
```

Claude Code users get a plugin route instead of a skills directory:

```bash
claude plugin marketplace add mims-harvard/ToolUniverse
claude plugin install tooluniverse@tooluniverse
```

The skills are thin without the tool layer, so the MCP server is part of the install rather than an optional extra. The README's manual configuration is a `uvx` entry:

```json
{
  "mcpServers": {
    "tooluniverse": {
      "command": "uvx",
      "args": ["--refresh", "tooluniverse"],
      "env": {"PYTHONIOENCODING": "utf-8"}
    }
  }
}
```

The `--refresh` flag checks PyPI on every launch, which keeps the tool layer current at the cost of startup time; dropping it starts from the `uv` cache, and `uv cache clean tooluniverse` is the upgrade path in that mode. The README also flags an old build that ships inside Claude Desktop's built-in Extensions directory and cannot start, so remove that copy before wiring the server this way. For Python work the base package covers the API and database tools, while local models, cheminformatics and plotting live in optional groups such as `[ml]`, `[visualization]` and `[bioinformatics]`; `tooluniverse-doctor` reports which groups are missing.

## What It Provides

The threshold for this guide is zero installs, so every indexed listing appears below:

| Skill | Installs | Use For |
|---|---|---|
| tooluniverse-sequence-retrieval | 1,726 | Fetches DNA, RNA and protein sequences from NCBI and ENA, preferring RefSeq records over predicted models and raw GenBank submissions. |
| tooluniverse-literature-deep-research | 669 | Runs systematic literature reviews across PubMed, EuropePMC and bioRxiv, grades evidence T1 to T4 and returns a cited report. |
| tooluniverse-image-analysis | 656 | Quantifies microscopy measurements: colony morphometry, fluorescence intensity, cell counts, dose-response curves and ANOVA on CellProfiler or ImageJ output. |
| tooluniverse-clinical-guidelines | 496 | Searches clinical practice guidelines from NICE, WHO, NCCN, AHA and other bodies, ranking NICE and WHO above society guidance. |
| tooluniverse | 485 | Plugin router for the suite: checks for executed notebooks first so earlier filters, samples and exclusions carry into the analysis. |
| tooluniverse-drug-research | 475 | Builds full drug profiles covering mechanism, targets, interactions, trial status, FAERS adverse events and approval history. |
| tooluniverse-drug-drug-interaction | 458 | Scores drug-drug interactions across CYP metabolism, transporters and pharmacodynamic effects, with management recommendations. |
| tooluniverse-clinical-trial-design | 458 | Assesses trial feasibility across six design dimensions and projects enrollment, endpoints and regulatory pathway from precedent trials. |
| setup-tooluniverse | 448 | Walks through ToolUniverse setup for the MCP server, the tu CLI or the Python SDK, including client configuration and troubleshooting. |
| tooluniverse-disease-research | 439 | Compiles disease reports covering causal genes, pathways, drugs and repurposing candidates, trials, epidemiology and phenotypes. |
| tooluniverse-systems-biology | 436 | Runs multi-database pathway enrichment and network reasoning over Reactome, KEGG, WikiPathways and BioCarta. |
| tooluniverse-protein-structure-retrieval | 435 | Retrieves and grades protein structures from RCSB PDB, PDBe, AlphaFold, SWISS-MODEL and PDB-REDO by resolution, R-factor and pLDDT. |
| tooluniverse-network-pharmacology | 434 | Builds compound-target-disease networks over STRING, BioGRID, ChEMBL and OpenTargets for repurposing and polypharmacology work. |
| tooluniverse-precision-oncology | 426 | Recommends cancer therapies from a molecular profile using CIViC, ClinVar and trial data, with resistance mechanisms and evidence tiers. |
| tooluniverse-epigenomics | 425 | Analyzes methylation, m6A, ChIP-seq, ATAC-seq and histone marks, combining pandas and pysam computation with annotation tools. |
| tooluniverse-pharmacovigilance | 424 | Mines FAERS reports for adverse-event signals with PRR, ROR and IC scoring, plus label changes and black-box warnings. |
| tooluniverse-chemical-compound-retrieval | 419 | Resolves compound names to SMILES, InChI, CID and ChEMBL IDs across PubChem and ChEMBL, handling isomers and stereochemistry. |
| tooluniverse-target-research | 412 | Profiles a drug target across nine parallel paths: tissue expression, pathways, interactions, variant landscape and druggability. |
| tooluniverse-proteomics-analysis | 412 | Analyzes mass-spec proteomics output for identification, LFQ and TMT quantification, differential expression and pathway enrichment. |
| create-tooluniverse-skill | 412 | Authors new ToolUniverse skills with a test-driven, implementation-agnostic method and validation of the skill contract. |

All 20 indexed listings clear the zero-install threshold, and none fall outside the table. That is the complete rendered skills.sh set, not the complete repository: the same page says 242 skills exist, and the tree carries 557 `SKILL.md` files after the plugin copies are counted.

The heaviest cluster in installs is retrieval of one kind or another. Sequence retrieval, literature deep research and image analysis sit at the top, and all three are written as disambiguation-first procedures: resolve the accession, the query or the measurement, then fetch, then grade. The clinical and drug skills carry the same shape with more rules attached, which is what separates them from a generic prompt. `tooluniverse-clinical-guidelines` states a source hierarchy, `tooluniverse-drug-drug-interaction` scores clinical significance before advising, and `tooluniverse-pharmacovigilance` computes PRR, ROR and IC rather than reporting a raw count of reports.

## Why This Matters for Hermes Agents

Scientific questions are the clearest case of an agent producing an answer that looks better than it is. A model asked for the sequence behind a transcript will return a plausible accession; asked whether two drugs interact, it will produce a paragraph of mechanisms with no source ordering; asked for a variant interpretation, it will cite a paper that may not exist. These skills replace that with a retrieval order and a quality hierarchy, which is the part a model cannot supply from memory.

The specific rules are worth naming because they encode domain judgement rather than syntax. RefSeq curated records outrank RefSeq predicted models, which outrank raw GenBank submissions. NICE and WHO guidance outranks specialty society guidance. Experimental structures under 2 Angstrom outrank predicted models, which outrank homology models. An agent that follows those orderings produces citations a domain expert will accept, and an agent that skips them produces a correct-looking list in the wrong order.

The suite also solves a context problem that shows up immediately with this much tooling. ToolUniverse exposes over 2,700 tools, and the standard MCP presentation of that many tools consumes a context window before any work starts. Compact mode reduces the surface to five discovery tools and routes everything else through `execute_tool`, which is the difference between a usable session and a session that spends its budget reading tool schemas.

The counterweight is that every one of these skills terminates in an external database call. Coverage, uptime and result shape are the dependencies, and a skill that expects a ChEMBL or ClinVar response will fail in a way the model may paper over with prose.

## Usage

| You say | What happens |
|---|---|
| "Fetch the mRNA sequence for NM_000546" | Sequence retrieval resolves the accession, prefers the curated RefSeq record, and flags whether the returned entry is a predicted model or a GenBank submission |
| "Write a literature review on GLP-1 agonists and cardiovascular outcomes" | Deep research disambiguates the query, runs collision-aware searches across PubMed, EuropePMC and bioRxiv, grades the evidence and returns a structured report with citations |
| "What do guidelines say about first-line treatment for type 2 diabetes?" | Clinical guidelines searches NICE, WHO, ADA and other bodies, then ranks the answers by source authority, with NICE and WHO above society guidance |
| "Is warfarin with fluconazole safe?" | Drug-drug interaction checks CYP substrate, inhibitor and inducer roles, adds transporter effects, scores clinical significance and recommends management |
| "Profile EGFR as a drug target" | Target research runs its nine paths in parallel: tissue expression, pathways, interactions, variant landscape and druggability, with citations |
| "What adverse events are reported for metformin?" | Pharmacovigilance mines FAERS, scores signals with PRR, ROR and IC, and adds label warnings and demographic risk factors |
| "Quantify the colonies in this CellProfiler export" | Image analysis computes morphometry, intensity and counts, fits dose-response curves where a dose series exists, and runs ANOVA or Dunnett across groups |

## Verification

Each listing resolves to a raw `SKILL.md` under `skills/`, one directory per skill. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/mims-harvard/tooluniverse/main/skills/setup-tooluniverse/SKILL.md | head -5
```

It should open with frontmatter holding `name: setup-tooluniverse`, a description starting `Install and configure ToolUniverse for any use case`, and below the delimiter a `# Setup ToolUniverse` heading. The same path shape works for any listing, so swap the directory name to inspect the skill before installing it.

After an install, confirm the directory landed in the agent skills directory rather than as loose files:

```bash
ls -d ~/.claude/skills/*/ | head -20
test -f ~/.claude/skills/setup-tooluniverse/SKILL.md && echo ok
```

The plugin route manages its own copy of these skills, so the directory check applies to the CLI and manual routes; for the plugin install, confirm the marketplace entry and plugin name from the commands above.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| tooluniverse-sequence-retrieval | Pass | Pass | Warn |
| tooluniverse-literature-deep-research | Pass | Pass | Warn |
| tooluniverse-image-analysis | Pass | Pass | Warn |
| tooluniverse-clinical-guidelines | Pass | Pass | Warn |
| tooluniverse | Fail | Pass | Pass |
| tooluniverse-drug-research | Pass | Pass | Warn |
| tooluniverse-drug-drug-interaction | Pass | Pass | Warn |
| tooluniverse-clinical-trial-design | Pass | Pass | Warn |
| setup-tooluniverse | Fail | Warn | Pass |
| tooluniverse-disease-research | Pass | Pass | Warn |
| tooluniverse-systems-biology | Pass | Pass | Pass |
| tooluniverse-protein-structure-retrieval | Pass | Pass | Pass |
| tooluniverse-network-pharmacology | Pass | Pass | Warn |
| tooluniverse-precision-oncology | Pass | Pass | Warn |
| tooluniverse-epigenomics | Pass | Pass | Pass |
| tooluniverse-pharmacovigilance | Pass | Pass | Warn |
| tooluniverse-chemical-compound-retrieval | Pass | Pass | Pass |
| tooluniverse-target-research | Pass | Pass | Warn |
| tooluniverse-proteomics-analysis | Warn | Pass | Pass |
| create-tooluniverse-skill | Pass | Pass | Pass |

The verdicts split cleanly by scanner. Agent Trust Hub passes 17 of 20 but fails `tooluniverse` and `setup-tooluniverse`, the two skills that configure the tool layer. Socket passes 19 of 20, warning only on `setup-tooluniverse`. Snyk is the strict one here, passing 8 and warning on 12, including the three most installed skills in the suite.

Treat the two failed skills as the ones with the most reach. `setup-tooluniverse` writes MCP client configuration for more than a dozen clients and walks through package setup; `tooluniverse` is the entry point an analysis starts from, so it decides which tools run. Run them in a session where you can read the config diff, and prefer the manual MCP block above if you would rather not have an agent editing client settings.

The larger exposure is credentials and data flow. Many of these skills call databases that need API keys, and the README's setup material walks through key handling, so keys end up somewhere in the environment or a config file. Skills that query clinical or genomic sources also carry whatever identifiers you pass them to a third party, which matters if the input is patient-adjacent. Scope keys per project, keep them out of the repository, and treat a trial or variant query with real identifiers as a data-handling decision rather than a lookup.

## Limitations

- Snapshot data, verified 2026-11-09: 10,545 combined installs across 20 indexed listings; 1,780 GitHub stars; Apache-2.0 license; last pushed 2026-11-09. Counts drift over time.
- The skills.sh source page renders at most 20 listings, while the publisher page describes 242 skills, so the install numbers here cover less than a tenth of what the repository claims to ship. The README is looser still, describing 68 pre-built research workflows in its feature list; none of the three counts can be reconciled from the tree alone.
- The tree carries 557 `SKILL.md` files, with skills published under `skills/` and a parallel plugin copy under `plugin/skills/`. A file count is not a skill count on this repository.
- Most listings are procedures over the ToolUniverse tool layer, so they need the MCP server or the `tu` CLI configured before they do anything useful. Installed alone through `npx skills add`, several will describe steps their tools cannot perform.
- Results depend on live third-party databases (NCBI, ChEMBL, ClinVar, FAERS, ClinicalTrials.gov and others) whose coverage, rate limits and response shapes change without notice. A skill cannot report a source outage as a finding.
- Two of the three scanners return warnings on most of the suite: Snyk warns on 12 of 20 listings and Agent Trust Hub fails on the two setup skills. The tier line above is the repository-level summary; the per-scanner detail in the table is the accurate picture, and the two failed setup skills are why it carries a caveat rather than a clearance.

## Related

- [Arize Phoenix Skills - LLM Observability for Agents](/hermes/skills/catalog/arize-phoenix-skills-setup)
- [Startup Validation Skills - Design, Pitch and Positioning](/hermes/skills/catalog/startup-validation-skills-setup)
- [Finance Skills - Financial Analysis for Agents Setup](/hermes/skills/catalog/finance-skills-setup)

## Pro Tips

- Install `setup-tooluniverse` first and let it finish before adding the analysis skills. Every other skill assumes a working tool layer, and the failure mode when it is missing is a confident narrative with no tool calls behind it.
- Read the source-precedence rule in whichever skill you are about to use, then state it in your prompt. Telling the agent that NICE outranks society guidance or that RefSeq beats GenBank produces better ordering than hoping the skill's internal rule survives a long context.
- Prefer one deep skill to five narrow ones per question. The master-style skills (`tooluniverse-drug-research`, `tooluniverse-target-research`, `tooluniverse-disease-research`) already chain the narrow lookups and keep their outputs consistent with each other.
- Check whether compact mode is active before a long session. Five discovery tools instead of 2,700 keeps the context budget for the actual analysis, and `execute_tool` reaches everything the short list hides.
- Keep a scratch directory for retrieved structures, sequences and FAERS dumps. These skills re-query on every run, and a saved payload is the only way to reproduce a result after a database changes underneath you.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
