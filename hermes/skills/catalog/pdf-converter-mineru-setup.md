---
title: "PDF Converter (MinerU) - PDF to Markdown Skill Setup"
description: "PDF Converter (MinerU): 9.6K combined installs. A thin SKILL.md that has an agent run the mineru-open-api CLI for PDF to Markdown, Word and OCR."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pdf-converter-mineru-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "pdf conversion", "ocr", "document extraction"]
---

# PDF Converter (MinerU) - Setup Guide

**Source:** [tanis90/pdf-converter-mineru](https://www.skills.sh/tanis90/pdf-converter-mineru) via skills.sh - 9.6K combined installs across 1 indexed listing; snapshot 2026-10-29 (Oct 29 morning sweep)

**GitHub:** [tanis90/pdf-converter-mineru](https://github.com/tanis90/pdf-converter-mineru) - 55 stars, no LICENSE file at the repo root, branch main, last pushed 2026-05-15; the whole tree is one `SKILL.md` at the repository root plus a 1.1 KB `README.md`, with no scripts, no assets and no manifest

**Category:** Document conversion and OCR instruction sets (PDF, Office files and images to Markdown)

**Quality Tier:** 🟡 Community - a single instruction file from an individual publisher, 55 GitHub stars against 9,620 listed installs, no LICENSE file at the root, and both Gen Agent Trust Hub and Snyk return Fail on the sampled listing while Socket passes

The repository is a wrapper, not a converter. Its entire contents are 7.1 KB of markdown that tells an agent which command to run, and the conversion itself happens on someone else's infrastructure. In the file's own words: "Both commands send the document to MinerU's API (mineru.net) for processing. This is a stateless API call with no persistent storage." The CLI is a separate dependency the file expects to find already installed, and its Troubleshooting section lists the routes: `npm i -g mineru-open-api`, `uv tool install mineru-open-api`, or a vendor script fetched with curl and piped to a shell. Nothing in the repository installs any of that for you, and nothing in it checks that the CLI is present.

What the file does supply is the judgement a conversion task needs. Work is split into two modes: `flash-extract`, no auth, capped at 10 MB or 20 pages per document and returning Markdown only, and `extract`, behind a token from `mineru-open-api auth`, capped at 200 MB or 600 pages with `md`, `json`, `html`, `latex` and `docx` output, formula and table recognition on by default, an `--ocr` toggle, batch mode from globs or a `--list` file, and model selection across `vlm`, `pipeline` and `html`. Language hints default to `ch` (Chinese plus English), with 80 or more languages available through `--language` using PaddleOCR codes. The division of labour is stated plainly: MinerU handles OCR and layout, the agent does the understanding, and raw Markdown is not restructured for you. The last commit, dated 2026-05-15 and titled "Add page range extraction rule and update examples to use explicit file paths", documents a real CLI trap: with `--pages` and `-o` pointing at a directory, the output name comes from the input file alone, so successive chunk extracts of the same PDF overwrite each other.

## Installation

The README's Install section gives the skills.sh CLI form:

```bash
npx skills add tanis90/pdf-converter-mineru
```

The listing is a root-level `SKILL.md` with no skill directory, and Hermes loads skills from named directories, so the predictable route is to create the directory and fetch the file:

```bash
mkdir -p ~/.hermes/profiles/corpusiq/skills/pdf-converter-mineru
curl -sL -o ~/.hermes/profiles/corpusiq/skills/pdf-converter-mineru/SKILL.md \
  https://raw.githubusercontent.com/tanis90/pdf-converter-mineru/main/SKILL.md
```

Then install the CLI the skill actually drives, using one of the two package-manager routes the SKILL.md names:

```bash
npm i -g mineru-open-api
uv tool install mineru-open-api
```

Skip the third route it offers, the curl to shell installer, unless you have read the script. `extract` mode additionally needs a token, which the SKILL.md says comes from running `mineru-open-api auth`; `flash-extract` needs no key at all. The README calls this "A Claude Code skill" and nothing in the tree mentions Hermes, so expect to adjust the wording if your agent needs an explicit trigger phrase.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| pdf-converter | 9620 | One instruction file that has the agent call the MinerU Open API CLI: `flash-extract` for quick reads up to 10 MB or 20 pages with no auth, `extract` for full fidelity up to 200 MB or 600 pages with a token, output as md, json, html, latex or docx, an `--ocr` toggle for scans, batch mode, 80+ language hints, and a page-range naming rule that stops chunked extracts overwriting each other. |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

Reading a PDF is one of the most common things a builder asks an agent to do, and it is also one of the fastest ways to burn a context window, which makes the routing rule in this file worth copying even if you never install it. The file's core instruction is that extraction is step one and understanding is step two: the agent picks a mode, gets text, and then does the summarising or table pulling itself instead of pretending the converter did it.

The two-mode split is a good shape because the limits are explicit rather than discovered. Ten megabytes and twenty pages with no auth covers most quick reads, and the 200 megabyte, 600 page path with a token covers the rest, so an agent can refuse a job or switch modes with a stated reason instead of failing halfway through a large upload.

The page-range rule is the most transferable detail. Directory output plus a page range silently overwrites, and the documented fix is to name each chunk yourself with a `_p{range}` suffix. Any skill that shells out to a vendor CLI should carry that kind of observed-behaviour note, because the failure is silent and destroys work.

The honest caveat is how thin the wrapper is. There is no code, no schema, no test and no version pin, so the skill's correctness depends entirely on the upstream CLI keeping the flags described here, and on the agent reading prose carefully. It also means the documents you hand it leave the host: the skill's own claim is that the call is stateless with no persistent storage, which is a claim about the vendor's service rather than something this repository can enforce.

## Usage

| You say | What happens |
|---|---|
| "What does this paper say?" | The agent runs `flash-extract` without `-o`, reads stdout directly and summarises, because the SKILL.md treats immediate consumption as the no-save case. |
| "Convert report.pdf to Word" | The agent moves to `extract` mode with `-f md,docx`, and tells you to run `mineru-open-api auth` first if no token is configured. |
| "Split this PDF into 20-page chunks" | Output paths are generated explicitly as `./out/report_p1-20.md`, `./out/report_p21-40.md` and so on, because a directory target would overwrite itself per the page-range rule. |
| "Extract the tables from this PDF" | The agent uses `extract` for table fidelity, saves with `-o`, then reads the saved file and pulls the tables out itself. |
| "This is a scan, run OCR on it" | `extract` with `--ocr`, since OCR is described as a toggle on the precision mode rather than a separate command. |
| "It is a German contract" | `--language de` is appended; the default is `ch`, so a language hint is the documented fix for wrong-language output. |
| "Convert every PDF in this folder" | `extract *.pdf -o ./results/`, or `--list files.txt` for an explicit set; batch processing is listed as an `extract` capability only. |

## Verification

The raw path this guide is built on returned 200 on the main branch when it was written on 2026-10-29:

```bash
curl -sL -o /dev/null -w "%{http_code} SKILL.md\n" \
  https://raw.githubusercontent.com/tanis90/pdf-converter-mineru/main/SKILL.md
```

Confirm the copy landed in the profile's skills directory before trusting it:

```bash
ls -l ~/.hermes/profiles/corpusiq/skills/pdf-converter-mineru/SKILL.md
head -3 ~/.hermes/profiles/corpusiq/skills/pdf-converter-mineru/SKILL.md
```

The frontmatter name should read `pdf-converter`. There is no version string anywhere in the file, so compare the byte size instead: the copy cloned for this guide is 7149 bytes.

Finally confirm the dependency exists, because the skill cannot convert anything without it:

```bash
command -v mineru-open-api
```

If that prints nothing, the install step above did not take and every command in the skill will fail.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| pdf-converter | Fail | Pass | Fail E005/W011 |

One listing was sampled and two of the three auditors fail it: Gen Agent Trust Hub returns Fail with no code recorded in this snapshot, Socket returns Pass, and Snyk returns Fail with the codes E005 and W011. These codes are rule identifiers in the auditors' own code lists, and the pack records the codes rather than the finding text, so this guide cannot say what E005 or W011 specifically flagged in this repository. Read the finding text on the listing's security page before installing. As written, the E prefix reads as an error-level rule and the W prefix as a warning, which means Snyk raised at least one hard error and one warning against a repository whose only content is a markdown file and a README, so the finding is likely about what the prose instructs or where it sends data rather than about bundled code.

That distinction matters here, because what installs is a single instruction file that will direct your agent to upload documents to a third-party service. The skill is explicit that both modes send the file to mineru.net and that the call is stateless with no persistent storage, and that is the vendor's claim about its own service, not something verifiable from the repository. Treat any confidential or regulated document accordingly, and read the Data Flow paragraph in the SKILL.md yourself.

One step in the file deserves a direct warning: its Troubleshooting section offers a macOS and Linux CLI install that pipes a remote script into a shell from a CDN host, and a Windows equivalent that pipes into PowerShell. That is a supply-chain path you did not audit. Use the npm or uv route instead, and if you must use the script, download it first and read it.

The licensing position is separate and unresolved: GitHub reports no license, there is no LICENSE file at the root of the tree, and neither the SKILL.md nor the 1.1 KB README carries a license statement. Until the author adds one, the repository is effectively unlicensed for redistribution, which matters if you vendor the file into an internal skills repository or ship it inside a product.

## Limitations

- Snapshot data, verified 2026-10-29: 9620 combined installs across 1 indexed listing; 55 GitHub stars; no license file; last pushed 2026-05-15. Counts drift over time.
- No LICENSE file at the repo root and no license text in the SKILL.md or README, so the repository is unlicensed for redistribution purposes even though it is publicly readable and widely installed.
- The install base is far ahead of the visible community: 9,620 listed installs against 55 GitHub stars, one indexed listing, and a single maintainer whose other indexed repositories are tanis90/coc-cardwright and tanis90/ssskill. There is no issue traffic, review or release history to read as a quality signal.
- The last push was 2026-05-15, roughly five and a half months before this snapshot, and the file documents CLI flags without pinning a CLI version. A flag change upstream would break the instructions silently.
- The repository ships no code and no tests, so the skill can do nothing on its own: it needs `mineru-open-api` on PATH, network access to mineru.net, and a token for `extract` mode. Everything the skill claims about output quality is a claim about MinerU, not about this repository.
- Index and tree agree on one skill only because the `SKILL.md` sits at the repository root with no directory of that name, while the listing is named `pdf-converter`; the README describes the file as "A Claude Code skill", so Hermes users are adapting instructions written for a different harness.

## Related

- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)
- [Agent Research Skills - Academic Paper Suite Setup](/hermes/skills/catalog/lingzhi227-agent-research-skills-setup)
- [Kami - PDF, PNG and Editable PPTX Layout Skill Setup](/hermes/skills/catalog/kami-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the CLI before the skill. Run `command -v mineru-open-api` first, because the skill assumes it is there and its only fallback is a paragraph of troubleshooting prose.
- Default to `flash-extract` and escalate on a stated reason: over 20 pages, over 10 MB, a need for preserved images or formulas, a non-Markdown target, or a scan that needs `--ocr`.
- Always pass an explicit output filename when you use `--pages`. The documented failure is silent overwrite of earlier chunks, and the fix costs one filename suffix.
- Set `--language` on anything that is not Chinese or English. The default is `ch`, and the file names wrong-language output as the symptom of forgetting it.
- Keep the extraction and the understanding as two steps in your own prompt. The skill states that MinerU returns raw Markdown and does not restructure it, so an agent that expects tables or findings to arrive pre-parsed will report nothing useful.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
