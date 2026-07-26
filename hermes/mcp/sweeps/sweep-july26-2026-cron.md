# MCP Sweep — July 26, 2026 (Cron — ~12:00 UTC)

## Summary
- **Method:** mcp.so homepage SSR scrape + mcpservers.org homepage scrape + GitHub API
- **Compared against:** 92 existing catalog entries
- **New servers discovered since last sweep (July 26 01:00 UTC):** 3

## New Servers Discovered

### 1. Oromi Agent Services ★★★ — GUIDE WRITTEN
- **Source:** mcp.so (created July 23, 2026)
- **Website:** https://agents.oromi.co.uk
- **Description:** 25 pay-per-call tools for UK business operations via MCP — Companies House registry, HM Land Registry property data, agent-readiness audits, domain/email/VAT/IBAN verification, human-in-the-loop tasks. x402 micropayments (USDC on Base). Remote endpoint + npx package.
- **Category:** Business Intelligence
- **Business relevance:** HIGH — UK company due diligence, property market intelligence, business name checking, agent-readiness scanning, and verification tools all in one MCP connection. Directly useful for UK-based business operators.
- **Status:** Full integration guide written → [`oromi-agent-services/index.md`](/hermes/mcp/servers/external/oromi-agent-services/)

### 2. ctxfile
- **Source:** mcp.so (created July 19, 2026)
- **Repo:** `github.com/ctxfile/ctxfile`
- **Stars:** 2
- **Description:** Local-first MCP server that snapshots your project's working state into one context object. Open-core, privacy-first.
- **Category:** Developer Tools / Memory & Knowledge
- **Business relevance:** LOW-MODERATE — Useful for developers working with AI agents who need reproducible context states. Niche for general business operators.
- **Status:** Noted, no guide. Monitoring for adoption.

### 3. mcp-fns-check
- **Source:** mcp.so (created July 22, 2026)
- **Repo:** `github.com/atomno-mcp/mcp-fns-check`
- **Stars:** 14
- **Description:** MCP server for Russian counterparty due diligence via FNS open data — EGRUL/EGRIP, EFRSB, KAD, FSSP. 7 tools: check_contractor, check_inn, check_ogrn, get_legal_status, get_okveds, get_directors_history, check_for_red_flags.
- **Category:** Compliance / Finance
- **Business relevance:** NONE — Russia-specific (FNS federal tax service data). Not relevant to general business operators.
- **Status:** Noted, no guide.

## Previously Monitored Servers (No Change)

- **AptiBuild AI** (July 26) — FRED/BLS labor data, $39/month. Still monitoring.
- **Medplum** (July 26) — Healthcare compliance. Still no business-ops relevance.

## mcpservers.org Latest Activity

mcpservers.org homepage "latest" section showed 8 servers — all already in our catalog (CDN.MN, TaskerArmy Agent, Reelier, Taplio, iGaming Tools, Outside Agent, Fixou, Argus Testing). No new servers from this source since the afternoon sweep on July 25.

## Blockers
- **web_extract:** Firecrawl not configured. curl-based extraction used throughout.
- **GitHub Search API:** Not tested this sweep (mcp.so SSR + direct API calls sufficient).
- **Firecrawl API:** Still unconfigured on this Hermes instance.

## Catalog Update
- **Added:** oromi-agent-services/index.md (full guide)
- **Noted:** ctxfile, mcp-fns-check
- **Total catalog:** 93 servers (+1 from last sweep)
- **Guides written this sweep:** 1
