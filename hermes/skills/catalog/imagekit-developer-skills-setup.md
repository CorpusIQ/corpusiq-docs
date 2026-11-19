---
title: "ImageKit Developer Skills - MCP and Agent Skills Setup"
description: "imagekit-developer/skills: 4.0K combined installs across 9 listings; official ImageKit MCP servers and agent skills for DAM, Admin, and DevTools."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/imagekit-developer-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "imagekit", "mcp", "media library"]
---

# ImageKit Developer Skills - Setup Guide

**Source:** [imagekit-developer/skills](https://www.skills.sh/imagekit-developer/skills) via skills.sh - 4.0K combined installs across 9 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 morning sweep)
**GitHub:** 2 stars, MIT licence, `main` branch, last pushed 2026-10-09. Eight skills under `skills/`, a Claude Code plugin under `.claude-plugin/`, and a `.mcp.json` listing the bundled MCP servers.
**Category:** Media management and MCP
**Quality Tier:** 🟡 Yellow - 3 Warns among 9 sampled skills (search-docs, mcp-preflight, imagekit-integrations); MIT licence.

ImageKit Developer Skills is the official ImageKit skill pack for coding agents. It pairs agent skills with three hosted MCP servers - DAM (media library), Admin (origins, URL endpoints, usage), and DevTools (docs search and transformation URLs) - so an agent can upload, organize, transform, and share images without inline file bytes or hand-built transformation URLs.

The install index reports 9 listings against the 8 skill directories in the current tree. `imagekit-sdk-reference` (357 installs) was the TypeScript SDK reference for `@imagekit/nodejs`, removed from the repository on 2026-09-10 when the skills moved to the MCP-first path; it no longer has a `skills/` directory in the current tree.

## Installation

There are two pieces: the skills and the MCP servers. On Claude Desktop, Claude.ai (web), and VS Code, the plugin installs both in one step: add the `imagekit-developer/skills` marketplace, install the ImageKit plugin, and enable the bundled `imagekit_devtools`, `imagekit_dam`, and `imagekit_admin` connectors (authenticate DAM and Admin when prompted).

Manually, install the skills:

```bash
npx skills add imagekit-developer/skills --all
```

Then add the three MCP servers. For Claude Code:

```bash
claude mcp add --transport http imagekit_devtools https://devtools-mcp.imagekit.io/mcp
claude mcp add --transport http imagekit_dam https://imagekit.io/mcp/dam
claude mcp add --transport http imagekit_admin https://imagekit.io/mcp/admin
```

DevTools needs no sign-in; DAM and Admin sign in with your ImageKit account. Restart your editor after installing.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| upload-files | 523 | Upload files to the ImageKit media library via DAM MCP: bulk upload signatures from a shell or the interactive picker. |
| transformation-builder | 518 | Build ImageKit image and video transformation URLs: resize, crop, AI edits, overlays, effects, and video transforms. |
| search-docs | 518 | Query ImageKit documentation through search_docs: query rewriting, source selection, and result handling. |
| mcp-preflight | 516 | Route to the right ImageKit MCP server (DAM, Admin, or DevTools) before any MCP call. |
| ai-tasks | 514 | Apply AI-powered analysis to images for tagging, metadata extraction, and quality checks with controlled vocabularies. |
| imagekit-integrations | 482 | Index of ImageKit SDKs, plugins, and integrations to find the right one for a stack, then query docs for detail. |
| search-assets | 475 | Lucene searchQuery cheatsheet for DAM search_media_library: describe assets in everyday language and build filters. |
| imagekit-sdk-reference | 357 | TypeScript SDK reference for @imagekit/nodejs: method signatures, parameter and return types, and error handling for application code (removed from the tree on 2026-09-10). |

The remaining 1 indexed listing is asset-access-control (121 installs), sharing and revoking access on ImageKit files, folders, and media collections.

## Why This Matters for Hermes Agents

For an agent operating an ImageKit account, the failure modes are concrete: sending file bytes into the conversation, calling the wrong MCP server, or assembling a transformation URL by memory. These skills are routing and cheatsheets that sit in front of the MCP tools, so the agent picks the right server and query before it acts.

The `mcp-preflight` skill is the entry point: it maps DAM, Admin, and DevTools to their responsibilities so the agent never guesses which server to call. Because the skills are plain `SKILL.md` files and the servers are standard HTTP MCP endpoints, the setup works across Claude, VS Code Copilot, Codex, Cursor, Windsurf, and other MCP clients.

## Usage

| You say | What happens |
|---|---|
| "Upload these files to ImageKit" | upload-files routes to DAM create_upload_signatures_in_bulk from a shell, or the upload_file picker. |
| "Crop this image to 800x600" | transformation-builder produces the correct transformation URL via the DevTools tool. |
| "How do I search the docs for overlays?" | search-docs rewrites the query and selects the right sources for search_docs. |
| "Who can see this asset?" | asset-access-control reads the ACL via DAM and reports READ, CONTRIBUTE, or MANAGE access. |
| "Find my spring campaign assets" | search-assets turns everyday language into a Lucene searchQuery for search_media_library. |
| "Which MCP server handles usage analytics?" | mcp-preflight routes the question to Admin. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/imagekit-developer/skills/main/skills/upload-files/SKILL.md
```

Then install the pack and the MCP servers, restart your editor, and ask your agent to list the media library.

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| upload-files | Pass | Pass | Pass |
| transformation-builder | Pass | Pass | Pass |
| search-docs | Pass | Pass | Warn |
| mcp-preflight | Pass | Pass | Warn |
| ai-tasks | Pass | Pass | Pass |
| imagekit-integrations | Pass | Pass | Warn |
| search-assets | Pass | Pass | Pass |
| imagekit-sdk-reference | Pass | Pass | Pass |
| asset-access-control | Pass | Pass | Pass |

The sample covers all 9 indexed listings; three carry a Warn (search-docs, mcp-preflight, imagekit-integrations). DAM and Admin require your ImageKit account credentials, so treat the account scope before granting agent access.

## Limitations

- Snapshot data, verified Nov 19, 2026: 4,024 combined installs across 9 indexed listings; 2 GitHub stars; MIT licence; last pushed 2026-10-09. Counts drift over time.
- The install index outruns the repo tree: 9 indexed listings against 8 skill directories. imagekit-sdk-reference (357 installs) has no `skills/` directory in the current tree; it was removed on 2026-09-10 as the skills moved to an MCP-first path.
- DAM and Admin MCP servers require signing in with an ImageKit account; DevTools needs no sign-in.
- The repo previously exposed a retired API MCP (`https://api-mcp.imagekit.io/mcp`); remove it and add DAM and Admin instead.

## Related

- [ImageGen Skills - Design Images for Coding Agents](/hermes/skills/catalog/imagegen-skills-setup)
- [MCP Client - MCP Client Operations Setup](/hermes/skills/catalog/mcp-client-setup)
- [Generative Media Skills - 153-Skill Media Production Suite Setup](/hermes/skills/catalog/generative-media-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read mcp-preflight first; it is the routing guide every other skill assumes.
- For bulk uploads, prefer create_upload_signatures_in_bulk from a shell; never inline file bytes into the conversation.
- After install, restart the editor so the MCP servers take effect, then authenticate DAM and Admin when prompted.
- Build transformation URLs through transformation-builder rather than typing parameters by hand.
- The retired API MCP is replaced by DAM and Admin; if you still have `api-mcp` connected, remove it.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
