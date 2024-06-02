import whisper
import os
from datetime import timedelta

model = whisper.load_model("medium", "cuda")
result = model.transcribe("output.m4a")
srt_filename = "input.srt"

def to_srt(result):
    segments = result["segments"]
    srt = ""
    
    for segment in segments:
        start_time = str(timedelta(seconds=int(segment['start'])))
        end_time = str(timedelta(seconds=int(segment['end'])))
        text = segment['text']
        srt += f"{segment['id'] + 1}\n{start_time} --> {end_time}\n{text}\n\n"
        
    return srt

srt_text = to_srt(result)


with open(srt_filename, "w", encoding="utf-8") as srt_file:
    srt_file.write(srt_text)

print("SRT file saved as" + srt_filename)
