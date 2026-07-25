# MCP Sweep — July 25, 2026 Afternoon (11:00 AM MST)

## Summary
- **Method:** mcpservers.org sitemap scrape (GitHub Search API blocked — "user flagged as spammy")
- **Servers indexed:** 9,634 (mcpservers.org)
- **Compared against:** 91 existing catalog entries
- **New servers discovered:** 17
- **Guides written:** 1 (OpusGrowth MCP)

## New Business-Relevant Servers Found

### ★★★ OpusGrowth MCP — Guide Written
- **Repo:** opusgrowth/Opus-Growth-The-MCP-Connector-for-Ad-Platforms
- **Created:** July 10, 2026 | **Updated:** July 24, 2026
- **Stars:** 0 (new)
- **Description:** Hosted MCP connector for Google Ads, Microsoft Advertising, TikTok Ads, LinkedIn Ads — 233 tools, write actions with approval gates
- **Business value:** HIGH — Ad spend management is a top operator use case
- **Status:** Pre-launch, waitlist only

### Additional Discoveries (No Guides — Monitoring)

| Server | Stars | Created | Relevance |
|--------|-------|---------|-----------|
| codeChap/mcp-server-linkedin | 0 | Apr 2026 | LinkedIn automation (stub, no updates since April) |
| codeChap/mcp-server-seo | 0 | Jul 19, 2026 | SEO audit, crawl, GSC, PageSpeed |
| dashi96/chromium-bridge | 4 | - | Browser MCP bridge for Arc/Vivaldi |
| infimium-ai/infimium-agent | 15 | - | Cross-IDE coding session memory |
| lulu-the-narwhal/lulu-ads | 1 | Jul 14, 2026 | MCP monetization with sponsored slots |
| antohins/seo-tools-mcp | - | - | SEO tools |
| gitdealflow-com | - | - | Deal flow tracking |
| 11agents/11agents-cloud-mcp | 0 | - | Hosted agent cloud API |
| agentcouch-dev | - | - | Agent development platform |
| codecrafted-uk/cc-design-mcp | - | - | Design tools |
| yiaany/ghostapi | - | - | Ghost CMS API |
| tiagohanna123/agent-web-search-mcp | - | - | Web search for agents |
| +5 others (niche/non-business) | - | - | Various |

## Blockers Encountered
- **GitHub Search API:** All queries return "User flagged as spammy" (HTTP 422). The classic PAT at `~/.hermes/profiles/corpusiq/secrets/github.token` (prefix ghp_) has been flagged. Individual repo API calls still work but Search endpoint is unavailable.
- **mcp.so:** SSR-only, no API endpoint. Homepage scraping yielded categories but not individual server listings.
- **mcpservers.org:** SSR-only, but sitemap XML is accessible and was used as primary data source.

## Recommendations
1. **GitHub token:** The current token has been flagged for search spam. Consider rotating to a new classic PAT or using a different account for search queries.
2. **OpusGrowth:** Monitor for public launch. This is the most promising business-operator MCP server found this week.
3. **codeChap servers:** The same developer (codeChap) has multiple MCP servers (LinkedIn, SEO, agent-browser). Worth monitoring their GitHub activity for new releases.
