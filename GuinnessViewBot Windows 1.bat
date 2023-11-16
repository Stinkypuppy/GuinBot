@echo off
where /q choco
if %errorlevel% neq 0 (
    :: Install Chocolatey
    @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
)
choco install python -y
CALL :REFRESHENV
SET PATH=%PATH%;C:\Python39\Scripts\;C:\Python39\
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install requests pystyle urllib3
start cmd /k "cd data && python GuinnessViewBot.py"
@FOR /F "tokens=*" %%i IN ('choco source') DO CALL %%i
GOTO :EOF
