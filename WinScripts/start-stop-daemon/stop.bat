@echo off
tasklist /fi "imagename eq syncthing.exe" 2>NUL | findstr /I /N "syncthing.exe">NUL

IF "%ERRORLEVEL%"=="0" (
   taskkill /F /IM syncthing.exe
   echo Pulse is running
) ELSE (
  echo Pulse isn't running
)