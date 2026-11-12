"""
Download Advertising Dataset
Dataset: Advertising spend vs Sales
"""

import kagglehub

# Download latest version
path = kagglehub.dataset_download("ashydv/advertising-dataset")

print("Path to dataset files:", path)
print("\nDataset downloaded successfully!")
print("Copy the Advertising.csv file to this folder.")
