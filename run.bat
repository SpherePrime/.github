@echo off
echo [SpherePrime] Building assets...
call build.bat
if errorlevel 1 goto error
echo [SpherePrime] Opening SpherePrime profile...
start https://github.com/SpherePrime
exit /b 0

:error
echo [SpherePrime] Build failed!
exit /b 1
