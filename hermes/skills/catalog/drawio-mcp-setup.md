---
title: "draw.io MCP - Diagram Authoring Setup"
description: "Official draw.io MCP server: 3.4K combined installs for the drawio skill, authoring editable diagrams, PNG/SVG/PDF exports and browser URLs"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/drawio-mcp-setup/"
robots: "index,follow"
last_updated: "2026-11-10"
tags: ["hermes skill", "agent skill", "skill setup", "drawio", "mcp server", "diagramming", "architecture diagrams"]
---

# draw.io MCP - Setup Guide

**Source:** [jgraph/drawio-mcp](https://www.skills.sh/jgraph/drawio-mcp) via skills.sh - 3.4K combined installs across 1 indexed listing (3,421 exact); first seen 2026-02-22 (Nov 10, 2026 sweep)
**GitHub:** 5,809 stars, Apache-2.0 license, `main` branch, last pushed 2026-11-10, 339 blobs and 5 `SKILL.md` files, the same `drawio` skill packaged once per client under `plugins/antigravity/skills/drawio/`, `plugins/claude-code/skills/drawio/`, `plugins/codex/drawio/skills/drawio/`, `plugins/copilot/skills/drawio/` and `plugins/cursor/skills/drawio/`
**Category:** Diagramming: architecture, flowcharts and diagram files authored through the draw.io MCP server
**Quality Tier:** 🟡 Solid with caveats - official vendor repository, Apache-2.0, pushed on the sweep date, with one Snyk Warn on its single indexed listing and a hosted endpoint that receives the diagram XML.

This is draw.io's own MCP server, published by jgraph rather than a community wrapper, and the repository is really four products behind one name. The hosted MCP App Server at `mcp.draw.io` renders a diagram inline in the conversation. The MCP Tool Server, published as `@drawio/mcp`, opens the diagram in the draw.io editor instead. The assistant plugins generate `.drawio` files locally with optional export. The fourth route needs no server at all and teaches a Claude Project to build draw.io URLs from Python.

The skills.sh index sees one skill named `drawio` with 3,421 installs, because all five client plugins ship the same skill text. That compression hides the interesting part: the skill's own description tells the agent when NOT to use it. In a chat that renders diagrams inline, and where the `create_diagram` tool is available, the correct move is the MCP tool. In Claude Code, Codex, Copilot CLI and their IDE extensions, nothing renders inline, so the skill takes over and writes files.

For an agent workflow the distinction is the whole point. A diagram that appears in the conversation is a preview, not an artifact. A `.drawio` file is editable, diffable, reviewable, and exports to PNG, SVG or PDF with the diagram XML embedded so the export stays editable in draw.io.

## Installation

The hosted MCP App Server needs no installation. Add the endpoint as a remote HTTP MCP server in any MCP Apps host:

```
https://mcp.draw.io/mcp
```

GitHub Copilot CLI takes it from the terminal, where the tool still works but answers with a link instead of an inline viewer:

```bash
copilot mcp add --transport http drawio https://mcp.draw.io/mcp
```

The stdio tool server is an npm package and opens diagrams in the draw.io editor:

```bash
npx @drawio/mcp
```

The plugin route is per client, all from the same marketplace repository. Claude Code:

```
/plugin marketplace add jgraph/drawio-mcp
/plugin install drawio@drawio
```

Codex CLI, GitHub Copilot CLI and Antigravity:

```bash
codex plugin marketplace add jgraph/drawio-mcp
codex plugin add drawio@drawio

copilot plugin marketplace add jgraph/drawio-mcp
copilot plugin install drawio@drawio

agy plugin install https://github.com/jgraph/drawio-mcp/tree/main/plugins/antigravity
```

Cursor installs from its own Marketplace (Customize, then drawio, then Install), or by copying `plugins/cursor` to `~/.cursor/plugins/local/drawio` and reloading the window. For a host with no plugin system, the README notes that OpenCode reads skills from `.claude/skills/` and takes the Claude Code skill folder as-is, so copying `plugins/claude-code/skills/drawio/` into the agent skills directory is the portable route. Nothing about that install touches the MCP servers; the skill writes files and shells out to the draw.io Desktop CLI.

## What It Provides

The single indexed listing clears the 500-install threshold and appears below:

| Skill | Installs | Use For |
|---|---|---|
| drawio | 3,421 | Creates diagrams as native .drawio files from Mermaid or draw.io XML, with optional ELK auto-layout, PNG/SVG/PDF export with the XML embedded, or a browser URL; defers to the MCP create_diagram tool where the chat renders diagrams inline. |

No indexed listings fall below the threshold. The single listing covers five install layouts, one per client plugin, not one skill per client.

The skill text itself is short and opinionated about authoring format. Mermaid is the recommended path for flowcharts, sequence, class, state, ER, gantt, mindmap, timeline, user journey, quadrant, C4, git graph and pie charts, because the draw.io Desktop CLI converts it and lays it out, which the skill calls far more reliable than hand-positioning cells in XML. Raw XML is for custom styling, precise placement, specific shape libraries such as AWS, Azure, network or detailed UML, and for machines where the desktop CLI is not installed.

## Why This Matters for Hermes Agents

Diagrams are one of the few deliverables an agent can produce that a human actually reads in a meeting. The failure mode is well known: a plausible box-and-arrow Mermaid block that renders unreadable, or an ASCII sketch pasted into a markdown file that nobody can edit afterwards.

This repository fixes the output format rather than the aesthetics. The agent writes `.drawio` XML or Mermaid, and draw.io does the layout and rendering, so the result opens in an editor the team already has. The ELK pass and the libavoid routing pass exist for the same reason: hand-routed connectors are where generated diagrams look machine-made.

The tool surface is narrow on purpose. `create_diagram` renders XML or Mermaid (28 diagram types) inline in chat. `search_shapes` searches 10,000+ shapes across the draw.io libraries (AWS, Azure, GCP, P&ID, electrical, Cisco, Kubernetes, UML, BPMN and others) and returns exact style strings for the XML, which is what stops an agent inventing a shape name that draw.io will not resolve. `get_drawio_reference` returns the XML or Mermaid generation reference the model should read once per format before its first diagram.

The choice between the two servers matters for a terminal-first agent. In a host that cannot render inline, the tool server's link and the skill's local file are the only usable outputs, and the skill is the one that produces something reviewable in a pull request.

## Usage

| You say | What happens |
|---|---|
| "Draw the refund flow for support" | The skill authors a Mermaid flowchart and the desktop CLI converts it to a `.drawio` file, then opens it in draw.io |
| "Diagram our AWS setup with the real AWS shapes" | `search_shapes` returns exact style strings from the AWS library, then `create_diagram` renders the XML where the host supports inline diagrams, or the skill writes the file where it does not |
| "Make an ER diagram from these tables" | Mermaid or XML is generated from the schema description, with entities and relations laid out by the converter rather than positioned by hand |
| "Export it as SVG for the docs site" | The plugin routes the export through the local draw.io Desktop CLI with `--embed-diagram`, so the SVG stays editable when reopened |
| "Give me a link instead of a file" | The `url` output mode compresses the XML with Node's zlib and opens it at `app.diagrams.net`, keeping a `.drawio` copy locally |
| "This layout is a mess, re-space it" | The ELK auto-layout pass (`postLayout: "elk"`) re-arranges nodes into a layered layout and routes the edges with them |
| "Keep my positions but tidy the arrows" | libavoid routing (`routing: "libavoid"`) reroutes connectors orthogonally around the shapes without moving any node |

## Verification

Every client path resolves to a raw `SKILL.md` on `main`. This one returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/jgraph/drawio-mcp/main/plugins/claude-code/skills/drawio/SKILL.md | head -3
```

It should print the frontmatter delimiter, then `name: drawio`, then a quoted description beginning `Always use when user asks to create, generate, draw, or design a diagram`. The other four layouts sit at `plugins/antigravity/skills/drawio/`, `plugins/copilot/skills/drawio/` and `plugins/cursor/skills/drawio/`, with the Codex copy one level deeper at `plugins/codex/drawio/skills/drawio/`. All five returned 200 on 2026-11-10.

After an install, confirm the skill landed as a directory holding `SKILL.md`:

```bash
test -f ~/.claude/skills/drawio/SKILL.md && echo ok
```

For the plugin routes, check the plugin listing in the client instead, because the bundle lives in that client's plugin cache rather than the skills directory. For the export path, `which drawio` is the honest check: if the desktop CLI is absent, the `.drawio` file is still written and the export silently does not happen.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-10) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| drawio | Pass | Pass | Warn |

One listing, and Snyk warns on it. The other two scanners pass. A Snyk Warn on a skill that runs a local export command is unsurprising: the skill shells out to the draw.io Desktop CLI and writes files into the working directory, so a prompt that names an absolute output path will write outside the project.

The larger consideration is not scanner-grade at all, it is data residency, and the README is unusually explicit about it. The hosted App Server at `mcp.draw.io` sends the diagram to draw.io's server as the MCP request. Self-hosting (local Node, the `jgraph/drawio-mcp` Docker image, or your own Cloudflare Worker) keeps it local. The stdio tool server carries the diagram in the URL `#fragment`, which browsers do not transmit. The plugins write locally and export with the local CLI. Nothing in the repository calls a cloud rasterizer, and there is no fallback to one when a local dependency is missing.

Two residual network facts worth knowing before you call a deployment air-gapped: the viewer loads its code from `viewer.diagrams.net` unless built with `VIEWER_PATH`, and `search_shapes` queries `icons.diagrams.net` unless `DRAWIO_ICON_SERVICE_URL=off`. Both fetch application code and assets, not your diagram. And the diagram is generated by the LLM, so a hosted model means the content is produced in that provider's cloud regardless of where this server runs.

## Limitations

- Snapshot data, verified 2026-11-10: 3,421 combined installs across 1 indexed listing; 5,809 GitHub stars; Apache-2.0 license; last pushed 2026-11-10. Counts drift over time.
- The index measures a skill name, not client coverage. One listing maps to five `SKILL.md` files, so install counts say nothing about which host the installer used, and the plugin READMEs are the only per-client source.
- Behaviour differs by host in a way that is easy to miss. In an inline-rendering chat the skill's own description says to call `create_diagram` instead, so the same prompt produces a preview there and a file from a terminal.
- PNG, SVG and PDF export needs the draw.io Desktop CLI on the machine (located via `which drawio`), and Mermaid conversion needs the same CLI. Without it you get `.drawio` files only, with no error beyond a missing export.
- The hosted App Server route sends diagram content to draw.io. The README documents self-hosting as the fix, which means running Node, Docker or a Cloudflare Worker yourself before any sensitive architecture diagram goes through it.
- Snyk warns on the single listing. The scanners read skill text, not the shell commands an agent composes with it, so the export path deserves a manual read.

## Related

- [Diagram Design - Editorial HTML and SVG Diagrams](/hermes/skills/catalog/diagram-design-setup)
- [Markdown Viewer Skills - Diagrams, Charts and Cards Setup](/hermes/skills/catalog/markdown-viewer-skills-setup)
- [Archify - Interactive Architecture Diagram Skill Setup](/hermes/skills/catalog/archify-setup)

## Pro Tips

- State the output format in the prompt. "as a .drawio file", "export SVG", "give me a url" each select a different code path, and the default is a file that opens in draw.io.
- Ask for `search_shapes` before a vendor diagram. The AWS, Azure and Kubernetes libraries have exact style strings, and an agent that guesses a shape name produces a diagram that renders as a plain box.
- Let the layout pass do the routing. ELK re-arranges nodes and routes its own edges, so adding libavoid on top is redundant; use libavoid alone when you placed the nodes deliberately.
- Prefer Mermaid unless you need styling. The desktop CLI conversion is more predictable than hand-positioned XML, and the skill says so in its own authoring table.
- Keep the `.drawio` file in the repository next to the code it describes. The exports are for reading, the `.drawio` file is the thing a human can still change next quarter.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
