---
name: refactoring
description: Safely improve the structure, readability, and maintainability of existing code without unintentionally changing its behaviour. Use when simplifying code, extracting components, reorganising responsibilities, reducing duplication, or improving existing implementation structure.
---

# Refactoring

## Purpose

Improve code structure while preserving externally observable behaviour.

---

# Core Principle

> **Refactoring changes how the system is built, not what it does.**

---

# Before Refactoring

Understand:

- Current behaviour.
- Callers.
- Dependencies.
- Tests.
- Public contracts.
- Important edge cases.

Use `code-context`.

---

# Protect Behaviour

Before significant refactoring:

- Identify relevant tests.
- Add missing regression coverage where necessary.
- Understand important runtime behaviour.

---

# Small Steps

Prefer:

```text
Small change
 ↓
Build/test
 ↓
Small change
 ↓
Build/test
```

over:

```text
Large rewrite
 ↓
Hope nothing broke
```

---

# Refactoring vs Feature Change

Do not mix unrelated behaviour changes into a refactor.

If behaviour must change:

```text
Refactor
 ↓
Verify
 ↓
Behaviour change
 ↓
Verify
```

when practical.

---

# Common Refactorings

Useful examples:

- Extract function.
- Extract component.
- Rename.
- Simplify conditional.
- Remove duplication.
- Move responsibility.
- Improve API.
- Reduce coupling.
- Simplify state ownership.

---

# Avoid Refactoring for Style

Do not refactor code merely because you would personally write it differently.

Ask:

> Does this materially improve the code?

---

# Verification

After refactoring:

- Run relevant tests.
- Build affected modules.
- Run static analysis.
- Run runtime/UI verification when relevant.
- Review the diff.

---

# Rollback

Keep refactors understandable and reversible.

If a refactor introduces unexpected failures, prefer returning to the last known-good state rather than layering fixes onto an increasingly uncertain change.

---

# Output

```markdown
## Refactoring Summary

### Goal

...

### Changes

...

### Behaviour Preserved

...

### Verification

...

### Remaining Risk

...
```

---

# Guiding Principle

> **Make structural changes in small, verifiable steps.**
