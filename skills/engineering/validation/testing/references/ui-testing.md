# UI & Screenshot Testing Reference

## Overview

UI tests verify user-visible behaviour, interactions, semantics, and layouts across application states and configurations.

---

## Compose & Declarative UI Testing

For declarative UI frameworks (such as Jetpack Compose):

### Recommended Separation:
- **UI Tests**: User interaction, accessibility semantics, state transitions, user-visible behaviour.
- **Screenshot Tests**: Visual appearance, design fidelity, layout regressions, responsive differences across form factors.
- **Unit Tests**: State transformation, ViewModel/Presenter logic, business invariants.

Do not test business logic through the UI unless the UI behaviour itself is the requirement.

---

## Test Semantics Over Implementation Details

Prefer meaningful semantics rather than implementation details.

For example, match on semantic content:
- Text content, accessibility labels, actions.
- Meaningful test tags or accessibility roles where appropriate.

Avoid tests that depend unnecessarily on:
- Internal view/composable hierarchy.
- Specific layout implementation classes.
- Exact number of intermediary wrapper nodes.
- Arbitrary internal component structures.

Tests should survive reasonable UI refactoring without false failures.

---

## Screenshot Testing

Use screenshot testing when visual regression protection provides meaningful value.

### Good Candidates
- Important core screens and user journeys.
- Design-system components and design tokens.
- Complex layouts with custom drawing/measurement.
- Adaptive layouts (compact vs expanded).
- Regression-prone visual components.

### Common Screenshot States
```text
Default
Loading
Empty
Content
Error
Selected
Disabled
Expanded
Collapsed
Long content
```

Do not create screenshot tests for every trivial static layout.

---

## Deterministic Screenshots

Screenshot tests must be deterministic. Control external variability:
- Random values and dynamic placeholders.
- Current time and dates.
- Live network responses.
- Active animations and transitions (disable or snap animations).
- Font rendering differences across platforms.
- Unstable element ordering.

Always use fixed, predictable test fixtures.

---

## UI State Coverage

For important screens, identify meaningful states. At minimum consider:
```text
Loading
Empty
Content
Error
```

Where relevant:
```text
Partial content
Refreshing
Disabled
Selected
Expanded / Collapsed
Offline
Permission denied
Long content / Large dataset
```

Do not test states that do not exist in the product.

---

## Adaptive UI Testing

Do not validate responsive UI on only one device configuration.

Where relevant, verify:
```text
Compact (phones)
Medium (foldables / small tablets)
Expanded (tablets / desktop / large displays)
```

Also consider:
- Portrait vs. Landscape orientations.
- Resizable windows and split-screen mode.
- System font scaling (large / accessibility typography).

---

## Accessibility Testing

Where relevant verify:
- Content descriptions on visual elements.
- Semantic roles (Button, Heading, Checkbox).
- State descriptions (Checked, Expanded, Selected).
- Minimum touch target sizes (e.g. 48x48 dp).
- Focus behaviour and keyboard navigation order.
