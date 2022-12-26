# Whisper

## install

pip install git+https://github.com/openai/whisper.git 
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
pip uninstall torch
pip cache purge
pip install torch -f https://download.pytorch.org/whl/torch_stable.html


## use
..\Scripts\Activate.ps1
whisper intput --language zh --model medium > test1.txt
