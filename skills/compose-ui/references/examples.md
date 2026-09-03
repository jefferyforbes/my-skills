# Device-Agnostic UI

## 9. Design for Window Size, Not Device Type

Do not write UI around assumptions such as:

```text
phone
tablet
foldable
desktop
```

Instead reason about the **available window**.

A tablet in split-screen may have less width than a phone in another configuration.

A foldable may change its available layout space.

A desktop window may be resized arbitrarily.

Therefore:

```text
Available Window
      ↓
Layout Decision
      ↓
Composable UI
```

not:

```text
Device Type
      ↓
Layout
```

Use Window Size Classes and Material 3 Adaptive APIs for app-level layout decisions.

---

## 10. Prefer Responsive Constraints Before Breakpoints

First attempt to make a component naturally adapt to its constraints.

Prefer:

```kotlin
Row(
    modifier = modifier.fillMaxWidth(),
) {
    ...
}
```

with appropriate weights, wrapping, minimum/maximum sizes, and flexible content.

Only introduce explicit layout variants when the UX genuinely needs to change.

---

## 11. Distinguish Responsive from Adaptive UI

### Responsive

The same composition adjusts to available space.

Examples:

- Padding changes
- Content wraps
- Elements resize
- Text reflows

### Adaptive

The composition itself changes.

Examples:

```text
Compact:
Bottom navigation

Medium:
Navigation rail

Expanded:
Navigation rail + additional content
```

Or:

```text
Compact:
List → Detail

Expanded:
List + Detail
```

Use adaptive layouts when additional space provides meaningful UX value.

Do not simply stretch everything across a large screen. Long text and oversized controls can become less usable.

---

# `BoxWithConstraints`

## 12. Use `BoxWithConstraints` for Local Constraint-Based Decisions

`BoxWithConstraints` is useful when a component genuinely needs to respond to the constraints supplied by its parent.

Example:

```kotlin
@Composable
fun AdaptiveContent(
    modifier: Modifier = Modifier,
) {
    BoxWithConstraints(modifier) {
        if (maxWidth < 600.dp) {
            CompactContent()
        } else {
            ExpandedContent()
        }
    }
}
```

Use it when the decision belongs to the component itself.

Do not use `BoxWithConstraints` as a replacement for application-level adaptive layout architecture.

For screen-level layout decisions, prefer window size classes and adaptive APIs.

This creates a useful separation:

```text
App-level adaptation
        ↓
Window Size Class

Component-level adaptation
        ↓
Constraints
```

---

# 13. Avoid Device-Specific Dimensions

Avoid hardcoding layouts around a particular device.

Bad:

```kotlin
if (screenWidth == 1080.dp) {
    ...
}
```

Avoid:

- Device model checks
- Pixel-specific assumptions
- Orientation-only layout logic
- Fixed screen dimensions
- `LocalConfiguration` for layout when window APIs are more appropriate

Prefer constraints, window size classes, and intrinsic layout behaviour.

---

# Layout

## 14. Prefer Standard Compose Layouts

Use:

- `Row`
- `Column`
- `Box`
- `LazyColumn`
- `LazyRow`
- `FlowRow`
- `FlowColumn`
- Material components
- Material 3 Adaptive components

before introducing custom layouts.

Use `Layout` or custom measurement only when standard primitives cannot express the required behaviour.

---

## 15. Use Lazy Containers for Collections

Use:

```kotlin
LazyColumn
LazyRow
LazyVerticalGrid
```

for potentially large or dynamic collections.

Provide stable keys when appropriate:

```kotlin
items(
    items = tasks,
    key = { it.id },
) { task ->
    TaskItem(task)
}
```

Do not use eager `Column` + `forEach` for collections that may grow substantially.

---

# Modifiers

## 16. Every Reusable Composable Should Usually Accept `Modifier`

Preferred:

```kotlin
@Composable
fun ProfileCard(
    modifier: Modifier = Modifier,
) {
    Column(modifier) {
        ...
    }
}
```

The modifier should generally be applied to the component's root UI element.

This allows callers to control:

- Size
- Padding
- Position
- Semantics
- Interaction
- Layout behaviour

without modifying the component itself.

---

## 17. Respect Modifier Ordering

Modifier order matters.

For example:

```kotlin
Modifier
    .padding(16.dp)
    .background(...)
```

does not have the same behaviour as:

```kotlin
Modifier
    .background(...)
    .padding(16.dp)
```

Reason about modifiers as an ordered chain.

Do not reorder modifiers casually during refactoring.

---

## 18. Do Not Overuse Modifier Parameters

A component should normally expose one `modifier`.

Avoid exposing separate:

```kotlin
containerModifier
contentModifier
textModifier
iconModifier
```

unless those are meaningful parts of the component's public API.

---

# State and Recomposition

## 19. Understand Recomposition Before Optimising It

Do not prematurely optimise recomposition.

First make the UI correct and maintainable.

Optimise when:

- Profiling identifies a problem.
- A composable executes expensive work unnecessarily.
- Large lists exhibits poor performance.
- Frequently changing state causes excessive recomposition.

---

## 20. Never Perform Expensive Work Directly During Composition

Avoid:

```kotlin
@Composable
fun Screen(data: List<Item>) {
    val result = expensiveCalculation(data)
}
```

Prefer:

- Precomputed state
- ViewModel/state holder
- `remember` when appropriate
- Derived state
- Background work where appropriate

Remember that `remember` is a composition cache, not a general-purpose data cache.

---

## 21. Use `derivedStateOf` for Derived UI State

Use `derivedStateOf` when a frequently changing state produces a derived value that does not need to update as frequently.

Do not use `derivedStateOf` automatically.

It introduces overhead and is useful only when it prevents unnecessary recomposition.

---

# Stability

## 22. Prefer Stable UI Models

Compose performance benefits when parameters are stable and predictable.

Prefer immutable UI models:

```kotlin
@Immutable
data class TaskUiModel(
    val id: String,
    val title: String,
    val completed: Boolean,
)
```

Use `@Immutable` only when the class genuinely satisfies the immutability contract.

Use `@Stable` only when the type genuinely satisfies Compose's stability guarantees.

Do not add these annotations simply to silence compiler warnings or force performance behaviour.

---

# Side Effects

## 23. Keep Side Effects Explicit

Do not perform side effects directly during composition.

Use appropriate effect APIs when necessary:

- `LaunchedEffect`
- `DisposableEffect`
- `SideEffect`
- `produceState`
- `rememberCoroutineScope`

Choose the smallest appropriate effect.

Effect keys must represent the values that determine whether the effect should restart.

Avoid:

```kotlin
LaunchedEffect(Unit) {
    // everything
}
```

when the effect actually depends on changing inputs.

---

# ViewModels

## 24. Keep ViewModels at Screen/Route Boundaries

Prefer:

```kotlin
@Composable
fun TaskRoute(
    viewModel: TaskViewModel,
) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()

    TaskScreen(
        state = state,
        onEvent = viewModel::onEvent,
    )
}
```

Then:

```kotlin
@Composable
fun TaskScreen(
    state: TaskUiState,
    onEvent: (TaskEvent) -> Unit,
) {
    ...
}
```

This creates a clear separation:

```text
Route
  ↓
State collection / ViewModel
  ↓
Screen
  ↓
Reusable components
```

Prefer lifecycle-aware state collection such as `collectAsStateWithLifecycle()` on Android.

---

# Architecture

## 25. Keep UI Independent from Data Sources

Composable functions should not directly depend on:

- Room
- Retrofit
- Ktor
- repositories
- network clients
- database entities

Translate domain/data models into UI-facing models when this improves separation.

Example:

```text
Repository
    ↓
Domain
    ↓
UiState / UiModel
    ↓
Composable
```

Do not force this abstraction into tiny components where it provides no value.

---

# Design System

## 26. Use the Application Design System

Prefer:

```kotlin
MaterialTheme.colorScheme
MaterialTheme.typography
MaterialTheme.shapes
```

and application-specific design tokens.

Avoid scattering:

```kotlin
Color(...)
16.dp
TextStyle(...)
```

throughout the application when the value represents a design-system decision.

Centralise repeated design decisions.

---

## 27. Avoid Hardcoded Styling

Prefer theme values over hardcoded values.

Bad:

```kotlin
Text(
    color = Color.Black,
    fontSize = 16.sp,
)
```

Prefer:

```kotlin
Text(
    color = MaterialTheme.colorScheme.onSurface,
    style = MaterialTheme.typography.bodyLarge,
)
```

Hardcoded values are acceptable when they represent a component-specific design decision rather than a global design token.

---

# Accessibility

## 28. Accessibility Is Part of Component Design

Reusable components should provide appropriate:

- Content descriptions
- Semantic roles
- Touch targets
- State descriptions
- Keyboard interaction
- Focus behaviour

Do not rely exclusively on visual appearance to communicate meaning.

Icon-only controls should have meaningful accessibility semantics.

---

# Input

## 29. Do Not Assume Touch Is the Only Input

Compose UI should remain usable with:

- Touch
- Mouse
- Trackpad
- Keyboard
- Stylus

Avoid interactions that only make sense through touch.

Adaptive Android guidance explicitly recommends supporting external keyboards, mice, trackpads, and styluses.

---

# Testing

## 30. Build Components That Are Easy to Test

Prefer components that accept explicit state and events.

This makes them suitable for:

- Screenshot tests
- Compose UI tests
- Preview
- Unit testing surrounding state logic

Avoid requiring a ViewModel merely to render a reusable component.

---

# Previewability

## 31. Make UI Previewable

Where practical, reusable and screen-level composables should be previewable with representative state.

Prefer:

```kotlin
@Preview
@Composable
private fun TaskScreenPreview() {
    AppTheme {
        TaskScreen(
            state = TaskUiState.preview(),
            onEvent = {},
        )
    }
}
```

Create preview data rather than requiring real repositories or network calls.

Test important states:

```text
Loading
Empty
Content
Error
Partial content
Long content
Large data sets
```

---

# Resource and Text Handling

## 32. Keep User-Facing Text Out of Reusable Logic

Prefer string resources or the application's localisation system for user-facing text.

Avoid embedding business copy throughout composables.

Reusable components should generally receive text as parameters rather than deciding application-specific copy themselves.

---

# Navigation

## 33. Keep Navigation Outside Reusable UI

Reusable components should emit navigation events rather than directly navigating.

Prefer:

```kotlin
TaskCard(
    onClick = {
        onNavigateToTask(task.id)
    },
)
```

rather than coupling the component to a navigation implementation.

---

# Error, Loading and Empty States

## 34. Treat UI States Explicitly

Prefer an explicit state model:

```kotlin
sealed interface TaskUiState {
    data object Loading : TaskUiState

    data class Content(
        val tasks: List<TaskUiModel>,
    ) : TaskUiState

    data class Error(
        val message: String,
    ) : TaskUiState
}
```

Avoid scattering loading/error flags throughout the UI when the states are mutually exclusive.

However, do not force every screen into a sealed hierarchy if the actual state model is naturally independent.

---

# Performance

## 35. Prefer Correctness Before Micro-Optimisation

Do not:

- Add `remember` everywhere.
- Add `derivedStateOf` everywhere.
- Add `@Stable` everywhere.
- Extract every composable into tiny functions.
- Create complicated custom layouts prematurely.

Use profiling and Compose tooling to identify actual bottlenecks.

---

## 36. Pay Particular Attention to Lists

For large lists:

- Use lazy containers.
- Provide stable keys.
- Avoid expensive work inside item composition.
- Keep item parameters stable where practical.
- Avoid unnecessary state reads.
- Avoid nested scrolling containers unless intentional.

---

# KMP / Platform Agnosticism

## 37. Prefer Platform-Agnostic UI Where Practical

When working in Kotlin Multiplatform / Compose Multiplatform:

Prefer components based on:

- Compose runtime
- Compose UI
- Foundation
- Material
- Shared UI models
- Shared state/events

Avoid Android-specific APIs inside shared UI unless necessary.

Separate platform-specific concerns behind interfaces or platform implementations.

Example:

```text
commonMain
├── UI
├── UI state
├── UI models
└── design system

androidMain
└── Android-specific integration

iosMain
└── iOS-specific integration
```

Do not sacrifice good Android architecture merely to achieve theoretical cross-platform reuse.

The goal is **portable by design**, not platform abstraction for its own sake.

---

# Component Hierarchy

Prefer a hierarchy similar to:

```text
App
 └── Navigation / Window Adaptation
      └── Route
           └── Screen
                ├── Section
                │    └── Component
                └── Component
```

Responsibilities:

### App

Global configuration, theme, navigation, window adaptation.

### Route

ViewModel/state collection and navigation integration.

### Screen

Compose screen structure and state-to-UI mapping.

### Section

Logical grouping of screen content.

### Component

Reusable UI behaviour and presentation.

Avoid allowing lower-level components to reach upward into higher architectural layers.

---

# Adaptive Architecture

For large-screen or multi-window support, prefer:

```text
Window information
        ↓
Adaptive layout decision
        ↓
Screen layout
        ↓
Reusable components
```

Do not scatter window-size checks throughout dozens of components.

Centralise major layout decisions and pass the resulting configuration down.

This makes adaptive behaviour easier to reason about and test.

Use Material 3 Adaptive components where they match the UX instead of rebuilding canonical adaptive patterns manually. Current Android guidance specifically recommends APIs such as `NavigationSuiteScaffold`, `ListDetailPaneScaffold`, and `SupportingPaneScaffold`.

---

# When to Create a New Composable

Create a separate composable when at least one of these is true:

- It has a meaningful reusable responsibility.
- It is reused.
- It has independent state or behaviour.
- It improves readability substantially.
- It needs independent testing or previewing.
- It represents a meaningful UI concept.

Do not extract a composable simply because a function exceeds an arbitrary number of lines.

---

# When NOT to Abstract

Do not create:

- Generic wrappers with no reuse.
- Components with dozens of configuration parameters.
- Design-system abstractions for one-off UI.
- Platform abstractions that provide no real portability.
- State-holder classes for trivial local state.

Prefer duplication over a bad abstraction when the abstraction would make the code harder to understand.

Refactor when actual reuse or complexity demonstrates the need.

---

# Common Anti-Patterns

Avoid:

```text
Composable → ViewModel → Repository
```

inside reusable components.

Avoid:

```text
Device model → Layout
```

Prefer:

```text
Window constraints → Layout
```

Avoid:

```text
Everything is mutable state
```

Prefer explicit state ownership.

Avoid:

```text
One giant Screen composable
```

Prefer meaningful component boundaries.

Avoid:

```text
One generic component with 20 parameters
```

Prefer focused APIs and slot APIs where appropriate.

Avoid:

```text
Every component knows about navigation
```

Prefer events.

Avoid:

```text
Every component has BoxWithConstraints
```

Prefer constraint-based adaptation only where the component genuinely needs it.

---

# Implementation Workflow

When implementing Compose UI:

### 1. Understand the UI requirement

Identify:

- Content
- User interactions
- States
- Navigation events
- Responsive requirements
- Accessibility requirements

### 2. Inspect the existing design system

Look for:

- Theme
- Typography
- Colours
- Spacing
- Existing components
- Existing adaptive patterns

Reuse them.

### 3. Determine state ownership

Identify:

```text
Screen state
Local UI state
Derived state
Events
```

### 4. Determine adaptive behaviour

Ask:

- Does this need to respond to width?
- Does the layout need to change at larger sizes?
- Can the component naturally respond to constraints?
- Should adaptation happen at screen level or component level?

### 5. Design the composable API

Before implementing the body, determine:

```kotlin
@Composable
fun Component(
    state: ...,
    onEvent: ...,
    modifier: Modifier = Modifier,
)
```

### 6. Implement the simplest correct layout

Prefer standard Compose and Material components.

### 7. Add accessibility

Verify semantics and interaction behaviour.

### 8. Verify different states

At minimum consider:

```text
Loading
Empty
Content
Error
Long content
Small width
Large width
```

### 9. Verify behaviour

Run appropriate tests, previews, or manual verification.

### 10. Refactor only where justified

Remove duplication and improve component boundaries based on actual complexity.

---

# Completion Criteria

A Compose implementation is considered complete when:

- [ ] The UI correctly represents its state.
- [ ] State ownership is appropriate.
- [ ] Events flow upward.
- [ ] Reusable components are not coupled to screen/business infrastructure.
- [ ] Reusable composables accept `Modifier` where appropriate.
- [ ] Layout does not rely unnecessarily on a specific device.
- [ ] Window size/adaptive behaviour is handled appropriately.
- [ ] Large layouts do not simply stretch content unnecessarily.
- [ ] Accessibility has been considered.
- [ ] Loading, empty and error states are handled where applicable.
- [ ] Large collections use appropriate lazy containers.
- [ ] Expensive work is not performed unnecessarily during composition.
- [ ] Existing design-system components are reused.
- [ ] Preview/test coverage is appropriate.
- [ ] No unnecessary abstraction has been introduced.

---

# Guiding Principle

Build composables as **small, predictable UI APIs**, not miniature applications.

A good composable should be able to answer:

> What state do I display, what events can I emit, and what space am I given?

It should not need to know:

> What device am I running on, where did this data come from, which screen am I on, or how does the application store it?

Design for the available **window**, not a specific device.

Design APIs for **reuse**, not hypothetical flexibility.

Design state for **clear ownership**, not convenience.

Design architecture for **change**, not maximum abstraction.

---

# Compose UI Testing

## Purpose

Validate that a Jetpack Compose implementation correctly represents the intended UI across:

- Visual appearance
- Layout
- Typography
- Spacing
- Colour
- Components
- Interaction
- State
- Accessibility
- Window sizes
- Device configurations

The goal is to validate **rendered behaviour**, not merely whether the Kotlin code appears correct.

When Android CLI tooling is available, prefer runtime evidence over assumptions.

---

# Core Principle

> **Do not assume the UI is correct because the code looks correct. Render it and verify it.**

Compose UI should be validated through a feedback loop:

```text
Design / Requirement
        ↓
Implementation
        ↓
Build
        ↓
Render
        ↓
Observe
        ↓
Compare
        ↓
Identify discrepancy
        ↓
Fix
        ↓
Render again
```

When visual correctness matters, screenshots and rendered output are evidence.

---

# When to Use

Use this skill when:

- Implementing UI from Figma.
- Recreating an existing design.
- Debugging visual differences.
- Reviewing Compose UI changes.
- Building a new screen.
- Refactoring UI components.
- Testing adaptive layouts.
- Verifying accessibility.
- Verifying interactive behaviour.
- Comparing UI before and after a change.
- A user reports that UI "looks wrong".

Do not use this skill for purely non-visual business logic.

---

# Design Sources

UI intent may come from:

1. Figma.
2. Design specifications.
3. Existing screenshots.
4. Existing application UI.
5. Product requirements.
6. User-provided descriptions.

Treat these as evidence.

If multiple sources conflict, identify the conflict rather than silently choosing one.

---

# Figma Workflow

When a Figma design is available, do not immediately translate individual pixels into Compose code.

First understand the underlying design system and layout structure.

## 1. Inspect the Design

Identify:

- Screen dimensions.
- Layout hierarchy.
- Component boundaries.
- Spacing.
- Padding.
- Typography.
- Colours.
- Shapes.
- Icons.
- Images.
- Alignment.
- States.
- Interactions.

Do not reproduce the Figma frame as one giant composable.

Infer the underlying UI structure.

---

## 2. Identify Design Tokens

Extract recurring:

- Spacing values.
- Typography styles.
- Colours.
- Corner radii.
- Elevations.
- Component sizes.

Map them to the existing design system where possible.

Do not create new tokens merely because Figma contains a value that already has an equivalent project token.

---

## 3. Identify Component Boundaries

Determine which elements are:

- Screen-level structure.
- Sections.
- Reusable components.
- Design-system components.
- Content.
- Decorative elements.

Example:

```text
Screen
 ├── AppBar
 ├── Content
 │    ├── Hero
 │    ├── Summary
 │    └── List
 │         └── Item
 └── BottomAction
```

Avoid translating the entire design into a single screen-level composable.

---

# Implementation Validation

After implementation:

1. Build the application.
2. Verify an appropriate Android device or emulator is available.
3. Install or update the application.
4. Launch the relevant screen.
5. Reproduce the required state.
6. Capture the rendered result where possible.
7. Compare against the intended design.
8. Identify discrepancies.
9. Correct the implementation.
10. Repeat the verification loop.
11. Run relevant automated UI/screenshot tests.
12. Record any remaining verification limitations.

Do not consider visual implementation complete merely because the application builds successfully.

---

# Android CLI & Runtime Verification

## Purpose

When Android CLI tooling is available, use it to validate the actual rendered application rather than relying solely on:

- Source code.
- Static reasoning.
- Compose previews.
- Figma.
- Unit tests.

The Android CLI is a verification tool.

Prefer:

```text
Implement
   ↓
Build
   ↓
Install
   ↓
Launch
   ↓
Interact
   ↓
Capture evidence
   ↓
Compare
   ↓
Fix
```

over:

```text
Implement
   ↓
Assume correct
```

---

# CLI Capabilities

Use the available Android CLI tooling when appropriate to:

- Build the application.
- Install APKs.
- Launch activities.
- Inspect connected devices/emulators.
- Capture screenshots.
- Record screen output where supported.
- Inspect application/logcat output.
- Verify runtime behaviour.
- Reproduce UI states.
- Verify different device/window configurations.
- Collect evidence for visual or behavioural issues.

Use the actual capabilities available in the environment rather than assuming a particular CLI command exists.

---

# Runtime Verification

When the requested change affects UI, prefer runtime verification when practical.

At minimum:

1. Build the relevant application/variant.
2. Verify an appropriate Android device or emulator is available.
3. Install or update the application.
4. Launch the relevant screen.
5. Reproduce the required state.
6. Interact with the UI where relevant.
7. Capture screenshots where visual accuracy matters.
8. Compare against the intended design.
9. Inspect runtime logs if behaviour differs from expectations.
10. Make corrections.
11. Re-run verification.

If the application cannot be built or launched, document the failure rather than claiming the UI was verified.

---

# Device and Emulator Selection

Do not assume a single emulator represents all supported environments.

Select configurations based on the UI being tested.

Consider:

- Screen width.
- Screen height.
- Density.
- Orientation.
- Android version.
- Font scale.
- Window size.
- Resizable/multi-window behaviour.

For adaptive UI, intentionally test meaningful differences in available window space.

Example:

```text
Compact
Medium
Expanded
```

The exact device configuration should be selected based on the application's supported environments.

---

# Screenshot Evidence

When visual correctness is important, use runtime screenshots where possible.

Associate screenshots with:

```text
Device/configuration
Screen/state
Expected result
Observed result
```

Example:

```text
Configuration:
Compact emulator

State:
Task list populated with 5 items

Expected:
List matches design reference

Observed:
Bottom action is positioned higher than expected
```

Do not rely on memory of what the UI looked like.

---

# Visual Comparison

Compare the rendered UI against the intended design systematically.

## Structure

Check:

- Overall hierarchy.
- Section order.
- Element positioning.
- Content relationships.

## Dimensions

Check:

- Component size.
- Button/input dimensions.
- Card dimensions.
- Container dimensions.

## Spacing

Check:

- Outer margins.
- Internal padding.
- Element gaps.
- Section spacing.
- Baseline spacing.

Do not rely solely on visual intuition when exact measurements are available.

---

## Typography

Check:

- Font family.
- Weight.
- Size.
- Line height.
- Letter spacing.
- Text wrapping.
- Alignment.

Text wrapping is particularly important because it can change the entire layout.

Test realistic content rather than only short placeholder text.

---

## Colour

Check:

- Background.
- Surface.
- Primary.
- Secondary.
- Error.
- Disabled states.
- Text.
- Icons.

Prefer existing design-system tokens.

---

## Shapes

Check:

- Corner radius.
- Borders.
- Stroke width.
- Clipping.
- Shadows.
- Elevation.

---

## Icons and Images

Check:

- Correct asset.
- Size.
- Alignment.
- Tint.
- Scaling.
- Cropping.
- Content description where appropriate.

Do not substitute arbitrary icons simply because they are visually similar.

---

# Visual Discrepancy Prioritisation

When the implementation differs from the reference, fix discrepancies in this order:

```text
1. Layout structure
2. Positioning
3. Component sizing
4. Spacing
5. Typography
6. Colour
7. Shapes
8. Minor visual details
```

Do not spend time tuning colours while the underlying layout hierarchy is incorrect.

---

# Avoid Pixel Patching

Do not repeatedly add arbitrary:

```kotlin
.padding(...)
.offset(...)
.width(...)
.height(...)
```

until the screenshot looks approximately correct.

If many compensating modifiers are required, reconsider the layout hierarchy.

Fix the underlying cause rather than compensating for it.

---

# Screenshot Testing

Use screenshot testing when visual regression protection provides meaningful value.

Screenshot tests are particularly useful for:

- Design-system components.
- Important screens.
- Complex layouts.
- Adaptive layouts.
- Regression-prone UI.

A screenshot test should represent a meaningful UI state.

Examples:

```text
Default
Loading
Empty
Error
Populated
Long content
Selected
Disabled
```

Do not create screenshot tests for every trivial composable.

---

# Deterministic Screenshots

Screenshots should be deterministic.

Control or eliminate:

- Random data.
- Current time.
- Network responses.
- Animations.
- Unstable ordering.
- Dynamic content.
- External dependencies.

Use fixed test data.

Example:

```kotlin
TaskUiState(
    tasks = previewTasks,
)
```

rather than loading real production data.

---

# Interaction Testing

Use Compose UI testing to verify semantics and user-visible behaviour.

Verify:

- Clicks.
- Input.
- Scrolling.
- Selection.
- State changes.
- Navigation events.
- Loading.
- Errors.
- Empty states.
- Accessibility actions.

Prefer finding elements through meaningful semantics rather than implementation details.

Prefer:

```kotlin
onNodeWithText("Complete")
```

or appropriate semantic identifiers.

Avoid tests that depend unnecessarily on:

- Internal composable structure.
- Exact node hierarchy.
- Implementation-specific modifiers.

Tests should survive reasonable refactoring.

---

# Semantics

Ensure important UI elements expose meaningful semantics.

Check:

- Text.
- Content descriptions.
- Roles.
- State.
- Actions.
- Labels.

A UI that looks correct but cannot be meaningfully interacted with through accessibility semantics is incomplete.

---

# State Coverage

For every meaningful screen, identify its important states.

At minimum consider:

```text
Loading
Empty
Content
Error
```

When relevant:

```text
Partial content
Refreshing
Disabled
Selected
Expanded
Collapsed
Offline
Permission denied
Long content
Large dataset
```

Do not create states that do not exist in the actual product.

---

# Realistic Data

Do not validate UI exclusively using idealised data.

Test:

- Long titles.
- Long descriptions.
- Missing optional fields.
- Multiple items.
- Zero items.
- Large collections.
- Large numbers.
- Localised text.
- Different text lengths.

Example:

```text
Short:
"Buy milk"

Realistic:
"Prepare presentation for Thursday's product strategy meeting"

Extreme:
"Prepare the revised product strategy presentation including..."
```

The layout should remain usable.

---

# Adaptive UI Testing

Never validate responsive behaviour on only one screen size.

Test meaningful window sizes.

At minimum consider:

```text
Compact
Medium
Expanded
```

Where relevant, also test:

- Landscape.
- Portrait.
- Split-screen.
- Foldable-like dimensions.
- Resizable windows.
- Desktop-sized windows.

The exact configurations should be determined by the UI's expected supported environments.

---

# Device Agnostic Validation

Do not ask:

> Does this look correct on my phone?

Ask:

> Does this layout behave correctly within the available window constraints?

Test different:

- Widths.
- Heights.
- Aspect ratios.
- Density configurations.
- Font scales.

Avoid tying correctness to a particular physical device.

---

# Font Scaling

Test increased font scale.

Verify:

- Text does not clip.
- Important content remains accessible.
- Buttons remain usable.
- Layout does not overlap.
- Text wrapping behaves appropriately.

Do not assume the default font scale is sufficient.

---

# Accessibility Validation

Where possible verify:

- Minimum touch target sizes.
- Content descriptions.
- Semantic roles.
- State announcements.
- Traversal order.
- Keyboard navigation.
- Focus behaviour.

Accessibility is part of UI correctness.

---

# Scroll Validation

For scrollable screens verify:

- Content can reach the bottom.
- Important controls remain accessible.
- Nested scrolling behaves correctly.
- Keyboard interaction does not obscure inputs.
- Large content does not cause unexpected clipping.

Test both short and long content.

---

# Keyboard and Input

For screens containing text input verify:

- Focus.
- Keyboard appearance.
- IME action.
- Input persistence.
- Cursor behaviour.
- Keyboard dismissal.
- Content visibility when the keyboard is open.

Do not assume touch-only interaction.

---

# Compose-Specific Visual Pitfalls

## Modifier Order

Modifier order can change:

- Padding.
- Background.
- Click area.
- Size.
- Clipping.
- Semantics.

Verify modifier order when visual behaviour is unexpected.

---

## Intrinsic Sizing

Be careful when relying on:

- `wrapContent`.
- Intrinsic measurements.
- Weight.
- Minimum/maximum constraints.

Understand which parent determines the child's available space.

---

## Weight

Check whether weighted children behave correctly at different widths.

---

## `fillMaxWidth`

Do not use `fillMaxWidth()` automatically.

Determine whether the design intends:

- Full width.
- Maximum width.
- Content width.
- Constrained width.

---

## `BoxWithConstraints`

Use it when local layout decisions depend on available constraints.

Do not use it to compensate for a poorly structured screen-level adaptive architecture.

---

# Animation

Animations can make screenshot and UI testing unreliable.

When testing:

- Disable or control animations where possible.
- Use deterministic animation clocks when supported.
- Test the final state separately from animation behaviour.

Do not allow timing-dependent tests to become flaky.

---

# Test Pyramid

Prefer the smallest appropriate test.

```text
                 E2E
                  ▲
             UI / Screenshot
                  ▲
             Integration
                  ▲
                Unit
```

## Unit Tests

Use for:

- State transformations.
- Business rules.
- ViewModel logic.

## Compose UI Tests

Use for:

- Interaction.
- Semantics.
- User-visible state.

## Screenshot Tests

Use for:

- Visual appearance.
- Layout regression.

## End-to-End Tests

Use for:

- Critical user journeys spanning multiple layers.

Do not use E2E tests to test behaviour that can be reliably tested at a lower level.

---

# Android CLI Failure Handling

If Android CLI tooling is unavailable or a command fails:

1. Determine whether the failure is environmental or implementation-related.
2. Inspect available output/logs.
3. Attempt safe recovery where appropriate.
4. Do not repeatedly retry the same failing operation without changing the diagnosis.
5. Continue with static or preview-based validation where possible.
6. Explicitly document what could not be verified.

Example:

```markdown
### Verification Limitation

The UI implementation was compiled successfully, but runtime
screenshot verification could not be completed because no
compatible emulator/device was available.
```

---

# Evidence

Every UI conclusion should be based on available evidence.

Evidence may include:

- Figma measurements.
- Screenshot comparison.
- Rendered UI.
- Compose test results.
- Accessibility tree.
- Existing design-system components.
- Existing implementation.
- Runtime behaviour.
- Android CLI output.

Distinguish:

```text
Observed
Inferred
Assumed
Unable to verify
```

Do not claim pixel-level accuracy if no visual comparison was performed.

---

# Evidence Hierarchy

When evidence conflicts, prefer stronger evidence.

Generally:

```text
Observed runtime behaviour
        ↓
Screenshot / UI test result
        ↓
Runtime logs
        ↓
Reference design measurements
        ↓
Compose preview
        ↓
Source-code reasoning
        ↓
Assumption
```

This hierarchy is not absolute.

For example, an explicit product requirement may override an inferred visual behaviour.

When sources conflict, document the conflict.

---

# Uncertainty

If visual correctness cannot be fully verified, explicitly state why.

Examples:

```text
The Figma reference was available, but the exact font was unavailable.
```

```text
The UI was implemented but could not be rendered at expanded width.
```

```text
The screenshot differs from Figma, but the source design uses
a proprietary asset that is unavailable.
```

Do not silently substitute assumptions for missing evidence.

---

# Evidence-Based Completion

Do not say:

```text
The UI is correct.
```

unless sufficient evidence exists.

Prefer:

```text
The populated task screen was verified against the Figma reference
on the compact emulator. Empty and error states were also verified.
Expanded-window behaviour remains unverified.
```

Claims should be proportional to the evidence collected.

---

# Visual Validation Loop

For UI implementation from Figma or another visual reference:

```text
Reference Design
      ↓
Design Decomposition
      ↓
Compose Implementation
      ↓
Android Build
      ↓
Install
      ↓
Launch
      ↓
Navigate to Screen
      ↓
Reproduce State
      ↓
Capture Screenshot
      ↓
Compare
      ↓
Identify Largest Difference
      ↓
Fix Underlying Cause
      ↓
Repeat
```

Do not stop after the first successful render if meaningful discrepancies remain.

---

# Completion Criteria

Compose UI is considered sufficiently validated when:

- [ ] The UI correctly represents its intended state.
- [ ] Important interactions work.
- [ ] Layout structure matches the intended design.
- [ ] Spacing is correct.
- [ ] Typography is correct.
- [ ] Colours are correct.
- [ ] Shapes are correct.
- [ ] Icons/assets are correct.
- [ ] Long content has been considered.
- [ ] Loading, empty, and error states are validated where applicable.
- [ ] Relevant adaptive layouts have been tested.
- [ ] Font scaling has been considered.
- [ ] Accessibility has been considered.
- [ ] Relevant UI tests pass.
- [ ] Screenshot validation has been performed where appropriate.
- [ ] Runtime verification has been performed where practical.
- [ ] Remaining uncertainty is documented.

---

# Output

Return:

```markdown
## Compose UI Test Review

### Result

<Pass | Pass With Issues | Fail | Unable to Verify>

### Tested States

- <state>
- <state>

### Configurations

- <window size>
- <font scale>
- <orientation/device configuration>

### Visual Findings

#### <Severity> <Finding>

**Evidence**

<Observed discrepancy>

**Expected**

<Expected behaviour>

**Recommendation**

<Recommended change>

### Behavioural Findings

- <finding>

### Accessibility

<Findings>

### Evidence

- <Evidence collected>

### Uncertainty

- <Missing evidence or limitation>

### Verification

- <Tests executed>
- <Screenshots captured>
- <Runtime verification performed>
- <Manual verification performed>
```

---

# Final Principle

> **Compose UI is not finished when it compiles. It is finished when its rendered behaviour has been verified against its intended design across the states and environments that matter.**

When visual accuracy matters:

```text
Don't guess.
Render.
Compare.
Measure.
Fix.
Render again.
```
