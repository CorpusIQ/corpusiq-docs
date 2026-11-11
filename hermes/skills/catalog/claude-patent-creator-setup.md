---
title: "Claude Patent Creator - USPTO Patent Drafting Setup"
description: "USPTO patent drafting: 2.7K combined installs across 17 listings, prior-art search, 35 USC 112 checks and MPEP lookup over a local index"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-patent-creator-setup/"
robots: "index,follow"
last_updated: "2026-11-11"
tags: ["hermes skill", "agent skill", "skill setup", "patent", "uspto", "intellectual property", "rag"]
---

# Claude Patent Creator - Setup Guide

**Source:** [robthepcguy/claude-patent-creator](https://www.skills.sh/robthepcguy/claude-patent-creator) via skills.sh - 2.7K combined installs across 17 indexed listings (2,710 exact); first seen 2026-11-11 (Nov 11, 2026 sweep)
**GitHub:** 211 stars, MIT license, `main` branch, last pushed 2026-11-11, 17 `SKILL.md` files under `skills/<name>/` plus `agents/`, `commands/`, `hooks/` and an `mcp_server/` package
**Category:** Intellectual property: patent drafting, claims analysis, prior-art search, MPEP and EPO law lookup, formalities checking
**Quality Tier:** 🟡 Mixed - MIT licensed and the most complete USPTO workflow in the marketplace, with a setup measured in tens of minutes and one Fail verdict on the diagram generator in the sampled set.

Patent drafting is a task with a specific shape that makes it unusually well suited to an agent, and unusually dangerous when the agent improvises. The shape is: a large corpus of rules, a formal document structure, and a set of checks that are mechanical. The danger is that a patent is a legal instrument, and a plausible-sounding claim that fails 35 USC 112 is worse than no draft at all.

This project attacks both sides. It builds a local hybrid retrieval index over MPEP, 35 USC and 37 CFR, so section lookup is grounded in the actual rulebook rather than in model memory. It exposes a wide set of MCP tools for search, analysis and generation. And it wraps the whole thing in guided slash commands and long-running agents that produce a draft plus a validation report rather than free text.

The tool surface is the most detailed part of the README, and it is worth reading before you install, because it shows what is checkable. Search covers `search_mpep` with filters, `get_mpep_section` for a specific section such as 608.01(b), Google Patents full text, BigQuery for bulk retrieval, non-patent literature through OpenAlex, arXiv and Semantic Scholar, and USPTO and EPO APIs. Analysis covers `review_patent_claims` for 35 USC 112(b) definiteness and antecedent basis, `review_specification` for 112(a) written description and enablement, `check_formalities` for MPEP 608, and EPO equivalents under Articles 83 and 84. Generation covers Graphviz diagrams, flowcharts and block diagrams with reference-number handling.

## Installation

The README's quick start is written for someone who is not a programmer, which is a fair signal of the intended user. It estimates about an hour, most of it waiting for the rulebook download and the index build.

The install makes a private virtual environment so nothing else on the machine is touched, then runs the setup command:

```bash
cd ~
python3 -m venv patent-creator-venv
patent-creator-venv/bin/pip install git+https://github.com/RobThePCGuy/Claude-Patent-Creator.git
patent-creator-venv/bin/patent-creator setup
```

`setup` runs for 5 to 45 minutes. On an NVIDIA card it installs the GPU build of PyTorch and restarts itself; on Apple Silicon and everything else the index builds on CPU, which the README says is faster than Apple's GPU for this job. Re-running setup is safe and skips completed steps.

The README's second step adds the guided workflows to Claude Code, and the third enables patent search with a free SerpApi key, which it lists at 250 searches a month. Additional optional keys extend coverage: an EPO OPS key for European full text, a USPTO Open Data Portal key, an OpenAlex key and a Semantic Scholar key. Cloud LLM keys are only needed if you turn on HyDE query expansion, which is off by default.

Python 3.10 to 3.13 is the stated requirement, with 3.9 or older called out explicitly as too old. On Windows the README warns to tick "Add python.exe to PATH" in the installer.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| patent-application-creator | 835 | Guided end-to-end drafting of a patent application, covering prior art, claims, specification, diagrams and compliance |
| patent-claims-analyzer | 457 | Deep claims review against 35 USC 112(b): definiteness, antecedent basis and structure |
| patent-diagram-generator | 316 | Patent-style technical diagrams, flowcharts, block diagrams and system architectures through Graphviz |
| prior-art-search | 250 | Novelty and freedom-to-operate analysis through a documented prior-art discovery methodology |
| bigquery-patent-search | 101 | Keyword, CPC classification and patent detail retrieval across the BigQuery patent corpus |

The remaining 12 indexed listings range from 51 to 88 installs and cover the supporting cast: the MPEP search skill, the reviewer that runs claims plus specification plus formalities together, the EPO analyzer and search skills, the PCT application skill, the index manager, and the development, troubleshooting, testing and setup assistants.

The repository ships more than skills. There are 13 agents in `agents/`, two of which the README presents as starting points because they run independently: a `patent-creator` agent that drafts a complete USPTO application in 55 to 80 minutes and returns specification, claims, abstract, diagrams and a validation report, and a `prior-art-searcher` that takes 15 to 30 minutes and returns a patentability report with the top prior art, claim strategy and an IDS list. Slash commands wrap the same flows: `/create-patent`, `/create-epo-patent` and `/search-prior-art`.

## Why This Matters for Hermes Agents

The hardest part of patent work for an agent is that everything it writes sounds authoritative. A claim that recites a limitation with no antecedent basis reads the same as one that does, and a specification that fails to enable a claimed range reads the same as one that enables it. This project's contribution is that it separates generation from checking and gives the checking its own tools.

The 35 USC 112 split is the clearest example of that design. `review_patent_claims` handles 112(b), definiteness and antecedent basis. `review_specification` handles 112(a), written description and enablement, and the README is honest that the best mode requirement stays a manual review. Two different statutory questions, two different tools, and one explicit admission of a limit.

The prior-art path matters more than the drafting path for most filers. `search_non_patent_literature` covers papers and preprints through OpenAlex, arXiv and Semantic Scholar, filterable by priority date, and that is where a lot of damaging prior art lives. A search that only covers patents misses the conference paper that anticipates the claim.

The local rulebook index is what makes MPEP answers trustworthy. `get_mpep_section` pulls a section by number and, per the README, says when section boundaries are approximate or when text is cut off. That kind of self-reporting is rare and it is the behaviour you want when a section number is being quoted into a filing.

The cost structure is worth knowing because it shapes use. Google Patents search through SerpApi is free to 250 searches a month and is the recommended path; the BigQuery fallback costs roughly two dollars per search past the free monthly tier. An agent that runs twenty searches in a session is spending money, and knowing which tool it chose matters.

## Usage

| You say | What happens |
|---|---|
| "Create a patent for this invention, use the patent-creator agent" | Runs the long-form agent, drafts claims, specification, abstract and diagrams, and returns a validation report |
| "Search prior art for this idea and assess novelty" | Runs the documented prior-art methodology across patents and non-patent literature and returns a patentability report |
| "Review these claims for 112(b) issues" | Checks definiteness, antecedent basis and claim structure and reports the defects |
| "Does my specification meet the written description requirement" | Applies the 112(a) heuristics and flags enablement gaps, while stating that best mode needs manual review |
| "What does MPEP 608.01(b) say about the abstract" | Retrieves the section from the local index and notes if the boundary is approximate |
| "Check the formalities on this application" | Runs the MPEP 608 formalities check over abstract, title, drawings and required sections |
| "Draw a block diagram for figure 1" | Generates a patent-style block diagram from Graphviz with reference numbers applied |

## Verification

Skills sit at `skills/<name>/SKILL.md`. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/robthepcguy/claude-patent-creator/main/skills/patent-claims-analyzer/SKILL.md | head -6
```

The real verification is whether the index built, since every grounded answer depends on it. The README ships status tools for exactly this and they are the fastest check: `check_bigquery_status` for the BigQuery configuration, `check_google_patents_status` for the SerpApi key and remaining searches, `check_uspto_api_status`, `check_epo_api_status` and `check_diagram_tools_status` for Graphviz.

A working setup answers a section lookup with real text. If `get_mpep_section` returns an error, or returns a summary that reads like model output, the index is missing and the drafting skills are working from memory.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-11) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| patent-application-creator | Pass | Pass | Warn |
| patent-claims-analyzer | Pass | Pass | Pass |
| patent-diagram-generator | Fail | Pass | Pass |
| prior-art-search | Pass | Pass | Pass |
| bigquery-patent-search | Pass | Pass | Warn |

One Fail, on `patent-diagram-generator` at the trust hub, and two Snyk Warns. The diagram generator is the skill that shells out to Graphviz and writes files, which is a plausible reason for the trust-hub flag, but read the skills.sh page rather than inferring from the pattern.

The confidentiality dimension is the one to think about hardest. A patent application before filing is the most sensitive document a company produces, and this tool has a network path: Google Patents through SerpApi, BigQuery, OpenAlex, arXiv, Semantic Scholar, USPTO and EPO. The retrieval direction is outbound queries rather than uploaded documents, and the local index keeps the rulebook on your machine. Still, the queries themselves describe the invention, so review what leaves the machine before you search against an unfiled idea.

## Limitations

- Snapshot data, verified 2026-11-11: 2,710 combined installs across 17 indexed listings; 211 GitHub stars; MIT; last pushed 2026-11-11. Counts drift over time.
- Setup is not a two-minute install. The README estimates 5 to 45 minutes for the index build and about an hour overall, and the first run downloads the patent rulebook.
- The corpus size is stated two ways in the repository. The description cites 76M+ patents while the BigQuery skill row in the README says 100M+, so treat the corpus as large and the exact figure as unverified.
- External keys gate coverage. Google Patents search needs a SerpApi key (250 searches a month free), EPO full text needs an OPS key, and USPTO search needs an Open Data Portal key. Without them the relevant search paths are unavailable.
- BigQuery past the free tier costs roughly two dollars per search according to the README, so bulk searching has a real bill attached.
- Best mode under 112(a) is explicitly left to manual review, which is a documented gap rather than an oversight.
- This is drafting assistance, not legal advice. Nothing in the tool checks whether your disclosure strategy makes commercial sense, and a patent attorney still has to read the result.
- The App Store style plugin path is Claude Code specific. The MCP server is the portable piece for other agents.

## Related

- [Claude for Legal Skills - Anthropic Legal Workflow Suite Setup](/hermes/skills/catalog/claude-for-legal-skills-setup)
- [LinkFox Skills - IP, Legal and Trade Data Setup](/hermes/skills/catalog/linkfox-skills-setup)
- [Skill Vetter - Security Audit for Hermes Skills Setup](/hermes/skills/catalog/skill-vetter-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the status tools before your first real request. Five cheap checks tell you whether search and diagrams are wired up, and the answer determines whether the output is grounded.
- Start with prior art, not with drafting. A patentability answer changes whether you draft at all, and the prior-art agent is much faster than the full drafting agent.
- Ask for the section number with every MPEP answer. A citation you can open in the rulebook is checkable in seconds, and a paragraph with no section number is model text.
- Use Google Patents search before BigQuery for exploratory work. It is free to 250 searches a month and BigQuery has a per-search cost past the free tier.
- Keep the validation report. The drafting agent returns one alongside the documents, and that report is the part a reviewer actually reads first.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
