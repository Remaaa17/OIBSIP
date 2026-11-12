@echo off
echo ============================================================
echo Starting Jupyter Notebook - Unemployment Analysis
echo ============================================================
echo.

if not exist venv (
    echo Virtual environment not found!
    echo Please run setup_environment.bat first
    pause
    exit /b 1
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Starting Jupyter Notebook...
echo.
echo NOTE: Press Ctrl+C to stop the server when done
echo.
jupyter notebook unemployment_analysis.ipynb

pause
