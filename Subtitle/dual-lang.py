import ctranslate2
import transformers

translator = ctranslate2.Translator("opus-mt-zh-en")
tokenizer = transformers.AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")

input_filename = "input.srt"
output_filename = "output.srt"

with open(input_filename, "r", encoding="utf-8") as input_file:
    lines = input_file.readlines()

srt = ""
subtitle_id = 1
time = ""
text = ""

for line in lines:
    if line.strip().isdigit():
        subtitle_id = int(line.strip())
    elif "-->" in line:
        time = line
    elif line.strip() == "":
        source = tokenizer.convert_ids_to_tokens(tokenizer.encode(text.strip()))
        results = translator.translate_batch([source])
        target = results[0].hypotheses[0]
        translated_text = tokenizer.decode(tokenizer.convert_tokens_to_ids(target))
        srt += f"{subtitle_id}\n{time}{text.strip()}\n{translated_text}\n\n"
        subtitle_id += 1
        text = ""
    else:
        text += line

with open(output_filename, "w", encoding="utf-8") as output_file:
    output_file.write(srt)
