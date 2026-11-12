@echo off
echo ============================================================
echo Starting Jupyter Notebook - Unemployment Analysis
echo ============================================================
echo.
echo Kernel: Unemployment Analysis (Task2)
echo.

cd /d "%~dp0"

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Starting Jupyter Notebook...
echo.
echo The notebook will open in your default browser.
echo Your custom kernel "Unemployment Analysis (Task2)" is ready!
echo.
echo Press Ctrl+C to stop the server when done.
echo.

jupyter notebook unemployment_analysis.ipynb

pause
