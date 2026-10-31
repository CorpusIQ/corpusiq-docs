---
title: "JEO Skills - Presentation and Document Suite"
description: "akillness/jeo-skills: 37.9K combined installs. A 411-skill catalog for decks, documents, design and code work, installed through its own router."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/jeo-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "presentations", "documents", "design"]
---

# JEO Skills - Setup Guide

**Source:** [akillness/jeo-skills](https://www.skills.sh/akillness/jeo-skills) via skills.sh - 37.9K combined installs across 112 indexed listings; first seen 2026-10-31 (morning sweep)

**GitHub:** [akillness/jeo-skills](https://github.com/akillness/jeo-skills) - 53 stars, none (no LICENSE file), branch main, last pushed 2026-10-30; 411 `SKILL.md` directories under `.agent-skills/`, flat as `<name>/SKILL.md` with taxonomy kept in `.agent-skills/skills.json` rather than in folders

**Category:** Presentation and document production for agents: slide decks, documents and office deliverables

**Quality Tier:** 🟡 Yellow - the most-installed skill in the catalog, rtk, carries a Gen Agent Trust Hub Fail, and the repository has no LICENSE file despite a badge claiming MIT

This is a curated catalog rather than a package: 411 skills in one flat tree, ten categories of metadata in a single JSON file, and a router called `jeo-skill` that browses, searches and previews a selection before writing anything to disk. The install story is deliberately conservative for a catalog this size, with `--dry-run` on by default in the documented workflow and a `usage scan` lifecycle command for finding skills no agent has ever loaded.

The deck and document work is what the catalog is best at, and it has more depth there than the title suggests. `presentation-builder` produces real editable artifacts (HTML review, PPTX, PDF, Google Slides, Figma Slides) and explicitly routes long-form prose to `technical-writing`; `google-workspace` covers Docs, Sheets, Slides, Drive, Gmail, Calendar and the Admin SDK with an Apps Script, REST or admin-API decision up front; and around them sit `data-analysis`, `design-system`, `responsive-design`, `web-accessibility`, `file-organization` and two Remotion-adjacent video skills. The rest of the catalog is a broad engineering and agent-infrastructure shelf, which is worth knowing before you copy all 411 folders into a profile.

## Installation

The README's recommended route is to let the agent install it, by pasting one line into Claude Code, Codex, Antigravity CLI, Kimi Code, Grok Build, OpenCode or another coding agent:

```text
Read https://raw.githubusercontent.com/akillness/jeo-skills/main/setup-all-skills-prompt.md in full and follow it to install the jeo-skills.
```

That guide detects the OS and the installed agents, and installs the full catalog by default unless you ask for "core only". The second route installs the router first and then lets you pick:

```bash
curl -fsSL https://raw.githubusercontent.com/akillness/jeo-skills/main/install.sh | bash
jeo-skill doctor
jeo-skill search "react performance"
jeo-skill install react-best-practices --global --dry-run
jeo-skill install react-best-practices --global --yes
```

Add `$HOME/.local/bin` to `PATH` if `jeo-skill` is not found afterwards. Bundles and category slices are first class, which is the sane way to take a subset:

```bash
jeo-skill install --bundle starter --global --yes
jeo-skill install --category web --global --yes
```

Under the hood the router delegates to `npx skills@1.7.0 add` and copies each selection into the root its target runtime expects. For this profile, copy the folders directly, and take a named subset rather than the whole catalog:

```bash
git clone --depth 1 https://github.com/akillness/jeo-skills.git /tmp/jeo-skills
cp -r /tmp/jeo-skills/.agent-skills/presentation-builder \
      /tmp/jeo-skills/.agent-skills/technical-writing \
      /tmp/jeo-skills/.agent-skills/google-workspace \
      /tmp/jeo-skills/.agent-skills/design-system \
      ~/.hermes/profiles/corpusiq/skills/
```

Swap in `cp -r /tmp/jeo-skills/.agent-skills/. ~/.hermes/profiles/corpusiq/skills/` only if you genuinely want all 411, and remember that placement is not activation: the host still decides which skill loads.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| rtk | 681 | Installing and wiring RTK, a shell-output compressor that wraps `rtk git status`, `rtk read`, `rtk grep` and similar commands, with `rtk gain` reporting what it saved. |
| graphify | 668 | Driving Graphify from its CLI to build, refresh, query and serve a durable code or corpus knowledge graph, including the stdio MCP server. |
| data-analysis | 599 | Analysing datasets for patterns and reports, with tags covering CSV, SQL, notebooks, telemetry and experimentation. |
| code-refactoring | 519 | Turning a cleanup packet into one behaviour-preserving refactor brief: freezing behaviour first, then slicing the diff into reviewable pieces. |
| technical-writing | 518 | Internal technical documentation: specs, architecture docs, ADRs, runbooks, migration plans and rollout guides for builders and maintainers. |
| remotion-video-production | 514 | A retired name with no folder in the clone; its Remotion route was merged into `video-production` on 2026-09-19 according to the catalog metadata. |
| web-accessibility | 498 | Classifying an accessibility failure by surface (semantics, keyboard, labels, reflow, media alternatives) and turning it into one remediation packet. |
| backend-testing | 498 | Backend test coverage design: API, service and auth-flow coverage, fixture strategy, container-versus-mock choices and flaky-suite stabilisation. |
| video-production | 477 | Programmable video pipelines: Remotion compositions and render workers, template-first generation, captioned variants and video APIs. |
| research-paper-writing | 464 | Drafting and revising ML, CV, NLP and systems papers: claim-evidence flow, ablations, related work and rebuttal letters. |
| design-system | 463 | Defining or refactoring a shared UI system: token governance, visual-language rules, primitive naming and component library foundations. |
| responsive-design | 452 | Responsive layout strategy and verification, sorting "breaks on mobile" into page-shell, component, dense-data or reflow failures. |
| strix | 436 | Running Strix for authorized application security testing: Docker and LLM provider setup, scan depth choice and authenticated test instructions. |
| presentation-builder | 424 | Building editable deck artifacts (HTML review, PPTX, PDF, Google Slides, Figma Slides) for pitch, QBR, launch, architecture and workshop decks. |
| google-workspace | 403 | Workspace automation across Docs, Sheets, Slides, Drive, Gmail, Calendar and Admin SDK, choosing Apps Script, REST API or admin-only APIs first. |
| vercel-react-best-practices | 383 | A name-only listing with no folder and no entry in the catalog metadata; the shipped React performance skill here is `react-best-practices`. |
| survey | 380 | A bounded cross-platform landscape scan before planning: what exists, how people work around it, and which patterns repeat, saved as `.survey/{slug}/` artifacts. |
| task-planning | 378 | Turning vague features or bug clusters into an execution-ready planning packet, separating discovery from delivery and naming blockers and dependencies. |
| react-best-practices | 377 | Measurement-led React and Next.js performance audits: waterfalls, bundle size, client-server boundaries, hydration mismatch and rerender churn. |
| file-organization | 372 | Choosing the right structural boundary (feature, shared layer, route segment, workspace package) and planning the migration between them. |

The remaining 92 indexed listings range from 240 to 371 installs.

The tail is dense and tightly clustered: 92 listings inside a 132-install band, mostly engineering and agent-infrastructure skills such as `codebase-search`, `task-estimation`, `api-design`, `database-schema-design`, `monitoring-observability` and a large game-development group. Two of the twenty table rows are names without a directory, which is a small warning about how the index is built.

## Why This Matters for Hermes Agents

Deliverable work is where general-purpose agents produce the most plausible rubbish. A deck is not an essay with slides, a technical spec is not a tutorial, and a Google Workspace automation is a permission decision before it is a script. This catalog splits those jobs into routed skills with explicit handoffs: `presentation-builder` picks one deck mode and one handoff format, `technical-writing` takes the long-form document, `google-workspace` makes you choose Apps Script versus REST versus admin APIs, and `design-system` refuses responsive-only fixes. That structure is what keeps an agent from producing a 30-slide pitch deck when the request was a one-page review.

The catalog also gives a Hermes profile reach it does not otherwise have. `graphify` builds and serves a knowledge graph over a codebase, `rtk` compresses shell output before it reaches the context window, `survey` runs a bounded landscape scan and stores artifacts rather than chat, and `strix` runs authorized security scans. Those are capabilities rather than writing advice, and they are the reason this pack is worth more than its deck skills.

The cost is attention. 411 skills in one flat tree is far more than a router can reliably choose between, and the catalog's own README argues for installing only what you need. On a profile like this one, install five to ten and let the router stay honest.

## Usage

| You say | What happens |
|---|---|
| "Build me an investor deck from these numbers" | `presentation-builder` picks the deck mode, assembles the smallest useful artifact packet and asks which handoff format you want back. |
| "Turn this design doc into an ADR" | `technical-writing` restructures it to the decision/spec shape and names what still needs a runbook. |
| "Automate a weekly report into a Google Sheet" | `google-workspace` decides between Apps Script and the Sheets API, then handles the Drive and sharing side. |
| "Our design tokens drifted across three products" | `design-system` works token governance and primitive naming before any screen-level polish. |
| "The dashboard breaks on mobile at 380px" | `responsive-design` classifies the failure first (shell, component, dense-data, reflow) and returns one strategy packet. |
| "Which of these three approaches already exists" | `survey` runs the bounded scan and writes reusable artifacts under `.survey/{slug}/` instead of answering in chat. |
| "This page loads slowly after the refactor" | `react-best-practices` audits waterfalls, bundle size and client-server boundaries before anyone touches code. |

## Verification

The raw path for the most-installed skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} rtk\n" \
  https://raw.githubusercontent.com/akillness/jeo-skills/main/.agent-skills/rtk/SKILL.md
```

Expect `200`. After the copy lands, confirm the selection and read one header:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/presentation-builder \
      ~/.hermes/profiles/corpusiq/skills/technical-writing \
      ~/.hermes/profiles/corpusiq/skills/google-workspace \
      ~/.hermes/profiles/corpusiq/skills/design-system | wc -l
head -6 ~/.hermes/profiles/corpusiq/skills/presentation-builder/SKILL.md
```

The count should print 4, and the header should show `name: presentation-builder`, a block `description:` opened with `>`, and an `allowed-tools` list. Confirm that any bundle you installed by name actually landed, since the router resolves names against `skills.json` and a retired alias can resolve to nothing:

```bash
ls -d /tmp/jeo-skills/.agent-skills/rtk /tmp/jeo-skills/.agent-skills/presentation-builder
```

## Security

rtk, the most-installed skill in this catalog at 681 installs, carries a Fail from Gen Agent Trust Hub, while Socket returns Warn and Snyk returns Pass on the same skill - that combination is the main reason to read this section before installing anything here.

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| rtk | Fail | Warn | Pass |
| api-design | Pass | Pass | Pass |
| frontend-design-system | Pass | Pass | Pass |
| zoom-out | Pass | Pass | Pass |
| migrate-to-shoehorn | Pass | Pass | Pass |

The four other sampled skills are clean on all three auditors, so the failure is concentrated rather than systemic, but it lands on the skill the index pushes hardest. rtk is a binary installer and a shell wrapper: it installs a Rust CLI through Homebrew, `install.sh` or Cargo, then wraps common shell commands so their output is compressed before it reaches the model. An agent following that skill will install and execute a third-party binary in your shell, which is exactly the class of action a trust-hub Fail is meant to flag. If you want the token savings, read the skill and install the binary yourself.

The rest of the risk is structural. There is no LICENSE file in the repository, although the README badge links to one and reads MIT, so the actual licensing position is undocumented and redistribution obligations are unclear. `install.sh` is a remote script piped into `bash`, and the README notes that the optional Jev harness and Jevgrep can send data to a configured backend, with remote use gated behind `--allow-remote` in the router but not in the standalone harness.

Two skills in the table deserve a deliberate decision rather than a default install. `strix` pulls a Docker sandbox image and runs vulnerability scans against a codebase, repository, staging URL or domain, which needs an authorization boundary you set yourself. `graphify` writes a code graph into the project and can serve it over stdio MCP, so the graph becomes readable by any client you connect.

## Limitations

- Snapshot data, verified 2026-10-31: 37,915 combined installs across 112 indexed listings; 53 GitHub stars; none (no LICENSE file); last pushed 2026-10-30. Counts drift over time.
- The index covers a fraction of the tree. 112 listings are indexed against 411 `SKILL.md` directories in the clone, so most of what an install actually brings is invisible to the install counts, and the counts say nothing about the other 299 skills.
- Two indexed names have no directory at all. `remotion-video-production` was merged into `video-production` on 2026-09-19 per the catalog metadata, and `vercel-react-best-practices` appears in neither the tree nor `skills.json`. An install that resolves by name will produce nothing for either.
- There is no LICENSE file. The README badge claims MIT and links to `LICENSE`, but the repository does not contain one, so reuse and redistribution are on uncertain ground regardless of the badge.
- The catalog is broad rather than deep on documents. The presentation and document cluster is a handful of entries (`presentation-builder`, `slides-grab`, `technical-writing`, `research-paper-writing`, `api-documentation`, `google-workspace`); the remaining 400-odd skills are engineering, agent infrastructure, game development, design and three.js, so a reader who installs this expecting a document suite gets a general skill library.
- The `skills.json` count and the tree disagree slightly. The metadata declares `skill_count` 409 while the checkout holds 411 `SKILL.md` files, so anything that trusts the JSON for a total is off by two.
- The counts are not a ranking. Everything in the table sits inside 372 to 681 installs, a spread of under two to one, so ordering by installs tells you very little about which skill will help most.
- The router is the only supported path and it is young. `jeo-skill` resolves selections against `skills.json`, delegates installs to a pinned `skills@1.7.0`, and its own README warns that placement is not activation, so a skill on disk may never load.
- One of the two most-installed skills fails an auditor, and it is a binary installer with a shell wrapper. That is a poor default for an unattended profile.

## Related

- [PowerPoint - Create, Read, Edit .pptx Decks Setup](/hermes/skills/catalog/powerpoint-setup)
- [Jwynia Agent Skills - Presentation and Writing Suite](/hermes/skills/catalog/jwynia-agent-skills-setup)
- [Adobe Skills - PDF, Document and Creative Suite Setup](/hermes/skills/catalog/adobe-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Take a bundle, not the catalog. `jeo-skill install --bundle starter --global --dry-run` shows the exact selection before anything is written, which is the only sane way to approach 411 skills.
- Skip rtk unless you have read it. It is the top listing and the only Fail in the sample, and its whole job is installing a binary and intercepting shell output; the token savings are real but so is the surface.
- Check that a name resolves to a folder before you debug a missing skill. `remotion-video-production` and `vercel-react-best-practices` are indexed without directories, so `jeo-skill install` on either is a no-op.
- Use `jeo-skill usage scan` and `jeo-skill usage report` after a month. The catalog's own lifecycle tooling finds skills no host ever loaded, which is the honest measure of whether a 411-skill install was worth it.
- Reach for `presentation-builder` and `technical-writing` together on anything with an appendix. The builder routes long-form prose out by design, so letting both load produces a deck plus the document behind it rather than a deck pretending to be one.
- Keep the `.agent-skills/skills.json` taxonomy if you copy folders. Category and bundle resolution read from it, and a hand-copied subset without it loses the router's ability to find anything.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
