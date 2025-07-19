import os
import time
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import pygame


pygame.mixer.init()


sample_rate = 16000  # Hz
duration = 2.5  # seconds
beep_freq = 1000  # Hz
beep_duration = 0.2  # seconds
dir_path = "recorded_wav_dataset"

def play_beep():
    try:
        beep_mono = np.sin(2 * np.pi * 1000 * np.linspace(0, 0.2, int(44100 * 0.2))) * 0.3
        beep_stereo = np.column_stack([beep_mono, beep_mono])  
        beep_stereo = (beep_stereo * 32767).astype(np.int16)  
        beep_stereo = np.ascontiguousarray(beep_stereo)  
        beep_sound = pygame.sndarray.make_sound(beep_stereo)
        beep_sound.play()
        sd.wait()  
    except Exception as e:
        print(f"Error playing beep: {e}")


def create_directories(dir_file):
    try:
        os.makedirs(f"{dir_path}/{dir_file[0]}/{dir_file[1]}/{dir_file[2]}/{dir_file[3]}", exist_ok=True)
    except Exception as e:
        print(f"Error creating directories: {e}")
        return False
    return True

def writefile(filename, sample_rate, recording):

    try:
        write(filename, sample_rate, recording)
    except Exception as e:
        print(f"Error saving file {filename}: {e}")
        return False
    return True

def record_sample(dir_file, index):
    print(f"[{index+1}/20] Speak now:")
    play_beep()
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  
    filename = f"{dir_path}/{dir_file[0]}/{dir_file[1]}/{dir_file[2]}/{dir_file[3]}/{dir_file[4]}_{index:02d}.wav"
    writefile(filename, sample_rate, recording)
    print(f"Saved: {filename}\n")
    return True


def main():
    # print("Available audio devices:")
    # print(sd.query_devices())

    input_dir = input("Enter voice command (e.g., bat_den/bac/nam/3/sang): ").strip().split('/')
    if len(input_dir) != 5:
        print("Input directory format is not correct, please try again")
        return
    create_directories(input_dir)
    for i in range(20):
        success = record_sample(input_dir, i)
        if not success:
            print("Recording failed, stopping...")
            break
        # time.sleep(1)

    print("Done recording!")

if __name__ == "__main__":
    main()
