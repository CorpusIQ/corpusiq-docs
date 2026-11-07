---
title: "SumOffice MCP - Edit the Real xlsm and Get It Back"
description: "Opens your own docx or xlsx, reads formulas, VBA modules and Power Query, then returns an edited copy with the macros byte-identical."
category: Productivity
stars: n/a (free, no account and no key; the vendor's own paid products are the desktop apps)
added: 2026-11-07
source: "The chatmcp/mcpso submission #6890 (SumOffice, com.sumoffice/office, named 2026-11-07T09:19:17Z); the official MCP registry record com.sumoffice/office at sumoffice.com with the Docker image hissih/sumoffice-mcp 0.3.1 for linux/amd64 and arm64 and the repo github.com/SumOfficeApp/sumoffice-mcp; the vendor page sumoffice.com/mcp.html (formats, limits, the 20 September 2026 proof run); and a live driven session on https://view.sumoffice.com/mcp where initialize answered 200 as sumoffice-document 0.3.0, tools/list returned 21 tools, and the cashflow demo .xlsm was opened, inspected, read and queried"
relevance: ★★★★
tags: [documents, excel, word, xlsm, vba, macros, power-query, docx, pdf-export, approval, mcp, streamable-http, docker, stdio]
last_updated: "2026-11-07"
---

# SumOffice MCP

**An agent that cannot open the actual file is reduced to describing what the file probably says.** Convert the spreadsheet to CSV and the formulas are gone. Screenshot the page and the macros are gone. Ask a model to produce a "new version" and the revision marks, the styles and the VBA project come back invented. SumOffice takes the file itself: it opens your .xlsx, .xlsm or .docx in a private editor cabin for the session, reads it the way an editor reads it - cells and formulas, VBA entry points with their blockers, Power Query steps and load targets, paragraphs, comments and tracked changes - proposes a change, applies it only after you say yes, and hands back a copy that Word and Excel open without a repair dialog.

```
Server type:  Remote, Streamable HTTP, or the same server as a local Docker
              image over stdio (hissih/sumoffice-mcp 0.3.1, amd64 and arm64)
Endpoint:     https://view.sumoffice.com/mcp
Registry:     com.sumoffice/office
Auth:         none. No account and no key
Formats:      .docx .doc .odt .xlsx .xlsm .xlsb .xls .ods, up to 50 MB
Tools:        21 over MCP
Cost:         free
```

**Evidence tier: driven, read path only.** A keyless `initialize` answered **200** as `sumoffice-document` **0.3.0** on protocol **2025-06-18** and `tools/list` returned **21** tools. The demo workbook `cashflow` then opened and was read: a real `.xlsm` with three sheets (`Cash flow` A1:I33, `Bank export` A1:F61, `Monthly from bank` A1:F13), `workbook_inspect` reporting `vba_project: true`, `vba_signature: false`, two tables, one query table, one connection, `data_mashup: true` and zero external links. The write path was attempted twice and refused twice, with the reasons recorded below, so this entry does not claim a driven write.

## What it read out of one workbook

The demo is a Northwind Tools cash-flow model whose own note in A2 says the actuals arrive from a bank export through the query `MonthlyCashflow`, three assumptions sit in I5:I7, and a macro marks the months where cash runs out. Every one of those claims is machine-readable through a different tool, which is the point:

| Question | Tool | What came back |
|---|---|---|
| What is in this file, structurally? | `workbook_inspect` | Sheets with used ranges, a package map (VBA project present, no signature, 2 tables, 1 query table, data mashup present) and the application model in one call |
| What are the vintages, formulas, values? | `sheet_read`, `sheet_find`, `sheet_describe` | Values **and** formulas side by side: `D28` carries `=B28-C28` with its computed `-57,200`, `E28` carries `=E27+D28` with `6,700`, read through a rectangular window under a 60-row, 26-column cap |
| Can this file run code? | `macro_list`, `macro_read_source`, `macro_plan` | `Module1.FlagCashGaps` is a public sub, user-runnable, route **native**, no blockers. `Sheet1.Worksheet_Change` is private, route **excel-bridge**, blocked as an event-or-document module at line 12. Nothing was executed to learn this |
| Where does the data come from? | `query_list`, `query_explain` | `MonthlyCashflow` loads to a Table, background refresh on, connection refreshed to version 6, and the M body is **withheld by engine policy** with only its `sha256` exposed |
| What did a human change here? | `document_comments` | Comments with author, text, anchor and resolved state, plus tracked changes, up to 50 |

That last row of the query table is the most interesting behaviour in the product. The Power Query M expression is the thing that decides which server the actuals come from and which credentials ride with them, and the engine exposes a hash instead of the source. An agent can reason about the query's shape, its load target and its refresh state, and cannot read the connection string out of it.

## The 20 September proof, and why it is the entry

The vendor published a run of this exact public server, from a laptop over HTTPS, not a lab build. An agent opened an Enron-corpus workbook with a VBA project and a dynamic-array UDF, read A1:F12, proposed `H2 = SUM(B2:B5)` plus a label in H1, applied, and saved a copy. Microsoft Excel 16 opened the copy with no repair dialog, `xl/vbaProject.bin` in the copy was **byte-identical** to the original, and H2 held both the formula and its computed value. The document run replaced paragraph 1, applied, saved a copy and rendered a PDF, and Word 16 showed the new text with `styles.xml` and every other package part unchanged.

Byte-identical VBA is the hard part and it is the reason this belongs in the catalog. Macro workbooks are where document tooling normally gives up: re-save through a library that does not model the VBA project and the project is either dropped or silently altered, and the operator finds out when the file will not open on the finance machine. A copy you can trust to still be the same workbook is what makes it safe to let an agent touch it at all.

## What it refuses, measured

The refusals are the design, and they showed up in this session rather than in a limitations section:

- **A value edit was refused at the preview.** `sheet_propose_edits` with plain numbers in I5:I7 returned `unsupported-cell-preview-edits ... preview_cell_edits accepts a non-empty formatting, formula, or drag-fill edit batch`. The tool description offers numbers and text; the preview engine as configured on the hosted demo accepted neither on this pass. Treat value writes as unverified here and lead with formula edits.
- **Then the capacity ceiling answered.** The next three attempts returned `busy: all 5 editor cabins are in use`, which is the documented concurrency limit of the hosted server, hit after a handful of sessions from one client. There is no close-cabin tool in the 21, so cabins free themselves on expiry rather than on request.
- **A document demo did not open.** `document_open` with the `offer` slug and every `document_*` call answered `This feature does not work in the browser yet (sumdoc-shell:get-state)` while the sheet demos worked, so the hosted browser path is ahead of the document path as of this pass.
- **Argument names are strict and the errors are specific.** `sheet_find` wants `query`, not `text` (`-32602`). `sheet_read` on a three-sheet workbook refuses without the sheet name and lists the choices.
- **By the vendor's own statement** it will not write into your original (every change stays in the cabin and returns as a copy), will not run macros or refresh queries in this version (it reads and plans them), and refuses a stale proposal or an edit outside the previewed window rather than best-efforting it.

## Operational facts an operator should hold

- **One file per session, five concurrent sessions per server, sessions expire after 10 minutes of silence.** The hosted server runs in Frankfurt.
- **Files are deleted.** The vendor states the opened file and every copy or PDF are deleted after 24 hours and that nothing in the file is executed. That is a vendor statement about their own service, not something an outside test can confirm.
- **Edits are narrow on purpose.** Up to **20 cells** of values or formulas in a rectangular window, or the full new text of **one paragraph** with its formatting kept.
- **The document comes back as a 24-hour download link**, and the macro workbook comes back as `.xlsm` with the VBA project untouched.
- **A local option exists** for teams that cannot send files out: the same server as a Docker image, with `document_open_file` taking a path under a mounted folder. The vendor is explicit that the file still opens in a cabin on their infrastructure in that mode, and offers an on-premise conversation separately.

## Where it sits against the rest of this catalog

The document entries here generate: template-to-DOCX and PDF, native .pptx on a company's own slide masters, invoice and proposal builders. Those start from data and produce a file. This starts from the file the business already runs on and returns it changed, which is the only shape that works for a model with macros in it. On the spreadsheet side the catalog now carries **[Basis MCP](/hermes/mcp/servers/external/basis-mcp/)**, catalogued the evening before this entry, and the split between them is clean: Basis turns an .xlsx into a typed cell graph, recomputes every formula against Excel's cached values and reports the divergences and the plugs, while SumOffice opens the same kind of file, reads its package including the VBA project and the Power Query connections, and ships the edited artifact back with those parts intact. An operator who wants to know whether the numbers are right wants the first; an operator who wants the file updated without breaking it wants the second. The older spreadsheet class here, carried by **SheetsFinance** and held for `workbook-tools-mcp`, builds a model from vendor statement data, which is a third job again.

## Connect

```json
{
  "mcpServers": {
    "sumoffice": {
      "url": "https://view.sumoffice.com/mcp"
    }
  }
}
```

Claude Code takes `claude mcp add --transport http sumoffice https://view.sumoffice.com/mcp`. For a local file, run the Docker image with the folder mounted and call `document_open_file` with the path under it.
