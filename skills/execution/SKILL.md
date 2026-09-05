---
name: engineering-execution
description: Progressive disclosure routing hub for codebase exploration, refactoring, and dead code cleanup during implementation.
---

# Engineering Execution Hub

## Purpose

This is the execution stage of the engineering lifecycle. Execution converts planned designs into clean, correct, verifiable code modifications while leaving the simplest implementation behind.

---

## The Execution Flow

```text
code-context (Locate entry points, trace callers & dependencies)
         ↓
Implementation / refactoring (Apply minimal, verifiable changes)
         ↓
code-path-cleanup (Identify & eliminate obsolete paths, dead code, & redundant wrappers)
```

---

## Specialist Workflows

Load the relevant specialist guide on demand using `view_file`:

- **[Code Context & Navigation](./code-context/SKILL.md)**: Build a focused understanding of entry points, callers, and data flows before touching code.
- **[Refactoring](./refactoring/SKILL.md)**: Safely improve structure and maintainability in small steps without altering observable behavior.
- **[Code Path Cleanup](./code-path-cleanup/SKILL.md)**: Identify and remove obsolete code paths, orphaned functions, and redundant abstractions made unnecessary by changes.

---

## Execution Principle

> **Make the requested change work, while leaving the simplest correct implementation behind.**
