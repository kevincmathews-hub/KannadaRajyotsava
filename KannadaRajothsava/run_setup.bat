@echo off
REM Kannada Rajyotsava 2025 - Windows Setup Script
REM This batch file makes it easy to run the setup on Windows

title Kannada Rajyotsava 2025 Setup

echo.
echo ================================================================
echo   KANNADA RAJYOTSAVA 2025 - WINDOWS SETUP
echo ================================================================
echo   ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ - ವಿಂಡೋಸ್ ಸೆಟಪ್
echo ================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed or not in PATH
    echo    Please install Python 3.6 or higher from python.org
    echo    Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo ✅ Python found - proceeding with setup...
echo.

REM Run the Python setup script
python setup.py

echo.
echo Press any key to exit...
pause >nul