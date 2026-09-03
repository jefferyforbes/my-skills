---
name: compose-ui
description: Design, implement, review, and refactor scalable Jetpack Compose UI using modern Android architecture, state management, adaptive layouts, accessibility, performance, and reusable composable design. Validate Jetpack Compose UI against design intent using Android CLI runtime verification, screenshots, Compose UI tests, previews, accessibility semantics, and adaptive layouts.
---

# Compose UI

## Purpose

Build modern, scalable, maintainable Jetpack Compose UI.

The primary goal is not merely to make a UI look correct on one device.

The UI should be:

- Composable
- Reusable
- Testable
- Accessible
- Adaptive
- Device agnostic where practical
- Resilient to changing requirements
- Efficient under recomposition
- Consistent with the application's design system

Prefer simple solutions first. Do not introduce architectural complexity without a demonstrated need.

---

# Core Principles

## 1. Compose Is Declarative

Treat UI as a function of state.

```text
State
  ↓
Composable
  ↓
UI
  ↓
User Event
  ↓
State Update
```

Do not treat composables like mutable Views.

A composable should primarily:

1. Receive state.
2. Render state.
3. Emit events.

Keep business logic and persistent state outside presentation composables unless the state is genuinely local UI state.

---

# 2. Prefer Unidirectional Data Flow

Use:

```text
State ↓
Events ↑
```

State should flow down the hierarchy.

Events should flow upward.

Example:

```kotlin
@Composable
fun TaskItem(
    task: TaskUiModel,
    onComplete: () -> Unit,
) {
    Checkbox(
        checked = task.isCompleted,
        onCheckedChange = { onComplete() },
    )
}
```

Avoid having leaf composables directly manipulate ViewModels, repositories, databases, or application state.

Prefer:

```text
Screen
    ↓
Container
    ↓
Reusable UI
```

rather than:

```text
Reusable UI
    ↓
ViewModel
    ↓
Repository
```

This improves reuse, previewability, testing, and portability.

---

# 3. Hoist State Intentionally

State should be hoisted when doing so improves:

- Reusability
- Testability
- State ownership
- Coordination between components

Use the lowest common owner that needs to read or modify the state.

Do not automatically hoist every piece of state to a ViewModel.

Local UI state can remain local when it has no reason to be shared.

Examples of appropriate local state:

- Expanded/collapsed state
- Temporary animation state
- Scroll position
- Local input state
- Temporary UI selection

Examples of state that generally belongs higher:

- Screen state
- Business state
- Data shared between components
- State that must survive configuration/process recreation

Prefer `rememberSaveable` when local state should survive configuration changes and is saveable.

---

# 4. Separate Stateful and Stateless Composables

When useful, expose a stateless version of a component.

Example:

```kotlin
@Composable
fun SearchField(
    query: String,
    onQueryChange: (String) -> Unit,
    modifier: Modifier = Modifier,
) {
    ...
}
```

Then provide stateful convenience APIs only when they provide meaningful value.

This allows the same component to be driven by:

- ViewModel state
- Local state
- Tests
- Previews
- Different screens
- Different platforms

---

# 5. Design Composables as APIs

A composable is an API.

Treat its parameters as carefully as you would a public Kotlin function.

Prefer:

```kotlin
@Composable
fun ProfileCard(
    profile: ProfileUiModel,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
)
```

over tightly coupled implementations.

Ask:

- Can another screen use this?
- Does it expose only the state it actually needs?
- Can the parent control its behaviour?
- Can it be previewed independently?
- Can it be tested independently?
- Does the API unnecessarily expose implementation details?

---

# Scalable Composable Design

## 6. Design for the Next Use Case, Not Every Possible Use Case

Do not build an abstraction for hypothetical requirements.

Start with the simplest reusable API that satisfies the current requirement.

Generalize when a second real use case demonstrates the need.

Avoid:

```kotlin
UniversalCard(
    title = ...,
    subtitle = ...,
    leadingContent = ...,
    trailingContent = ...,
    footerContent = ...,
    expandable = ...,
    selectable = ...,
    loading = ...,
    ...
)
```

unless the component genuinely needs this flexibility.

Prefer focused components with meaningful APIs.

---

## 7. Separate Layout from Content

Prefer components that describe their responsibility rather than their location.

Good:

```kotlin
TaskList(
    tasks = tasks,
    onTaskClick = onTaskClick,
)
```

Less reusable:

```kotlin
HomeScreenTaskSection(...)
```

The latter couples the component to a specific screen.

A component should generally not know whether it is being rendered inside:

- A screen
- A dialog
- A bottom sheet
- A navigation destination
- A tablet layout
- A desktop window

unless that knowledge is intrinsic to its responsibility.

---

## 8. Use Slots for Genuine Structural Flexibility

When a component needs flexible content, prefer slot APIs.

```kotlin
@Composable
fun Section(
    title: String,
    modifier: Modifier = Modifier,
    actions: @Composable RowScope.() -> Unit = {},
    content: @Composable ColumnScope.() -> Unit,
)
```

Slot APIs are often preferable to adding numerous boolean or nullable parameters.

Use them when the structure genuinely varies.

Do not use slots merely because they are available.

---


---

# Detailed UI Templates & Examples

For comprehensive code templates, layout patterns, preview configurations, and Compose UI test snippets, see [references/examples.md](file:///Users/jefferyforbes/.gemini/config/skills/compose-ui/references/examples.md).
