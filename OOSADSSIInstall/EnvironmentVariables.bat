@echo off
set $env=%Path%;C:\Python27\;C:\Python27\Scripts\;
set /m Path "%$env%"
ECHO.%Path:;= & ECHO.%
pause
call .\AutoPip.bat