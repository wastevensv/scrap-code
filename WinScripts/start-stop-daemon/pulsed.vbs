Set objShell = CreateObject("Wscript.Shell")

strPath = Wscript.ScriptFullName

Set objFSO = CreateObject("Scripting.FileSystemObject")

Set objFile = objFSO.GetFile(strPath)
strFolder = objFSO.GetParentFolderName(objFile)
If WScript.Arguments.Count = 0 then
    WScript.Echo "Missing parameters"
Else
    If Wscript.Arguments.Item(0) = "start" Then
        objShell.Run strFolder+"\start.bat", 0, False
    ElseIf Wscript.Arguments.Item(0) = "stop" Then
        objShell.Run strFolder+"\stop.bat", 0, False
    Else
        Wscript.Echo "Unknown command. Use start or stop"
    End If
End If