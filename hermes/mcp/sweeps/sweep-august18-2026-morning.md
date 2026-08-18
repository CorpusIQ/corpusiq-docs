# Sweep Report — August 18, 2026 (Morning Cron Sweep)

**Shift:** Morning (10:05 UTC)
**Sources scanned:**
- mcp.so homepage SSR (`recentServers` with createdAt) — 8 fresh entries (Aug 17–18)
- chatmcp/mcpso GitHub issues — 30 most recent submissions (Aug 16–18)
- mcpservers.org homepage — 29 slugs, no new business-relevant entries

**Result:** 7 new servers catalogued with guides, 8 skipped, index updated.

## Catalogued (7 new, 7 guides)

| Server | Stars | Category | Signal |
|---|---|---|---|
| Caribooks MCP (QuickBooks Online CA+US, 160+ read/write tools) | ★★★ | Finance & Accounting | GH issue #3598 |
| Coldrig MCP (agent-cold-email, 28 tools) | ★★★ | Marketing | GH issue #3602 |
| Waqi — AI Privacy Layer (PII redaction + audit) | ★★ | Data & Analytics | mcp.so homepage (Aug 18) |
| Sonar ASO MCP (25 ASO tools, iOS + Play) | ★★ | Marketing | mcp.so homepage (Aug 18) |
| GitLab MCP (zereight, 1,898★) | ★★ | Developer Tools | GH issue #3604 |
| ProShip MCP (Thailand Post shipping) | ★ | Commerce | GH issue #3622 |
| Moltline Studio MCP Suite (14 servers, business math) | ★★ | Business Operations | GH issue #3601 |

## Skipped (evaluated, not catalogued)

- VisionGemma — Windows-only local single-tool vision OCR, thin surface
- otto — 0-star paper-trading testbed, experiment-stage
- 402oracle — x402 attestation infra (consistent with prior x402 skips)
- opengist-mcp — self-hosted gists, dev tool
- livetennisapi-mcp — consumer sports data
- traderspy — crypto signals
- designesy-org — design-QA dev tool
- dsh-verify — browser acceptance testing, dev tool

## Hygiene fixes in this cycle

- Quoted `source:` YAML values in 8 guides from the Aug 17 evening sweep (issue numbers like `#3609` were being parsed as YAML comments, failing the frontmatter gate)

## Verification

- Frontmatter validator: all 3,087 markdown files valid
- Push verified: local HEAD == remote main (7c335fb4)
- Catalog count: 249 → 256 servers, 139 → 146 guides
