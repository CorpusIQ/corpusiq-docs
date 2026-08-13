---
title: "MCP Directory Submission Guide — Where to List a Server in 2026"
description: "Field-tested walkthrough of every major MCP directory: free vs paid, form vs GitHub, sign-in requirements, and what actually works. Updated August 2026 from real submissions."
category: "MCP"
tags: ["mcp", "directory", "submission", "listing", "discovery", "registry", "marketing"]
last_updated: "2026-08-13"
canonical: "https://www.corpusiq.io/docs/hermes/mcp/directories/submission-guide-2026/"
robots: "index,follow"
---

# MCP Directory Submission Guide — 2026

A server only helps developers who can find it. This guide documents every major MCP directory, how submission actually works (field-tested August 2026), and what each one costs in effort.

## Tier 1 — Auto-indexed from the Official Registry

The official Model Context Protocol registry at registry.modelcontextprotocol.io feeds many directories automatically. If your server is in the registry, several directories pick it up without a manual submission. Reverse-DNS naming (io.yourorg.your-server) is the registry standard.

Directories that mirror the official registry include mcpservers.org and several aggregator mirrors. Being listed there gives you multilingual coverage (English, Russian, Simplified Chinese, Traditional Chinese, and more) with zero manual work.

## Tier 2 — Free web forms

| Directory | Method | Notes |
|-----------|--------|-------|
| FutureTools.io | Web form + Cloudflare Turnstile | Human-curated by Matt Wolfe. Turnstile can auto-pass in a real browser. Finance and Sales categories exist. ~3M visits per month |
| MCP.Directory | Web form, paste GitHub repo URL | Auto-pulls name, description, stars, and README. Auto-detects tools and generates install configs for Cursor, Claude, VS Code, Codex. Review about 24 hours |
| Stork.AI | Web form, paste repo or remote endpoint | Runs a real MCP handshake in their Test Lab on submit. Requires sign-in (Google or GitHub) |
| Glama.ai | Add Server button | Large registry (70,000+ servers). Requires account creation |
| MCP Server Space | Web form | Requires Google or GitHub OAuth sign-in |
| AgenticSkills.io | Web form | 200+ servers, security-audit focused. Review about 48 hours. Their backend can be flaky |

## Tier 3 — GitHub-based

| Directory | Method | Notes |
|-----------|--------|-------|
| mcpservers.org | GitHub PR or website form | De facto standard directory. Also pulls from the official registry |
| Developers Digest MCP Directory | GitHub issue or PR | Template: server name, GitHub URL, description, install command, category, tags. Their submission repo link returned 404 in August 2026 — email the maintainers if that happens |
| Cursor Directory | GitHub PR or website | Popular for Cursor-focused tooling |
| MCPHub | GitHub | Small but dev-focused |

## Tier 4 — Paid or blocked

| Directory | Cost | Notes |
|-----------|------|-------|
| MCP.so | $39 one-time | Publish immediately, verified badge, featured placement, dofollow link. No free path on the submission page |
| Whatsthebigdata | Free with badge, else $599+ | Add their badge to your homepage footer for a free listing |
| PulseMCP | Paused (Aug 2026) | Submissions temporarily closed while they overhaul their pipeline. They auto-pull from the official registry |

## What makes a listing stick

1. **A real remote endpoint.** Directories that run live handshakes (Stork) verify your server actually works. A dead endpoint gets flagged or rejected.
2. **Read-only posture.** Servers with readOnlyHint annotations are easier to approve and safer to recommend. Avoid write-capable tools in public directories unless the use case demands them.
3. **OAuth 2.1 PKCE.** The current MCP spec guidance expects modern OAuth. Servers that ship API-key-only auth get downgraded in review.
4. **A GitHub repo with a README.** Most directories pull description and stars from the repo. A clean README with install instructions is half the listing.
5. **Specific categories.** Finance, CRM, and analytics categories have far less competition than database or dev-tools. Pick the narrowest honest category.

## Field notes (August 2026)

- FutureTools Turnstile auto-passed in a real browser after filling the form. The challenge widget resolved itself on submit.
- The official registry search API paginates alphabetically and ignores query parameters — verify listing by pulling the server entry directly rather than searching.
- Claude's built-in connector directory (claude.ai) is separate from the public MCP registry and has its own compliance review. Being in both is the strongest possible placement.
- Track every submission in a log with the email or issue URL used. Directory coverage decays silently; a quarterly re-check is cheap.

## Source

Field-tested August 13, 2026 across FutureTools.io, MCP.Directory, Stork.AI, Glama.ai, mcpservers.org, MCP.so, PulseMCP, and Developers Digest.
