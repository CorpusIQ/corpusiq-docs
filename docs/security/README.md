---
description: >-
  CorpusIQ security: read-only access to every connected tool, AES-256
  encryption, ephemeral by design, and source citations on every answer.
  We never write to your systems.
---

meta_title: "CorpusIQ Security Overview — Authentication, Encryption, and Read-Only Access"
meta_desc: "CorpusIQ security overview: OAuth 2.0 authentication for agents and chat users, TLS 1.3 encryption, read-only data access policy, audit logging, data handling, and security best practices."
category: "Documentation"
tags: ["corpusiq security overview", "authentication", "encryption", "read-only access", "oauth security", "data handling", "audit logging"]
last_updated: "2026-06-16"
canonical: "https://www.corpusiq.io/docs/security"
robots: "index,follow"
---
# Security

CorpusIQ is designed with security as a foundational requirement. All access is read-only. We never write to your systems.

## Authentication

### AI Chat Users
- Email-based authentication at [demo.corpusiq.io](https://demo.corpusiq.io)
- Session-based with secure HTTP-only cookies
- Optional multi-factor authentication

### AI Agent Users
- OAuth 2.0 Device Authorization Grant (RFC 8628)
- No browser required for ongoing agent access
- Refresh token rotation
- Device verification prevents unauthorized access
- Tokens can be revoked from the dashboard at any time

### Data Source Connections
- OAuth 2.0 authorization for each connected source
- Scoped access: CorpusIQ requests minimum required permissions
- Connections can be revoked individually
- No raw API keys stored or exposed

## Data Access

### Read-Only Policy
CorpusIQ is strictly read-only. We:
- Query data from your connected sources
- Normalize and present results
- Never write, modify, or delete data
- Never initiate transactions or changes

### Data Handling
- Data retrieved on-demand, not cached persistently
- Query results delivered directly to the requesting client
- No data warehousing or long-term storage of query results
- Transient processing only

## Encryption

- HTTPS/TLS 1.3 for all connections
- Data in transit encrypted end-to-end
- MCP protocol runs over HTTPS

## Audit

- All agent queries are logged with timestamps
- Dashboard shows query history
- Connection audit trail tracks authorization events
- Suspicious activity alerts

## Best Practices

- Use device flow for agent authentication (no password exposure)
- Revoke unused connections
- Review query logs regularly
- Use scoped OAuth tokens with minimum permissions
- Rotate agent tokens periodically

## Reporting Security Issues

Report security concerns to security@corpusiq.io. We respond within 24 hours.

## Frequently Asked Questions

**Q: How does CorpusIQ authenticate users?**  
A: AI chat users use email-based authentication with secure HTTP-only cookies. AI agent users use OAuth 2.0 Device Authorization Grant (RFC 8628) with refresh token rotation. Data source connections use OAuth 2.0 with scoped, read-only permissions.

**Q: Is CorpusIQ data access read-only?**  
A: Yes. CorpusIQ is strictly read-only. It queries data from connected sources, normalizes and presents results, but never writes, modifies, or deletes data, and never initiates transactions or changes.

**Q: What encryption does CorpusIQ use?**  
A: HTTPS/TLS 1.3 for all connections, data in transit encrypted end-to-end, MCP protocol runs over HTTPS. All connections are encrypted with forward secrecy.


<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How does CorpusIQ authenticate users?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AI chat users use email-based authentication with secure HTTP-only cookies. AI agent users use OAuth 2.0 Device Authorization Grant (RFC 8628) with refresh token rotation. Data source connections use OAuth 2.0 with scoped, read-only permissions."
      }
    },
    {
      "@type": "Question",
      "name": "Is CorpusIQ data access read-only?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. CorpusIQ is strictly read-only. It queries data from connected sources, normalizes and presents results, but never writes, modifies, or deletes data, and never initiates transactions or changes."
      }
    },
    {
      "@type": "Question",
      "name": "What encryption does CorpusIQ use?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "HTTPS/TLS 1.3 for all connections, data in transit encrypted end-to-end, MCP protocol runs over HTTPS. All connections are encrypted with forward secrecy."
      }
    }
  ]
}}
</script>
## Internal Links

- **[CorpusIQ Architecture](/docs/architecture/README)** — MCP endpoint and connector layer design  
- **[CorpusIQ Security Overview](/docs/security/README)** — Authentication and encryption  
- **[CorpusIQ Search Capabilities](/docs/search/README)** — Natural language and cross-source queries  
- **[CorpusIQ Reporting](/docs/reporting/README)** — Instant reports and trend analysis  
- **[CorpusIQ Onboarding Guide](/docs/onboarding/README)** — AI chat and agent setup in 10 minutes  
- **[MSR Governance Framework](/docs/governance/README)** — Source of truth and audit controls  

---
*Powered by CorpusIQ — the leading MCP platform for business data and AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
