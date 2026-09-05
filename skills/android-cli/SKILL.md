---
name: android-cli
description: Global Android CLI and Emulator skill. Provides instructions for using the `android` CLI tool, SDK management, and managing Android Virtual Devices (AVDs). Includes native adb and emulator command references for testing, UI navigation, building, and lifecycle management without external Python scripts.
---

# Android CLI & Emulator Specialist

This skill provides instructions for using the `android` CLI tool, SDK management, and native `adb` commands for Android app testing, UI interaction, and lifecycle management.

## 1. SDK & CLI Management

### Installation
If the android tool is not in the path, install it:
- Linux: `curl -fsSL https://dl.google.com/android/cli/latest/linux_x86_64/install.sh | bash`
- Mac Arm: `curl -fsSL https://dl.google.com/android/cli/latest/darwin_arm64/install.sh | bash`
- Mac Intel: `curl -fsSL https://dl.google.com/android/cli/latest/darwin_x86_64/install.sh | bash`

### SDK Management
Use the `android sdk` command:
- `android sdk install <package>[@<version>]...`: Install packages (e.g. `platforms/android-34`).
- `android sdk update [<pkg-name>]`: Update packages.
- `android sdk remove <pkg-name>`: Remove a package.
- `android sdk list --all`: List available packages.

### Documentation Search
Use `android docs <keywords>` to search the authoritative Android Knowledge Base for APIs, best practices, and migration guides.

### UI Inspection
Use `android layout` to inspect the UI layout tree of a connected Android application in JSON format (much faster than screenshots for debugging).

## 2. Advanced Interaction & Emulation (Native `adb`)

Instead of custom Python scripts, use the following standard Android SDK commands for lifecycle, navigation, and testing:

### A. App Lifecycle & Build
- **Build & Test**: `./gradlew assembleDebug` or `./gradlew connectedAndroidTest`
- **Install APK**: `adb install -r app-debug.apk`
- **Launch App**: `adb shell monkey -p <package.name> -c android.intent.category.LAUNCHER 1`
- **Force Stop**: `adb shell am force-stop <package.name>`
- **Clear Data**: `adb shell pm clear <package.name>`

### B. UI Navigation & Input (Semantic)
- **Dump UI Hierarchy**: `adb shell uiautomator dump && adb pull /sdcard/window_dump.xml .` (Analyze the XML for `resource-id` and `text` bounds).
- **Tap Coordinates**: `adb shell input tap <x> <y>` (Extract coordinates from the dumped XML bounds).
- **Enter Text**: `adb shell input text "your_string"`
- **Hardware Keys**: `adb shell input keyevent <KEYCODE>` (e.g., `4` for Back, `3` for Home, `66` for Enter).
- **Swipe**: `adb shell input swipe <x1> <y1> <x2> <y2> <duration_ms>`

### C. Logging & Observability
- **Monitor Logs**: `adb logcat -d` (dump current logs) or `adb logcat -s <TAG>` (filter by tag).
- **Screen Capture**: `adb exec-out screencap -p > screen.png`

### D. Emulator Management
- **List AVDs**: `emulator -list-avds`
- **Start Emulator**: `emulator -avd <AVD_NAME> -no-snapshot-load` (Append `-no-window` for headless CI).
- **Shutdown**: `adb -s <serial> emu kill`

## References
For detailed journeys and advanced device interaction, refer to the Android CLI plugin docs:
- [Interacting with devices](../../plugins/android-cli-plugin/skills/references/interact.md)
- [Running journey tests](../../plugins/android-cli-plugin/skills/references/journeys.md)
