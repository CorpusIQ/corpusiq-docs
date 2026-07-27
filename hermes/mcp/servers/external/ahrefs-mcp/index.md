# Ahrefs MCP Server ★★★ Official

**Source:** mcpservers.org · **Last updated:** July 26, 2026 (evening sweep)  
**Website:** [ahrefs.com](https://ahrefs.com)  
**Endpoint:** Hosted MCP (Ahrefs-managed, URL provided after connection)  
**Auth:** Ahrefs account (Lite plan or higher required)  
**Category:** SEO / Marketing Analytics

---

## Overview

The **official Ahrefs MCP server** connects AI agents to Ahrefs' industry-leading SEO data — backlinks, domain ratings, keyword research, competitor analysis, and site health. Agents can enrich their responses with real Ahrefs data, pulling from Ahrefs' web-scale index of backlinks, keywords, and traffic estimates.

This is the first major SEO platform to ship an official MCP server, bringing AI-assisted SEO workflows to operators who use Ahrefs for growth and competitive intelligence.

## Key Capabilities

- **Backlink Analysis** — Get referring domains, backlinks, anchor details for any domain (`get_backlinks`)
- **Domain Rating & SEO Metrics** — Retrieve Domain Rating (DR), traffic estimates, and keyword counts (`get_domain_metrics`)
- **Top Pages by Traffic** — Identify highest-traffic pages on a site and the keywords driving visits (`get_top_pages`)
- **Competitor Keywords** — Find which organic keywords a competing domain ranks for and their positions (`get_competitor_keywords`)
- **Site Health Issues** — Pull a list of SEO issues detected on a site to prioritize fixes (`list_issues`)
- **Keyword Research** — Search for keyword ideas with volume, difficulty, and CPC data

## Integration

### 1. Ahrefs MCP Connection Flow

1. Log in to your Ahrefs account (Lite plan or higher)
2. Navigate to **Account Settings → MCP Connections**
3. Click **Connect AI Tool** — Ahrefs provides a unique MCP server URL
4. Add that URL to your MCP client configuration

### 2. Claude Desktop

```json
{
  "mcpServers": {
    "ahrefs": {
      "type": "http",
      "url": "https://mcp.ahrefs.com/YOUR_UNIQUE_ENDPOINT",
      "auth": "bearer",
      "token": "YOUR_AHREFS_MCP_TOKEN"
    }
  }
}
```

### 3. Hermes Agent (config.yaml)

```yaml
mcp:
  servers:
    ahrefs:
      type: http
      url: https://mcp.ahrefs.com/${AHREFS_MCP_ENDPOINT}
      headers:
        authorization: Bearer ${AHREFS_MCP_TOKEN}
```

### 4. Cursor / VS Code

Add the Ahrefs-provided MCP URL and token to your MCP configuration. Once connected, your setup syncs across all devices linked to your Ahrefs account.

## Business Operator Use Cases

1. **Competitive Content Gap Analysis** — "What keywords does competitor X rank for that we don't?" — agent finds the gaps and suggests content opportunities
2. **Backlink Profile Audit** — "Show me all referring domains to our site, sorted by DR" — agent surfaces link-building opportunities and toxic links
3. **Site Health Monitoring** — Weekly automated scan: "Check our site for new SEO issues and prioritize by impact"
4. **Content Performance Review** — "Which of our blog posts drive the most organic traffic and from which keywords?"
5. **Market Entry Research** — "What's the keyword difficulty and search volume for [new market segment]?" — agent evaluates market opportunity

## Pricing

- **Ahrefs MCP server:** Free (included with Ahrefs subscription)
- **Ahrefs plans:** Lite from $129/month, Standard $249/month, Advanced $449/month
- **MCP access requires Lite or higher**

## Security Considerations

- Ahrefs-hosted MCP endpoint — no self-hosting required
- Token-based auth scoped to your Ahrefs account
- All API calls respect your Ahrefs plan limits (rows per report, reports per month)
- ⚠️ Agent can consume your API quota — set expectations for query frequency

## Verdict

★★★★★ — The first major SEO platform to ship MCP. Essential for growth operators, content marketers, and SEO professionals. Having an agent that can answer "what are our competitors ranking for?" with live Ahrefs data instead of stale training data transforms competitive intelligence workflows. The Lite-plan requirement ($129/month) is the only barrier for smaller operators.
