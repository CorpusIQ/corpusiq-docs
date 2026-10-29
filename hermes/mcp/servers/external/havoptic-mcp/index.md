---
title: "Havoptic MCP - AI Coding Tool Release Intelligence"
description: "See what Claude Code, Codex, Cursor and the other coding agents shipped, what breaks on upgrade, and which tool shipped a feature first."
category: DevOps
stars: ★★★ (200 keyless, 15 tools verified)
added: 2026-10-28
source: "live probe of https://mcp.havoptic.com/mcp answering HTTP 200 keyless on initialize as havoptic 2.1.0 on protocol 2025-06-18 with a full tools/list of 15 tools (4 marked deprecated, 11 current), found on the mcpservers.org /all listing, and the vendor site mcp.havoptic.com"
relevance: ★★★
tags: [developer-tools, release-notes, breaking-changes, upgrade, claude-code, codex, cursor, keyless, remote-mcp]
last_updated: "2026-10-28"
---

# Havoptic MCP

**The tools an engineering team codes with now ship faster than anyone can read. The upgrade that breaks the build is usually documented, in a changelog nobody opened.**

```
Server type: Remote (Streamable HTTP), keyless
Endpoint:    https://mcp.havoptic.com/mcp
Auth:        None, read-only
Server:      havoptic 2.1.0, protocol 2025-06-18
Tools:       15 at tools/list, 4 of them deprecated aliases
Tracking:    Claude Code, Codex CLI, Cursor, Gemini CLI, Kiro CLI, Copilot CLI, Devin Desktop, agent SDKs, inference runtimes
Pricing:     Free
```

## Why This Matters for Operators

A team that standardises on Claude Code, Codex and Cursor is running three release trains it does not control. A flag gets renamed, a hook changes shape, a permission model tightens, and the first sign is a broken workflow on a Monday. The information exists, inside three changelogs, in prose, released weekly.

This server turns the changelogs into typed questions: what changed since this date, what breaks between these two versions, which tool shipped a capability first and how far behind the others are, and how fast each vendor ships at all. `whats_changed_since` accepts relative windows like `7d` and `30d` and groups the answer by tool with breaking changes first, which is the shape of a Monday morning question rather than the shape of a changelog.

It is adjacent to the catalogue's `Versionly` entry and distinct from it: Versionly watches the vendor changelogs a company's own code depends on, from a GitHub App against selected repos. Havoptic tracks the assistant and agent tooling itself, across vendors, with feature-adoption timing and an editorial comparison.

## What It Returns, Verified

A bare `initialize` on `https://mcp.havoptic.com/mcp` returned **HTTP 200** with no credential as `havoptic` **2.1.0** on protocol `2025-06-18`. `tools/list` returned **fifteen tools**: eleven current and four kept as deprecated aliases that point at their successors, which is itself a useful signal about how the vendor handles its own surface.

The eleven current tools:

- **`list_tools`** is the catalogue of tracked products: AI coding tools plus model and API platforms, agent SDKs and inference runtimes, with release counts.
- **`get_latest_releases`** returns the newest releases across one or all tracked tools, with a `since` and `until` window.
- **`whats_changed_since`** returns typed changes, breaking, security, features and fixes, grouped by tool with breaking changes first.
- **`search_changes`** is full-text search across typed change items and legacy release notes, for a flag, an error string, a config key or a feature name.
- **`get_release`** takes a release id such as `claude-code@2.1.183` or a tool plus version, with a full-detail mode.
- **`get_upgrade_notes`** returns everything between two versions of one tool, including an explicit coverage gap where legacy releases carry no typed changes.
- **`get_breaking_changes`** lists breaking changes and deprecations across tools in a window, 30 days by default.
- **`compare_tools`** compares two to four tools on release cadence, feature-matrix differences and recent changes.
- **`feature_adoption`** answers who shipped a cross-tool feature first, such as MCP support, subagents, planning mode, hooks or checkpoints, and the lag in days for the rest.
- **`cadence_stats`** gives release counts over 7, 30 and 90 days, average days between releases and the last release.

## Limits Worth Recording

Read-only, so it informs decisions and changes nothing. The typed changes and the coverage gap matter more than the release count: the vendor states that legacy releases without typed changes are counted separately rather than silently treated as change-free, which is the honest shape and worth checking before anyone concludes a version was quiet. This tracks the assistant and coding-agent tooling layer, not the wider SDK and cloud changelog space, so `Versionly` remains the entry for a company's own dependency surface.

## FAQ

### Do I need an API key?
No. All fifteen tools answer without a credential, which is how this entry was verified.

### Which tools are tracked?
AI coding tools including Claude Code, Codex CLI, Cursor, Gemini CLI, Kiro CLI, GitHub Copilot CLI and Devin Desktop, plus model and API platforms, agent SDKs and inference runtimes.

### Can it tell me what breaks when I upgrade?
Yes. `get_upgrade_notes` returns everything between two versions of one tool with breaking changes, deprecations, security fixes, features and fixes, and `get_breaking_changes` does the same across tools in a window.

### Does it tell me which tool shipped a feature first?
Yes. `feature_adoption` answers who shipped a cross-tool feature first and how many days behind the others were, and `compare_tools` compares two to four tools including cadence.

### How is this different from Versionly in this catalogue?
Versionly watches the vendor changelogs your repositories depend on, through a GitHub App against selected repos. This tracks the coding assistants and agent tooling themselves across vendors, including cross-tool feature timing.
