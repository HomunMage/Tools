# Subtitle 

Subtitle with dual-lang

* Requirement:
  * [Whisper](./Whisper/)
  * [CTranslate2](./CTranslate2/)
* usage:
  * powershell example:
  * <div class="load_as_code_session" data-url="convert.ps1">Loading content...</div>

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

<script src="{{ '/assets/js/LoadAsCodeSession.js' | relative_url }}"></script>