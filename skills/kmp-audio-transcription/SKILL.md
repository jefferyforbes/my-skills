---
name: kmp-audio-transcription
description: Kotlin Multiplatform audio recording, background capture, segment chunking, and speech-to-text (STT) transcription pipelines across Android and iOS.
license: Apache-2.0
metadata:
  author: Jeffery Forbes
  last-updated: '2026-09-05'
  keywords:
  - Kotlin Multiplatform
  - Audio Recording
  - Speech to Text
  - Transcription
  - Whisper
  - Gemini Audio
  - Android
  - iOS
  - AVAudioEngine
  - MediaRecorder
  - Media3
---

# Kotlin Multiplatform Audio Recording & Transcription

## Overview

Implementing audio capture and transcription in Kotlin Multiplatform requires bridging native hardware capabilities (microphones, background execution, audio codecs) with shared business logic and streaming STT services (e.g. Whisper, Gemini Audio, or custom server endpoints).

---

## 1. Expect/Actual Architecture

Define pure Kotlin domain interfaces in `commonMain`:

```kotlin
package com.example.app.audio

import kotlinx.coroutines.flow.StateFlow

enum class RecordingStatus {
    IDLE, RECORDING, PAUSED, PROCESSING
}

data class AudioChunk(
    val fileUri: String,
    val durationMs: Long,
    val sequenceIndex: Int,
    val isFinal: Boolean
)

interface AudioRecorder {
    val status: StateFlow<RecordingStatus>
    val amplitude: StateFlow<Float> // 0.0f to 1.0f for audio visualizer waveforms
    
    suspend fun startRecording(outputDirectory: String, maxChunkDurationMs: Long = 60_000L)
    suspend fun pauseRecording()
    suspend fun resumeRecording()
    suspend fun stopRecording(): List<AudioChunk>
    suspend fun cancelRecording()
}

expect fun createPlatformAudioRecorder(): AudioRecorder
```

---

## 2. Platform Implementations

### iOS (`iosMain`)
Use `AVAudioEngine` or `AVAudioRecorder` via Kotlin/Native CocoaPods/Framework bindings:

```kotlin
import platform.AVFAudio.*
import platform.Foundation.*

class IosAudioRecorder : AudioRecorder {
    private var recorder: AVAudioRecorder? = null

    override suspend fun startRecording(outputDirectory: String, maxChunkDurationMs: Long) {
        val audioSession = AVAudioSession.sharedInstance()
        audioSession.setCategory(
            AVAudioSessionCategoryPlayAndRecord,
            mode = AVAudioSessionModeMeasurement,
            options = AVAudioSessionCategoryOptionAllowBluetooth or AVAudioSessionCategoryOptionDefaultToSpeaker,
            error = null
        )
        audioSession.setActive(true, error = null)

        val settings: Map<Any?, Any> = mapOf(
            AVFormatIDKey to kAudioFormatMPEG4AAC,
            AVSampleRateKey to 16000.0,
            AVNumberOfChannelsKey to 1,
            AVEncoderAudioQualityKey to AVAudioQualityHigh
        )

        val fileUrl = NSURL.fileURLWithPath("$outputDirectory/session_chunk_0.m4a")
        recorder = AVAudioRecorder(fileUrl, settings, null).apply {
            meteringEnabled = true
            record()
        }
    }
    // ...
}
```

**iOS Info.plist Requirements**:
- `NSMicrophoneUsageDescription`: Explanation for recording patient conversations.
- `UIBackgroundModes`: Add `audio` to prevent iOS from suspending recording on screen lock.

---

### Android (`androidMain`)
Use Android `MediaRecorder` or `AudioRecord` hosted within an Android **Foreground Service**:

```kotlin
// Android foreground notification is required to prevent OS killing long recordings
class AndroidAudioRecorder(
    private val context: Context
) : AudioRecorder {
    private var mediaRecorder: MediaRecorder? = null

    override suspend fun startRecording(outputDirectory: String, maxChunkDurationMs: Long) {
        // Start Foreground Service with FOREGROUND_SERVICE_TYPE_MICROPHONE
        AudioRecordingService.start(context)

        mediaRecorder = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
            MediaRecorder(context)
        } else {
            @Suppress("DEPRECATION")
            MediaRecorder()
        }.apply {
            setAudioSource(MediaRecorder.AudioSource.MIC)
            setOutputFormat(MediaRecorder.OutputFormat.MPEG_4)
            setAudioEncoder(MediaRecorder.AudioEncoder.AAC)
            setAudioSamplingRate(16000)
            setAudioEncodingBitRate(64000)
            setOutputFile(File(outputDirectory, "session_chunk_0.m4a").absolutePath)
            prepare()
            start()
        }
    }
}
```

**Android Manifest Requirements**:
- `<uses-permission android:name="android.permission.RECORD_AUDIO" />`
- `<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />`
- `<uses-permission android:name="android.permission.FOREGROUND_SERVICE_MICROPHONE" />`

---

## 3. Chunking & Duration Limits (e.g. 30-min caps, 25MB file limits)

For clinical sessions up to 30–60 minutes:
1. **Rolling Chunks**: Segment audio into 5-minute chunks (`chunk_001.m4a`, `chunk_002.m4a`) or roll over when approaching 25 MB (standard STT payload cap).
2. **Seamless Stitching**: Maintain continuous timestamps across chunks so transcription segments can align timestamps correctly for playback.
3. **Emergency Auto-Stop**: Implement a coroutine timer that triggers `stopRecording()` when reaching duration limits (e.g. 30:00).

---

## 4. Transcription Engine Integration

Connect audio output to speech-to-text models:

```kotlin
interface TranscriptionEngine {
    suspend fun transcribeChunk(
        audioChunk: AudioChunk,
        languageHint: String? = null
    ): Result<TranscriptionSegment>
}

data class TranscriptionSegment(
    val text: String,
    val startTimeMs: Long,
    val endTimeMs: Long,
    val speakerTag: String? = null
)
```

### Options:
- **Cloud (Gemini / Whisper API)**: Upload chunks via Ktor HTTP client to cloud endpoints with Bearer tokens.
- **On-Device (Whisper.cpp / TFLite)**: Run on-device inference using native bindings for complete clinical privacy without sending audio off-device.

---

## Deep References
Load on-demand using `view_file`:
- **[Audio Pipeline & Platform Recipes](./references/pipeline-recipes.md)**: Android foreground services, iOS AVAudioSession, and segment chunking algorithms.
