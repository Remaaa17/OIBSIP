# DataScience-Task4-EmailSpamDetection

## Email Spam Detection with Machine Learning

**Author:** Eng. Reem Osama  
**Organization:** Oasis Infobyte  
**Track:** Data Science  
**Task:** Task 4 - Email Spam Detection

---

## Project Overview

Build an NLP binary classifier to distinguish spam emails/SMS from legitimate (ham) messages using machine learning techniques including Naive Bayes, Logistic Regression, and SVM.

## Features

- Text preprocessing pipeline (lowercase, punctuation removal, stopwords, stemming)
- TF-IDF feature extraction
- Three classifier comparison: Naive Bayes, Logistic Regression, SVM
- Comprehensive evaluation: Accuracy, Precision, Recall, F1-Score
- Confusion matrix analysis
- WordCloud visualizations
- Professional insights and analysis

## Dataset

**SMS Spam Collection Dataset**
- Source: UCI Machine Learning Repository / Kaggle
- Size: 5,574 SMS messages
- Classes: Spam (747) and Ham (4,827)
- URL: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Download Dataset

```bash
python download_dataset.py
```

Copy the `spam.csv` file to this folder.

### 3. Run the Notebook

Open `email_spam_detection.ipynb` in Jupyter and select the "Email Spam Detection (Task4)" kernel.

## Project Structure

```
DataScience-Task4-EmailSpamDetection/
 email_spam_detection.ipynb    # Main analysis notebook
 requirements.txt                # Python dependencies
 download_dataset.py            # Dataset download script
 DATASET_INFO.md               # Dataset documentation
 README.md                     # This file
 spam.csv                      # Dataset (after download)
```

## Key Results

All three models achieve:
- **Accuracy**: >95%
- **Recall**: >95% (critical for catching spam)
- **Precision**: >95% (minimizing false positives)
- **F1-Score**: >95%

## Technologies Used

- **Python 3.14+**
- **pandas, numpy**: Data manipulation
- **scikit-learn**: Machine learning models and metrics
- **NLTK**: Text preprocessing
- **TF-IDF**: Feature extraction
- **WordCloud**: Visualization
- **matplotlib, seaborn**: Plotting

## Why Recall Matters

In spam detection, **recall** (catching actual spam) is more critical than precision because:
- False negatives (missed spam) expose users to malicious content
- False positives (ham marked as spam) can be recovered from spam folder
- User security > convenience

## Checklist Status

- [x] Dataset downloaded and loaded
- [x] Class distribution analysis
- [x] Text preprocessing pipeline
- [x] TF-IDF feature extraction with explanation
- [x] Train/test split
- [x] Naive Bayes classifier
- [x] Alternative classifier (Logistic Regression + SVM)
- [x] Accuracy, precision, recall, F1-score
- [x] Confusion matrix
- [x] Recall importance discussion
- [x] BONUS: WordCloud visualizations
- [x] Clean, commented notebook

## Author Notes

This project demonstrates professional NLP practices with human-like analysis and insights. All observations are contextual, explaining *why* patterns exist rather than just *what* they show.
