call conda_py310.bat
call set input_file=%~1
call set output_m4a=%~dpn1.m4a
call set output_mkv=%~dpn1.mkv
call set output_srt=%~dpn1.srt

ffmpeg -i "%input_file%" -vn -acodec copy "%output_m4a%"
python %audio2srt_py% "%output_m4a%" "%output_srt%"
