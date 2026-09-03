---
name: architecture
description: Evaluate and design software architecture based on current requirements, system boundaries, ownership, dependencies, and maintainability. Use when introducing features, changing data flow, creating abstractions, moving responsibilities, or making architectural decisions.
---

# Architecture

## Purpose

Make architectural decisions that solve real problems while keeping the system understandable and adaptable.

---

# Core Principle

> **Architecture exists to manage complexity, not to demonstrate sophistication.**

---

# Responsibilities

For a proposed change determine:

- What owns the behaviour?
- Where should it live?
- What does it depend on?
- What depends on it?
- What boundary should exist?
- What should remain local?

---

# Dependency Direction

Prefer dependencies that flow toward stable abstractions.

Avoid unnecessary:

```text
UI → Infrastructure
Domain → UI
Core → Feature implementation
```

---

# Separation of Concerns

Separate responsibilities when doing so creates meaningful value.

Examples:

```text
Presentation
Domain
Data
Infrastructure
```

Do not create layers solely because a textbook architecture contains them.

---

# Abstractions

Create an abstraction when there is a real reason:

- Multiple implementations.
- Dependency isolation.
- Clear boundary.
- Testability.
- Encapsulation.

Avoid abstraction for hypothetical future requirements.

---

# State Ownership

Keep state with the layer responsible for its lifecycle and meaning.

Distinguish:

```text
Business state
UI state
Ephemeral presentation state
```

---

# Module Boundaries

Create or change module boundaries when they provide meaningful:

- Dependency isolation.
- Build isolation.
- Ownership.
- Reuse.
- Platform separation.

Do not create modules merely to make the project look organised.

---

# APIs

Treat APIs as contracts.

Consider:

- Compatibility.
- Ownership.
- Nullability.
- Error semantics.
- Extensibility.
- Versioning.

---

# Architecture Decisions

For meaningful architectural choices explain:

```markdown
### Decision

<Chosen approach>

### Why

...

### Alternative

...

### Trade-off

...

### Future Pressure

<What would cause this decision to need revisiting?>
```

---

# Avoid Over-Engineering

Do not introduce:

- Unnecessary abstractions.
- Excessive layers.
- Generic frameworks.
- Premature modularisation.
- Hypothetical extensibility.

Prefer the simplest architecture that handles current requirements safely.

---

# Architecture Review

Before completing a significant architectural change verify:

- Ownership is clear.
- Dependencies are sensible.
- Boundaries are intentional.
- Existing conventions are respected.
- The solution is not unnecessarily complex.
- Future change remains reasonably easy.

---

# Guiding Principle

> **Choose architecture based on the complexity you actually have, not the complexity you might someday have.**
