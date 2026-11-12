"""
Dataset Download Script
Downloads unemployment dataset from Kaggle using kagglehub
"""

import os
import shutil

try:
    import kagglehub
    print("kagglehub is already installed")
except ImportError:
    print("Installing kagglehub...")
    import subprocess
    subprocess.check_call(['pip', 'install', 'kagglehub'])
    import kagglehub
    print("kagglehub installed successfully")

print("\n" + "="*60)
print("Downloading Unemployment in India Dataset")
print("="*60 + "\n")

# Download latest version
print("Downloading dataset from Kaggle...")
path = kagglehub.dataset_download("gokulrajkmv/unemployment-in-india")

print(f"\nDataset downloaded to: {path}")
print("\n" + "="*60)

# List files in the downloaded path
print("Files in dataset:")
print("="*60)
for file in os.listdir(path):
    print(f"  - {file}")
    file_path = os.path.join(path, file)
    file_size = os.path.getsize(file_path) / 1024  # Size in KB
    print(f"    Size: {file_size:.2f} KB")

print("\n" + "="*60)
print("Copying dataset to project folder...")
print("="*60 + "\n")

# Copy CSV file to current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]

if csv_files:
    for csv_file in csv_files:
        source = os.path.join(path, csv_file)
        destination = os.path.join(current_dir, 'Unemployment_in_India.csv')
        
        shutil.copy2(source, destination)
        print(f"Copied: {csv_file}")
        print(f"To: {destination}")
        
        # Display first few rows
        print("\n" + "="*60)
        print("Dataset Preview (First 5 rows):")
        print("="*60 + "\n")
        
        import pandas as pd
        df = pd.read_csv(destination)
        print(df.head())
        
        print("\n" + "="*60)
        print("Dataset Info:")
        print("="*60)
        print(f"Rows: {len(df)}")
        print(f"Columns: {len(df.columns)}")
        print(f"\nColumn names:")
        for col in df.columns:
            print(f"  - {col}")
        
        print("\n" + "="*60)
        print("SUCCESS! Dataset is ready to use.")
        print("="*60)
        print(f"\nYou can now run: jupyter notebook unemployment_analysis.ipynb")
        print(f"Dataset location: {destination}")
else:
    print("ERROR: No CSV file found in the downloaded dataset")
    print(f"Available files: {os.listdir(path)}")

print("\n" + "="*60)
