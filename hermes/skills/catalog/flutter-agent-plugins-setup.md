---
title: Flutter Agent Plugins — Official Flutter Skills Setup Guide for Hermes Agents
description: "flutter/agent-plugins — the official Flutter team skills: 86 skills, 538.2K total installs. flutter-apply-architecture-best-practices (29.9K), flutter-build-responsive-layout (29.0K), flutter-fix-layout-issues (27.8K), widget/integration testing, routing, localization, plus dart-* and general best-practice skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/flutter-agent-plugins-setup/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes skill", "agent skill", "skill setup", "flutter", "dart", "mobile development"]
---

# Flutter Agent Plugins — Setup Guide

**Source:** [flutter/agent-plugins](https://skills.sh/flutter/agent-plugins)
**GitHub:** [flutter/agent-plugins](https://github.com/flutter/agent-plugins)
**Skills:** 86 skills · 538.2K total installs
**Category:** Mobile Development (Flutter/Dart)
**First Seen:** August 14, 2026 evening sweep
**Quality Tier:** 🟢 Production (official Flutter team)

The official Flutter team ships 86 agent skills covering the complete Flutter development lifecycle: architecture best practices (29.9K installs), responsive layout building (29.0K), layout issue fixing (27.8K), widget and integration testing (27.1K / 26.6K), declarative routing, JSON serialization, localization, widget previews, HTTP usage, state management, theming, animation, navigation, app size reduction, caching, and more. A `dart-*` series covers Dart CLI apps, package maintenance, checks migration, and test coverage, plus cross-cutting skills (`grill-me`, `api-review`, `unix-cli-best-practices`, `code-documentation`).

---

## Installation

```bash
npx skills add flutter/agent-plugins
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Flutter SDK** | Skills operate on Flutter projects — install the SDK and put `flutter` on PATH |
| **Node.js + npx** | Required for the `skills add` installer |
| **Hermes Agent** | Any recent version; skills work with any agent |

## What It Provides

| Capability | Representative Skills | Installs |
|---|---|---|
| Architecture | flutter-apply-architecture-best-practices, flutter-architecting-apps | 29.9K / 10.5K |
| Layout & UI | flutter-build-responsive-layout, flutter-fix-layout-issues, flutter-building-layouts, flutter-theming-apps | 9.6K–29.0K |
| Testing | flutter-add-widget-test, flutter-add-integration-test, flutter-testing-apps, dart-test-coverage | 6–27.1K |
| Routing & Data | flutter-setup-declarative-routing, flutter-implement-json-serialization, flutter-use-http-package, flutter-caching-data | 8.8K–26.5K |
| Localization & Preview | flutter-setup-localization, flutter-add-widget-preview | 25.7K |
| Cross-cutting | grill-me, api-review, unix-cli-best-practices, code-documentation, dart-package-maintenance | 3–6 |

## Quick Start

1. `npx skills add flutter/agent-plugins`
2. In a Flutter project, ask: "apply flutter architecture best practices to this app"
3. "Build a responsive layout for the dashboard screen" — the skill guides the agent through responsive patterns
4. "Add a widget test for the sign-in form" — uses the widget-testing skill

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Mobile client work** | Flutter-based consumer apps or internal tools built by the CorpusIQ team |
| **Test coverage** | widget/integration test skills for CI pipelines on any Dart/Flutter service |
| **Code review** | `grill-me` and `api-review` as pre-merge review passes |
| **Documentation** | `code-documentation` for public API surfaces |

## Limitations / Verification

- Flutter-specific: minimal value for non-Flutter stacks; the general skills (unix-cli-best-practices, code-documentation, api-review) apply anywhere
- Requires the Flutter SDK for the majority of skills to be useful

```bash
flutter --version   # verify SDK
npx skills list | grep flutter
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [ECC Engineering Skills Setup](/hermes/skills/catalog/ecc-engineering-skills-setup/) — general engineering standards

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
