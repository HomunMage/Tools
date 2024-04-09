#!/bin/bash

echo "Updating yt-dlp..."
docker exec yt-dlp yt-dlp --update

echo "Processing URLs from url.txt..."
for line in $(cat url.txt); do
    echo "Downloading URL: $line"
    docker exec yt-dlp yt-dlp -f 22 "$line"
    docker exec yt-dlp yt-dlp -f 140 "$line"
done
