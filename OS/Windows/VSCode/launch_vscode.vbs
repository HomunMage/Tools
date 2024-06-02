Set objShell = CreateObject("WScript.Shell")
objShell.Run "vscode.bat " & WScript.Arguments.Item(0), 0, False