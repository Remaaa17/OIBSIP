# Jupyter Kernel Setup - Unemployment Analysis

## Your Custom Kernel is Ready!

**Kernel Name:** unemployment_analysis  
**Display Name:** "Unemployment Analysis (Task2)"  
**Status:** Active and installed

## How to Use the Kernel

### Option 1: Quick Start (Recommended)
Double-click `START_JUPYTER.bat` or `run_notebook.bat`

The notebook will open with your custom kernel automatically.

### Option 2: Manual Start
```powershell
# Activate environment
venv\Scripts\Activate.ps1

# Start Jupyter
jupyter notebook unemployment_analysis.ipynb
```

### Option 3: Select Kernel Manually in Jupyter
1. Open Jupyter Notebook
2. Open `unemployment_analysis.ipynb`
3. Click "Kernel" menu → "Change Kernel"
4. Select "Unemployment Analysis (Task2)"

## Kernel Features

Your kernel includes all required packages:
- pandas 3.1.0
- numpy 2.5.4
- matplotlib 3.11.2
- seaborn 0.13.2
- jupyter 1.1.1
- notebook 7.6.4

## Visual Confirmation

When the kernel is running, you'll see in Jupyter:
- Top-right corner: "Unemployment Analysis (Task2)"
- Or: "Python 3 (ipykernel)" if using default kernel

## Kernel Location

The kernel is installed at:
```
C:\Users\Cairo Lap\AppData\Roaming\jupyter\kernels\unemployment_analysis
```

## Troubleshooting

### Kernel Not Showing
If you don't see the custom kernel:
1. Restart Jupyter server
2. Clear browser cache
3. Verify kernel: `jupyter kernelspec list`

### Kernel Dies on Startup
1. Activate venv: `venv\Scripts\Activate.ps1`
2. Reinstall ipykernel: `pip install --force-reinstall ipykernel`
3. Recreate kernel:
   ```powershell
   python -m ipykernel install --user --name=unemployment_analysis --display-name="Unemployment Analysis (Task2)"
   ```

### Wrong Kernel Selected
In Jupyter:
1. Kernel → Change Kernel
2. Select "Unemployment Analysis (Task2)"

## Running the Analysis

Once Jupyter opens:
1. Verify kernel name in top-right corner
2. Click "Cell" → "Run All"
3. Watch the analysis execute
4. Review visualizations and insights

## All Available Kernels

Your system has these kernels:
1. `python3` - Default Python kernel
2. `unemployment_analysis` - Your custom kernel (Recommended)

## Package Management

To add more packages to your kernel:
```powershell
# Activate environment
venv\Scripts\Activate.ps1

# Install package
pip install package_name

# Restart Jupyter to use new packages
```

## Quick Commands

**List kernels:**
```powershell
jupyter kernelspec list
```

**Start Jupyter:**
```powershell
jupyter notebook unemployment_analysis.ipynb
```

**Remove kernel (if needed):**
```powershell
jupyter kernelspec remove unemployment_analysis
```

## Status Check

Run this to verify everything:
```powershell
venv\Scripts\Activate.ps1
jupyter kernelspec list
pip list | Select-String -Pattern "pandas|matplotlib|seaborn"
```

You should see:
- unemployment_analysis kernel listed
- All packages installed

## Success!

Your custom kernel is configured and ready to run your unemployment analysis!

**Next Step:** Double-click `START_JUPYTER.bat` to begin!

---

**Author:** Eng. Reem Osama  
**Task:** Task 2 - Unemployment Analysis  
**Organization:** Oasis Infobyte
