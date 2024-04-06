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

# Extract the m4a
docker exec whisper ffmpeg -i "$input_file" -vn -c:a copy "$output_m4a"

./audio2srt.sh "$output_m4a"