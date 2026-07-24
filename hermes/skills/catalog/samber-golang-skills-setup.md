---
title: Samber Go Skills — Golang Engineering Standards for Hermes Agents
description: Golang code style, error handling, testing, naming, and design patterns with 35K+ combined installs. Enforce idiomatic Go standards across agent-generated code.
---

# Samber Go Skills — Setup Guide

**Source:** [samber/cc-skills-golang](https://skills.sh/samber/cc-skills-golang) (35K+ combined installs)
**Category:** Engineering / Development
**Quality Tier:** 🟢 Production

Comprehensive Golang engineering standards for agents. Enforces idiomatic code style, proper error handling patterns, testing conventions, naming rules, and design patterns. "Clear is better than clever" — Go Proverbs. Designed to produce production-quality Go that passes code review on first submission.

---

## Installation

```bash
npx skills add samber/cc-skills-golang --skill golang-code-style
npx skills add samber/cc-skills-golang --skill golang-error-handling
npx skills add samber/cc-skills-golang --skill golang-testing
npx skills add samber/cc-skills-golang --skill golang-naming
npx skills add samber/cc-skills-golang --skill golang-design-patterns
npx skills add samber/cc-skills-golang --skill golang-structs-interfaces
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **golang-code-style** | 35.6K | Idiomatic Go style — line breaking, variable declarations, composite literals, nil handling |
| **golang-error-handling** | 35.2K | Error wrapping, sentinel errors, custom error types, panic recovery |
| **golang-testing** | 34.8K | Table-driven tests, subtests, mocking, test helpers, benchmarks |
| **golang-naming** | — | Package, variable, function, and interface naming conventions |
| **golang-design-patterns** | — | Functional options, builder, strategy, dependency injection for Go |
| **golang-structs-interfaces** | — | Struct design, interface segregation, embedding best practices |

---

## Key Capabilities

### Code Style Enforcement
- **Line Breaking**: Semantic boundaries over arbitrary column counts; 4+ arguments = one per line
- **Variable Declarations**: `:=` for non-zero values, `var` for zero-value initialization
- **Slice/Map Initialization**: Always explicit, never nil; preallocate when capacity is known
- **Composite Literals**: Always use field names — positional fields break on type changes
- **Nil Handling**: Nil slices serialize to `null` in JSON (vs `[]` for empty) — surprising API consumers

### Error Handling
- Error wrapping with `fmt.Errorf("%w", err)`
- Sentinel errors for package-level error constants
- Custom error types with `Error()` method
- Panic recovery at goroutine boundaries

### Testing Standards
- Table-driven tests as default pattern
- Subtests with `t.Run()` for organized test output
- Test helpers must call `t.Helper()`
- Benchmark functions with `b.N` loop

---

## Quick Start

The skills activate automatically when writing Go code. Key conventions:

```go
// Variables: := for non-zero, var for zero-value
var count int              // zero value, set later
name := "default"          // non-zero

// Slices/Maps: always initialized
users := []User{}                       // never nil
m := make(map[string]int, len(items))   // preallocate when size known

// Composite literals: always use field names
srv := &http.Server{
    Addr:         ":8080",
    ReadTimeout:  5 * time.Second,
    WriteTimeout: 10 * time.Second,
}

// Error handling: wrap with context
if err != nil {
    return fmt.Errorf("processUser: %w", err)
}
```

---

## Verification

```bash
npx skills list | grep samber/cc-skills-golang
```

---

## Notes

- 35K+ combined installs across the Go engineering community
- Designed for Claude Code but directly applicable to any agent writing Go (Hermes, Cursor, Copilot)
- Linters handle formatting; these skills handle clarity and design judgment
- "When ignoring a rule, add a comment to the code" — pragmatic, not dogmatic
- Complements `golangci-lint` for comprehensive Go code quality
