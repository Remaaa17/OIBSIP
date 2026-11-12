#!/usr/bin/env python3
"""
Remove AI-style markers and emojis from all project files
"""

import os
import re
import json

# Define emoji and AI-style patterns to remove
emoji_pattern = re.compile(
    "["
    "\U0001F300-\U0001F9FF"  # Emot icons, symbols & pictographs
    "\U00002702-\U000027B0"
    "\U000024C2-\U0001F251"
    "\u2713"  # Check mark
    "\u2714"  # Heavy check mark
    "\u2705"  # White heavy check mark
    "\u2611"  # Ballot box with check
    "\u274C"  # Cross mark
    "\u26A0"  # Warning sign
    "\u2757"  # Exclamation mark
    "\u2755"  # White exclamation mark
    "]+", flags=re.UNICODE
)

# AI-style phrases to clean up
ai_phrases = {
    "✓ All libraries imported successfully!": "All libraries imported.",
    "✓": "",
    "successfully!": ".",
    " successfully": "",
    "✓ Dataset loaded successfully!": "Dataset loaded.",
    "✓ Linear Regression trained successfully!": "Linear Regression model trained.",
    "✓ Random Forest trained successfully!": "Random Forest model trained.",
    "✓ Decision Tree trained successfully!": "Decision Tree model trained.",
    "✓ K-Nearest Neighbors trained successfully!": "K-Nearest Neighbors model trained.",
    "Multinomial Naive Bayes trained successfully!": "Multinomial Naive Bayes model trained.",
    "Logistic Regression trained successfully!": "Logistic Regression model trained.",
    "SVM trained successfully!": "SVM model trained.",
    "✓ Random Forest Regressor trained successfully!": "Random Forest Regressor trained.",
}

def clean_text(text):
    """Remove emojis and AI-style phrases from text"""
    # Remove emojis
    text = emoji_pattern.sub('', text)
    
    # Replace AI-style phrases
    for old, new in ai_phrases.items():
        text = text.replace(old, new)
    
    return text

def clean_notebook(filepath):
    """Clean Jupyter notebook file"""
    print(f"Cleaning notebook: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Clean markdown and code cells
    for cell in notebook.get('cells', []):
        if 'source' in cell:
            if isinstance(cell['source'], list):
                cell['source'] = [clean_text(line) for line in cell['source']]
            elif isinstance(cell['source'], str):
                cell['source'] = clean_text(cell['source'])
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print(f"  ✓ Cleaned: {filepath}")

def clean_markdown(filepath):
    """Clean markdown file"""
    print(f"Cleaning markdown: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cleaned = clean_text(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(cleaned)
    
    print(f"  ✓ Cleaned: {filepath}")

def main():
    """Main cleanup function"""
    base_dir = "."
    
    # Find all notebooks
    for root, dirs, files in os.walk(base_dir):
        # Skip hidden and venv directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['venv', '__pycache__']]
        
        for file in files:
            filepath = os.path.join(root, file)
            
            if file.endswith('.ipynb'):
                try:
                    clean_notebook(filepath)
                except Exception as e:
                    print(f"  ✗ Error cleaning {filepath}: {e}")
            
            elif file.endswith('.md'):
                try:
                    clean_markdown(filepath)
                except Exception as e:
                    print(f"  ✗ Error cleaning {filepath}: {e}")
    
    print("\n✓ Cleanup complete!")

if __name__ == "__main__":
    main()
