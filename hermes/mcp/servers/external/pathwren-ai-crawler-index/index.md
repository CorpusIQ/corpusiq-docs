---
title: "AI Crawler Index MCP - Robots.txt Control for AI Bots"
description: "Keyless hosted MCP that identifies AI crawlers by user-agent or IP and generates the robots.txt that matches your stance: look up any crawler's operator, category and verification method, test IPs against operator-published prefixes remirrored every six hours, and produce ready-to-paste robots.txt blocks for eight stances with reasoning."
category: SEO
stars: "n/a (hosted service)"
added: 2026-09-01
source: "mcpservers.org homepage (Sep 1, 2026 night sweep)"
relevance: ★★
tags: [mcp-server, seo, aeo, robots-txt, ai-crawlers, webmaster, keyless, remote-mcp]
---

# AI Crawler Index MCP

**Know every AI crawler and say so in robots.txt.** The AI Crawler Index identifies AI crawlers by user-agent or IP and generates the robots.txt block that matches the site's stance, with the reasoning and the crawlers it names. Live-probed Sep 1, 2026: all 7 tools captured from the endpoint with no key or account.

```
Server type: Hosted, remote (Streamable HTTP)
Endpoint: https://www.pathwren.workers.dev/mcp
Auth: None - keyless (verified live)
Tools: 7 (live-probed: classify_user_agent, lookup_crawler, list_crawlers, generate_robots_txt, is_verified_crawler_ip, whats_changed, changes_since)
Index freshness: operator sources remirrored every 6 hours
Built by: Pathwren (pathwren.workers.dev)
```

## Why This Matters for Operators

AI crawlers now decide how a site appears in AI answers, and every operator has a stance - block, allow, or license. The problem is the crawler landscape moves weekly and robots.txt mistakes are silent until the traffic or the AI visibility is already gone.

First, **identification is the hard part.** `classify_user_agent` and `lookup_crawler` tell you what a crawler is, who operates it, its robots.txt token and stance, and what blocking it costs - before you write a line of robots.txt.

Second, **verifiable IP checks.** `is_verified_crawler_ip` tests any IPv4 or IPv6 address against the prefixes the crawler operators themselves publish, remirrored every six hours - so blocking decisions rest on operator-published ranges, not folklore.

Third, **stance-shaped output.** `generate_robots_txt` returns a ready-to-paste block for one of eight stances with the reasoning and the crawlers it names, so the operator picks the policy and the machine writes the syntax.

## Tools and Capabilities

All 7 tools captured live Sep 1, 2026.

| Tool | What it does |
|------|--------------|
| `classify_user_agent` | Identify the crawler behind a raw User-Agent header: operator, category, robots.txt stance, verification method, and what blocking it costs |
| `lookup_crawler` | Full index record for one crawler: operator, category, robots.txt token and stance, user-agent substring, verification method |
| `list_crawlers` | The filtered or whole index, each row stating what the crawler is and what blocking it costs |
| `generate_robots_txt` | Ready-to-paste robots.txt block for one stance with reasoning and the crawlers it names; omit the argument for all eight stances |
| `is_verified_crawler_ip` | Test an IP against every operator-published crawler prefix, remirrored every 6 hours |
| `whats_changed` | Freshness and change state: index build time, per-source fetch times, what changed, what is failing |
| `changes_since` | Only what changed since the caller's cursor: prefixes added or removed, upstreams recovered or failed |

## Installation

```bash
claude mcp add --transport http ai-crawler-index https://www.pathwren.workers.dev/mcp
```

No account, no key. The endpoint is POST-only Streamable HTTP; the vendor also publishes companion pages at mcp-doctor.html, mcp-netcheck.html and mcp-robots.html on the same domain.

## Configuration

```json
{
  "mcpServers": {
    "ai-crawler-index": {
      "type": "http",
      "url": "https://www.pathwren.workers.dev/mcp"
    }
  }
}
```

That is the entire configuration. The index remirrors operator sources every six hours; use `changes_since` with the returned cursor in scheduled checks to keep a site's robots.txt current as the crawler landscape shifts.

## Business Relevance

- **SEO and AEO operators** keep a site's AI-crawler stance current as new crawlers launch and operators change their published prefixes.
- **Publishers and media operators** implement licensing stances (allow, block, or conditional) in robots.txt with per-crawler reasoning.
- **Security teams** check whether traffic hitting a site matches verified crawler IP ranges before allowing or rate-limiting it.
- **Webmaster agencies** audit client robots.txt files against the current index and document the cost of each blocking decision.

## Integration with CorpusIQ

The AI Crawler Index composes with CorpusIQ as the technical layer under an AEO decision. A CorpusIQ workflow that reports search visibility or traffic by page can check which AI crawlers are hitting the site, verify their IP ranges, and propose the robots.txt stance that matches the operator's policy - then log the decision alongside the traffic data it affects. The operator keeps one governance point: CorpusIQ supplies the performance context, the AI Crawler Index supplies the crawler ground truth, and the human picks the stance; the machine writes the syntax.

## Limitations

- Hosted on a Cloudflare Workers domain with no vendor company page or repo found - the operator is identified only as Pathwren; evaluate accordingly for production policy decisions.
- The index is only as current as its remirror cadence (6 hours) and its operator sources.
- robots.txt is advisory - most AI crawlers honor it, but stance enforcement ultimately depends on each operator's own published policy.
- No authentication means the tool cannot store per-site state; keep your stance decisions in your own system.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Ranki MCP - SEO and AEO Audits](/docs/hermes/mcp/servers/external/ranki-mcp)
- [Seomely MCP - Google Index Monitoring with History](/docs/hermes/mcp/servers/external/seomely-mcp)
