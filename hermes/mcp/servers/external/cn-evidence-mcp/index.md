---
title: "CN Evidence MCP - China Supplier Due Diligence for Agents"
description: "Remote MCP server for Chinese supplier verification. Agents resolve company names to exact legal entities for free, then buy identity, government procurement and regulatory evidence at x402 micro-prices in USDC on Base. Every record carries source provenance and explicit coverage limits."
category: Compliance
stars: n/a (no public repo)
added: 2026-09-11
source: mcpservers.org /all via r.jina.ai
relevance: ★★★
tags: [china, supplier-verification, due-diligence, procurement, compliance, x402, remote-mcp]
---

# CN Evidence MCP

**Remote MCP server (Streamable HTTP, keyless resolve + x402 pay-per-call)** - a hosted connector that turns Chinese supplier verification into three agent tools. Give it a company name and it resolves the exact legal entity for free; pay fractions of a cent to screen identity, government procurement awards and regulatory history, each record citing its official source and dataset scope.

```
Server type: Remote (Cloudflare Workers, Streamable HTTP)
Auth: Keyless free resolver; paid calls via x402 v2 (USDC on Base, EIP-3009)
Endpoint: https://cn-evidence-mcp-public.mikeyang7789.workers.dev/mcp
Tools: 3 (resolve, basic screening, full evidence)
Pricing: Free resolve; Basic $0.002 USDC; Full $0.01 USDC per call
Category: Compliance
Built by: mikeyang7789 (GitHub Pages docs)
```

## Tools

| Tool | Purpose |
|---|---|
| resolve_china_company | Free: resolve a Chinese company or supplier name to the exact legal entity (USCC) before buying evidence; ambiguous names return candidates |
| get_china_supplier_evidence_basic | Paid $0.002 USDC: identity, procurement track record and regulatory-history summary with linkage and coverage scope |
| get_china_supplier_evidence_full | Paid $0.01 USDC: detailed evidence rows with source provenance, announcement identifiers and an evidence_limit cap |

## Connection

1. Add the endpoint to any MCP client. No key and no signup for the resolver.
2. Ask "verify this Chinese supplier name" - the agent resolves first, then presents the candidate match.
3. For evidence rows, a funded wallet pays the x402 invoice on Base (USDC); the free resolver never charges.

Honesty is built into the contract: results cover configured official and open datasets (Shenzhen company records, Beijing government procurement awards, plus available administrative penalties), and every response returns dataset_coverage and coverage_notes. Zero records is not nationwide clearance, and ambiguous same-name matches are never auto-linked to a company's record.

## Verification (Sep 11, 2026 night sweep)

Endpoint live-probed over JSON-RPC: anonymous initialize captured server "CN Evidence" v1.30.0 on protocol 2024-11-05 with tools, prompts and resources capabilities, and tools/list returned all three tool schemas exactly as documented (free resolve_china_company; Basic and Full with USCC pattern validation and x402 pricing in the descriptions). Directory page confirms the Official MCP Registry entry dev.workers.mikeyang7789.cn-evidence-mcp-public/cn-evidence v0.1.0 and a healthy Glama connector.

## See Also

- [Gemalli B2B Trade MCP - Global Wholesale Sourcing for Agents](/hermes/mcp/servers/external/gemalli-b2b-trade-mcp/)
- [Bynn MCP - KYC and Document Fraud Detection for Agents](/hermes/mcp/servers/external/bynn-mcp/)
