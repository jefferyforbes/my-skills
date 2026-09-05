# Learning & Decision Reporting: Formats & Examples

## Purpose

This reference provides illustrative concrete examples, format templates, and domain checklists for communicating important technical decisions to the user under the `learning` skill.

---

# 1. Decision Templates & Formats

### Standard Decision Format
```markdown
### Decision — <Short Title>

<What was chosen and why.>

**Trade-off:** <Important downside or alternative that was rejected.>
```

### Trade-Off Comparison Format
```markdown
### Trade-off — <Decision>

**Chosen:** <Approach>
**Alternative:** <Alternative>
**Why:** <Reason>
**Cost:** <Downside>
**When I would choose the alternative:** <Condition>
```

### Workaround / Hack Format
```markdown
### Workaround — <Title>

**Problem:** <Problem>
**Solution:** <Workaround>
**Why:** <Why this is currently necessary>
**Trade-off:** <Cost/risk>
**Better long-term solution:** <If known>
```

---

# 2. Concrete Illustrative Examples

### Example: Architecture & State Hoisting
```markdown
### Decision — Keep state local rather than hoisting to ViewModel

The general architecture favors hoisting screen state, but this state only controls temporary dropdown animation and has no business impact. Keeping it local prevents cluttering the screen ViewModel with transient presentation flags.

**Trade-off:** UI state is held locally in the composable via `rememberSaveable`, which means other sibling composables cannot observe it directly.
```

### Example: Layout & Performance
```markdown
### Decision — LazyColumn vs Column

Used a `LazyColumn` instead of a standard `Column` because the collection size is unbound and driven by network responses.

**Trade-off:** `LazyColumn` adds slight structural overhead and disables eager layout measurement, but avoids composing hundreds of items simultaneously.
```

### Example: Compose Nuance (Modifier Order)
```markdown
### Decision — Modifier padding applied before background

`Modifier.padding(8.dp).background(Color.Gray)` was chosen intentionally. In Compose, modifier order is sequential: applying padding first creates an outer margin around the colored box; reversing it would color the padded area.
```

### Example: Architectural Boundary
```markdown
### Decision — Keep adaptation at the screen level

The window size class decision is handled at the top-level screen container rather than by individual list item components.

**Trade-off:** The parent screen becomes responsible for selecting compact vs expanded item variants, but prevents dozens of child widgets from coupling to window size infrastructure.
```

---

# 3. Domain Checklists for Decision Reporting

Consider providing explanations when making decisions in:
- **Architecture**: State ownership, module boundaries, public interfaces, inversion of control.
- **Compose / UI**: Recomposition triggers, stability, modifier order, adaptive layout breakpoints.
- **Concurrency & Coroutines**: Scope ownership, cancellation handling, dispatcher selection (`Dispatchers.IO` vs `Default`).
- **Data & Persistence**: Schema migrations, transaction isolation, in-memory caching strategies.
- **Performance & Security**: Allocations in render loops, input validation, authentication/token lifecycles.
