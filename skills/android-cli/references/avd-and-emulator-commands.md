# Android CLI, AVD & Emulator Command Reference

This reference provides native command patterns for managing Android emulators and debugging via ADB.

---

## 1. Emulator & AVD Commands
- **List installed AVDs**: \`emulator -list-avds\`
- **Start headless emulator (CI/Testing)**: \`emulator -avd <avd_name> -no-window -no-audio -no-boot-anim &\`
- **Create new AVD**: \`avdmanager create avd -n test_device -k "system-images;android-34;google_apis;arm64-v8a"\`

---

## 2. ADB Diagnostic Commands
- **Logcat by Tag**: \`adb logcat -s <Tag>:V\`
- **Clear & Dump Crashes**: \`adb logcat -c && adb logcat *:E\`
- **Inspect Installed Packages**: \`adb shell pm list packages -3\`
- **Take Screenshot to Host**: \`adb exec-out screencap -p > screen.png\`
