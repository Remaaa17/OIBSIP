# Task 1: Iris Flower Classification - Project Report

**Author:** Eng. Reem Osama  
**Internship:** Oasis Infobyte - Data Science Track  
**Date:** November 2026  
**Status:** Completed

---

## Project Overview

This project implements a multi-class classification system to identify three species of iris flowers (Setosa, Versicolor, and Virginica) based on physical measurements of their petals and sepals.

## Dataset Information

- **Source:** Scikit-learn built-in dataset (iris dataset)
- **Samples:** 150 observations (50 per species)
- **Features:** 4 numerical measurements
  - Sepal Length (cm)
  - Sepal Width (cm)
  - Petal Length (cm)
  - Petal Width (cm)
- **Target Classes:** 3 species (Setosa, Versicolor, Virginica)
- **Data Quality:** Complete dataset with no missing values

## Technical Approach

### Data Preprocessing
- Loaded iris dataset from scikit-learn
- Explored data distribution across features and classes
- Applied feature scaling using StandardScaler
- Split data into training (80%) and testing (20%) sets with stratification

### Models Implemented
1. **Logistic Regression** - Linear classification baseline
2. **K-Nearest Neighbors (KNN)** - Distance-based classification
3. **Decision Tree Classifier** - Rule-based classification
4. **Random Forest Classifier** - Ensemble method

### Evaluation Metrics
- Accuracy Score
- Confusion Matrix
- Classification Report (Precision, Recall, F1-Score)
- Feature Importance Analysis

## Key Results

### Model Performance
All models achieved excellent accuracy (>90%) due to clear class separation in the dataset:

- **Logistic Regression:** High accuracy with simple linear boundaries
- **K-Nearest Neighbors:** Strong performance with distance-based classification
- **Decision Tree:** Interpretable rules with good accuracy
- **Random Forest:** Best overall performance with ensemble approach

### Feature Importance
Analysis revealed that petal measurements (length and width) are the most discriminative features for species classification, showing stronger correlation with species than sepal measurements.

### Class Separability
- **Setosa:** Easily separable from other species
- **Versicolor and Virginica:** Show slight overlap but remain distinguishable

## Visualizations Created

1. **Pairplot:** Showing relationships between all features colored by species
2. **Box Plots:** Distribution of each feature across species
3. **Correlation Heatmap:** Feature relationships
4. **Confusion Matrices:** Model prediction accuracy visualization
5. **Feature Importance Charts:** For tree-based models

## Key Insights

1. **Petal measurements** are more informative than sepal measurements for classification
2. **Setosa species** has distinct characteristics making it easily identifiable
3. All four models perform well, indicating the dataset's clear structure
4. **Ensemble methods** (Random Forest) provide slight improvements over single models

## Technical Skills Demonstrated

- Data loading and preprocessing
- Exploratory Data Analysis (EDA)
- Feature scaling and normalization
- Train-test splitting with stratification
- Multiple classification algorithms
- Model evaluation and comparison
- Data visualization with matplotlib and seaborn
- Feature importance interpretation
- Confusion matrix analysis

## Real-World Applications

- **Botanical Research:** Automated species identification
- **Agriculture:** Plant classification systems
- **Education:** Teaching machine learning classification
- **Conservation:** Species monitoring and tracking
- **Horticulture:** Plant identification for gardening

## Project Deliverables

- Complete Jupyter notebook with analysis
- Trained classification models
- Comprehensive visualizations
- Feature importance analysis
- Professional documentation
- Model comparison results

## Technical Stack

- **Language:** Python 3.14
- **Libraries:**
  - pandas - Data manipulation
  - numpy - Numerical operations
  - matplotlib - Visualization
  - seaborn - Statistical visualization
  - scikit-learn - Machine learning models and utilities

## Code Repository

GitHub: https://github.com/Remaaa17/OIBSIP-DataScience-Task1-IrisClassification

## Conclusions

This project successfully demonstrates multi-class classification using the classic iris dataset. The high accuracy across all models confirms that the iris species can be reliably identified from physical measurements. The analysis provides valuable insights into feature importance and model selection for classification tasks.

The project serves as a strong foundation for understanding supervised learning, model evaluation, and the complete machine learning workflow from data loading to model deployment.

---

**Project Duration:** 1 week  
**Difficulty Level:** Beginner-Intermediate  
**Learning Focus:** Classification, Model Comparison, Feature Analysis
