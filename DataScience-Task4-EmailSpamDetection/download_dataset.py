"""
Download SMS Spam Collection Dataset
Dataset: UCI SMS Spam Collection from Kaggle
"""

import kagglehub

# Download latest version
path = kagglehub.dataset_download("uciml/sms-spam-collection-dataset")

print("Path to dataset files:", path)
print("\nDataset downloaded successfully!")
print("Copy the spam.csv file to this folder to use in the notebook.")
