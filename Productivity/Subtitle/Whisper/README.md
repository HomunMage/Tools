# Whisper 
* Requirement
  * python  >=3.7, < 3.11
  * ffmpeg

## install (GPU ver)
```
pip install git+https://github.com/openai/whisper.git 
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
pip uninstall torch
pip cache purge
pip install torch -f https://download.pytorch.org/whl/torch_stable.html
```

## use whisper (command ver)
need to source activate script

```
<<WhisperInstallPath>>\Scripts\Activate.ps1
whisper intput.m4a --language zh --model medium > test1.txt
```

## use whisper (py ver)
python convert.py

## other reference:
https://www.youtube.com/watch?v=YhLyeOJIoGE
