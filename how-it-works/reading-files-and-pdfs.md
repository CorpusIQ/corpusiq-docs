# Reading files and PDFs

When you connect a file source — Google Drive, OneDrive, or Dropbox —
CorpusIQ doesn't just see filenames. It reads the text *inside* your
documents and answers from it. Ask "what's the deadline in the vendor
contract in my Drive?" and CorpusIQ opens the PDF, pulls the text, and
answers — citing the file.

This page explains how that text extraction works, and where its limits
are.

## Which files it reads

Across Google Drive, OneDrive, and Dropbox, CorpusIQ reads the common
document formats:

- **PDF** — the main one, and the one with the most care behind it
  (below).
- **Word** (`.docx`, and older `.doc` where possible).
- **Excel** (`.xlsx`) — sheets and rows.
- **PowerPoint** (`.pptx`) — slide text.

The same engine runs no matter which of the three file connectors the
document lives in. Connect Dropbox or Drive or OneDrive — the reading
behaves the same way.

## How PDF reading works

PDFs are deceptively hard. A clean-looking invoice can store its text in
any order, split across columns, or locked inside form fields. CorpusIQ
uses a three-tier strategy and automatically picks the best one that
works for each file:

1. **Form-field reading first.** Many business PDFs — tax forms,
   e-filed paperwork, structured applications — store their real values
   in named form fields rather than free-flowing text. CorpusIQ reads
   those fields directly. This is the most reliable data in the
   document, so it's surfaced first.

2. **Layout-aware extraction.** For everything else, CorpusIQ reads the
   text using each character's actual position on the page. That's the
   part that keeps **tables and multi-column pages intact** — a label
   stays matched to its value instead of getting scrambled the way a
   plain text dump would. A two-column report or a line-item table comes
   out readable, not jumbled.

3. **Plain-text fallback.** If the layout-aware pass isn't available for
   a given file, a straightforward text reader runs as a safety net, so
   you still get an answer.

You can also point CorpusIQ at a **specific page range** in a long
document, or have it **search the document for a term** and return only
the pages that mention it — useful when the file is 200 pages and you
care about one clause.

## The one limit worth knowing

CorpusIQ reads PDFs that contain real, digital text — the kind produced
when a document is exported or saved as a PDF. That covers the vast
majority of business documents.

What it does **not** do today is read a PDF that's purely a *scanned
image* — a photo or scan of a page with no embedded text behind it. For
those, CorpusIQ will tell you honestly that there's no extractable text
rather than guess. Reading text off scanned images is a separate
capability (optical character recognition), and it isn't part of the
file connectors today.

If a scanned document doesn't read, the quickest fix is usually to open
it in the source app and re-save or export it as a text-based PDF, which
most tools can do.

## What this unlocks

Because CorpusIQ reads the contents and not just the file list, you can
ask questions that span your documents the same way you ask about your
sales or marketing data:

- "Summarize the statement of work in the contract in my Drive."
- "What payment terms are in the latest invoice in Dropbox?"
- "Find the renewal date in the lease PDF on OneDrive."

The answer comes back with the source file cited, read-only, pulled live
when you ask — nothing about your files is moved or stored. See
[privacy-and-security.md](privacy-and-security.md) for what that means.
