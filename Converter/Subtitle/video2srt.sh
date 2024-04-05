#!/bin/bash

start_time=$(date +%s) # Capture start time

# Ensure an argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

# Extract the directory, filename without extension, and extension
input_file="$1"
dir_name=$(dirname "$input_file")
file_name=$(basename "$input_file")
base_name="${file_name%.*}"

# Define output filenames
output_m4a="$dir_name/$base_name.m4a" # Define the output m4a file name
output_srt="$dir_name/$base_name.tmp.srt"
zh_tw_srt="$dir_name/$base_name.srt"

# Extract the m4a
docker exec whisper ffmpeg -i "$input_file" -vn -c:a copy "$output_m4a"

# Generate SRT using the input file
docker exec whisper python ./audio2srt.py "$output_m4a" "$output_srt"

# Convert SRT to Traditional Chinese
docker exec whisper opencc -i "$output_srt" -o "$zh_tw_srt" -c s2twp.json

end_time=$(date +%s) # Capture end time

# Calculate and display total execution time
total_time=$((end_time - start_time))
echo "Total execution time: $total_time seconds"
