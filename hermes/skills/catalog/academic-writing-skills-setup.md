---
title: "Academic Writing Skills - Paper Workflow"
description: "bahayonghang/academic-writing-skills: 18.7K combined installs. Post-writing polish and audit for LaTeX, Typst and Chinese theses, with citations."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/academic-writing-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "academic writing", "latex", "typst", "citations"]
---

# Academic Writing Skills - Setup Guide

**Source:** [bahayonghang/academic-writing-skills](https://www.skills.sh/bahayonghang/academic-writing-skills) via skills.sh - 18.7K combined installs across 11 indexed listings; first seen 2026-10-31 (evening sweep)

**GitHub:** [bahayonghang/academic-writing-skills](https://github.com/bahayonghang/academic-writing-skills) - 528 stars, no license file at the repository root, branch main, last pushed 2026-10-28; 8 `SKILL.md` directories under `academic-writing-skills/`, each with optional `scripts/`, `references/`, `examples/`, `templates/`, `evals/` and `agents/` folders

**Category:** Academic writing for agents: literature review, argument structure, citation hygiene and revision

**Quality Tier:** 🟡 Yellow - all five sampled verdicts are Pass, but the repository ships no LICENSE file and its README closes with "Academic Use Only - Not for commercial use"

This is a working researcher's toolkit rather than a publisher product. The README says the collection grew out of the author's own paper workflow, that `latex-thesis-zh` keeps changing as the dissertation behind it progresses, and that `paper-audit` reports are for reference only and should be verified. The scope is deliberately narrow: post-writing polish and validation for existing drafts, not drafting papers from scratch.

The eleven indexed listings divide by input format and job. Three skills own a file format end to end (`latex-paper-en`, `latex-thesis-zh`, `typst-paper`), two own the post-processing jobs (`paper-writing-studio` for venue-profiled polish and translation, `paper-audit` for reviewer-style critique), one owns the bibliography (`bib-search-citation`), one owns submission correspondence (`cover-letter`), and one renders a defense deck from an existing thesis repository (`latex-defense-zh`). That is eight, the number of in-tree skills, and the README's routing table covers exactly those eight. The other three listings (`industrial-ai-research`, `ieee-writing-materials`, `elsevier-writing-materials`) carry install counts and no files.

## Installation

The README and the installation guide document two different jobs, and it is worth keeping them apart: maintaining this development repository, and installing skill packages into a manuscript project. For a Hermes profile, the second is the relevant one. The collection installs as a whole:

```bash
npx skills add bahayonghang/academic-writing-skills
```

`docs/installation.md` also documents a per-skill form for each of the eight in-tree skills:

```bash
npx skills add bahayonghang/academic-writing-skills/latex-paper-en
npx skills add bahayonghang/academic-writing-skills/paper-audit
npx skills add bahayonghang/academic-writing-skills/typst-paper
npx skills add bahayonghang/academic-writing-skills/bib-search-citation
```

Those per-skill command strings are the documented installer surface, but the same page states plainly that the `npx` installer, any symlink layout it creates and five-tool runtime discovery stay unverified, with no captured real run. Treat the first install as a test rather than a guarantee. There is also a maintainer helper for a clone of the repository, invoked through `just skills-install`, which targets `.claude/skills`, `.cursor/skills`, `.agents/skills` and three other agent directories.

The manual route is the one to use when sibling layout matters, and here it does. `paper-audit` resolves the other skills' scripts from the parent of its own directory: `audit.py` looks for `latex-paper-en/scripts`, `latex-thesis-zh/scripts` and `typst-paper/scripts` beside `paper-audit/`, and the installation guide reports that a lone `paper-audit` copy runs with 8 checks missing while the full sibling layout runs with none missing. Copy the whole directory, never one skill:

```bash
git clone --depth 1 https://github.com/bahayonghang/academic-writing-skills.git /tmp/aws
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -r /tmp/aws/academic-writing-skills/. ~/.hermes/profiles/corpusiq/skills/
```

The toolchain is external to the repository. The README lists Python 3.10 and `uv` for the bundled helpers, TeX Live or MiKTeX with `latexmk` and optionally `chktex` for LaTeX work, XeLaTeX plus CJK fonts for Chinese documents, the Typst CLI for Typst work, and PyMuPDF for PDF audits, with `pymupdf4llm` optional. Install only what the skills you use actually need. The README also notes that the LaTeX loaders reject includes outside the project root, which is a deliberate boundary rather than a bug.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| latex-paper-en | 5,973 | English LaTeX conference and journal papers: compile repair, venue formatting, bibliography and citation checks, section writing, logic, tables, pseudocode, de-AI polish, translation and submission readiness. |
| latex-thesis-zh | 4,247 | Chinese LaTeX master's and doctoral theses: compile diagnostics, GB/T 7714 references, chapter structure, bilingual captions, de-AI polish, blind-review anonymisation and point-by-point review responses. |
| paper-audit | 3,451 | Reviewer-style audit and submission gate for `.tex`, `.typ` or `.pdf` inputs: peer-review critique, readiness decisions, blocker triage, revision roadmaps and re-audits, without editing the source. |
| bib-search-citation | 1,761 | Searching and citing local BibTeX or BibLaTeX libraries, including Zotero exports: filtering by topic, author, year, venue, DOI, arXiv ID or claim support, then emitting LaTeX or Typst citation snippets. |
| typst-paper | 1,545 | Typst manuscripts in English or Chinese: compile and export diagnosis, venue formatting, BibTeX and Hayagriva checks, grammar, logic, tables, pseudocode, related work and submission readiness. |
| cover-letter | 889 | Submission cover letters built against an existing LaTeX manuscript: generating, optimising, align-checking and journal-fit-checking claims against the paper's evidence and the venue's expectations. |
| industrial-ai-research | 469 | Indexed on skills.sh with no directory in the current tree and no entry in the README routing table, so its scope is not documented in the repository. |
| paper-writing-studio | 202 | Polishing or translating academic prose under an explicit Nature, IEEE, Elsevier or neutral profile, reporting venue conflicts and missing evidence instead of guessing. |
| latex-defense-zh | 114 | Chinese doctoral or master's defense decks: read-only extraction from a XeLaTeX thesis repository, page planning by talk length, Beamer rendering with speaker notes and a fidelity gate. |
| ieee-writing-materials | 2 | No directory in the current tree; the in-tree route for IEEE venue style is the IEEE profile inside `paper-writing-studio`. |
| elsevier-writing-materials | 2 | No directory in the current tree; the in-tree route for Elsevier venue style is the Elsevier profile inside `paper-writing-studio`. |

All 11 indexed listings clear the 0-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Most academic-writing prompts fail at the same place: the model improves prose and quietly invents a citation, a result or a venue rule. This collection is built against that failure. The README's safety section says the skills should not invent experiments, citations, policies or unsupported claims, that citation keys, DOIs, arXiv IDs and local `.bib` matches are provenance fields rather than proof that a paper supports a claim, and that suggestions should mark required evidence as pending instead of filling it in. Findings come out in a fixed shape with a module, line number, severity, priority and an explicit `[PENDING VERIFICATION]` marker when evidence is missing.

The split between editing and auditing is the other useful design decision. `paper-audit` diagnoses without rewriting, the format skills rewrite with the syntax preserved, and `bib-search-citation` works on the library rather than the manuscript. That gives an agent three distinct modes with three distinct output contracts, which is a better fit for a review loop than a single general-purpose writing skill.

The eight in-tree skills also carry their own scripts. `paper-audit`, the LaTeX skills, the Typst skill and the bibliography skill ship Python helpers under `scripts/`, run through `uv`, and the README documents opt-in flags that change what the checkers report: `--school`, `--author-cite`, `--repeat-cite`, `--cross-surface` and others each add checks and report local candidates rather than verdicts. For a profile doing document review, that is the difference between a model asserting that a table is consistent and a script listing where the numbers disagree.

## Usage

| You say | What happens |
|---|---|
| "Compile my English LaTeX paper with latexmk and explain the first blocking error" | `latex-paper-en` runs the compile path, reads the log and explains the first blocking error before touching the source. |
| "Check the introduction for logic gaps, citation stacking and AI-like phrasing" | `latex-paper-en` applies its logic, claim-forward and de-AI checks and reports findings by module and line with severity and priority. |
| "Run a paper-audit gate on main.tex and separate blockers from polish issues" | `paper-audit` produces a reviewer-style report with a readiness decision, blocker triage and a revision roadmap, and leaves the source unchanged. |
| "Search references.bib for recent Mamba forecasting papers with code and give me LaTeX and Typst snippets" | `bib-search-citation` filters the local library by topic, year and availability, then emits both citation forms. |
| "Align-check this cover letter against main.tex and report unsupported claims only" | `cover-letter` compares each claim in the draft against the manuscript and lists only the ones it cannot support. |
| "Turn my thesis into a defense deck for a 20 minute talk" | `latex-defense-zh` extracts chapters, figures, equations and publications read only, plans the pages, and renders a Beamer deck with speaker notes and a fidelity gate. |

## Verification

The raw path for `latex-paper-en` returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} latex-paper-en\n" \
  https://raw.githubusercontent.com/bahayonghang/academic-writing-skills/main/academic-writing-skills/latex-paper-en/SKILL.md
```

Expect `200`. After the copy lands, confirm the sibling layout survived, since `paper-audit` depends on it:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/{paper-audit,latex-paper-en,latex-thesis-zh,typst-paper}/ | wc -l
head -5 ~/.hermes/profiles/corpusiq/skills/latex-paper-en/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/paper-audit
```

The count should print 4, the header should show `name: latex-paper-en`, and the `paper-audit` listing should include its `scripts/` folder alongside `SKILL.md`.

## Security

All five sampled skills pass every verdict on skills.sh, which would normally be a Green result; the tier is Yellow because of the license position rather than the security one.

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| latex-paper-en | Pass | Pass | Pass |
| paper-audit | Pass | Pass | Pass |
| cover-letter | Pass | Pass | Pass |
| latex-defense-zh | Pass | Pass | Pass |
| elsevier-writing-materials | Pass | Pass | Pass |

There is no LICENSE file anywhere in the repository root, which is why the pack records the license as none. The README's final section reads "Academic Use Only - Not for commercial use", so the project is source-available under an author-stated restriction rather than under an OSI license. Cite both facts before redistributing anything from it, and treat the skills as usable for personal academic work rather than as a component you can fold into a commercial product.

The executable surface is larger here than in a markdown-only skill pack. Each skill can carry Python helpers under `scripts/`, invoked through `uv`, which read the manuscript, the `.bib` library and the PDF, so they touch local files rather than the network. The README states that online checks are optional and that current venue rules or external metadata should be verified from the original source. The LaTeX loaders reject includes outside the project root as a boundary control, and the installation guide documents the `E-INCLUDE-BOUNDARY` alert for it. Run the helpers in the manuscript's own environment, keep unpublished drafts and reviewer correspondence out of any path the agent writes to, and read a skill's `scripts/` folder before the first run, because the chain from prompt to executed Python here is real.

## Limitations

- Snapshot data, verified 2026-10-31: 18,655 combined installs across 11 indexed listings; 528 GitHub stars; no LICENSE file at the repository root; last pushed 2026-10-28. Counts drift over time.
- The repository has no license file and the README restricts use to academic, non-commercial work. That is a licensing constraint, not a technical one, and it applies to every skill in the collection.
- Index and tree disagree: 11 indexed listings against 8 `SKILL.md` directories. `industrial-ai-research`, `ieee-writing-materials` and `elsevier-writing-materials` have install counts but no directory in the current tree, and `industrial-ai-research` is absent from the README routing table as well.
- `paper-audit` loses coverage when installed alone. The installation guide reports 8 missing checks for a standalone copy against 0 for the full sibling layout, so the per-skill `npx` route is the wrong choice for that one skill.
- The author states that the `npx` installer, any symlink layout it creates and multi-tool runtime discovery are unverified, with no captured real run. Verify the landing directory yourself after the first install.
- The skills assume an external toolchain: Python 3.10 with `uv`, a TeX distribution with `latexmk`, XeLaTeX with CJK fonts for Chinese documents, and the Typst CLI. A profile without those gets advice and no execution.

## Related

- [CCFA Skills - Academic Paper and Research Suite](/hermes/skills/catalog/ccfa-skills-setup)
- [Nature Skills - Academic Writing Setup](/hermes/skills/catalog/nature-skills-setup)
- [Jwynia Agent Skills - Presentation and Writing Suite](/hermes/skills/catalog/jwynia-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy `academic-writing-skills/.` as one unit. `paper-audit` finds the other skills' scripts by walking up to their sibling directories, so a tidy per-skill install quietly disables most of its checks.
- Point the agent at `paper-audit` before a submission deadline rather than after. It separates blockers from polish, which is the ordering a revision plan needs.
- Use `bib-search-citation` for the library and the format skills for the manuscript. Asking a writing skill to invent a citation is the failure mode the README warns about.
- Keep `[PENDING VERIFICATION]` markers in the output. They mark where a human has to supply evidence, and removing them is how a helpful-looking draft turns into an unsupported claim.
- Check the tree before depending on a listing. Three of the eleven indexed names have no skill file, so a workflow built around `industrial-ai-research` has nothing to load.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
