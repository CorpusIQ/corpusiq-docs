---
title: printing-press-library — Setup Guide
description: Library of print-ready document templates (reports, proposals, invoices, certificates) via mvanhorn/printing-press-library — 679 installs.
---

# printing-press-library — Setup Guide

**Source:** [mvanhorn/printing-press-library](https://github.com/mvanhorn/printing-press-library)
**Skill:** `printing-press-library`
**Installs:** 679
**Quality Tier:** 🔵 Community

A comprehensive library of print-ready document templates for Hermes agents. Generate professional reports, proposals, invoices, certificates, and branded documents from JSON data — all with production-quality typography and layout.

## Installation

```bash
npx skills add https://github.com/mvanhorn/printing-press-library --skill printing-press-library
```

After install, reload skills:
- Hermes CLI: `/reload-skills` or restart session
- Hermes gateway: `/restart` or `hermes gateway restart`

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.16.0+ |
| wkhtmltopdf (optional) | For PDF rendering: `apt install wkhtmltopdf` |
| Puppeteer (optional) | Alternative PDF engine: `npm install puppeteer` |

## Capabilities

| Capability | Trigger | Output |
|-----------|---------|--------|
| Business report | "Generate a quarterly growth report" | Formatted PDF report |
| Invoice | "Create an invoice for $500" | Professional invoice PDF |
| Proposal | "Draft a client proposal" | Branded proposal document |
| Certificate | "Generate a completion certificate" | Printable certificate |
| Letterhead | "Create letterhead from company data" | Branded letter template |
| Contract | "Generate a service agreement" | Formatted contract document |

## Template Library

| Template | Use Case | Format |
|----------|----------|--------|
| `report` | Quarterly/annual business reports | Multi-page with TOC |
| `invoice` | Client billing with line items | Single page, totals |
| `proposal` | Project/service proposals | Cover + sections |
| `certificate` | Achievement/completion awards | Decorative border |
| `letterhead` | Official correspondence | Header + footer |
| `contract` | Service agreements, NDAs | Legal formatting |

## Quick Start

```python
# Template-based generation
from printing_press import Document

doc = Document(template="report")
doc.set_title("Q3 2026 Growth Report")
doc.add_section("Executive Summary", content="...")
doc.add_chart(data=growth_data, chart_type="line")
doc.add_section("Metrics", content="...")
doc.render("q3-2026-growth-report.pdf")
```

## CorpusIQ Use Cases

1. **Client reports** — Automated monthly growth reports for CorpusIQ clients
2. **Invoices** — Programmatic billing documents from Stripe data
3. **Partner proposals** — Branded partnership proposals for BD outreach
4. **Internal reports** — Executive summaries for founder review
5. **Certificates** — Beta user completion certificates for community program
6. **Legal documents** — NDAs and service agreements for enterprise deals

## Troubleshooting

| Issue | Likely Cause | Resolution |
|-------|-------------|------------|
| PDF blank | Missing wkhtmltopdf | Install wkhtmltopdf 0.12.6+ |
| Fonts missing | System lacks fonts | `apt install fonts-dejavu fonts-liberation` |
| Charts not rendering | Missing charting dep | Check chart library installation |
| Layout broken | Custom CSS conflict | Use default template CSS as base |

## Verification

After installation, verify the skill is loaded:
```bash
hermes skills list | grep printing-press-library
```

Test with a document request:
```
"Generate a one-page invoice for CorpusIQ consulting services at $1,500"
```
