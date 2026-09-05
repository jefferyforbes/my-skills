---
name: design
description: Core routing hub for product, interface, and system design. Routes to specialized sub-skills for UI Design (visual hierarchy, layout, typography, tokens), UX Design (user flows, state completeness, accessibility), and System Architecture Design (system boundaries, APIs, data modeling, resilience).
---

# Design Core & Routing Hub

## Purpose

This is the foundational skill for **designing software products, interfaces, and systems**.

Under the root `AGENTS.md` and engineering operating model, design precedes implementation for any non-trivial modification.

This skill acts as a **routing hub**, delegating specialized design tasks into three focused sub-skills:

```text
Design Routing Hub
  ├── Visual styling & spatial systems ──────→ UI Design (`ui/SKILL.md`)
  ├── Flows, state completeness & a11y ─────→ UX Design (`ux/SKILL.md`)
  └── Structural boundaries, APIs & state ───→ System Architecture (`system-architecture/SKILL.md`)
```

---

# Core Principles

1. **Form Follows Function**: Visual styling and system architecture must serve user tasks and operational reliability, never aesthetic vanity or speculative engineering.
2. **Explicitness Over Cleverness**: Obvious interfaces and straightforward data flows outlast complex abstractions and hidden magic.
3. **Graceful Degeneration & State Completeness**: Design for failures, network latencies, empty states, and partial outages as first-class citizens.
4. **Reversible Decisions First**: Favor architectures and UI patterns that preserve optionality and minimize irreversible lock-in.

---

# Sub-Skill Routing

When executing specific design tasks, load the relevant specialist sub-skill on demand by calling `view_file` on the relative path:

## 1. [UI Design](./ui/SKILL.md)
Use when styling, structuring, or refining visual user interfaces:
- **Visual Hierarchy & Scannability**: Guiding user attention with typography weight, contrast, and layout anchors.
- **Spatial Rhythm (8pt / 4pt Grid)**: Disciplined margins, paddings, and component gutters.
- **Design Tokens & Color Architecture**: Semantic tokens (`surface`, `content`, `border`, `status`), dark mode, and theme mapping.
- **Component Craft**: Elevation, micro-interactions, transitions, and hit targets.

👉 Load: `view_file` on `skills/design/ui/SKILL.md`

---

## 2. [UX Design](./ux/SKILL.md)
Use when mapping user journeys, handling edge cases, and ensuring accessible interactions:
- **8-State Completeness Matrix**: Designing for Default, Hover/Focus, Active, Loading, Disabled, Empty, Error, and Truncated states.
- **Cognitive Ergonomics & Forms**: Input validation timing, preserving user input, and progressive disclosure.
- **Mobile & Touch Ergonomics**: Thumb-zone layout, touch target sizes (minimum 48x48dp), and tap separation.
- **Universal Accessibility (a11y)**: WCAG 2.1 AA/AAA contrast ratios, screen reader semantics (`aria-label`, `contentDescription`), and keyboard navigation.

👉 Load: `view_file` on `skills/design/ux/SKILL.md`

---

## 3. [System Architecture Design](./system-architecture/SKILL.md)
Use when designing distributed systems, service boundaries, APIs, or backend architectures:
- **Subsystem Boundaries & Ownership**: Bounded contexts, single source of truth, and failure domain isolation.
- **API Contract Design**: REST, gRPC, and Event-Driven paradigms with idempotency keys, cursor pagination, and structured error schemas.
- **Data & State Modeling**: ACID vs. eventual consistency, optimistic concurrency, and cache-aside architectures.
- **Resilience Engineering**: Circuit breakers, request timeouts, bulkheading, and exponential backoff with full jitter.

👉 Load: `view_file` on `skills/design/system-architecture/SKILL.md`

---

# Design Composition Rules

Skills compose across the design and engineering lifecycles. For example:

### Feature / Screen Creation:
```text
Requirements Analysis
       ↓
ux-design (Flows, State Completeness, a11y)
       ↓
ui-design (Layout, Tokens, Typography, Spacing)
       ↓
implementation-plan
       ↓
Implementation & Verification
```

### Subsystem / Backend Feature:
```text
Requirements Analysis
       ↓
system-architecture (Boundaries, API Contracts, State Models)
       ↓
implementation-plan
       ↓
Implementation & Verification
```

### Full-Stack Product Feature:
```text
Requirements Analysis
       ↓
system-architecture (Data contracts & APIs)
       ↓
ux-design (Screen states & error recovery)
       ↓
ui-design (Component styling & layout)
       ↓
implementation-plan
```

---

# Verification Contract

Every design decision must be accompanied by proof:
- **UI Verification**: Visual rendering checks, 8pt grid alignment, design token compliance.
- **UX Verification**: State matrix walkthrough (especially Loading, Empty, Error), WCAG contrast checks, touch target validation.
- **System Architecture Verification**: Schema compatibility tests, boundary isolation proof, failure recovery simulations.

---

## Deep Design References
Load on-demand using `view_file`:
- **[Spatial & Token Systems](./references/spatial-and-token-system.md)**: 8pt grid scales, margin intervals, and semantic color token architectures.
