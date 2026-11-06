---
title: "WPS Skills - Office Automation via MCP Tools"
description: "lc2panda/wps-skills on skills.sh: 5.9K combined installs across 4 listings; control WPS Office Excel, Word and PPT through 243 MCP tools."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/wps-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "wps office", "document automation", "mcp"]
---

# WPS Skills - Setup Guide

**Source:** [lc2panda/wps-skills](https://www.skills.sh/lc2panda/wps-skills) via skills.sh - 5.9K combined installs across 4 indexed listings; first seen 2026-11-05 (Nov 5, 2026 evening sweep, first documentation)
**GitHub:** 685 stars, MIT, last pushed 2026-06-30, four SKILL.md directories under `skills/` plus a TypeScript MCP server in `wps-office-mcp/`
**Category:** Document automation for agents: WPS Office Excel, Word and PPT control through 243 MCP tools
**Quality Tier:** 🟡 Caution - Snyk reports Warn on the wps-excel audit, the one non-Pass verdict in the sample of four; MIT, 685 stars.

WPS Skills is an MCP server plus a skills layer. The README describes it as a framework that lets an AI assistant drive WPS Office, the office suite popular in China, from natural language, and it targets Claude Code, Cursor and Augment by name. It covers Excel, Word and PowerPoint, runs on macOS, Windows and Linux, and needs WPS Office installed before any of it works.

The numbers come straight from the README: 231 registered MCP tools plus 12 built-in tools, which is 243 in total. The split is Excel 82, Word 28, PPT 112 and 9 general tools, and the wps-office SKILL.md repeats the same 231 figure as a sum of the four parts. The built-in dozen cover connection checks, a universal method call and a data cache.

The architecture is three layers. A skills layer of natural language guidance, an MCP server layer, and an execution layer that differs per platform: a `wps-claude-assistant` helper with 227 actions driven by HTTP polling on macOS, and `wps-com.ps1` with 231 actions over the COM interface on Windows. A WPS add-on sits on the other end and is what actually touches open documents.

## Installation

The README installs from a clone. Prerequisites are WPS Office, Node.js 18.0.0 or newer, and Git.

```bash
git clone https://github.com/lc2panda/wps-skills.git
cd wps-skills
```

Then build the MCP server:

```bash
cd wps-office-mcp
npm install
npm run build
cd ..
```

Register the server with your client. For Claude Code the README writes this block to `~/.claude/settings.json`, with the path replaced by the real absolute path:

```json
{
  "mcpServers": {
    "wps-office": {
      "command": "node",
      "args": ["/your/path/wps-skills/wps-office-mcp/dist/index.js"]
    }
  }
}
```

Cursor takes the same block in `.cursor/mcp.json` at the project root, and Codex takes a TOML equivalent under `[mcp_servers.wps-office]` in `~/.codex/config.toml`. The README also shows a command-line registration through `codex mcp add`, passing the server name `wps-office` and then the `node` command with the absolute path to `dist/index.js`.

The add-on install is a human step, because an agent cannot operate the WPS application itself. Run the script for your platform, then restart WPS Office before anything works:

```bash
# macOS
bash scripts/auto-install-mac.sh

# Windows (PowerShell)
powershell scripts/install.ps1

# Linux
bash scripts/install.sh
```

Claude Code also needs the four skills linked into its skills directory:

```bash
mkdir -p ~/.claude/skills
ln -sf "$(pwd)/skills/wps-excel" ~/.claude/skills/wps-excel
ln -sf "$(pwd)/skills/wps-word" ~/.claude/skills/wps-word
ln -sf "$(pwd)/skills/wps-ppt" ~/.claude/skills/wps-ppt
ln -sf "$(pwd)/skills/wps-office" ~/.claude/skills/wps-office
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| wps-office | 2,114 | Cross-application work: connection checks, switching between apps, moving data from Excel into Word, batch conversion and template application |
| wps-excel | 1,435 | Excel by natural language: formulas, data cleaning, charts, pivot tables, worksheets, formatting, rows and columns, comments and protection |
| wps-word | 1,307 | Word documents: content editing, layout and formatting, headers and footers, comments, template filling and paragraph structure |
| wps-ppt | 1,060 | Presentation work: slides, shapes, images, tables, layout beautification, animation, charts, 3D and data visualisation |

No indexed listings fall below the 500-install threshold; all 4 appear above.

## Why This Matters for Hermes Agents

Office files are the part of an agent's output that a human still opens by hand. A model can write a CSV in one call, but writing an .xlsx with a working pivot table, or a deck that survives a review meeting, usually ends in a manual pass. Driving the real application removes that pass, because the file is produced by the same engine the reviewer will open it in.

The tool split is what makes it tractable. 82 Excel tools, 112 PPT tools and 28 Word tools means the agent picks a document-shaped capability rather than a generic file writer, and the wps-office skill exists to coordinate the cases that span two applications, such as moving Excel data into a Word table or batch converting formats across a folder.

Cross-platform coverage is the other practical gain. The execution layer differs between macOS and Windows, but the MCP surface above it does not, so the same tool call means the same thing on either machine.

The caveat is that this is desktop automation, not a document library. Something has to be running on the machine, the add-on has to be installed, and WPS has to be open with the right document type loaded. Agents that treat it as a headless converter will collect null returns.

## Usage

| You say | What happens |
|---|---|
| "Build a month-end summary sheet from this CSV" | wps-excel writes formulas, formats the sheet and adds a chart through the MCP tools |
| "Clean this data and drop duplicate rows" | Excel data tools run against the open workbook |
| "Make this deck look presentable" | wps-ppt applies layout and beautification, then adds animation or charts |
| "Reformat this report to house style" | wps-word applies paragraph structure, fonts, headers and footers |
| "Move this table into a Word document" | wps-office coordinates the cross-app copy and keeps formatting consistent |
| "Convert every doc file in this folder" | wps-office batch conversion across the folder |
| "Is the add-on connected?" | wps-office connection check across all three applications |

## Verification

Start the server directly and read the log line the README asks for:

```bash
node wps-office-mcp/dist/index.js
```

It should print `MCP Server started successfully`. That string is emitted by the server at startup, so a clean build is confirmed before a client is involved. Then check the registration and the skill links:

```bash
claude mcp list | grep -i wps
ls ~/.claude/skills/wps-excel/SKILL.md
```

The first command should show the `wps-office` server, the second should resolve. If the tools return null, the README's troubleshooting row for that symptom points at one cause first: no document of the matching type is open in WPS.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| wps-office | Pass | Pass | Pass |
| wps-excel | Pass | Pass | Warn |
| wps-word | Pass | Pass | Pass |
| wps-ppt | Pass | Pass | Pass |

The trust question here is not the markdown, it is the local server. `npm install` pulls a dependency tree that includes the MCP SDK, the add-on scripts modify your WPS installation, and the server then holds the ability to read and write every open document. Install from a clone you have read, run the add-on scripts with your own eyes on them, and treat the server as a local automation daemon rather than a sandbox. The README states the server is a standard stdio implementation against spec 2025-11-25, so no network listener is involved.

## Limitations

- Snapshot data, verified 2026-11-05: 5,916 combined installs across 4 indexed listings; 685 GitHub stars; MIT; last pushed 2026-06-30. Counts drift over time.
- The README is written in Chinese. Every fact in this guide is a translation of it or of the repository's own SKILL.md files; the install commands are reproduced verbatim.
- The README gives two different tool totals in the same document: 243 in the project section (231 plus 12 built-in) and 239 in the architecture diagram. The skills layer repeats 231 as 82 plus 28 plus 112 plus 9, so treat 243 as the current figure.
- The add-on install cannot be automated by an agent, and WPS Office must be restarted afterwards. This is desktop automation with a mandatory human step.
- The skills.sh listings carry the four SKILL.md files, but the MCP server lives in `wps-office-mcp/` and is built from the clone. An index-only install gives the agent instructions for tools that are not present.
- `package.json` still points its repository field at `github.com/laowang/wps-skills`, not the lc2panda path. Harmless today, but a sign the project moved between accounts.
- Last push was 2026-06-30, so the tree has been static for months. Check the add-on scripts against your WPS version before relying on them.

## Related

- [Claude Office Skills - XLSX, DOCX and PPTX Setup](/hermes/skills/catalog/tfriedel-claude-office-skills-setup)
- [powerpoint - Setup Guide - CorpusIQ Docs](/hermes/skills/catalog/powerpoint-setup)
- [Markdown Viewer Skills - Diagrams, Charts and Cards Setup](/hermes/skills/catalog/markdown-viewer-skills-setup)

## Pro Tips

- Open the document before asking. The README's null-return row names a missing or wrong-type open document as the first cause to rule out.
- Use wps-office for anything that crosses applications. The three app skills are scoped, and the cross-app skill is the one that knows how to move content between them.
- Keep the absolute path in the MCP config. A relative path works until the client launches from a different working directory.
- Restart WPS after every add-on change, not just the first time. The add-on is loaded into the running application.
- Prefer this for files a human will open, and a library for files a machine will read. Desktop automation costs a running application; a document library does not.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
