@echo off
setlocal enabledelayedexpansion

set input_file=%~1
set renamed_file=%~n1.old%~x1
set output_audio=%~n1.m4a

rem Rename the original file
rename "%input_file%" "%renamed_file%"

rem Process the video
ffmpeg -i "%renamed_file%" -c:v copy -c:a aac -b:a 192k -af "acompressor=threshold=-20dB:ratio=4:attack=200:release=1000,volume=1.5" "%input_file%"

rem Extract the audio
ffmpeg -i "%input_file%" -vn -c:a copy "%output_audio%"

endlocal
