---
title: "OpenOSINT MCP — Integration Guide"
description: "MCP-native OSINT framework — 9 intelligence tools for email enumeration, breach checks, WHOIS, IP intel, subdomain discovery, dorks, and more. Free and open source."
category: "Security & Intelligence"
stars: "★★"
source: mcpservers.org
github: https://github.com/OpenOSINT/OpenOSINT
date_added: 2026-07-28
---

# OpenOSINT MCP

MCP-native open-source intelligence framework. Nine tools covering the full OSINT stack — email enumeration, username search, breach verification, WHOIS lookups, IP intelligence, subdomain discovery, Google dorks, paste searches, and phone intelligence. Free, open source (MIT), and works as both an MCP server and standalone Python CLI.

## What It Does

- **Email Enumeration:** Find all accounts tied to an email address across social platforms
- **Username Search:** Check username availability and account presence across 300+ platforms
- **Breach Check:** Query HaveIBeenPwned for compromised credentials
- **WHOIS Lookup:** Domain registration details, nameservers, and expiry dates
- **IP Intelligence:** Geolocation, ASN, hosting provider, and threat reputation
- **Subdomain Enumeration:** Discover subdomains for any domain
- **Google Dorks:** Execute advanced Google search queries for exposed documents
- **Paste Search:** Search Pastebin and similar sites for leaked credentials
- **Phone Intelligence:** Carrier lookup, line type, and basic validation

## Why It Matters for Operators

Before OpenOSINT MCP, an operator doing vendor due diligence would:
1. Open 5 different browser tabs (WHOIS, Shodan, HaveIBeenPwned, Google, Hunter.io)
2. Manually type the vendor's domain into each
3. Copy-paste results into a document
4. Repeat for the next vendor

Now:
```
Agent: "Run full OSINT on vendor.com before we sign the contract"
→ OpenOSINT runs all 9 tools → returns consolidated report in one response
```

For competitive research, security assessments, and domain acquisitions, this turns hours of manual OSINT into seconds of conversation.

## Setup

### Prerequisites
- Python ≥ 3.10
- No API keys required (uses public data sources)
- Some tools may need optional API keys for higher limits (HaveIBeenPwned, Shodan)

### Install
```bash
pip install openosint-mcp
```

### Claude Desktop
```json
{
  "mcpServers": {
    "openosint": {
      "command": "python",
      "args": ["-m", "openosint_mcp"],
      "env": {
        "HIBP_API_KEY": "optional-haveibeenpwned-key",
        "SHODAN_API_KEY": "optional-shodan-key"
      }
    }
  }
}
```

### Cursor / VS Code
```json
{
  "mcpServers": {
    "openosint": {
      "command": "python",
      "args": ["-m", "openosint_mcp"],
      "env": {}
    }
  }
}
```

### Hermes Agent
```yaml
mcp_servers:
  openosint:
    command: python
    args: ["-m", "openosint_mcp"]
    env: {}
```

## Tools

| Tool | Description | Requires API Key? |
|------|-------------|-------------------|
| `email_lookup` | Find accounts, breaches, and profiles tied to an email | No |
| `username_search` | Check username presence across 300+ platforms | No |
| `breach_check` | Check email/domain against HaveIBeenPwned database | Optional (HIBP) |
| `whois_lookup` | Domain WHOIS: registrar, dates, nameservers, contacts | No |
| `ip_lookup` | IP geolocation, ASN, hosting provider, threat intel | Optional (Shodan) |
| `subdomain_enum` | Discover subdomains via certificate transparency + DNS | No |
| `google_dorks` | Run advanced Google queries (filetype:, site:, intitle:) | No |
| `paste_search` | Search Pastebin and similar for leaked data | No |
| `phone_lookup` | Carrier, line type, country, basic validation | No |

## Use Cases

### Vendor Due Diligence
```
Agent: "We're about to sign a $50K contract with vendor.com. Run full OSINT — anything concerning?"
→ whois_lookup(vendor.com) → subdomain_enum → email_lookup(contact emails) → breach_check(vendor.com) → google_dorks("site:vendor.com confidential") → paste_search("vendor.com") → consolidated report
```
Result: "vendor.com registered 2019, clean WHOIS, no breaches, but found exposed .env backup on staging.vendor.com (Google dorks hit) and one employee email in a 2024 breach — flag for security review."

### Competitive Intelligence
```
Agent: "What subdomains does competitor.com have and what tech stack is on each?"
→ subdomain_enum(competitor.com) → ip_lookup for each → identify hosting/CDN/tech stack → report
```
Result: 24 subdomains found — staging, api, admin, analytics, internal wiki, partner portal. Tech stack: AWS + Cloudflare + React.

### Domain Acquisition Research
```
Agent: "The domain we want is registered. Who owns it and when does it expire?"
→ whois_lookup(domain.com) → email_lookup(registrant email) → username_search(registrant name)
```
Result: Registered to [company], expires 2027-03-15, registrant is VP Engineering, also owns 12 related domains.

### Hiring & Background Checks
```
Agent: "We're hiring a senior engineer. Run OSINT on their email and public profiles"
→ email_lookup(candidate@email.com) → breach_check(email) → username_search(known usernames)
```
Result: Profiles found on GitHub, LinkedIn, Stack Overflow, Twitter. One breach hit from 2023 (Adobe). Clean otherwise.

### Security Posture Assessment
```
Agent: "Check our own domain for any exposed information we should know about"
→ subdomain_enum(ourcompany.com) → google_dorks("site:ourcompany.com filetype:pdf confidential") → paste_search("ourcompany.com") → breach_check("ourcompany.com")
```
Result: 18 subdomains, 2 staging servers exposed, 1 PDF with API keys found via dorks (critical), no paste leaks. Take down the PDF immediately.

## Privacy & Ethics

OpenOSINT uses only publicly available data sources. No hacking, no credential stuffing, no bypassing access controls. It automates what a human can already do manually — just faster.

**Operators should:**
- Only investigate domains and emails you have a legitimate business reason to research
- Respect rate limits on public APIs
- Don't use for stalking, harassment, or unauthorized surveillance
- Be aware that WHOIS lookups and Google dorks may be logged

## Limitations

- **Rate limits:** Public APIs (WHOIS, DNS, Google) have rate limits. Bulk enumeration may require paid API keys.
- **HaveIBeenPwned:** Without an API key, breach checks are limited to basic domain search. HIBP API key is $3.50/month for full access.
- **Google Dorks:** Google may CAPTCHA or rate-limit automated queries. Use sparingly.
- **Paste searches:** Coverage depends on Pastebin and similar sites' availability — not all paste sites are indexed.
- **Accuracy:** IP geolocation is approximate (~city level). Phone carrier data may be stale for ported numbers.

## See Also

- [[datanexus-mcp]] — Public data intelligence (complementary: federal contracts, patents, CVE)
- [[sanctions-screening-mcp]] — OFAC/EU/UK/UN sanctions screening
- [[browserless-mcp]] — Browser automation for visual investigation
