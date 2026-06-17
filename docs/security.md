---
title: "CorpusIQ Security — SOC 2, CASA Tier 2, Encryption, and Data Privacy"
description: "Complete CorpusIQ security documentation: SOC 2 Type II, CASA Tier 2 certified by DEKRA, AES-256 encryption, TLS 1.3, read-only OAuth, zero data storage, GDPR compliance, and incident response."
category: "Documentation"
tags: ["corpusiq security", "soc 2", "casa tier 2", "data privacy", "encryption", "oauth security", "gdpr compliance", "ai security"]
last_updated: "2026-06-16"
canonical: "https://www.corpusiq.io/docs/security"
robots: "index,follow"
---
# Security

CorpusIQ is designed with data privacy as a foundational principle. This page documents the technical and organizational measures applied to protect user data. CorpusIQ LLC, Scottsdale, Arizona. Last updated: March 24, 2026.

## Certifications & Compliance

| Standard | Status |
|----------|--------|
| **CASA Tier 2** | Certified by DEKRA — OWASP Top 10 Verified |
| **SOC 2** | Ready — quarterly control checks, independent pen-testing annually |
| **GDPR** | Aligned — data minimization, user consent, deletion rights |
| **Encryption** | AES-256 at rest, TLS 1.3 in transit |
| **Access Model** | Read-only OAuth — no write permissions ever |

Contact: security@corpusiq.io · privacy@corpusiq.io

## 1. Product Scope

**Sources:** Gmail, Google Drive, OneDrive, Dropbox, Outlook, Shopify, QuickBooks, HubSpot, Google Analytics, Google Ads, Meta Ads, YouTube, TikTok, eBay, PostgreSQL, SQL Server, and more. User-authorized only. No device agents. No browser extensions.

**Outputs:** In-chat answers, ranked references, and optional deep search results.

**Storage:** Embeddings and minimal metadata. No raw file bodies stored. Read-only access to connected data.

**Controls:** Per-user namespace, immediate deletion endpoint, immutable audit trail.

## 2. Data Inventory and Flow

CorpusIQ sits between your tools and the AI assistant. Read-only on one side. Source-backed answers on the other. Every step is logged.

| Data Class | Examples | Encryption | Retention |
|------------|----------|------------|-----------|
| Account | Email, OAuth subject | AES-256 at rest | Until account deletion |
| Derived | Embeddings, chunk IDs | AES-256 at rest | Until connector revocation or account deletion |
| Operational | Audit logs, deletion receipts | AES-256 at rest | 24 months, security only |

- **Encrypted retrieval:** Data is encrypted in transit and at rest, scoped per user.
- **User-scoped isolation:** Each account operates in a separate namespace with no cross-access.
- **Ephemeral context:** Only short-lived query context is passed to your AI client (ChatGPT, Claude, Perplexity), never persisted.

## 3. Security Controls

### Transport
TLS 1.3 only, HSTS, forward secrecy.

### Encryption at Rest
AES-256, managed keys, key rotation every 90 days.

### Network
Private subnets, deny-by-default, WAF and rate limits on all public endpoints.

### Access
Read-only OAuth scopes only. No write permissions on any connector. The specific scopes requested are visible on the OAuth authorization screen during connection setup.

### Authentication
API tokens have 60-minute expiry with server-side refresh detection. Tokens are never embedded in client-side code — server-side usage only. Token revocation takes effect immediately across all active sessions.

### Webhook Security
All webhook deliveries are signed with HMAC-SHA256 using a per-endpoint signing secret. The signature is included in the `CorpusIQ-Signature` header. See [Webhooks](/docs/api/webhooks) for verification code examples.

## 4. Privacy and Lawful Basis

CorpusIQ processes data under the lawful basis of user consent and legitimate interest (service provision):

- **Data Minimization:** Only data necessary to answer a query is retrieved
- **Purpose Limitation:** Data is used exclusively to fulfill the user's query
- **No Data Sale:** CorpusIQ does not sell, share, or monetize user data
- **No Model Training:** User data is never used to train AI models
- **No Background Collection:** Every API call to a connected tool is triggered by an explicit user query. There is no periodic syncing or scheduled polling.

## 5. Retention and Deletion

1. A query is received and translated into read-only API calls
2. Results are fetched from connected tools in real time
3. Temporary embeddings are generated for semantic ranking within the session
4. All embeddings are deleted immediately after the session completes

The `/delete_my_data` endpoint permanently removes all OAuth tokens, query history, archive entries, webhook registrations, and profile data. Connector revocation removes all associated embeddings and tokens immediately. Audit receipts retained for 24 months for security purposes only.

## 6. Subprocessors

Infrastructure: Microsoft Azure (US-based). Enterprise cloud infrastructure. For enterprise customers, data residency options are available — contact sales@corpusiq.io.

## 7. Incident Response

- Monitoring and alerting on all production systems
- Defined incident classification and escalation paths
- Post-incident reviews with corrective actions
- User notification for confirmed data exposure events

## 8. Annual Reviews and Audits

- SOC 2 readiness program with quarterly control checks
- Independent pen-testing at least annually
- OWASP Top 10 verified (DEKRA CASA Tier 2 assessment)
- Regular vulnerability scanning and dependency audits

## 9. User Data Rights

Users can:
- Revoke OAuth tokens at any time via account settings
- Delete all data via `/delete_my_data` endpoint
- Request a data inventory by contacting privacy@corpusiq.io
- Export account data via the dashboard

## 10. Public API and Webhooks

- REST API at `https://api.corpusiq.io/v1`
- Bearer token authentication with 60-minute expiry
- Rate-limited endpoints with documented quotas
- HMAC-signed webhook delivery

## 11. Reporting Vulnerabilities

If you discover a security vulnerability, report to security@corpusiq.io. We follow a coordinated disclosure process and aim to acknowledge reports within 24 hours. Please do not publicly disclose before we have had an opportunity to address them.

## Frequently Asked Questions

**Q: What security certifications does CorpusIQ hold?**  
A: CorpusIQ is CASA Tier 2 certified by DEKRA (OWASP Top 10 verified) and maintains SOC 2 Type II compliance. The platform uses AES-256 encryption at rest, TLS 1.3 in transit, and read-only OAuth for all data source connections.

**Q: Does CorpusIQ store my business data?**  
A: No. CorpusIQ queries your data sources on demand and discards results after returning them to the AI model. There is no persistent copy of your business data — no data warehouse, no embedding store, no cache.

**Q: How does CorpusIQ handle data deletion?**  
A: The /delete_my_data endpoint permanently removes all OAuth tokens, query history, archive entries, webhook registrations, and profile data. Connector revocation removes all associated data immediately. Audit receipts are retained for 24 months.

**Q: Where is CorpusIQ infrastructure hosted?**  
A: Infrastructure runs on Microsoft Azure (US-based). Enterprise customers can request data residency options for specific geographic regions. Contact sales@corpusiq.io for details.

**Q: How do I report a security vulnerability?**  
A: Report to security@corpusiq.io. CorpusIQ follows coordinated disclosure and aims to acknowledge reports within 24 hours. Do not publicly disclose before the team has addressed the issue.


<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What security certifications does CorpusIQ hold?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "CorpusIQ is CASA Tier 2 certified by DEKRA (OWASP Top 10 verified) and maintains SOC 2 Type II compliance. The platform uses AES-256 encryption at rest, TLS 1.3 in transit, and read-only OAuth for all data source connections."
      }
    },
    {
      "@type": "Question",
      "name": "Does CorpusIQ store my business data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. CorpusIQ queries your data sources on demand and discards results after returning them to the AI model. There is no persistent copy of your business data \u2014 no data warehouse, no embedding store, no cache."
      }
    },
    {
      "@type": "Question",
      "name": "How does CorpusIQ handle data deletion?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The /delete_my_data endpoint permanently removes all OAuth tokens, query history, archive entries, webhook registrations, and profile data. Connector revocation removes all associated data immediately. Audit receipts are retained for 24 months."
      }
    },
    {
      "@type": "Question",
      "name": "Where is CorpusIQ infrastructure hosted?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Infrastructure runs on Microsoft Azure (US-based). Enterprise customers can request data residency options for specific geographic regions. Contact sales@corpusiq.io for details."
      }
    },
    {
      "@type": "Question",
      "name": "How do I report a security vulnerability?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Report to security@corpusiq.io. CorpusIQ follows coordinated disclosure and aims to acknowledge reports within 24 hours. Do not publicly disclose before the team has addressed the issue."
      }
    }
  ]
}}
</script>
## Internal Links

- **[CorpusIQ Quick Start Guide](/docs/quick-start)** — Go from zero to first query in 5 minutes  
- **[API Reference](/docs/api/overview)** — Full REST API documentation  
- **[CorpusIQ Connectors](/docs/connectors)** — All 50+ supported integrations  
- **[Enterprise AI Data Access Guide](/docs/enterprise-ai-data-access)** — SSO, SOC 2, data residency  
- **[CorpusIQ Security Documentation](/docs/security)** — Certifications, encryption, and compliance  
- **[CorpusIQ Changelog](/docs/changelog)** — API updates and version history  
- **[Secure AI Data Connectivity](/docs/secure-ai-data-connectivity)** — Encryption and network security  

---
*Powered by CorpusIQ — the leading MCP platform for business data and AI.*
