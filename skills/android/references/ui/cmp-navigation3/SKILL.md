---
name: cmp-navigation3
description: Compose Multiplatform (CMP) Navigation 3 architectural patterns, recipes, type-safe destinations, NavDisplay, scene strategies, and ViewModel retention across Android, iOS, and Desktop.
license: Apache-2.0
metadata:
  author: Jeffery Forbes
  last-updated: '2026-09-05'
  keywords:
  - Compose Multiplatform
  - Navigation 3
  - NavDisplay
  - CMP
  - Android
  - iOS
  - Desktop
  - ViewModel
  - Scenes
  - Backstack
---

# Compose Multiplatform (CMP) Navigation 3

## Overview

Jetpack Navigation 3 provides a declarative, list-driven backstack architecture natively compatible with Compose Multiplatform (`org.jetbrains.navigation3:navigation3-ui` and `org.jetbrains.lifecycle:lifecycle-viewmodel-navigation3`).

Unlike Navigation 2's string-based routes and `NavController`, Navigation 3 treats the backstack as a simple observable collection of type-safe key objects (`List<Any>`), delegating UI rendering to a `NavDisplay`.

---

## 1. Core Concepts & Principles

1. **Explicit, Observable Backstack**: The backstack is managed as an observable list (`SnapshotStateList<Any>` or `List<NavKey>`). Navigating forward is `backStack.add(Key)`, popping is `backStack.removeLast()`.
2. **Key-to-Content Mapping**: The `entryProvider` DSL maps each key class to a `NavEntry`, returning the appropriate Composable.
3. **Target Portability**: UI and navigation code remain identical across Android, iOS, and Desktop (JVM). Platform-specific behavior (like Android system back button or predictive back) is bridged automatically via `NavDisplay`.
4. **Lifecycle & Scoped ViewModels**: Use `lifecycle-viewmodel-navigation3` to ensure ViewModels survive within the lifecycle scope of their backstack entry and clean up when popped.

---

## 2. Dependency Setup (CMP `build.gradle.kts`)

```kotlin
// In shared or feature build.gradle.kts
commonMain.dependencies {
    // Navigation 3 Core UI & ViewModel integration for Compose Multiplatform
    implementation(libs.jetbrains.navigation3.ui)
    implementation(libs.jetbrains.lifecycle.viewmodelNavigation3)
    
    // Core Compose
    implementation(libs.compose.runtime)
    implementation(libs.compose.foundation)
    implementation(libs.compose.material3)
    implementation(libs.compose.ui)
}
```

---

## 3. Defining Type-Safe Keys

Model destinations as pure Kotlin `@Serializable` data classes or objects:

```kotlin
package com.example.app.navigation

import kotlinx.serialization.Serializable

sealed interface Screen {
    @Serializable
    data object Home : Screen

    @Serializable
    data class PatientDetail(val patientId: String) : Screen

    @Serializable
    data class SessionRecording(val sessionId: String, val autoStart: Boolean = false) : Screen

    @Serializable
    data class SessionReview(val sessionId: String) : Screen
}
```

---

## 4. Backstack State Management & `NavDisplay`

Set up the top-level navigation container using `rememberNavBackStack` or a `mutableStateListOf`:

```kotlin
@Composable
fun AppNavigation(
    modifier: Modifier = Modifier,
    initialScreen: Screen = Screen.Home
) {
    // Observable backstack state
    val backStack = rememberMutableStateListOf<Any>(initialScreen)

    NavDisplay(
        backstack = backStack,
        modifier = modifier,
        onBack = {
            if (backStack.size > 1) {
                backStack.removeLast()
            }
        },
        entryProvider = { key ->
            when (key) {
                is Screen.Home -> NavEntry(key) {
                    HomeScreen(
                        onPatientClick = { patientId ->
                            backStack.add(Screen.PatientDetail(patientId))
                        },
                        onNewSession = { sessionId ->
                            backStack.add(Screen.SessionRecording(sessionId, autoStart = true))
                        }
                    )
                }

                is Screen.PatientDetail -> NavEntry(key) {
                    PatientDetailScreen(
                        patientId = key.patientId,
                        onBack = { backStack.removeLast() },
                        onStartSession = { sessionId ->
                            backStack.add(Screen.SessionRecording(sessionId))
                        }
                    )
                }

                is Screen.SessionRecording -> NavEntry(key) {
                    SessionRecordingScreen(
                        sessionId = key.sessionId,
                        onFinished = { sessionId ->
                            // Replace recording screen with review screen
                            backStack.removeLast()
                            backStack.add(Screen.SessionReview(sessionId))
                        },
                        onCancel = { backStack.removeLast() }
                    )
                }

                is Screen.SessionReview -> NavEntry(key) {
                    SessionReviewScreen(
                        sessionId = key.sessionId,
                        onDone = {
                            // Pop back to Home
                            while (backStack.size > 1) {
                                backStack.removeLast()
                            }
                        }
                    )
                }

                else -> null
            }
        }
    )
}
```

---

## 5. Scoped ViewModels with Navigation 3

In CMP, retain ViewModels per `NavEntry` using `viewModel()` or `NavEntry`-scoped lifecycle:

```kotlin
@Composable
fun SessionReviewScreen(
    sessionId: String,
    onDone: () -> Unit,
    viewModel: SessionReviewViewModel = viewModel {
        SessionReviewViewModel(sessionId = sessionId)
    }
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    SessionReviewContent(
        state = uiState,
        onSaveNote = viewModel::saveNote,
        onDone = onDone
    )
}
```

When `backStack.removeLast()` is invoked, the `NavEntry` is discarded, and its associated `ViewModelStore` is cleared, executing `ViewModel.onCleared()`.

---

## 6. Multi-Pane & Adaptive Layouts (Scenes)

Navigation 3 allows inspecting more than one backstack key simultaneously for adaptive two-pane or list-detail layouts:

```kotlin
@Composable
fun AdaptiveNavigation(
    isExpandedScreen: Boolean,
    backStack: MutableList<Any>,
    modifier: Modifier = Modifier
) {
    if (isExpandedScreen) {
        // Dual pane: List on the left, Detail or placeholder on the right
        val detailKey = backStack.findLast { it is Screen.PatientDetail || it is Screen.SessionReview }

        Row(modifier = modifier.fillMaxSize()) {
            Box(modifier = Modifier.weight(1f)) {
                HomeScreen(
                    onPatientClick = { id ->
                        backStack.removeAll { it is Screen.PatientDetail }
                        backStack.add(Screen.PatientDetail(id))
                    },
                    onNewSession = { /* ... */ }
                )
            }
            Box(modifier = Modifier.weight(1.5f)) {
                if (detailKey is Screen.PatientDetail) {
                    PatientDetailScreen(patientId = detailKey.patientId, onBack = {})
                } else {
                    EmptyDetailPlaceholder()
                }
            }
        }
    } else {
        // Standard single-pane NavDisplay
        NavDisplay(
            backstack = backStack,
            onBack = { if (backStack.size > 1) backStack.removeLast() },
            entryProvider = { /* entry provider mappings */ }
        )
    }
}
```

---

## 7. Migration Checklist from Navigation 2

- [ ] Remove `NavHost`, `NavGraphBuilder.composable("route/{id}")` string routes.
- [ ] Define sealed interface / class hierarchy with `@Serializable` for all destination keys.
- [ ] Replace `navController.navigate(Route)` with `backStack.add(Key)`.
- [ ] Replace `navController.popBackStack()` with `backStack.removeLast()`.
- [ ] Replace `NavHost` with `NavDisplay(backstack, entryProvider = { ... })`.
- [ ] Update ViewModel resolution to use `viewModel` from `lifecycle-viewmodel-navigation3`.
- [ ] Verify back handling on Android (Predictive Back), iOS (Swipe gesture / UI back button), and Desktop (Window controls / Escape key).
