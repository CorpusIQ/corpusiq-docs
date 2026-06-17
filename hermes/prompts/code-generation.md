---
title: Code Generation Prompts for Hermes Agent — AI-Powered Development Templates
description: Curated Hermes Agent code generation prompts for writing, refactoring, debugging, and reviewing code. Prompt templates with placeholders for Python, JavaScript, SQL, and more. Model selection guide for code tasks.
category: prompts
tags: [hermes-agent, prompts, code-generation, debugging, refactoring, python, javascript, sql, ai-coding]
last_updated: 2026-06-16
---

# Code Generation Prompts — AI-Powered Development Templates

## How to Use These Prompts

Replace text in `[brackets]` with your project details. For best results, provide concrete examples of input and desired output. These prompts work across Claude, GPT-4, DeepSeek, and other capable models.

---

## Code Generation from Scratch

### Function or Module Generation

```
You are a senior software engineer writing production-quality [LANGUAGE] code.

Generate a [FUNCTION/CLASS/MODULE] that [DESCRIPTION OF WHAT IT SHOULD DO].

Requirements:
- Input: [DESCRIBE INPUT TYPES AND FORMAT]
- Output: [DESCRIBE EXPECTED OUTPUT]
- Error handling: [DESCRIBE EDGE CASES TO HANDLE]
- Performance constraints: [ANY LATENCY OR MEMORY REQUIREMENTS]

Include docstrings, type hints, and inline comments explaining non-obvious logic. Write unit-testable code.
```

### API Endpoint Generation

```
Create a [REST/GRAPHQL/gRPC] endpoint in [FRAMEWORK] for [RESOURCE NAME].

Specifications:
- Method: [GET/POST/PUT/DELETE]
- Path: [/api/v1/resource]
- Authentication: [JWT/API Key/OAuth2/None]
- Request body schema: [DESCRIBE OR PASTE SCHEMA]
- Response format: [DESCRIBE EXPECTED RESPONSE]

Include input validation, proper HTTP status codes, and rate limiting considerations. The endpoint connects to [DATABASE/CACHE/SERVICE].
```

### Full-Stack Scaffold

```
Generate a [FRONTEND FRAMEWORK] + [BACKEND FRAMEWORK] application skeleton for [APP DESCRIPTION].

Include:
- Project structure with clear separation of concerns
- Database schema for [DATABASE TYPE]
- REST API design with [N] endpoints
- Frontend routing with [N] pages
- Authentication flow using [AUTH METHOD]
- Environment configuration template
- README with setup instructions

Use best practices for the chosen stack. Include package.json/requirements.txt with pinned versions.
```

---

## Code Refactoring

### Improving Readability

```
Refactor the following [LANGUAGE] code for readability and maintainability.
Do not change the external behavior — only improve internal structure.

[PASTE CODE HERE]

Focus on:
- Meaningful variable and function names
- Extracting helper functions where logic is repeated
- Reducing nesting depth
- Adding clarifying comments where the intent isn't obvious
- Consistent formatting following [STYLE GUIDE]

Explain each change you made and why.
```

### Performance Optimization

```
Analyze and optimize the following [LANGUAGE] code for performance.

[PASTE CODE HERE]

Context:
- Expected input size: [NUMBER OF RECORDS/FILES]
- Current bottleneck appears to be: [CPU/MEMORY/I/O/NETWORK]
- Target performance: [LATENCY OR THROUGHPUT GOAL]

Identify the top 3 performance issues with complexity analysis.
Provide optimized code with benchmarks before and after where possible.
```

---

## Debugging Assistance

### Error Diagnosis

```
I'm encountering the following error in my [LANGUAGE] application:

[PASTE ERROR MESSAGE AND STACK TRACE]

Relevant code:

[PASTE RELEVANT CODE]

Environment:
- Language version: [VERSION]
- Framework/library versions: [LIST]
- Operating system: [OS]

Explain the root cause, provide the fix, and suggest how to prevent similar issues.
```

---

## Code Review

### Comprehensive Review Prompt

```
You are a lead engineer conducting a code review. Review the following [LANGUAGE] pull request.

[PASTE DIFF OR CODE]

Evaluate across these dimensions (1-10 scale with specifics):
1. Correctness — does it handle edge cases?
2. Security — injection risks, auth bypass, data exposure?
3. Performance — algorithmic complexity, query efficiency?
4. Maintainability — naming, coupling, testability?
5. Test coverage — what scenarios are missing?

Highlight the top 3 issues that must be fixed before merge, and 2-3 suggestions for improvement that are non-blocking.
```

### Security-Focused Review

```
Review this [LANGUAGE] code for security vulnerabilities:

[PASTE CODE]

Check specifically for:
- SQL/NoSQL injection vectors
- XSS vulnerabilities (reflected and stored)
- Insecure deserialization
- Authentication/authorization bypass risks
- Sensitive data in logs or error messages
- Missing input validation or output encoding
- Insecure cryptographic usage

For each finding, categorize as Critical/High/Medium/Low with remediation code.
```

---

## Tips for Better Results

- **Be specific about constraints.** Vague prompts produce generic code. Specify frameworks, patterns, and standards.
- **Provide example input/output.** Show the model what "correct" looks like.
- **Iterate.** Start broad, then refine with follow-up prompts targeting specific functions.
- **Use system role.** Set the model's system prompt to define its persona (e.g., "You are a Rust expert").
- **Chain prompts.** Use code generation → code review → test generation as a pipeline for higher quality output.


---
*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*


---
*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
