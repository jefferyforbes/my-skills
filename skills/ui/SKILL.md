---
name: ui-design
description: UI craft, visual hierarchy, layout, typography, spatial systems, component design, semantic tokens, and visual styling. Use when styling, structuring, or refining visual user interfaces.
---

# UI Design & Visual Craft

## Purpose

This skill guides the design, implementation, and refinement of visual interfaces. It governs typography, color tokens, spatial rhythm, component aesthetics, and visual hierarchy to ensure clean, high-craft user interfaces.

---

## Core Principles

1. **Hierarchy First**: Every screen must have an unmistakable focal point. Guide the user's eye naturally from primary elements down to secondary metadata.
2. **Systemic Spacing**: Never guess pixel values. Base all layouts, padding, margins, and gutters on a strict 8pt grid with 4pt half-steps.
3. **Semantic Abstraction**: Decouple styling from hardcoded values. UI components consume semantic tokens (`surface-primary`, `text-secondary`, `border-subtle`), never raw palette primitives (`#1E293B`, `blue-500`).
4. **Scannability**: Leverage typography weight, scale, and contrasting values to make dense information rapidly parseable in scanning patterns (F- and Z-patterns).

---

## Workflow & Checklists

### 1. Spatial Rhythm (8pt / 4pt Grid)
Anchor all measurements to the grid:
- **4px / 4dp**: Micro-spacing (icon-to-label offset, badge padding, tag margins).
- **8px / 8dp**: Tight component interior padding, compact list item gutters.
- **12px / 12dp**: Card internal padding on compact/mobile screens.
- **16px / 16dp**: Default screen horizontal margin, form field gutters, standard container padding.
- **24px / 24dp**: Inter-card gutters, spacing between grouped form sections.
- **32px / 32dp**: Major section breaks and modal headers.
- **48px+ / 48dp+**: Hero spacing and breathing room.

**The Law of Proximity**: Related elements (e.g. input label + input field) must be spaced closer (`4-8px`) than unrelated elements (`16-24px`).

### 2. Typographic Scale & Composition
- **Line Length**: Constrain body copy width to `45-75` characters (`~60ch`) for optimal readability.
- **Line Heights**:
  - Headings: Tight (`1.15 - 1.25`) to prevent multiline titles from falling apart.
  - Body copy: Comfortable (`1.4 - 1.6`) for effortless reading.
- **Micro-copy & Captions**: Small, subdued contrast, slightly expanded tracking (`+0.02em` to `+0.05em`) for legibility.

### 3. Design Tokens & Color Architecture
- Organize tokens into three layers:
  ```text
  Primitive Palette (e.g., slate-900, violet-600)
        ↓
  Semantic Tokens (e.g., surface-base, surface-raised, text-primary, border-subtle)
        ↓
  Component Tokens (e.g., button-primary-bg, card-elevation)
  ```
- **Dark Mode / Theming**: Ensure semantic tokens cleanly map to dark variants without inverting semantic intent (e.g. errors remain alerting, elevated surfaces lighten rather than darken).

### 4. Component Craft & Micro-interactions
- **Touch & Hit Targets**: Minimum `48x48dp` (mobile) / `40x40px` (desktop buttons) / `24x24px` (inline links).
- **Transitions**: Keep durations purposeful (`150ms - 250ms`). Ease-out on entry, ease-in on exit.
- **Elevation & Shadows**: Use subtle, multi-layered ambient shadows rather than harsh single-offset drop shadows.

---

## Verification & Proof

- [ ] **Visual Proof**: Capture screenshots or inspect live previews to verify alignment and balance.
- [ ] **Grid Conformance**: Confirm all margins, paddings, and heights align with 8pt/4pt intervals.
- [ ] **Token Discipline**: Inspect code to ensure no raw hex codes or unsanctioned style primitives are hardcoded.

👉 **Deep Reference**: Inspect [references/tokens-and-typography.md](./references/tokens-and-typography.md) via `view_file` for comprehensive typography ratios, token schemas, and theme definitions.
