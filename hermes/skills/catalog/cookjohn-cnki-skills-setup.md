---
title: "CNKI Skills - Academic Search, Download & Zotero Setup"
description: "cookjohn/cnki-skills: CNKI skills for Claude Code - search, browse journals, download PDFs and export to Zotero - 6.3K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cookjohn-cnki-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-22"
tags: ["hermes skill", "agent skill", "skill setup", "cnki", "academic search", "zotero"]
---

# CNKI Skills - Academic Search, Download & Zotero Setup

**Source:** [cookjohn/cnki-skills](https://www.skills.sh/cookjohn/cnki-skills) via skills.sh - 6.3K combined installs across 10 indexed listings; first seen Nov 22, 2026 (Nov 22, 2026 morning sweep)
**GitHub:** [cookjohn/cnki-skills](https://github.com/cookjohn/cnki-skills) - 1,092 stars, no LICENSE file, master branch, last pushed Mar 13, 2026; ten skill directories under `skills/<name>/SKILL.md` plus an `agents/cnki-researcher.md` agent that coordinates the whole suite.
**Category:** Academic Search and Citation Management
**Quality Tier:** 🟡 Yellow - 1,092 stars but no LICENSE file and an eight-month-stale repository (last pushed Mar 13, 2026); the 10 sampled skills carry no Fail cells, with Snyk Warns across the whole sample.

CNKI (China National Knowledge Infrastructure) is China's largest academic database, indexing journals, theses, conference papers and patents. This repository is a Claude Code skills suite that drives CNKI through the Chrome DevTools MCP: it runs JavaScript directly in a Chrome tab to search papers, browse journal issues, check journal indexing status, download PDF and CAJ files and export citations to Zotero, with no screenshot parsing or OCR. The README is bilingual English and Chinese; the English install block is reproduced below.

The ten skills split the workflow into small, single-purpose steps: keyword search, advanced filtered search, result parsing, pagination, paper detail extraction, journal lookup, journal indexing checks, table-of-contents browsing, download and Zotero export. A single `cnki-researcher` agent coordinates all ten and handles captcha detection, tab management and multi-step flows such as search, then filter, then export to Zotero.

## Installation

Prerequisites are the Claude Code CLI, a Chrome browser (login is handled manually for downloads), and optionally the Zotero desktop app and Python 3 for the Zotero push script.

1. Register the Chrome DevTools MCP server:

```bash
claude mcp add chrome-devtools \
-- npx -y chrome-devtools-mcp@latest
```

2. Clone the repository and copy the skills and agent into `.claude/`:

```bash
git clone https://github.com/cookjohn/cnki-skills.git
cd cnki-skills
cp -r skills/ agents/ .claude/
```

Or add to an existing project:

```bash
git clone https://github.com/cookjohn/cnki-skills.git /tmp/cnki-skills
cp -r /tmp/cnki-skills/skills/ your-project/.claude/skills/
cp -r /tmp/cnki-skills/agents/ your-project/.claude/agents/
```

3. Start Chrome with remote debugging enabled:

```bash
# Windows
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222

# macOS
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

# Linux
google-chrome --remote-debugging-port=9222
```

4. Launch Claude Code:

```bash
claude
```

The skills and agent are picked up automatically; try `/cnki-search machine learning` to verify.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| cnki-search | 1,203 | keyword search on CNKI with structured result extraction |
| cnki-download | 796 | download a paper PDF or CAJ file from CNKI (requires login) |
| cnki-advanced-search | 783 | filtered search by author, title, journal, date range or source category (SCI/EI/CSSCI/Peking University Core) |
| cnki-paper-detail | 696 | extract full paper metadata: title, authors, affiliations, abstract, keywords, fund, classification |
| cnki-journal-search | 611 | find journals by name, ISSN, CN number or sponsor |
| cnki-journal-index | 565 | check which databases include a journal (Peking University Core, CSSCI, CSCD, SCI, EI), impact factors and evaluation data |
| cnki-export | 450 | push a paper to Zotero or save citation data as a RIS file |
| cnki-parse-results | 420 | parse the current search results page into structured paper data |
| cnki-navigate-pages | 366 | move between search result pages and change sort order |
| cnki-journal-toc | 364 | browse a journal issue's table of contents or download the TOC PDF |

All 10 indexed listings clear the 50-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

CNKI is the reference source for Chinese-language academic literature, and most of its content sits behind a login and institutional access, which makes it hard for an agent to reach through a plain HTTP client. This suite routes around that by driving a real Chrome tab through the Chrome DevTools MCP, running `evaluate_script` calls that read the page state directly instead of parsing screenshots or OCR, so the agent gets structured paper data in one or two tool calls per operation. The single-async-script design and direct navigation over link clicking are both worth copying: they sidestep the tab-management and timing flakiness that plagues snapshot-based browser agents. The captcha-aware `cnki-researcher` agent is the standout piece, because it detects the Tencent slider captcha and pauses for a human rather than silently failing mid-download. For an agent that needs to gather, cite and file Chinese-language papers, the download and Zotero export pair closes the loop from discovery to a usable citation library. The caveats are the missing license and the stale repository, plus the institutional login CNKI itself requires.

## Usage

| You say | What happens |
|---|---|
| Search CNKI for papers on machine translation | Runs a keyword search and returns structured paper results |
| Find CSSCI papers on a topic from 2020 to 2025 | Runs an advanced search filtered by source category and date range |
| Download this paper | Fetches the paper's PDF or CAJ file (requires you to be logged in to CNKI) |
| Save this paper to Zotero | Pushes the paper to Zotero or writes a RIS citation file |
| Is this journal in CSSCI? | Reports the journal's indexing status, impact factors and evaluation data |
| Show the 2025 issue 1 table of contents | Browses the journal issue and fetches the original TOC PDF |
| Go to the next page of results | Moves between search result pages or changes the sort order |

## Verification

Confirm the skills landed under `.claude/skills/` and the agent under `.claude/agents/`, then review a skill's SKILL.md before relying on it:

```bash
curl -sL https://raw.githubusercontent.com/cookjohn/cnki-skills/master/skills/cnki-search/SKILL.md | head -40
```

Inspect the advanced search and download skills:

```bash
curl -sL https://raw.githubusercontent.com/cookjohn/cnki-skills/master/skills/cnki-advanced-search/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/cookjohn/cnki-skills/master/skills/cnki-download/SKILL.md | head -40
```

Review the Zotero export skill and its push script before wiring up a citation library:

```bash
curl -sL https://raw.githubusercontent.com/cookjohn/cnki-skills/master/skills/cnki-export/SKILL.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Nov 22, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| cnki-search | Pass | Pass | Warn |
| cnki-download | Pass | Pass | Warn |
| cnki-advanced-search | Pass | Pass | Warn |
| cnki-paper-detail | Pass | Pass | Warn |
| cnki-journal-search | Warn | Pass | Warn |
| cnki-journal-index | Pass | Pass | Warn |
| cnki-export | Pass | Warn | Warn |
| cnki-parse-results | Pass | Pass | Warn |
| cnki-navigate-pages | Pass | Pass | Warn |
| cnki-journal-toc | Pass | Pass | Warn |

None of the ten sampled skills carries a Fail cell, but every one carries a Snyk Warn and the repository ships no LICENSE file, so review the SKILL.md files and re-check the security pages on skills.sh before relying on the suite in production.

## Limitations

- Snapshot data, verified Nov 22, 2026: 6.3K combined installs across 10 indexed listings; 1,092 GitHub stars; no LICENSE file; last pushed Mar 13, 2026. Counts drift over time.
- No LICENSE file at the repository root, though the README's License section says MIT; treat redistribution and modification rights as unclear.
- Access to CNKI content normally requires an institutional subscription, and downloads require you to be logged in to CNKI manually.
- The repository is eight months stale (last pushed Mar 13, 2026), so the skills may lag CNKI's current site layout.
- Snyk flags every sampled skill with a Warn and cnki-export also carries a Socket Warn; these are scanner-flagged, not confirmed vulnerabilities.

## Related

- [arXiv - Academic Paper Search Setup Guide](/hermes/skills/catalog/arxiv-setup)
- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)
- [Claude Scholar - Research Pipeline for Agents](/hermes/skills/catalog/claude-scholar-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read each SKILL.md before relying on it; the repository has no LICENSE file and is eight months stale.
- Keep Chrome's remote-debugging port fixed at 9222 and log in to CNKI manually once so downloads and exports reuse your session.
- Install Zotero and use the export skill to close the loop from search to a citation library instead of hand-building RIS files.
- Prefer the advanced search skill for filtered queries (author, journal, date range, source category) over broad keyword searches that return noisy pages.
- Use the `cnki-researcher` agent for multi-step flows like search then export; it pauses on the Tencent slider captcha instead of failing mid-download.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
