import subprocess
import sys
import whisper
import os


mp3_file = sys.argv[1]
[filename, extension] = mp3_file.split('.')
command = ['ffmpeg', '-i', f"mps/{mp3_file}", '-ac', '1', f'{filename}.wav']
subprocess.run(command)


model = whisper.load_model("turbo")
wav_file = f"{filename}.wav"
result = model.transcribe(wav_file, fp16=False)

with open(f"texts/{filename}.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

try:
    os.remove(wav_file)
    print("\n","-------------------------------")
    print("|  File removed successfully  |")
    print("\n","-------------------------------")
except FileNotFoundError:
    print("File not found")

