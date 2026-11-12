@echo off
echo ============================================================
echo Setting up Python Environment for Unemployment Analysis
echo ============================================================
echo.

echo Step 1: Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: Failed to create virtual environment
    echo Please ensure Python is installed and added to PATH
    pause
    exit /b 1
)
echo Virtual environment created successfully!
echo.

echo Step 2: Activating virtual environment...
call venv\Scripts\activate.bat
echo.

echo Step 3: Upgrading pip...
python -m pip install --upgrade pip
echo.

echo Step 4: Installing required packages...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install packages
    pause
    exit /b 1
)
echo.

echo ============================================================
echo Setup Complete!
echo ============================================================
echo.
echo To use the environment:
echo 1. Activate it: venv\Scripts\activate
echo 2. Run Jupyter: jupyter notebook unemployment_analysis.ipynb
echo.
echo Or simply run: run_notebook.bat
echo.
pause
