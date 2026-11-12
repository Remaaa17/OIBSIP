# PowerShell Script to Push All Tasks to GitHub
# Run this AFTER creating the GitHub repositories

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "GitHub Push Script for OIBSIP Tasks" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$baseDir = "c:\Users\Cairo Lap\OneDrive\Desktop\OIBSI _internship of Data Science\-OIBSIP-"

# Task 3: Car Price Prediction
Write-Host "Pushing Task 3: Car Price Prediction..." -ForegroundColor Yellow
cd "$baseDir\DataScience-Task3-CarPricePrediction"
git branch -M main
git remote add origin https://github.com/Remaaa17/OIBSIP-DataScience-Task3-CarPricePrediction.git 2>$null
git push -u origin main
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Task 3 pushed successfully!" -ForegroundColor Green
} else {
    Write-Host "✗ Task 3 push failed. Check if repo exists on GitHub." -ForegroundColor Red
}
Write-Host ""

# Task 4: Email Spam Detection
Write-Host "Pushing Task 4: Email Spam Detection..." -ForegroundColor Yellow
cd "$baseDir\DataScience-Task4-EmailSpamDetection"
git branch -M main
git remote add origin https://github.com/Remaaa17/OIBSIP-DataScience-Task4-EmailSpamDetection.git 2>$null
git push -u origin main
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Task 4 pushed successfully!" -ForegroundColor Green
} else {
    Write-Host "✗ Task 4 push failed. Check if repo exists on GitHub." -ForegroundColor Red
}
Write-Host ""

# Task 5: Sales Prediction
Write-Host "Preparing and pushing Task 5: Sales Prediction..." -ForegroundColor Yellow
cd "$baseDir\DataScience-Task5-SalesPrediction"

# Check if already initialized
if (!(Test-Path ".git")) {
    git init
    git add .
    git commit -m "Initial commit: Sales Prediction with ML"
}

git branch -M main
git remote add origin https://github.com/Remaaa17/OIBSIP-DataScience-Task5-SalesPrediction.git 2>$null
git push -u origin main
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Task 5 pushed successfully!" -ForegroundColor Green
} else {
    Write-Host "✗ Task 5 push failed. Check if repo exists on GitHub." -ForegroundColor Red
}
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Push Complete!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Summary:" -ForegroundColor White
Write-Host "Task 2: Already pushed ✓" -ForegroundColor Green
Write-Host "Task 3: Check status above" -ForegroundColor Yellow
Write-Host "Task 4: Check status above" -ForegroundColor Yellow
Write-Host "Task 5: Check status above" -ForegroundColor Yellow
