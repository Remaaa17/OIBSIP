# Sales Prediction Using Python

## 📊 Project Overview
This project builds a regression model to predict product sales based on advertising spend across different media channels (TV, Radio, Newspaper).

## 🎯 Objective
Build a regression model that predicts product sales based on advertising spend across different media channels.

## 🛠️ Tech Stack
- **Python 3.x**
- **pandas** - Data manipulation and analysis
- **scikit-learn** - Machine learning models and evaluation
- **matplotlib** - Data visualization
- **seaborn** - Statistical data visualization
- **Jupyter Notebook** - Interactive development environment

## 📋 Feature Checklist
- [x] Data loading and EDA: null check, descriptive statistics, pairplot of all features
- [x] Individual scatter plots: Sales vs. TV spend, Sales vs. Radio spend, Sales vs. Newspaper spend
- [x] Correlation matrix heatmap
- [x] Train/test split
- [x] Train a Linear Regression model as the baseline
- [x] Train at least one additional model (Random Forest Regressor)
- [x] Evaluate using: MAE, RMSE, R² score
- [x] Residual plot for the best model
- [x] Interpretation: which advertising channel has the highest impact on sales?
- [x] Clean, well-commented Jupyter Notebook

## 📁 Dataset
The dataset used is the classic "Advertising.csv" dataset containing:
- **TV**: Advertising spend on TV (in thousands of dollars)
- **Radio**: Advertising spend on Radio (in thousands of dollars)
- **Newspaper**: Advertising spend on Newspaper (in thousands of dollars)
- **Sales**: Product sales (in thousands of units) - Target variable

**Source**: Available on Kaggle or from various ML repositories

## 🚀 How to Run
1. Install required packages:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn jupyter
   ```

2. Download the Advertising.csv dataset and place it in the project folder

3. Open the Jupyter Notebook:
   ```bash
   jupyter notebook sales_prediction.ipynb
   ```

4. Run all cells sequentially

## 📈 Models Used
1. **Linear Regression** (Baseline model)
2. **Random Forest Regressor** (Advanced model)
3. **Polynomial Regression** (Optional enhancement)

## 📊 Evaluation Metrics
- **MAE** (Mean Absolute Error): Average absolute difference between predicted and actual values
- **RMSE** (Root Mean Squared Error): Square root of average squared differences
- **R² Score**: Proportion of variance explained by the model (0 to 1, higher is better)

## 💡 Key Insights
Results will be documented in the notebook showing:
- Which advertising channel has the highest impact on sales
- Model performance comparison
- Prediction accuracy

## 👤 Author
**Eng. Reem Osama**

**Track**: Data Science  
**Task**: Task 5 - Sales Prediction Using Python  
**Organization**: Oasis Infobyte Internship

## 📝 License
This project is part of the Oasis Infobyte Data Science Internship program.

---
#oasisinfobyte #datascience #machinelearning #python #internship
