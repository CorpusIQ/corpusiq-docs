---
title: "Drawio Skills - Diagram Authoring for Agents"
description: "bahayonghang/drawio-skills on skills.sh: 9.6K combined installs across 2 listings; YAML-first draw.io authoring, export and academic figure skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/drawio-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "diagrams", "drawio", "architecture"]
---

# Drawio Skills - Setup Guide

**Source:** [bahayonghang/drawio-skills](https://www.skills.sh/bahayonghang/drawio-skills) via skills.sh - 9.6K combined installs across 2 indexed listings; first documented November 4, 2026 (morning sweep)
**GitHub:** 299 stars, MIT licence, last pushed 2026-09-08, 2 SKILL.md directories under skills/
**Category:** Diagrams for agents: draw.io XML authoring, layout rules and export workflows for architecture and flow documents
**Quality Tier:** 🟢 Green: both indexed skills pass Gen Agent Trust Hub, Socket and Snyk, the repository ships an MIT LICENSE at the root and the source is plain YAML plus a local CLI

This is a two-part draw.io package built around one opinion: the diagram should be generated offline from YAML, not drawn through a browser session. The README calls the default path `YAML/CLI -> .drawio + sidecars`, with draw.io Desktop as an optional step for PNG, PDF, JPG and embedded SVG export.

The two skills split cleanly. `skills/drawio` is the base skill and owns the execution primitives: the CLI, schemas, references, themes, palettes, style presets, export helpers and a diagrams.net URL fallback. `skills/drawio-academic-skills` is a publication overlay that owns venue policy and paper assets, and it calls the base skill's CLI rather than shipping a second runtime.

## Installation

The standard route is the skills CLI:

```bash
npx skills add bahayonghang/drawio-skills
```

Restart the client afterwards so it reloads the skill list.

For a manual install, clone the repo and copy the base skill into the client's skill directory:

```bash
git clone https://github.com/bahayonghang/drawio-skills.git
cp -r drawio-skills/skills/drawio ~/.codex/skills/
```

If you need the publication overlay, copy `skills/drawio-academic-skills` next to `drawio` in the same directory, because the overlay resolves its sibling `../drawio` for execution. The README lists the common locations as `~/Library/Application Support/Claude/skills/` and `~/.config/Claude/skills/` for Claude, and `~/.codex/skills/` for Codex.

Live browser refinement is optional and off by default. Only add `@next-ai-drawio/mcp-server` when you want the base skill to iterate in a browser:

```json
{
  "mcpServers": {
    "drawio": {
      "command": "npx",
      "args": ["--yes", "@next-ai-drawio/mcp-server@latest"]
    }
  }
}
```

## What It Provides

Two listings carry the whole install base, and both clear the threshold.

| Skill | Installs | Use For |
|---|---|---|
| drawio | 8,619 | YAML-first creation, editing, replication and import of draw.io diagrams: architectures, network topologies, flowcharts, UML and ER, org charts, Mermaid and CSV conversion, existing .drawio bundles, 7 themes and 15 palettes |
| drawio-academic-skills | 1,009 | Publication figures for papers, theses and IEEE or ACM submissions: venue and audience preflight, figure typing into architecture, roadmap or workflow, caption and legend checks, formula fidelity and A4, Word or LaTeX expectations |

No indexed listings fall below the threshold; all 2 appear above.

## Why This Matters for Hermes Agents

Diagram output is where agent-written documentation usually falls apart: a Mermaid diagram that renders in one viewer and breaks in another, or an architecture sketch with no stable identity, so every regeneration is a fresh guess.

This package keeps a canonical bundle instead. A diagram ships as `.drawio` plus `.spec.yaml` plus `.arch.json`, and the CLI can validate the YAML before it renders, so an agent edits a spec rather than hand-tuning XML.

The importers are the part that changes what an agent can do with a repository it is already reading. Terraform, Kubernetes manifests, Compose files, SQL DDL, OpenAPI specs, GitHub Actions and GitLab CI can all be turned into a diagram offline, with no provider CLI, no Graphviz and no network.

For publication work the overlay adds a policy layer that a general agent will not supply on its own: which figure type fits which venue, and what a camera-ready caption has to carry.

## Usage

| You say | What happens |
|---|---|
| "Create a horizontal login flow with six nodes" | drawio generates the YAML spec, renders the .drawio file and keeps the sidecars aligned |
| "Diagram our network with a firewall, a core switch and two app servers" | drawio uses semantic device types and fills link labels from interface, IP, VLAN and bandwidth metadata |
| "Turn these Terraform files into an architecture diagram" | the config-import route normalizes the Terraform input and renders it offline |
| "Map the module relationships in this Python repo" | the code-import route reads the local directory and renders module and class relationships |
| "Import our existing diagram and give me an editable spec" | the CLI converts the .drawio file into a YAML bundle with --input-format drawio --export-spec |
| "Export this as a PNG for the deck" | the CLI renders through draw.io Desktop with --use-desktop |
| "Make an IEEE-style workflow figure for the manuscript" | drawio-academic-skills applies venue gates and delivers the bundle plus standalone SVG |

## Verification

Fetch the base skill file and confirm the frontmatter and route list are present:

```bash
curl -fsSL https://raw.githubusercontent.com/bahayonghang/drawio-skills/main/skills/drawio/SKILL.md | head -20
```

Then render one of the shipped example specs, which the README uses as its representative network case:

```bash
node skills/drawio/scripts/cli.js skills/drawio/references/examples/vendor-device-mapping.yaml output.drawio --validate --write-sidecars
```

A `.drawio` file plus matching `.spec.yaml` and `.arch.json` next to it confirms the CLI, the schemas and the renderer all work. If the overlay was installed, repeat the fetch against `skills/drawio-academic-skills/SKILL.md` and check that `../drawio` exists in the same parent directory.

## Security

skills.sh verdicts for sampled skills (verified November 4, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| drawio | Pass | Pass | Pass |
| drawio-academic-skills | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified November 4, 2026: 9,628 combined installs across 2 indexed listings; 299 GitHub stars; MIT licence; last pushed 2026-09-08. Counts drift over time.
- PNG, PDF and JPG export depends on draw.io Desktop being installed. Without it the CLI reports those outputs as unavailable rather than failing silently.
- The academic overlay is not standalone: it requires the sibling `../drawio` directory, so a partial copy breaks publication workflows.
- The README directs faithful replication of existing draw.io diagrams at a separate project on its dev branch rather than at this package, so treat the replicate route here as structural redraw rather than pixel matching.
- Six postprocess operations ship (`mermaid`, `explain`, `relabel`, `restyle`, `heatmap`, `html`); the README names runbook, animated SVG, tube and sequence layout, compression, buildup, PPTX, timelapse and PR diff as deferred.
- Multi-page bundles and local PNG or JPEG assets are v1 features with limits: SVG assets and multi-page `assets` blocks are out of scope.

## Related

- [Diagram Design - Editorial HTML and SVG Diagrams](/hermes/skills/catalog/diagram-design-setup)
- [Architecture Diagram - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/architecture-diagram-setup)
- [Markdown Viewer Skills - Diagrams, Charts and Cards Setup](/hermes/skills/catalog/markdown-viewer-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Keep the three-file bundle together. Regenerating from the spec gets the same diagram back; editing the `.drawio` by hand and dropping the spec is how the identity drift starts.
- Run the validate step before every export. It catches structure and layout problems while they are still cheap to fix in YAML.
- Prefer the offline importers for anything already declared in the repo. Reading Terraform or a Compose file is more reliable than asking the agent to describe the architecture from memory.
- Install the overlay only if you write papers. For product docs the base skill carries everything, and the overlay adds policy you will not use.
- Skip the MCP server until you need browser refinement. The offline path is the documented default and keeps the bundle canonical.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
