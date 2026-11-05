---
title: "Claude Office Skills - XLSX, DOCX and PPTX Setup"
description: "tfriedel/claude-office-skills on skills.sh: 7.0K combined installs across 4 listings; XLSX, DOCX, PPTX and PDF workflows for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tfriedel-claude-office-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "office documents", "xlsx", "pptx"]
---

# Claude Office Skills - Setup Guide

**Source:** [tfriedel/claude-office-skills](https://www.skills.sh/tfriedel/claude-office-skills) via skills.sh - 7.0K combined installs across 4 indexed listings; first seen 2026-11-05 (Nov 5, 2026 morning sweep)
**GitHub:** 849 stars, no LICENSE file, last pushed 2026-04-01, 4 SKILL.md directories under public/
**Category:** Office document workflows for agents: spreadsheet, word processor, presentation and PDF production
**Quality Tier:** 🟡 Beta - no LICENSE file in the repository plus Socket and Trust Hub Warns on xlsx; 849 stars.

This repository packages the Office document skills that Claude desktop uses for command line agents. Four formats, one directory each: `xlsx` for spreadsheets and financial models, `docx` for Word documents with tracked changes and OOXML edits, `pptx` for presentations including an HTML-to-PPTX path, and `pdf` for forms, merges, extraction and conversion. Each directory holds a SKILL.md that defines the workflow plus the scripts the workflow calls.

The README carries a 2026-04-01 update saying the repo was published before Anthropic made these skills public, and pointing readers at the official `anthropics/skills` tree for maintained copies. That note matters more than the install counts: this is a snapshot of a workflow Anthropic now publishes itself.

## Installation

The README documents no cross-agent installer command. It documents the dependency step and then running the workflows in place:

```bash
venv/bin/pip install -r requirements.txt
```

```bash
npm install
```

Node dependencies are needed for the `html2pptx` path. The README also assumes LibreOffice (`soffice`), Poppler (`pdftoppm`) and Pandoc are present on the host, described as usually pre-installed.

The four workflows are then loaded from `public/docx`, `public/pdf`, `public/pptx` and `public/xlsx`, and the README's Claude Code section describes the loop it expects: check whether a skill exists for the task, read the relevant SKILL.md, execute the workflow step by step, run the OOXML validation scripts, and write everything to `outputs/<document-name>/`.

The README's manual commands are repository-relative, so an install that moves a SKILL.md away from its sibling `scripts/` directory breaks the workflow. Keep `public/<format>/` intact when copying the skill into an agent's skills directory. The listings are indexed on skills.sh at the URL in the Source line above, but with no CLI line in the README, confirm the command your installer proposes rather than assuming one.

## What It Provides

All four listings are above the threshold.

| Skill | Installs | Use For |
|---|---|---|
| xlsx | 2,539 | Building financial models with working formulas, colour-coded inputs, number formats and zero formula errors |
| docx | 1,801 | Tracked-changes redlining, comments, OOXML structure edits and text extraction that keeps the changes |
| pptx | 1,740 | HTML-to-PPTX conversion, template slide rearrangement, text replacement from JSON and thumbnail validation |
| pdf | 922 | Filling forms, merging documents, extracting data, and converting PPTX to PDF or PDF to images |

No indexed listings fall below the 500-install threshold; all 4 appear above.

## Why This Matters for Hermes Agents

Asked for a deck or a model, a coding agent will usually write python-pptx or openpyxl from scratch and produce something that opens but is wrong in ways nobody checks: a broken formula reference, a table that overflows its slide, a tracked change silently rewritten as a flat edit. These skills encode the output conventions instead. The `xlsx` workflow requires every delivered model to carry zero formula errors, names the specific failures it means (#REF!, #DIV/0!, #VALUE!, #N/A, #NAME?), and fixes a colour convention that separates hardcoded inputs from formulas, internal links, external links and flagged assumptions.

The `pptx` workflow adds a step that generation usually skips: render a thumbnail grid and inspect it for text cutoff and layout breakage before calling the deck done. The `docx` workflow edits through tracked changes and OOXML rather than rewriting the file, which is what preserves a human review step in a contract or a handbook.

For a Hermes agent the practical gain is determinism. The work runs as named scripts with saved intermediates in `outputs/<document-name>/`, so a failed run leaves a rebuildable directory rather than a half-written binary. That makes batch jobs, monthly report generation and document pipelines reasonable things to hand to an agent.

## Usage

| You say | What happens |
|---|---|
| "Build a five-year budget model with scenarios" | xlsx creates the workbook with formulas, colour-coded inputs and number formats, then checks for formula errors |
| "Add tracked changes and comments to this contract" | docx unpacks the OOXML, applies tracked edits and writes the document back |
| "Turn these speaker notes into a 10 slide deck" | pptx builds slides from the notes, then validates layout with a thumbnail grid |
| "Restyle this deck from our HTML template" | pptx renders the HTML/CSS design to PPTX with formatting preserved |
| "Fill in this PDF form from the JSON" | pdf populates the fillable fields and writes the completed file |
| "Convert the deck to images for review" | pdf converts PPTX to PDF and PDF to images for a visual pass |
| "Merge these twelve PDFs into one appendix" | pdf combines the documents in order |

## Verification

Confirm the raw workflow file an agent will read:

```bash
curl -fsSL https://raw.githubusercontent.com/tfriedel/claude-office-skills/main/public/pptx/SKILL.md | head -6
```

It should open with `name: pptx` and a description naming presentation creation, editing, layouts and speaker notes. The spreadsheet workflow carries the stricter output rules:

```bash
curl -fsSL https://raw.githubusercontent.com/tfriedel/claude-office-skills/main/public/xlsx/SKILL.md | head -8
```

It should reach the zero formula errors requirement within the first screen. From a clone, confirm the four directories and that the scripts run:

```bash
ls public
venv/bin/python public/pptx/scripts/thumbnail.py template.pptx outputs/review/thumbnails
```

`ls public` should print docx, pdf, pptx and xlsx, and the thumbnail command should write a review grid to the output path.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| xlsx | Warn | Warn | Pass |
| docx | Pass | Pass | Warn |

There is no LICENSE file in the repository. The README's Attribution section states that most scripts and workflows come directly from Claude, included verbatim, and offers to comply if Anthropic asks for removal. Treat the code as source-available rather than as a standard permissive licence until terms are clear.

## Limitations

- Snapshot data, verified 2026-11-05: 7,002 combined installs across 4 indexed listings; 849 GitHub stars; no LICENSE file; last pushed 2026-04-01. Counts drift over time.
- No licence grant. The repository has no LICENSE file despite 849 stars, so redistribution and commercial use are unresolved on the face of the repo.
- The README itself, updated 2026-04-01, recommends `anthropics/skills` for maintained versions of the same skills because this repo predates their public release. Expect drift and prefer upstream for new work.
- Installation is manual. There is no cross-agent install command in the README, only Python and Node dependencies plus the format workflows to load.
- Host dependencies are real: LibreOffice, Poppler, Pandoc, a Python virtualenv and Node for the HTML-to-PPTX path. A slim container will fail partway through a workflow rather than at install time.
- Outputs land in `outputs/<document-name>/`, which the README marks gitignored. In CI that path has to exist and be writable, and the agent needs permission to create directories.

## Related

- [PowerPoint - Create, Read, Edit .pptx Decks Setup](/hermes/skills/catalog/powerpoint-setup)
- [Adobe Skills - PDF, Document and Creative Suite Setup](/hermes/skills/catalog/adobe-skills-setup)
- [JEO Skills - Presentation and Document Suite](/hermes/skills/catalog/jeo-skills-setup)

## Pro Tips

- Run the thumbnail check on every deck, including the ones that look fine. Text cutoff is the failure that survives a text extraction check and shows up in the room.
- Keep a template directory outside `outputs/`. The workflows edit a copy, and pointing them at an already-edited deck compounds formatting drift.
- Pin LibreOffice and Pandoc versions in CI. The README treats them as usually pre-installed, which is true on a laptop and rarely true in a container.
- For anything long-lived, port the SKILL.md rules you rely on into your own skill and keep this repo as the reference. The rules are plain prose and survive the move.
- Do not run `xlsx` against a template with an established colour scheme. Its own guidance says existing template conventions override the built-in standards, so check which side won before shipping the model.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
