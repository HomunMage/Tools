# Whisper

## Request
python  >=3.7, < 3.11

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

## convert video to srt
convert.ps1

## 其他參考資料
https://www.youtube.com/watch?v=YhLyeOJIoGE
