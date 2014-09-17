#hide cmd window while running .exe file

Set ws = CreateObject("Wscript.Shell")
ws.run "cmd /c CheckIn.exe",vbhide 
