#!/bin/bash

echo "Updating yt-dlp..."
yt-dlp --update

echo "Processing URLs from url.txt..."
for line in $(cat url.txt); do
    echo "Downloading URL: $line"
    yt-dlp -f 22 "$line"
    yt-dlp -f 140 "$line"
done
