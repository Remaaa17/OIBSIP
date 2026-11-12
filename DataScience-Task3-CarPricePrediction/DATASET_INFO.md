# Dataset Information - Car Price Prediction

## Dataset Found!

**Source:** Kaggle  
**Dataset Name:** Vehicle dataset from cardekho  
**Author:** nehalbirla  
**Direct Link:** https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho

## Dataset Details

### File Information
**Filename:** CAR DETAILS FROM CAR DEKHO.csv or car data.csv  
**Format:** CSV  
**Source Website:** www.cardekho.com (India's leading car marketplace)

### Dataset Features

The dataset contains information about used cars with the following columns:

1. **Car_Name** - Name/Model of the car
2. **Year** - Manufacturing year
3. **Selling_Price** - Price at which car was sold (Target variable)
4. **Present_Price** - Current showroom price of the car
5. **Kms_Driven** - Total kilometers driven
6. **Fuel_Type** - Type of fuel (Petrol/Diesel/CNG)
7. **Seller_Type** - Type of seller (Dealer/Individual)
8. **Transmission** - Transmission type (Manual/Automatic)
9. **Owner** - Number of previous owners (0/1/3)

### Dataset Characteristics

**Size:** ~300 rows  
**Time Period:** Used cars data from India  
**Target Variable:** Selling_Price (in lakhs INR)  
**Features:** Mix of numerical and categorical

### Use Cases

This dataset is perfect for:
- Regression modeling
- Price prediction
- Feature engineering practice
- EDA and visualization
- Comparing multiple ML algorithms

## How to Download

### Method 1: Using Kaggle Website

1. Go to: https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho
2. Sign in to your Kaggle account
3. Click "Download" button
4. Extract the CSV file
5. Rename to `car_data.csv` (if needed)
6. Place in this folder

### Method 2: Using Kaggle API

```bash
kaggle datasets download -d nehalbirla/vehicle-dataset-from-cardekho
```

### Method 3: Using kagglehub (Python)

```python
import kagglehub
path = kagglehub.dataset_download("nehalbirla/vehicle-dataset-from-cardekho")
print("Dataset downloaded to:", path)
```

## Expected Data Structure

```
Car_Name           | Year | Selling_Price | Present_Price | Kms_Driven | Fuel_Type | Seller_Type | Transmission | Owner
-------------------|------|---------------|---------------|------------|-----------|-------------|--------------|-------
ritz               | 2014 | 3.35          | 5.59          | 27000      | Petrol    | Dealer      | Manual       | 0
sx4                | 2013 | 4.75          | 9.54          | 43000      | Diesel    | Dealer      | Manual       | 0
ciaz               | 2017 | 7.25          | 9.85          | 6900       | Petrol    | Dealer      | Manual       | 0
wagon r            | 2011 | 2.85          | 4.15          | 5200       | Petrol    | Dealer      | Manual       | 0
swift              | 2014 | 4.60          | 6.87          | 42450      | Diesel    | Dealer      | Manual       | 0
```

**Note:** Prices are in Indian Lakhs (1 Lakh = 100,000 INR)

## Data Quality

**Expected Issues:**
- May have missing values
- Some inconsistencies in naming
- Outliers in price/mileage
- Need for feature engineering

## Feature Engineering Opportunities

1. **Car Age** = Current Year - Year
2. **Brand Extraction** = Extract brand from Car_Name
3. **Price per KM** = Selling_Price / Kms_Driven
4. **Depreciation** = Present_Price - Selling_Price
5. **Depreciation Rate** = (Present_Price - Selling_Price) / Present_Price

## ML Models to Try

Based on similar projects, these models work well:

1. **Linear Regression** - Baseline model
2. **Ridge/Lasso Regression** - With regularization
3. **Decision Tree Regressor** - Non-linear relationships
4. **Random Forest Regressor** - Ensemble method (often best)
5. **Gradient Boosting** - Advanced ensemble
6. **XGBoost** - High performance

## Expected Model Performance

Based on similar projects:
- **R² Score:** 0.85 - 0.95
- **RMSE:** 1-2 lakhs
- **MAE:** 0.5-1.5 lakhs

**Best Model:** Usually Random Forest or XGBoost with 90-95% accuracy

## Alternative Datasets

If the primary dataset is unavailable, search for:
- "car price prediction India"
- "used car dataset"
- "automobile price dataset"
- "vehicle selling price data"

## Citation

If using this dataset, cite:
- Source: Kaggle
- Author: nehalbirla
- Dataset: Vehicle dataset from cardekho
- URL: https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho

## Next Steps

1. Download the dataset
2. Place in project folder as `car_data.csv`
3. Run the Jupyter notebook
4. Explore and clean the data
5. Build prediction models
6. Evaluate and compare results

---

**Ready to Download?** Visit: https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho

**Author:** Eng. Reem Osama  
**Task:** Task 3 - Car Price Prediction  
**Organization:** Oasis Infobyte
