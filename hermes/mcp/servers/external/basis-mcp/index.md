---
title: "Basis MCP - The Excel Engine an Agent Can Audit"
description: "Hosted MCP that turns an .xlsx into a typed cell graph, re-runs every formula against Excel's cached values and names the hard-coded plug."
category: "Business Operations / Spreadsheets"
stars: n/a (pre-GA, free during early access, no billing yet)
added: "2026-11-06"
source: "chatmcp/mcpso issue #6864 (Submit Remote MCP Server: Basis); the hosted endpoint at api.basis1.tech/mcp answering a keyless initialize and tools/list; the vendor references at basis1.tech/llms.txt and api.basis1.tech/llms-full.txt; and a keyless tools/call answering 401 unauthorized"
relevance: ★★★★
tags: [excel, xlsx, xlsm, spreadsheets, financial-models, audit, formula-evaluation, dependency-graph, workbook-diff, mcp, remote, stdio]
last_updated: "2026-11-06"
---

# Basis MCP

**Every spreadsheet question an operator asks has the same hidden assumption in it: that the number on screen is the number the formula produces.** Most tools that read Excel break that assumption quietly. They read the values Excel cached the last time a human pressed save, so a workbook whose inputs changed in another system still reports last week's answer, and nothing in the response says so. Basis is built around the opposite claim: it re-runs the computation and tells you where the file and reality disagree.

```
Server type:    Remote, Streamable HTTP (hosted), plus a stdio package
Endpoint:       https://api.basis1.tech/mcp
Auth:           API key as a Bearer token, self-serve from the account
                settings; no OAuth sign-in and no key to paste from a browser
Stdio option:   npx -y @basis1/mcp with BASIS_API_KEY in the environment
Protocol:       2025-06-18
Server info:    basis-mcp 0.0.1
Tools:          25, each annotated read-only or write
Reads:          .xlsx and .xlsm
Pricing:        free during early access, no billing yet
Limits:         1,000 requests, 2 GB uploaded and 50,000,000 cells returned
                per key per calendar month (UTC)
Status:         pre-GA, no SLA, jobs held in memory with a 15-minute TTL
```

**Evidence tier: documented, with the schema read live.** The endpoint answers a keyless `initialize` with HTTP **200** as `basis-mcp` **0.0.1** and a keyless `tools/list` returns all **25** tools with their annotations and input schemas, so the surface below is the server's own contract rather than a marketing page. What was not done is a driven session: `tools/call` without a key answers `401 {"error":{"code":"unauthorized","message":"missing or invalid bearer token"}}`, and no key exists on this machine. The behaviour of the parse records, the audit and the session model is read from the vendor's machine-readable references at `basis1.tech/llms.txt` and `api.basis1.tech/llms-full.txt`, which are written for agents and agree with the schemas the server actually serves.

## What the server is

Three surfaces over one parser: an HTTP stream that returns newline-delimited JSON, an asynchronous job route for files too large to wait on, and this MCP server on top of both. An `.xlsx` goes in and a typed record stream comes out, one JSON object per line, in a fixed emission order:

| Record | What it carries |
| --- | --- |
| `workbook_meta` | Sheet count, core properties (creator, last modified by, created, title), defined names with their targets, whether a name is broken, and data tables with their row and column inputs |
| `sheet` | Sheet header and dimensions, including hidden sheets, which is where the inputs a model depends on usually live |
| `cell` | One record per cell: value, formula, number format, error state, and the kind (`formula_number`, `formula_text` and the rest) |
| `edge` | The formula dependency edge list, one row per reference from one cell to another |
| `image` and `image_summary` | Embedded pictures with their cell anchors, described for a vision model |
| `audit` | The findings: matched formulas, divergences by coordinate, plugs, broken references, circularity |

There is no OCR and no screenshotting anywhere in the path, which is the whole point: the formula text arrives as text, and the numbers arrive as numbers.

## The audit is the product

The verification pass is what separates this from a parser. Basis recomputes every formula and compares it against the value Excel itself cached in the file, then reports the divergence by coordinate. On the vendor's own public corpora that measurement reads **97.31%** of the **3,344** FUSE `.xlsx` workbooks under 1 MB recomputing with zero mismatches, over **4,033,846** formulas compared, which is an honest number rather than a flattering one, because the remaining 2.7% are exactly the files where the cache and the math had drifted.

The other finding is the one a reviewer of a financial model would make by hand. A hard-coded plug is a constant typed over a formula in an otherwise uniform fill-down, and the vendor states it is found by bytecode-program identity rather than by heuristic, so a cell that legitimately breaks the pattern is not reported as a mistake:

- **43.2%** of substantial models (**1,000** formulas or more) across the Enron spreadsheets and the FUSE corpus from Common Crawl contain at least one hard-coded plug, **29.9%** in the FUSE half and **43.2%** in the Enron half, over **4,207** formula-bearing workbooks.
- **Broken references**: `#REF!` cells and every dependent that inherited the error.
- **Circularity**: cycle membership, and whether the workbook's own iterative-calculation setting sanctions it, which is the difference between a bug and a deliberate design.
- **Staleness**: volatile functions and links to workbooks that are not present on the machine.

Read that 43.2% as an argument about the market rather than about Basis. If nearly half of substantial public models carry a plug someone typed to make a number tie, an agent answering a question off a workbook without checking is guessing with a straight face.

## The tools, by what they are allowed to do

The annotation map is unusually clean for a write surface, and it is worth reading before connecting the server to anything that can act:

| Read-only | What it does |
| --- | --- |
| `parse_workbook` | Parse a whole file in one call into NDJSON; 20 MB cap, public `https` URL or base64, optional HMAC-signed webhook |
| `stream_job` | Read a parse job started by `submit_job`, or check its status only |
| `diff_workbooks` | Compare two workbooks |
| `evaluate_formula` | Evaluate a formula |
| `get_outputs` | Read outputs from a session |
| `inspect_model` | Inspect the model |
| `trace_dependencies` | Follow what a cell depends on and what depends on it |
| `audit_workbook` | Run the audit |
| `recalc_workbook` | Recalculate a workbook and return it with computed values |
| `export_workbook` | Get the workbook back as `.xlsx` |
| `get_formula_range` | Read a range of formulas |
| `list_sessions`, `list_library_files` | Enumerate state |

| Write | Note |
| --- | --- |
| `submit_job` | Starts an async parse; each call counts against the parse quota |
| `create_session`, `add_sheet`, `rename_sheet`, `set_calc_settings`, `commit_session`, `save_to_library` | Session-scoped edits |
| `set_inputs`, `define_variable`, `delete_variable` | Marked **destructive** |
| `close_session`, `restore_session` | Marked **destructive** |

The session is the pattern to notice: open a workbook as a session, change inputs, recalculate, read the outputs, then commit. A what-if question ("what does this model say if freight goes up eight percent") becomes a real recalculation rather than a language model's estimate of one, and the file is not touched until commit. Destructive annotations on `set_inputs` and `restore_session` are the honest kind: they do change a workbook.

## Limits, stated by the vendor

The quota is per key per calendar month: **1,000** requests, **2 GB** of uploaded bytes and **50,000,000** cells returned. A request over a limit gets **402** `quota_exceeded` naming the dimension that ran out, with `X-Basis-Quota-Dimension`, `-Limit`, `-Used` and `-Reset` headers. Jobs live in memory with a **15-minute** TTL, so a stalled workflow restarts rather than resumes. There is no formal SLA and no contractual uptime, which the vendor says plainly instead of implying otherwise, and the service is pre-GA, meaning the pricing is free now and will change.

Two limits are implied by the surface rather than stated as a rule. `.xls`, `.xlsb` and `.ods` are not read by the browser app, and the API converts them server-side, so a legacy file is a conversion step rather than a parse. And a `.xlsm` is read for its cells and formulas; nothing in the published material claims the macro project is executed or inspected, so treat VBA as outside the surface.

## Can an agent change a workbook's inputs?

Yes, and it is the most useful thing on the server. `create_session` opens a workbook, `set_inputs` and `define_variable` change values, `recalc_workbook` recomputes, `get_outputs` reads the answers, and `commit_session` writes the result back or `close_session` throws it away. Three of those calls carry `destructiveHint: true` because they do change a workbook, so the annotation is the signal to put a human in front of the commit rather than after it.

## What does the audit catch that a formula check does not?

The two findings a passing recomputation hides. A workbook can recompute perfectly and still be wrong, because the cached value and the formula agree with each other while the formula is a constant typed over the fill-down, which is the plug, or while the cell references a workbook nobody has, which is the staleness. Basis reports match and divergence counts together, so a model that is 99.95% verified is also told which 0.05% diverged and why.

## Connecting it

Hosted, with the key in a header:

```json
{
  "mcpServers": {
    "basis": {
      "url": "https://api.basis1.tech/mcp",
      "headers": { "Authorization": "Bearer ${BASIS_API_KEY}" }
    }
  }
}
```

Or locally over stdio, which is the easier route for a laptop that already has Node:

```bash
npx -y @basis1/mcp
```

with `BASIS_API_KEY` exported. Keys are self-serve from the account settings, and the browser app opens workbooks without an account if the point is to look at the audit before wiring anything up.

## Why it earns a guide

Because the spreadsheet is the one business system this catalog can read but could not check. The neighbours all stop short in the same place: **InvoiceParser Pro** turns a PDF invoice into rows in a sheet, **Azquo** keeps an audited store where every figure traces back to a source file and a user, **SyncWith** pumps third-party data into Sheets, and the BI readers query a warehouse. None of them answers what a formula in a workbook computes, which cells feed it, or whether the cached number still equals the math.

That is the question an operator asks when a board pack, a valuation, a budget or a lender's model arrives from somebody else. Today the answer is a human opening the file, pressing F9, and eyeballing for the cell that does not follow the pattern. That work now has a tool surface, and the audit findings are the reason to use it rather than the parsing.
