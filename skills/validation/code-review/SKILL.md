---
name: code-review
description: Review code for correctness, maintainability, architecture, security, performance, testability, and alignment with existing project conventions. Use when reviewing existing code, evaluating implementation quality, validating code changes, or deciding whether an implementation should be improved before being considered complete.
---

# Code Review & Quality Assurance

## Purpose

Evaluate code based on how well it solves the actual problem within the existing system. The objective is not aesthetic perfection, but to identify meaningful risks, defects, and architectural misalignments.

---

## Core Principle

> **Review for meaningful risk, not personal preference.**
> Ground every finding in repository evidence and observable impact.

---

## Review Priority Hierarchy

Prioritize review findings strictly in this order:

```text
1. Correctness (Logic errors, invalid edge cases, broken state machines)
       ↓
2. Data Integrity (Persistence races, corruption, missing idempotency)
       ↓
3. Security (Trust boundaries, unvalidated input, credential exposure)
       ↓
4. Concurrency & Lifecycle (Thread races, leaking coroutine scopes, deadlock)
       ↓
5. Regression Risk (Broken callers, signature shifts, missing fallback)
       ↓
6. Architecture & Maintainability (Unnecessary complexity, tight coupling)
       ↓
7. Performance & Testability (Hot-loop allocations, untestable hidden state)
```

Do not spend time debating code formatting or style preference.

---

## Progressive Disclosure References

Load specialized framework reviews on demand using `view_file`:
- **[Compose & Declarative UI Review](./references/compose-review.md)**: Recomposition stability, state hoisting, modifier ordering, and side-effect lifecycles.
- **[Kotlin & Modern Idioms Review](./references/kotlin-idioms.md)**: Sealed hierarchies, null safety, structured concurrency, and flow operators.

---

## Review Output Format

```markdown
## Code Review Summary

### Finding 1: [Severity: Critical/High/Medium/Low] <Title>
- **Threat/Defect**: Concrete failure mode under realistic conditions.
- **Evidence**: File path and line number.
- **Impact**: Why this breaks correctness, security, or state.
- **Recommendation**: Minimal correct remediation.

### Overall Assessment
[APPROVE / REQUEST_CHANGES]
```
