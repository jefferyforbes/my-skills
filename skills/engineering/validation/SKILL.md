---
name: engineering-validation
description: Progressive disclosure routing hub for testing strategy, threat-based security review, and multi-dimensional code reviews.
---

# Engineering Validation Hub

## Purpose

This is the validation stage of the engineering lifecycle. Validation provides rigorous empirical proof that implementations satisfy behavioral contracts, prevent regressions, and meet security and quality standards.

---

## The Validation Flow

```text
testing (Choose smallest test level: Unit → Integration → UI)
         ↓
security (Evaluate trust boundaries, input validation, & data exposure)
         ↓
code-review (Multi-dimensional review: Correctness → Safety → Maintainability)
```

---

## Specialist Workflows

Load the relevant specialist guide on demand using `view_file`:

- **[Testing (Strategy & Levels)](./testing/SKILL.md)**: Implement the smallest appropriate automated tests protecting meaningful behavior over implementation details.
- **[Security Review](./security/SKILL.md)**: Evaluate realistic threats, trust boundaries, credentials, injection risks, and sensitive data protection.
- **[Code Review](./code-review/SKILL.md)**: Review code for correctness, lifecycle safety, maintainability, edge cases, and architectural integrity.

---

## Validation Principle

> **Compilation is not proof. Verify observable behavior, not implementation details.**
