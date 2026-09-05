---
name: wear-compose-m3
description: Expert guidance for working with Wear OS Compose Material3. Use this skill when creating, updating, or migrating Wear OS projects (androidx.wear.compose.material3, foundation, navigation3, AppScaffold, ScreenScaffold, TransformingLazyColumn).
---

# Wear OS Compose Material3

## Purpose

Provide authoritative guidance for designing, implementing, and migrating Wear OS apps using Jetpack Compose Material3.

---

# Key Principles & Rules

1. **Use Stable Material3 APIs**: Target `androidx.wear.compose:compose-material3`. Target Kotlin 2.0.0+ with the official Compose Gradle plugin. Ensure `minSdk` is at least 25.
2. **Scaffold Architecture**:
   - Use `AppScaffold` at the root of the app.
   - Use `ScreenScaffold` for each individual screen.
   - Use `TransformingLazyColumn` for scrollable lists (replaces legacy `LazyColumn` / `ScalingLazyColumn`).
3. **No Direct Horologist/Material 2 Dependencies**: Do not use legacy Horologist Composables or Wear Material 2.5 libraries in new/migrated code.
4. **Ambient Mode & Battery Optimisation**: Handle `AmbientMode` callbacks gracefully for always-on displays.
5. **Screenshot & Testing Defaults**: Material3 updates component padding, target sizes, and typography defaults. Prefer Material3 defaults over forced legacy styling.

---

# Component Guidance & Reference Samples

For detailed component sample mappings, migration checklists, and `TransformingLazyColumn` reference implementations, see [references/components.md](file:///Users/jefferyforbes/.gemini/config/skills/wear-compose-m3/references/components.md).
