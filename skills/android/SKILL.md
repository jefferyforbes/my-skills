---
name: android
description: Modern Android engineering, architecture, and routing hub. Use when designing, implementing, or debugging Android applications, including Clean Architecture, Jetpack Compose UI, Navigation 3, Wear OS Material3, ViewModels, Coroutines, testing setup, data layer, Gradle build logic, and Koog AI agent integration.
---

# Android Modern Architecture & Modularization

## Operating Contract

This skill operates under the root `AGENTS.md`.

Use Android architecture guidance as a set of strong defaults, not an excuse to retrofit every project into an idealised architecture.

Before changing architecture:

- inspect the existing project structure;
- identify the current conventions;
- determine whether the requested change actually requires architectural change;
- preserve simpler existing patterns when they are sufficient;
- introduce additional layers only when they provide meaningful value.

## Instructions

When designing or refactoring an Android application, prefer modern Android architecture and clear separation of responsibilities where appropriate.

### 1. High-Level Layers
Structure the application into three primary layers. Dependencies must strictly flow **inwards** (or downwards) to the core logic.

*   **UI Layer (Presentation)**:
    *   **Responsibility**: Displaying data and handling user interactions.
    *   **Components**: Activities, Fragments, Composables, ViewModels.
    *   **Dependencies**: Depends on the Domain Layer (or Data Layer if simple). **Never** depends on the Data Layer implementation details directly.
*   **Domain Layer (Business Logic) [Optional but Recommended]**:
    *   **Responsibility**: Encapsulating complex business rules and reuse.
    *   **Components**: Use Cases (e.g., `GetLatestNewsUseCase`), Domain Models (pure Kotlin data classes).
    *   **Pure Kotlin**: Must NOT contain any Android framework dependencies (no `android.*` imports).
    *   **Dependencies**: Depends on Repository Interfaces.
*   **Data Layer**:
    *   **Responsibility**: Managing application data (fetching, caching, saving).
    *   **Components**: Repositories (implementations), Data Sources (Retrofit APIs, Room DAOs, Koog AI Agents).
    *   **Dependencies**: Depends only on external sources and libraries.

### 2. Dependency Injection

Prefer the dependency injection framework already used by the project.

Do not introduce Hilt solely because this skill recommends it.

If the project has no DI framework, choose one based on project size, platform constraints, existing dependencies, and the actual testing/composition requirements. For small applications, direct construction may be preferable.

*   **@HiltAndroidApp**: Annotate the `Application` class.
*   **@AndroidEntryPoint**: Annotate Activities and Fragments.
*   **@HiltViewModel**: Annotate ViewModels; use standard `constructor` injection.
*   **Modules**:
    *   Use `@Module` and `@InstallIn(SingletonComponent::class)` for app-wide singletons (e.g., Network, Database, Koog AI Agents).
    *   Use `@Binds` in an abstract class to bind interface implementations (cleaner than `@Provides`).

### 3. Modularization Strategy
For production apps, use a multi-module strategy to improve build times and separation of concerns.

*   **:app**: The main entry point, connects features.
*   **:core:model**: Shared domain models (Pure Kotlin).
*   **:core:data**: Repositories, Data Sources, Database, Network, Koog Agents (refer to `koog-agent-framework` skill).
*   **:core:domain**: Use Cases and Repository Interfaces.
*   **:core:ui**: Shared Composables, Theme, Resources.
*   **:feature:[name]**: Standalone feature modules containing their own UI and ViewModels. Depends on `:core:domain` and `:core:ui`.

### 4. Checklist for implementation
- [ ] Ensure `Domain` layer has no Android dependencies.
- [ ] Repositories should default to main-safe suspend functions (use `Dispatchers.IO` internally if needed).
- [ ] ViewModels should interact with the UI layer via `StateFlow` (see `references/async/android-viewmodel/SKILL.md`).
- [ ] If using AI agents or Koog framework, isolate Koog dependencies within `:core:data` and refer to the `koog-agent-framework` skill.

---

# Detailed Android References

Use `view_file` to read these deep-dive reference guides when executing specific Android tasks.

## UI Layer
- **[Compose UI](./references/ui/compose-ui/SKILL.md)**: Compose UI patterns, state hoisting, and performance guidelines.
- **[Navigation 3](./references/ui/navigation-3/SKILL.md)**: Jetpack Navigation 3 migration, recipes, type-safe destinations, and scenes.
- **[Wear Compose (M3)](./references/ui/wear-compose-m3/SKILL.md)**: Wear OS Material3 components, Scaffold, and TransformingLazyColumn.
- **[Media3 Cast Integration](./references/ui/media3-cast-integration/SKILL.md)**: Media3 playback, Session, and Cast framework wiring.
- **[Coil Compose](./references/ui/coil-compose/SKILL.md)**: Async image loading with Coil in Compose.

## Async & State
- **[Android ViewModels](./references/async/android-viewmodel/SKILL.md)**: Lifecycle-aware ViewModels, StateFlow, and SavedStateHandle.
- **[Android Coroutines](./references/async/android-coroutines/SKILL.md)**: Coroutines best practices, Dispatchers, and structured concurrency.

## Testing
- **[Android Testing Setup](./references/testing/testing-setup/SKILL.md)**: Minimum test harness setup, JUnit4/5, MockK, and Robolectric.
- **[Android Testing Guide](./references/testing/android-testing/SKILL.md)**: Unit, integration, and UI testing patterns.
- **[Screenshot Debugging Workflow](./references/testing/screenshot-debugging-workflow/SKILL.md)**: Screenshot test failure diagnosis and visual diff verification.

## Data Layer & Build
- **[Data Layer Architecture](./references/data/android-data-layer/SKILL.md)**: Repository pattern, offline-first caching, and Koog agent isolation.
- **[Retrofit Configuration](./references/data/android-retrofit/SKILL.md)**: Network data sources, interceptors, and OkHttp client setup.
- **[Android Gradle Logic](./references/build/android-gradle-logic/SKILL.md)**: Convention plugins, build-logic, and dependency catalogs.

## CLI & Emulators
- **Android CLI & Emulator Controls**: Refer to the global `android-cli` skill.
