---
title: Connect Dropbox to ChatGPT via MCP
description: "Connect Dropbox to ChatGPT through CorpusIQ MCP. Ask what a contract says, what changed this week and what actually lives in a folder."
category: ChatGPT Integrations
tags: ["connect Dropbox to ChatGPT", "Dropbox MCP", "Dropbox ChatGPT integration", "ask ChatGPT about Dropbox files", "file search in ChatGPT", "CorpusIQ MCP"]
last_updated: "2026-11-08"
canonical: "https://www.corpusiq.io/docs/connect-dropbox-to-chatgpt"
robots: "index,follow"
---

# How to Connect Dropbox to ChatGPT with CorpusIQ MCP

A lot of operating context lives in Dropbox: contracts, past board decks, vendor invoices, design files. Dropbox will find a file by name. It will not tell you what the renewal clause says, and it will not put that clause next to the invoice it belongs to.

Connecting Dropbox through CorpusIQ MCP makes those questions answerable inside ChatGPT, read-only, with the file named in the answer.

## What Questions Can You Ask?

**Find and read**

- "Find my Dropbox file mentioning 'Q3 board deck'."
- "Read the latest agency contract and tell me the notice period."
- "What is in my /Contracts folder?"

**Change over time**

- "Show me Dropbox files I have touched in the last week."
- "Which contracts were updated since the first of the month?"

**Account and storage**

- "How much Dropbox storage am I using, and what is left?"
- "Which folders hold the most files?"

**Cross-source**

- "Compare the invoices in Dropbox against overdue bills in QuickBooks." (requires the QuickBooks connector)
- "Find the signed scope of work for the client whose Stripe subscription lapsed." (requires the Stripe connector)

## FAQ: Common Questions

<details>
<summary><strong>Can ChatGPT upload, edit, move or delete Dropbox files?</strong></summary>

No. The connection approves read access and the connector exposes search and read tools only. Nothing in the surface writes to your account.
</details>

<details>
<summary><strong>Which file types can it read?</strong></summary>

Word documents, Excel workbooks, PowerPoint decks, PDFs and plain text files. The text embedded in the file is what gets read.
</details>

<details>
<summary><strong>A scanned PDF reads as blank. Why?</strong></summary>

Image-only PDFs carry no embedded text, so there is nothing to read. The file needs OCR before any tool can quote from it.
</details>

<details>
<summary><strong>A file I just uploaded is not found.</strong></summary>

Dropbox search runs on Dropbox's own index, which can lag for very recent uploads. Wait a few minutes and ask again rather than reconnecting.
</details>

<details>
<summary><strong>It says the token expired. How do I fix that?</strong></summary>

Disconnect Dropbox in the CorpusIQ dashboard and reconnect. The consent flow issues a fresh token in one step.
</details>

<details>
<summary><strong>Does this work with Dropbox Business?</strong></summary>

Yes. The connection reads what the authorized account can open, whether that is a personal account or a Business team account.
</details>

<details>
<summary><strong>What is retained after a query?</strong></summary>

Direct MCP retrieval is read-only. Raw customer files and full connector response payloads are not retained; operational query logs keep query text and bounded outcome summaries for up to 30 days.
</details>

## How It Works

1. You connect Dropbox in the CorpusIQ dashboard and approve read access on Dropbox's consent screen.
2. CorpusIQ exposes search across file names and content, file reads, recent activity and account storage as MCP tools.
3. You add the CorpusIQ MCP server to ChatGPT. See the [Quick Start guide](quick-start.md).
4. ChatGPT searches for the file, reads the text and answers from it.
5. The answer names the file and folder it came from, so the claim can be checked against the document.

## Setup Guide

1. **Sign up** at [corpusiq.io](https://www.corpusiq.io). The 30-day trial needs no credit card.
2. **Connect Dropbox.** Dashboard, then Connectors, then Dropbox, then sign in and approve read access.
3. **Connect ChatGPT.** Add the CorpusIQ MCP server per the [Quick Start guide](quick-start.md).
4. **Verify.** Ask "how much Dropbox storage am I using". A real quota number means the connection is live.
5. **Explore.** Then ask what a contract actually commits you to, instead of opening it.

## Related Pages

- [Dropbox connector reference](connectors/dropbox.md) - what the connection can see and how the consent flow works
- [Connect Dropbox to Perplexity](connect-dropbox-to-perplexity.md) - the same folders inside a Perplexity thread
- [Connect Google Drive to ChatGPT](connect-google-drive-to-chatgpt.md) - the other file store, same questions
- [Connect Google Docs to ChatGPT](connect-google-docs-to-chatgpt.md) - documents written rather than stored
- [Connect Notion to ChatGPT](connect-notion-to-chatgpt.md) - the knowledge base next to the file store
- [Browse all CorpusIQ connectors](connectors.md) - the full list
- [How to Connect Business Data to ChatGPT](how-to-connect-business-data-to-chatgpt.md) - the general setup

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
