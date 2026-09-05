# KMP Audio Recording & Transcription Recipes

This reference provides concrete platform implementations for audio capture and STT pipeline handling across Android and iOS.

---

## 1. Android Background Capture
- **Foreground Service**: Must declare \`android:foregroundServiceType="microphone"\` in \`AndroidManifest.xml\`.
- **MediaRecorder / AudioRecord**: Capture 16-bit PCM at 16kHz mono for optimal Whisper / STT accuracy.

---

## 2. iOS Audio Session Configuration
- **AVAudioSession**: Set category to \`AVAudioSessionCategoryPlayAndRecord\` with options \`[.allowBluetooth, .defaultToSpeaker]\`.
- **Background Modes**: Enable \`audio\` in \`UIBackgroundModes\` in Info.plist.

---

## 3. Chunking & Network Retries
- Slice audio into 30-second WAV/M4A segments with a 1-second overlap.
- Implement exponential backoff with jitter on HTTP 429/503 responses.
