---
title: "DDC Construction Skills - BIM and Cost Takeoff Setup"
description: "DataDrivenConstruction: 4.5K combined installs across 20 listings; construction skills for BIM analysis, CAD conversion and cost takeoff"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ddc-construction-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-10"
tags: ["hermes skill", "agent skill", "skill setup", "construction", "bim", "cost estimation", "cad"]
---

# DDC Construction Skills - Setup Guide

**Source:** [datadrivenconstruction/ddc_skills_for_ai_agents_in_construction](https://www.skills.sh/datadrivenconstruction/ddc_skills_for_ai_agents_in_construction) via skills.sh - 4.5K combined installs across 20 indexed listings (4,538 exact); first seen 2026-11-10 (Nov 10, 2026 sweep)
**GitHub:** 402 stars, MIT license, `main` branch, last pushed 2026-10-19, 238 `SKILL.md` files across six numbered category trees (`1_DDC_Toolkit/`, `2_DDC_Book/`, `3_DDC_Insights/`, `4_DDC_Curated/`, `5_DDC_Innovative/`, `6_OpenConstructionERP/`)
**Category:** Construction operations: BIM analysis, CAD and IFC conversion, quantity takeoff, cost estimation, scheduling and document control
**Quality Tier:** 🟡 Solid with caveats - Agent Trust Hub and Snyk pass every sampled listing, but Socket warns on five of the conversion skills, and this is a vertical suite with real file-format dependencies.

DataDrivenConstruction publishes this collection as a working toolkit rather than a demo. The root README counts 238 skills in six categories and describes them as production tools and databases from the vendor's own product line, backed by three separate open repositories: a cost database with eight national bases and thirty markets, a CAD and BIM conversion pipeline, and a BIM visualisation tool.

The six categories are a progression rather than a taxonomy. `1_DDC_Toolkit` holds the tool-backed skills that wrap real CLIs: exporters that turn Revit, IFC, DWG and DGN files into Excel, a CWICR cost database, analytics. `2_DDC_Book` maps skills to chapters of a construction data book, moving from data types through estimation to machine learning. `3_DDC_Insights` is workflow automation with n8n and field tools. `4_DDC_Curated` is document generation across PDF, Excel, DOCX and PPTX. `5_DDC_Innovative` is the advanced end: computer vision, digital twins, ESG, EU AI Act and generative design. `6_OpenConstructionERP` covers the vendor's open-source ERP.

The 20 indexed listings are heavily weighted toward the first two categories, and they cluster around one workflow that any construction data team recognises: get the model out of the authoring tool, extract quantities, price them, schedule them, and track the paperwork afterwards.

## Installation

The README's own route is deliberately low-tech: install the prerequisites, open a skill folder in your AI assistant, and follow the `SKILL.md`. Its prerequisite line covers the Python side of the conversion skills:

```bash
pip install pandas openpyxl ifcopenshell pdfplumber
```

`ifcopenshell` is the load-bearing dependency. The IFC extraction skills parse models through it, and nothing works without it.

Because the repository follows the open Agent Skills format and carries plugin metadata for Claude Code and Codex, the CLI route also works and is what skills.sh indexes:

```bash
npx skills add datadrivenconstruction/ddc_skills_for_ai_agents_in_construction
```

Individual listings install by name:

```bash
npx skills add datadrivenconstruction/ddc_skills_for_ai_agents_in_construction --skill warranty-tracker
```

The two routes differ in what you get. The README route assumes you are reading one skill and adapting its generated code by hand, which matches how the toolkit skills are written. The CLI route drops skill text into the agent's directory and leaves the environment setup to you, so the `pip install` line is still required either way.

Two skills need more than Python. `dwg-to-excel`, `ifc-to-excel` and `batch-cad-converter` drive DDC's own exporter CLIs (`DwgExporter`, `IfcExporter`), which are separate downloads from the tool repository the README links. Read the skill's own prerequisites section before promising an output file.

## What It Provides

Twelve listings clear the 150-install threshold:

| Skill | Installs | Use For |
|---|---|---|
| warranty-tracker | 1,000 | Tracks construction warranties: expiration dates, claims and manufacturer documentation. |
| cad-to-data | 349 | Converts CAD and BIM files to structured data, extracting element data from Revit, IFC, DWG and DGN. |
| dwg-to-excel | 321 | Turns AutoCAD DWG files from 1983 onward into Excel databases through the DwgExporter CLI, including layers and blocks. |
| drawing-analyzer | 276 | Extracts dimensions, annotations, symbols and metadata from construction drawings, supporting quantity work. |
| permit-tracking-automation | 248 | Tracks permit applications, renewal deadlines and status changes across a project. |
| cost-estimation-resource | 204 | Resource-based cost estimation from work items, physical resources and rates. |
| bim-qto | 193 | Extracts quantities from BIM and CAD data grouped by type, level and zone, then produces QTO reports. |
| ifc-data-extraction | 181 | Parses IFC models with IfcOpenShell into structured data for downstream analysis. |
| bim-clash-detection | 165 | Detects geometric clashes and identifies MEP, structural and architectural conflicts. |
| ifc-qto-extraction | 164 | Quantity takeoff from IFC and Revit models using DDC converters, returning element counts and properties. |
| bim-consistency-checker | 162 | Checks naming conventions, parameter completeness and spatial relationships across a model. |
| estimate-builder | 153 | Builds detailed project estimates with labour, materials and equipment breakdowns. |

The remaining 8 indexed listings range from 136 to 148 installs: `ifc-to-excel` (148), `gantt-chart` (146), `pandas-construction-analysis` (143), `cwicr-takeoff-helper` (138), `pdf-to-structured` (137), `batch-cad-converter` (137), `excel-to-bim` (137) and `xlsx-construction` (136).

The shape of the table is the shape of the workflow. Conversion and extraction come first in volume, estimation and takeoff in the middle, and the paperwork skills sit at the edges. `warranty-tracker` at 1,000 installs is more than twice the next skill and has nothing to do with BIM: it is the one skill in the indexed slice that needs no model and no Python dependency, which is a reasonable explanation for its lead.

## Why This Matters for Hermes Agents

Construction data work is a sequence of format conversions, and each conversion is where an agent invents a shortcut. A quantity takeoff built from a spreadsheet someone exported by hand is not the same number as one built from the model, and the difference is invisible in the output. These skills force the model to be the source: the IFC or RVT file goes in, structured data comes out, and the estimate is built from that.

The second value is domain vocabulary. A general-purpose agent asked to check a BIM model will produce something plausible and wrong, because it does not know that quantities are grouped by level and zone, that waste factors apply to takeoff, or that a clash report has to distinguish MEP from structural conflicts. Each of those is a skill here.

For a Hermes operator the practical use is narrow and real. If your business touches construction, property development or facilities, this is the only agent toolkit in the catalog that speaks the format of the files you actually hold. If it does not, nothing here transfers.

The caveat is dependency weight. `ifcopenshell` and the DDC exporter CLIs are substantial, and a session that fails on a missing dependency looks like a session that fails on the model.

## Usage

| You say | What happens |
|---|---|
| "Pull the quantities out of this IFC file" | IFC extraction parses the model with IfcOpenShell and returns elements with their properties, ready for a takeoff |
| "Build a cost estimate from this model" | Quantities come from the model first, then resource-based estimation prices them, then the estimate builder assembles labour, materials and equipment |
| "Convert this DWG to something Excel can read" | The DWG exporter CLI produces a workbook with layers and blocks preserved rather than a flattened table |
| "Why is this model failing validation?" | The consistency checker reports naming, parameter and spatial-relationship problems, which is usually why a downstream takeoff is short |
| "Find the clashes before the coordination meeting" | Clash detection reports geometric conflicts by discipline so the list is actionable rather than a count |
| "Track the warranty dates on this handover package" | Warranty tracking builds a register with expiration dates and manufacturer documentation per item |
| "Turn these PDF specifications into a table" | PDF to structured extracts schedules and specifications into rows an agent can query |

## Verification

Each listing resolves to a raw `SKILL.md` in its category tree. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/datadrivenconstruction/ddc_skills_for_ai_agents_in_construction/main/1_DDC_Toolkit/Closeout/warranty-tracker/SKILL.md | head -5
```

It should open with quoted frontmatter holding `name: "warranty-tracker"` and a description about tracking construction warranties, plus a `homepage` pointing at the vendor site, then the instruction body. Paths are not uniform: the same category holds skills at different depths, so confirm the path from the tree rather than assuming a layout.

After an install, confirm the skill landed as a directory holding `SKILL.md`, and confirm the Python side independently:

```bash
test -f ~/.claude/skills/warranty-tracker/SKILL.md && echo skill ok
python3 -c "import ifcopenshell, pandas, openpyxl; print('deps ok')"
```

If the second command fails, the IFC skills will run and produce nothing useful, which is a worse failure than an import error.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-10) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| warranty-tracker | Pass | Pass | Pass |
| cad-to-data | Pass | Pass | Pass |
| dwg-to-excel | Pass | Warn | Pass |
| drawing-analyzer | Pass | Pass | Pass |
| permit-tracking-automation | Pass | Pass | Pass |
| cost-estimation-resource | Pass | Pass | Pass |
| bim-qto | Pass | Pass | Pass |
| ifc-data-extraction | Pass | Pass | Pass |
| bim-clash-detection | Pass | Pass | Pass |
| ifc-qto-extraction | Pass | Warn | Pass |
| bim-consistency-checker | Pass | Pass | Pass |
| estimate-builder | Pass | Pass | Pass |
| ifc-to-excel | Pass | Warn | Pass |
| gantt-chart | Pass | Pass | Pass |
| pandas-construction-analysis | Pass | Pass | Pass |
| cwicr-takeoff-helper | Pass | Pass | Pass |
| pdf-to-structured | Pass | Pass | Pass |
| batch-cad-converter | Pass | Warn | Pass |
| excel-to-bim | Pass | Warn | Pass |
| xlsx-construction | Pass | Pass | Pass |

Agent Trust Hub and Snyk pass all 20 sampled listings. Socket warns on five, and all five are converter or model-write skills: `dwg-to-excel`, `ifc-qto-extraction`, `ifc-to-excel`, `batch-cad-converter` and `excel-to-bim`. That is a coherent pattern rather than noise, since those are the skills that shell out to external binaries and touch files.

The property the scanners do not score is `excel-to-bim`. It pushes spreadsheet data back into a model, which means an agent can overwrite parameters in a file that is the deliverable. Keep it out of any session that does not start from a copy, and diff the model after the run.

Commercial terms are the second consideration. The skill files are MIT, but the cost database, the exporter CLIs and the visualisation tool are separate products with their own licensing, and nothing in the skills licence grants you the data.

## Limitations

- Snapshot data, verified 2026-11-10: 4,538 combined installs across 20 indexed listings; 402 GitHub stars; MIT license; last pushed 2026-10-19. Counts drift over time.
- The skills.sh source page renders 20 listings, while the root README counts 238 skills and the tree carries 238 `SKILL.md` files. A wider search of the skills.sh index associates 55 listings with this source, so the 20 rendered rows are a slice rather than the collection.
- The source page reports a larger total install figure than the sum of the rendered rows, which is consistent with the 20-listing cap rather than with any single skill being uncounted.
- The README cites 221 skills in the repository description and 238 in the badges and body. Both numbers are the vendor's own, and the tree supports 238.
- `ifcopenshell` and the DDC exporter CLIs are hard dependencies for the conversion skills. Without them the skills still load and still describe a workflow, which is the failure mode that wastes the most time.
- Format support is versioned by the vendor's tools. DWG files are documented from 1983 onward and IFC from 2x3 to 4x3, but a newer schema than the bundled exporter understands will fail late, after the file has been read.

## Related

- [Metabase Skills - BI and Dashboard Agent Suite](/hermes/skills/catalog/metabase-skills-setup)
- [Excel Automation Skills](/hermes/skills/catalog/claude-office/excel-automation)
- [Ziniao Skills - ERP and Store Automation Setup](/hermes/skills/catalog/ziniao-open-skills-setup)

## Pro Tips

- Run the dependency check before the model. A missing `ifcopenshell` produces a confident narrative about a model the agent never parsed.
- Start with `cad-to-data` or `ifc-data-extraction` even if the task is estimation. Every other number in the suite comes from that extraction, and skipping it means the estimate has no traceable source.
- Give the agent one model per session. These skills hold file paths and intermediate quantities in context, and two projects in one session is how quantities get mixed.
- Keep `excel-to-bim` behind a copy. It is the one skill in the indexed set that writes back into the source model.
- Use `bim-consistency-checker` before a takeoff, not after. A model with incomplete parameters produces a takeoff that is short by an amount nobody can see in the output.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
