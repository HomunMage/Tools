# CTranslate2


## Example
* requirement
  * git lfs system
    * git lfs install
* reference:
  * https://opennmt.net/CTranslate2/guides/transformers.html

```
mkdir Helsinki-NLP
cd Helsinki-NLP
git clone https://huggingface.co/Helsinki-NLP/opus-mt-zh-en/
cd ..
ct2-transformers-converter --model Helsinki-NLP/opus-mt-zh-en --output_dir opus-mt-zh-en
```

## convert srt to dual-lang
python dual-lang.py