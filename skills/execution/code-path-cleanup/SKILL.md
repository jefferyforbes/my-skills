---
name: code-path-cleanup
description: Ensure that code changes leave the codebase in a clean, consolidated state by identifying and removing obsolete implementation paths, redundant abstractions, compatibility layers, dead code, and duplicated logic.
---

# Code Path Cleanup

## Purpose

Ensure code changes leave the codebase in a clean, consolidated state by identifying and removing obsolete paths, redundant abstractions, dead code, and compatibility layers made unnecessary by recent work.

---

## Core Principle

> **What did this change make obsolete? Make the requested change work, while leaving the simplest correct implementation behind.**

Do not preserve old code merely because deleting it feels risky.

---

## When Cleanup Is Required
- Replacing or refactoring an existing implementation.
- Migrating APIs, data models, or dependency injection modules.
- Removing or updating a feature workflow.
- Consolidating duplicated logic across components.

---

## The Cleanup Procedure

```text
1. Identify Preceding Implementation (What existed before this change?)
       ↓
2. Reference Audit (Find all usages of old classes, methods, flags, routes)
       ↓
3. Migrate Callers (Update consumers to use the new implementation directly)
       ↓
4. Remove Dead Elements (Safely delete obsolete classes, wrappers & unused imports)
       ↓
5. Repository Verification (Re-scan repository to ensure zero broken references)
```

---

## Progressive Disclosure Routing

Load detailed removal checklists via `view_file`:
- **[Dead Code & Obsolete Path Checklist](./references/dead-code-checklist.md)**: Exhaustive audit lists for wrappers, interfaces, factories, DI modules, and unused dependencies.

---

## Completion Criteria
- [ ] No unnecessary `@Deprecated` wrappers remain without documented external consumers.
- [ ] Obsolete implementations are deleted, not commented out.
- [ ] All consumers use the modern implementation directly.
- [ ] Build and automated tests pass cleanly.
