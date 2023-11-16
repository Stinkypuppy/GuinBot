@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
WHERE choco >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    SET "CHOCO_INSTALL_SCRIPT=https://chocolatey.org/install.ps1"
    PowerShell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('%CHOCO_INSTALL_SCRIPT%'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
WHERE python >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    choco install python -y
)
SET "temp_dir=%localappdata%\temp_script_dir"
XCOPY /E /I . "%temp_dir%"
(
echo @echo off
echo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
echo python get-pip.py
echo pip install requests urllib3 pystyle
echo cd data
echo python GuinnessViewBot.py
) > "%temp_dir%\run_script.bat"
(
echo @echo off
echo :LOOP
echo tasklist | find /i "python" >nul 2>nul
echo IF NOT ERRORLEVEL 1 (
echo   timeout /t 5 /nobreak >nul
echo   GOTO LOOP
echo )
echo del "%temp_dir%\run_script.bat"
) > "%temp_dir%\monitor_script.bat"
start "" "%temp_dir%\run_script.bat"
start "" "%temp_dir%\monitor_script.bat"
