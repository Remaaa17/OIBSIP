# Unemployment Analysis with Python

## Project Overview
Exploratory data analysis on unemployment data to uncover regional and temporal trends, focusing on COVID-19's impact on unemployment rates in India.

## Objective
Analyze unemployment trends across regions and time periods with a special focus on comparing pre-COVID and post-COVID periods to understand the pandemic's economic impact.

## Features
- Data loading, cleaning, and preprocessing
- Region-wise unemployment rate analysis
- Monthly and yearly trend analysis
- Time-series visualizations for multiple states
- Top 10 states with highest unemployment (bar chart)
- Correlation heatmap between employment metrics
- Pre-COVID vs Post-COVID comparison
- Distribution analysis and statistical insights
- Professional visualizations with detailed observations

## Tech Stack
- **Python 3.8+**
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **matplotlib** - Data visualization
- **seaborn** - Statistical data visualization
- **Jupyter Notebook** - Interactive development environment
- **kagglehub** - Dataset management

## Dataset
**Source:** [Kaggle - Unemployment in India](https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india)  
**Time Period:** May 2019 - June 2020  
**Format:** CSV

**Columns:**
- Region/State
- Date
- Estimated Unemployment Rate (%)
- Estimated Employed
- Estimated Labour Participation Rate (%)
- Area (Urban/Rural)

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd DataScience-Task2-UnemploymentAnalysis
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Download Dataset

**Option 1: Using kagglehub (Recommended)**
```python
python download_dataset.py
```

**Option 2: Manual Download**
1. Visit [Kaggle Dataset](https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india)
2. Download the CSV file
3. Place it in the project folder as `Unemployment_in_India.csv`

## Usage

### Quick Start (Windows)
```bash
setup_environment.bat
run_notebook.bat
```

### Manual Start
```bash
# Activate environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Start Jupyter Notebook
jupyter notebook unemployment_analysis.ipynb
```

### Running the Analysis
1. Open `unemployment_analysis.ipynb` in Jupyter
2. Run all cells: `Cell > Run All`
3. Review generated visualizations and insights

## Project Structure
```
DataScience-Task2-UnemploymentAnalysis/
 unemployment_analysis.ipynb    # Main analysis notebook
 Unemployment_in_India.csv      # Dataset (download required)
 requirements.txt               # Python dependencies
 download_dataset.py            # Dataset download script
 setup_environment.bat          # Setup script (Windows)
 run_notebook.bat              # Launch script (Windows)
 README.md                     # Project documentation
 .gitignore                    # Git ignore rules
 venv/                         # Virtual environment (not in repo)
```

## Key Insights

The analysis reveals:
- **COVID-19 Impact:** Sharp increase in unemployment rates (from ~7% to 23%) during lockdown (April-May 2020)
- **Regional Disparities:** Significant variation in unemployment across Indian states
- **Recovery Patterns:** Different recovery trajectories for urban vs rural areas
- **Seasonal Trends:** Monthly patterns in employment across the year
- **Correlation Insights:** Strong inverse relationship between unemployment and employment rates

## Visualizations

The notebook includes:
1. Top 10 states bar chart
2. Time-series plots for multiple states
3. Monthly unemployment patterns
4. Correlation heatmap
5. Pre-COVID vs Post-COVID comparison charts
6. Timeline with COVID-19 impact marker
7. Distribution histograms and box plots

## Results

All analysis results, visualizations, and detailed observations are documented within the Jupyter notebook with professional commentary explaining each finding.

## Requirements

See `requirements.txt` for complete list. Main dependencies:
- pandas >= 1.3.0
- numpy >= 1.21.0
- matplotlib >= 3.4.0
- seaborn >= 0.11.0
- jupyter >= 1.0.0
- notebook >= 6.4.0
- kagglehub >= 0.1.0

## Author

**Eng. Reem Osama**  
Data Science Track  
Oasis Infobyte Internship - Task 2

## License

This project is part of the Oasis Infobyte Data Science Internship program.

## Acknowledgments

- Dataset source: [Kaggle - gokulrajkmv](https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india)
- Organization: Oasis Infobyte

---

**Keywords**: Data Science, Data Analysis, Python, Unemployment Analysis, COVID-19 Impact, Economic Research
