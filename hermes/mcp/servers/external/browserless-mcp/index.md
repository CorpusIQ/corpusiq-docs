---
title: "Browserless MCP — Integration Guide"
description: "Official Browserless MCP server — navigate, scrape, screenshot, and automate any website through headless Chrome at scale. Built by the Browserless team."
category: "Browser Automation"
stars: "★★"
source: mcpservers.org
github: https://github.com/browserless/browserless-mcp
date_added: 2026-07-28
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/browserless-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# Browserless MCP

Official MCP server from Browserless — the leading headless Chrome SaaS used by Apify, n8n, and thousands of operators. AI agents describe what they want in natural language and Browserless executes it on production-grade Chrome infrastructure.

## What It Does

- **Navigate:** Browse any website with full JavaScript rendering
- **Scrape:** Extract structured data from any page (tables, text, prices, listings)
- **Screenshot:** Capture full-page or element-specific screenshots
- **PDF Generation:** Convert any web page to PDF
- **Form Interaction:** Fill forms, click buttons, submit data
- **Performance:** Get Core Web Vitals, Lighthouse scores, and page speed metrics

## Why It Matters for Operators

Browserless is already the production standard for headless Chrome at scale. This MCP removes the final barrier — instead of writing Playwright scripts:
```
Agent: "Go to competitor.com/pricing, find their enterprise plan price, and tell me if it changed since last week"
→ Browserless navigates → extracts pricing table → compares to stored value → reports delta
```

No more `page.goto()`, `page.waitForSelector()`, or CSS selector debugging. The AI agent handles the intent; Browserless handles the browser.

## Setup

### Prerequisites
- Browserless account ([browserless.io](https://www.browserless.io))
- API token (Dashboard → API Keys)
- Or self-host Browserless (open source, Docker image)

### Claude Desktop
```json
{
  "mcpServers": {
    "browserless": {
      "type": "streamable-http",
      "url": "https://chrome.browserless.io/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_BROWSERLESS_TOKEN"
      }
    }
  }
}
```

### Self-Hosted
```json
{
  "mcpServers": {
    "browserless": {
      "type": "streamable-http",
      "url": "http://localhost:3000/mcp",
      "headers": {}
    }
  }
}
```

### Hermes Agent
```yaml
mcp_servers:
  browserless:
    type: streamable-http
    url: "https://chrome.browserless.io/mcp"
    headers:
      Authorization: "Bearer ${BROWSERLESS_TOKEN}"
```

## Tools

| Tool | Description |
|------|-------------|
| `navigate` | Go to a URL with full JS rendering |
| `screenshot` | Capture page or element screenshots |
| `scrape` | Extract text, tables, and structured data |
| `click` | Click any element by text, selector, or position |
| `type` | Type into input fields |
| `pdf` | Generate PDF from any URL |
| `performance` | Get Core Web Vitals and Lighthouse scores |
| `execute_script` | Run arbitrary JavaScript on the page |
| `wait_for` | Wait for element, text, or network idle |
| `extract_links` | Get all links on a page |
| `get_network_requests` | Monitor XHR/fetch calls |

## Pricing

Browserless Cloud:
- **Free:** 1,000 sessions/month, 1 concurrent browser
- **Starter:** $49/month — 10,000 sessions, 5 concurrent
- **Growth:** $199/month — 50,000 sessions, 20 concurrent
- **Business:** $499/month — 200,000 sessions, 50 concurrent
- **Enterprise:** Custom — unlimited sessions, dedicated infrastructure

Self-hosted: Free (open source, Docker: `docker run -p 3000:3000 browserless/chrome`)

## Use Cases

### Competitive Price Monitoring
```
Agent: "Every Monday at 8 AM, scrape the pricing pages of our top 5 competitors and alert me if anything changed"
→ navigate to each → extract pricing → diff against baseline → alert
```

### SEO & Content Audits
```
Agent: "Check our top 20 landing pages for Core Web Vitals issues and list the 10 slowest"
→ navigate → performance for each → sort by LCP → report
```

### Form Automation
```
Agent: "Register us for this industry conference — my email is [x], use the early bird code"
→ navigate to registration → type form fields → click submit → screenshot confirmation
```

### Data Extraction at Scale
```
Agent: "From this list of 100 company URLs, extract the CEO name and contact email from each"
→ batch_navigate → scrape contact pages → extract email patterns → return CSV
```

### Visual Regression Testing
```
Agent: "Take screenshots of our checkout flow on mobile and desktop and compare to last week's baseline"
→ navigate to checkout → screenshot(mobile) → screenshot(desktop) → diff against baseline
```

## Self-Hosting

Browserless is open source. For operators who want full control:

```bash
docker run -d \
  -p 3000:3000 \
  -e "CONCURRENT=10" \
  -e "TOKEN=your-secret-token" \
  -e "MAX_QUEUE_LENGTH=100" \
  browserless/chrome:latest
```

Then point the MCP at `http://localhost:3000/mcp`.

Self-hosted benefits:
- No session limits (bounded only by your hardware)
- No third-party data exposure
- Custom Chrome flags and extensions
- VPN/geo-targeted browsing

## Limitations

- **JavaScript-heavy sites:** Some SPAs may require `wait_for` or explicit delays. The MCP handles most cases but extremely dynamic pages may need scripted approaches.
- **CAPTCHA:** Browserless does not solve CAPTCHAs. For sites with CAPTCHA gates, use the LinkedIn MCP's managed infrastructure or similar solutions.
- **Session limits:** Free tier is generous (1,000 sessions) but high-frequency scraping requires a paid plan.
- **Concurrency:** Cloud plans have concurrency caps — large batch jobs queue automatically.

## See Also

- [[apify-mcp]] — Pre-built scrapers for common sites
- [[linkedin-mcp-gtm]] — LinkedIn automation with anti-bot infrastructure
- [[stripe-mcp]] — Payment processing
