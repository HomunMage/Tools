# Subtitle 

## Flow:


```mermaid
graph TD;
    Video(Video File)--> ffmpeg;
    ffmpeg --> Audio(Audio File);
    Audio --> Whisper;
    Whisper --> srt(Text File);
    srt --> CTranslate2;
    CTranslate2 --> dual(dual lang);

```


## See Methods:
* [Translate](./Translate.md)
* [Whisper](./Whisper.md)