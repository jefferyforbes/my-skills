---
name: wear-compose-m3
description: Expert guidance for working with Wear OS Compose Material3. Use this
  skill when creating, updating, or migrating Wear OS projects. This includes the
  androidx.wear.compose.material3, androidx.wear.compose.foundation, and androidx.wear.compose.navigation3
  libraries. Also working with core components such as AppScaffold, ScreenScaffold,
  and TransformingLazyColumn, and core Wear OS concepts such as ambient mode. Migration
  from lower versions such as Material 2.5 and Horologist.
license: Complete terms in LICENSE.txt
metadata:
  author: Google LLC
  last-updated: '2026-08-22'
  keywords:
  - Wear OS
  - Compose
  - Material3
  - Horologist
  - TransformingLazyColumn
  - AppScaffold
  - ScreenScaffold
---

## Prerequisites and compatibility

1. **Current Wear OS Compose version in-use:** To find the installed library version, read `gradle/libs.versions.toml` or `build.gradle.kts` directly. Don't run `./gradlew dependencies` or other shell commands to resolve versions.
2. **Wear OS Compose Material3 version:** If an internal tool is available to establish the **latest stable version** `{VERSION}` of `androidx.wear.compose:compose-material3`, use that tool.
   - Otherwise, fetch the [official Maven metadata XML](https://dl.google.com/dl/android/maven2/androidx/wear/compose/compose-material3/maven-metadata.xml) to identify `{VERSION}` (highest number, ignoring `-alpha`, `-beta`, or `-rc`).
3. **Strict compliance:** If a version is listed as stable, you MUST use it, unless overridden by the user. Do not downgrade based on initial "Unresolved reference" errors in the editor or outdated web search results.
4. **Kotlin version:** For Wear Compose Material3, use Kotlin **2.0.0 or
   higher**.
5. **Compose compiler:**
   - If Kotlin version is **2.0.0+** , the project must use the `org.jetbrains.kotlin.plugin.compose` Gradle plugin.
   - If Kotlin version is **\< 2.0.0** , the project must use `kotlinCompilerExtensionVersion` in `composeOptions`, matching the [Compose to Kotlin Compatibility Map](https://developer.android.com/jetpack/androidx/releases/compose-kotlin).
6. **Min SDK:** Ensure `minSdk` is at least **25**.
7. **Sample extraction mandate**: Wear Compose libraries ship with an additional JAR file which contains individual samples for each and every component. You mustn't propose code changes, other than previews or basic changes such as color changes, until the samples in Capability 3 are extracted to the local cache. Library source files are incomplete and NOT a substitute for these samples; bypassing extraction is an environment setup failure.

## Gotchas

1. **Mandatory sync and validation:** After updating versions in `libs.versions.toml` or `build.gradle.kts`, you **must** perform a Gradle sync before refactoring any code. This ensures the environment has resolved the libraries correctly.
2. **Prohibition of guessing (error protocol):** If you encounter an 'Unresolved Reference' or API mismatch after a successful sync, do not attempt to 'fix' it by downgrading the library version.

## Capabilities and tools

### Capability 1: Migration

Use this guidance when migrating from an older version of Wear OS Compose or
Horologist.

1. Unless otherwise indicated by the developer, use the latest stable version of Wear Compose Material3 from `{VERSION}`.
2. Read the [migration guide](./android/training/wearables/compose/migrate-to-material3.md).
3. Use the official component mappings from the migration guide.
4. Before refactoring any component (for example, `Chip` -\> `Button`), check the parameter names, slot types, and "Expressive" design tokens.
5. Do not use the Horologist Composables, Compose Layout, or Compose Material libraries.
6. **Always** check against the component guidance in Capability 4.
7. Expect screenshot tests to fail when a migration has been performed: Even when migrating to very similar components, expected defaults for padding and positioning will have changed. Do not seek to artificially match the pre-migration screenshot, but give preference to the Material3 defaults.

### Capability 2: Adding Wear OS Compose Material3 features or updating the app

Use this guidance when the developer asks to update a project which is using an
earlier version of Wear OS Compose Material3, or when they ask to add further
features.

1. Unless otherwise indicated by the developer, use the latest stable version of Wear Compose Material3 from `{VERSION}`.
2. Do not use the Horologist Composables, Compose Layout, or Compose Material libraries.
3. **Always** check against the component guidance in Capability 4.
4. Expect screenshot tests to fail when a migration has been performed: Even when migrating to very similar components, expected defaults for padding and positioning will have changed. Do not seek to artificially match the pre-migration screenshot, but give preference to the Material3 defaults.

### Capability 3: Component samples

Use this table of reference to find canonical samples for Wear Compose
components.
When working with a Wear Compose component, you must use the samples linked
from the table to ensure you know how to correctly use it.

#### Material 3 components in `androidx.wear.compose.material3.*`

| Component / Symbol | Reference Samples |
|---|---|
| `AlertDialog`, `AlertDialogDefaults` | [AlertDialogSample](./material3/AlertDialogSample.kt.md.txt) |
| `AnimatedPage`, `HorizontalPagerScaffold`, `VerticalPagerScaffold` | [OneHandedGestureSamples](./material3/OneHandedGestureSamples.kt.md.txt), [PageIndicatorSample](./material3/PageIndicatorSample.kt.md.txt), [PagerScaffoldSample](./material3/PagerScaffoldSample.kt.md.txt) |
| `AnimatedText`, `rememberAnimatedTextFontRegistry` | [AnimatedTextSample](./material3/AnimatedTextSample.kt.md.txt) |
| `AppCard` | [CardSample](./material3/CardSample.kt.md.txt) |
| `AppScaffold` | [ListHeaderSample](./material3/ListHeaderSample.kt.md.txt), [PagerScaffoldSample](./material3/PagerScaffoldSample.kt.md.txt), [ScaffoldSample](./material3/ScaffoldSample.kt.md.txt), [SurfaceTransformationSample](./material3/SurfaceTransformationSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](./material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `ArcProgressIndicator`, `ArcProgressIndicatorDefaults`, `CircularProgressIndicator`, `CircularProgressIndicatorDefaults`, `ProgressIndicatorDefaults`, `SegmentedCircularProgressIndicator`, `drawCircularProgressIndicator` | [ProgressIndicatorSample](./material3/ProgressIndicatorSample.kt.md.txt) |
| `Button` | [AlertDialogSample](./material3/AlertDialogSample.kt.md.txt), [AnimatedTextSample](./material3/AnimatedTextSample.kt.md.txt), [ButtonGroupSample](./material3/ButtonGroupSample.kt.md.txt), [ButtonSample](./material3/ButtonSample.kt.md.txt), [DatePickerSample](./material3/DatePickerSample.kt.md.txt), [DynamicColorSchemeSample](./material3/DynamicColorSchemeSample.kt.md.txt), [FadingExpandingLabelSample](./material3/FadingExpandingLabelSample.kt.md.txt), [ListHeaderSample](./material3/ListHeaderSample.kt.md.txt), [OneHandedGestureSamples](./material3/OneHandedGestureSamples.kt.md.txt), [PageIndicatorSample](./material3/PageIndicatorSample.kt.md.txt), [PagerScaffoldSample](./material3/PagerScaffoldSample.kt.md.txt), [PickerSample](./material3/PickerSample.kt.md.txt), [ScaffoldSample](./material3/ScaffoldSample.kt.md.txt), [ScrollIndicatorSample](./material3/ScrollIndicatorSample.kt.md.txt), [StepperSample](./material3/StepperSample.kt.md.txt), [SurfaceTransformationSample](./material3/SurfaceTransformationSample.kt.md.txt), [SwipeToRevealSample](./material3/SwipeToRevealSample.kt.md.txt), [TimePickerSample](./material3/TimePickerSample.kt.md.txt), [TransformationSpecSample](./material3/TransformationSpecSample.kt.md.txt), [TransformingLazyColumnSample](./foundation/TransformingLazyColumnSample.kt.md.txt), [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `ButtonDefaults` | [ButtonSample](./material3/ButtonSample.kt.md.txt), [CurvedTextSamples](./material3/CurvedTextSamples.kt.md.txt), [DynamicColorSchemeSample](./material3/DynamicColorSchemeSample.kt.md.txt), [EdgeButtonSample](./material3/EdgeButtonSample.kt.md.txt), [ListHeaderSample](./material3/ListHeaderSample.kt.md.txt), [PlaceholderSample](./material3/PlaceholderSample.kt.md.txt), [ScaffoldSample](./material3/ScaffoldSample.kt.md.txt), [ScrollAwaySample](./material3/ScrollAwaySample.kt.md.txt), [ScrollIndicatorSample](./material3/ScrollIndicatorSample.kt.md.txt), [SurfaceTransformationSample](./material3/SurfaceTransformationSample.kt.md.txt), [TextButtonSample](./material3/TextButtonSample.kt.md.txt), [TransformationSpecSample](./material3/TransformationSpecSample.kt.md.txt), [TransformingLazyColumnSample](./foundation/TransformingLazyColumnSample.kt.md.txt), [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `ButtonGroup` | [ButtonGroupSample](./material3/ButtonGroupSample.kt.md.txt), [TransformationSpecSample](./material3/TransformationSpecSample.kt.md.txt) |
| `Card` | [CardSample](./material3/CardSample.kt.md.txt), [SwipeToRevealSample](./material3/SwipeToRevealSample.kt.md.txt), [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `CardDefaults` | [CardSample](./material3/CardSample.kt.md.txt), [SurfaceTransformationSample](./material3/SurfaceTransformationSample.kt.md.txt), [SwipeToRevealSample](./material3/SwipeToRevealSample.kt.md.txt), [TransformingLazyColumnSample](./foundation/TransformingLazyColumnSample.kt.md.txt), [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `CheckboxButton` | [CheckboxButtonSample](./material3/CheckboxButtonSample.kt.md.txt), [SwipeToDismissBoxSample](./material3/SwipeToDismissBoxSample.kt.md.txt) |
| `ChildButton`, `OutlinedButton` | [ButtonSample](./material3/ButtonSample.kt.md.txt) |
| `ColorScheme`, `dynamicColorScheme` | [DynamicColorSchemeSample](./material3/DynamicColorSchemeSample.kt.md.txt) |
| `CompactButton`, `CompactButtonDefaults` | [ButtonSample](./material3/ButtonSample.kt.md.txt), [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `ConfirmationDialog`, `ConfirmationDialogDefaults`, `FailureConfirmationDialog`, `FavoriteIcon`, `SuccessConfirmationDialog`, `confirmationDialogCurvedText` | [ConfirmationDialogSample](./material3/ConfirmationDialogSample.kt.md.txt) |
| `CurvedTextDefaults` | [CurvedTextSamples](./material3/CurvedTextSamples.kt.md.txt) |
| `DatePicker`, `DatePickerType` | [DatePickerSample](./material3/DatePickerSample.kt.md.txt) |
| `EdgeButton` | [EdgeButtonSample](./material3/EdgeButtonSample.kt.md.txt), [OneHandedGestureSamples](./material3/OneHandedGestureSamples.kt.md.txt), [ScaffoldSample](./material3/ScaffoldSample.kt.md.txt), [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `EdgeButtonSize` | [EdgeButtonSample](./material3/EdgeButtonSample.kt.md.txt) |
| `FadingExpandingLabel` | [FadingExpandingLabelSample](./material3/FadingExpandingLabelSample.kt.md.txt) |
| `FilledIconButton`, `FilledTonalIconButton`, `IconButtonColors`, `IconButtonShapes`, `OutlinedIconButton` | [IconButtonSample](./material3/IconButtonSample.kt.md.txt) |
| `FilledTonalButton` | [AlertDialogSample](./material3/AlertDialogSample.kt.md.txt), [ButtonSample](./material3/ButtonSample.kt.md.txt), [ConfirmationDialogSample](./material3/ConfirmationDialogSample.kt.md.txt), [OpenOnPhoneDialogSample](./material3/OpenOnPhoneDialogSample.kt.md.txt), [PlaceholderSample](./material3/PlaceholderSample.kt.md.txt), [ScrollAwaySample](./material3/ScrollAwaySample.kt.md.txt), [SwipeToDismissBoxSample](./material3/SwipeToDismissBoxSample.kt.md.txt) |
| `GestureAction`, `OneHandedGestureClickIndicator`, `OneHandedGestureClickIndicatorState`, `oneHandedGesture`, `rememberOneHandedGestureConfiguration` | [ButtonSample](./material3/ButtonSample.kt.md.txt), [CardSample](./material3/CardSample.kt.md.txt), [OneHandedGestureSamples](./material3/OneHandedGestureSamples.kt.md.txt) |
| `GesturePriority`, `LocalOneHandedGestureEnabled`, `OneHandedGestureDefaults`, `OneHandedGestureHorizontalPageIndicator`, `OneHandedGesturePageIndicatorState`, `OneHandedGestureScrollIndicator`, `OneHandedGestureScrollIndicatorState`, `OneHandedGestureVerticalPageIndicator` | [OneHandedGestureSamples](./material3/OneHandedGestureSamples.kt.md.txt) |
| `HeadphoneIcon`, `Stepper`, `StepperLevelIndicator`, `rangeSemantics` | [StepperSample](./material3/StepperSample.kt.md.txt) |
| `HorizontalPageIndicator`, `VerticalPageIndicator` | [PageIndicatorSample](./material3/PageIndicatorSample.kt.md.txt) |
| `Icon` | [AlertDialogSample](./material3/AlertDialogSample.kt.md.txt), [ButtonSample](./material3/ButtonSample.kt.md.txt), [CardSample](./material3/CardSample.kt.md.txt), [CheckboxButtonSample](./material3/CheckboxButtonSample.kt.md.txt), [ConfirmationDialogSample](./material3/ConfirmationDialogSample.kt.md.txt), [CurvedTextSamples](./material3/CurvedTextSamples.kt.md.txt), [DatePickerSample](./material3/DatePickerSample.kt.md.txt), [EdgeButtonSample](./material3/EdgeButtonSample.kt.md.txt), [IconButtonSample](./material3/IconButtonSample.kt.md.txt), [ListHeaderSample](./material3/ListHeaderSample.kt.md.txt), [PlaceholderSample](./material3/PlaceholderSample.kt.md.txt), [ProgressIndicatorSample](./material3/ProgressIndicatorSample.kt.md.txt), [RadioButtonSample](./material3/RadioButtonSample.kt.md.txt), [SwipeToRevealSample](./material3/SwipeToRevealSample.kt.md.txt), [SwitchButtonSample](./material3/SwitchButtonSample.kt.md.txt), [TimePickerSample](./material3/TimePickerSample.kt.md.txt) |
| `IconButton` | [IconButtonSample](./material3/IconButtonSample.kt.md.txt), [LevelIndicatorSample](./material3/LevelIndicatorSample.kt.md.txt), [ProgressIndicatorSample](./material3/ProgressIndicatorSample.kt.md.txt) |
| `IconButtonDefaults` | [IconButtonSample](./material3/IconButtonSample.kt.md.txt), [ProgressIndicatorSample](./material3/ProgressIndicatorSample.kt.md.txt) |
| `IconToggleButton`, `IconToggleButtonDefaults`, `WifiOffIcon`, `WifiOnIcon` | [IconToggleButtonSample](./material3/IconToggleButtonSample.kt.md.txt) |
| `LevelIndicator` | [LevelIndicatorSample](./material3/LevelIndicatorSample.kt.md.txt) |
| `LinearProgressIndicator` | [LinearProgressIndicatorSample](./material3/LinearProgressIndicatorSample.kt.md.txt) |
| `ListHeader` | [ListHeaderSample](./material3/ListHeaderSample.kt.md.txt), [ScrollAwaySample](./material3/ScrollAwaySample.kt.md.txt), [TransformingLazyColumnNotificationsSample](./material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `ListHeaderDefaults` | [ListHeaderSample](./material3/ListHeaderSample.kt.md.txt), [ScrollAwaySample](./material3/ScrollAwaySample.kt.md.txt), [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `ListSubHeader` | [ListHeaderSample](./material3/ListHeaderSample.kt.md.txt) |
| `MaterialTheme` | [AlertDialogSample](./material3/AlertDialogSample.kt.md.txt), [ButtonSample](./material3/ButtonSample.kt.md.txt), [CardSample](./material3/CardSample.kt.md.txt), [CurvedTextSamples](./material3/CurvedTextSamples.kt.md.txt), [DynamicColorSchemeSample](./material3/DynamicColorSchemeSample.kt.md.txt), [LinearProgressIndicatorSample](./material3/LinearProgressIndicatorSample.kt.md.txt), [PagerScaffoldSample](./material3/PagerScaffoldSample.kt.md.txt), [ProgressIndicatorSample](./material3/ProgressIndicatorSample.kt.md.txt), [SwipeToDismissBoxSample](./material3/SwipeToDismissBoxSample.kt.md.txt), [TimeTextSample](./material3/TimeTextSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](./material3/TransformingLazyColumnNotificationsSample.kt.md.txt) |
| `OpenOnPhoneDialog`, `OpenOnPhoneDialogDefaults`, `openOnPhoneDialogCurvedText` | [OpenOnPhoneDialogSample](./material3/OpenOnPhoneDialogSample.kt.md.txt) |
| `OutlinedCard` | [CardSample](./material3/CardSample.kt.md.txt), [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `PagerScaffoldDefaults` | [PageIndicatorSample](./material3/PageIndicatorSample.kt.md.txt), [PagerScaffoldSample](./material3/PagerScaffoldSample.kt.md.txt) |
| `Picker` | [PickerSample](./material3/PickerSample.kt.md.txt) |
| `PickerGroup` | [PickerGroupSample](./material3/PickerGroupSample.kt.md.txt) |
| `RadioButton`, `SplitRadioButton` | [RadioButtonSample](./material3/RadioButtonSample.kt.md.txt) |
| `ResponsiveTransformationSpec`, `TransformationVariableSpec` | [SurfaceTransformationSample](./material3/SurfaceTransformationSample.kt.md.txt), [TransformationSpecSample](./material3/TransformationSpecSample.kt.md.txt) |
| `RevealValue`, `SwipeToReveal`, `SwipeToRevealDefaults`, `rememberRevealState` | [SwipeToRevealSample](./material3/SwipeToRevealSample.kt.md.txt) |
| `ScreenScaffold` | [ListHeaderSample](./material3/ListHeaderSample.kt.md.txt), [OneHandedGestureSamples](./material3/OneHandedGestureSamples.kt.md.txt), [PagerScaffoldSample](./material3/PagerScaffoldSample.kt.md.txt), [ScaffoldSample](./material3/ScaffoldSample.kt.md.txt), [SurfaceTransformationSample](./material3/SurfaceTransformationSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](./material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `ScreenScaffoldDefaults`, `ScrollIndicator` | [ScrollIndicatorSample](./material3/ScrollIndicatorSample.kt.md.txt) |
| `ScreenStage`, `scrollAway` | [ScrollAwaySample](./material3/ScrollAwaySample.kt.md.txt) |
| `Slider`, `SliderDefaults` | [SliderSample](./material3/SliderSample.kt.md.txt) |
| `SplitCheckboxButton` | [CheckboxButtonSample](./material3/CheckboxButtonSample.kt.md.txt) |
| `SplitSwitchButton` | [SwitchButtonSample](./material3/SwitchButtonSample.kt.md.txt) |
| `StepperDefaults`, `VolumeDownIcon`, `VolumeUpIcon` | [LevelIndicatorSample](./material3/LevelIndicatorSample.kt.md.txt), [StepperSample](./material3/StepperSample.kt.md.txt) |
| `SurfaceTransformation` | [AlertDialogSample](./material3/AlertDialogSample.kt.md.txt), [DynamicColorSchemeSample](./material3/DynamicColorSchemeSample.kt.md.txt), [ListHeaderSample](./material3/ListHeaderSample.kt.md.txt), [ScaffoldSample](./material3/ScaffoldSample.kt.md.txt), [SurfaceTransformationSample](./material3/SurfaceTransformationSample.kt.md.txt), [TransformationSpecSample](./material3/TransformationSpecSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](./material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](./foundation/TransformingLazyColumnSample.kt.md.txt), [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `SwipeToDismissBox` | [SwipeToDismissBoxSample](./material3/SwipeToDismissBoxSample.kt.md.txt) |
| `SwitchButton` | [AlertDialogSample](./material3/AlertDialogSample.kt.md.txt), [OneHandedGestureSamples](./material3/OneHandedGestureSamples.kt.md.txt), [SwitchButtonSample](./material3/SwitchButtonSample.kt.md.txt) |
| `Text` | [AlertDialogSample](./material3/AlertDialogSample.kt.md.txt), [AnimatedTextSample](./material3/AnimatedTextSample.kt.md.txt), [ButtonGroupSample](./material3/ButtonGroupSample.kt.md.txt), [ButtonSample](./material3/ButtonSample.kt.md.txt), [CardSample](./material3/CardSample.kt.md.txt), [CheckboxButtonSample](./material3/CheckboxButtonSample.kt.md.txt), [ConfirmationDialogSample](./material3/ConfirmationDialogSample.kt.md.txt), [DatePickerSample](./material3/DatePickerSample.kt.md.txt), [DynamicColorSchemeSample](./material3/DynamicColorSchemeSample.kt.md.txt), [EdgeButtonSample](./material3/EdgeButtonSample.kt.md.txt), [ListHeaderSample](./material3/ListHeaderSample.kt.md.txt), [OneHandedGestureSamples](./material3/OneHandedGestureSamples.kt.md.txt), [OpenOnPhoneDialogSample](./material3/OpenOnPhoneDialogSample.kt.md.txt), [PageIndicatorSample](./material3/PageIndicatorSample.kt.md.txt), [PagerScaffoldSample](./material3/PagerScaffoldSample.kt.md.txt), [PickerGroupSample](./material3/PickerGroupSample.kt.md.txt), [PickerSample](./material3/PickerSample.kt.md.txt), [PlaceholderSample](./material3/PlaceholderSample.kt.md.txt), [RadioButtonSample](./material3/RadioButtonSample.kt.md.txt), [ScaffoldSample](./material3/ScaffoldSample.kt.md.txt), [ScrollAwaySample](./material3/ScrollAwaySample.kt.md.txt), [ScrollIndicatorSample](./material3/ScrollIndicatorSample.kt.md.txt), [StepperSample](./material3/StepperSample.kt.md.txt), [SurfaceTransformationSample](./material3/SurfaceTransformationSample.kt.md.txt), [SwipeToDismissBoxSample](./material3/SwipeToDismissBoxSample.kt.md.txt), [SwipeToRevealSample](./material3/SwipeToRevealSample.kt.md.txt), [SwitchButtonSample](./material3/SwitchButtonSample.kt.md.txt), [TextButtonSample](./material3/TextButtonSample.kt.md.txt), [TextToggleButtonSample](./material3/TextToggleButtonSample.kt.md.txt), [TimePickerSample](./material3/TimePickerSample.kt.md.txt), [TransformationSpecSample](./material3/TransformationSpecSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](./material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `TextButton` | [TextButtonSample](./material3/TextButtonSample.kt.md.txt) |
| `TextButtonDefaults` | [TextButtonSample](./material3/TextButtonSample.kt.md.txt), [TextToggleButtonSample](./material3/TextToggleButtonSample.kt.md.txt) |
| `TextToggleButton`, `TextToggleButtonDefaults`, `touchTargetAwareSize` | [TextToggleButtonSample](./material3/TextToggleButtonSample.kt.md.txt) |
| `TimePicker`, `TimePickerType` | [TimePickerSample](./material3/TimePickerSample.kt.md.txt) |
| `TimeText` | [ScrollAwaySample](./material3/ScrollAwaySample.kt.md.txt), [ScrollIndicatorSample](./material3/ScrollIndicatorSample.kt.md.txt), [TimeTextSample](./material3/TimeTextSample.kt.md.txt) |
| `TimeTextDefaults`, `timeTextCurvedText` | [TimeTextSample](./material3/TimeTextSample.kt.md.txt) |
| `TitleCard` | [CardSample](./material3/CardSample.kt.md.txt), [SurfaceTransformationSample](./material3/SurfaceTransformationSample.kt.md.txt), [SwipeToRevealSample](./material3/SwipeToRevealSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](./material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](./foundation/TransformingLazyColumnSample.kt.md.txt) |
| `TransformationSpec` | [TransformationSpecSample](./material3/TransformationSpecSample.kt.md.txt) |
| `curvedText` | [CurvedTextSamples](./material3/CurvedTextSamples.kt.md.txt), [ScrollAwaySample](./material3/ScrollAwaySample.kt.md.txt), [TimeTextSample](./material3/TimeTextSample.kt.md.txt) |
| `firstVisibleItemLayoutItemInfo`, `layoutItemInfoOf`, `rememberTransformingLazyColumnFirstLayoutItemProvider` | [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `placeholder`, `placeholderShimmer`, `rememberPlaceholderState` | [PlaceholderSample](./material3/PlaceholderSample.kt.md.txt) |
| `rememberPickerState` | [PickerGroupSample](./material3/PickerGroupSample.kt.md.txt), [PickerSample](./material3/PickerSample.kt.md.txt) |
| `rememberTransformationSpec`, `transformedHeight` | [AlertDialogSample](./material3/AlertDialogSample.kt.md.txt), [DynamicColorSchemeSample](./material3/DynamicColorSchemeSample.kt.md.txt), [ListHeaderSample](./material3/ListHeaderSample.kt.md.txt), [ScaffoldSample](./material3/ScaffoldSample.kt.md.txt), [SurfaceTransformationSample](./material3/SurfaceTransformationSample.kt.md.txt), [SwipeToRevealSample](./material3/SwipeToRevealSample.kt.md.txt), [TransformationSpecSample](./material3/TransformationSpecSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](./material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](./foundation/TransformingLazyColumnSample.kt.md.txt), [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `timeTextSeparator` | [ScrollAwaySample](./material3/ScrollAwaySample.kt.md.txt), [TimeTextSample](./material3/TimeTextSample.kt.md.txt) |

#### Foundation components in `androidx.wear.compose.foundation.*`

| Component / Symbol | Reference Samples |
|---|---|
| `AmbientMode`, `AmbientTickEffect`, `LocalAmbientModeManager`, `rememberAmbientModeManager` | [AmbientModeSample](./foundation/AmbientModeSample.kt.md.txt) |
| `AutoCenteringParams`, `ScalingLazyColumnDefaults`, `ScalingLazyListAnchorType` | [ScalingLazyColumnSample](./foundation/ScalingLazyColumnSample.kt.md.txt) |
| `BasicSwipeToDismissBox` | [SwipeToDismissBoxSample](./foundation/SwipeToDismissBoxSample.kt.md.txt) |
| `CurvedAlignment`, `CurvedTextStyle`, `angularGradientBackground`, `angularSize`, `basicCurvedText`, `clearAndSetSemantics`, `curvedColumn`, `padding`, `radialGradientBackground`, `radialSize`, `semantics`, `size` | [CurvedWorldSample](./foundation/CurvedWorldSample.kt.md.txt) |
| `CurvedDirection`, `CurvedLayout`, `angularSizeDp`, `background`, `curvedBox`, `curvedComposable`, `curvedRow` | [CurvedTextSamples](./material3/CurvedTextSamples.kt.md.txt), [CurvedWorldSample](./foundation/CurvedWorldSample.kt.md.txt) |
| `CurvedModifier` | [CurvedTextSamples](./material3/CurvedTextSamples.kt.md.txt), [CurvedWorldSample](./foundation/CurvedWorldSample.kt.md.txt), [TimeTextSample](./material3/TimeTextSample.kt.md.txt) |
| `ExperimentalWearFoundationApi`, `RevealValue`, `SwipeToReveal`, `rememberRevealState` | [SwipeToRevealSample](./foundation/SwipeToRevealSample.kt.md.txt) |
| `HorizontalPager`, `VerticalPager`, `rememberPagerState` | [OneHandedGestureSamples](./material3/OneHandedGestureSamples.kt.md.txt), [PageIndicatorSample](./material3/PageIndicatorSample.kt.md.txt), [PagerSamples](./foundation/PagerSamples.kt.md.txt), [PagerScaffoldSample](./material3/PagerScaffoldSample.kt.md.txt) |
| `ItemEdge`, `TransformingLazyColumnDefaults` | [TransformingLazyColumnSample](./foundation/TransformingLazyColumnSample.kt.md.txt) |
| `PagerDefaults` | [PagerScaffoldSample](./material3/PagerScaffoldSample.kt.md.txt) |
| `RotaryScrollableDefaults` | [PagerScaffoldSample](./material3/PagerScaffoldSample.kt.md.txt), [RotarySamples](./foundation/RotarySamples.kt.md.txt), [ScalingLazyColumnSample](./foundation/ScalingLazyColumnSample.kt.md.txt), [TransformingLazyColumnSample](./foundation/TransformingLazyColumnSample.kt.md.txt) |
| `RotarySnapLayoutInfoProvider`, `rotaryScrollable` | [RotarySamples](./foundation/RotarySamples.kt.md.txt) |
| `ScalingLazyColumn` | [ExpandableSample](./foundation/ExpandableSample.kt.md.txt), [HierarchicalFocusSample](./foundation/HierarchicalFocusSample.kt.md.txt), [OneHandedGestureSamples](./material3/OneHandedGestureSamples.kt.md.txt), [ScalingLazyColumnSample](./foundation/ScalingLazyColumnSample.kt.md.txt), [SwipeToRevealSample](./foundation/SwipeToRevealSample.kt.md.txt), [SwipeToRevealSample](./material3/SwipeToRevealSample.kt.md.txt) |
| `ScrollInfoProvider` | [ScrollAwaySample](./material3/ScrollAwaySample.kt.md.txt) |
| `SwipeToDismissValue`, `edgeSwipeToDismiss`, `rememberSwipeToDismissBoxState` | [SwipeToDismissBoxSample](./foundation/SwipeToDismissBoxSample.kt.md.txt), [SwipeToDismissBoxSample](./material3/SwipeToDismissBoxSample.kt.md.txt) |
| `TransformingLazyColumn` | [DynamicColorSchemeSample](./material3/DynamicColorSchemeSample.kt.md.txt), [ListHeaderSample](./material3/ListHeaderSample.kt.md.txt), [OneHandedGestureSamples](./material3/OneHandedGestureSamples.kt.md.txt), [ScaffoldSample](./material3/ScaffoldSample.kt.md.txt), [ScrollAwaySample](./material3/ScrollAwaySample.kt.md.txt), [ScrollIndicatorSample](./material3/ScrollIndicatorSample.kt.md.txt), [SurfaceTransformationSample](./material3/SurfaceTransformationSample.kt.md.txt), [SwipeToRevealSample](./material3/SwipeToRevealSample.kt.md.txt), [TransformationSpecSample](./material3/TransformationSpecSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](./material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](./foundation/TransformingLazyColumnSample.kt.md.txt), [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `TransformingLazyColumnFirstLayoutItemProvider` | [TransformingLazyColumnSample](./foundation/TransformingLazyColumnSample.kt.md.txt), [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `TransformingLazyColumnItemScrollProgress` | [TransformationSpecSample](./material3/TransformationSpecSample.kt.md.txt) |
| `expandableButton`, `expandableItems` | [ExpandableSample](./foundation/ExpandableSample.kt.md.txt) |
| `expandableItem`, `rememberExpandableState` | [ExpandableSample](./foundation/ExpandableSample.kt.md.txt), [SwipeToRevealSample](./foundation/SwipeToRevealSample.kt.md.txt) |
| `hierarchicalFocusGroup` | [HierarchicalFocusSample](./foundation/HierarchicalFocusSample.kt.md.txt) |
| `items` | [SwipeToRevealSample](./material3/SwipeToRevealSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](./material3/TransformingLazyColumnNotificationsSample.kt.md.txt) |
| `itemsIndexed` | [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `rememberScalingLazyListState` | [OneHandedGestureSamples](./material3/OneHandedGestureSamples.kt.md.txt), [ScalingLazyColumnSample](./foundation/ScalingLazyColumnSample.kt.md.txt), [SwipeToRevealSample](./material3/SwipeToRevealSample.kt.md.txt) |
| `rememberTransformingLazyColumnState` | [ListHeaderSample](./material3/ListHeaderSample.kt.md.txt), [OneHandedGestureSamples](./material3/OneHandedGestureSamples.kt.md.txt), [ScaffoldSample](./material3/ScaffoldSample.kt.md.txt), [ScrollAwaySample](./material3/ScrollAwaySample.kt.md.txt), [ScrollIndicatorSample](./material3/ScrollIndicatorSample.kt.md.txt), [SurfaceTransformationSample](./material3/SurfaceTransformationSample.kt.md.txt), [SwipeToRevealSample](./material3/SwipeToRevealSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](./material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](./foundation/TransformingLazyColumnSample.kt.md.txt), [TransformingLazyColumnSample](./material3/TransformingLazyColumnSample.kt.md.txt) |
| `requestFocusOnHierarchyActive` | [HierarchicalFocusSample](./foundation/HierarchicalFocusSample.kt.md.txt), [RotarySamples](./foundation/RotarySamples.kt.md.txt) |
| `weight` | [CurvedWorldSample](./foundation/CurvedWorldSample.kt.md.txt), [TimeTextSample](./material3/TimeTextSample.kt.md.txt) |

### Capability 4: Component guidance

**Mandatory**: Use this capability as a checklist against any component use. It
provides more holistic guidance on how to use each component in practice, beyond
the component syntax.

1. `AppScaffold` and `ScreenScaffold`
   - \[ \] Use `AppScaffold` as the outer container, with `ScreenScaffold` children.
   - \[ \] Use only **ONE** `AppScaffold` and any number of `ScreenScaffold`.
2. `ScalingLazyColumn` - Use `TransformingLazyColumn` instead.
3. `TransformingLazyColumn` - You will need the following imports:


   ```kotlin
   import androidx.wear.compose.foundation.lazy.TransformingLazyColumn
   import androidx.wear.compose.foundation.lazy.TransformingLazyColumnDefaults
   import androidx.wear.compose.foundation.lazy.rememberTransformingLazyColumnState
   // ...
   import androidx.wear.compose.material3.lazy.rememberTransformationSpec
   import androidx.wear.compose.material3.lazy.transformedHeight
   ```

   <br />

   **Canonical example**:


   ```kotlin
   val columnState = rememberTransformingLazyColumnState()
   val transformationSpec = rememberTransformationSpec()
   ScreenScaffold(
       scrollState = columnState
   ) { contentPadding ->
       TransformingLazyColumn(
           state = columnState,
           contentPadding = contentPadding
       ) {
           item {
               ListHeader(
                   modifier = Modifier
                       .fillMaxWidth()
                       .transformedHeight(this, transformationSpec)
                       .minimumVerticalContentPadding(ListHeaderDefaults.minimumTopListContentPadding),
                   transformation = SurfaceTransformation(transformationSpec)
               ) {
                   Text(text = "Header")
               }
           }
           // ... other items
           item {
               Button(
                   modifier = Modifier
                       .fillMaxWidth()
                       .transformedHeight(this, transformationSpec)
                       .minimumVerticalContentPadding(ButtonDefaults.minimumVerticalListContentPadding),
                   transformation = SurfaceTransformation(transformationSpec),
                   onClick = { /* ... */ },
                   icon = {
                       Icon(
                           imageVector = Icons.Default.Build,
                           contentDescription = "build",
                       )
                   },
               ) {
                   Text(
                       text = "Build",
                       maxLines = 1,
                       overflow = TextOverflow.Ellipsis,
                   )
               }
           }
       }
   }
   ```

   <br />

   - \[ \] Use `TransformingLazyColumn` instead of `ScalingLazyColumn`.
   - \[ \] You must pass the `contentPadding` parameter from `ScreenScaffold` to the `TransformingLazyColumn`.
   - \[ \] Use the `minimumVerticalContentPadding` modifier to achieve required padding top and bottom.
     - This expects a value from defaults, such as `ButtonDefaults`, `CardDefaults`, \`ListHeaderDefaults.
     - Note: This is a scoped modifier available within `TransformingLazyColumnItemScope`.
   - \[ \] Ensure the list morphs and scales.
   - \[ \] Use `transformedHeight` modifier.
   - \[ \] Use `transform = SurfaceTransform(...)`.
   - \[ \] If configuring a list for snapping, use `flingBehavior` and `rotaryScrollableBehavior` **together**:


   ```kotlin
   val columnState = rememberTransformingLazyColumnState()
   ScreenScaffold(scrollState = columnState) { contentPadding ->
       TransformingLazyColumn(
           state = columnState,
           flingBehavior = TransformingLazyColumnDefaults.snapFlingBehavior(columnState),
           rotaryScrollableBehavior = RotaryScrollableDefaults.snapBehavior(columnState)
       ) {
           // ...
           // ...
       }
   }
   ```

   <br />

4. `ScreenScaffold`

   - \[ \] Guard the `scrollIndicator` with `!LocalScrollCaptureInProgress.current`.
5. `EdgeButton`

   - \[ \] Do **NOT** use as the final item within a `TransformingLazyColumn`. Instead, use the slot in `ScreenScaffold`.
   - \[ \] When used in a `TransformingLazyColumn`, add the required overscroll behavior:


   ```kotlin
   val columnState = rememberTransformingLazyColumnState()
   ScreenScaffold(
       scrollState = columnState,
       edgeButton = {
           EdgeButton(
               onClick = { /* TODO */ },
               modifier = Modifier.scrollable(
                   columnState,
                   orientation = Orientation.Vertical,
                   reverseDirection = true,
                   // Apply overscroll to the EdgeButton for proper scrolling behavior.
                   overscrollEffect = rememberOverscrollEffect(),
               )
           ) {
               Text("More")
           }
       }
   ) { contentPadding ->
       TransformingLazyColumn(
           contentPadding = contentPadding,
           state = columnState,
       ) {
           // ...
           // ...
       }
   }
   ```

   <br />

6. `Column`

   - \[ \] USE as a direct child of `ScreenScaffold` *if* the screen is will **never** scroll, even with the largest system font.
   - \[ \] Use `TransformingLazyColumn` instead for all other cases.
7. Styles

   - \[ \] Do **NOT** hard-code text sizes, use `typography` from `MaterialTheme`.
   - \[ \] Do **NOT** hard-code colors, use `colorScheme` from `MaterialTheme`.
8. Use component defaults:

   - \[ \] Components such as `Button` have a corresponding `ButtonDefaults` object.
   - \[ \] Check for and use the `*Defaults` object for any component when working with padding and styling values, in preference to hard-coded values.
9. Use Wear specific previews:

   - \[ \] `WearPreviewDevices`
   - \[ \] `WearPreviewFontScales`
10. Ambient mode

    - \[ \] Use `LocalAmbientModeManager` instead of `AmbientLifecycleObserver`.
11. Navigation

    - \[ \] When adding navigation fresh, use Navigation3.
    - \[ \] For Navigation3 in Wear OS, use `SwipeDismissableSceneStrategy()` from the Wear Compose `compose-navigation3` library.
12. Comments

    - \[ \] Where any Kotlin file has been modified, ensure that the existing comments are up to date and accurately reflect any changes to the implementation.
13. `HorizontalPager` or `VerticalPager`

    - \[ \] Use the Composable hierarchy in this order: `AppScaffold`, `HorizontalPagerScaffold`, `HorizontalPager`, `AnimatedPage`, `ScreenScaffold`. Or similarly for `VerticalPager`.
