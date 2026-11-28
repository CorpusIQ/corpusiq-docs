---
title: "FatturaPA MCP - Italian E-Invoices Read Locally, Eight"
description: "Reads Italian FatturaPA e-invoices (XML, .p7m, ZIP) into JSON or CSV locally, installed and driven against ten fixtures."
category: "Finance & Accounting"
stars: "0 (github.com/Agent90ia/fatturapa-converter, MIT, created 2026-11-23T21:25:56Z and pushed 2026-11-28T09:28:50Z, measured this pass)"
added: 2026-11-28
source: "queue filing chatmcp/mcpso#8287 read on 2026-11-28; cloned from source at the filing's repository, npm install in mcp/ (zod and the MCP SDK), stdio initialize 200 as fatturapa-mcp 1.0.0 on protocol 2025-06-18, a 2-tool tools/list, and fourteen tools/call attempts across two sessions against the repository's own ten fixtures plus two crafted ones"
relevance: "★★"
tags: [fattura, fatturapa, italian-e-invoice, invoicing, finance, xml, p7m, csv, local-mcp, stdio]
last_updated: "2026-11-28"
---

# FatturaPA MCP

**Italy made the electronic invoice mandatory and then made it awkward: the document that arrives from the supplier is not a PDF but an XML file with abbreviated element names, and a signed copy is a `.p7m` envelope that most tools open as noise. An operator with a folder of these needs one thing before any accounting decision, which is the number, the counterparty, the VAT breakdown and the line items in something a spreadsheet or an agent can read. This server does exactly that and nothing else, on your own machine, with no network call at any point. It is small, it is honest about what it does not verify, and it was installed and driven for this entry rather than quoted from its filing.**

```
Server type:  Local (stdio, Node.js)
Install:      git clone github.com/Agent90ia/fatturapa-converter, cd mcp, npm install
              not published to npm at the time of this pass
Runtime:      node server.js over stdio; deps @modelcontextprotocol/sdk and zod
Tools:        2 (parse_fattura, to_csv)
Limits:       20 files per call, 20 MB per file, 200 MB and 2,000 entries inside a ZIP
Network:      none - the server makes no request
```

`initialize` answered in **0.07 s** as `fatturapa-mcp` **1.0.0** on protocol **2025-06-18** with `tools.listChanged` set, and `tools/list` returned in under a millisecond with the two tools. The repository ships ten fixtures under `samples/` and its own test harness at `mcp/test/test_mcp.js`, so a reader can reproduce every number below without an invoice of their own.

## What it reads

`parse_fattura` takes an array of file objects, each `{ path }` or `{ name, base64 }`, and returns one JSON document with `fatture`, `file`, `avvisi`, `saltati` and `troncato`. Each invoice carries `fmt` (FPR12 or FPA12), `tipo` (TD01 invoice, TD06 professional fee, and the rest of the TD codes), `numero`, `data`, `divisa`, `causale`, the seller as `ced` and the buyer as `ces` with VAT number, tax code, name and address, then `imp` taxable, `iva` VAT, `tot` total, `righe` line items, `riep` VAT summary by rate and nature, `pag` payment terms, `ritenute` withholding, `casse` social-security charges, `iban`, `condPag` and `bollo` stamp duty.

The field that earns trust in a parse is `orig`, which states where the total came from: **`da documento`** on the fixture that carries one, **`calcolato (imponibile + IVA)`** on the fixture that does not. A parser that silently recomputes a total is a parser you cannot audit.

## Driven, on the author's own fixtures

- **Two VAT rates.** `S1_fattura_due_aliquote.xml` returned invoice `2026/17` dated `2026-03-05`: **1075** taxable, **221.5** VAT, **1296.5** total, with the summary split correctly by rate, **125 at 10 percent** (12.5 VAT) and **950 at 22 percent** (209 VAT), against line items of 10 units at 12.5 and one at 950. The seller name came back as `Caffè & Dolci Fittizi S.r.l.` and one description as `Macchina espresso <modello X>` - both survived entity decoding and angle brackets intact.
- **A batch inside one file.** `S3_lotto_due_fatture.xml` produced two invoices labelled `(fattura 1 di 2)` and `(fattura 2 di 2)`, `101` at 300 / 66 / 366 with `orig` reading **calcolato**, and `102` dated the next day with a **49.9** line at 22 percent.
- **A professional's fee.** `S9_professionista_ritenuta_cassa_bollo.xml` is the fixture that shows what an Italian invoice actually carries: withholding `RT01` at **20 percent** taking **200**, a social-security charge `TC04` at **4 percent on a 1000 base = 40**, stamp duty `bollo` **2**, and a payable of **1120.8** against a total of **1320.8**. The arithmetic is checkable and it holds: **1090 + 228.8 + 2 = 1320.8**, and the payable is the total minus the withheld 200. One caveat that belongs in the record: the payable does **not** add the 40 cassa, so on this fixture `pag.imp` equals total minus withholding and nothing else - check that against a real invoice before treating `pag.imp` as the amount the client owes.
- **A signed envelope.** `S6_firmata_base64.xml.p7m` parsed to the same invoice as S1, which is the useful behaviour: the `.p7m` wrapper is unwrapped and the XML inside is read.
- **A ZIP.** `S7_archivio.zip` returned the invoice inside as `S1.xml`, so a supplier's monthly archive works without unzipping it first.
- **Not an invoice.** `S8_non_fattura.xml` answered `isError: true` with the root element named: *"non è una fattura elettronica FatturaPA (elemento radice «Libro»)"* - a refusal that tells you what the file is instead of failing to parse it.
- **CSV with the Italian conventions.** `to_csv` with `foglio: righe` emitted `;`-separated, comma-decimal rows with `\r\n` endings and a weekday-agnostic `01/04/2026` date, which opens in Italian Excel without an import step.

## The CSV is guarded against formula injection, and that was tested

The tool description claims cells beginning with `=`, `+`, `-` or `@` are neutralised. A crafted copy of S1 whose first line description reads `=HYPERLINK("http://evil.example","x")` came back in the CSV as `"'=HYPERLINK(""http://evil.example"",""x"")"` - an apostrophe prefix inside a properly quoted cell, so the spreadsheet shows the text and does not execute it. This matters because the recipients of a mail-merged or exported invoice list are exactly the people an attacker controls.

## Five defects, all reproducible

1. **The `files` argument is an array of objects, and a string array fails the validator.** The filing describes the input as *"files per call"*; the first pass at this entry sent `{"files": ["/path/S1.xml"]}` and every call returned `-32602 Expected object, received string at files[0]`. The correct form is `{"files": [{"path": "..."}]}`. A one-line filing note or a second accepted shape would save every integrator this round trip.
2. **The per-file cap differs by layer.** The MCP tool rejects anything above **20 MB** (`MAX_BYTES` in `server.js`), while the shared core module sets `MAX_ENTRY` at **50 MB** and `MAX_TOTAL` at **200 MB**. A caller reading the core constants will expect a 40 MB signed archive to work and will be refused.
3. **The dependency carries a high-severity advisory.** `npm audit --omit=dev` reports **zod < 4.6.6**, GHSA-mrhx-c7xc-m3w5, *"Zod can exhaust memory while validating oversized constrained collections"*, fixable only by a breaking move to zod 4. For a local-only server the exposure is your own input, but a finance team installing this should know the audit line rather than discover it.
4. **Installation is a git clone.** The package declares a `bin` entry but is not on npm, so a chat client cannot install it and an MCP directory cannot offer a one-click. `git clone`, `npm install`, then an absolute path in `mcpServers`. For an operator audience that is the difference between a five-second trial and a support ticket.
5. **The output speaks one language and its keys are abbreviations.** Field names are `ced`, `ces`, `imp`, `iva`, `tot`, `riep`, `pag`, and error text is Italian throughout. That is correct for its audience - an Italian accountant reads `imponibile` faster than `taxable` - but an agent working in English will either translate freely, which is where mistakes enter a finance workflow, or paste abbreviations into a report.

## Where it belongs

It is a **reader**, not a connector: no authentication, no account, no remote, nothing to revoke, and no data leaving the machine, which is the strongest privacy position available to any tool in this catalog. Pair it with the accounting entries already here - QuickBooks, Odoo, and the invoice and e-invoice parsers in the finance shelf - when the job is *"take this folder of XML my commercialista sent and tell me what I bought and what I owe"*. It does not validate against the XSD schema and it does not verify the digital signature, both stated by the author in the tool description and confirmed here. Treat a parsed `.p7m` as a convenience copy, not as evidence of who signed it.

```bash
# Install and register (tested on node v22.23.4)
git clone --depth 1 https://github.com/Agent90ia/fatturapa-converter
cd fatturapa-converter/mcp && npm install
hermes mcp add fatturapa --command node --args /absolute/path/fatturapa-converter/mcp/server.js
```

## Also worth knowing

The server is by an AI agent (Agent90) on behalf of the Rinveta project, disclosed in the filing and in the repository. The code is plain Node with a single shared core module `src/fpa-core.js` that the project's own converter also uses, so the parsing behaviour is the same one its web tool ships. At the time of this pass the repository had **0 stars**, **0 forks**, no issues open, and was created five days earlier - a young project, and the reason this entry documents behaviour rather than promising a support relationship.
