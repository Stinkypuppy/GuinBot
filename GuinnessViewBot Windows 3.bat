@echo off
SETLOCAL EnableDelayedExpansion
SET "TEMP_DIR=%LOCALAPPDATA%\TempScriptDir"
MD "%TEMP_DIR%"
XCOPY ".\*" "%TEMP_DIR%" /E /I /Q
IF NOT EXIST "%ProgramFiles%\Chocolatey\choco.exe" (
    powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" > NUL
)
IF NOT EXIST "%LOCALAPPDATA%\Programs\Python\Python39\python.exe" (
    choco install python3 -y
)
CD /D "%TEMP_DIR%"
ECHO @echo off > temp_script.bat
ECHO CD "%TEMP_DIR%\data" >> temp_script.bat
ECHO curl https://bootstrap.pypa.io/get-pip.py -o yiffmedaddy.py >> temp_script.bat
ECHO python yiffmedaddy.py >> temp_script.bat
ECHO pip install requests urllib3 pystyle >> temp_script.bat
ECHO python GuinnessViewBot.py >> temp_script.bat
START "" cmd /c temp_script.bat
tasklist | find /i "temp_script.bat" >nul 2>&1
IF ERRORLEVEL 1 (
    DEL "%TEMP_DIR%\temp_script.bat"
    RMDIR /S /Q "%TEMP_DIR%"
    GOTO End
)
TIMEOUT /T 5 /NOBREAK >NUL
GOTO Monitor
ENDLOCAL
