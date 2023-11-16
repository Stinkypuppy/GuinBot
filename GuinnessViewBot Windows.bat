@echo off
where /q choco
if %errorlevel% neq 0 (
    echo Chocolatey not found. Installing Chocolatey...
    @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
)
where /q python
if %errorlevel% neq 0 (
    echo Python not found. Installing Python...
    choco install python -y
)
setx PATH "%PATH%;C:\Python39\Scripts\;C:\Python39\"
start cmd /k "cd data & python GuinnessViewBot.py"
