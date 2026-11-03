---
title: "Effective HTML - Artifact and Prototype Skills"
description: "plannotator/effective-html: 18.0K combined installs. Eight MIT skills for self-contained HTML artifacts, wireframes, prototypes, plans and diagrams."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/effective-html-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "html", "wireframes", "prototypes", "diagrams"]
---

# Effective HTML - Setup Guide

**Source:** [plannotator/effective-html](https://www.skills.sh/plannotator/effective-html) via skills.sh - 18.0K combined installs across 8 indexed listings; first documented 2026-11-03 (nightly sweep)

**GitHub:** [plannotator/effective-html](https://github.com/plannotator/effective-html) - 3,826 stars, MIT, branch main, last pushed 2026-10-31; eight skill directories under `skills/`, each holding a `SKILL.md` plus an `agents/openai.yaml` invocation policy, and `skills/html` also carrying five reference files under `references/`

**Category:** Single-file HTML deliverables for agents - creative direction, wireframes, prototypes, plans and diagrams

**Quality Tier:** 🟢 Green - all three sampled listings pass Gen Agent Trust Hub, Socket and Snyk, and the repository ships an MIT LICENSE

Effective HTML is published by plannotator, the team behind the Plannotator tool for rendering and annotating local HTML. The repository exists because a wall of text is often the worst way to explain something a model already understands: the README's opening argument is that modern models do well when they are handed real references and asked to show the answer as an artifact rather than describe it.

The collection is eight small skills, not a framework. `html` is the only implicit router and decides which specialist owns the request; the others are direct-invocation specialists that are explicitly told not to activate from a general request. `design-artifact` supplies creative direction, and four workflows cover the artifact types that keep coming up: wireframe, prototype, plan and diagram. The README is candid that the repository is worth reading before it is worth installing, and that framing holds up in the tree: the eight `SKILL.md` files total 466 lines, every skill ships a one-page invocation policy in `agents/openai.yaml`, and the only heavy directory is a marketing site that is not part of any skill.

## Installation

The README's primary route installs the whole collection through the skills CLI:

```bash
npx skills add plannotator/effective-html
```

Listing and per-skill installs are supported, which matters because the router only works well when its siblings are present:

```bash
npx skills add plannotator/effective-html --list
npx skills add plannotator/effective-html --skill html
npx skills add plannotator/effective-html --skill design-artifact
npx skills add plannotator/effective-html --skill html-prototype
```

Claude Code users get the plugin marketplace path, and Codex users get the matching plugin commands:

```bash
/plugin marketplace add plannotator/effective-html
/plugin install plannotator-effective-html@effective-html

codex plugin marketplace add plannotator/effective-html
codex plugin add plannotator-effective-html@effective-html
```

For a Hermes profile, the manual route is a shallow clone and a directory copy into the profile skill root. Copy the whole skill directory, because `skills/html` links relatively into `references/`:

```bash
git clone --depth 1 https://github.com/plannotator/effective-html.git /tmp/effective-html
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -r /tmp/effective-html/skills/html /tmp/effective-html/skills/design-artifact \
      ~/.hermes/profiles/corpusiq/skills/
```

Nothing is installed beyond Markdown and YAML. There is no build step, no package manager dependency and no credential to configure.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| html-diagram | 4,254 | Relationships, sequence, topology, state, hierarchy and system diagrams, built from the smallest visual model that answers the reader's question. |
| html | 3,976 | Broad requests where HTML is the deliverable: reports, explainers, landing pages, presentations, small tools and mixed artifacts, plus routing to the matching specialist. |
| html-plan | 3,897 | Plans, roadmaps, rollouts and implementation sequences that keep the source commitments easy to verify. |
| html-prototype | 1,915 | Polished responsive mockups and working interactive prototypes, with mockup treated as the static fidelity mode inside the same skill. |
| html-wireframe | 1,912 | Low-fidelity layout directions that test information hierarchy, content, navigation, task flow and responsive structure before visual design. |
| design-artifact | 1,804 | Palette, type pairing, layout, theming and overall register for any HTML deliverable, including the case where the output must not look generically AI-generated. |
| big-pics-little-words | 229 | Explaining the current subject in HTML with large visuals and minimal text while keeping the key details. |
| one-pager | 30 | A single HTML page that shares an early idea with teammates or recaps finished work, using big pictures and little words. |

No indexed listings fall below the threshold; all 8 appear above.

The routing logic is worth reading before the individual skills. `html` states that it is the collection's only implicit router and tells the model to continue with itself for reports, explainers, presentations, landing pages, data stories, tools and mixed artifacts, and to hand off when structure, fidelity, plan or diagram is the main review question. Each specialist repeats the boundary from the other side: `html-wireframe` is told not to be used for polished mockups or production-like interaction, `html-prototype` is told not to add behavior merely to make a mockup look complete, and `html-plan` is told that creative direction must not inflate a plan into a dashboard or campaign page.

The invocation policy is enforced in metadata rather than prose. Every skill carries `agents/openai.yaml`, and the flag splits cleanly: `html` and `design-artifact` set `allow_implicit_invocation: true`, while `html-wireframe`, `html-prototype`, `html-plan`, `html-diagram`, `big-pics-little-words` and `one-pager` set it to false. That is the mechanism behind the README's claim that the collection separates creative freedom from reliability.

## Why This Matters for Hermes Agents

An agent that answers a design question in prose is guessing about the thing it was asked to produce. An HTML artifact is inspectable, diffable and reviewable in a browser, and it needs no toolchain: the skills require one self-contained file that opens directly, which is the cheapest possible deliverable to hand back to a human.

The specialist split solves a problem that shows up in every agent with a broad visual skill. A single "make HTML" skill drifts toward one house style, so the tenth artifact looks like the first. Here the router decides fidelity first, `design-artifact` is invoked only when palette, type or register are still open, and the skill text forbids reproducing a prior run's palette or card system. The four workflows also encode different review questions, which is what makes them separable at all: a wireframe answers what belongs on the screen, a prototype answers how the flow behaves, a plan answers who owns what and in what order, a diagram answers how the parts relate.

For a Hermes profile, the practical gain is that artifact work stops being a prompt-engineering problem. The skills carry the authority order explicitly (user instruction, then project design system, then subject, then judgment), they tell the agent to hunt for `AGENTS.md`, `CLAUDE.md` or a tokens file before designing, and they ban lorem ipsum in favour of real content from the first draft.

## Usage

| You say | What happens |
|---|---|
| "Turn this feature brief into a wireframe I can review" | `html` routes to `html-wireframe`, which keeps the artifact visibly low fidelity and may compare two or three structural directions. |
| "Make a clickable prototype of the checkout flow" | `html-prototype` runs in prototype mode and covers navigation, input, state change, feedback and recovery rather than static screens. |
| "Show me a polished mockup of the settings page" | `html-prototype` runs in mockup mode, producing a responsive static artifact with no invented behavior. |
| "Diagram how the ingestion pipeline works" | `html-diagram` picks the model first (topology, sequence, process, state, hierarchy or timeline), then the rendering method. |
| "This report looks AI-generated, fix the design" | `design-artifact` sets palette, type pairing and register, then `html` rebuilds the artifact under that direction. |
| "Make a one-pager for the team about the migration" | `one-pager` produces a single shareable page aimed at a reader who is new to the subject and has a minute. |
| "Explain this whole thing with big pictures" | `big-pics-little-words` builds an HTML explainer that leads with visuals and keeps the key details. |

## Verification

The raw path below returned 200 on branch main on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/plannotator/effective-html/main/skills/html/SKILL.md
```

After a clone, confirm the collection really is eight skills and that the reference tree came with the router:

```bash
git clone --depth 1 https://github.com/plannotator/effective-html.git /tmp/effective-html
ls -d /tmp/effective-html/skills/*/ | wc -l
ls /tmp/effective-html/skills/html/references
grep -H allow_implicit_invocation /tmp/effective-html/skills/*/agents/openai.yaml
```

The count should print 8, the reference listing should show five Markdown files (`charts-and-data.md`, `creative-direction.md`, `diagrams.md`, `documents-and-presentations.md`, `interfaces.md`), and the grep should show two `true` values (`html`, `design-artifact`) and six `false` values.

On the installed copy, check that the router can still see its siblings, because its handoff instructions are relative links:

```bash
ls ~/.hermes/profiles/corpusiq/skills/html/references
grep -n "\.\./html-prototype/SKILL.md" ~/.hermes/profiles/corpusiq/skills/html/SKILL.md | head -3
```

If the sibling directories are missing, `html` still works but loses the handoff, and the agent will build every artifact at the router's default fidelity.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-03) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| html-diagram | Pass | Pass | Pass |
| html | Pass | Pass | Pass |
| html-plan | Pass | Pass | Pass |

The three sampled listings pass all three auditors, which is why this guide is green. The repository supports that reading: across `skills/` there are 13 Markdown files and 8 YAML files and nothing else, with no install script, no hook, no dependency and no network call. Installing a skill copies prose and a policy file.

What the skills do produce is executable content: the artifacts are self-contained HTML files with inline CSS and JavaScript, written to be opened in a browser. Treat an artifact from an untrusted brief the way you would treat any generated page, and open it in a sandboxed browser profile if it was built from third-party content. The repository also ships `examples/release-readiness`, which contains a working prototype and its validation record; those files are examples, not part of any installed skill.

The publisher is plannotator, and the skills only instruct the agent to read local project files (design systems, `AGENTS.md`, existing components) before writing. There is no API key and no third-party service in the loop.

## Limitations

- Snapshot data, verified 2026-11-03: 18,017 combined installs across 8 indexed listings; 3,826 GitHub stars; MIT; last pushed 2026-10-31. Counts drift over time.
- The specialists are direct-invocation only. `html-wireframe`, `html-prototype`, `html-plan`, `html-diagram`, `big-pics-little-words` and `one-pager` all set `allow_implicit_invocation: false` and their descriptions say not to activate from a general request, so installing one alone can leave it unused.
- Handoffs between skills are relative links (`../html-prototype/SKILL.md`, `../design-artifact/SKILL.md`). Install siblings side by side or the router silently degrades to building everything itself.
- `big-pics-little-words` and `one-pager` are 12-line and 13-line prompt files copied from another repository, and they are the two lowest-install listings at 229 and 30. They are prompts, not workflow specifications.
- The README states the repository is usable as a reference without installing anything. If you only want the guidance, read the Markdown instead of wiring eight skills into a profile.
- Nothing here validates the artifact. The examples directory shows a validation record for one worked example, but there is no test harness, linter or checker shipped with the skills.

## Related

- [Popular Web Designs - 54 Design Systems as HTML/CSS Templates Setup](/hermes/skills/catalog/popular-web-designs-setup)
- [Archify - Interactive Architecture Diagram Skill Setup](/hermes/skills/catalog/archify-setup)
- [Diagram Design - Editorial HTML and SVG Diagrams](/hermes/skills/catalog/diagram-design-setup)
- [Markdown Viewer Skills - Diagrams, Charts and Cards Setup](/hermes/skills/catalog/markdown-viewer-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `html` and `design-artifact` first, then add only the specialists you actually reach for. The router plus creative direction covers most requests, and each extra skill competes for the same trigger.
- Copy the whole `skills/html` folder. The router's five reference files carry the detail on charts, documents, interfaces and diagrams, and a skill installed without them is a much thinner instruction.
- Read `design-artifact` before any restyle request. It is the skill that stops the tenth artifact from looking like the first, and it is the one the specialists call when visual direction is still open.
- Follow the authority order the skills state: user instruction, then the project's design system, then the subject, then your own judgment. Most "the artifact looks wrong" complaints trace to skipping step two.
- Compare fidelity on the same content. `examples/release-readiness` does exactly this with a wireframe and a prototype of one brief, which is the cheapest way to review a decision before committing to a design.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
