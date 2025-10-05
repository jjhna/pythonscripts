@echo off
setlocal

set PYTHON_DIRECTORY=%~dp0python\
set SCRIPT_NAME=%~dp0csv2xml.py
"%PYTHON_DIRECTORY%python.exe" "%SCRIPT_NAME%" %*
pause
endlocal