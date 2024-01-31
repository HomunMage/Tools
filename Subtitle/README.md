# Subtitle 

Subtitle with dual-lang

* Requirement:
  * [Whisper](./Whisper.md)
  * [CTranslate2](./CTranslate2.md)
* usage:
  * convert.ps1

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
