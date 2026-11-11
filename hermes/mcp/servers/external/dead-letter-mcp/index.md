---
title: "dead-letter MCP - Email Archives an Agent Can Actually Read"
description: "Converts exported .eml and .mbox mail, Gmail Takeout included, into Markdown with YAML front matter: five stdio tools measured end to end, an honest conversion sample, and a noncommercial licence that decides the use case before the install does"
category: "Communication"
stars: "8 (GitHub, 2026-11-11)"
added: 2026-11-11
source: "the mcp.so feed card for /servers/dead-letter read 2026-11-11T10:00Z, the GitHub repository BigCactusLabs/dead-letter, the official registry record io.github.BigCactusLabs/dead-letter at 0.4.10, the LICENSE file on main, the PyPI metadata for 0.4.10, and a local install measured on this host: initialize, tools/list, resources/list and prompts/list over stdio plus four CLI conversions of a crafted .eml"
relevance: ★★★
tags: [email, archive, markdown, eml, mbox, gmail-takeout, rag, digital-preservation, mcp, stdio, python]
last_updated: "2026-11-11"
---

# dead-letter MCP

**The largest corpus most businesses own is a mail archive nobody can query, and the reason is not the mail client. It is the format.** An `.eml` file is MIME: multipart boundaries, duplicated HTML and plain bodies, base64 attachments, tracking pixels and a signature table, all of it noise before a single sentence of business information. dead-letter converts that into Markdown with YAML front matter, locally, one file or ten thousand, and exposes the same conversion as five MCP tools so an assistant can do it without shelling out.

```text
Server type:  stdio, local Python process
Install:      uvx --python 3.12 --from "dead-letter[mcp]" dead-letter-mcp
Server:       dead-letter 0.4.10 (serverInfo), protocol 2025-06-18
Registry:     io.github.BigCactusLabs/dead-letter 0.4.10
Licence:      PolyForm Noncommercial 1.0.0   (read the section below before planning)
Tools:        5 measured, 1 annotated read-only
Resources:    0   Prompts: 0   (both advertised in capabilities, both empty)
Probe:        initialize, tools/list, resources/list, prompts/list over stdio, plus 4 CLI conversions
```

## What the server answered

A local stdio server has no handshake to authenticate, so the only honest measurement is what it declares. `initialize` returned `dead-letter` **0.4.10**, protocol `2025-06-18`, and capabilities `prompts`, `resources` and `tools`. `tools/list` returned exactly **five** tools:

```text
convert_eml            14 inputs   convert one .eml, return Markdown, optionally write it
convert_eml_to_bundle  15 inputs   one .eml into a directory with markdown + attachments
convert_directory      15 inputs   a whole folder of .eml files, bounded recursion
convert_mbox           16 inputs   one flat .mbox archive, Gmail Takeout named explicitly
get_diagnostics        13 inputs   inspect structure and quality, writes nothing  (readOnlyHint: true)
```

`get_diagnostics` is the only tool carrying `readOnlyHint: true`, which is the right shape for an archive job: the agent can look before it writes. `resources/list` and `prompts/list` both came back with **zero** entries even though both capabilities are advertised, so a client that shows a resources panel should be told not to expect any.

The conversion flags are not hidden behind a config file. `convert_eml` exposes `strip_signatures`, `strip_disclaimers`, `strip_tracking_pixels`, `strip_signature_images`, `strip_quoted_headers`, `embed_inline_images`, `include_all_headers`, `include_raw_html`, `no_calendar_summary`, `thread_mode` and `thread_order` as tool inputs, so the model can make a per-message decision rather than inheriting one global setting.

## What the conversion actually produced

The vendor's description is not the test, so a synthetic message was built with the shapes that break naive converters: an HTML body with a duplicated plain-text part, a signature inside an HTML table, a one-pixel tracking image, and threaded headers (`In-Reply-To`, `References`).

Default conversion, 868 bytes in, 465 bytes out:

```markdown
---
source: q3-invoice-discrepancy.eml
subject: 'RE: Q3 invoice discrepancy'
sender: dana@northfield-supply.com
date: '2026-11-09T19:22:10+00:00'
attachments: []
---

Hi Ben,

Short answer: the invoice total is right, our PO was wrong.

Dana

| Dana Whitfield                      |
| ----------------------------------- |
| Accounts Payable, Northfield Supply |
| (555) 013-8821                      |

![](https://track.northfield-supply.com/pixel.gif?id=abc123)
```

Three measured facts in that output. The duplicate plain-text part was resolved to **one** body, not two. The HTML signature table survived as a Markdown table with its phone number intact, which is exactly what you want for contact extraction and exactly what you do not want in a chunk for retrieval. And **the tracking pixel survived the default conversion**: it is still an image reference in the Markdown. Adding `--strip-tracking-pixels` removed it. Adding `--strip-signatures` **did not** remove that table-shaped signature, which is the useful limit to record: the signature heuristic looks for the familiar delimiters, not for a table of contact details.

A second, less obvious win: the date was normalised to ISO 8601 in UTC (`2026-11-09T19:22:10+00:00`) from a `-0500` header, which is the difference between an archive you can sort and an archive you can only read.

## The licence decides the use case before the install does

The repository badge says PolyForm Noncommercial, and the `LICENSE` file on main is that text with a copyright line reading `Copyright (c) 2026 Big Cactus Labs`. The licence defines the boundary in one sentence: **"Any noncommercial purpose is a permitted purpose."**

For a business, that is the whole decision. Converting your own company's mail for internal analysis, a knowledge base or a retrieval pipeline is commercial activity, and the README does not publish a commercial licence or a price. Personal archiving, research and digital preservation are inside the grant; a revenue-generating pipeline is not. The licence is also why this entry sits in the catalog with a warning rather than a recommendation: a free tool with a noncommercial licence is not a free tool for a company, and the check belongs before the install, not after the archive exists.

## What the vendor claims, labelled as vendor copy

The README publishes a token benchmark rather than a feature claim: across an **11-message synthetic set** it reports roughly **88 percent** fewer tokens than the raw `.eml`, and it says where it loses, which is worth quoting because most vendors do not. The naive extractors are cheaper per message precisely because they discard metadata, links and thread structure; the attachment category's median is about **126,000** tokens raw against **180** converted. Those counts measure the Markdown representation, not the binaries or the answer quality.

The same README states the boundary an operator needs to hear plainly: conversion is local, but your MCP host may still send the returned email text to a remote model, so "local conversion" and "private analysis" are two different promises.

## What it does not do

There is no mailbox connection. No IMAP, no OAuth to Gmail, no live sync. It converts files you already exported, which means the workflow starts with an export step that is the operator's to own: Google Takeout, an Outlook export, or a `.mbox` pulled off a server. The MCP surface covers `.eml`, a directory of `.eml` and a flat `.mbox`; the CLI additionally accepts `.zip` and `.tgz` containers, and that is a CLI capability, not a tool input.

## Where it fits

An assistant that answers "what did this customer agree to in the March thread" needs the thread as text with its metadata attached. Converting once, deterministically, with a front matter block that names the source file, beats asking a model to parse MIME every time. The five tools are the right five: one message, one message with its attachments, a directory, an archive, and a read-only inspect. The licence, the missing mailbox connection and the signature heuristic are the three facts that decide whether it belongs in your pipeline, and they were all measured rather than assumed.

The nearest neighbours in this catalog solve different halves. [emailmd MCP](/hermes/mcp/servers/external/emailmd-mcp/) writes and previews outbound email, and the mailbox connectors in this catalog read a live account. This one is the archive-in, Markdown-out step that sits between an export file and everything else.
