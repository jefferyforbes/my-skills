---
name: code-path-cleanup
description: Ensure that code changes leave the codebase in a clean, consolidated state by identifying and removing obsolete implementation paths, redundant abstractions, compatibility layers, dead code, and duplicated logic.
---

# Code Path Cleanup

## Purpose

Ensure that code changes leave the codebase in a clean, consolidated state by identifying and removing obsolete implementation paths, redundant abstractions, compatibility layers, dead code, and duplicated logic introduced or made unnecessary by the change.

The goal is not simply:

> "Make the requested functionality work."

The goal is:

> **"Make the requested functionality work while leaving the simplest correct implementation behind."**

AI-generated code frequently preserves existing code paths unnecessarily because modifying or deleting existing code introduces perceived risk. This skill exists to counter that behaviour.

---

## Core Principle

### Every implementation change must answer:

> **What did this change make obsolete?**

When introducing a new implementation, the agent must actively determine whether the previous implementation, abstraction, or code path is still required.

Do not preserve old code merely because it is easier or safer to leave it in place.

---

## No Unnecessary Compatibility Layers

Do not introduce or preserve compatibility layers unless there is an explicit requirement for them.

Avoid patterns such as:

```kotlin
@Deprecated
fun oldMethod() = newMethod()
```

when `oldMethod()` has no legitimate remaining consumers.

Avoid:

```text
OldService
    ↓
NewService
    ↓
Implementation
```

when callers can use:

```text
Callers
    ↓
NewService
```

directly.

Compatibility should be intentional, not accidental.

---

## When Cleanup Is Required

Perform code-path analysis whenever a change:

- Replaces an existing implementation
- Refactors an existing component
- Changes an API
- Introduces a new abstraction
- Changes a repository or data source
- Replaces business logic
- Changes dependency injection
- Migrates from one architecture/pattern to another
- Removes or changes a feature
- Introduces a new UI implementation
- Replaces state management
- Changes navigation
- Changes persistence
- Consolidates duplicated logic
- Makes an existing class, method, interface, or dependency potentially unnecessary

Small changes do not require unnecessary refactoring, but the agent must still check whether the change invalidated an existing path.

---

# Code Path Analysis

After implementation, identify the previous implementation or path affected by the change.

Ask:

1. What implementation existed before this change?
2. What implementation exists now?
3. Which callers use the old implementation?
4. Is the old implementation still required?
5. Is any abstraction now redundant?
6. Are there now multiple ways to perform the same operation?
7. Did the new implementation make any code unreachable?
8. Did the change make any parameters, dependencies, state, or interfaces unnecessary?
9. Are there compatibility wrappers that no longer serve a purpose?
10. Are there feature flags or transitional mechanisms that are now obsolete?

Do not assume that unused-looking code is obsolete without checking references.

---

# Reference Analysis

Before deleting an existing implementation:

### 1. Search for references

Find all usages of:

- Classes
- Interfaces
- Functions
- Properties
- DI bindings
- Factory methods
- Extensions
- Navigation destinations
- Routes
- Database entities
- Serializers
- Feature flags
- Configuration
- Tests

### 2. Update callers

Where appropriate, migrate callers to the new implementation.

Prefer direct usage of the new implementation over retaining an unnecessary intermediary.

### 3. Search again

After migration, search the repository again for references to the old implementation.

The expected result should be:

```text
OldImplementation → 0 meaningful references
```

Only then should it normally be removed.

---

# Remove Obsolete Code

When the old path is no longer required, remove it completely.

Look for:

- Obsolete classes
- Obsolete interfaces
- Obsolete functions
- Compatibility wrappers
- Dead branches
- Duplicate implementations
- Duplicate business logic
- Unused parameters
- Unused state
- Unused imports
- Unused dependencies
- Obsolete DI bindings
- Redundant factories
- Redundant adapters
- Obsolete feature flags
- Transitional code
- Dead navigation routes
- Obsolete test helpers
- Tests that only validate removed behaviour

Do not leave behind code simply because it is harmless.

---

# Avoid Partial Migration

Do not leave the codebase in a state where both the old and new approaches are unnecessarily supported.

Avoid:

```text
                    ┌── OldImplementation
Callers ────────────┤
                    └── NewImplementation
```

when the desired architecture is:

```text
Callers
   ↓
NewImplementation
```

Likewise, avoid introducing a new abstraction while leaving the previous abstraction fully intact unless both are genuinely required.

---

# Simplification

After removing the obsolete path, look for opportunities to simplify the resulting implementation.

Consider whether cleanup allows you to remove:

- An interface
- A wrapper
- A factory
- A mapper
- A repository layer
- A ViewModel dependency
- A state holder
- A parameter
- A configuration value
- A dependency
- A test fixture
- A utility function

Do not refactor unrelated areas simply because they could be improved.

The scope of cleanup should be directly related to the implementation being changed.

---

# Compatibility Exceptions

Do **not** automatically delete old implementations.

Preserve them when there is a legitimate reason, such as:

- Public API compatibility
- External consumers
- Database migration requirements
- Backwards-compatible data handling
- Staged rollout
- Feature flags
- Platform-specific implementations
- Legacy data that still needs to be supported
- Explicit product requirements
- Explicit architectural requirements

When preserving an old path, understand and document why it must remain.

The agent should be able to answer:

> **"Why does this old implementation still exist?"**

If there is no clear answer, investigate whether it should be removed.

---

# Testing After Cleanup

Cleanup must not reduce confidence in the implementation.

After removing an obsolete path:

1. Run relevant unit tests.
2. Run relevant integration tests.
3. Run static analysis.
4. Run the build.
5. Run relevant UI tests where applicable.
6. Verify that the new implementation is still exercised.
7. Verify that removed functionality was not unintentionally required elsewhere.

Tests should be updated alongside the code.

Do not preserve obsolete tests solely because deleting them feels risky.

---

# Test Naming

When modifying tests during cleanup, ensure test names clearly describe the behaviour being verified.

Prefer:

```text
completingTask_persistsCompletedState
```

over:

```text
testCompleteTask
```

Test names should communicate:

- The scenario
- The relevant action or condition
- The expected behaviour

A test should be understandable without reading its implementation.

---

# Repository Verification

Before declaring the task complete, perform a final repository search for the old implementation.

Look for:

- Old class names
- Old method names
- Old interfaces
- Old DI bindings
- Old feature flags
- Old routes
- Old configuration
- Old imports
- Old test references

The final result should demonstrate that the obsolete path has either:

### Been removed

or:

### Been intentionally retained for a documented reason.

---

# Cleanup Checklist

Before finishing:

- [ ] Identified the implementation/path replaced by the change
- [ ] Searched for references to the old path
- [ ] Migrated remaining callers where appropriate
- [ ] Removed obsolete implementations
- [ ] Removed redundant abstractions
- [ ] Removed unnecessary compatibility wrappers
- [ ] Removed dead branches
- [ ] Removed obsolete DI/configuration
- [ ] Removed obsolete tests and test helpers
- [ ] Removed unused imports/dependencies
- [ ] Searched again for references to the old path
- [ ] Confirmed the new implementation is the canonical path
- [ ] Confirmed any retained legacy path has a legitimate reason
- [ ] Ran relevant tests
- [ ] Ran static analysis
- [ ] Verified the build
- [ ] Left the repository in a clean state

---

# Completion Criteria

A task is not considered fully complete merely because the new functionality works.

The task is complete when:

1. The requested behaviour works.
2. The new implementation is correctly integrated.
3. Obsolete implementation paths have been removed where appropriate.
4. There is no unnecessary duplication between old and new approaches.
5. Remaining legacy code has a legitimate reason to exist.
6. Tests and verification pass.
7. The resulting codebase is simpler or at least no more complex than necessary.

## Final Question

Before completing the task, ask:

> **"If another engineer opened this codebase tomorrow, would they see one clear way to do this, or would they see multiple historical ways that happen to still work?"**

Prefer **one clear canonical implementation** whenever the requirements allow it.
