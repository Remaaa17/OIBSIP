# Task 3: Car Price Prediction - Complete Checklist

## Status: Ready to Start

### Phase 1: Data Acquisition
- [ ] Download dataset from Kaggle
  - URL: https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho
  - Run: `python download_dataset.py`
- [ ] Verify dataset has all required columns
- [ ] Place as `car_data.csv` in project folder

### Phase 2: Data Cleaning (Required)
- [ ] Load dataset and check shape
- [ ] Check for null values in all columns
- [ ] Handle nulls (drop/fill based on percentage)
- [ ] Remove duplicate rows
- [ ] Fix inconsistent categorical values
  - [ ] Standardize Fuel_Type (Petrol/petrol → Petrol)
  - [ ] Standardize Transmission (Manual/manual → Manual)
  - [ ] Check Seller_Type consistency
- [ ] Standardize column names (remove spaces)

### Phase 3: Feature Engineering (Required)
- [ ] Create Car_Age feature
  - Formula: 2024 - Year
- [ ] Extract Brand from Car_Name
  - Method: Split by space, take first word
- [ ] Optional additional features:
  - [ ] Depreciation = Present_Price - Selling_Price
  - [ ] Depreciation_Rate = (Depreciation / Present_Price) * 100
  - [ ] Price_per_KM = Selling_Price / Kms_Driven

### Phase 4: Exploratory Data Analysis (Required)
- [ ] Price distribution
  - [ ] Histogram of Selling_Price
  - [ ] Box plot of Selling_Price
  - [ ] Calculate mean, median, std dev
- [ ] Price vs Fuel Type
  - [ ] Box plots for each fuel type
  - [ ] Calculate average price per fuel type
- [ ] Price vs Car Age
  - [ ] Scatter plot
  - [ ] Calculate correlation coefficient
- [ ] Additional EDA:
  - [ ] Price vs Transmission
  - [ ] Price vs Owner count
  - [ ] Price vs Kilometers driven
  - [ ] Top brands analysis

### Phase 5: Data Preprocessing (Required)
- [ ] Encode categorical variables
  - Method A: One-Hot Encoding (creates multiple columns)
  - Method B: Label Encoding (creates single numeric column)
  - [ ] Encode Fuel_Type
  - [ ] Encode Seller_Type
  - [ ] Encode Transmission
  - [ ] Encode or handle Brand (many categories)
- [ ] Create feature correlation heatmap
  - [ ] Identify highly correlated features
  - [ ] Select relevant features for modeling
- [ ] Prepare X (features) and y (target: Selling_Price)

### Phase 6: Model Training (Required - Minimum 2 Models)
- [ ] Split data: Train/Test (80/20 or 70/30)
- [ ] Train Model 1: Linear Regression (Baseline)
  - [ ] Fit on training data
  - [ ] Make predictions on test data
- [ ] Train Model 2: Random Forest Regressor (Recommended)
  - [ ] Configure parameters (n_estimators, max_depth)
  - [ ] Fit on training data
  - [ ] Make predictions on test data
- [ ] Optional Model 3: Gradient Boosting
- [ ] Optional Model 4: XGBoost
- [ ] Optional Model 5: Ridge/Lasso Regression

### Phase 7: Model Evaluation (Required)
- [ ] Calculate metrics for each model:
  - [ ] MAE (Mean Absolute Error) - in lakhs
  - [ ] RMSE (Root Mean Squared Error) - in lakhs
  - [ ] R² Score (0 to 1, higher is better)
- [ ] Create comparison table
  - [ ] Sort models by R² score
  - [ ] Identify best performing model
- [ ] Visualize model comparison
  - [ ] Bar charts for each metric
  - [ ] Side-by-side comparison

### Phase 8: Model Insights (Required)
- [ ] Feature importance analysis
  - [ ] For tree-based models (Random Forest, Gradient Boosting)
  - [ ] Create horizontal bar chart
  - [ ] Identify top 5 most important features
- [ ] Predictions visualization
  - [ ] Actual vs Predicted scatter plot
  - [ ] Add perfect prediction line (diagonal)
  - [ ] Calculate prediction accuracy
- [ ] Error analysis
  - [ ] Identify largest prediction errors
  - [ ] Understand where model struggles

### Phase 9: Documentation (Required)
- [ ] Clean code in all cells
- [ ] Add comments explaining complex logic
- [ ] Markdown cells between major sections
- [ ] Clear section headers
- [ ] Observations after each visualization
- [ ] Summary of findings at end
- [ ] Model performance comparison
- [ ] Recommendations and conclusions

### Phase 10: Final Checks
- [ ] Run all cells from top to bottom
- [ ] Verify no errors occur
- [ ] Check all visualizations display correctly
- [ ] Verify metrics make sense
- [ ] Spell check markdown cells
- [ ] Remove any unnecessary code
- [ ] Save notebook with outputs

## Minimum Requirements Met When:
- [x] Dataset downloaded
- [ ] All data cleaning steps completed
- [ ] Both required features engineered (Age, Brand)
- [ ] All 3 required EDA plots created
- [ ] Categorical encoding completed
- [ ] Correlation heatmap created
- [ ] Train/test split performed
- [ ] At least 2 models trained
- [ ] All 3 metrics calculated (MAE, RMSE, R²)
- [ ] Feature importance chart created
- [ ] Notebook is clean and commented

## Success Criteria

**Target Metrics:**
- R² Score: > 0.85 (85% accuracy)
- RMSE: < 2 lakhs
- MAE: < 1.5 lakhs

**Best Practices:**
- Code runs without errors
- Visualizations are clear and labeled
- Findings are well-documented
- Model comparison is thorough
- Insights are actionable

---

**Author:** Eng. Reem Osama  
**Task:** Task 3 - Car Price Prediction  
**Organization:** Oasis Infobyte

**Status:** [ ] In Progress  [ ] Ready for Review  [ ] Complete
