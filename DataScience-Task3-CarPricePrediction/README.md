# Car Price Prediction with Machine Learning

## Project Overview
Build a regression model that predicts the selling price of a used car based on features such as brand, age, mileage, fuel type, and transmission.

## Objective
Train multiple machine learning regression models to accurately predict used car prices and compare their performance using standard evaluation metrics.

## Tech Stack
- Python
- pandas - Data manipulation
- scikit-learn - Machine learning
- matplotlib - Data visualization
- seaborn - Statistical visualization
- Jupyter Notebook - Interactive development

## Feature Checklist

### Data Acquisition
- [ ] Download suitable car dataset from Kaggle
  - Recommended: "Vehicle dataset from cardekho" by nehalbirla
  - Link: https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho

### Data Cleaning
- [ ] Handle null values (check and fill/drop as appropriate)
- [ ] Remove duplicate rows
- [ ] Address inconsistent categorical values (e.g., "Petrol" vs "petrol")
- [ ] Standardize column names

### Feature Engineering
- [ ] Calculate car age from year column (current_year - year)
- [ ] Extract brand from car name column (first word)
- [ ] Create additional features if beneficial (depreciation rate, price per km, etc.)

### Exploratory Data Analysis (EDA)
- [ ] Distribution of selling prices (histogram + box plot)
- [ ] Price vs fuel type (box plots)
- [ ] Price vs car age (scatter plot)
- [ ] Price vs transmission type
- [ ] Price vs kilometers driven
- [ ] Analyze top brands and their average prices

### Data Preprocessing
- [ ] Encode categorical variables
  - One-Hot Encoding OR Label Encoding
  - Apply to: Fuel Type, Seller Type, Transmission, Brand
- [ ] Feature correlation heatmap (identify relationships)
- [ ] Select relevant features for modeling

### Model Training
- [ ] Train/test split (typically 80-20 or 70-30)
- [ ] Train at least 2 regression models:
  - [ ] Linear Regression (baseline)
  - [ ] Random Forest Regressor (recommended)
  - [ ] Additional: Gradient Boosting / XGBoost / Ridge / Lasso

### Model Evaluation
- [ ] Evaluate all models using:
  - [ ] MAE (Mean Absolute Error)
  - [ ] RMSE (Root Mean Squared Error)
  - [ ] R² Score (Coefficient of Determination)
- [ ] Compare model performance
- [ ] Identify best-performing model

### Model Insights
- [ ] Feature importance chart for best model
- [ ] Analyze which features most pricing
- [ ] Actual vs Predicted price visualization

### Documentation
- [ ] Clean, well-commented Jupyter Notebook
- [ ] Clear markdown explanations between code cells
- [ ] Summary of findings and model performance
- [ ] All visualizations properly labeled

## Dataset Information

**Source:** Kaggle - Vehicle dataset from cardekho  
**Link:** https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho

**Expected Features:**
- Car_Name - Model/Brand name
- Year - Manufacturing year
- Selling_Price - Target variable (in lakhs INR)
- Present_Price - Current showroom price
- Kms_Driven - Total kilometers driven
- Fuel_Type - Petrol/Diesel/CNG
- Seller_Type - Dealer/Individual
- Transmission - Manual/Automatic
- Owner - Number of previous owners

## How to Run

### Step 1: Setup Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Step 2: Download Dataset
```bash
python download_dataset.py
```
Or download manually from Kaggle and place as `car_data.csv`

### Step 3: Run Analysis
```bash
jupyter notebook car_price_prediction.ipynb
```

## Expected Results

**Model Performance Targets:**
- R² Score: 0.85 - 0.95
- RMSE: 1-2 lakhs
- MAE: 0.5-1.5 lakhs

**Best Models:** Usually Random Forest or Gradient Boosting

## Project Structure
```
DataScience-Task3-CarPricePrediction/
 car_price_prediction.ipynb  # Main analysis notebook
 car_data.csv                # Dataset (download required)
 download_dataset.py         # Dataset download script
 requirements.txt            # Python dependencies
 README.md                   # This file
 DATASET_INFO.md            # Detailed dataset documentation
 TASK3_START.md             # Quick start guide
```

## Author

**Eng. Reem Osama**  
**Track:** Data Science  
**Task:** Task 3 - Car Price Prediction  
**Organization:** Oasis Infobyte

---

**Keywords**: Machine Learning, Regression Analysis, Data Science, Python, Scikit-learn, Automotive Pricing
