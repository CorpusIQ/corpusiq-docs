---
title: "Qodex AI Agent Skills - 81 Skill Starter Library"
description: "qodex-ai/ai-agent-skills: 21.4K combined installs. Eighty-one skills across documents, research, coding, design and agent operations."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/qodex-ai-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "agent library", "documents", "research"]
---

# Qodex AI Agent Skills - Setup Guide

**Source:** [qodex-ai/ai-agent-skills](https://www.skills.sh/qodex-ai/ai-agent-skills) via skills.sh - 21.4K combined installs across 81 indexed listings; first seen 2026-11-02 (morning sweep)

**GitHub:** [qodex-ai/ai-agent-skills](https://github.com/qodex-ai/ai-agent-skills) - 47 stars, no license and no `LICENSE` file in the root, branch main, last pushed 2026-01-05; 81 `SKILL.md` files, 80 of them one directory each under `skills/` and the last the top-level `template/SKILL.md`

**Category:** General agent skill library: 81 skills spanning research, coding, content, business and operations workflows

**Quality Tier:** 🟡 Beta - 21.4K installs across a large tree, but no license file in the root, four document skills that are source-available rather than open source, and one Snyk warning across five sampled listings

This is a general-purpose skill library rather than one focused pack. The eighty skills under `skills/` cover document processing, multi-agent orchestration, financial and legal analysis, research, RAG and retrieval, design and interface work, cloud and deployment patterns, and a long tail of documentation and workflow helpers. Each skill is a self-contained folder with a `SKILL.md` carrying instructions, examples and guidelines, which is the same layout Anthropic defines for the Agent Skills format.

The README is Anthropic's skills README carried over almost verbatim, down to the note at the top that the repository contains Anthropic's implementation of skills for Claude. Its install instructions therefore describe the upstream marketplace, not this repository, and the local `.claude-plugin/marketplace.json` still declares the name `anthropic-agent-skills` with two plugin bundles: `document-skills` with four skills and `example-skills` with twelve. That covers sixteen of the eighty skills in the tree, so the plugin route installs a fraction of the library and the skills CLI is the better entry point.

The four document skills are the pull. `word-document-processor`, `spreadsheet-processor`, `presentation-builder` and `portable-document-handler` are the ones the README says power Claude's own document capabilities, and they are the ones that ship real code: OOXML helpers, Python scripts, templates, schemas and fonts. They are also the ones the README explicitly calls source-available rather than open source, and each carries its own `LICENSE.txt`.

## Installation

The README documents no `npx skills add` line, so the generic skills CLI path is the one to use:

```bash
npx skills add qodex-ai/ai-agent-skills
```

That pulls the whole library. To take one skill, the CLI's own `--skill` flag narrows it, but confirm the folder exists in the current tree first, because the tree and the index do not line up exactly:

```bash
npx skills add qodex-ai/ai-agent-skills --skill word-document-processor
```

The README's documented route is the Claude Code plugin marketplace, and it names the upstream repository it was copied from:

```text
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

Those two plugins map to `.claude-plugin/marketplace.json` in this repository, which declares four document skills and twelve example skills. If you want the plugin route against this fork, point the marketplace command at `qodex-ai/ai-agent-skills` instead, and expect the sixteen bundled skills rather than all eighty.

Each skill is a folder with a `SKILL.md`, so a directory copy is the manual route. This loop copies every skill folder into a Hermes profile and leaves existing folders alone:

```bash
git clone https://github.com/qodex-ai/ai-agent-skills.git
mkdir -p ~/.hermes/profiles/corpusiq/skills
for skill in ai-agent-skills/skills/*; do
  [ -f "$skill/SKILL.md" ] || continue
  destination="$HOME/.hermes/profiles/corpusiq/skills/$(basename "$skill")"
  [ -e "$destination" ] || cp -R "$skill" "$destination"
done
```

Nothing in the repository mentions Hermes. The instructions are Markdown, so the same folders load anywhere, but several of the document skills expect Python and Node at run time and their scripts are written against Anthropic's own file layout.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| word-document-processor | 3,586 | Word documents with format preservation, tracked changes and metadata, backed by the docx Python scripts, OOXML helpers and templates that ship inside the skill folder. |
| multi-agent-orchestration | 2,111 | Designing coordinated agent teams: communication between agents, task delegation, workflow orchestration and aggregation of results. |
| financial-analysis-agent | 1,263 | Agents for financial analysis, investment research and portfolio work: data processing, risk analysis and recommendation generation. |
| legal-document-analyzer | 1,167 | Contract review, compliance checking, document parsing and risk identification for legal and procurement workflows. |
| ecommerce-platform-specialist | 657 | Expert guidance on Shopify: store setup, product data, customization and optimization. |
| spreadsheet-processor | 623 | Creating, editing and analyzing Excel files with formula and formatting support, plus a recalculation script. |
| creative-generation-agent | 572 | Agents that generate music, memes, podcasts and multimedia, with style transfer and creative control. |
| chat-with-arxiv | 303 | Chat agents over arXiv papers: paper retrieval, content processing, question answering and research synthesis. |
| deep-research-agent | 286 | Research planning, source evaluation and report generation across multiple sources. |
| autonomous-agent-gaming | 270 | Game-playing agents with reinforcement learning, decision-making, strategy development and performance tuning. |
| rag-agent-builder | 260 | Retrieval-augmented generation: vector databases, embeddings, retrieval strategies and response generation. |
| generate-swagger-docs | 254 | OpenAPI documentation generated from source: endpoint discovery, `swagger.json` and interactive HTML docs. |
| system-design | 217 | Planning system components, their interactions and deployment patterns for scalability and maintainability. |
| voice-ai-integration | 209 | Voice-enabled applications: speech recognition, text to speech and real-time processing across providers. |
| user-interface-designer | 205 | Wireframes, visual designs and interactive prototypes for web applications with a usability focus. |
| presentation-builder | 201 | Slide creation and editing: layouts, animations, speaker notes and an HTML to PPTX path. |
| financial-document-management | 195 | Organizing invoices and financial records: categorization, information extraction and structured filing. |
| llm-fine-tuning-guide | 194 | Fine-tuning for a domain: data preparation, training techniques, optimization strategies and evaluation. |
| aesthetic-analysis | 190 | Extracting design systems from visual references: palettes, typography, layout principles and component patterns. |
| component-interface-design | 182 | Interfaces built from component libraries and design systems, using accessible primitives. |

The remaining 61 indexed listings range from 123 to 172 installs.

That tail is dense and mostly self-describing: research and documentation helpers (`research-management`, `workspace-documentation`, `capability-documentation`), planning skills (`plan-implementation`, `planning-documentation`, `specification-executor`), interface skills (`web-interface-architect`, `interactive-component-creator`, `design-system-generator`) and a cluster of agent-infrastructure skills around capability assessment, delegation and workspace isolation. The floor is `infrastructure-code-synthesis` at 123.

The index is one row wider than the tree. There are 81 listings and 80 `SKILL.md` files under `skills/`; the missing listing is `template-skill`, which resolves to the top-level `template/SKILL.md`, where the frontmatter reads `name: template-skill`. It is the blank skill template the README points at, not a folder under `skills/`.

## Why This Matters for Hermes Agents

A general library is useful for the opposite reason a focused pack is: it gives an agent vocabulary it did not have. The document skills are the concrete case. Word and Excel work is where agents usually produce a plausible file that a human then has to rebuild, and these skills ship the OOXML handling and scripts that keep formatting, tracked changes and metadata intact.

The agent-infrastructure half is the interesting read for anyone running a multi-agent setup. `multi-agent-orchestration` covers communication, delegation and result aggregation; `capability-assessment`, `capability-activation` and `capability-documentation` describe how an agent inventories and exposes what it can do; `workspace-isolation` and `distributed-task-execution` cover the plumbing around concurrent work. Read as a set, they are a description of an agent platform written as skills.

The library is also a pattern reference. The `spec/` folder holds the Agent Skills specification, `template/` holds the blank template, and the README explains that frontmatter needs only a `name` and a `description`. That makes the repository a decent place to learn the format before writing your own skills, which is what the README says it is for.

The caveats matter as much as the contents. There is no license file in the root, four of the document skills are source-available rather than open source, the README calls everything demonstration and educational, and the last push was 2026-01-05. Treat this as a source of patterns to review and adopt selectively, not as a dependency to install wholesale and forget.

## Usage

| You say | What happens |
|---|---|
| "Turn this outline into a formatted Word document with tracked changes" | word-document-processor builds the docx through its OOXML scripts, preserving styles and metadata rather than flattening the document. |
| "Build me a spreadsheet that recalculates this model" | spreadsheet-processor creates or edits the workbook, keeps formulas intact and uses its recalculation script to check the numbers. |
| "Design the agent team for this workflow" | multi-agent-orchestration lays out the specialists, how they talk to each other, how tasks are delegated and how results are merged. |
| "Review this contract for risk and compliance gaps" | legal-document-analyzer parses the document, flags risky clauses and checks compliance points, then returns the findings. |
| "Read these arXiv papers and brief me" | chat-with-arxiv retrieves the papers, processes the content and answers with citations to the source sections. |
| "Document our API from the codebase" | generate-swagger-docs walks the repository, discovers endpoints and writes `swagger.json` plus interactive HTML documentation. |
| "Give me a retrieval pipeline over our internal docs" | rag-agent-builder plans the embeddings, vector store and retrieval strategy, then describes the response generation layer. |

## Verification

The raw paths below returned 200 on branch main when this guide was written on 2026-11-02:

```bash
for p in word-document-processor multi-agent-orchestration spreadsheet-processor; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/qodex-ai/ai-agent-skills/main/skills/$p/SKILL.md"
done
```

After a clone, count what actually exists rather than trusting the index:

```bash
git clone --depth 1 https://github.com/qodex-ai/ai-agent-skills.git /tmp/qodex-agent-skills
find /tmp/qodex-agent-skills/skills -name SKILL.md | wc -l
find /tmp/qodex-agent-skills -name SKILL.md | wc -l
head -4 /tmp/qodex-agent-skills/skills/word-document-processor/SKILL.md
```

The first count should be 80 and the second 81, the difference being `template/SKILL.md`. The `head` prints the `name:` and `description:` frontmatter of the top listing, which is what the agent routes on.

Check the license terms before you adopt the document skills, since they are the ones with real code in them:

```bash
ls /tmp/qodex-agent-skills/skills/word-document-processor/LICENSE.txt
ls /tmp/qodex-agent-skills/LICENSE
```

The first file exists and the second does not, which is the whole licensing story: per-skill terms, no repository-wide grant.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| word-document-processor | Pass | Pass | Pass |
| market-intelligence-gather | Pass | Pass | Warn |
| quality-validation | Pass | Pass | Pass |
| diagnostic-analysis | Pass | Pass | Pass |
| infrastructure-code-synthesis | Pass | Pass | Pass |

Four of the five sampled listings pass all three auditors. `market-intelligence-gather` carries the single Snyk warning in the sample, and it is a scraping-and-aggregation skill, so the warning is worth reading before you point it at a source you care about.

The disk surface is larger than a Markdown-only pack. The repository holds 123 Python files, 78 XSD schemas, 54 font files and 7 shell scripts, concentrated in the document skills: `word-document-processor` ships a `scripts/` folder, an `ooxml/` helper directory and a `docx-js.md` note, `presentation-builder` carries an `ooxml/` copy and an `html2pptx.md`, and `portable-document-handler` ships form and reference material next to its scripts. Nothing runs on clone, but a document skill that writes to disk and shells out to Python deserves a read of its `scripts/` folder before an unattended run.

There is no license file in the repository root, and four of the document skills carry their own `LICENSE.txt` marking them source-available. That is a permission question rather than a vulnerability, and it lands on exactly the skills most people want from this repo.

## Limitations

- Snapshot data, verified 2026-11-02: 21,371 combined installs across 81 indexed listings; 47 GitHub stars; no license file; last pushed 2026-01-05. Counts drift over time.
- No `LICENSE` file exists in the repository root. The four document skills carry their own `LICENSE.txt` and the README calls them source-available, not open source, so redistribution needs a read of those terms first.
- The index is one row wider than the tree: 81 listings against 80 `SKILL.md` files under `skills/`, with `template-skill` resolving to the top-level `template/SKILL.md`.
- The README is Anthropic's skills README carried over, so its plugin block names `anthropics/skills`. The local `.claude-plugin/marketplace.json` bundles 16 of the 80 skills, and the README's own disclaimer calls the skills demonstration and educational only.
- Last pushed 2026-01-05, which makes this the oldest snapshot in its batch. The plugin manifest still declares version 1.0.0 and the upstream `anthropic-agent-skills` name.
- Several skills expect Python and Node at run time, and their scripts are written against Anthropic's own document layout rather than a general environment.

## Related

- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)
- [Agentic Awesome Skills - 2,000+ Skill Catalog Setup](/hermes/skills/catalog/agentic-awesome-skills-setup)
- [Agent Skill Creator - Skill Generation and Templating Setup](/hermes/skills/catalog/agent-skill-creator-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by name, not by collection. Eighty skills compete for context, and a library this wide is better treated as a menu you pick from than a folder you drop in whole.
- Read the `spec/` folder before writing your own skills. It is the Agent Skills specification, and it explains the `name` and `description` contract that every routing decision depends on.
- Start with the four document skills if documents are the job. They are the ones with scripts, the ones the README says run in production, and the ones with their own license terms.
- Check for a `SKILL.md` before asking for a skill by name. `template-skill` exists in the index but not under `skills/`, and a missing folder fails quietly.
- Copy the pattern, not the code, for anything you plan to depend on. The last push is old, and a skill read as a design document ages much better than one installed as a dependency.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
