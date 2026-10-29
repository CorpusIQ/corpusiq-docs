---
title: "Kami - PDF, PNG and Editable PPTX Layout Skill Setup"
description: "Kami: 13.4K combined installs. Layout rules and eight document templates that let AI agents export polished PDF, PNG and editable PowerPoint."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/kami-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "document design", "pdf", "pptx", "typesetting"]
---

# Kami - Setup Guide

**Source:** [tw93/kami](https://www.skills.sh/tw93/kami) via skills.sh - 13.4K combined installs across 1 indexed listing; snapshot 2026-10-28 (Oct 28 evening sweep)

**GitHub:** [tw93/kami](https://github.com/tw93/kami) - 12,119 stars, MIT, branch main, last pushed 2026-10-29T02:40Z; one skill with two identical `SKILL.md` copies, `skills/kami/SKILL.md` and `plugins/kami/skills/kami/SKILL.md`, each sitting beside its own `assets/`, `references/` and `scripts/` directories plus a `CHEATSHEET.md`, with the per-type JSON schemas under `references/schemas/`, and `.claude-plugin/marketplace.json` at the root

**Category:** Document design and typesetting, PDF, PNG and PowerPoint delivery

**Quality Tier:** 🟡 Beta - one author's focused, heavily installed layout skill with permissive licensing and a real verification pipeline, held back from production tier by a Snyk warning on the only sampled listing and by a dependency chain that is not packaged with the skill

Kami is Tw93's layout skill, and the name is the thesis: it means paper in Japanese, and the repository's line is that good content deserves good paper. It is the delivery piece of the author's trilogy, where Kaku writes code and Waza drills engineering habits, and it is deliberately one skill rather than a collection. Everything the skill knows about a document lives in one `SKILL.md`, its reference files, a set of HTML and Python templates and one build script.

What it actually adds is a design system plus a gate. The defaults are a warm parchment canvas at `#f5f4ed`, ink-blue accents at `#1B365D` and one serif family per language, with type size and spacing carrying the hierarchy instead of rules and boxes. On top of that sit eight document templates (One-Pager, Long Doc, Letter, Portfolio, Resume, Slides, Equity Report, Changelog) and a Landing Page system, each in English, Chinese and Korean variants that the skill picks from the language you write in. Around them are eighteen inline SVG diagram types, a chart builder driven by a JSON spec, and three separate slide paths. The output is HTML as the source and PDF as the deliverable, with PNG or editable PPTX on request.

## Installation

The README's primary route installs into the shared `~/.agents/skills` directory, which Claude Code symlinks into and which Codex, Cursor and any other host reading that directory picks up as `/kami`:

```bash
npx skills add tw93/kami -a claude-code codex cursor -g -y
npx skills update -g -y
```

If you prefer the host's own package manager, the repository is also a plugin marketplace, which namespaces the skill as `/kami:kami` and needs Claude Code v2.1.142 or newer:

```text
/plugin marketplace add tw93/kami
/plugin install kami@kami
```

Codex has the same shape:

```bash
codex plugin marketplace add tw93/kami
codex plugin add kami@kami
```

Claude Desktop does not take either route. Download the release asset `kami.zip` from the latest release rather than GitHub's source ZIP, then use Customize, Skills, "+", Create skill and upload the file; updating means Replace on the skill card.

Nothing in the README is written for Hermes, so the copy route is the one that applies here, and the whole directory has to travel because the scripts and templates are the skill:

```bash
git clone https://github.com/tw93/kami.git
cp -R kami/skills/kami ~/.hermes/profiles/corpusiq/skills/
```

Large CJK fonts are kept out of every package. `bash scripts/ensure-fonts.sh` recovers a missing Chinese or Korean face into the user font directory, and inside a repository checkout it copies the tracked fonts into the skill so templates load them locally before falling back to the jsDelivr CDN. On Windows the skill asks for WSL, because the helpers are Bash and WeasyPrint needs the GTK and Pango runtime that native Windows does not ship.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| kami | 13398 | Typesetting resumes, one-pagers, long documents, letters, portfolios, slide decks, equity reports, changelogs and landing pages: pick a template, fill it from a validated `content.json`, then build HTML, PDF, PNG or editable PPTX with content, coverage and page-image checks. |

The single indexed listing clears the 1-install threshold and appears in the table above.

The one row hides most of the surface, so read the repository tree alongside it. `assets/templates/` holds the HTML templates per language and the Marp deck variant, `references/` holds the design spec, the writing guides, per-type JSON schemas, the diagram and Mermaid docs and a production troubleshooting file, and `scripts/` holds the build, brand-extract, Mermaid normalise, font and update-check helpers. The same directory also carries a zero-dependency MCP server that exposes capability diagnosis, render, structured check and screenshot tools, so a pipeline can drive Kami as an engine without loading the full skill prompt.

## Why This Matters for Hermes Agents

An agent's writing is judged by the artifact it produces, and most agents can produce text but not a document that survives a printer, a recruiter or a board pack. Kami closes that gap with rules rather than taste: the templates carry the tokens and components, and the agent's job is to choose the right one, fill it honestly and verify the render.

The verification ladder is the part worth copying into other work. Content is written to `content.json` and validated against a JSON schema before any layout happens, `--deliver` then checks the HTML for placeholders, Markdown residue, unmatched charts and coverage, renders the PDF with WeasyPrint, and finally checks the PDF for page count, font substitution, density and orphans before exporting page images. A missing CJK serif shows up as a heavier, flatter page rather than visible fallback boxes, which is why the font gate exists and why the skill forbids calling a CJK document visually verified on the build result alone.

The honesty rules matter as much as the checks. Anything the template needs and the input lacks goes into one gap table and is marked in the document as `[DATA NEEDED]`, and the skill forbids filling a gap with a guess, a stock image or an approximated logo. Numbers an agent computes must sit next to their inputs or be labelled derived, and the closing message has to state the deliverable path, the build verdict, every gap and the visual verdict as it actually is.

That makes the skill usable in unattended work. It needs no account, no API key and no network beyond a once-daily release check, the build is a single command that ends in `READY` with `ERROR`, `WARN` and `GAP` lines to act on, and the escalate-after-two-rounds rule replaces endless nudging of a value with a labelled A/B/C comparison the human can pick from.

## Usage

| You say | What happens |
|---|---|
| "Make me a two-page resume for this job posting" | The skill locks a contract from the posting and your material, writes `content.json` against the resume schema, fills the resume template, runs `scripts/build.py --deliver` and returns the PDF plus the page count and any gaps. |
| "Turn this research into a one-pager for investors" | The one-pager template is filled from the distilled facts, the metric tiles come from your numbers rather than invented ones, and the PDF is checked for page contract and density before delivery. |
| "I need an editable PowerPoint deck for my talk" | Slides are built on the PPTX path with `python-pptx`, then `--verify slides` and `--check-rhythm` check the deck, and the PDF render is kept as the visual reference. |
| "This printout looks cramped, fix the spacing" | Visual repair mode treats the render as the brief, names the concrete defect and property, changes the smallest thing that fixes it, then re-runs `--deliver` and compares the affected page images. |
| "Build a landing page for my app launch" | The landing page system produces a screen-first static HTML file with the product's own accent colour, and the responsive matrix is screenshotted across every shipped locale before it is called done. |
| "Write a formal recommendation letter for a colleague" | The letter template is used with a single-page contract, the four metadata placeholders in the head are filled, and the build returns a letter PDF whose author, title, description and keywords are set. |
| "Export that changelog as a PNG I can post" | The changelog template is rendered to PDF and the page images are exported as PNG, which is the same path the skill uses for sharing and preview requests. |

## Verification

Both raw paths below returned 200 on the main branch when this guide was written, and the two copies are byte-identical, so read either one:

```bash
for p in skills/kami/SKILL.md \
         plugins/kami/skills/kami/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/tw93/kami/main/$p"
done
```

The skill you should read before installing is the prompt itself, because it carries the routing table, the contract rules and the quality bars:

- https://raw.githubusercontent.com/tw93/kami/main/skills/kami/SKILL.md

After the copy, confirm the whole directory landed rather than just `SKILL.md`. A skill without `scripts/` and `assets/` cannot build anything:

```bash
ls ~/.hermes/profiles/corpusiq/skills/kami
head -5 ~/.hermes/profiles/corpusiq/skills/kami/SKILL.md
python3 ~/.hermes/profiles/corpusiq/skills/kami/scripts/build.py --doctor
```

`--doctor` is the fastest separation of a broken install from a broken host: it reports what is installed before you wait on a render. The update check is the other quick probe, `bash scripts/check-update.sh`, which prints a line only when a newer release exists.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| kami | Pass | Pass | Warn W011 |

One listing was sampled and one verdict is a warning, so the sample says very little about the repository as a whole. Read that as a reason to skim the `SKILL.md` and the scripts before install rather than as a verdict either way.

What runs is small and local. The skill is instructions plus Bash and Python helpers, there is no credential, no API key and no account, and the build renders HTML to PDF through WeasyPrint on the machine doing the work. The update check is the only outbound call by default: `scripts/check-update.sh` writes a daily marker in the local XDG cache directory and resolves GitHub's latest public release, uploads no document or task content, and stays silent when offline or sandboxed.

Two surfaces still deserve attention. `ensure-fonts.sh` writes into the user font directory and can pull fonts from the jsDelivr CDN when the local copies are missing, so on a locked-down host pre-seed the fonts instead. The MCP server loads referenced file, HTTP and HTTPS resources with the permissions of the MCP process, so render only trusted local HTML there; a document template that points at a remote stylesheet or image is a fetch you have authorised. Treat any third-party HTML you feed the build like code, because it is rendered by the same process that reads your working directory.

## Limitations

- Snapshot data, verified 2026-10-28: 13398 combined installs across 1 indexed listing; 12119 GitHub stars; MIT license; last pushed 2026-10-29T02:40Z. Counts drift over time.
- The two `SKILL.md` copies are the same skill in two layouts, byte-identical at this snapshot: `skills/kami/` is the portable directory and `plugins/kami/skills/kami/` is the host plugin. Install one path, not both, or the same trigger phrases get two candidate skills.
- One skill carries all 13,398 installs, so there is no per-capability adoption signal. Nothing in the index tells you whether users lean on resumes, decks or landing pages.
- The build depends on things the package does not ship: WeasyPrint for PDF, `python-pptx` for an editable deck, optional Pygments for code highlighting, and Node 20 or 22 or newer only for LaTeX math delivered as MathJax SVG. Windows needs WSL. `--doctor` reports all of it.
- Chinese and English are the complete paths; Japanese and Korean run on language-specific font fallbacks and layout adjustments and, in the skill's own words, need a visual pass on the page images before shipping. The commercial TsangerJinKai02 face never ships inside the package.
- The install docs cover the skills.sh CLI, the Claude Code and Codex plugins, and Claude Desktop. Nothing is written for Hermes, so the copy route above is the one to use, and the last-push timestamp is the API's UTC value, one calendar day after the snapshot date.

## Related

- [Waza - Engineering Habit Skills for Coding Agents](/hermes/skills/catalog/waza-skills-setup)
- [PowerPoint - Create, Read, Edit .pptx Decks Setup](/hermes/skills/catalog/powerpoint-setup)

## Pro Tips

- Run `python3 scripts/build.py --doctor` before the first deliver on any new host. A missing WeasyPrint fails in the render, and a missing CJK face does not fail at all: it just produces a heavier, flatter page, which is why the font check exists.
- Write `content.json` and check it with `build.py --check-content content.json` before touching layout. Fixing schema errors in content is cheap; fixing them after a fill means rewriting a filled page.
- Put your defaults in `~/.config/kami/brand.md` once: name, role, brand colour, language, page size and tone. The profile fills only the choices the request leaves open, and explicit instructions still win, so it saves repetition without overriding you.
- Ask for PPTX explicitly when you need to edit the deck. The default slide path is PDF, `python-pptx` is the on-request path, and asking later costs a rebuild rather than a conversion.
- When the host cannot view images, ask for the page image paths and the checklist instead of accepting "done". The skill's own definition of done allows the phrase "build verified, visuals unconfirmed", and that is the honest state to report.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
