---
title: "365 Skills - Diagram, Research and Media Suite Setup"
description: "Agents365-ai's 67.5K-install suite: draw.io, Excalidraw, PlantUML, Tldraw diagrams plus paper search, journals, TTS and video skills for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agents365-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "diagrams", "academic research", "claude code plugins"]
---

# 365 Skills - Setup Guide

**Source:** [agents365-ai/365-skills](https://www.skills.sh/agents365-ai/365-skills) via skills.sh - 67.5K combined installs across 40 indexed listings; snapshot 2026-10-28 (Oct 28 morning sweep)

**GitHub:** [Agents365-ai/365-skills](https://github.com/Agents365-ai/365-skills) - 97 stars, no LICENSE file at the repo root (31 plugin manifests declare MIT, 3 declare CC-BY-NC-4.0, and `pi-plugin-cc` ships its own Apache 2.0 text), branch main, 36 `SKILL.md` files across 34 plugin groups under `plugins/<plugin>/skills/<name>/`, last push 2026-10-16

**Category:** Diagrams as code, academic research, and Chinese-language media generation for coding agents

**Quality Tier:** 🟡 Beta - single-publisher vendor set, 97 GitHub stars, 40 indexed listings against 36 `SKILL.md` files, mixed per-plugin licensing with no root LICENSE file, six sampled security verdicts carrying three warnings

Agents365-ai publishes this repository as a general-purpose skill shelf rather than one product's workflow. The README groups its 34 plugin directories into five buckets: development and CLI design, drawing and diagrams, scientific research, knowledge and notes, and media and creative. A single `.claude-plugin/marketplace.json` manifest lists all 34 plugins with versions, keywords and per-plugin licenses, and the skills themselves are ordinary `SKILL.md` directories under `plugins/<plugin>/skills/`, so the set works with any agent that reads that layout.

The shape worth noting is that the diagram family is deliberately plural. Separate skills cover draw.io, Excalidraw, PlantUML, Mermaid and Tldraw, each emitting an editable source format (`.drawio`, `.excalidraw`, `.puml`, `.mmd`, `.tldr`) and exporting to raster or vector through Kroki or a local CLI, and the draw.io skill says outright to prefer Mermaid or PlantUML when diagrams as code are enough. The research side is a chain rather than a single skill: search the Semantic Scholar graph, fetch the PDF through a seven-source cascade, look up journal abbreviations and impact factors, and rank drug targets from a gene list. Two of the fifteen skills above the install cut are not in this tree at all: the README states that `drawio-skill` and `video-podcast-maker` live in their own repositories and are installed from there.

## Installation

The README leads with the skills.sh CLI, which copies the repository's skills into the agent's skill directory:

```bash
npx skills add Agents365-ai/365-skills -g
```

Claude Code users can add the repository as a plugin marketplace and install one group at a time:

```bash
/plugin marketplace add Agents365-ai/365-skills
/plugin install mermaid
```

The two separately hosted skills have their own install lines, both given in the README's Development section:

```bash
npx skills add Agents365-ai/drawio-skill -g
npx skills add Agents365-ai/video-podcast-maker/skills/video-podcast-maker -g
```

For any other agent, the clone is the install source. Each plugin directory holds one skill directory (three for `pi-plugin-cc`), and copying that directory into the agent's skills path is equivalent to a CLI install of it:

```bash
git clone --depth 1 https://github.com/Agents365-ai/365-skills.git
cp -R 365-skills/plugins/plantuml/skills/plantuml-skill ~/.hermes/profiles/corpusiq/skills/
```

Two dependencies sit outside the install. `asta-skill` queries the Semantic Scholar corpus through AI2's Asta MCP server, so the server has to be configured before the skill does anything. The Chinese media skills (`ttscn`, `imagencn`, `videogencn`) call vendor APIs and read their keys from the environment.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| drawio-skill | 9,009 | Editable `.drawio` diagrams: architecture, UML, ERD, sequence, BPMN, network and swimlane views authored from a description or converted from code, IaC, SQL and API schemas, then synced, queried, tested, reviewed and exported through `scripts/diagramctl.py`. Hosted in its own repository. |
| excalidraw | 4,604 | Hand-drawn whiteboard diagrams as `.excalidraw` files exported to PNG or SVG through the Kroki API or a local brute-export CLI, for sketches that should look deliberately informal. |
| creating-mermaid-diagrams | 4,155 | Mermaid text diagrams with automatic layout. The install index uses this name but the current tree has no directory of it, and the tree's Mermaid plugin is indexed separately as `mermaid-skill`. |
| plantuml-skill | 4,068 | PlantUML `.puml` sources for UML, C4, sequence, class, component and ER diagrams, including rendering PlantUML blocks already embedded in Markdown and exporting through Kroki with no local install. |
| tldraw-skill | 3,738 | Infinite-canvas `.tldr` JSON sketches exported to PNG or SVG locally through `@kitschpatrol/tldraw-cli`, for whiteboard-style systems and data-flow drawings. |
| paper-fetch | 3,429 | Fetching paper PDFs by DOI, arXiv id, title or citation list through a seven-source cascade (Unpaywall, Semantic Scholar, arXiv, PubMed Central, bioRxiv and medRxiv, publisher direct, Sci-Hub last), with batch mode and idempotent retries. |
| semanticscholar-skill | 3,417 | Semantic Scholar API work: paper search, citation graph lookups, author profiles and publications, paper recommendations and BibTeX export. |
| asta-skill | 3,068 | Ai2 Asta MCP queries against the Semantic Scholar graph: intent-to-tool routing, citation traversal, evidence snippets and DOI, arXiv or PMID lookup. Needs the Asta MCP server configured. |
| journal-abbrev | 3,000 | Journal abbreviation lookup and conversion between full names and ISO 4 or MEDLINE forms through a JabRef, AbbrevISO and NLM cascade, with BibTeX rewriting, an idempotency key and a JSON envelope for agents. |
| target-prioritization | 2,877 | Turning a ranked gene list into per-gene dossiers from UniProt, OpenTargets, PubMed, the Human Protein Atlas and ChEMBL, then re-ranking by a configurable composite score for convergence, druggability, genetics and tractability. |
| pi-prompting | 2,869 | Internal guidance from the `pi-plugin-cc` group for composing prompts that the Pi coding agent (DeepSeek by default) handles reliably on coding, review, diagnosis and research work. |
| pi-result-handling | 2,830 | The companion internal contract for presenting Pi helper output back to the user, so delegated results arrive in a consistent shape. |
| pi-cli-runtime | 2,823 | The runtime contract for calling the pi-companion CLI from Claude Code, covering how the helper is invoked and what it returns. |
| video-podcast-maker | 2,710 | Topic to narrated 4K explainer video: research, script, local TTS, Remotion render and background music, aimed at Bilibili, YouTube, Xiaohongshu, Douyin and WeChat Channels. Hosted in its own repository. |
| bangumi-frames | 2,293 | Bilibili anime frame collection: download, scene-change keyframes, scenery versus character crops, CCIP identity clustering, and optional OCR plus LaMa subtitle and watermark cleanup. Read-only, uploads nothing. |

The remaining 25 indexed listings range from 38 to 1,950 installs. `agent-native-design` (1,950), `obsidian-organizer` (1,799), `imagencn` (1,710) and `ttscn` (1,632) carry most of that weight, followed by `mermaid-skill` (593) and `assetseeker` (423). The middle of the tail is the research and reasoning set: `journal-if`, `videogencn`, `yt2bb`, `journal-meta`, `xfetch`, `bbc-skill`, the Obsidian and Zotero developer references, the scientific and grant reasoning skills, `figshare-skill`, `zenodo-skill`, `pi-dev-rules` and `tmux-skill`. It ends at `asta` (100), `pi-durable-dev-rules` (58) and `scholar-deep-research` (38).

## Why This Matters for Hermes Agents

Agents describe architecture constantly and usually produce prose or a screenshot. Every diagram skill here emits a source file the agent can edit later, which is the difference between a picture in a chat log and an artifact in the repository that survives the next refactor. The renderers also overlap on purpose: a flowchart belongs in Mermaid because it diffs cleanly, a review-ready system diagram belongs in draw.io because someone will move boxes, and the skills say which is which instead of guessing.

The research skills solve the part of literature work that agents fake most often. `paper-fetch` reports which of its seven sources answered, so a session can distinguish an open-access PDF from a paywall bypass, and `semanticscholar-skill` returns citation counts and author data rather than a plausible-looking reference list. `journal-abbrev` closes the last gap in a manuscript pipeline, because ISO 4 and MEDLINE forms are the thing a bibliography needs and the thing a model invents.

For Hermes the useful default is narrower than the index. A session almost never needs all five diagram skills, and installing all five costs context on every turn while they differ mainly in output format. Pick by output format: text when the diagram has to be reviewed as a diff, a canvas file when a human will rearrange it, and a rendered export when the diagram is going into a document.

Two cautions belong in the same breath as the recommendation. Three of the 34 plugin manifests declare CC-BY-NC-4.0 rather than MIT, so a set installed wholesale is not uniformly usable in commercial work, and the repository has no root LICENSE file to settle the question. And the install index runs ahead of the tree: 40 listings point at 36 `SKILL.md` files, with two of the biggest living in other repositories.

## Usage

| You say | What happens |
|---|---|
| "Draw the architecture of this repo as something I can edit" | drawio-skill reads the code and infrastructure files, builds an editable `.drawio` file, then exports PNG or SVG while leaving the source for later sync and review. |
| "This diagram has to survive code review" | The Mermaid plugin emits `.mmd` text that diffs line by line in a pull request, rather than a binary canvas that shows up as a changed blob. |
| "Get me the PDF for this DOI" | paper-fetch walks its seven sources in order and tells you which one produced the file, so an open-access copy and a last-resort fallback are not reported the same way. |
| "Who cited this paper, and who else works on it" | semanticscholar-skill traverses the citation graph and author profiles, or asta-skill does the same over the Asta MCP server with evidence snippets when that server is configured. |
| "Standardise the journal names in my .bib file" | journal-abbrev runs a dry pass, rewrites to ISO 4 or MEDLINE abbreviations with a stable idempotency key, so a second run changes nothing. |
| "Which of these candidate genes should we follow up" | target-prioritization fans out UniProt, OpenTargets, PubMed, HPA and ChEMBL queries per gene, then returns a scored dossier with the evidence behind each rank. |
| "Turn this topic into a ten minute explainer" | video-podcast-maker runs research, script, TTS and a Remotion render to a 4K MP4, and reuses the existing project directory when you ask for a re-render. |

## Verification

Probe the paths before installing. These five returned 200 when this guide was written:

```bash
for p in plugins/plantuml/skills/plantuml-skill/SKILL.md \
         plugins/paper-fetch/skills/paper-fetch/SKILL.md \
         plugins/asta/skills/asta-skill/SKILL.md \
         plugins/semanticscholar/skills/semanticscholar-skill/SKILL.md \
         plugins/mermaid/skills/mermaid-skill/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/Agents365-ai/365-skills/main/$p"
done
```

The two separately hosted skills have their own paths, both confirmed at 200:

- https://raw.githubusercontent.com/Agents365-ai/drawio-skill/main/skills/drawio-skill/SKILL.md
- https://raw.githubusercontent.com/Agents365-ai/video-podcast-maker/main/skills/video-podcast-maker/SKILL.md

Read the ones that touch credentials, paywalls or vendor APIs before installing them: `paper-fetch`, `asta-skill`, `ttscn`, `imagencn` and `videogencn`.

After install, confirm what actually landed. The frontmatter `name` is what the install index matches on, and it does not always equal the directory name, so check both:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -cE '^(plantuml|paper-fetch|asta|semanticscholar|mermaid)'
head -3 ~/.hermes/profiles/corpusiq/skills/asta-skill/SKILL.md
```

The clone carries 36 `SKILL.md` files, so a count well above that after an install means the same skill landed twice, which happens when the CLI and a manual copy both run.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| drawio-skill | Pass | Pass | Pass |
| excalidraw | Pass | Warn | Warn |
| creating-mermaid-diagrams | Pass | Pass | Pass |
| plantuml-skill | Pass | Pass | Warn |
| tldraw-skill | Pass | Pass | Pass |
| paper-fetch | Pass | Warn | Warn |

The warnings land on three of the six sampled skills, and all three reach outside the local machine for their output. `excalidraw` and `plantuml-skill` send diagram source to the Kroki API unless a local renderer is installed, and `paper-fetch` reaches out to seven sources including Sci-Hub mirrors. The recorded codes are W011 and W012 on Snyk and a Socket warning on `excalidraw` and `paper-fetch`; read the detail page rather than treating the single word as a verdict.

Install time is quiet and run time is not. The repository has no root `package.json`, so adding the skills runs no lifecycle script, and only `pi-plugin-cc` ships a `hooks` directory: `SessionStart`, `SessionEnd` and a `Stop` gate that runs node scripts, with the stop gate allowed 900 seconds. That plugin also carries its own Apache 2.0 license text, which is broader than the MIT string its manifest declares.

Credentials and licensing are the two things to settle before a fleet install. The media skills read vendor keys from the environment (`DASHSCOPE_API_KEY`, `ARK_API_KEY`, `HUNYUAN_API_KEY`, `ZHIPUAI_API_KEY`, `OPENAI_API_KEY`), so they should get scoped keys rather than a shared production one, and `asta-skill` needs an Asta MCP endpoint before it can do anything. On licensing, the root of the repository has no LICENSE file, 31 plugin manifests declare MIT, three declare CC-BY-NC-4.0 (`obsidian-organizer`, `tmux`, `zotero-dev-rules`) and the non-commercial terms are repeated in each of those three plugin directories. Treat a wholesale install as a mixed-license bundle.

## Limitations

- Snapshot data, verified 2026-10-28: 67,542 combined installs across 40 indexed listings; 97 GitHub stars; no LICENSE file at the repo root; last pushed 2026-10-16. Counts drift over time.
- The install index outruns the tree: 40 indexed listings against 36 `SKILL.md` files. `drawio-skill` and `video-podcast-maker` are published from their own repositories by the README's own instruction, `creating-mermaid-diagrams` has no directory of that name in the current tree, and `asta-skill` resolves to `plugins/asta/skills/asta-skill` whose `SKILL.md` is named `asta`, with a second `asta` listing at 100 installs.
- There is no LICENSE file at the repository root. 31 plugin manifests declare MIT, `obsidian-organizer`, `tmux` and `zotero-dev-rules` declare CC-BY-NC-4.0, and `pi-plugin-cc` ships Apache 2.0 text under an MIT manifest string. Install the permissive groups only if the work is commercial.
- Three of the fifteen rows above are not standalone tasks. `pi-prompting`, `pi-result-handling` and `pi-cli-runtime` are internal contracts for the `pi-plugin-cc` commands, and installing them alone gives an agent guidance it has no entry point to use.
- The media skills are thin wrappers over Chinese vendor APIs and change with those vendors. Key names, model lists and backends drift between the README (14 TTS backends), the skill file (15) and the vendor consoles.
- `paper-fetch` uses Sci-Hub mirrors as its last-resort source. Treat that path as a policy decision for your own environment rather than a neutral fallback, and disable it where it is not acceptable.

## Related

- [Design Doc Mermaid Skill - Diagram & Documentation Setup](/hermes/skills/catalog/design-doc-mermaid-setup)
- [Archify - Interactive Architecture Diagram Skill Setup](/hermes/skills/catalog/archify-setup)
- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by output format, not by topic. Text formats (`.mmd`, `.puml`) for anything that will be reviewed as a diff, canvas formats (`.drawio`, `.excalidraw`, `.tldr`) for anything a human will rearrange, and one renderer is enough for most sessions.
- Use `drawio-skill` when the diagram must stay editable and Mermaid when it must stay readable. Its own description says to prefer Mermaid or PlantUML when diagrams as code are enough, and following that advice saves a large skill from being loaded for a flowchart.
- Ask for the source path before the image. Every diagram skill writes a file, and confirming which file was written catches the case where the agent rendered into a temp directory that the next turn will not find.
- For literature work, chain the skills in order: `semanticscholar-skill` or `asta-skill` to find the paper, `paper-fetch` to get the PDF, `journal-abbrev` and `journal-if` to fix the citation. Each one reports its own sources, so a chained run leaves an audit trail.
- Keep `pi-plugin-cc` out of a shared skills directory unless you want its hooks. It is the only plugin here that registers session lifecycle commands, and the stop gate can hold a turn for up to 900 seconds.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
