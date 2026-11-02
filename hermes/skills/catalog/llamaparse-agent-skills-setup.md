---
title: "LlamaParse Skills - Document Parsing for Agents"
description: "LlamaParse agent skills: 6.0K combined installs. Cloud parsing, local liteparse, and LlamaCloud Index v2 retrieval for document work."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/llamaparse-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "document parsing", "pdf", "llamaindex"]
---

# LlamaParse Skills - Setup Guide

**Source:** [run-llama/llamaparse-agent-skills](https://www.skills.sh/run-llama/llamaparse-agent-skills) via skills.sh - 6.0K combined installs across 4 indexed listings; first seen 2026-11-01 (evening sweep)

**GitHub:** [run-llama/llamaparse-agent-skills](https://github.com/run-llama/llamaparse-agent-skills) - 85 stars, MIT, branch main, last pushed 2026-07-03; 3 `SKILL.md` directories under `skills/`: `llamaparse`, `liteparse` and `llamacloud-index`

**Category:** Document intelligence for agents: LlamaParse cloud parsing, local liteparse and LlamaCloud Index retrieval

**Quality Tier:** 🟡 Yellow - vendor maintained by LlamaIndex, MIT licensed, 3 skills in the tree; Gen Agent Trust Hub and Socket pass on all four sampled listings, with one Snyk warning on the retrieval skill

LlamaIndex publishes three skills here, split by where the parsing runs. `liteparse` parses on the local machine through the `lit` CLI from `@llamaindex/liteparse`, with no API key and no model in the loop. `llamaparse` uploads a file to the LlamaParse cloud and parses it through the `@llamaindex/llama-cloud` TypeScript client, which needs `LLAMA_CLOUD_API_KEY` in the environment. `llamacloud-index` skips parsing and does retrieval over an existing LlamaCloud Index v2 knowledge base with `curl` and, recommended, `jq`.

What makes the suite worth reading is that the skills carry cost discipline rather than only API shape. The liteparse `SKILL.md` is written from agent traces where the same PDF was parsed up to nine times and a single high-DPI page screenshot cost about 140,000 characters of context, so it prescribes one parse to a temp file followed by cheap `grep -C` passes over that file, and ships a BM25 ranker at `skills/liteparse/scripts/search.py` for when plain keyword searches stall. The llamaparse skill names four parse tiers (`fast`, `cost_effective`, `agentic`, `agentic_plus`), defaults to `agentic`, and insists on the two-step upload then parse pattern with an explicit `expand` value. The index skill treats a knowledge base as a file system: discover indexes, locate files, grep indexed content, then retrieve passages with hybrid sparse plus dense search instead of one-shot RAG.

## Installation

The skills.sh CLI installs the whole suite, or one skill by name:

```bash
npx skills add run-llama/llamaparse-agent-skills
npx skills add run-llama/llamaparse-agent-skills --skill llamaparse
```

The README also points at a zip of the `skills` folder on the GitHub releases page, which the `release.yaml` workflow builds when a release pull request merges into main. That route suits a host without npm, and it ships the same three directories.

Prerequisites differ per skill. Node 18+ and npm are shared. `liteparse` needs the parser installed globally, plus optional host dependencies for non-PDF input:

```bash
npm install -g @llamaindex/liteparse
lit --version
# LibreOffice for Office documents, ImageMagick for images
```

`llamaparse` needs `LLAMA_CLOUD_API_KEY` and the cloud client in the working Node environment; its `SKILL.md` opens with a step 0 that offers `npm install @llamaindex/llama-cloud@latest`. `llamacloud-index` needs the same key, `curl`, and an index that already exists in the account.

For Hermes the CLI step becomes a directory copy, since nothing in the README targets Hermes:

```bash
git clone https://github.com/run-llama/llamaparse-agent-skills.git
cp -R llamaparse-agent-skills/skills/llamaparse ~/.hermes/profiles/corpusiq/skills/
```

Swap `llamaparse` for `liteparse` or `llamacloud-index` to take one of the others. Copy the whole `liteparse` directory rather than the `SKILL.md` alone, because its `scripts/search.py` helper travels with the skill.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| liteparse | 4,129 | Local, model-free extraction with the `lit` CLI: parse a PDF, DOCX, PPTX, XLSX or image once to a text file, then search that file with `grep -C` instead of re-parsing; Office and image input need LibreOffice and ImageMagick. |
| llamaparse | 1,334 | Cloud parsing for documents whose layout defeats plain text extraction: upload, parse at one of four tiers with an explicit `expand` set, and get text, markdown, tables or images back. |
| effective-liteparse | 315 | Listing with no directory of its own in the clone; the repository's local parsing material is the liteparse skill, whose `SKILL.md` is headed Effective LiteParse and refers to its bundled ranker under an effective-liteparse path. |
| llamacloud-index | 201 | Agentic retrieval over a LlamaCloud Index v2 knowledge base through the REST API: discover indexes, locate files, grep indexed content, then pull passages with hybrid sparse plus dense search. |

All 4 indexed listings appear in the table above; the smallest is 201 installs.

## Why This Matters for Hermes Agents

Documents are the most common way an agent blows its context budget, and the failure is quiet: the parse succeeds, the answer arrives, and every later turn pays for the dumped text. The liteparse skill attacks that directly. It makes the parse a one-time step that writes to a file, then keeps every search bounded with `grep -C`, `head` and line numbers, and it batches independent lookups into one shell command so a three-fact question costs one turn instead of three. That is a pattern a Hermes run can follow on any binary format, not only PDFs.

The split by location is the second gain. Two of the three skills send bytes to LlamaIndex infrastructure and need a bearer key; liteparse keeps everything on the host. For a client document under an NDA, or a cron that parses invoices nightly, that distinction decides which skill is allowed to run at all.

The third is retrieval shape. A Hermes agent asked a question about a document set usually issues one semantic query and hopes the top results contain the answer. `llamacloud-index` documents the other loop: list indexes, list files, grep the indexed content, and only then retrieve passages, which is how an agent recovers when the first query misses.

Version metadata is handled too. `metadata.json` tracks a version per skill, `bump_version.py` bumps the semver in that file and in the matching `SKILL.md` frontmatter together, and `ensure_frontmatter.yaml` checks frontmatter on pull requests and pushes to main, so a copy you take today is traceable to a stated skill version.

## Usage

| You say | What happens |
|---|---|
| "Pull the revenue table out of this 90-page annual report" | liteparse parses once with `--no-ocr` to a temp file, greps the term with context and line numbers, and only falls back to `search.py` if two targeted searches miss. |
| "Parse this scanned contract, including the signature blocks" | llamaparse uploads the file first, parses it at tier `agentic` with `expand` set to `markdown_full` plus page metadata, so tables and page-level detail come back as markdown rather than one text blob. |
| "What does our index say about the Q3 refund policy" | llamacloud-index lists indexes, finds the files that mention refunds, greps the indexed content, then retrieves the passages with hybrid search rather than one query. |
| "Convert these 40 invoices to markdown" | liteparse runs `lit parse` per file to its own output path and reports the failures, which is cheaper than streaming 40 documents into the conversation. |
| "The text layer on page 13 is unreadable, get the numbers" | liteparse renders that single page with `--target-pages` at 150 DPI instead of trusting OCR, which avoids the six-figure context cost of a full-resolution screenshot. |
| "Keep this cheap, it is a born-digital report" | liteparse leaves OCR off, uses `--format text` rather than JSON, and reuses the saved text file for every later question about the same document. |

## Verification

Probe the three skill paths on the branch before installing them. All three returned 200 when this guide was written:

```bash
for p in skills/liteparse/SKILL.md skills/llamaparse/SKILL.md skills/llamacloud-index/SKILL.md; do
  curl -s -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/run-llama/llamaparse-agent-skills/main/$p"
done
```

Check the local parser and the key separately, because they fail for different reasons:

```bash
lit --version
test -n "$LLAMA_CLOUD_API_KEY" && echo key-set || echo key-missing
```

After the copy, confirm what landed and that the frontmatter name matches the directory name:

```bash
ls ~/.hermes/profiles/corpusiq/skills/liteparse
head -6 ~/.hermes/profiles/corpusiq/skills/llamacloud-index/SKILL.md
```

A cheap end-to-end check is one page of one document: `lit parse /abs/path/doc.pdf --format text --no-ocr --target-pages "1" -o /tmp/probe.txt`, then `wc -l /tmp/probe.txt`. A non-zero line count proves the CLI, the parse path and the output flags before a batch runs.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| liteparse | Pass | Pass | Pass |
| llamaparse | Pass | Pass | Pass |
| effective-liteparse | Pass | Pass | Pass |
| llamacloud-index | Pass | Pass | Warn |

What installs is small. Each skill directory holds a `SKILL.md`, and two of them add one helper file: `skills/liteparse/scripts/search.py` and `skills/llamaparse/scripts/example.ts`. The repo-level `scripts/` directory (`add_skill.py`, `bump_version.py`, `ensure_frontmatter.py`) is maintainer tooling for the release workflow and is not part of an install.

`search.py` deserves a read before you run it. It starts with a `uv` inline script block that resolves `bm25s` and `aiofiles` from PyPI on first execution, so installing the skill downloads nothing extra while running the helper does fetch and execute third-party Python. If that is not acceptable on a host, keep the shell `grep` workflow the same file describes and skip the ranker.

The credential is the real exposure. `LLAMA_CLOUD_API_KEY` is a bearer token for the LlamaCloud API, and two of the three skills require it, which means the parsed bytes leave the machine and the key sits in the environment of whatever tool call runs. Keep it out of the repo and out of `SKILL.md` edits, scope it to one account, and prefer liteparse for anything that should not leave the host.

The one warning in the sample sits on `llamacloud-index` under Snyk. Read that `SKILL.md` before wiring it into an unattended job, since every operation in it is an authenticated `curl` call against a live knowledge base, and the file's own instruction on a 401 or 403 is to check the key and the region rather than retry. Treat all three files as executable instruction, not documentation: they steer what the agent does next.

## Limitations

- Snapshot data, verified 2026-11-01: 5,979 combined installs across 4 indexed listings; 85 GitHub stars; MIT; last pushed 2026-07-03. Counts drift over time.
- The install index lists 4 listings but the clone holds 3 `SKILL.md` directories (`liteparse`, `llamaparse`, `llamacloud-index`), and `metadata.json` tracks only those three. The fourth listing, `effective-liteparse`, has no directory of its own in the tree.
- The liteparse `SKILL.md` points at its BM25 helper as `./.claude/skills/effective-liteparse/scripts/search.py` while the repo stores it at `skills/liteparse/scripts/search.py`, so that path needs adjusting after a plain copy.
- Two of the three skills need `LLAMA_CLOUD_API_KEY` and send content to LlamaIndex infrastructure; only liteparse runs with no key and no network.
- liteparse is the fast option, not the exact one. The README frames it as a quick parse that is not 100 percent accurate and routes complex layouts to llamaparse.
- The skills assume Node 18+ and a global npm install, and Office or image input adds LibreOffice or ImageMagick as host dependencies that the install does not provide.

## Related

- [PDF Converter (MinerU) - PDF to Markdown Skill Setup](/hermes/skills/catalog/pdf-converter-mineru-setup)
- [Tavily Research - AI-Powered Deep Research Setup](/hermes/skills/catalog/tavily-research-setup)
- [Firecrawl Skills - Web Scraping, Research & Workflow Suite Setup](/hermes/skills/catalog/firecrawl-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Parse once per document per session, then search the file. Every `lit parse` call re-extracts the whole document, and re-parsing per question is the waste the skill was written to stop.
- Ask for the tier before a big file goes to the cloud. `fast` and `cost_effective` suit simple documents, `agentic` is the default for mixed layouts, and `agentic_plus` is the one to name explicitly when accuracy matters more than cost.
- Keep the key in the environment of the tool that parses, not in the skill directory. A `SKILL.md` edited to hold a token gets copied into every later install.
- Verify `lit --version` once, then stop checking it on every run. The skill treats `--version`, `ls` and `--help` calls as wasted turns unless something has already failed.
- When a number matters, read the page, do not trust the OCR. The skill's own guidance is one page render at 150 DPI, not a re-render at higher resolution.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
