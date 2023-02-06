ffmpeg -i input.mkv -vn -acodec copy output.m4a
python ./convert.py
python ./dual-lang.py
