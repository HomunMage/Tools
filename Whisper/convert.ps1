<<WhisperInstallPath>>\Whisper\Scripts\Activate.ps1
ffmpeg -i input.mkv -vn -acodec copy output.m4a
whisper output.m4a --language zh --model medium > output.txt
python ./conpert.py