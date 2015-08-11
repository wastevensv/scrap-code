@echo off
cd /d "%~dp0"

tasklist /fi "imagename eq pulse.exe" 2>NUL | findstr /I /N "pulse.exe">NUL

IF "%ERRORLEVEL%"=="0" (
   echo Pulse is running
) ELSE (
   syncthing -logfile="C:\Users\William\Pulse\pulse.log" -no-browser
)

exit 0