---
name: testing
description: Determine and implement the appropriate testing strategy for code changes. Use when adding features, fixing bugs, refactoring code, or validating behaviour to decide what should be tested, at which level, and how to create meaningful, deterministic, maintainable tests whose names clearly describe the behaviour they protect.
---

# Testing Strategy & Verification

## Purpose

Create automated tests that protect **important behavior**, rather than tests that merely inflate code coverage metrics or test counts.

---

## Core Principle

> **Test behavior, not implementation details.**
> What meaningful behavior would become unsafe if this test disappeared?

---

## Testing Workflow

```text
1. Understand Invariants (Identify critical business contracts & edge cases)
       ↓
2. Choose Test Level (Unit → Integration → UI → End-to-End)
       ↓
3. Write Deterministic Test (Descriptive behavioral name)
       ↓
4. Verify Failure (Confirm test fails without the fix/feature)
       ↓
5. Implement & Pass (Verify test passes with minimal correct code)
```

---

## Choose the Smallest Appropriate Test Level

```text
Unit Tests: Pure business logic, state transformations, ViewModels, mappings.
      ↓
Integration Tests: Repository contracts, database operations, multi-component coordination.
      ↓
UI & Interaction Tests: User visibility, accessibility semantics, state transitions.
      ↓
Screenshot Tests: Visual regression, responsive layouts, design token compliance.
```

---

## Progressive Disclosure References

Load specialized guides on demand using `view_file`:
- **[Test Naming & Documentation](./references/test-naming.md)**: Naming tests as behavioral contracts (`showsErrorWhenTaskCreationFails`).
- **[UI & Screenshot Testing](./references/ui-testing.md)**: Declarative UI testing, screenshot determinism, responsive form factors.
- **[Test Doubles, Fakes & Determinism](./references/test-doubles-and-fakes.md)**: Fakes vs mocks, controlling time, eliminating flaky concurrency.

---

## Verification Checklist
- [ ] Test names clearly communicate the protected behavior without inspecting the code body.
- [ ] Tests are deterministic (no arbitrary `sleep`, uncontrolled clocks, or live network).
- [ ] For bug fixes: A regression test reproduces the issue before fixing it.
- [ ] All automated tests pass via CLI command.
