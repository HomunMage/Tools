# VSCode on windows

Using VSCode with costmized usr/ext folder

## Regedit
* folder: 電腦\HKEY_CLASSES_ROOT\Directory\shell\VSCode\command
* key:
  * name:
    * (default)
  * data:
    * cmd /c "wscript.exe "C:\<path to it>\launch_vscode.vbs" "%V""