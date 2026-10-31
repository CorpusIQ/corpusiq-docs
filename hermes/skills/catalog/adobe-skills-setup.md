---
title: "Adobe Skills - PDF, Document and Creative Suite Setup"
description: "adobe/skills: 76.5K combined installs. Adobe's official agent skills for PDF and document work, AEM sites, analytics, and creative editing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/adobe-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "adobe", "pdf", "aem", "creative"]
---

# Adobe Skills - Setup Guide

**Source:** [adobe/skills](https://www.skills.sh/adobe/skills) via skills.sh - 76.5K combined installs across 137 indexed listings; first seen 2026-10-30 (evening sweep)

**GitHub:** [adobe/skills](https://github.com/adobe/skills) - 318 stars, Apache-2.0, branch main, last pushed 2026-10-30; 178 `SKILL.md` files across nine plugin trees, the largest being `plugins/aem/` with 103

**Category:** Vendor-published agent skills for Adobe document, site, analytics and creative products

**Quality Tier:** 🟡 Yellow - the sampled skills Pass on Gen Agent Trust Hub and Socket but two carry a Snyk Warn, and the Apache-2.0 licence covers a vendor-maintained repo rather than an audited one

Adobe ships this repository as its official collection of skills for AI coding agents, and the README says so in one line: a repository of Adobe skills for AI coding agents. What makes it more than a demo catalog is the breadth under that sentence. Nine plugin trees cover AEM Edge Delivery Services, AEM as a Cloud Service and 6.5 LTS, Adobe Analytics and Customer Journey Analytics, App Builder, Commerce app management, Workfront, the Stardust redesign flow, a browser automation plugin, and a Creative Cloud set that handles PDF, Word, PowerPoint and Excel work plus image editing.

The weight sits in the Edge Delivery Services plugin. Twenty-six skills there form something close to a full development loop for EDS: plan, model content, build blocks, test in a browser, review the code, search the docs, and import an existing page from any URL into EDS block format through a chained pipeline of six skills. The rest of the tree is thinner per product but covers ground most suites leave out, including Dispatcher configuration, Oak query index tuning, replication troubleshooting, and a Universal Editor component model editor.

## Installation

The README documents four install routes. The Claude Code route is the primary one, a marketplace add followed by one plugin install per product area:

```bash
/plugin marketplace add adobe/skills
/plugin install aem-edge-delivery-services@adobe-skills
/plugin install aem-project-management@adobe-skills
/plugin install adobe-analytics@adobe-skills
```

The marketplace manifest registers fifteen plugins, and the README lists an install line for each. The Vercel skills CLI pulls everything at once, which is the shortest route when you want the whole tree:

```bash
npx skills add adobe/skills --all
```

The GitHub CLI extension does the same job:

```bash
gh extension install ai-ecoverse/gh-upskill
gh upskill adobe/skills --all
```

Hermes is not a target of any of those installers, and the Copilot CLI route documented in the README applies to Copilot only, so the durable path for this profile is a directory copy of the plugin you want. Each plugin keeps its skills under a `skills/` folder, so the copy is one directory per product:

```bash
git clone https://github.com/adobe/skills.git
cp -r skills/plugins/aem/edge-delivery-services/skills ~/.hermes/profiles/corpusiq/skills/adobe-eds
```

The checkout holds 178 `SKILL.md` files in all, which is the number to check after a copy. Copy the `skills/` subdirectory rather than the plugin root, because the plugin root also carries manifests, evals and, in some plugins, a `scripts/` tree the agent does not need.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| scrape-webpage | 1,800 | Fetching a source webpage for the import pipeline: scrape the content, extract metadata, download images, and return analysis JSON with local paths. Called by page-import, not directly. |
| code-review | 1,641 | Reviewing Edge Delivery Services code before a pull request or reviewing an existing one: block structure, CSS and JS patterns, DOM output, Lighthouse and accessibility, with findings posted as review comments. |
| docs-search | 1,635 | Searching the aem.live documentation when general web search misses, ranking the matching pages and surfacing code examples and deprecation warnings. |
| building-blocks | 1,633 | Implementing EDS code changes: new or modified block folders and decorate functions, updates to core scripts, scoped CSS, and delayed loading. |
| block-inventory | 1,631 | Surveying the block palette in a local EDS project and in the Block Collection so content modeling decisions rest on what is actually available. |
| content-driven-development | 1,628 | Running the EDS development process: identify or create real test content first, design an author-friendly content model, and validate against that content as the code changes. |
| content-modeling | 1,619 | Designing content models that authors can fill in, when building a new block or reshaping the initial structure of an existing one. |
| analyze-and-plan | 1,616 | Turning an EDS request into acceptance criteria, requirements, a task breakdown, edge cases and a definition of done before code is written. |
| testing-blocks | 1,607 | Validating EDS changes before a pull request: unit tests for utilities and logic, Playwright browser tests, and linting. |
| block-collection-and-party | 1,605 | Finding an existing block, build tool, snippet, integration pattern or plugin to start from, by searching the Block Collection and Block Party repositories. |
| generate-import-html | 1,604 | Producing structured EDS HTML from authoring analysis: section structure, block tables, metadata, and the images folder. |
| page-import | 1,601 | Importing or migrating a single webpage from any URL into canonical EDS block format, including local preview of the result. |
| identify-page-structure | 1,599 | Finding section boundaries and content sequences in a scraped page, with candidate block types annotated per section. |
| find-test-content | 1,599 | Locating existing pages in an EDS project that already use a given block, with occurrence counts and block variants. |
| authoring-analysis | 1,593 | Deciding default content versus blocks for scraped content, including block selection and section styling, before import HTML is generated. |
| page-decomposition | 1,592 | Describing the content sequences inside one section and marking the breaking points between default content and blocks. |
| preview-import | 1,589 | Previewing an import on a local dev server: block rendering, DOM structure, comparison against the original page, and broken references or 404s. |
| whitepaper | 1,577 | Generating a professional PDF whitepaper from a Markdown file, with argument hints for input and output paths. |
| handover | 1,544 | Generating handover documentation for an EDS project, split into guides for content authors, developers and administrators. |
| ue-component-model | 1,543 | Configuring EDS blocks for the Universal Editor through component-definition.json, component-models.json and component-filters.js. |

The remaining 117 indexed listings range from 3 to 1,541 installs.

## Why This Matters for Hermes Agents

The AEM and EDS skills are the reason to install this. They encode a working method rather than a pile of API notes: content-driven development starts from real test content instead of an imagined layout, page-import chains six skills so a single request becomes scrape, structure, decompose, analyze, generate and preview, and code-review closes the loop with the checks a reviewer would run by hand. That division of labour is what makes the suite usable by an agent that has never seen an EDS project.

The PDF and document skills are the second draw, and they are more opinionated than the average document skill. The `adobe-anypdf` family is written to fire before an agent reaches for a Python library: a PDF task routes through the Adobe PDF path even when the text already sits in the conversation, and the docx, pptx and excel skills exist to stop hand-authored `python-docx` and `pptxgenjs` output when a PDF is the source. An agent that follows those descriptions produces converted documents rather than reconstructed ones.

There is a real cost to the size. At 178 skills the routing surface is large, several names are near-duplicates across AEM versions (`aem-workflow` exists under both 6.5 LTS and Cloud Service, each holding eight `SKILL.md` files in the same seven sub-skill layout), and a Copilot CLI install exposes skills under bare names with no plugin prefix, which the README warns produces ambiguity. Copy one plugin per product into the profile rather than the whole tree, so the trigger descriptions stay distinguishable.

The analytics and commerce skills are a different trade. Adobe Analytics and Customer Journey Analytics skills call Adobe-hosted MCP servers and require IMS auth headers, so they only work where an organisation id and a token are available, and the App Builder skills expect a working `aio` project. Install those deliberately, not as part of a bulk copy.

## Usage

| You say | What happens |
|---|---|
| "Import this marketing page into our EDS site" | page-import runs its pipeline: scrape-webpage fetches and cleans the page, identify-page-structure and page-decomposition lay out sections, authoring-analysis picks default content versus blocks, generate-import-html writes the HTML, and preview-import starts the dev server against it. |
| "Review this branch before I open the pull request" | code-review checks block structure, CSS and JS patterns, DOM output, Lighthouse and accessibility, then posts the findings as review comments or GitHub suggestions. |
| "This block needs a new variant and real test content" | content-driven-development finds or creates the content, content-modeling proposes a model authors can fill in, building-blocks writes the block, and testing-blocks runs unit and Playwright checks. |
| "What does aem.live say about the sidekick config?" | docs-search queries the aem.live documentation, ranks the matching pages, and returns the article with its code examples and any deprecation warnings. |
| "Highlight what matters in this contract PDF" | adobe-document-review classifies the document, offers a review focus such as risks, obligations or key dates, and returns highlights with comments. |
| "Wire this new block into the Universal Editor" | ue-component-model edits component-definition.json, component-models.json and component-filters.js so the block appears with the authoring fields you asked for. |
| "Turn this markdown into a PDF whitepaper" | whitepaper renders the Markdown file to a PDF with the skill's own typography and layout conventions, then reports the output path. |

## Verification

The raw path below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/adobe/skills/main/plugins/aem/edge-delivery-services/skills/scrape-webpage/SKILL.md
```

After a copy lands in the profile, confirm the skills are there and readable:

```bash
find ~/.hermes/profiles/corpusiq/skills/adobe-eds -name SKILL.md | wc -l
head -8 ~/.hermes/profiles/corpusiq/skills/adobe-eds/page-import/SKILL.md
```

Expect `26` for the Edge Delivery Services plugin and a frontmatter block that opens with `name: page-import` and a `license: Apache-2.0` line. A whole-tree copy should report `178`.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - two of the five samples carry a Snyk Warn, which means static analysis flagged a pattern worth reading rather than a confirmed exploit, and Gen Agent Trust Hub and Socket Passed on all five; re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| scrape-webpage | Pass | Pass | Warn |
| code-review | Pass | Pass | Warn |
| docs-search | Pass | Pass | Pass |
| building-blocks | Pass | Pass | Pass |
| performance-tuning | Pass | Pass | Pass |

The two Warns sit on the skills that touch the most external surface. scrape-webpage fetches arbitrary URLs and writes downloaded images to disk, and code-review reads repository code and can post review comments through the GitHub API, so both are skills whose input is not under the agent's control. That is the ordinary shape of a Warn on this index: a network-facing or write-capable skill rather than a malicious one, and neither verdict is a Fail.

Read the frontmatter before installing a plugin you do not need. Several skills declare `allowed-tools` including `Bash` and `Write`, `whitepaper` and `handover` among them, which means those skills are permitted to run shell commands and write files on your behalf; the descriptions are written to scope when they run, but the tool grants are the real limit. The analytics, CJA and commerce plugins call Adobe-hosted endpoints and require IMS auth headers, so credentials for those services never live in the skill files themselves, and the OAuth proxy the README mentions is where that token handling should stay.

## Limitations

- Snapshot data, verified 2026-10-30: 76,451 combined installs across 137 indexed listings; 318 GitHub stars; Apache-2.0; last pushed 2026-10-30. Counts drift over time.
- The index is thinner than the tree. skills.sh carries 137 listings against 178 `SKILL.md` files in the checkout, so some skills have no install count of their own, and several listings point at a directory that holds a family of nested sub-skills rather than a single file.
- The install counts are uneven and the tail is long. Twenty listings sit between 1,543 and 1,800 installs, almost all of them Edge Delivery Services, while the remaining 117 run down to 3, so a low number records how recently a listing was indexed more than how good the skill is.
- The Creative Cloud skills are the least installed part of the suite and the least advertised. The `adobe-for-creativity` plugin carries sixteen skills including the PDF, docx, pptx and excel converters, ships its own plugin manifest, and does not appear among the fifteen entries in the top-level marketplace manifest, so the `/plugin install` route does not reach it and a directory copy is the way in.
- Product skills need product access. Adobe Analytics and Customer Journey Analytics skills call Adobe-hosted MCP servers and require IMS auth headers, App Builder skills assume an existing `aio` project, and Workfront skills assume a Workfront tenant, so installing the markdown alone does not make any of them functional.
- The AEM version trees overlap by design. `aem-workflow`, `dispatcher` and `aem-replication` exist under both 6.5 LTS and Cloud Service with near-identical sub-skill layouts, so two installed plugins can put same-named skills in front of the same agent.

## Related

- [K2F - Document Generation Skills Setup](/hermes/skills/catalog/k2f-setup)
- [Kami - PDF, PNG and Editable PPTX Layout Skill Setup](/hermes/skills/catalog/kami-setup)
- [PDF Converter (MinerU) - PDF to Markdown Skill Setup](/hermes/skills/catalog/pdf-converter-mineru-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy per plugin, not the whole tree. `aem-edge-delivery-services` alone is twenty-six skills that route cleanly; all 178 at once buries the trigger descriptions that make routing work.
- Start with `page-import` if you have a single page to move. It is the one skill that composes the rest of the pipeline, and watching its six steps run tells you which of the other EDS skills you actually need.
- Run `docs-search` before letting the agent invent an EDS pattern. It ranks the aem.live pages and returns the deprecation warnings that a model trained earlier will get wrong.
- Use `testing-blocks` and `code-review` together at the end of a change, not instead of each other: the first runs the tests, the second reads the diff against EDS conventions.
- Reach for `adobe-anypdf` first on document work. Its description is written to override the reflex to hand-author a PDF with a Python library, and the docx, pptx and excel variants exist to route conversions through it.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
