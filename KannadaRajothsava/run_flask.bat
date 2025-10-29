@echo off
REM Flask Setup and Run Script for Kannada Rajyotsava Website
REM Windows Batch File

echo ======================================================================
echo    KANNADA RAJYOTSAVA 2025 - FLASK SERVER SETUP
echo ======================================================================
echo    Karnataka Rajyotsava - Flask Web Application
echo ======================================================================

echo.
echo [1/4] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.6+ from https://python.org
    pause
    exit /b 1
)
python --version

echo.
echo [2/4] Installing dependencies...
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [3/4] Generating QR codes...
python generate_qr.py
if errorlevel 1 (
    echo WARNING: QR code generation failed, but continuing...
)

echo.
echo [4/4] Starting Flask server...
echo.
echo Flask server will start in 3 seconds...
echo Press Ctrl+C to stop the server
timeout /t 3 /nobreak >nul

python main.py

echo.
echo Server stopped. Thank you for celebrating Kannada Rajyotsava!
echo ಧನ್ಯವಾದಗಳು! ^| Thank you!
pause