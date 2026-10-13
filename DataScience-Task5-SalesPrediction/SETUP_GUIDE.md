# 🚀 Setup Guide - Sales Prediction Project

## Step 1: Install Required Packages

Open your terminal/command prompt in this folder and run:

```bash
pip install -r requirements.txt
```

Or install packages individually:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter notebook
```

## Step 2: Download the Dataset

### Option A: Download from Kaggle (Recommended)

1. Go to [Kaggle](https://www.kaggle.com/)
2. Create a free account if you don't have one
3. Search for "Advertising.csv" or "Advertising dataset"
4. Download the dataset
5. Place the `Advertising.csv` file in this folder:
   ```
   DataScience-Task5-SalesPrediction/
   ├── Advertising.csv  ← Place here
   ├── sales_prediction.ipynb
   └── README.md
   ```

### Option B: Use Direct Link

You can also find the dataset at:
- GitHub repositories with sample datasets
- Search "advertising.csv dataset" on Google

### Expected Dataset Format

The CSV should have these columns:
- `TV` - TV advertising budget (in thousands)
- `Radio` - Radio advertising budget (in thousands)
- `Newspaper` - Newspaper advertising budget (in thousands)
- `Sales` - Product sales (in thousands of units)

## Step 3: Launch Jupyter Notebook

In this folder, run:

```bash
jupyter notebook
```

This will open Jupyter in your browser.

## Step 4: Open and Run the Notebook

1. Click on `sales_prediction.ipynb` to open it
2. Run cells sequentially from top to bottom
3. Use `Shift + Enter` to run each cell

## Step 5: Customize the Notebook

Before running, make sure to:
- [ ] Add your name in the first markdown cell
- [ ] Verify the dataset path in cell that loads the CSV
- [ ] Review and understand each code cell before running

## 🎥 Step 6: Record Your Demo Video

After completing the analysis:

1. **Prepare Title Card**:
   - Your Full Name
   - Track: Data Science
   - Task: Task 5 - Sales Prediction Using Python

2. **Record Demo**:
   - Start with 2-second title card
   - Show the notebook running
   - Walk through key visualizations
   - Explain model results
   - Show final insights

3. **Tools for Recording**:
   - OBS Studio (Free)
   - Windows Game Bar (Win + G)
   - Loom (Online)
   - Zoom (Record screen)

## 📤 Step 7: GitHub Upload

```bash
# Navigate to OIBSIP folder
cd "C:\Users\Cairo Lap\OneDrive\Desktop\OIBSI _internship of Data Science\-OIBSIP-"

# Add files
git add DataScience-Task5-SalesPrediction/

# Commit
git commit -m "Add Task 5: Sales Prediction Using Python"

# Push to GitHub
git push origin main
```

## 📱 Step 8: LinkedIn Post

Post template:

```
🎉 Completed Task 5 of my Data Science Internship at Oasis Infobyte! 

📊 Project: Sales Prediction Using Python
Built machine learning models to predict product sales based on advertising spend across TV, Radio, and Newspaper channels.

🔍 Key Highlights:
✅ Performed comprehensive EDA with visualizations
✅ Trained Linear Regression and Random Forest models
✅ Achieved R² score of [X.XX]
✅ Identified TV advertising as the most impactful channel

💻 Tech Stack: Python | Pandas | Scikit-learn | Matplotlib | Seaborn

[Link to demo video]
[Link to GitHub repo]

#oasisinfobyte #datascience #machinelearning #python #internship

@Oasis Infobyte
```

## 🆘 Troubleshooting

### Issue: Package installation fails
**Solution**: Try upgrading pip first
```bash
python -m pip install --upgrade pip
```

### Issue: Jupyter doesn't start
**Solution**: Try
```bash
python -m notebook
```

### Issue: Dataset not found
**Solution**: Make sure `Advertising.csv` is in the same folder as the notebook

### Issue: Import errors
**Solution**: Verify all packages are installed
```bash
pip list
```

## ✅ Checklist Before Submission

- [ ] All cells run without errors
- [ ] Your name is added to the notebook
- [ ] All visualizations are displaying correctly
- [ ] Model evaluation metrics are calculated
- [ ] Key insights are documented
- [ ] README.md is updated with your name
- [ ] Demo video recorded (2-sec title card + walkthrough)
- [ ] Code pushed to GitHub (OIBSIP repo)
- [ ] LinkedIn post created with #oasisinfobyte

---

**Need Help?** Check the task card requirements or reach out to fellow interns!

Good luck! 🚀
