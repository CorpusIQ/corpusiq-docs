---
title: "K2F - Document Generation Skills Setup"
description: "k2f: 62.5K combined installs. An open document format and 42 agent skills that compile semantic JSON into Word, PowerPoint, fillable PDF and IDML."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/k2f-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "document generation", "docx", "pdf", "idml"]
---

# K2F - Document Generation Skills Setup

**Source:** [suzheng/k2f](https://www.skills.sh/suzheng/k2f) via skills.sh - 62.5K combined installs across 42 indexed listings; first seen 2026-10-29 (evening sweep)

**GitHub:** [suzheng/k2f](https://github.com/suzheng/k2f) - 3 stars, Apache-2.0 License (in-repo `LICENSE` and `LICENSE-APACHE`), branch main, last pushed 2026-10-30; 42 in-tree skill folders at `skills/<category>/<skill>/SKILL.md` across 11 category folders (academic, business, core, education, events, expert, forms, legal, marketing, personal, presentation) plus a machine index at `skills/registry.json`, with the core folder `skills/core/k2f/` carrying `references/`, `scripts/`, `schema/`, `catalog/` and `starter/` alongside its SKILL.md (77 files, 2.5M)

**Category:** Document generation and office-format export for agents: Word DOCX, PowerPoint PPTX, fillable AcroForm PDF and Adobe InDesign IDML from a semantic source file

**Quality Tier:** 🟡 Beta - Socket and Snyk Warns on five of the six sampled listings, structural to a document generator that shells out to a Python CLI; Apache-2.0, 3 stars

K2F is an open document format from the suzheng/k2f project, packaged here as a suite of 42 agent skills and published on skills.sh as separate listings. The pitch is that a `.K2F` file is a ZIP holding two states: a semantic JSON tree in `content/root.json`, where every node has a stable dotted `id`, a `role` and optionally a `variant`, and an immutable render lock at `document.K2F.lock` that holds the exact geometry, paint operations and integrity hashes. The agent edits meaning, the engine compiles the lock, and every viewer and every export paints the lock rather than reflowing the tree. Style lives only in `styles/theme.json`, keyed by role and variant, which is what makes a restyle request a theme edit instead of a layout rewrite.

The suite is layered rather than flat. One core skill, `k2f`, does the authoring loop: unpack or init a workspace, write content and design as Markdown first, edit the JSON tree, run `scripts/pack_verify.py`, look at the rendered PNG, then export. The other 41 are task and expert blueprints, roughly 5 to 7 KB of markdown each, that teach the agent what belongs in a given document before any layout happens, so a worksheet gets response types per item and a grant proposal gets a falsifiable hypothesis and independent aims. Exports are one-way drawings of the built lock: `k2f export-pdf`, `export-pptx`, `export-docx` and `export-idml`, with the repo's own constant names spelling out the rule, `PDF_IS_NOT_A_SOURCE` and the same for PPTX, DOCX and IDML.

## Installation

The README's install block is two commands, the skill through the skills CLI and the CLI itself through pip:

```bash
npx skills add suzheng/k2f --skill k2f
pip install k2f
```

`pip install k2f` puts the `k2f` CLI and the Python SDK on the machine (the docs state Python 3.9 or later); `cargo install k2f` is the optional route to a CLI without Python. `npm i @openk2f/k2f` is only for embedding the `<k2f-viewer>` web component. The skill scripts are stdlib-only Python and call `k2f` from `PATH`, or from `K2F_CLI` if you point that variable at a binary explicitly; `scripts/pack_verify.py` does not walk a git checkout looking for one.

Task skills install the same way, one `--skill` flag per invocation, using the `name:` field of each folder. The README only spells out the core name, so read the frontmatter before you assume a slug:

```bash
npx skills add suzheng/k2f --skill k2f-worksheet
npx skills add suzheng/k2f --skill k2f-idml
```

Every one of the 41 task skills carries the same instruction, that the core skill must be installed first, because the task file is a blueprint and the core file is the authoring procedure. When `npx skills` is unavailable, `skills/README.md` documents the manual fallback: copy the `skills/core/k2f` folder into your agent skills path as `k2f/`. That folder is 2.5M, so fetch the archive rather than a single markdown file:

```bash
curl -sL -o /tmp/k2f-main.tar.gz \
  https://github.com/suzheng/k2f/archive/refs/heads/main.tar.gz
tar -xzf /tmp/k2f-main.tar.gz -C /tmp
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -R /tmp/k2f-main/skills/core/k2f ~/.hermes/profiles/corpusiq/skills/k2f
```

One caveat on that copy: `pack_verify.py` resolves its starter package, catalog shapes and schemas relative to the skill directory, so a copy that drops `starter/`, `catalog/` or `schema/` still loads and still fails at pack time.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| k2f-worksheet | 3,275 | Printable fill-in worksheets: practice sets, graphic organizers, lab records, reflections and gap-closure forms, with a response type declared per item (blank line, checkbox, table cell, short paragraph box) and an optional answer key kept separate from the student-facing page. |
| k2f-quotation | 3,141 | Client-ready quotations from scope notes, line items, rates and terms: a scannable offer story, reconciled pricing, explicit in and out of scope, and a validity date, with an explicit ban on inventing rates, deliverables or legal terms. |
| k2f-invitation | 3,079 | Ceremonial invitations for weddings, parties, galas, save-the-dates, RSVP inserts and mobile e-invites, tiering information for guests and expressing formality, density and motif as design intent. |
| k2f-sales-deck | 3,076 | Sales decks, demo presentations and executive briefings with one objective per meeting, the prospect as hero, pain in their own words and proof tied to outcomes, and an instruction not to invent ROI, logos or results. |
| k2f-idml | 3,039 | Multi-page print publications (brochures, magazines, catalogs, annual reports, lookbooks) blueprinted spread by spread with typed editorial blocks for designer handoff, then exported as an InDesign package with its `Document Fonts/` folder. |
| k2f-flyer | 3,002 | Single-page flyers, leaflets and promo sheets for events, offers, restaurants, fitness, real estate and hiring, built around a scannable headline, one primary call to action and hierarchy chosen for a three-second stop. |
| k2f-resume | 2,972 | Achievement-led resumes and CVs, including a refresh targeted at a named job posting, with recruiter-scan tiers and honest metrics instead of a generic duty list. |
| k2f-grant-proposal | 2,918 | Grant narratives, specific aims pages, NIH R01/R21/K and NSF proposals built on a falsifiable hypothesis, explicit gaps, independent aims and reviewer-scannable significance. |
| k2f | 2,883 | The core authoring skill: choose one reference workflow, init or unpack a workspace, write the content and design blueprint as Markdown, edit `content/root.json`, keep style only in `styles/theme.json`, run `scripts/pack_verify.py`, inspect the rendered PNG and export. |
| k2f-lesson-plan | 2,811 | Classroom-ready lesson plans with anchored standards, a timed instructional arc, concrete student tasks and teacher, student and observation artifacts that stay in sync. |
| k2f-company-deck | 2,728 | Company overview and brand decks for stakeholders: who the company is, what it delivers, proof and a contact-ready close, distinct from a fundraising pitch or sales proposal. |
| k2f-business-report | 2,687 | Executive business reports from KPIs, sales or operational data: prioritized findings, trend context, honest data gaps and recommendations that name the next action. |
| k2f-thesis | 2,664 | Book-length theses and dissertations: one defensible central claim, institution-aligned chapter architecture, merged and attributed sources, and defense-ready hierarchy. |
| k2f-purchase-order | 2,596 | Purchase orders with unambiguous buyer and vendor identity, ship and bill routing, reconciled line items, and terms clear enough that the vendor ships and invoices without a clarification loop. |
| k2f-media-kit | 2,498 | Journalist and partner media kits: scannable facts, boilerplate, leadership material and asset guidance, tiered for grab-and-quote use rather than sold as a pitch deck. |
| k2f-aesthetic-ms-word | 1,857 | General-purpose, highly aesthetic Word documents that stay editable in Microsoft Word, built from explicit copy, section-level reading beats and typographic roles instead of manual bold and spacing hacks. |

The remaining 26 indexed listings range from 552 to 840 installs.

## Why This Matters for Hermes Agents

Most document work an agent is asked to do ends in a format the agent cannot safely edit. A DOCX survives a rewrite only until the next style pass, and a PDF is a locked drawing, so "change clause 4" turns into a regeneration with no guarantee that anything else stayed put. K2F separates the two concerns that make that hard: content is a semantic tree with stable dotted node ids, presentation is a theme keyed by role, and the compiled lock sits between the output and any further editing, so a single node can be patched or reverted while the rest stays addressed by id rather than by position.

The second reason is token cost. The 41 task skills are 5 to 7 KB of markdown each, and the core skill is explicit that the agent should read exactly one reference file per task rather than loading every workflow, so a single `--skill` install adds a document-shaped procedure to the profile without dragging a framework into context on turns that have nothing to do with documents, while schemas, catalog node shapes and starter assets stay on disk until the workflow reaches for them.

The third is that the format has a real verification gate rather than an exit code. `pack_verify.py` relocks and can render pages, and the skill treats a blank lower third of a designed sheet as a failure even when the pack exits 0, flagging it as `PAGE_UNDERFILL` and telling the agent to open the PNG, which targets the exact failure mode of generated documents: technically valid, visually empty.

What it is not: a template gallery wrapper or a Word plugin, since the exports are drawings of the lock, so a recipient who edits the DOCX has forked from the source and the K2F tree has to be edited and re-exported to stay authoritative.

## Usage

| You say | What happens |
|---|---|
| "Write a fill-in worksheet on fractions for my grade 8 class" | The k2f-worksheet blueprint fixes the learning frame, sections, item count and a response type per item, writes the answer key separately when asked, then the core k2f skill packs the tree and exports PDF or DOCX. |
| "Turn these scope notes into a quotation the client can accept" | k2f-quotation builds the offer story, reconciles line items against the rates you supplied and states what is out of scope, refusing to invent prices or terms the notes do not contain. |
| "Build a sales deck for Thursday's demo" | k2f-sales-deck keeps the deck to one objective for that meeting with the prospect as hero and proof on each slide; ask for a company overview instead and the agent should route to k2f-company-deck. |
| "Our designer wants the brochure in InDesign" | k2f-idml blueprints the publication spread by spread, then `k2f export-idml doc.K2F -o doc` writes the `.idml` beside a `Document Fonts/` folder for handoff. |
| "Make the intake form fillable" | k2f-fillable-pdf copies real `form_field` nodes rather than underscore blanks, and the default `k2f export-pdf` writes AcroForm widgets; `--flatten` paints glyphs instead when you want a flat print file. |
| "Restyle that deck in a darker palette, keep the layout" | The agent edits `styles/theme.json` only, runs `scripts/pack_verify.py` to relock, then opens the rendered PNG, because `source/` edits are invisible to viewers until compile. |
| "Fix the typo in item 4 and nothing else" | The node is addressed by its dotted id and patched in place, then repacked; the lock is regenerated rather than hand-edited, and the rest of the tree is untouched. |

## Verification

The raw paths below returned 200 on branch main when this guide was written on 2026-10-29:

```bash
curl -sL -o /dev/null -w "%{http_code} core SKILL.md\n" \
  https://raw.githubusercontent.com/suzheng/k2f/main/skills/core/k2f/SKILL.md
curl -sL -o /dev/null -w "%{http_code} grant-proposal SKILL.md\n" \
  https://raw.githubusercontent.com/suzheng/k2f/main/skills/academic/k2f-grant-proposal/SKILL.md
curl -sL -o /dev/null -w "%{http_code} idml SKILL.md\n" \
  https://raw.githubusercontent.com/suzheng/k2f/main/skills/expert/k2f-idml/SKILL.md
```

Expect three `200` lines. Reviewing a SKILL.md before install is worth doing on this suite because the names are the contract: the frontmatter carries a `name:` and a long `description:`, and the description is what the agent matches a request against, so a task skill with a vague description will not fire. Fetch the file, read the `name:` and the "When to Use" section, and confirm the "Built on K2F" section still tells you to install the core skill.

After install, confirm the folder is complete rather than just present, since the scripts need their neighbours:

```bash
ls -l ~/.hermes/profiles/corpusiq/skills/k2f/
head -3 ~/.hermes/profiles/corpusiq/skills/k2f/SKILL.md
k2f --version
```

A good copy shows `SKILL.md`, `references/`, `scripts/`, `schema/`, `catalog/` and `starter/`, the head prints `name: k2f` and its description, and `k2f --version` reports the 0.3.x line the repo is currently on. The machine index at `skills/registry.json` is the other thing to read, because it maps skill ids to category folders and is the only place that lists the suite in one place.

A dry run is cheap and catches most setup faults: init a package, pack it, and open the PNG.

```bash
cd ~/.hermes/profiles/corpusiq/skills/k2f
python scripts/init_package.py --workspace /tmp/k2f-smoke --title "Hello K2F" --page a4
python scripts/pack_verify.py /tmp/k2f-smoke/source -o /tmp/k2f-smoke/doc.K2F --render preview.png
```

The pack prints `UNSIGNED`, which is expected and by design, and the render lands under `/tmp/k2f-smoke/tmp/`.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| k2f-worksheet | Pass | Warn | Warn |
| k2f-quotation | Pass | Warn | Warn |
| k2f-invitation | Pass | Pass | Warn |
| k2f-sales-deck | Pass | Warn | Warn |
| k2f-idml | Pass | Warn | Warn |
| k2f-contract | Pass | Pass | Warn |

No sampled listing fails, and Gen Agent Trust Hub passes all six. The worst verdict is a Warn, and in practice it points at the shape of the thing rather than a known exploit: the skills instruct an agent to shell out to a `k2f` binary that was installed from PyPI at setup time, to fetch Gallery packages over HTTP at run time, and to execute Python helpers from the skill folder. Each of those is a trust boundary a reviewer should accept deliberately, which is why the pack's tier note calls the warns structural.

Two concrete mitigations. Pin the CLI version you install rather than tracking latest, because the skill and the CLI ship from the same repository and track the same 0.3.x line, so a mismatch is a debugging problem rather than a feature. And treat a fetched Gallery package as untrusted input: `k2f unpack` on a downloaded ZIP is the documented route, but the package carries assets and fonts, and the docs' own advice is not to load the ZIP into the agent's context, which is a good habit for size as well as safety. Nothing in this repository pipes curl to bash, and the skill folders themselves contain markdown and stdlib Python only.

## Limitations

- Snapshot data, verified 2026-10-29: 62,502 combined installs across 42 indexed listings; 3 GitHub stars; Apache-2.0; last pushed 2026-10-30. Counts drift over time.
- The listing count and the registry disagree. skills.sh indexes 42 listings and the tree holds 42 skill folders, but `skills/registry.json` names 48 ids: `k2f-award`, `k2f-brochure`, `k2f-certificate`, `k2f-nda`, `k2f-portfolio` and `k2f-template-finder` have entries and no folder, and the registry points `k2f-template-finder` at a `skills/discovery/` path that does not exist in the checkout.
- The task skills are blueprints with no scripts of their own. They hand off to the core skill, so a task-only install produces an agent that knows what a grant proposal should contain and cannot pack one until `k2f` and the core folder are both present.
- 3 stars and the 0.3.x line mean pre-1.0 churn. The format spec is v0.3, the changelog has an Unreleased section ahead of 0.3.3, and the desktop reader is still preview quality with unsigned installers, so pin versions if you depend on exact export behaviour.
- Exports are one-way. Word, PowerPoint, PDF and IDML are drawings of the compiled lock, fillable fields are PDF-only so Word and PowerPoint export them as drawn boxes, and edits made in Office or InDesign fork away from the K2F source with no import path back.
- The install is heavier than the listing suggests. The core folder is 77 files and 2.5M once `catalog/`, `schema/`, `references/` and the starter package with its embedded font are counted, which is fine on disk and wrong for any tooling that copies a single markdown file.

## Related

- [PDF Converter (MinerU) - PDF to Markdown Skill Setup](/hermes/skills/catalog/pdf-converter-mineru-setup)
- [Kami - PDF, PNG and Editable PPTX Layout Skill Setup](/hermes/skills/catalog/kami-setup)
- [Pilio Skills - Image and PDF Utility API Skills Setup](/hermes/skills/catalog/pilioai-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the core skill before any task skill, even the ones you think are standalone. Every task file depends on `scripts/pack_verify.py` and the catalog node shapes that only `skills/core/k2f/` carries.
- Read one reference file per job. The core SKILL.md opens its workflow table with "Read one reference file for the task. Do not load all workflows", and following that keeps a document task at a few thousand tokens instead of pulling the 2.5M folder into context.
- Trust the PNG, not the exit code. `pack_verify.py` returning 0 with `pages=1` does not mean the page is filled; a blank lower third on a designed sheet is a must-fix, and the skill names it `PAGE_UNDERFILL` so you can grep for it.
- Never count text modifier byte ranges by hand. Inline emphasis and links take UTF-8 byte offsets, `scripts/modifier_range.py` computes them, and hand-counting across newlines is the reliable way to produce a broken range.
- Start from a Gallery package when one fits. Fetching `<origin>/api/gallery/templates/<slug>` and running `k2f unpack` gives you a real themed workspace, which is faster and better looking than an empty `starter/` init.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
