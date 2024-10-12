# VSCode on windows

Using VSCode with costmized usr/ext folder

and right click have able to open with vscode

### 
---
* launch_vscode.vbs
  * example: 
  * <div class="load_as_code_session" data-url="launch_vscode.vbs">Loading content...</div>
* vscode.bat
  * example: 
  * <div class="load_as_code_session" data-url="vscode.bat">Loading content...</div>
###
--- 
Regedit folder: 電腦\HKEY_CLASSES_ROOT\Directory\shell\VSCode\command
* key:
  * name:
    * (default)
  * data:
    * cmd /c "wscript.exe "C:\<path-to-it>\launch_vscode.vbs" "%V""
* vs.reg
  * example: 
  * <div class="load_as_code_session" data-url="vs.reg">Loading content...</div>


<script src="https://posetmage.com/assets/js/LoadAsCodeSession.js"></script>
