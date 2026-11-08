---
title: "Patchwell MCP - Clean Data, Cited Research, Transcripts"
description: "Three agent tools that return evidence: a change log on every cleaned row, a source on every sentence, timings on every word."
category: Data & Document Operations
stars: n/a (vendor-hosted; no public repository)
added: 2026-11-07
source: "The mcpservers.org twelve-sitemap addition `patchwell-io` in the November 7 evening window; the official MCP registry record `io.patchwell/patchwell` at 1.1.0 with remotes `https://patchwell.io/mcp/` and `https://patchwell.io/connect/`; the vendor site and pricing table at patchwell.io; and a keyless initialize on the MCP endpoint that answered 200 as Patchwell 1.30.0 with five tools listed and no credential"
relevance: ★★★★
tags: [data-cleaning, csv, excel, deduplication, cited-research, transcription, change-log, usage-pricing, remote-mcp]
last_updated: "2026-11-07"
---

# Patchwell MCP

**An agent handed a messy export usually does one of two things: refuses it, or quietly changes values and reports success.** Patchwell is a narrow answer to that specific failure. Its cleaning tool returns every edit as a row, a column, a before, an after and the rule that made the change, plus a row count that reconciles the input with the output, and a recipe that replays the same rules on next month's file.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://patchwell.io/mcp/
Connector:   https://patchwell.io/connect/ (signed-in key for chat clients)
Auth:        Bearer API key (bought with prepaid credit)
Tools:       5 (transcribe, research, clean_data, get_job_result, listen_clip)
Pricing:     usage-based, per call, no subscription
Free path:   $1 of credit with an email, no card
```

## What the endpoint says about itself

A keyless `initialize` on `https://patchwell.io/mcp/` answers **200**, not a 401. The server identifies itself as **Patchwell 1.30.0** on protocol `2025-06-18`, and `tools/list` returns five tools:

| Tool | What it does |
| --- | --- |
| `clean_data` | Clean a messy spreadsheet or JSON export into typed, deduplicated records with a log of each change |
| `research` | Answer a question from the live web, with each sentence citing the page it came from |
| `transcribe` | Speech to text with word timestamps and confidence, speaker labels, SRT and VTT |
| `get_job_result` | Fetch the result of a call that returned `{"status": "running", "job_id": ...}`, polled every 20 to 30 seconds |
| `listen_clip` | Play a spot the speaker labels are unsure of. Free |

The key arrives as a bearer token on the MCP connection, and the vendor also exposes REST endpoints on the same domain (`/v1/clean_data`, `/v1/research`, `/v1/transcribe`, `/v1/jobs/{id}`, `/v1/credits/balance`) for code that would rather call HTTP than speak MCP.

## Clean data is the reason to keep the key

The published example is a 352-row customer export cleaned in 1.7 seconds: **301 clean records, 45 duplicate rows merged, 1,429 values changed**, quality scored **0.30 before and 0.998 after**, and each change returned as:

```json
{"row": 2, "column": "Signup Date", "before": "05/03/19", "after": "2019-05-03"}
```

What the tool normalises, per the vendor: dates, phones, money, names, US street addresses, postal codes for **177 countries**, units and broken encodings. Identifiers keep their leading zeros, and barcodes, ISBNs and IBANs are checked against their own check digits rather than guessed at. It merges duplicates and lists the likely ones it will not merge on a guess, which is the behaviour that makes the change log trustworthy: a refused merge is visible, not silent.

Input limits are stated: CSV, TSV, Excel and JSON up to **100 MB or two million rows**. Output downloads as CSV or Excel, and the **recipe** is the part an operator reuses: apply the same decisions to next month's export instead of re-deciding them.

## Research and transcribe, and what "cited" means here

`research` answers in about a minute and attaches a source URL to each statement, lists what it could not confirm in a separate `gaps` field, and reports a confidence level. It **declines questions about individuals** and returns a typed refusal category such as `contact_details` or `tracking_location`, so a policy refusal is distinguishable from an error in code. The sample answer on card processing fees returns the pricing, three source links, and a note that two claims were left out because the sources did not clearly support them.

`transcribe` takes any audio or video link up to three hours (MP4, MOV, WebM, MP3, WAV, M4A, FLAC), detects the language or takes the one you set, and returns words with start, end, probability and speaker labels, plus SRT, VTT and plain text. It removes the phrases Whisper invents over silence and repeated loops and **lists every removal in `flags`**, which is the same discipline as the change log applied to audio.

## Pricing, read off the pricing table

Prepaid credit, deducted per call, no subscription and no expiry:

| Tool | Price | Charged when |
| --- | --- | --- |
| Transcribe | **$0.008** per audio minute, **$0.02** minimum a file | The transcript is delivered |
| Clean data | **$0.50** per 1,000 rows, **$0.01** minimum | The cleaned file is delivered |
| Research | **$0.15** per answered question | A sourced answer is delivered |

Credit is bought in whole dollars from **$10 to $500**, unused credit is refundable within **30 days**, and failed downloads, refused files, refusals and empty answers are not charged. Each response carries a `billing` object, and a long job holds its maximum price and releases the difference on completion. **$20** is presented as roughly 41 hours of audio, 10,000 rows cleaned, or 133 research answers. There is a **$1 free key with no card**.

## Limits worth writing down

- **Trial credit is small.** One dollar buys about 125 audio minutes or two research answers, enough to test the shape of the output and not enough to run a month.
- **100 seconds is the line between a response and a job**, so any real transcription run needs the polling loop, not a single call.
- **It deletes files after the call** and holds only long-job results for a short window, so there is no archive to come back to; keep your own copy.
- **Research refuses people by policy.** An operator expecting a contact lookup will get a typed refusal, by design.
- **No public repository and no self-host path**, so the data path cannot be audited from outside beyond what the vendor states: isolated temporary containers, hashed keys, private and internal network addresses rejected.

## Where it fits beside the other entries

The catalog already carries transcription utilities ([Bulk Transcripts](/hermes/mcp/servers/external/bulktranscripts-mcp/), transcript fetchers) and document automation. None of them do the cleaning step, and the cleaning step is where an operator's data actually breaks: the same customer twice under two spellings, a date column with three formats, a postal code that lost its leading zero. The pairing that earns this entry is the reconciliation: a change log for structured data, a source link for prose, and a flags list for audio, all three returned in fields an agent can check before it acts.

## Frequently asked questions

### What does Patchwell MCP cost?

Usage-based, per call: **$0.008** an audio minute with a **$0.02** minimum per file, **$0.50** per 1,000 cleaned rows with a **$0.01** minimum, and **$0.15** per answered research question. Credit is bought from **$10** to **$500**, does not expire, and is refundable for **30 days**.

### Is there a free way to test it?

Yes. An email address buys a key with **$1** of credit and no card, which covers about 125 audio minutes or two research answers.

### Does `clean_data` tell me what it changed?

Every edit comes back as a row, a column, a before value, an after value and the rule that made the change, plus `stats` that reconcile input rows to clean records and a `recipe` that replays the same decisions on a later file.

### How do long jobs work?

Anything past **100 seconds** returns a `job_id`, and `get_job_result` is polled every 20 to 30 seconds until the result is ready.
