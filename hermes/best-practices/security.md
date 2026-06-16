# Security Best Practices for Hermes

Hermes connects to your data, executes code, and runs scheduled tasks — all capabilities that require thoughtful security design. This guide covers the non-negotiable practices and the patterns that prevent the most common security failures.

## Token and Credential Management

**Never hardcode credentials in skills, crons, or prompt templates.** Credentials belong in the secrets manager or environment variables, never in version-controlled text. A skill that reads `api_key = "sk-abc123"` is a breach waiting to happen the first time someone shares their skill config.

**Use the principle of least privilege for every connector.** When you authenticate a service (email, CRM, database, cloud provider), grant only the permissions Hermes actually needs. If Hermes only needs to read emails from one label, don't grant full Gmail access. If it only needs `SELECT` on one database table, don't grant write access to the entire database. Create scoped API keys, service accounts, or database roles with explicit permission boundaries.

**Rotate credentials on a schedule.** API keys and tokens should have planned rotation cycles. Quarterly rotation is reasonable for most integrations. Document the rotation procedure for each connector so it's a 5-minute task, not a panic-inducing fire drill when a key expires.

**Never share personal API keys across team members.** Each team member using Hermes should have their own credentials to shared services. This provides audit trails and allows individual revocation without disrupting the team.

## Approval Gates and Human-in-the-Loop

**Write operations require explicit confirmation.** Reading data and generating reports can be automated. Writing data — sending emails, updating CRM records, modifying databases, executing financial transactions — should require human approval. Configure confirmation gates before any destructive or externally-visible action.

**Tier your approval levels:**

- **Tier 0 (read-only):** No approval needed. Data queries, report generation, analysis.
- **Tier 1 (internal write):** One-click confirm. Updating internal notes, creating draft documents, scheduling tasks.
- **Tier 2 (external write):** Explicit confirmation with preview. Sending emails, posting messages, updating customer-facing data.
- **Tier 3 (high-impact):** Multi-step confirmation with reason capture. Financial transactions, bulk data changes, security-sensitive operations.

**Approval gates should show what will happen before it happens.** "Send email to 42 recipients with subject 'Monthly Update'" is a useful confirmation. "Execute command" is not. Show the payload, the targets, and the expected impact.

## Audit Logging

**Log every significant action.** What was done, by whom (which Hermes instance or user), when, with what inputs, and what the result was. This is non-negotiable for production deployments.

**Structured logging beats free-text.** A log entry like `{"action": "email_sent", "recipient_count": 42, "campaign_id": "abc123", "timestamp": "..."}` is queryable and analyzable. "Sent the campaign email" is not.

**Retain logs commensurate with risk.** For financial operations, retain logs for the same period as your financial records. For general operations, 30-90 days is a reasonable starting point. Consider log immutability — append-only stores prevent tampering.

**Review logs periodically.** Unreviewed logs provide no security value. Schedule a weekly 15-minute log review or set up automated anomaly detection that flags unusual patterns (off-hours activity, unexpected data volumes, new tool combinations).

## Secrets and Sensitive Data

**What to never store in Hermes memory, skills, or conversation context:**

- API keys, passwords, or access tokens
- Credit card numbers or financial account details
- Personal identifiable information (PII) unless explicitly required and approved
- Authentication cookies or session tokens
- Private keys or certificates

**Data minimization in context.** When Hermes retrieves data to answer a question, it often brings back more than needed. Strip sensitive fields before the data enters the model's context window. If you're querying a user database for email statistics, you don't need to include home addresses in the context.

**Redact sensitive data in logs.** Accidentally logging a customer's email address or phone number happens more often than anyone admits. Implement log redaction patterns — mask emails, truncate IDs, hash identifiers where full values aren't needed.

## Plugin and Skill Security

**Validate skill provenance.** Before installing a skill from a community marketplace, understand what it does. Read the SKILL.md. Check what tools it calls. Look for network requests to unexpected destinations. Community skills are valuable but they run with your credentials.

**Isolate untrusted code.** If a skill runs custom code (scripts, commands), sandbox it. Run it with minimal filesystem access, network restrictions, and resource limits. A skill that claims to format JSON shouldn't need filesystem write access.

**Version pinning.** Always pin skill and plugin versions in production. Auto-updating dependencies is convenient but introduces supply-chain risk — a compromised update to a popular skill could cascade across many deployments.

## Operational Security Checklist

- [ ] All credentials stored in secrets manager, never in version control
- [ ] Each connector uses scoped, least-privilege credentials
- [ ] Write operations require confirmation gates
- [ ] Audit logging is enabled and logs are reviewed
- [ ] Sensitive data is stripped before entering model context
- [ ] Community skills are reviewed before installation
- [ ] Credentials rotate on a documented schedule
- [ ] Logs are stored in append-only, immutable storage
- [ ] Off-hours or anomalous activity triggers alerts

Security is not a one-time setup. It's a practice. Revisit this checklist monthly.
