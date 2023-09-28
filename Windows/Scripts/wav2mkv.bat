call set input_file=%~1
call set output_m4a=%~dpn1.m4a
call set output_mkv=%~dpn1.mkv
call set output_srt=%~dpn1.srt

ffmpeg -i "%input_file%" -c:a aac -b:a 320k -strict -2 "%output_m4a%"
ffmpeg -i "%output_m4a%" -loop 1 -i LatticeMageCover.png -c:v h264_nvenc -c:a copy -shortest "%output_mkv%"

echo M4A file saved as %output_m4a%
echo MKV file saved as %output_mkv%