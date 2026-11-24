---
title: Connect OneDrive to ChatGPT via MCP
description: "Connect OneDrive to ChatGPT through CorpusIQ MCP. Ask what a contract says or what changed this quarter without opening a single folder."
category: ChatGPT Integrations
tags: ["connect OneDrive to ChatGPT", "OneDrive MCP", "OneDrive ChatGPT integration", "ask ChatGPT about OneDrive files", "file search in ChatGPT", "CorpusIQ MCP"]
last_updated: "2026-11-23"
canonical: "https://www.corpusiq.io/docs/connect-onedrive-to-chatgpt"
robots: "index,follow"
---

# How to Connect OneDrive to ChatGPT with CorpusIQ MCP

Contracts, spreadsheets, board decks, the prior report you wrote three months ago. It is all in OneDrive, and OneDrive will find a file if you remember the name it was given.

The questions that actually matter are the other kind. What the renewal clause says. Which pricing sheet is current. What changed since the last review.

Connecting OneDrive through CorpusIQ MCP makes those questions answerable inside ChatGPT, read-only, with the file named in the answer.

## What Questions Can You Ask?

**Find and read**

- "Find my OneDrive file about the Q3 board meeting."
- "Search OneDrive for any contract with Acme Corp and read the payment terms."
- "What does the latest pricing spreadsheet say?"

**Change over time**

- "Show me files I opened recently."
- "Which spreadsheets were edited since the first of the month?"

**Account state**

- "How much OneDrive storage am I using?"
- "Which files have been shared with me?"

**Cross-source**

- "Compare the invoice totals in OneDrive against the bills in QuickBooks." (requires the QuickBooks connector)
- "Does the renewal date in the vendor contract match the next invoice date in Stripe?" (requires the Stripe connector)

## FAQ: Common Questions

<details>
<summary><strong>Can ChatGPT edit, delete or share OneDrive files?</strong></summary>

No. The connection carries read access and the connector exposes file listing and file read tools only. You read files inside ChatGPT; anything that changes a file happens in OneDrive, by you.
</details>

<details>
<summary><strong>Which file types can it read?</strong></summary>

Word documents, Excel workbooks, PowerPoint decks, PDFs and plain text files. What gets read is the text embedded in the file.
</details>

<details>
<summary><strong>It cannot find a file that exists in OneDrive.</strong></summary>

Confirm the file lives in OneDrive rather than a SharePoint site or a Teams shared library. Those are different stores, and this connection reads the personal OneDrive store.
</details>

<details>
<summary><strong>Permission denied on one specific file.</strong></summary>

That file was shared with restricted access. Access follows the Microsoft account you authorized, so a file you cannot open yourself stays out of reach too.
</details>

<details>
<summary><strong>The consent screen is blocked by my organisation.</strong></summary>

Your Microsoft 365 administrator restricts third-party applications. Ask them to approve CorpusIQ for the tenant, then reconnect.
</details>

<details>
<summary><strong>I already connected Outlook. Do I need to connect OneDrive separately?</strong></summary>

Often not. OneDrive can already be authorized under the same Microsoft connection, so check the connector list before running the consent flow again.
</details>

<details>
<summary><strong>What is retained after a query?</strong></summary>

Direct MCP retrieval does not retain raw customer files or full connector response payloads. Operational query logs keep query text and bounded outcome summaries for up to 30 days.
</details>

## How It Works

1. You connect OneDrive in the CorpusIQ dashboard and approve read access on Microsoft's consent screen.
2. CorpusIQ exposes file listing, folder structure, file reads, storage usage and recent activity as MCP tools.
3. You add the CorpusIQ MCP server to ChatGPT. See the [Quick Start guide](quick-start.md).
4. ChatGPT finds the file, reads the text and answers from it.
5. The answer names the file it came from, so the claim can be checked against the document.

## Setup Guide

1. **Sign up** at [corpusiq.io](https://www.corpusiq.io). The 30-day trial needs no credit card.
2. **Connect OneDrive.** Dashboard, then Connectors, then OneDrive, then sign in with your Microsoft account and accept the permissions shown.
3. **Connect ChatGPT.** Add the CorpusIQ MCP server per the [Quick Start guide](quick-start.md).
4. **Verify.** Ask "how much OneDrive storage am I using". A real storage number means the connection is live.
5. **Explore.** Then ask what the current pricing sheet actually says, instead of opening three of them.

## Related Pages

- [OneDrive connector reference](connectors/onedrive.md) - what the connection can see and how the Microsoft consent flow works
- [Connect OneDrive to Perplexity](connect-onedrive-to-perplexity.md) - the same document questions, asked from Perplexity
- [Connect Google Drive to ChatGPT](connect-google-drive-to-chatgpt.md) - the same questions against the other file store
- [Connect SharePoint to ChatGPT](connect-sharepoint-to-chatgpt.md) - the team document libraries beside the personal store
- [Connect Outlook to ChatGPT](connect-outlook-to-chatgpt.md) - the mailbox that usually shares the same Microsoft connection
- [Connect QuickBooks to ChatGPT](connect-quickbooks-to-chatgpt.md) - put the numbers beside the documents
- [Browse all CorpusIQ connectors](connectors.md) - the full list
- [How to Connect Business Data to ChatGPT](how-to-connect-business-data-to-chatgpt.md) - the general setup

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
