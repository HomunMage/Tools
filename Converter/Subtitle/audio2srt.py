import sys
import whisper
import os
from datetime import timedelta

if len(sys.argv) != 3:
    print("Usage: python converter.py input.m4a output.srt")
    sys.exit(1)

input_filename = sys.argv[1]
srt_filename = sys.argv[2]

model = whisper.load_model("large")
result = model.transcribe(input_filename)

# Open the previously created file for writing
with open(srt_filename, "w", encoding="utf-8") as srt_file:
    for segment in result["segments"]:
        start_time = str(timedelta(seconds=int(segment['start'])))
        end_time = str(timedelta(seconds=int(segment['end'])))
        text = segment['text']
        srt_file.write(f"{segment['id'] + 1}\n{start_time} --> {end_time}\n{text}\n\n")
        srt_file.flush()    # Flush the Python buffer
        os.fsync(srt_file.fileno())    # Flush the OS buffer

print("SRT file saved as " + srt_filename)
