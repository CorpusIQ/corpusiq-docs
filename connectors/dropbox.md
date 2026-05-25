# Dropbox

## What it unlocks
A lot of operating context — contracts, past board updates, vendor invoices, design files — lives in Dropbox folders. Connecting Dropbox lets CorpusIQ search and read those documents so they can show up in answers alongside live data from your other tools.

## Before you connect
- A Dropbox account (personal or Business)
- About 2 minutes

## How to connect
1. In CorpusIQ, open Settings → Connectors and find Dropbox.
2. Click Connect.
3. Sign in to Dropbox when the consent screen appears.
4. <!-- screenshot: Dropbox OAuth consent screen -->
5. Approve read access and you'll be returned to CorpusIQ.

You'll see Dropbox change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- Account info and storage quota
- Files and folders, with search by name or content
- Recently modified files
- The contents of Word docs, Excel, PowerPoint, PDFs, and text files

CorpusIQ never uploads, edits, deletes, or moves files.

## Questions you can ask
- "Find my Dropbox file mentioning 'Q3 board deck'."
- "What's in my Dropbox /Contracts folder?"
- "How much Dropbox storage am I using?"
- "Read the latest agency contract from Dropbox."
- "Show me Dropbox files I've touched in the last week."

## Troubleshooting
- **"Token expired"** — Disconnect and reconnect from Settings → Connectors.
- **Can't find a file** — Search uses Dropbox's index, which can lag for very recent uploads. Wait a few minutes and try again.
- **PDF reads blank** — Image-only PDFs need OCR; CorpusIQ only reads embedded text.
