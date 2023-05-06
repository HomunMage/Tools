# Markdonw To Docx

convert mermaid to png and then replace to ```![]()``` in markdown  
convert markdown to html then convert to docx  
upload to drive and open with google doc (usually cannot open by microsoft office word)

## requierment

* npm
    * mmdc
* python
    * pypandoc
    * markdown

```
npm install -g mermaid.cli
pip install pypandoc markdown
```

## usage 
```
python Markdown2DOCX.py -i input.md -of ./
```