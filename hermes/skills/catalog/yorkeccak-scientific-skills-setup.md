---
title: "Scientific Skills - Literature Search Suite Setup"
description: "yorkeccak/scientific-skills: natural language literature search across PubMed, arXiv, ChEMBL, DrugBank and clinical trials - 5.1K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/yorkeccak-scientific-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-22"
tags: ["hermes skill", "agent skill", "skill setup", "scientific literature", "semantic search", "research"]
---

# Scientific Skills - Literature Search Suite Setup

**Source:** [yorkeccak/scientific-skills](https://www.skills.sh/yorkeccak/scientific-skills) via skills.sh - 5.1K combined installs across 13 indexed listings; first seen Nov 22, 2026 (Nov 22, 2026 morning sweep)
**GitHub:** [yorkeccak/scientific-skills](https://github.com/yorkeccak/scientific-skills) - 64 stars, MIT license, main branch, last pushed Oct 4, 2026; thirteen skill directories under `skills/<name>/SKILL.md`, each with a `scripts/search` bash wrapper and a `scripts/search.mjs` Node implementation, plus a `.claude-plugin/` manifest.
**Category:** Scientific Literature Search
**Quality Tier:** 🟠 Orange - MIT license and 64 stars, but all 13 sampled skills carry a Snyk Fail with Gen Agent Trust Hub and Socket clean across the sample.

Yorkeccak Scientific Skills is a suite of natural language search skills for scientific literature, built on Valyu semantic search. Each skill wraps a single data source - PubMed, arXiv, bioRxiv, medRxiv, ChEMBL, DrugBank, ClinicalTrials.gov, FDA drug labels, Open Targets or global patents - behind a plain-language interface: the caller passes a natural language query and gets back full-text results with figures, not API parameters or search syntax. Three aggregated skills (literature-search, biomedical-search and drug-discovery-search) combine related sources in a single call.

Every skill ships as a directory with a SKILL.md plus a scripts/search bash wrapper over a scripts/search.mjs Node implementation. There are no npm dependencies; Node.js 18+ with its built-in fetch is the only runtime requirement. The single external credential is a Valyu API key (the README notes $10 of free credit), saved automatically to ~/.valyu/config.json on first use or set as a VALYU_API_KEY environment variable.

## Installation

The README's recommended path is the skills.sh CLI:

```bash
npx skills i yorkeccak/scientific-skills
```

Individual skills can be browsed on skills.sh (search "yorkeccak"), and the suite supports installation to many agents including Claude Code, Codex, Cursor, Windsurf, Gemini CLI and GitHub Copilot. As a Claude Code plugin:

```text
/plugin install yorkeccak/scientific-skills
```

Or clone manually and add as a local plugin:

```bash
cd ~/dev
git clone https://github.com/yorkeccak/scientific-skills.git
```

then add it in Claude Code with `/plugin add ~/dev/scientific-skills`. Before the first search, create a Valyu API key at platform.valyu.ai; on first use a skill detects the missing key, asks for it, saves it to ~/.valyu/config.json and runs the search.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| arxiv-search | 1,143 | Search arXiv physics, math and computer science preprints with natural language queries |
| biomedical-search | 738 | Combined biomedical search across PubMed, preprints, clinical trials and FDA drug labels |
| pubmed-search | 711 | Search PubMed biomedical literature with natural language queries and full-text access |
| patents-search | 642 | Search global patents for prior art, patent landscapes and innovation tracking |
| literature-search | 605 | Combined literature search across PubMed, arXiv, bioRxiv and medRxiv |
| medrxiv-search | 196 | Search medRxiv medical preprints with natural language queries |
| clinical-trials-search | 174 | Search ClinicalTrials.gov for trials, enrollment and outcomes |
| drug-discovery-search | 169 | Combined drug discovery search across ChEMBL, DrugBank, targets and FDA labels |
| biorxiv-search | 150 | Search bioRxiv biology preprints with natural language queries |
| drug-labels-search | 137 | Search FDA drug labels for indications and safety data |
| drugbank-search | 136 | Search DrugBank for drug mechanisms, interactions and safety data |
| open-targets-search | 130 | Search Open Targets drug-disease associations and target validation |
| chembl-search | 128 | Search ChEMBL for bioactive compounds and assay data |

All 13 indexed listings clear the 50-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

The suite's core idea is worth copying: it removes the API layer entirely. Callers pass a plain English question - "search PubMed for CRISPR advances in 2024" - and the skill turns it into a semantic search instead of asking the agent to learn each database's query syntax. That is a meaningful ergonomic win for agents that hop between PubMed, arXiv, ChEMBL, DrugBank and clinical trials, because one call pattern covers all of them. The results come back as full-text JSON with titles, URLs, content, relevance scores and image links, so an agent can pipe straight into jq or into its own context without further parsing. The three aggregated skills are a clean composition pattern: literature-search, biomedical-search and drug-discovery-search bundle related sources so a single query spans a whole research domain. Because each skill is a self-contained directory with a bash wrapper over a Node script and zero npm dependencies, the skills are easy to vendor or audit. The caveat is the Valyu dependency: every search round-trips through the Valyu third-party API, and the uniform Snyk Fail across all 13 samples means the source should be reviewed before production use.

## Usage

| You say | What happens |
|---|---|
| Search PubMed for CRISPR advances in 2024 | Sends the natural language query to Valyu semantic search and returns full-text PubMed articles with figures and relevance scores |
| Find kinase inhibitors for melanoma | Runs drug-discovery-search across ChEMBL, DrugBank and FDA labels for compounds and targets |
| Check clinical trials for checkpoint inhibitor combinations | Queries ClinicalTrials.gov for matching trials, enrollment and outcomes |
| Get papers on epigenetic modifications in cancer | Runs literature-search across PubMed, arXiv, bioRxiv and medRxiv |
| Look for prior art on CRISPR delivery methods | Searches global patents for prior art and patent landscapes |
| What are the interactions for this drug | Queries DrugBank for mechanisms, interactions and safety data |
| Pull just the article titles | Pipes search output through jq to extract .results[].title |

## Verification

Confirm a SKILL.md landed before installing, and review the search script behind it:

```bash
curl -sL https://raw.githubusercontent.com/yorkeccak/scientific-skills/main/skills/pubmed-search/SKILL.md | head -40
```

Inspect the aggregated biomedical skill that combines PubMed, preprints, trials and drug labels:

```bash
curl -sL https://raw.githubusercontent.com/yorkeccak/scientific-skills/main/skills/biomedical-search/SKILL.md | head -40
```

Review the drug discovery skill before trusting its compound and target results:

```bash
curl -sL https://raw.githubusercontent.com/yorkeccak/scientific-skills/main/skills/drug-discovery-search/SKILL.md | head -40
```

The Node implementation for any skill is its sibling scripts/search.mjs in the same directory, which you can read the same way.

## Security

skills.sh verdicts for sampled skills (verified Nov 22, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| arxiv-search | Pass | Pass | Fail |
| biomedical-search | Pass | Pass | Fail |
| pubmed-search | Pass | Pass | Fail |
| patents-search | Pass | Pass | Fail |
| literature-search | Pass | Pass | Fail |
| medrxiv-search | Pass | Pass | Fail |
| clinical-trials-search | Pass | Pass | Fail |
| drug-discovery-search | Pass | Pass | Fail |
| biorxiv-search | Pass | Pass | Fail |
| drug-labels-search | Pass | Pass | Fail |
| drugbank-search | Pass | Pass | Fail |
| open-targets-search | Pass | Pass | Fail |
| chembl-search | Pass | Pass | Fail |

Every one of the 13 sampled skills carries a Snyk Fail, with Gen Agent Trust Hub and Socket clean across the sample, so review each skill's scripts/search.mjs before production use. Searches also round-trip through the Valyu third-party API, so queries and results leave the host.

## Limitations

- Snapshot data, verified Nov 22, 2026: 5.1K combined installs across 13 indexed listings; 64 GitHub stars; MIT license; last pushed Oct 4, 2026. Counts drift over time.
- Every one of the 13 sampled skills carries a Snyk Fail, with Gen Agent Trust Hub and Socket Pass across the sample, so treat the source as requiring per-skill review before production use.
- Searches run through the Valyu third-party API, so queries and results round-trip outside the host; a Valyu API key is required (the README notes $10 of free credit).
- Each search returns a cost field in its JSON output, and the Valyu account starts with $10 of free credit, so high-volume literature sweeps will consume paid credit.
- The README documents no per-source rate limits or licensing terms for the underlying databases, so verify those directly with each source before heavy or commercial use.

## Related

- [Valyu Search Skills - Web Search and Research APIs](/hermes/skills/catalog/valyuai-skills-setup)
- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)
- [Claude Scholar - Research Pipeline for Agents](/hermes/skills/catalog/claude-scholar-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Set VALYU_API_KEY once in the shell (or let the first run save it to ~/.valyu/config.json) so all 13 skills share a single credential.
- Start broad with literature-search for a general review, then drop to a single-source skill such as pubmed-search or arxiv-search once you know which database you need.
- Pipe results through jq to keep only titles, URLs or high-relevance hits, since every skill returns the same JSON shape.
- Use more specific natural language questions rather than search syntax; the README notes you can also adjust the maxResults parameter.
- Read each skill's scripts/search.mjs before trusting it in a production agent, given the uniform Snyk Fail across the sample.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
