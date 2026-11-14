@echo off
echo [SpherePrime] Generating assets...
python generate_profile_assets.py
if errorlevel 1 goto error
echo [SpherePrime] Assets generated successfully!
exit /b 0

:error
echo [SpherePrime] Error generating assets!
exit /b 1
