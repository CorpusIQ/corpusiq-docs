---
title: Better Auth Skills — Authentication Infrastructure for Hermes Agent Projects
description: Auth best practices, multi-tenancy, 2FA, and security patterns from Better Auth. 203K+ combined installs across 6 skills. Framework-agnostic auth patterns for agent-built applications.
---

# Better Auth Skills — Setup Guide

**Source:** [better-auth/skills](https://skills.sh/better-auth/skills) (203K+ combined installs)
**Category:** Development / Security
**Quality Tier:** 🟢 Production

Complete authentication infrastructure skills from Better Auth — the open-source auth framework. Covers auth best practices, credential management, multi-tenant organization patterns, two-factor authentication, and security hardening. Framework-agnostic patterns applicable to any Hermes agent building user-facing applications.

---

## Installation

```bash
npx skills add better-auth/skills --skill better-auth-best-practices
npx skills add better-auth/skills --skill create-auth-skill
npx skills add better-auth/skills --skill email-and-password-best-practices
npx skills add better-auth/skills --skill organization-best-practices
npx skills add better-auth/skills --skill two-factor-authentication-best-practices
npx skills add better-auth/skills --skill better-auth-security-best-practices
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **better-auth-best-practices** | 78.1K | Core auth patterns — sessions, tokens, OAuth flows |
| **create-auth-skill** | 29.8K | Scaffold complete auth systems from requirements |
| **email-and-password-best-practices** | 26.2K | Credential auth — hashing, reset flows, brute-force protection |
| **organization-best-practices** | 24.9K | Multi-tenant org patterns — RBAC, teams, invitations |
| **two-factor-authentication-best-practices** | 23.4K | TOTP, SMS, passkeys, recovery codes |
| **better-auth-security-best-practices** | 21.3K | Security hardening — CSRF, CORS, rate limiting, audit logs |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Database** | PostgreSQL or SQLite (for session/user storage) |
| **Framework** | Works with any JS/TS framework; native plugins for Next.js, SvelteKit, Nuxt, Astro |

---

## Key Capabilities

### Auth Architecture (best-practices)
Session management, JWT vs opaque tokens, OAuth 2.0/OIDC flows, social login patterns, and refresh token rotation.

### Auth Scaffolding (create-auth-skill)
Generate complete auth systems: database schema, API routes, middleware, email templates, and client SDK setup — all from a requirements prompt.

### Credential Management (email-and-password)
Password hashing (bcrypt/argon2), secure reset flows with time-limited tokens, brute-force detection with progressive delays, and email verification patterns.

### Multi-Tenancy (organization)
Organization/workspace creation, role-based access control (RBAC), team member invitations, domain-based auto-joining, and cross-org access patterns.

### Two-Factor (2FA)
TOTP setup with QR codes, SMS fallback, WebAuthn/passkeys, backup recovery codes, and 2FA enforcement policies.

### Security Hardening (security)
CSRF protection, CORS configuration, rate limiting, session hijacking detection, security audit logging, and GDPR-compliant data handling.

---

## Quick Start

```bash
# Get core auth patterns
npx skills use better-auth/skills@better-auth-best-practices

# Scaffold a complete auth system
npx skills use better-auth/skills@create-auth-skill

# Add 2FA to existing auth
npx skills use better-auth/skills@two-factor-authentication-best-practices

# Hardening review
npx skills use better-auth/skills@better-auth-security-best-practices
```

---

## Verification

```bash
npx skills list | grep better-auth
```

---

## Notes

- Better Auth is the fastest-growing open-source auth framework (40K+ GitHub stars)
- Skills are framework-agnostic — patterns apply to any auth implementation
- Organization and 2FA skills are particularly valuable for SaaS products built by Hermes agents
- Quality tier 🟢 Production: 203K+ combined installs, active maintenance
