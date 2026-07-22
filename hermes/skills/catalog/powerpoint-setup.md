---
title: "powerpoint — Setup Guide"
description: "Create, read, and edit .pptx decks, slides, notes, and templates. Official Hermes skill. 393+ installs on skills.sh."
---

# powerpoint

**Source:** `nousresearch/hermes-agent` (official Hermes bundled skill)  
**Installs:** 393+ on skills.sh  
**Category:** Productivity / Office  
**Skill ID:** `powerpoint`

## Overview

Create, read, and edit PowerPoint decks from scratch or via template-based XML manipulation. Supports speaker notes, charts, design QA, and LibreOffice rendering. A `.pptx` is a ZIP archive of XML files — this skill gives you complete control over every element.

## Installation

```bash
npx skills add nousresearch/hermes-agent@powerpoint -a hermes-agent -y
```

### Prerequisites

```bash
# Node.js dependency
npm install pptxgenjs

# Python dependencies
pip install "markitdown[pptx]" Pillow defusedxml lxml

# System dependencies (Linux)
sudo apt install -y libreoffice poppler-utils

# macOS
brew install libreoffice poppler
```

## Quick Reference

| Task | Approach |
|---|---|
| **Create** a new deck | Write a `pptxgenjs` script |
| **Edit** an existing deck or template | unzip → edit `ppt/slides/slideN.xml` → zip |
| **Read** content | `markitdown deck.pptx` (one block per slide) |
| **Visual QA** | `python scripts/thumbnail.py deck.pptx` |
| **Validate** | `python scripts/office/validate.py deck.pptx` |

## Creating Decks with pptxgenjs — Key Gotchas

- **Set `pres.layout` before adding slides.** Default canvas is `LAYOUT_16x9` = 10" × 5.625", not 13.3" wide.
- **Hex colors: never `#`, never 8 digits.** Use `color: "FF0000"` — both `"#FF0000"` and alpha hex values corrupt the file.
- **pptxgenjs mutates option objects** — never share one `shadow`/options object across two `add*` calls.
- **Shadow `offset` must be ≥ 0** — negative offset corrupts the file. Use `angle` to cast direction.
- **`letterSpacing` is silently ignored** — use `charSpacing` instead.
- **Lists:** `bullet: true` on each item; never a literal `•` (renders double bullets).
- **One `new pptxgen()` per output file** — never reuse an instance.
- **Text boxes have built-in padding** — set `margin: 0` when aligning with shapes at same x.
- **Speaker notes:** `slide.addNotes("...")` (plain text, once per slide).
- **Keep charts native** — use `addChart()` for everything PowerPoint can chart. Only render images for chart types PowerPoint has no native form for (Sankey, network, chord).
- **On stacked bar/column charts, `dataLabelPosition` must be `ctr`, `inEnd`, or `inBase`.** `outEnd` corrupts the file.
- **Always run `validate.py` after generation** — catches chart faults and XML defects.

## Editing Existing Decks and Templates

Pick layouts first with thumbnail grid:

```bash
python scripts/thumbnail.py template.pptx template-thumbs
```

Then extract, edit, and repack:

```bash
# Unpack
python3 -c "import sys,zipfile; zipfile.ZipFile(sys.argv[1]).extractall('unpacked')" deck.pptx

# Duplicate a slide
python scripts/add_slide.py unpacked/ slide2.xml --after slide2.xml

# Edit content in ppt/slides/slideN.xml

# Repack (from inside unpacked/)
(cd unpacked && rm -f ../out.pptx && zip -Xr ../out.pptx .)

# Validate
python scripts/office/validate.py out.pptx --original deck.pptx
```

**Important rules:**
- Do all structural work (add, delete, reorder) before editing slide content
- Never copy a slide file by hand — use `add_slide.py`
- If using `python-pptx`: assign `run.text` not `text_frame.text` (preserves formatting)
- `.potx` templates unpack and pack identically — keep `.potx` extension on output
- Legacy `.ppt` must be converted first: `soffice --headless --convert-to pptx file.ppt`

## Design Guidelines

The skill includes comprehensive design guidance for creating professional presentations:

### Color Palettes

| Theme | Primary | Secondary | Accent |
|-------|---------|-----------|--------|
| **Midnight Executive** | `1E2761` navy | `CADCFC` ice blue | `FFFFFF` white |
| **Forest & Moss** | `2C5F2D` forest | `97BC62` moss | `F5F5F5` cream |
| **Coral Energy** | `F96167` coral | `F9E795` gold | `2F3C7E` navy |
| **Warm Terracotta** | `B85042` terracotta | `E7E8D1` sand | `A7BEAE` sage |
| **Ocean Gradient** | `065A82` deep blue | `1C7293` teal | `21295C` midnight |
| **Charcoal Minimal** | `36454F` charcoal | `F2F2F2` off-white | `212121` black |
| **Teal Trust** | `028090` teal | `00A896` seafoam | `02C39A` mint |
| **Berry & Cream** | `6D2E46` berry | `A26769` dusty rose | `ECE2D0` cream |
| **Sage Calm** | `84B59F` sage | `69A297` eucalyptus | `50808E` slate |
| **Cherry Bold** | `990011` cherry | `FCF6F5` off-white | `2F3C7E` navy |

### Slide Design Rules
- Every slide needs a visual element — image, chart, icon, or shape. Text-only slides are forgettable.
- Pick a bold, content-informed color palette. Dominance over equality: one color should dominate 60-70%.
- Dark/light contrast: dark backgrounds for title + conclusion slides, light for content ("sandwich" structure).
- Commit to a visual motif — one distinctive element repeated across all slides.

### Layout Options
- Two-column (text left, illustration right)
- Icon + text rows (icon in colored circle, bold header, description below)
- 2×2 or 2×3 grid (image on one side, grid of content blocks on other)
- Half-bleed image (full left or right side) with content overlay
- Large stat callouts (big numbers 60-72pt with small labels)
- Comparison columns (before/after, pros/cons)
- Timeline or process flow (numbered steps, arrows)

## Scripts

All paths relative to the skill directory:

| Script | Purpose |
|---|---|
| `scripts/thumbnail.py deck.pptx [prefix]` | Labeled grid of every slide for visual reference |
| `scripts/add_slide.py unpacked/ slide.xml [--after slideN.xml]` | Duplicate a slide with package bookkeeping |
| `scripts/clean.py unpacked/` | Delete orphaned slides, media, rels |
| `scripts/office/validate.py deck.pptx [--original src.pptx]` | Schema, relationship, content-type checks |
| `scripts/office/soffice.py --headless --convert-to pdf deck.pptx` | LibreOffice PDF conversion |

## Related Skills

- **`docx`** — Word document creation and editing
- **`xlsx`** — Excel spreadsheet creation and editing
- **`pdf`** — PDF manipulation
- **`pptx-author`** (optional finance skill) — Finance-specific presentation generation
- **`popular-web-designs`** — Design systems and color palettes for web UIs (complementary)

## Verification

```bash
# Check installation
hermes skills inspect powerpoint

# Test thumbnail generation
python ~/.hermes/skills/powerpoint/scripts/thumbnail.py test.pptx

# Validate a deck
python ~/.hermes/skills/powerpoint/scripts/office/validate.py deck.pptx
```

## Notes

- Official Hermes bundled skill adapted from Anthropic's original by Nous Research
- License: Proprietary (see LICENSE.txt in skill directory for complete terms)
- Supports both from-scratch generation (pptxgenjs) and template-based editing (XML manipulation)
- LibreOffice required for rendering/QA (headless mode supported)
- See skill's SKILL.md for the complete gotchas reference — 20+ common pitfalls documented
