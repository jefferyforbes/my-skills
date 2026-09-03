---
name: android
description: Expert guidance on setting up and maintaining a modern Android application architecture using Clean Architecture and Hilt. Use this when asked about project structure, module setup, or dependency injection. Refer to koog-agent-framework skill when integrating Koog AI agents.
---

# Android Modern Architecture & Modularization

## Instructions

When designing or refactoring an Android application, adhere to the **Guide to App Architecture** and **Clean Architecture** principles.

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

### 2. Dependency Injection with Hilt
Use **Hilt** for all dependency injection.

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
- **Compose UI**: `~/.gemini/config/skills/android/references/ui/compose-ui/SKILL.md`
- **Navigation 3**: `~/.gemini/config/skills/android/references/ui/navigation-3/SKILL.md`
- **Wear Compose (M3)**: `~/.gemini/config/skills/android/references/ui/wear-compose-m3/SKILL.md`
- **Media3 Cast Integration**: `~/.gemini/config/skills/android/references/ui/media3-cast-integration/SKILL.md`
- **Coil Compose**: `~/.gemini/config/skills/android/references/ui/coil-compose/SKILL.md`

## Async & State
- **Android ViewModels**: `~/.gemini/config/skills/android/references/async/android-viewmodel/SKILL.md`
- **Android Coroutines**: `~/.gemini/config/skills/android/references/async/android-coroutines/SKILL.md`

## Testing
- **Android Testing Setup**: `~/.gemini/config/skills/android/references/testing/testing-setup/SKILL.md`
- **Android Testing Guide**: `~/.gemini/config/skills/android/references/testing/android-testing/SKILL.md`
- **Screenshot Debugging Workflow**: `~/.gemini/config/skills/android/references/testing/screenshot-debugging-workflow/SKILL.md`

## Data Layer & Build
- **Data Layer Architecture**: `~/.gemini/config/skills/android/references/data/android-data-layer/SKILL.md`
- **Retrofit Configuration**: `~/.gemini/config/skills/android/references/data/android-retrofit/SKILL.md`
- **Android Gradle Logic**: `~/.gemini/config/skills/android/references/build/android-gradle-logic/SKILL.md`

## CLI & Emulators
- **Android CLI & Emulator Controls**: Refer to the global `android-cli` skill.
