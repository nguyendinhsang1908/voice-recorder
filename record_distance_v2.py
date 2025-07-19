#!/usr/bin/env python3
import os
import time
import sounddevice as sd
import soundfile as sf

# ─── CONFIG ─────────────────────────────────────────────────────────────
PROJECT_DIR    = "/home/thanh/Training_model" # To team members: Change this path according to your model
RECORDINGS_DIR = os.path.join(PROJECT_DIR, "recordings")
SAMPLE_RATE    = 16000      # in Hz
CHANNELS       = 1          # mono
SUBTYPE        = 'PCM_16'   # 16-bit WAV
# ────────────────────────────────────────────────────────────────────────

def record_until_enter(filepath):
    """Record audio into filepath until user hits Enter a second time."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with sf.SoundFile(filepath, mode='w',
                      samplerate=SAMPLE_RATE,
                      channels=CHANNELS,
                      subtype=SUBTYPE) as f:
        def callback(indata, frames, time_info, status):
            if status:
                print(f"Note: {status}", flush=True)
            f.write(indata)

        with sd.InputStream(samplerate=SAMPLE_RATE,
                            channels=CHANNELS,
                            callback=callback):
            input("RECORDING... press Enter again to STOP\n")

if __name__ == "__main__":
    # 1) Ask user for the desired output filename (without .wav)
    name = input("Enter the name for this recording: ").strip()
    out_path = os.path.join(RECORDINGS_DIR, f"{name}.wav")

    # 2) Wait for Enter to start recording
    input("Press Enter to START recording")
    start_time = time.time()

    # 3) Record until Enter is pressed again
    record_until_enter(out_path)

    # 4) Report and exit
    elapsed = time.time() - start_time
    print(f"\n Saved '{out_path}' ({elapsed:.2f}s recorded)")
