---
title: "AntV Chart Visualization Skills - Data to Charts"
description: "antvis/chart-visualization-skills: 18.1K combined installs. Nine AntV skills for picking chart types and generating G2, G6, X6 and infographic output."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/antvis-chart-visualization-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "data visualization", "charts", "antv"]
---

# AntV Chart Visualization Skills - Setup Guide

**Source:** [antvis/chart-visualization-skills](https://www.skills.sh/antvis/chart-visualization-skills) via skills.sh - 18.1K combined installs across 13 indexed listings; first seen 2026-11-02 (morning sweep)

**GitHub:** [antvis/chart-visualization-skills](https://github.com/antvis/chart-visualization-skills) - 524 stars, MIT with a `LICENSE` file in the root, branch master, last pushed 2026-09-22; 9 `SKILL.md` directories under `skills/` with 11 Markdown files between them, plus a TypeScript context service, a test suite and an `eval/` harness in the same repository

**Category:** Chart selection and rendering for agents: AntV grammar-of-graphics guidance for statistical and narrative charts

**Quality Tier:** 🟡 Yellow - the skill text is MIT, the repository is active and ships a 174-case evaluation harness, but three of the five sampled listings carry a warn (Socket on the narrative skill, Snyk on two of the GPT-Vis skills), two skills call a remote AntV API, and the install index carries four listings with no directory in the tree

AntV is Ant Group's open-source visualization stack, started in 2017 around the idea that charting should be expressed as a grammar rather than a fixed component list. The README splits the work into four series, 2, 6, 7 and 8, for statistical analysis, graph analysis, geographical analysis and unstructured data, and the skills in this repository are the agent-facing layer over the same libraries: G2 for statistical charts, G6 for graphs and networks, X6 for diagrams and editors, GPT-Vis for framework-agnostic output, and Infographic and T8 for text-shaped visual output.

The repository is more than Markdown. It ships a context retrieval service with a hosted HTTP endpoint, a CLI published as `@antv/chart-visualization-skills` (version 0.1.6 in `package.json`), and a TypeScript API, all built on an index of G2, G6 and X6 reference documents under `src/content/`. The README's evaluation table reports the harness tuned skills at up to 98.2 percent on G2 and 97.9 percent on G6 across 174 chart-generation cases, against a Context7 baseline of 80.5 and 79.2; those figures are the vendor's own measurements rather than an independent benchmark.

The nine directories are the whole shipped surface, and the install index disagrees with them: 13 indexed listings, 9 directories, and four names with no counterpart in the current tree. That gap is the main thing to understand before installing, because the four missing names include the second most installed listing in the pack.

## Installation

The README documents a Claude Code marketplace route and a skills CLI route:

```text
/plugin marketplace add antvis/chart-visualization-skills
```

```bash
npx skills add antvis/chart-visualization-skills
```

There is no `apm.yml` here; the plugin manifest lives in `.claude-plugin/`, and the two commands above are the documented install paths. The npm package is a separate thing: it installs the retrieval CLI, which searches the same reference corpus locally or against the hosted service, and it does not install the skill directories:

```bash
npm install -g @antv/chart-visualization-skills
antv retrieve "bar chart" --library g2 --topk 10
```

For a Hermes profile, copy the directories. Nothing in the repository mentions Hermes, and the skills are plain folders plus Markdown:

```bash
git clone https://github.com/antvis/chart-visualization-skills.git
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -r chart-visualization-skills/skills/* ~/.hermes/profiles/corpusiq/skills/
```

To update, run `git -C chart-visualization-skills pull` and copy again. The skills themselves carry no build step. The CLI and the context service are TypeScript and need `npm run build` from the package if you want to run them from a clone, which the `package.json` scripts show as `build:index` followed by `tsc`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| chart-visualization | 6,427 | Chart selection and rendering: picks one of 26+ chart types for a data description, extracts parameters, and renders a chart image by calling the AntV API with curl across time series, comparison, part-to-whole, relationship, geographic, hierarchical and statistical charts. |
| infographic-creator | 2,266 | Indexed listing with no directory in the current `skills/` tree and no entry in the README's Available Skills list. Read the count as install history rather than as a skill you can install under this name. |
| icon-retrieval | 1,626 | Icon search: queries the icon service over HTTP with curl and returns up to 5 matching SVG strings with their URLs, with `topK` to widen the set, for infographics, web UI and diagram work. |
| narrative-text-visualization | 1,558 | The tree carries this as antv-t8-ntv, whose own heading reads Narrative Text Visualization Skill: T8 Syntax reports with semantic entity annotations for metrics, values, trends and dimensions. |
| antv-g2-chart | 1,382 | G2 v5 code generation: 30+ chart types, data transforms, coordinate systems, scales, interactions, components and multi-view composition, with guard rails against v4 to v5 migration pitfalls. |
| antv-skills-maintainer | 1,243 | Indexed listing with no directory in the current `skills/` tree and no entry in the README's Available Skills list. Read the count as install history rather than as a skill you can install under this name. |
| antv-g6-graph | 1,164 | G6 v5 graph code: network and tree graphs, node, edge and combo structures, 10+ layouts, behaviours and plugins, custom elements, with migration guard rails. |
| antv-s2-expert | 1,163 | Indexed listing with no directory in the current tree. The shipped skills defer S2 pivot tables rather than cover them, and the G2, G6 and X6 descriptions all name S2 as out of scope. |
| antv-x6-editor | 695 | X6 v3 diagram editor code: flowcharts, DAGs, ER diagrams, org charts and UML, the 11 official plugins, HTML shape nodes, serialisation, with strict rules on container and render calls. |
| gpt-vis | 283 | GPT-Vis output in two modes: Syntax mode for declarative configuration that `GPTVis.render()` consumes, and code mode for runnable HTML, React or Vue across 26 chart types. |
| antv-infographic | 137 | Infographics from text content: 50+ templates across lists, sequences, hierarchies, comparisons, relations and charts, for turning written material into a visual summary. |
| antv-gpt-vis | 95 | The English-language GPT-Vis skill, the same two output modes and 26 chart types as gpt-vis, shipped as its own directory in the current tree. |
| antv-t8-ntv | 89 | T8 Syntax narrative text: data interpretation reports, summaries and structured articles with entity annotations, mini charts and framework-agnostic rendering. |

No indexed listings fall below the threshold; all 13 appear above. The index and the tree still disagree: `infographic-creator`, `antvis-skills-maintainer` and `antv-s2-expert` have no directory at all, and `narrative-text-visualization` has no directory of its own either, since the closest match is `antv-t8-ntv`, whose heading reads Narrative Text Visualization Skill. That same skill is also indexed separately under its own name at 89 installs.

## Why This Matters for Hermes Agents

Asking an agent to chart something exposes two different failures. The first is the wrong chart type: a pie chart for a trend, a bar chart for a distribution, a stacked layout for data that is not additive. The second is code that renders nothing, because a charting library's API has moved between major versions and the model's memory is one version behind.

This pack addresses both. `chart-visualization` is explicit that it selects the chart type from 26+ options before it renders, with the type families written into the README (time series, comparison, part-to-whole, relationships, geographic, hierarchical, statistical, specialist), and `antv-g2-chart` carries guard rails against the v4 to v5 migration mistakes: deprecated chain APIs, invalid palette names, and referencing `d3` in user code.

The grammar-of-graphics framing is what makes the guidance transferable. G2's model of marks, transforms, scales and coordinates is the same model the skill teaches, so an agent that has read it can reason about a chart it has not seen rather than pattern-match a snippet. The G6 and X6 skills follow suit for graph layouts and editor diagrams, which are the two cases where a generic "draw a chart" prompt produces the least useful code.

There is a retrieval layer that changes the cost profile. The repository indexes its own reference corpus and exposes it three ways, an HTTP endpoint at `sive.antv.antgroup.com`, a CLI (`antv retrieve`) and a TypeScript `retrieve()` function with filters by library, `topK`, strategy and token budget. For a Hermes agent that needs one answer about a stacked bar, that is a targeted lookup rather than loading a skill body.

The honest limit is the network dependency, and it is worth stating up front. The most installed skill, `chart-visualization`, and the icon search skill `icon-retrieval` both do their work by calling a remote AntV service with curl. They are useful and they are not local.

## Usage

| You say | What happens |
|---|---|
| "Chart this quarterly revenue data" | chart-visualization picks a chart type that fits the data shape, extracts the parameters and returns a rendered image rather than a code snippet to debug. |
| "Write G2 v5 code for a stacked area chart with a slider" | antv-g2-chart answers with the encode, transform and interaction configuration, and avoids the v4 chain API that no longer exists. |
| "Show me this network as a force-directed graph" | antv-g6-graph covers the data structure, layout choice, node and edge styling and the behaviours for zoom and drag. |
| "Build a flowchart editor with custom HTML nodes" | antv-x6-editor covers the graph setup, the stencil and DnD plugins, HTML shapes and the serialisation path. |
| "Find me an icon for a billing settings panel" | icon-retrieval searches the icon service and returns up to 5 matching SVGs with their URLs and full markup. |
| "Turn this report into an infographic" | antv-infographic or antv-t8-ntv answers depending on the output: a visual summary from the template set, or a structured narrative with entity annotations. |
| "Emit a chart config my renderer can stream" | gpt-vis answers in Syntax mode, producing declarative configuration instead of imperative code. |

## Verification

The raw path below returned 200 on branch master when this guide was written on 2026-11-02:

```bash
curl -sL -o /dev/null -w "%{http_code} chart-visualization\n" \
  "https://raw.githubusercontent.com/antvis/chart-visualization-skills/master/skills/chart-visualization/SKILL.md"
```

After a clone, count what actually ships, since the install index lists 13 names against 9 directories:

```bash
git clone --depth 1 https://github.com/antvis/chart-visualization-skills.git /tmp/antv-chart-skills
ls /tmp/antv-chart-skills/skills
find /tmp/antv-chart-skills/skills -name SKILL.md | wc -l
grep -c curl /tmp/antv-chart-skills/skills/chart-visualization/SKILL.md
```

The directory listing should show nine folders: `antv-g2-chart`, `antv-g6-graph`, `antv-gpt-vis`, `antv-infographic`, `antv-t8-ntv`, `antv-x6-editor`, `chart-visualization`, `gpt-vis` and `icon-retrieval`. The count should print 9, and the `grep` should return a non-zero number of `curl` mentions, which is the remote API dependency stated plainly in the file rather than buried in prose.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| chart-visualization | Pass | Pass | Pass |
| narrative-text-visualization | Pass | Warn | Pass |
| antv-g6-graph | Pass | Pass | Pass |
| gpt-vis | Pass | Pass | Warn |
| antv-t8-ntv | Pass | Pass | Warn |

No sampled listing fails Gen Agent Trust Hub, which is the scan that reads what a skill instructs an agent to do. Three of the five carry a warn: `narrative-text-visualization` on Socket, and `gpt-vis` plus `antv-t8-ntv` on Snyk.

The behaviour behind the verdicts is straightforward. The skills are Markdown, 11 files across 9 directories, and installing them runs nothing. What they instruct the agent to do is the part worth reading: `chart-visualization` renders by calling the AntV API through curl, and `icon-retrieval` searches an icon service over HTTP, so both send the data in your prompt to a third-party endpoint and receive image or SVG content back. The README documents that endpoint as `https://sive.antv.antgroup.com/api/v1/context/retrieve` and offers no local-only alternative for the rendering path.

That is a data-egress decision, not a code-execution risk. If the chart input contains customer figures, identifiers or anything else that should not leave the machine, use the code-generating skills (`antv-g2-chart`, `antv-g6-graph`, `antv-x6-editor`, `gpt-vis`) which produce code you run yourself, rather than the rendering skills.

The licence is MIT with a `LICENSE` file in the root, so the reuse terms are stated rather than implied. The README's contribution note is unusual and worth knowing: it states that the project only merges AI-generated code, and asks contributors to file an issue and assign it to Copilot rather than open a pull request by hand.

## Limitations

- Snapshot data, verified 2026-11-02: 18,128 combined installs across 13 indexed listings; 524 GitHub stars; MIT; last pushed 2026-09-22. Counts drift over time.
- The index outruns the tree. 13 indexed listings sit against 9 directories: `infographic-creator`, `antvis-skills-maintainer` and `antv-s2-expert` have no directory in the current repository, and `narrative-text-visualization` has no directory of its own, with `antv-t8-ntv` as the closest match and a separate listing at 89 installs.
- Two skills depend on a remote service. `chart-visualization` and `icon-retrieval` call AntV endpoints with curl, so they need network access and they send prompt data off the machine.
- Language is mixed. The `chart-visualization` and `gpt-vis` skill descriptions are written in Chinese while `antv-g2-chart`, `antv-g6-graph` and `antv-x6-editor` are in English, so trigger matching varies with the assistant's handling of non-English frontmatter.
- The accuracy figures in the README (up to 98.2 percent on G2, 97.9 on G6 across 174 cases) are the vendor's own evaluation against a Context7 baseline, not an independent benchmark.
- The security sample is five skills out of the 13 listings, and it mixes tree directories with two index-only names, so it does not cover `antv-gpt-vis`, `antv-infographic` or `antv-x6-editor`.

## Related

- [Design Doc Mermaid Skill - Diagram & Documentation Setup](/hermes/skills/catalog/design-doc-mermaid-setup)
- [Markdown Viewer Skills - Diagrams, Charts and Cards Setup](/hermes/skills/catalog/markdown-viewer-skills-setup)
- [Motion Design Skill - LottieFiles Animation Setup](/hermes/skills/catalog/lottiefiles-motion-design-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Decide the output before choosing the skill. `chart-visualization` returns an image, `antv-g2-chart` returns code you own, and the difference decides whether your data leaves the machine.
- Read the G2 skill's guard rails even when you are not using G2. The v4 to v5 migration list (deprecated chain APIs, invalid palette names, stray `d3` references) is the same class of mistake an agent makes with any charting library.
- Install `gpt-vis` or `antv-gpt-vis`, not both. They are the same skill in two languages, and having both in a profile gives the agent two routes to one answer.
- Use `antv retrieve` when you need one fact. A CLI query against the indexed corpus with `--library g2 --topk 5` is cheaper than loading a skill body for a single API question.
- Check the tree before trusting a listing. Four of the 13 names on skills.sh resolve to no directory of the same name, so a copy that claims to have installed "all" of them has installed nine.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
