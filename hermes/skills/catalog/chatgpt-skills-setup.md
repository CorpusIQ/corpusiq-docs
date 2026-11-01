---
title: "ChatGPT Skills - 12-Suite Deterministic Toolkit"
description: "dkyazzentwatwa/chatgpt-skills: 16.7K combined installs. Twelve consolidated suites with bundled Python scripts for OCR, documents, media and data."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/chatgpt-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "document processing", "data analysis", "python scripts"]
---

# ChatGPT Skills - Setup Guide

**Source:** [dkyazzentwatwa/chatgpt-skills](https://www.skills.sh/dkyazzentwatwa/chatgpt-skills) via skills.sh - 16.7K combined installs across 106 indexed listings; first seen 2026-11-01 (morning sweep)

**GitHub:** [dkyazzentwatwa/chatgpt-skills](https://github.com/dkyazzentwatwa/chatgpt-skills) - 126 stars, no LICENSE at the repo root, branch main, last pushed 2026-04-08; 12 `SKILL.md` files, one per top-level directory, each with a `scripts/` folder of Python helpers and optionally `references/` and `assets/`

**Category:** Document, data, media and image processing: the deterministic utility layer under an agent's prose

**Quality Tier:** 🟡 Yellow - the three sampled skills pass all three scanners, but the repository ships no LICENSE file at its root, so the terms for reuse are unstated

This pack is a deliberate consolidation. The README describes it as a reduced, higher-signal library that now favours fewer, broader skills with real deterministic tooling over a long tail of thin utility wrappers, and says the old micro-skill catalogue was intentionally pruned. What remains is twelve suites, each one a workflow document wrapped around a set of scripts: OCR and receipt parsing, document conversion, image work, audio and video, analytics and reporting, geography, SVG, QR codes, financial maths, MCP server construction and skill authoring itself.

The house style is consistent across all twelve. A suite lists what it is for, gives a numbered workflow that names the script to run at each step, and then closes with guardrails: do not promise visual fidelity, do not present indicator output as a guarantee, say when a background removal is heuristic, route scanned PDFs to OCR rather than to the converter. For an agent operator that last section is the valuable one, because it encodes the failure modes the author already hit.

## Installation

The README documents no install command for the skills themselves. Its Core Commands section is about the repository's own tooling, not about getting the skills into an agent:

```bash
python3 skill-creator/scripts/init_skill.py my-skill --path .
python3 skill-creator/scripts/quick_validate.py my-skill
python3 audit_all_skills.py
python3 verify_docs.py
```

There is no `npx skills` line, no plugin manifest and no clone step in the README, so the route below is ours rather than the project's:

```bash
git clone --depth 1 https://github.com/dkyazzentwatwa/chatgpt-skills.git /tmp/chatgpt-skills
for d in crypto-ta-analyzer data-storyteller document-converter-suite financial-calculator \
         geo-toolkit image-enhancement-suite mcp-builder media-toolkit \
         ocr-document-processor qr-code-generator skill-creator svg-precision-skill; do
  cp -r "/tmp/chatgpt-skills/$d" ~/.hermes/profiles/corpusiq/skills/
done
```

Name the directories rather than copying the root with a wildcard. The repository also holds `public/`, `tests/`, three zipped archives and a handful of loose markdown files, none of which are skills, and a wildcard copy puts all of it where the loader will try to read it. Keep each directory's internal structure intact, because the skill bodies call their helpers by relative path such as `scripts/ocr_processor.py`.

Several suites assume third-party Python packages and, for media work, external binaries. The README's stated convention is a `requirements.txt` inside `scripts/` whenever Python scripts exist, so install per skill rather than globally and check that file first.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ocr-document-processor | 4,765 | Text and structure from scans and images: searchable PDFs, table extraction, receipts and business cards, with confidence caveats. |
| crypto-ta-analyzer | 1,587 | Multi-indicator technical analysis on OHLCV data: trend, momentum, volume and divergence, with conflicts named rather than averaged. |
| text-summarizer | 693 | No directory in the current tree; the index lists it but there is no summariser skill to install. |
| financial-calculator | 504 | Loan, investment, NPV, IRR, retirement and Monte Carlo calculations, with the assumptions that drive the answer returned alongside it. |
| document-converter-suite | 483 | PDF, Office, markdown, HTML and table conversion plus merge, split, rotate, watermark and simple form filling. |
| image-enhancement-suite | 294 | Resize, crop, compress, background removal, comparison, metadata, palettes, icons, collages and sprite sheets. |
| svg-precision-skill | 280 | Deterministic SVG built from an explicit spec, validated before handoff: icons, diagrams, charts and technical drawings. |
| qr-code-generator | 244 | Single and batch QR codes with URL validation, optional UTM parameters and print-safe SVG output. |
| data-storyteller | 230 | Dataset profiling, quality audits, statistics, pivots, experiment reads and narrative reports from CSV or spreadsheet input. |
| roi-calculator | 196 | No directory in the current tree; the same maths ships as `roi_calculator.py` inside `data-storyteller`. |
| mcp-builder | 190 | MCP server design: tool inventory tied to workflows, strict schemas, corrective errors and an evaluation pass. |
| svg-precision | 188 | No directory in the current tree; this is the same skill as `svg-precision-skill` under an older listing name. |
| stock-screener | 183 | No directory in the current tree; the index lists it but there is no screener skill to install. |
| media-toolkit | 174 | Audio and video clipping, conversion, normalisation, captions, thumbnails, GIFs and batch utilities. |
| skill-creator | 159 | Skill authoring and refactoring: scaffold, generate `agents/openai.yaml`, validate frontmatter, then package. |
| report-generator | 153 | No directory in the current tree; narrative report output belongs to `data-storyteller`. |
| citation-bibliography-generator | 147 | No directory in the current tree; the index lists it but there is no citation skill to install. |
| geo-toolkit | 130 | Address parsing, geocoding, KML and GeoJSON conversion, territory mapping, distance calculation and visualisation. |
| gantt-chart-creator | 128 | No directory in the current tree; the index lists it but there is no Gantt skill to install. |
| table-extractor | 122 | No directory in the current tree; the same capability ships as `scripts/table_extractor.py` inside `document-converter-suite`. |
| scientific-paper-figure-generator | 122 | No directory in the current tree; figure work is covered by `svg-precision-skill` rather than by a dedicated suite. |
| background-remover | 122 | No directory in the current tree; the same capability ships as `background_remover.py` inside `image-enhancement-suite`. |

The remaining 84 indexed listings range from 53 to 116 installs, and almost none of them have a directory either: the pruned micro-skills live on in the index long after the code was merged into the suites above. The index carries 106 listings against 12 directories in the tree, which is the largest index-to-tree gap in this catalogue batch.

## Why This Matters for Hermes Agents

Most of what an agent is asked to do at the edges of a project is unglamorous and deterministic: read the table out of a scanned invoice, convert a deck to markdown, cut thirty seconds of audio, compute the payment schedule rather than approximate it. A language model doing those from first principles produces plausible output with quiet errors. These skills exist so the same request routes to a script.

The consolidation is the design decision worth stealing. Twelve broad suites with real helpers inside them are easier to keep correct than a hundred thin wrappers, because each suite has one owner, one set of guardrails and one place where the scripts are described. The pruned listings in the index are the cost of that decision, and it is a cost paid in discoverability rather than in correctness.

The guardrails are the second thing worth stealing. Each suite closes by telling the agent what not to claim: no visual fidelity promises from the converter, no guaranteed outcomes from the indicator stack, no exact fields when OCR confidence is low. That is a compact way to pre-empt the most common failure of an agent given a tool, which is overclaiming what the tool returned.

Finally, `skill-creator` is the pack eating its own cooking. It is the author's own authoring pipeline, with validation that enforces frontmatter shape, directory naming, agent metadata and script dependency rules, and it is the most transferable skill here if you write skills of your own.

## Usage

| You say | What happens |
|---|---|
| "Pull the line items out of these scanned receipts" | `ocr-document-processor` routes each image through the receipt helper and returns structured fields with confidence caveats where the scan is weak. |
| "Turn this 60-page PDF into a report with a chart per section" | `document-converter-suite` converts first, then `data-storyteller` profiles the extracted data and writes the narrative with the chart specs. |
| "Which of these three coins is trending and which is just volatile" | `crypto-ta-analyzer` normalises the OHLCV data, runs the indicator stack and explains where the indicators disagree and how regime-sensitive the read is. |
| "What does a 30-year mortgage at 6.2% cost with an extra 200 a month" | `financial-calculator` computes the schedule and returns the assumptions and sensitivity that actually move the answer. |
| "Compare these two quarterly exports and flag anything odd" | `data-storyteller` runs the comparer and outlier helpers, then reports the quality problems before any conclusion. |
| "Cut the dead air out of this podcast and normalise the levels" | `media-toolkit` picks the trimmer and the normaliser rather than re-encoding the whole file. |
| "Sketch an MCP server for our billing API" | `mcp-builder` returns a workflow-shaped tool inventory, the schemas and an evaluation prompt before any code is written. |

## Verification

The raw path for the OCR suite returned HTTP 200 on branch main when this guide was written on 2026-11-01:

```bash
curl -sL -o /dev/null -w "%{http_code} ocr\n" \
  https://raw.githubusercontent.com/dkyazzentwatwa/chatgpt-skills/main/ocr-document-processor/SKILL.md
```

Expect `200`. After the clone, count the real skills rather than trusting the index, and confirm the helpers arrived:

```bash
find /tmp/chatgpt-skills -name SKILL.md | wc -l
ls /tmp/chatgpt-skills/ocr-document-processor/scripts | wc -l
head -4 /tmp/chatgpt-skills/financial-calculator/SKILL.md
```

The first count should print 12. The second should print at least three, because the OCR suite names `ocr_processor.py`, `business_card_scanner.py` and `receipt_scanner.py`. The header should show `name: financial-calculator` with a single-line `description:` before the closing frontmatter.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ocr-document-processor | Pass | Pass | Pass |
| crypto-ta-analyzer | Pass | Pass | Pass |
| text-summarizer | Pass | Pass | Pass |

One of the three sampled listings, `text-summarizer`, has no directory at all, so the sample effectively covers two skills out of twelve. That is worth stating plainly: the verdict table is weaker evidence here than it looks.

The attack surface is real, and it is larger than most packs in this catalogue. These skills bundle executable Python, they are told to write outputs to disk, and at least three of them reach the network: `crypto-ta-analyzer` ships a CoinGecko converter, `geo-toolkit` ships a geocoder, and `qr-code-generator` validates target URLs before encoding them. A script that fetches a URL and then writes files is exactly the shape a supply-chain reviewer should read line by line, and none of the scanner verdicts above substitute for that.

Two practical mitigations follow from the repository's own structure. The README states that every Python skill carries a `requirements.txt` inside its `scripts/` folder, so pin and audit those rather than installing ad hoc. And because there is no LICENSE file at the root, treat the code as all rights reserved until the author says otherwise, which matters most if you intend to redistribute a suite inside your own product.

## Limitations

- Snapshot data, verified 2026-11-01: 16,721 combined installs across 106 indexed listings; 126 GitHub stars; no LICENSE at the repo root; last pushed 2026-04-08. Counts drift over time.
- The index lists 106 skills but the tree holds 12 directories. Most of the difference is pruned micro-skills that survive as listings with no code behind them, and ten of those orphans still sit above this guide's 122-install threshold.
- Install counts include listings that cannot be installed. Three of the rows above the threshold (`text-summarizer`, `roi-calculator`, `svg-precision`) have no directory in the tree, so the index overstates what the pack can deliver.
- No licence file at the root, and a repository that bundles executable code. The scanner verdicts cover two of twelve skills, so the code review is yours to do.
- Last pushed 2026-04-08, about seven months before this snapshot. The suites call each other by directory name and by relative script path, so a partial copy breaks routing rather than failing loudly.
- The skills assume their own working directory layout and call helpers as `scripts/<name>.py`. Copying a single file out of a suite, rather than the directory, is the most common way to break one of these.

## Related

- [Claude Office Skills](/hermes/skills/catalog/claude-office)
- [PowerPoint - Create, Read, Edit .pptx Decks Setup](/hermes/skills/catalog/powerpoint-setup)
- [PDF Converter (MinerU) - PDF to Markdown Skill Setup](/hermes/skills/catalog/pdf-converter-mineru-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the twelve directories, not the repository. The root holds tests, a public folder and three zip archives, and a flat copy puts all of it in the skills path where the loader will try to read it.
- Start with `ocr-document-processor` and `document-converter-suite` together. The two skills cross-reference each other on purpose, with scanned PDFs going to OCR and digital PDFs going to the converter, and installing one without the other loses that routing rule.
- Read the guardrail section before the workflow section. It tells you what the suite will refuse to claim, which is how you decide whether the output needs a human check before it reaches a customer.
- Treat the index as a historical record, not a catalogue. Ten of the rows above 122 installs have no code, so pick from the twelve directories in the tree and use the table only to see what people searched for.
- Use `skill-creator` on anything you write yourself. Its validator is stricter than most, it enforces the two-field frontmatter that this catalogue also expects, and it will catch a mismatched folder name before a loader does.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
