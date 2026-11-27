---
title: "Claude Office Skills Suite - Business Document Skills"
description: "claude-office-skills/skills: 577.3K combined installs. Ninety-six curated Claude Skills for office documents, automation and PDF workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-office-skills-suite-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "office", "documents", "automation"]
---

# Claude Office Skills Suite - Setup Guide

**Source:** [claude-office-skills/skills](https://www.skills.sh/claude-office-skills/skills) via skills.sh - 577.3K combined installs across 96 indexed listings; first documented 2026-11-27 (morning sweep)

**GitHub:** [claude-office-skills/skills](https://github.com/claude-office-skills/skills) - 597 stars, MIT, branch main, last pushed 2026-01-31; every skill is a directory at the repo root with its own SKILL.md, alongside five pre-built agent personas in `agents/`, the `mcp-servers/office-mcp/` TypeScript server, Anthropic's document guides in `official-skills/`, and a `_shared/knowledge/` layer.

**Category:** Office and business document skills, PDF tooling, and workflow automation for Claude and agent runtimes

**Quality Tier:** 🟡 Yellow - Snyk warns on four sampled listings while Socket and the Gen Agent Trust Hub pass.

Claude Office Skills is a community collection that packages real-world office work as Claude Skills: contracts, invoices, proposals, resumes, reports, presentations, emails, data analysis and document processing. The README positions it as zero-setup, copy-and-paste skills that carry embedded domain knowledge and professional workflows, with an optional Office MCP server adding 39 tools for Word, Excel, PowerPoint, PDF and OCR.

The index tracks 96 listings, and the heaviest are document-facing: html-slides (20,068), excel-automation (16,483), ppt-visual (13,123), pdf-extraction (9,678) and smart-ocr (8,993). Each skill is one directory at the repo root, so installing a single skill is a copy of one folder. The README also documents an install script, a knowledge base, and five pre-built agent personas that bundle curated skill sets.

## Installation

The README documents several routes. For Claude Code, place the skill in the skills directory and start Claude:

```bash
mkdir -p ~/.config/claude-code/skills/
cp -r contract-review ~/.config/claude-code/skills/
claude
```

A single skill can also be loaded by direct link without any install:

```
Please use this skill: https://raw.githubusercontent.com/claude-office-skills/skills/main/contract-review/SKILL.md
```

The Moltbot (Clawdbot) route installs all skills in one command:

```bash
curl -fsSL https://raw.githubusercontent.com/claude-office-skills/skills/main/install.sh | bash
```

The installer accepts a category argument such as `--category legal`, `--category pdf` or `--category workflow`; the README lists twelve categories (legal, hr, finance, pdf, workflow, template, doc, conversion, parsing, slide, productivity, marketing). The manual route is a clone followed by the same copy step:

```bash
git clone https://github.com/claude-office-skills/skills.git
cp -r claude-office-skills/skills/contract-review ~/.config/claude-code/skills/
```

Copy the whole directory, not only the SKILL.md, because several skills carry a README next to the SKILL.md and the knowledge layer lives in `_shared/knowledge/`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| html-slides | 20,068 | HTML-based slide decks; the README maps it to reveal.js. |
| excel-automation | 16,483 | Advanced Excel automation with Python, mapped to xlwings in the README. |
| ppt-visual | 13,123 | Presentation visuals and slide layouts: visual concepts, graphics and design specifications for PowerPoint. |
| pdf-extraction | 9,678 | Extract text, tables and metadata from PDFs using pdfplumber. |
| smart-ocr | 8,993 | OCR across 100+ languages, mapped to PaddleOCR in the README. |
| data-analysis | 8,464 | Analyze spreadsheet data, generate insights, build visualizations and reports from Excel/CSV. |
| tiktok-marketing | 7,328 | TikTok content strategy, video creation workflows, posting optimization and analytics, built on n8n templates. |
| stock-analysis | 7,272 | Stock analysis with fundamental and technical methods across US, China A-shares and Hong Kong markets. |
| office-mcp | 7,177 | MCP server with 39 tools for Word, Excel, PowerPoint, PDF and OCR operations. |
| xlsx-manipulation | 7,025 | Create, edit and manipulate Excel spreadsheets programmatically with openpyxl. |
| whatsapp-automation | 6,851 | WhatsApp Business automation: support, notifications, chatbots and broadcast messaging. |
| telegram-bot | 6,676 | Telegram bot development: chatbots, notifications, AI assistants and group automation. |
| google-ads-manager | 6,620 | Google Ads campaign management: setup, keyword research, bid optimization and performance reporting. |
| airtable-automation | 6,456 | Airtable database automation: views, automations, integrations and workflow triggers. |
| docx-manipulation | 6,450 | Create, edit and manipulate Word documents programmatically with python-docx. |
| cv-builder | 6,407 | YAML to PDF resume generation, mapped to rendercv in the README. |
| calendar-automation | 6,406 | Google Calendar and Outlook automation: scheduling, meeting workflows, time blocking, Slack/Sheets integration. |
| academic-search | 6,378 | Search and analyze academic literature: find papers, understand methodologies, synthesize findings. |
| pdf-to-docx | 6,285 | Convert PDF files to editable Word documents with pdf2docx. |
| chart-designer | 6,268 | Design charts and visualizations for ECharts, Chart.js and other libraries; dashboards and reports. |
| proposal-writer | 6,235 | Create compelling business proposals that win deals and partnerships. |

The remaining 52 indexed listings range from 4,960 to 5,977 installs.

The index also carries space-named listings the table cannot render, including Asana Automation (7,164) and PDF OCR Extraction (6,067), both above the table cut-off but not renderable there, plus File Organizer (5,730), Twilio SMS Automation (5,615) and 19 more.

## Why This Matters for Hermes Agents

The value here is breadth with a consistent shape: one directory, one SKILL.md, one task. An agent that holds contract-review, invoice-generator and proposal-writer can cover a negotiation workflow without any plugin, because each skill is plain Markdown with a YAML header and instructions, not a package with dependencies. That is the cheapest class of capability to install, audit and keep in context.

The README's copy-and-paste model matters for portability. The same SKILL.md text works in Claude.ai by pasting, in Claude Code by copying the directory, and over the API by loading the file into the system prompt, so a skill is not locked to one runtime. For builders, that means a skill you review once can be reused across every agent surface without a rewrite.

The document library choices are the other signal. The README maps each core skill to a known Python library (python-docx, openpyxl, xlwings, pdfplumber, pdf2docx, PaddleOCR, reveal.js), so the skill tells the agent exactly which tool to reach for rather than leaving it to guess. The official-skills/ directory goes further and mirrors Anthropic's own DOCX, XLSX, PPTX and PDF guidance under a source-available license.

For a Hermes-style setup, the one caution is scale. The index tracks 96 listings and the repo carries more than 130 skill directories, so installing everything pulls a large, overlapping surface. The heavy install counts concentrate in a handful of document skills, which is where an agent gets the most leverage for the least context cost.

## Usage

| You say | What happens |
|---|---|
| "Review this contract for risks" | Loads contract-review, which reads the document and returns risk findings, completeness checks and recommendations. |
| "Turn this CSV into a chart" | Uses data-analysis or chart-designer to generate chart configurations for ECharts, Chart.js and similar libraries. |
| "Generate an invoice from this order" | Loads invoice-generator to produce a properly formatted invoice. |
| "Convert this PDF to an editable Word file" | Uses pdf-to-docx, which drives pdf2docx to produce an editable document. |
| "Pull the text out of this scanned PDF" | Uses smart-ocr (PaddleOCR) to OCR the scan, or pdf-extraction for text and table extraction. |
| "Build a resume from this YAML" | Loads cv-builder, which renders a PDF resume from YAML via rendercv. |
| "Draft a proposal for this deal" | Uses proposal-writer to write a business proposal tailored to the opportunity. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/claude-office-skills/skills/main/html-slides/SKILL.md
```

After a clone, confirm the skill directory carries its SKILL.md and that the layout matches the README's one-directory-per-skill claim:

```bash
git clone --depth 1 https://github.com/claude-office-skills/skills.git /tmp/office-skills
ls /tmp/office-skills/html-slides/SKILL.md
ls /tmp/office-skills/agents/ | wc -l
head -3 /tmp/office-skills/contract-review/SKILL.md
```

The first ls should print the SKILL.md path, the agents count should print 5, and head should show the contract-review frontmatter. On the installed copy, confirm the skill sits in the skills directory:

```bash
ls ~/.config/claude-code/skills/contract-review
```

If the directory is empty, the copy step was run on the SKILL.md alone rather than the whole folder.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| html-slides | Pass | Pass | Pass |
| excel-automation | Pass | Pass | Pass |
| ppt-visual | Pass | Pass | Pass |
| pdf-extraction | Pass | Pass | Pass |
| smart-ocr | Pass | Pass | Pass |
| data-analysis | Pass | Pass | Warn |
| tiktok-marketing | Pass | Pass | Pass |
| stock-analysis | Pass | Pass | Pass |
| office-mcp | Pass | Pass | Pass |
| Asana Automation | not parsed | not parsed | not parsed |
| xlsx-manipulation | Pass | Pass | Pass |
| whatsapp-automation | Pass | Pass | Warn |
| telegram-bot | Pass | Pass | Warn |
| google-ads-manager | Pass | Pass | Pass |
| airtable-automation | Pass | Pass | Pass |
| docx-manipulation | Pass | Pass | Pass |
| cv-builder | Pass | Pass | Pass |
| calendar-automation | Pass | Pass | Warn |
| academic-search | Pass | Pass | Pass |
| pdf-to-docx | Pass | Pass | Pass |
| chart-designer | Pass | Pass | Pass |
| proposal-writer | Pass | Pass | Pass |
| PDF OCR Extraction | not parsed | not parsed | not parsed |
| office-to-md | Pass | Pass | Pass |

This guide is Yellow because Snyk warns on four sampled listings (data-analysis, whatsapp-automation, telegram-bot and calendar-automation); Socket and the Gen Agent Trust Hub pass every sampled listing. Two space-named listings (Asana Automation and PDF OCR Extraction) could not be parsed by the scanners, so they carry no verdict. The bulk of the repository is Markdown plus one TypeScript MCP server under `mcp-servers/office-mcp/`, which is the part to review before running, since it executes locally when the MCP server is started.

## Limitations

- Snapshot data, verified 2026-11-27: 577,292 combined installs across 96 indexed listings; 597 GitHub stars; MIT; last pushed 2026-01-31. Counts drift over time.
- The install index outruns the tree in two directions: 23 listings carry space-named titles the guide table cannot render, and the repo holds more than 130 skill directories while only 96 names appear in the index.
- The repository has not been pushed since 2026-01-31, so the README's feature notes (the MCP server, knowledge base and agents) may lag the skills.sh install counts.
- The README states the repository is MIT but also notes that individual skills may carry different licenses; official-skills/ guides are source-available, so check a skill's own folder before redistributing.
- Some skills wrap third-party services (Google Ads, WhatsApp, Telegram, Airtable) and will need credentials or API access that the SKILL.md alone does not provide.
- The Moltbot install script and the Office MCP server are the only executable surfaces; everything else is Markdown read at load time.

## Related

- [Claude Office Skills - XLSX, DOCX and PPTX Setup](/hermes/skills/catalog/tfriedel-claude-office-skills-setup)
- [Anthropic Claude API Skills - Model Reference Setup](/hermes/skills/catalog/anthropics-claude-api-skills-setup)
- [OpenAI Skills - Official Agent Skills Library Setup](/hermes/skills/catalog/openai-skills-setup)
- [Hermes Agent Skill Authoring - Official SKILL.md Writing Guide](/hermes/skills/catalog/hermes-agent-skill-authoring-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the handful of document skills you actually use (html-slides, excel-automation, ppt-visual, pdf-extraction) rather than the full 130-directory surface; the context cost of one SKILL.md each is far lower than the whole tree.
- Copy whole directories, never a bare SKILL.md, because the knowledge layer and per-skill README files sit beside the instructions.
- Treat the Office MCP server separately from the skills: the skills are inert Markdown, but the MCP server is a Node process that runs locally, so review `mcp-servers/office-mcp/` before starting it.
- For agent-to-agent reuse, load the SKILL.md into the system prompt the way the README's API example does; the same text works without any runtime-specific packaging.
- The five agent personas under `agents/` are a ready-made model for bundling skills into a role, worth reading before you build your own.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
