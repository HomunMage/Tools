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
output_srt="$dir_name/$base_name.tmp.srt"
zh_tw_srt="$dir_name/$base_name.srt"

container_name="whisper"
lock_file="/tmp/audio2srt.lock"
if docker exec $container_name test -f "$lock_file"; then
    echo "Process is already running."
    exit
else
    docker exec $container_name touch "$lock_file"
    # Generate SRT using the input file
    docker exec $container_name python ./audio2srt.py "$input_file" "$output_srt"
    docker exec $container_name rm -f "$lock_file"
fi

end_time=$(date +%s) # Capture end time

# Calculate and display total execution time
total_time=$((end_time - start_time))
echo "Total execution time: $total_time seconds"

# Convert SRT to Traditional Chinese
docker exec whisper opencc -i "$output_srt" -o "$zh_tw_srt" -c s2twp.json