fn = InputBox("Base file name")
am = InputBox("# of files to create (up to 999)")
ext = InputBox("File extension")
For i = 1 to am
	call createFile(fn,i,ext)
	
Next
Public Sub createFile(fileName,n,fileExt)
 
	Dim fso,myFile
	n  = RIGHT(String(3, "0") & n, 3)
	filePath = fn & n & "." &fileExt
	Set fso=CreateObject("Scripting.FileSystemObject")
	Set MyFile= fso.CreateTextFile( filePath )
	MyFile.WriteLine("This is a separate file")
	MyFile.close
 
End Sub