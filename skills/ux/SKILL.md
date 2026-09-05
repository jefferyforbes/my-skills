---
name: ux-design
description: UX patterns, interaction design, user flows, state completeness, cognitive ergonomics, and accessibility (a11y). Use when mapping user journeys, handling edge cases, and ensuring accessible, resilient interactions.
---

# UX Design & Interaction Architecture

## Purpose

This skill guides user experience architecture, flow design, edge-case mitigation, state coverage, and accessibility compliance. It ensures products are intuitive, resilient to human and network error, and accessible to all users.

---

## Core Principles

1. **State Completeness**: A screen is never merely "the happy path". Every feature must explicitly design and handle all 8 canonical states.
2. **Cognitive Load Reduction**: Minimize working memory requirements. Chunk long tasks, provide smart defaults, and make system state legible.
3. **Forgiving by Design**: Prevent errors before they happen. If an error occurs, provide clear, inline remediation rather than generic dead-ends.
4. **Universal Accessibility (a11y)**: Accessibility is an engineering invariant, not an afterthought. Adhere to WCAG 2.1 AA/AAA criteria across touch, keyboard, and screen readers.

---

## The 8-State Completeness Matrix

Before implementation, audit the target UI against the 8 canonical states:

| State | Definition & UX Requirement | Primary Remediation / Pattern |
| :--- | :--- | :--- |
| **1. Default / Idle** | Normal resting state with clear interactive affordance. | Standard presentation. |
| **2. Hover / Focus** | User is actively targeting the element via pointer or keyboard. | Visible focus ring (`min 3:1` contrast) or surface shift. |
| **3. Active / Pressed** | Tactile confirmation of user input. | Immediate visual/haptic response (< 50ms). |
| **4. Loading / Async** | Waiting on network, computation, or disk. | Skeleton loaders matching content dimensions; disable repeated clicks to prevent double submissions. |
| **5. Disabled** | Action temporarily unavailable. | Explain *why* it is disabled (via tooltip or helper text) or keep enabled and validate on click. |
| **6. Empty** | Zero items exist (fresh account, filtered out). | Welcoming graphic/icon, friendly explanation, unambiguous primary CTA to populate/create. |
| **7. Error** | Network failure, validation error, or server crash. | Inline, contextual error message; keep user input intact; clear retry/recovery button. |
| **8. Partial / Truncated** | Constrained width, overflow text, or degraded network payload. | Elegant ellipsis with tooltip, expandable sheets, graceful fallback. |

---

## Ergonomics & Interaction Dynamics

### 1. Mobile & Touch Ergonomics
- **Thumb Zone**: Place frequent primary actions (bottom navigation, primary CTAs, filters) in the bottom third of the screen. Keep destructive or rare actions out of easy accidental thumb reach.
- **Touch Target Padding**: Expand interactive bounds to at least `48x48dp` (Android) / `44x44pt` (iOS) with minimum `8dp` separating adjacent targets.

### 2. Form & Data Entry UX
- **Inline Validation**: Validate fields on blur or after input settles, not immediately on first keystroke while the user is typing.
- **Preserve User Input**: Never clear form fields on server error or submission failure.
- **Autofill & Input Types**: Explicitly tag input types (`email`, `tel`, `one-time-code`, `credit-card`) to trigger native platform keyboards.

### 3. Progressive Disclosure
- Display essential information upfront; provide secondary details on-demand via accordions, tabs, or modal sheets to avoid overwhelming users.

---

## Accessibility (a11y) Invariants

### 1. Contrast Requirements (WCAG 2.1 AA)
- Normal text (< 18pt or < 14pt bold): **Minimum 4.5:1** contrast ratio against background.
- Large text (≥ 18pt or ≥ 14pt bold): **Minimum 3:1** contrast ratio.
- Non-text UI boundaries & icons: **Minimum 3:1** contrast ratio against adjacent surfaces.

### 2. Screen Readers & Assistive Technology
- Provide descriptive accessibility labels (`contentDescription`, `aria-label`, `accessibilityLabel`) for all icon buttons.
- Avoid vague labels like "Click here" or "Button"; use actionable verbs like "Close dialog" or "Download monthly report".
- Ensure the accessibility reading order logically mirrors the visual flow.

### 3. Keyboard Traversal
- Ensure every interactive element is reachable via `Tab` / arrow keys and actionable via `Enter` or `Space`.
- Never trap keyboard focus within widgets unless explicitly modeling a modal dialog.

---

## Verification & Proof

- [ ] **State Matrix Audit**: Walk through all 8 states (especially Loading, Empty, and Error).
- [ ] **Accessibility Audit**: Verify contrast ratios using automated or manual checkers; verify touch targets.
- [ ] **Keyboard / TalkBack Navigation**: Validate focus traversal and screen reader labels.

👉 **Deep Reference**: Inspect [references/flows-and-accessibility.md](./references/flows-and-accessibility.md) via `view_file` for complete WCAG checklists and state handling patterns.
