---
title: "Markdown Viewer Skills - Diagrams, Charts and Cards Setup"
description: "Markdown Viewer skills: 51.0K combined installs for diagrams, architecture, charts and cards written as text in Markdown, rendered live."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/markdown-viewer-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "markdown diagrams", "visualization"]
---

# Markdown Viewer Skills - Setup Guide

Markdown Viewer (docu.md) is the team behind the multi-platform Markdown extension for Chrome, Edge, Firefox, VS Code and Obsidian, and this repository is its skill package for producing figures inside a Markdown document. The design decision that matters is simple: a figure is text in the document, written in a fence (`plantuml`, `vega`, `vega-lite`, `echarts`, `infographic`) or as bare HTML, and the host viewer renders it live. Nothing is pre-rendered, nothing is built, and the block stays editable.

The package is compact but the install index is not. skills.sh indexes 21 listings for this publisher at 51.0K combined installs, and 16 of them carry enough installs to matter, yet the current tree holds exactly one skill directory, `documd-visuals/`. The repository used to ship 14 engine- and domain-named skills (uml, cloud, network, security, iot, data-analytics, archimate, bpmn, mindmap, vega, graphviz, infographic, architecture, infocard) and consolidated them into one routing package whose content was rewritten rather than copied. The old names still carry install counts, which is why the top of this table reads like a catalogue of diagram engines.

**Source:** [markdown-viewer/skills](https://www.skills.sh/markdown-viewer/skills) via skills.sh - 51.0K combined installs across 21 indexed listings; first seen Feb 6, 2026 (Oct 26, 2026 sweep)
**GitHub:** [markdown-viewer/skills](https://github.com/markdown-viewer/skills) (3,378 stars; CC-BY-4.0 for the skill package, with the documd CLI and the rendering engines licensed separately under GPL-3.0-only; branch main, pushed 2026-10-06; layout is one package at `documd-visuals/SKILL.md` with `goals/`, `engines/`, `examples/`, `styles/` and `catalog/` beneath it, while `research/` and `scripts/` are repo-only and are never discovered as skills)
**Category:** Diagrams / Visual Deliverables
**Quality Tier:** 🟡 Beta - 51.0K installs, 3,378 stars and a CC-BY-4.0 skill package with Gen Agent Trust Hub, Socket and Snyk all Pass on the three sampled skills, held below Production by the index-versus-tree gap (21 indexed listings against one in-tree package) and by an install base that predates the Sep 22, 2026 consolidation, so most of the volume sits on skill names the repository no longer ships

## Installation

```bash
# Install the package with the skills CLI
npx skills add markdown-viewer/skills
```

```bash
# Manual install from the README, for Claude Code
cp -r skills/documd-visuals ~/.claude/skills/
```

The README's manual path assumes the package sits under `skills/`. In the current checkout `documd-visuals/` is at the repository root instead, so adjust the source path if that copy fails. Nothing else is required: there is no runtime, API key, environment variable or bundled dependency, because the figures are text and the host viewer does the drawing.

```bash
# Optional export half, a separate tool that the skill points at
npx @markdown-viewer/documd report.md report.docx
npm install -g @markdown-viewer/documd
```

Installing the skill does not install the CLI, and the README is explicit that it cannot: the Agent Skills format has no install hook, and `npx skills add` runs no scripts of its own, so there is no point at which a package could trigger `npm install`. Export to docx, pdf, epub, html, png or svg is documented inside the package in `documd-visuals/converting.md`, which is linked from `SKILL.md`, so an agent that reads the skill knows the export path exists without it being installed.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| uml | 3,866 | UML diagrams in PlantUML syntax; the content now lives in `engines/plantuml.md` plus the software-design and software-behaviour example sets |
| architecture | 3,727 | Layered system architecture diagrams as bare HTML, with the seven architecture shapes, page skeletons and connectors documented in `engines/html-css.md` |
| infographic | 3,522 | Template-driven infographics for roadmaps, sequences and comparisons using the `infographic` fence |
| graphviz | 3,399 | Graph and dependency diagrams; the README states the dot examples were re-authored as PlantUML rectangles and the dot engine was removed |
| bpmn | 3,365 | BPMN process and approval diagrams, now under the process-and-workflow example domain |
| canvas | 3,323 | JSON Canvas boards with free x/y node placement, for concept maps, knowledge graphs and planning boards; the format is no longer recommended by the package |
| network | 3,249 | Network topology diagrams with vendor device stencils, under the network-topology example domain |
| data-analytics | 3,248 | Charts and analytical views over a dataset, routed through the data and metrics goal domains |
| mindmap | 3,210 | Hierarchical mind maps and outline trees, under the knowledge-and-outline example domain |
| archimate | 3,181 | ArchiMate enterprise architecture models, under the enterprise-architecture example domain |
| vega | 3,120 | Vega and Vega-Lite charts that need data transforms, faceting or statistics, documented in `engines/vega.md` |
| cloud | 3,060 | Cloud architecture diagrams with provider icon sets, under the cloud-architecture example domain |
| infocard | 3,058 | Infographic cards and page-level layouts; the card prototypes became the internal-documents, catalogues-and-inventories and customer-and-partner-comms examples |
| iot | 2,986 | IoT and connected-device diagrams; the content was folded into the cloud, network and data-platform example sets |
| security | 2,919 | Security and compliance architecture diagrams, under the security-and-compliance example domain |
| mermaid | 539 | Flowcharts, sequence, state and class diagrams in mermaid syntax; the package now lists mermaid as not recommended and routes that work to PlantUML |

The remaining 5 indexed listings range from 112 to 319 installs. Only one listing, `documd-visuals`, still matches a directory in the current tree, so the install counts above describe names that were consolidated on Sep 22, 2026 rather than 16 separate packages you will find on disk.

## Why This Matters for Hermes Agents

Most diagram tooling asks an agent to leave the document: render a file, upload it, paste a URL back. This package removes that round trip. The agent writes a fence or a block of HTML into the Markdown it is already editing, and the figure is part of the file, reviewable in a diff and editable by the next person who opens it. For a docs pipeline that is the difference between a diagram that survives review and an image nobody can regenerate.

The routing is also built for context discipline. `documd-visuals/SKILL.md` is a router with iron rules and 31 goal domains; the domains are grouped into four meta-clusters (data and metrics, process and systems, infrastructure and governance, knowledge and expression), and each goal then points at a per-engine reference and a worked example. An agent loads the router, matches the request to one goal, and reads only that goal's examples, which is why a 242-example library does not flood the context window.

The choice of live rendering over pre-rendering has a practical consequence for agents working in CI: there is nothing to install on a build machine to produce the document, and no rendering step that can fail differently on a headless runner. The optional CLI is an export convenience, not a dependency of authoring, and the README is careful to keep those two things apart.

The honest limit is scope. This is a figure-authoring package, not a charting library: it will not fetch your data, and every chart fence must carry its own values inline. An agent that expects the skill to query an API will be disappointed, and one that can hand it a small inline dataset will get a clean, on-theme figure.

## Usage

| You say | What happens |
|---|---|
| "Draw the architecture for this service" | Loads the router, picks the bare-HTML architecture shape from `engines/html-css.md`, and writes a layered diagram into the Markdown |
| "Add a chart of monthly churn to this page" | Routes to the data and metrics cluster, then writes a `vega` or `echarts` fence with the data inlined |
| "I need an infographic for the rollout roadmap" | Uses the `infographic` fence and a roadmap or sequence template, then colours it from one of the nine themes |
| "Turn these notes into a one-page brief" | Starts from an internal-documents example as the page skeleton and fills the sections |
| "Export this report to docx" | Points at `converting.md` for the documd CLI and the flags that survive export |
| "Can we just do this in mermaid?" | Applies the iron rules: mermaid is named as not recommended, so the figure is re-authored in PlantUML or bare HTML |

## Verification

Confirm what the skills CLI installed:

```bash
npx skills list | grep -i documd-visuals
```

Read the package before installing it. The four URLs below returned 200 with `curl -s -o /dev/null -w "%{http_code}"` when checked on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/markdown-viewer/skills/main/README.md
curl -sL https://raw.githubusercontent.com/markdown-viewer/skills/main/documd-visuals/SKILL.md
curl -sL https://raw.githubusercontent.com/markdown-viewer/skills/main/documd-visuals/converting.md
curl -sL https://raw.githubusercontent.com/markdown-viewer/skills/main/documd-visuals/engines/plantuml.md
```

The repository root listing behind the install index also returned 200 on the same date, and it is the fastest way to see that the package is a single directory:

```bash
curl -s https://api.github.com/repos/markdown-viewer/skills/contents/ | grep '"name"'
```

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| uml | Pass | Pass | Pass |
| architecture | Pass | Pass | Pass |
| infographic | Pass | Pass | Pass |

The package is Markdown and nothing else. No SKILL.md declares an `allowed-tools` field, so no skill asks the host for shell, write or network permission of its own, and `npx skills add` copies or symlinks files without executing anything. The repository's own gates (`scripts/check-all.mjs`, `validate-skills.mjs`, `verify-examples.mjs`) run in the maintainer's checkout, not in yours.

The one real surface is rendering. Figures can be bare HTML, and bare HTML in a document is HTML that the viewer draws, so a document received from an untrusted source deserves the same caution as any other HTML file. The package also enforces its own hygiene rule that a fenced `html` block becomes an image rather than a live figure, which keeps the distinction visible.

Licensing is split and worth stating plainly: the skill package is CC-BY-4.0, while `@markdown-viewer/documd`, `@markdown-viewer/draw-uml` and `@markdown-viewer/drawio2svg` are separate works under GPL-3.0-only. Installing the skill licenses neither of those, and attribution is only required when you redistribute the package.

## Limitations

- The install index outruns the tree. 21 listings are indexed and one package is in the repository, so 20 of the names above are historical; a search for `uml` on skills.sh will not install an `uml` directory.
- One skill, not a suite. Installing gives an agent a single router with 31 goal domains, which is a smaller surface than the 16-row table suggests and a different mental model from picking a skill per engine.
- The README's manual install command points at `skills/documd-visuals`, while the current checkout has `documd-visuals/` at the repository root. Check the path before copying.
- Authoring only. No skill fetches data, queries an API or writes files; every chart fence must carry its own inline values, and there is no eval suite in the repo that measures output quality.
- The CLI and the engines are separate GPL-3.0-only works. Installing the skill does not install or license them, so export is a second decision with its own terms.
- Snapshot data, verified Oct 26, 2026: 50,975 combined installs across 21 indexed listings; 3,378 GitHub stars; CC-BY-4.0; last pushed 2026-10-06. Counts drift over time.

## Related

- [Diagram Design - Editorial HTML and SVG Diagrams](/hermes/skills/catalog/diagram-design-setup) - the closest alternative for hand-authored HTML and SVG figures when you want a fixed editorial style rather than a live-rendered fence.
- [Design Doc Mermaid Skill - Diagram & Documentation Setup](/hermes/skills/catalog/design-doc-mermaid-setup) - the mermaid-first route for teams already standardised on mermaid syntax, which this package explicitly does not recommend.
- [Archify - Interactive Architecture Diagram Skill Setup](/hermes/skills/catalog/archify-setup) - architecture diagrams as a standalone, interactive deliverable instead of a block inside a document.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Say which artifact you want before you describe the content. "A layered architecture diagram in the document" and "a PNG of our architecture" route to different halves of this package, and only one of them needs the CLI.
- Keep the package self-contained. Its gate fails the build if a file cites `research/` or `scripts/`, and the same rule is good practice in your own prompts: reference `examples/` files by path instead of pasting their content.
- Inline small datasets. A `vega` or `echarts` fence must carry its own `values`/`series`, so hand the agent a dozen rows rather than a database connection it cannot open.
- Never write a fenced `html` block for a figure. Bare HTML renders live; a fenced block becomes an image.
- Write the scope in full when calling the export CLI: `npx @markdown-viewer/documd`, never bare `documd`, which is an unrelated npm package.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
