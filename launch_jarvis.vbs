' JARVIS Silent Launcher — hides the command prompt window
' This script is placed in the Windows Startup folder to auto-launch Jarvis on boot

Set WshShell = CreateObject("WScript.Shell")
WshShell.Run """C:\Users\DELL\OneDrive\Desktop\New folder\jarvis\launch_jarvis.bat""", 0, False
Set WshShell = Nothing
