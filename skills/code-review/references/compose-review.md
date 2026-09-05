# Compose & Declarative UI Review Reference

This reference provides specialized review criteria for Jetpack Compose and Compose Multiplatform code.

---

## 1. State Hoisting & Recomposition

- **State Hoisting**: Do composables accept state and expose lambda events, or do they mutate state internally?
- **Expensive Computations**: Ensure expensive transformations (formatting, filtering, sorting) are wrapped in `remember` or calculated upstream in the ViewModel.
- **`derivedStateOf`**: Use only when a calculation observes rapidly changing state (e.g. scroll offset) but emits coarse updates.
- **Unnecessary Recomposition**: Check that parameters passed to composables are stable. Avoid passing ViewModels directly into reusable leaf components.

---

## 2. Side Effects & Modifiers

- **Side Effect Lifecycle**: Verify `LaunchedEffect` and `DisposableEffect` have appropriate key parameters. Ensure `rememberCoroutineScope` is only called within user interaction callbacks.
- **Modifier Ordering**: Modifier order matters (`Modifier.padding(...).clickable(...)` vs `clickable(...).padding(...)`). Reusable components must accept `modifier: Modifier = Modifier` as the first optional parameter.
- **Layout Constraints**: Check for unbounded height in lazy layouts, improper weights, or missing `fillMaxWidth()`.
