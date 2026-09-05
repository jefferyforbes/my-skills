# Android Testing Matrix, UI Matchers & Recipes

## Purpose

This reference provides detailed dimension matrices for screenshot testing, Compose UI matcher patterns, runtime fakes implementation details, and SQLite database verification recipes.

---

# 1. Screenshot Testing Strategy & Matrix Specifications

Screenshot testing is the recommended way to verify visual appearance in Compose UIs. When designing screenshot suites, balance coverage against maintenance overhead.

### 1.1 Combinatorial Pruning Rule (Avoid Cartesian Explosions)
Do NOT test every permutation of theme, font size, and device screen dimensions:
- Verify multi-dimension layout changes (Compact / Medium / Expanded) in the default theme and font scale.
- Verify font scaling (`1.5x`, `2.0x`) in a single standard theme.
- Verify dark mode/RTL independently without re-testing all screen sizes.
- Focus strictly on unique feedback per screenshot rather than redundant visual combinations.

### 1.2 Screen-Level Multi-Dimension Matrix
Test responsive screen layouts across representative window classes:
- **Widths**:
  - Compact: `400 dp`
  - Medium: `610 dp`
  - Expanded: `900 dp`
- **Heights**:
  - Short: `400 dp`
  - Standard: `500 dp`
  - Tall: `1000 dp`

### 1.3 Variations & Accessibility Matrix
For the standard mobile configuration (`400 x 500 dp`), capture:
- Primary theme variants (Light mode, Dark mode, Dynamic Color).
- Accessibility font scaling set to `1.5x` (or `2.0x` for high-risk text truncation).
- Right-to-Left (RTL) layout direction if localization is supported.

### 1.4 Component-Level Screenshots
Capture standalone UI components in:
- Light and Dark theme variants.
- Default (`1.0x`) and Large (`1.5x`) font scales.
- Interactive states: Default, Pressed/Focused, Disabled, Error/Alert.

### 1.5 Rendering Engines & Reference Image Storage
- **Layoutlib vs. RNG (Robolectric Native Graphics)**:
  - *Layoutlib* (used by Compose Preview Screenshot Testing and Paparazzi): Runs directly on host JVM using Android Studio's preview engine. Fast, lightweight, ideal for static component previews.
  - *RNG* (used by Roborazzi with native graphics): Integrates with full Robolectric runtime, allowing screenshots of complex interactive user states and activity flows.
- **Reference (Golden) Image Storage**:
  - Check PNG reference images directly into Git initially, while keeping overall image counts lean.
  - Transition to Git LFS or a cloud asset service if repository size becomes an issue as suites scale.

---

# 2. Compose UI Behavior & Semantic Matchers

Behavior UI tests analyze the hierarchy and assert properties or simulated interactions.

### 2.1 Framework Selection by Scope
- **Compose Single-App**: Use `ComposeTestRule` (`createComposeRule()` or `createAndroidComposeRule<ComponentActivity>()`). Synchronizes with Compose recompositions, clock, and animations automatically.
- **View Single-App**: Use Espresso (`espresso-core`). Automatically synchronizes with main thread message queue and registered IdlingResources.
- **Cross-App / System Dialogs**: Use UI Automator for multi-process flows (launcher, permissions, system settings).

### 2.2 Matcher Hierarchy
1. **Semantic Matchers (Preferred)**: Match by user-perceivable text, content descriptions, or accessibility actions:
   ```kotlin
   composeTestRule.onNodeWithText("Submit").performClick()
   composeTestRule.onNodeWithContentDescription("Close dialog").performClick()
   ```
2. **Compound Matchers**: Use `hasText` and `hasClickAction` together if text appears multiple times.
3. **`testTag` Rule of Thumb**: Use `Modifier.testTag("tag_name")` ONLY when semantic matchers require more than 3 nested criteria or when testing canvas/custom drawing components.

### 2.3 State Restoration Verification
Verify state survival across configuration changes:
```kotlin
val restorationTester = StateRestorationTester(composeTestRule)
restorationTester.setContent { MyStatefulScreen() }
// Perform interaction...
restorationTester.emulateSavedInstanceStateRestore()
// Assert UI restored correctly...
```

---

# 3. Database Testing Recipes (SQLite / Room / SQLDelight)

Always execute database verification as an instrumented or Robolectric test with an in-memory database:

```kotlin
@RunWith(AndroidJUnit4::class)
class AppDatabaseTest {
    private lateinit var db: AppDatabase
    private lateinit var dao: ItemDao

    @Before
    fun createDb() {
        val context = ApplicationProvider.getApplicationContext<Context>()
        db = Room.inMemoryDatabaseBuilder(context, AppDatabase::class.java)
            .allowMainThreadQueries()
            .build()
        dao = db.itemDao()
    }

    @After
    fun closeDb() {
        db.close()
    }
}
```
