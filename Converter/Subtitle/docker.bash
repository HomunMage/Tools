# docker create --name whisper -it -v "$(pwd)":/usr/src/app -w /usr/src/app python:3.8-slim bash
# docker exec whisper pip install openai-whisper